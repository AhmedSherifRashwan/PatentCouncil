"""The scheduler: runs the task graph with as much parallelism as the dependencies allow.

One agent turn = one `openclaw agent` call with the task's inputs embedded in the prompt. The agent writes its
outputs to the exact paths the prompt names; the runner then verifies them, runs the company's deterministic
checks, and spends at most one correction turn (in the same session, so the agent keeps its context) on
anything that failed. Runner steps (gates, stitching, merging, routing, packaging) run in-process.

A usage limit pauses the whole run until the limit resets, then carries on by itself. Every state change is
written to `council-state.json`, so `council run` on a stopped or crashed run resumes where it left off.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import subprocess
import sys
import threading
import time
from concurrent.futures import FIRST_COMPLETED, Future, ThreadPoolExecutor, wait
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

from council.paths import LESSONS, PROMPTS, TOOLS, Run

OPENCLAW = os.environ.get("OPENCLAW_BIN", str(Path.home() / ".openclaw" / "bin" / "openclaw"))
MAX_EMBED_FILE = 160_000   # characters; larger inputs are given by path
MAX_EMBED_TOTAL = 420_000  # characters per prompt, across all embedded inputs
AGENT_CAPS = {"pc-invention-analyst": 6, "pc-prior-art-analyst": 3, "pc-specification-drafter": 6,
              "pc-claims-architect": 4, "pc-examiner": 5, "pc-litigator": 5, "pc-adjudicator": 6}
# The terminology lock is enforced (with a correction turn) only on text that becomes the application. On
# analysis outputs it is advisory: they quote prior art and competitors in their own vocabulary.
TERMS_ENFORCED = {"x-p4-compose-description", "x-p4-revise", "x-p5-revise", "25", "39a"}
AGENT_NAMES = {"pc-invention-analyst": "Invention Analyst", "pc-prior-art-analyst": "Prior-Art Analyst",
               "pc-specification-drafter": "Specification Drafter", "pc-claims-architect": "Claims Architect",
               "pc-examiner": "Examiner", "pc-litigator": "Litigator", "pc-adjudicator": "Adjudicator"}


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


# -- task model ------------------------------------------------------------------------------------------


@dataclass
class PromptRef:
    pid: str
    reply: str                        # path relative to the run folder
    relax: tuple[str, ...] = ()       # inputs moved from required to optional (parallel siblings)


@dataclass
class Task:
    key: str
    title: str
    agent: str | None = None          # OpenClaw agent id; None = a runner step
    deps: list[str] = field(default_factory=list)
    what: str = ""
    prompts: list[PromptRef] = field(default_factory=list)
    embed: list[Any] = field(default_factory=list)   # extra files (run-relative str or Path) embedded in full
    refer: list[Any] = field(default_factory=list)   # files or folders named by path only
    outputs: list[str] = field(default_factory=list)  # run-relative files the agent must write
    model: str | None = None
    thinking: str | None = None
    budget: int = 10                  # target minutes
    stage: str = ""
    run: Callable[["Ctx"], dict] | None = None        # runner step body
    post: Callable[["Ctx"], dict] | None = None       # after an agent task's outputs pass
    checks: Callable[["Ctx"], list[tuple[str, str]]] | None = None  # extra checks -> [(file, problem)]
    expand: Callable[["Ctx"], list["Task"]] | None = None  # new tasks once this one is done
    optional: bool = False            # a failure does not stop the run
    review: bool = False              # replies are review-contract: write envelopes


class RateLimited(RuntimeError):
    def __init__(self, message: str, resume_at: dt.datetime | None):
        super().__init__(message)
        self.resume_at = resume_at


class Transient(RuntimeError):
    pass


LIMIT_SIGNS = ("hit your", "spend limit", "session limit", "usage limit", "rate limit", "rate_limit",
               "too many requests", "429", "quota", "credit balance", "overloaded")
TRANSIENT_SIGNS = ("timeout", "timed out", "econnrefused", "connection", "unavailable", "503", "502",
                   "in_flight", "already running", "another runner", "wait for it to finish", "was terminated",
                   "produced no output", "auth refresh")


def parse_reset(message: str) -> dt.datetime | None:
    """'resets 3:40pm (Europe/London)' -> the next such local time."""
    m = re.search(r"resets?\s+(?:at\s+)?(\d{1,2})(?::(\d{2}))?\s*([ap]m)?", message, re.I)
    if not m:
        return None
    h, mi = int(m.group(1)), int(m.group(2) or 0)
    if m.group(3):
        h = h % 12 + (12 if m.group(3).lower() == "pm" else 0)
    t = dt.datetime.now().replace(hour=h % 24, minute=mi, second=0, microsecond=0)
    return t if t > dt.datetime.now() else t + dt.timedelta(days=1)


# -- context -----------------------------------------------------------------------------------------------


class Ctx:
    def __init__(self, run: Run, settings: dict, engine: "Engine"):
        self.run, self.settings, self.engine = run, settings, engine
        self.R = run.r

    @property
    def full(self) -> bool:
        return self.settings.get("profile", "full") == "full"

    def pc(self, *args: str, allow_fail: bool = True) -> dict:
        """Run a company tool (`pc <command>`) with this interpreter; returns its JSON, always with `ok`.
        A broken tool (exit 2) raises; a failed check returns ok=False unless `allow_fail` is False."""
        cmd = [sys.executable, str(TOOLS / "patent_tools.py"), *args]
        proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(TOOLS.parent))
        try:
            out = json.loads(proc.stdout[proc.stdout.find("{"):]) if "{" in proc.stdout else {}
        except json.JSONDecodeError:
            out = {"ok": False, "error": proc.stdout[-500:]}
        if "ok" not in out:
            out["ok"] = proc.returncode == 0
        if proc.returncode == 2 or (not out["ok"] and not allow_fail):
            raise RuntimeError(f"pc {args[0]} failed: {json.dumps(out)[:600] or proc.stderr[-400:]}")
        return out

    def mark(self, stage: str, event: str, note: str = "") -> None:
        self.pc("mark", "--matter", str(self.run.m), "--stage", stage, "--event", event, "--note", note, allow_fail=True)

    def say(self, line: str, urgent: bool = False) -> None:
        self.engine.notifier.push(line, urgent)


# -- prompt assembly ------------------------------------------------------------------------------------------


def prompt_meta(pid: str) -> dict:
    path = next(PROMPTS.glob(f"{pid}-*.md"), None) if (pid[0].isdigit() or pid == "gate14") else PROMPTS / f"{pid}.md"
    if path is None or not path.exists():
        raise FileNotFoundError(f"prompt {pid} not found in {PROMPTS}")
    text = path.read_text(encoding="utf-8")
    _, fm, body = text.split("---", 2)

    def field_(key):
        m = re.search(rf"^{key}:\s*(.*)$", fm, re.M)
        return m.group(1).strip().strip('"') if m else ""

    def listed(key):
        return [x.strip() for x in field_(key).strip("[]").split(",") if x.strip()]

    return {"id": pid, "path": path, "kind": field_("kind"), "title": field_("title"), "body": body.strip(),
            "inputs": listed("inputs"), "optional": listed("optional_inputs"),
            "sections": [s.strip().strip('"') for s in field_("deliverable_sections").strip("[]").split('",') if s.strip()]}


def contract_kind(kind: str) -> str:
    return "review" if kind == "review" else "drafting"


def build_prompt(ctx: Ctx, task: Task) -> tuple[str, list[str]]:
    run, R = ctx.run, ctx.R
    name = AGENT_NAMES.get(task.agent or "", task.agent)
    lines = [f"# Patent Council · matter `{run.slug}` · run `{run.run}` · step `{task.key}` · profile {ctx.settings.get('profile')}",
             "", f"You are the **{name}**. Follow your AGENTS.md. This message is the whole brief: what to do, the prompts "
             "to execute, every input (embedded below, so do not re-read those files), and the exact files to write.", "",
             "## What to do", "", task.what.strip(), "",
             f"**Time budget:** about {task.budget} minutes. The whole matter is planned to finish end to end in two hours. "
             "Be complete, but write each deliverable once: no drafts, no repetition, no padding.", ""]
    embed: list[Path] = []
    refer: list[Path] = []
    kinds = set()
    for pr in task.prompts:
        meta = prompt_meta(pr.pid)
        kinds.add(contract_kind(meta["kind"]))
        required = [s for s in meta["inputs"] if s not in pr.relax]
        optional = meta["optional"] + [s for s in meta["inputs"] if s in pr.relax]
        for spec in required + optional:
            e, r = run.resolve(spec)
            embed += [p for p in e if p not in embed]
            refer += [p for p in r if p not in refer]
        lines += [f"## Prompt {meta['id']} — {meta['title']}  (kind `{meta['kind']}`)", "",
                  f"**Write your reply to:** `{R / pr.reply}`", "", meta["body"], ""]
    for item in task.embed:
        p = item if isinstance(item, Path) else R / item
        if p.is_dir():
            embed += [q for q in sorted(p.glob("*.md")) if q not in embed]
        elif p not in embed:
            embed.append(p)
    for item in task.refer:
        p = item if isinstance(item, Path) else R / item
        if p not in refer:
            refer.append(p)
    if not task.review and task.agent in ("pc-specification-drafter", "pc-claims-architect", "pc-prior-art-analyst"):
        embed.append(LESSONS)  # the recurring failures every drafter and the risk report must avoid
    for k in sorted(kinds):
        frag = PROMPTS / f"_contract-{k}.md"
        if frag.exists():
            lines += [f"## Output contract ({k})", "", frag.read_text(encoding="utf-8").strip(), ""]
    # Inputs, embedded in full up to the budget; the rest by path.
    total, shown, by_path = 0, [], []
    for p in embed:
        if not p.exists() or not p.is_file():
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        if len(text) > MAX_EMBED_FILE or total + len(text) > MAX_EMBED_TOTAL:
            by_path.append(p)
            continue
        total += len(text)
        shown.append((p, text))
    missing = [str(p) for p in embed if not p.exists()]
    if shown:
        lines += ["## Inputs (embedded)", ""]
        for p, text in shown:
            fence = "````" if "```" in text else "```"
            lines += [f"### `{p}`", "", f"{fence}{'json' if p.suffix == '.json' else 'markdown'}", text.rstrip(), fence, ""]
    extra = by_path + [p for p in refer if p.exists()]
    if extra:
        lines += ["## Files you may read (not embedded: open only what you need)", "",
                  *[f"- `{p}`{'/' if p.is_dir() else ''}" for p in extra], ""]
    if missing:
        lines += ["## Inputs that do not exist yet (work without them; do not wait)", "", *[f"- `{m}`" for m in missing], ""]
    outs = [R / pr.reply for pr in task.prompts] + [R / o for o in task.outputs]
    lines += ["## Files to write", "", f"Write each of these with your Write tool, at exactly this path, one file per call "
              "(the folders exist). Write nothing outside the run folder `{R}`. Do not run the checks yourself: the runner runs them and "
              "will tell you if anything fails.", "", *[f"- `{o}`" for o in outs], "",
              "When every file is written, reply with one line per file (path and a few words on what it holds) and "
              "anything the runner must route: open questions, disclosure requests, open disagreements, narrowing suggested. "
              "Nothing else."]
    return "\n".join(lines) + "\n", [str(o) for o in outs]


# -- transport -------------------------------------------------------------------------------------------------


def call_agent(agent: str, session: str, prompt_file: Path, timeout_s: int, model: str | None,
               thinking: str | None) -> dict:
    argv = [OPENCLAW, "agent", "--agent", agent, "--session-key", session, "--message-file", str(prompt_file),
            "--json", "--timeout", str(timeout_s)]
    if model:
        argv += ["--model", model if "/" in model else f"anthropic/{model}"]
    if thinking:
        argv += ["--thinking", thinking]
    started = time.monotonic()
    try:
        proc = subprocess.run(argv, capture_output=True, text=True, timeout=timeout_s + 90)
    except subprocess.TimeoutExpired as exc:
        raise Transient(f"openclaw agent exceeded {timeout_s + 90}s") from exc
    out = proc.stdout or ""
    payload = None
    if "{" in out:
        try:
            payload = json.loads(out[out.find("{"):])
        except json.JSONDecodeError:
            payload = None
    if payload is None:
        err = (proc.stderr or out)[-800:]
        _raise_classified(err or "no output")
    if payload.get("ok") is False or (payload.get("status") and payload.get("status") != "ok"):
        err = ((payload.get("error") or {}).get("message") or payload.get("summary") or json.dumps(payload)[:600])
        _raise_classified(str(err))
    result = payload.get("result") or {}
    text = "\n".join(p.get("text", "") for p in result.get("payloads") or [] if isinstance(p, dict))
    meta = result.get("meta") or {}
    return {"text": text, "model": (meta.get("systemPromptReport") or {}).get("model"),
            "seconds": round(time.monotonic() - started), "run_id": payload.get("runId")}


def _raise_classified(message: str) -> None:
    low = message.lower()
    if any(s in low for s in LIMIT_SIGNS):
        raise RateLimited(message, parse_reset(message))
    if any(s in low for s in TRANSIENT_SIGNS):
        raise Transient(message)
    raise RuntimeError(message)


# -- notifier ---------------------------------------------------------------------------------------------------


class Notifier:
    """Writes every line to progress.md at once; relays batches into the front door's chat session."""

    MARKER = "[Patent Council update]"
    RELAY = ("Progress from the Patent Council runner, newest last. Post these lines to the person exactly as they are, "
             "as a compact list, with no preamble or commentary and no tool calls to re-check them. Exception: a line "
             "starting QUESTIONS, DELIVERED, PAUSED or FAILED: follow the patent-council skill for it in the same reply "
             "(read the file it names; give the questions, the result, the reason or the verbatim error).")

    def __init__(self, run: Run, session: str | None, interval_s: int = 600):
        self.run, self.session, self.interval = run, session, interval_s
        self.pending: list[str] = []
        self.last = time.monotonic()
        self.lock = threading.Lock()

    def push(self, line: str, urgent: bool = False) -> None:
        stamp = dt.datetime.now().strftime("%H:%M")
        with (self.run.r / "progress.md").open("a", encoding="utf-8") as fh:
            fh.write(f"{dt.datetime.now():%Y-%m-%d %H:%M:%S}  {line}\n")
        print(f"{stamp}  {line}", flush=True)
        with self.lock:
            self.pending.append(f"{stamp} {line}")
        self.flush(force=urgent)

    def flush(self, force: bool = False) -> None:
        if not self.session:
            self.pending.clear()
            return
        with self.lock:
            if not self.pending or (not force and time.monotonic() - self.last < self.interval):
                return
            lines, self.pending = self.pending, []
            self.last = time.monotonic()
        msg = "\n".join([f"{self.MARKER} {self.run.slug}", *lines, "", f"({self.RELAY})"])
        log = (self.run.r / "notify.log").open("ab")
        try:
            subprocess.Popen([OPENCLAW, "agent", "--session-key", self.session, "--message", msg, "--json",
                              "--timeout", "300"], stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT,
                             start_new_session=True)
        finally:
            log.close()


