"""council — run Patent Council matters on OpenClaw.

    council new-matter --slug S --title T [--jurisdictions US,EP,GB] [--profile full|quick] [--from-example]
    council intake     --slug S --kind disclosure|answers|prior-art|data [--name N] (--stdin | --file PATH)
    council run        --slug S [--run r1] [--profile full|quick] [--parts 5] [--workers 10]
                       [--notify <openclaw session key>] [--background] [--only K1,K2] [--simulate-from DIR]
    council status     --slug S [--run r1]
    council stop       --slug S [--run r1]
    council plan       --slug S [--run r1]         (the task graph as it stands, no calls)

A run resumes where it stopped: finished steps are kept, failed and unfinished ones run again.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

from council import flow
from council.engine import Engine
from council.paths import COUNCIL, Run

EXAMPLE = Path.home() / "IP-Filing-Ecosystem" / "tests" / "fixtures" / "example-matter" / "00-intake"


def out(obj: dict) -> None:
    print(json.dumps(obj, indent=1, default=str))


def cmd_new_matter(a) -> int:
    run = Run(a.slug)
    if (run.intake / "matter.json").exists():
        out({"ok": False, "error": f"matter {a.slug} already exists", "path": str(run.m)})
        return 1
    run.intake.mkdir(parents=True, exist_ok=True)
    for sub in ("prior-art", "data", "drawings", "priority"):
        (run.intake / sub).mkdir(exist_ok=True)
    meta = {"title": a.title, "jurisdictions": a.jurisdictions.split(","), "profile": a.profile, "mode": "unattended",
            "flow": "fast", "platform": "openclaw", "created": dt.datetime.now().isoformat(timespec="seconds"),
            "fictional_test": bool(a.from_example)}
    (run.intake / "matter.json").write_text(json.dumps(meta, indent=1))
    if a.from_example:  # the fictional test invention, with its data, drawings and supplied prior art
        shutil.copytree(EXAMPLE, run.intake, dirs_exist_ok=True)
    out({"ok": True, "matter": str(run.m), "disclosure": str(run.intake / "disclosure.md"),
         "next": "council intake --kind disclosure" if not a.from_example else "council run"})
    return 0


def cmd_intake(a) -> int:
    run = Run(a.slug)
    if not run.intake.exists():
        out({"ok": False, "error": f"no matter {a.slug}; run new-matter first"})
        return 1
    text = sys.stdin.read() if a.stdin else Path(a.file).expanduser().read_text(encoding="utf-8")
    target = {"disclosure": run.intake / "disclosure.md", "answers": run.intake / "answers.md"}.get(a.kind)
    if target is None:
        target = run.intake / a.kind / f"{a.name or 'item'}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    out({"ok": True, "written": str(target), "chars": len(text)})
    return 0


def _settings(a, run: Run) -> dict:
    meta = json.loads((run.intake / "matter.json").read_text()) if (run.intake / "matter.json").exists() else {}
    s = {"profile": a.profile or meta.get("profile", "full"), "parts": a.parts, "slug": run.slug, "run": run.run}
    if a.notify:
        s["notify"] = a.notify
    return s


def cmd_run(a) -> int:
    run = Run(a.slug, a.run)
    if not (run.intake / "disclosure.md").exists():
        out({"ok": False, "error": f"{run.intake / 'disclosure.md'} is missing"})
        return 1
    run.r.mkdir(parents=True, exist_ok=True)
    (run.r / "STOP").unlink(missing_ok=True)
    state_file = run.r / "council-state.json"
    if state_file.exists():
        pid = json.loads(state_file.read_text()).get("pid")
        if pid and _alive(pid) and pid != os.getpid() and json.loads(state_file.read_text()).get("status") == "running":
            out({"ok": False, "error": f"this run is already going (pid {pid})"})
            return 1
    if a.background:
        argv = [sys.executable, "-m", "council.cli", *[x for x in sys.argv[1:] if x != "--background"]]
        log = (run.r / "council.log").open("ab")
        proc = subprocess.Popen(argv, cwd=str(COUNCIL), stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT,
                                start_new_session=True, env={**os.environ, "PYTHONPATH": str(COUNCIL)})
        out({"ok": True, "background_pid": proc.pid, "log": str(run.r / "council.log"),
             "status": f"council status --slug {a.slug}"})
        return 0
    fake = None
    if a.simulate_from:
        from council.simulate import make_fake
        fake = make_fake(Path(a.simulate_from))
    engine = Engine(run, _settings(a, run), flow.build, fake=fake)
    if a.only:
        only = set(a.only.split(","))
        for key in engine.tasks:
            if key not in only and engine.st(key)["status"] != "done":
                engine.st(key)["status"] = "held"
        rc = engine.run_all(max_workers=a.workers)
        for key in engine.tasks:
            if engine.st(key)["status"] == "held":
                engine.st(key)["status"] = "pending"
        engine.state["status"] = "partial"
        engine.save()
        return rc if any(engine.st(k)["status"] == "failed" for k in only if k in engine.tasks) else 0
    return engine.run_all(max_workers=a.workers)


def _alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def cmd_status(a) -> int:
    run = Run(a.slug, a.run)
    sf = run.r / "council-state.json"
    if not sf.exists():
        out({"ok": True, "status": "not started", "matter": str(run.m)})
        return 0
    st = json.loads(sf.read_text())
    tasks = st.get("tasks", {})
    by: dict[str, list[str]] = {}
    for k, v in tasks.items():
        by.setdefault(v.get("status", "pending"), []).append(k)
    started = st.get("started")
    elapsed = None
    if started:
        end = dt.datetime.fromisoformat(st["finished"]) if st.get("finished") and st.get("status") != "running" else dt.datetime.now().astimezone()
        elapsed = round((end - dt.datetime.fromisoformat(started)).total_seconds() / 60)
    recent = (run.r / "progress.md").read_text().splitlines()[-12:] if (run.r / "progress.md").exists() else []
    alive = bool(st.get("pid")) and _alive(st["pid"]) and st.get("status") == "running"
    res = {"ok": True, "matter": a.slug, "run": a.run, "status": st.get("status") if alive or st.get("status") != "running"
           else "stopped (process gone: `council run` resumes)", "elapsed_min": elapsed,
           "done": len(by.get("done", [])), "total": len(tasks), "running": by.get("running", []),
           "failed": {k: tasks[k].get("error", "")[:300] for k in by.get("failed", [])},
           "paused_until": st.get("paused_until"), "recent": recent}
    delivery = run.r / "package" / "delivery.json"
    if delivery.exists():
        res["delivered"] = json.loads(delivery.read_text())
    out(res)
    return 0


def cmd_stop(a) -> int:
    run = Run(a.slug, a.run)
    (run.r / "STOP").write_text("stop requested\n")
    out({"ok": True, "note": "the runner stops launching new steps; steps already running finish. `council run` resumes."})
    return 0


def cmd_plan(a) -> int:
    run = Run(a.slug, a.run)
    a.profile = a.profile or None
    engine = Engine(run, _settings(a, run), flow.build)
    out({"tasks": [{"key": t.key, "agent": t.agent or "runner", "deps": t.deps, "model": t.model,
                    "budget": t.budget if t.agent else None, "status": engine.st(t.key)["status"]}
                   for t in engine.tasks.values()]})
    return 0


def main() -> int:
    p = argparse.ArgumentParser(prog="council", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("new-matter")
    n.add_argument("--slug", required=True); n.add_argument("--title", required=True)
    n.add_argument("--jurisdictions", default="US,EP,GB"); n.add_argument("--profile", choices=["full", "quick"], default="full")
    n.add_argument("--from-example", action="store_true")
    i = sub.add_parser("intake")
    i.add_argument("--slug", required=True); i.add_argument("--kind", required=True,
                                                            choices=["disclosure", "answers", "prior-art", "data", "priority"])
    i.add_argument("--name"); g = i.add_mutually_exclusive_group(required=True)
    g.add_argument("--stdin", action="store_true"); g.add_argument("--file")
    for name in ("run", "plan"):
        r = sub.add_parser(name)
        r.add_argument("--slug", required=True); r.add_argument("--run", default="r1")
        r.add_argument("--profile", choices=["full", "quick"]); r.add_argument("--parts", type=int, default=5)
        r.add_argument("--workers", type=int, default=10); r.add_argument("--notify")
        r.add_argument("--background", action="store_true"); r.add_argument("--only")
        r.add_argument("--simulate-from")
    for name in ("status", "stop"):
        s = sub.add_parser(name)
        s.add_argument("--slug", required=True); s.add_argument("--run", default="r1")
    a = p.parse_args()
    return {"new-matter": cmd_new_matter, "intake": cmd_intake, "run": cmd_run, "status": cmd_status, "stop": cmd_stop,
            "plan": cmd_plan}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