# -- engine -------------------------------------------------------------------------------------------------------


class Engine:
    def __init__(self, run: Run, settings: dict, build: Callable[[Ctx], list[Task]], fake: Callable | None = None):
        self.run, self.settings = run, settings
        self.state_path = run.r / "council-state.json"
        self.state = json.loads(self.state_path.read_text()) if self.state_path.exists() else {"tasks": {}}
        self.state.setdefault("tasks", {})
        self.state["settings"] = {**self.state.get("settings", {}), **settings}
        self.settings = self.state["settings"]
        self.notifier = Notifier(run, self.settings.get("notify"), int(self.settings.get("notify_interval", 600)))
        self.ctx = Ctx(run, self.settings, self)
        self.fake = fake
        self.tasks: dict[str, Task] = {}
        self.lock = threading.RLock()
        for t in build(self.ctx):
            self.add(t)
        self._expand_done()
        self.pause_until: dt.datetime | None = None
        self.stop_file = run.r / "STOP"

    # state
    def st(self, key: str) -> dict:
        return self.state["tasks"].setdefault(key, {"status": "pending"})

    def save(self) -> None:
        with self.lock:
            tmp = self.state_path.with_suffix(".tmp")
            tmp.write_text(json.dumps(self.state, indent=1))
            tmp.replace(self.state_path)

    def add(self, task: Task) -> None:
        with self.lock:
            if task.key not in self.tasks:
                self.tasks[task.key] = task
                self.st(task.key)

    def _expand_done(self) -> None:
        changed = True
        while changed:
            changed = False
            for key, task in list(self.tasks.items()):
                if task.expand and self.st(key)["status"] == "done" and not self.st(key).get("expanded_now"):
                    before = len(self.tasks)
                    for t in task.expand(self.ctx):
                        self.add(t)
                    self.st(key)["expanded_now"] = True
                    changed = changed or len(self.tasks) != before
        for key in self.tasks:
            self.st(key).pop("expanded_now", None)

    # scheduling
    def ready(self, running: set[str]) -> list[Task]:
        out = []
        for key, t in self.tasks.items():
            s = self.st(key)["status"]
            if s in ("done", "failed", "skipped", "held") or key in running:
                continue
            deps_ok = True
            for d in t.deps:
                if d not in self.tasks:
                    continue  # a dependency the profile does not have
                ds = self.st(d)["status"]
                if ds == "done" or (ds in ("failed", "skipped") and self.tasks[d].optional):
                    continue
                deps_ok = False
                break
            if deps_ok:
                out.append(t)
        return out

    def run_all(self, max_workers: int = 10) -> int:
        self.state.setdefault("started", now())
        self.state["status"] = "running"
        self.state["pid"] = os.getpid()
        self.save()
        self.ctx.say(f"RUN started · {len([k for k in self.tasks if self.st(k)['status'] != 'done'])} steps to go · "
                     f"profile {self.settings.get('profile')}", urgent=True)
        running: dict[Future, Task] = {}
        failed_hard = False
        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            while True:
                if self.stop_file.exists():
                    self.ctx.say("STOPPED on request; `council run` resumes.", urgent=True)
                    break
                paused = self.pause_until and dt.datetime.now() < self.pause_until
                if not paused and not failed_hard:
                    busy = {}
                    for t in running.values():
                        busy[t.agent] = busy.get(t.agent, 0) + 1
                    for t in self.ready({x.key for x in running.values()}):
                        if len(running) >= max_workers:
                            break
                        if t.agent and busy.get(t.agent, 0) >= AGENT_CAPS.get(t.agent, 4):
                            continue
                        busy[t.agent] = busy.get(t.agent, 0) + 1
                        s = self.st(t.key)
                        s.update(status="running", started=s.get("started") if s.get("status") == "running" else now())
                        s["attempts"] = s.get("attempts", 0) + 1
                        self.save()
                        running[pool.submit(self.execute, t)] = t
                if not running:
                    if paused:
                        time.sleep(30)
                        continue
                    break
                done, _ = wait(list(running), timeout=30, return_when=FIRST_COMPLETED)
                self.notifier.flush()
                for fut in done:
                    t = running.pop(fut)
                    s = self.st(t.key)
                    try:
                        info = fut.result() or {}
                        s.update(status="done", finished=now(), info=info)
                        s["minutes"] = round((dt.datetime.fromisoformat(s["finished"]) -
                                              dt.datetime.fromisoformat(s["started"])).total_seconds() / 60, 1)
                        warn = f" · {len(info.get('warnings', []))} check warning(s)" if info.get("warnings") else ""
                        self.ctx.say(f"done  {t.key} · {t.title} · {s['minutes']} min{warn}")
                        if t.expand:
                            for nt in t.expand(self.ctx):
                                self.add(nt)
                    except RateLimited as exc:
                        s.update(status="pending", started=None)
                        until = exc.resume_at or (dt.datetime.now() + dt.timedelta(minutes=20))
                        until = until + dt.timedelta(minutes=2)
                        if not self.pause_until or until > self.pause_until:
                            self.pause_until = until
                            self.state["paused_until"] = until.isoformat(timespec="minutes")
                            self.ctx.say(f"PAUSED: usage limit ({str(exc)[:160]}). Resuming by itself at "
                                         f"{until:%H:%M}.", urgent=True)
                    except Exception as exc:  # noqa: BLE001 - a step failure is reported, never swallowed
                        s.update(status="failed", finished=now(), error=f"{type(exc).__name__}: {exc}"[:2000])
                        self.ctx.say(f"FAILED {t.key} · {t.title}: {str(exc)[:300]}", urgent=True)
                        if not t.optional:
                            failed_hard = True
                    self.save()
                if self.pause_until and dt.datetime.now() >= self.pause_until:
                    self.pause_until = None
                    self.state.pop("paused_until", None)
                    self.ctx.say("RESUMED after the usage limit.", urgent=True)
        pending = [k for k in self.tasks if self.st(k)["status"] not in ("done", "skipped") and not
                   (self.st(k)["status"] == "failed" and self.tasks[k].optional)]
        self.state["status"] = "done" if not pending else ("failed" if failed_hard else "stopped")
        self.state["finished"] = now()
        self.save()
        self.notifier.flush(force=True)
        return 0 if not pending else 1

    # one task
    def execute(self, task: Task) -> dict:
        if self.fake and task.agent:
            info = self.fake(self.ctx, task)
            problems = self.check(task)
            if problems:
                info["warnings"] = [f"{Path(f).name}: {p[:300]}" for f, p in problems]
            if task.post:
                info["post"] = task.post(self.ctx)
            return info
        if task.run:
            if task.stage:
                self.ctx.mark(task.stage, "start")
            out = task.run(self.ctx) or {}
            if task.stage:
                self.ctx.mark(task.stage, "end")
            return out
        return self.agent_task(task)

    def agent_task(self, task: Task) -> dict:
        R = self.run.r
        calls = R / "calls" / task.key
        calls.mkdir(parents=True, exist_ok=True)
        for o in [pr.reply for pr in task.prompts] + task.outputs:
            (R / o).parent.mkdir(parents=True, exist_ok=True)
        prompt, outs = build_prompt(self.ctx, task)
        attempt = self.st(task.key).get("attempts", 1)
        pfile = calls / f"prompt-a{attempt}.md"
        pfile.write_text(prompt, encoding="utf-8")
        session = f"agent:{task.agent}:{self.run.slug}-{self.run.run}-{task.key}-a{attempt}".lower()
        session = re.sub(r"[^a-z0-9:-]+", "-", session)[:96]
        timeout = min(5400, max(900, task.budget * 60 * 4))
        started = time.time()
        # Leave stale outputs from an earlier attempt out of the verification.
        replies: list[dict] = []

        def turn(text_file: Path) -> dict:
            for n in range(3):
                try:
                    r = call_agent(task.agent, session, text_file, timeout, task.model, task.thinking)
                    replies.append(r)
                    (calls / f"reply-a{attempt}-{len(replies)}.md").write_text(r["text"], encoding="utf-8")
                    return r
                except Transient as exc:
                    if n == 2:
                        raise
                    time.sleep(10 * (n + 1))
            raise AssertionError

        turn(pfile)
        missing = [o for o in outs if not Path(o).exists() or Path(o).stat().st_mtime < started - 5
                   or Path(o).stat().st_size == 0]
        if missing:
            fix = calls / f"fix-missing-a{attempt}.md"
            fix.write_text("These files were not written (or are empty):\n" + "\n".join(f"- `{m}`" for m in missing) +
                           "\n\nWrite them now with the Write tool, at exactly these paths, complete. Then reply with one "
                           "line per file.\n", encoding="utf-8")
            turn(fix)
            missing = [o for o in missing if not Path(o).exists() or Path(o).stat().st_size == 0]
            if missing:
                raise RuntimeError(f"outputs still missing after a correction turn: {', '.join(missing)}")
        warnings = []
        problems = self.check(task)
        if problems:
            fix = calls / f"fix-checks-a{attempt}.md"
            fix.write_text("The runner's checks failed on your files:\n\n" +
                           "\n".join(f"- `{f}`: {p}" for f, p in problems) +
                           "\n\nFix each file in place with your Edit tool: targeted replacements only, do not re-type a whole "
                           "file unless its structure is broken. A term the lock flags is either replaced by the locked "
                           "preferred term or declared in the envelope's `new_terms` with a reason. Then reply with one "
                           "line per file.\n", encoding="utf-8")
            turn(fix)
            problems = self.check(task)
            warnings = [f"{Path(f).name}: {p[:300]}" for f, p in problems]
        info: dict = {"turns": len(replies), "agent_seconds": sum(r["seconds"] for r in replies),
                      "model": replies[0].get("model") if replies else None}
        if warnings:
            info["warnings"] = warnings
            (calls / "warnings.md").write_text("\n".join(warnings) + "\n", encoding="utf-8")
        if task.post:
            info["post"] = task.post(self.ctx)
        return info

    def check(self, task: Task) -> list[tuple[str, str]]:
        """Blocking problems (earn a correction turn); advisory ones are logged in `advisory.md`."""
        R, problems, advisory = self.run.r, [], []
        locked = R / "terminology" / "LOCKED.md"
        for pr in task.prompts:
            f = R / pr.reply
            kind = contract_kind(prompt_meta(pr.pid)["kind"])
            args = ["contract", "--kind", kind, "--reply", str(f)]
            if task.review:
                args += ["--write-envelope", str(f.with_suffix(".envelope.json"))]
            res = self.ctx.pc(*args, allow_fail=True)
            if not res.get("ok"):
                problems.append((str(f), f"output contract: {res.get('error', res)}"))
                continue
            if kind != "review" and locked.exists():
                res = self.ctx.pc("terms", "--locked", str(locked), "--reply", str(f), "--kind", kind, allow_fail=True)
                if not res.get("ok"):
                    bad = {k: v for k, v in res.items() if k not in ("ok",)}
                    text = f"terminology lock: {json.dumps(bad)[:900]}"
                    if pr.pid in TERMS_ENFORCED:
                        problems.append((str(f), text))
                    else:
                        advisory.append(f"{f.name}: {text[:300]}")
        if task.checks:
            problems += task.checks(self.ctx)
        if advisory:
            calls = R / "calls" / task.key
            calls.mkdir(parents=True, exist_ok=True)
            (calls / "advisory.md").write_text("\n".join(advisory) + "\n", encoding="utf-8")
        return problems
