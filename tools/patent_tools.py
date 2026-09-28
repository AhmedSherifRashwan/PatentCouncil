"""Patent Council tools: deterministic checks and bookkeeping for the Patent Council agents.

Run through the wrapper, which uses the IP Filing Ecosystem's environment so the checks are the
runner's own tested code, not a copy:

    ~/PatentCouncil/tools/pc <command> [options]

Output contracts and the terminology lock
  contract --kind KIND --reply FILE [--write-envelope FILE]
      Validate a reply against its output contract (kind = the prompt's `kind:`). Review replies
      need --write-envelope so their findings can be merged.
  terms --locked FILE --reply FILE --kind KIND
      Check a reply's Deliverable against the locked terminology. Violations fail.
  lock-terms --reply 04.md --out LOCKED.md
      Gate 1: write the locked terminology from Prompt 04's Terminology Table.
  strip --reply FILE --kind KIND --out FILE
      Deliverable + Assumptions + Open Questions only (no Rationale). What later steps and the
      reviewers read.

Drafting checks (all deterministic, all instant)
  registry --reply 20a.md --out registry.json        parse the reference-numeral registry
  numerals --registry registry.json --description F --claims F
                                                     numerals used but unregistered, etc.
  support --description F --claims F [--out DIR]     heuristic claim-support check
  support-map --description F --claims F --map support-map.json
                                                     the live support map: every claim element mapped
                                                     to paragraphs that exist and that use its words
  antecedent --claims F                              "the X" / "said X" with no earlier "a X"
  claims-format --claims F                           numbering, dependencies, forward references

Gates, review and loop-backs
  confirm --replies F [F ...] --out CONFIRMED.md [--by NAME]
                                                     Gate 2: the confirmed embodiment set
  review-package --description F --claims F --figures 20.md --registry-reply 20a.md
                 [--abstract F] --out DIR            rationale-stripped package for blind review
  merge-findings --review-dir DIR                    merge both reviewers into DIR/findings.json
  apply-rulings --findings F --rulings F --out F     attach the Adjudicator's rulings
  route --findings F --state loopback.json [--cap 2] [--commit]
                                                     owner-only loop-back plan for upheld findings
  findings-report --findings F --title T --out F     readable report (with rulings when present)

Run records
  mark --matter DIR --stage NAME --event start|end [--note TEXT]
  scorecard --matter DIR --run rN [--out FILE]
  export --source F --out DIR [--title T]            markdown to Word and PDF

Every command prints one JSON object. Exit 0 = passed, 1 = check failed, 2 = could not run.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

from ecosystem import contracts, export, numerals, support_check, terminology

SEVERE = ("critical", "high")
# Where each finding category is routed, in pipeline order (the playbook's loop-back table).
# Each step receives only the findings of the categories that name it.
ROUTES = {
    "novelty": ["x-loopback-p3", "x-p4-revise", "x-p5-revise"],
    "design-around": ["x-loopback-p3", "x-p4-revise", "x-p5-revise"],
    "enablement": ["x-p4-revise", "x-p5-revise"],  # P5 only when a claim is touched
    "support": ["x-p4-revise"],  # add disclosure, never narrow
    "formal": ["x-formal-fix"],  # corrected in place, never counts against a cap
}
STEP_ORDER = ["x-loopback-p3", "x-p4-revise", "x-p5-revise", "x-formal-fix"]
STEP_OWNER = {
    "x-loopback-p3": "Embodiment Architect",
    "x-p4-revise": "Specification Drafter",
    "x-p5-revise": "Claims Architect",
    "x-formal-fix": "Specification Drafter",
}
_WORD = re.compile(r"[a-z][a-z0-9-]{2,}")
_STOP = set(
    "the and for with from that this which wherein whereby said each one more least into onto "
    "upon than then when where such being been are was were has have having its their them "
    "configured adapted arranged operable least plurality first second third further comprising "
    "comprises comprise including includes include claim claims according any".split()
)


def _read(path: str) -> str:
    return Path(path).expanduser().read_text(encoding="utf-8")


def _write(path: str | Path, text: str) -> Path:
    target = Path(path).expanduser()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    return target


def _emit(payload: dict, ok: bool = True) -> int:
    payload.setdefault("ok", ok)
    print(json.dumps(payload, default=str))
    return 0 if payload["ok"] else 1


def _words(text: str) -> set[str]:
    return {w for w in _WORD.findall((text or "").lower()) if w not in _STOP}


def _deliverable(path: str, kind: str) -> str:
    parsed = contracts.parse_reply(_read(path), kind)
    return parsed.deliverable or parsed.body_md


# -- contracts and terminology ---------------------------------------------------------------


def cmd_contract(args: argparse.Namespace) -> int:
    try:
        parsed = contracts.parse_reply(_read(args.reply), args.kind)
    except contracts.ContractError as exc:
        return _emit({"error": str(exc)}, ok=False)
    env = parsed.envelope.model_dump(mode="json") if parsed.envelope is not None else None
    if args.write_envelope and env is not None:
        _write(args.write_envelope, json.dumps(env, indent=2) + "\n")
    return _emit({"repairs": parsed.warnings, "sections": sorted(parsed.sections),
                  "envelope_written": bool(args.write_envelope and env is not None), "envelope": env})


def cmd_terms(args: argparse.Namespace) -> int:
    table = terminology.parse_locked(_read(args.locked))
    parsed = contracts.parse_reply(_read(args.reply), args.kind)
    envelope = parsed.envelope if isinstance(parsed.envelope, contracts.DraftingEnvelope) else None
    report = terminology.check_output(parsed.deliverable or parsed.body_md, envelope, table, args.kind)
    return _emit({"locked_terms": len(table),
                  "violations": [v.model_dump() for v in report.violations],
                  "drift": [d.model_dump() for d in report.drift],
                  "warnings": [w.model_dump() for w in report.warnings]}, ok=not report.blocked)


def cmd_lock_terms(args: argparse.Namespace) -> int:
    deliverable = _deliverable(args.reply, "analysis")
    table = terminology.parse_locked(deliverable)
    if len(table) == 0:
        return _emit({"error": "no Terminology Table with a 'Preferred term' column found in Prompt 04"}, ok=False)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    _write(args.out, f"# Locked terminology\n\nLocked at Gate 1, {stamp}, from `{Path(args.reply).name}`. "
                     "Every later drafting output must use these preferred terms verbatim or declare a new "
                     f"term in `new_terms`.\n\n{deliverable.strip()}\n")
    return _emit({"locked_terms": len(table), "written": args.out})


def cmd_strip(args: argparse.Namespace) -> int:
    parsed = contracts.parse_reply(_read(args.reply), args.kind)
    parts = []
    for heading in ("Deliverable", "Findings", "Corrections", "Assumptions", "Open Questions"):
        if parsed.sections.get(heading, "").strip():
            parts.append(f"## {heading}\n\n{parsed.sections[heading].strip()}\n")
    if not parts:
        parts = [parsed.body_md]
    _write(args.out, "\n".join(parts))
    return _emit({"written": args.out, "sections": [p.split("\n")[0][3:] for p in parts]})


# -- drafting checks -------------------------------------------------------------------------


def cmd_registry(args: argparse.Namespace) -> int:
    registry = numerals.parse_registry(_deliverable(args.reply, "drafting"), source=args.reply)
    _write(args.out, registry.model_dump_json(indent=2) + "\n")
    return _emit({"entries": len(registry.entries), "written": args.out}, ok=len(registry.entries) > 0)


def cmd_numerals(args: argparse.Namespace) -> int:
    registry = numerals.Registry.model_validate_json(_read(args.registry))
    result = numerals.cross_check(registry, _read(args.description), _read(args.claims))
    data = result.model_dump()
    problems = sum(len(v) for v in data.values() if isinstance(v, list))
    return _emit({"problems": problems, **data}, ok=problems == 0)


def cmd_support(args: argparse.Namespace) -> int:
    report = support_check.check_support(_read(args.description), _read(args.claims))
    out = {}
    if args.out:
        json_path, md_path = support_check.write_support_check(report, Path(args.out).expanduser())
        out = {"json": str(json_path), "markdown": str(md_path)}
    return _emit({"unsupported_count": report.unsupported_count, "paragraphs": report.paragraphs,
                  "dependency_issues": [i.model_dump() for i in report.dependency_check.issues],
                  "written": out, "method": report.method}, ok=report.ok)


def cmd_support_map(args: argparse.Namespace) -> int:
    """Check the drafters' live support map against the actual text.

    support-map.json: {"claims": {"1": [{"element": "<claim words>", "paragraphs": ["[0012]"]}]}}
    Every claim needs entries; every limitation must be covered by a mapped element; every cited
    paragraph must exist and share key words with its element.
    """
    paragraphs = {p.id: p.text for p in support_check.parse_paragraphs(_read(args.description))}
    claims = support_check.parse_claims(_read(args.claims))
    data = json.loads(_read(args.map))
    mapped = {str(k): v for k, v in (data.get("claims") or {}).items()}
    unmapped_claims, uncovered, missing_paras, weak = [], [], [], []
    for claim in claims:
        entries = mapped.get(str(claim.number)) or []
        if not entries:
            unmapped_claims.append(claim.number)
            continue
        element_words = [_words(e.get("element", "")) for e in entries]
        for limitation in support_check.split_limitations(claim.text):
            lw = _words(limitation)
            if len(lw) < 2:
                continue
            best = max((len(lw & ew) / len(lw) for ew in element_words), default=0.0)
            if best < 0.5:
                uncovered.append({"claim": claim.number, "limitation": limitation[:160]})
        for entry in entries:
            ew = _words(entry.get("element", ""))
            cited = entry.get("paragraphs") or []
            if not cited:
                missing_paras.append({"claim": claim.number, "element": entry.get("element", "")[:120],
                                      "problem": "no paragraph cited"})
            for pid in cited:
                if pid not in paragraphs:
                    missing_paras.append({"claim": claim.number, "paragraph": pid, "problem": "paragraph not found"})
                elif ew and len(ew & _words(paragraphs[pid])) / len(ew) < 0.3:
                    weak.append({"claim": claim.number, "paragraph": pid, "element": entry.get("element", "")[:120]})
    ok = not (unmapped_claims or uncovered or missing_paras)
    return _emit({"claims": len(claims), "paragraphs": len(paragraphs), "unmapped_claims": unmapped_claims,
                  "uncovered_limitations": uncovered, "bad_citations": missing_paras,
                  "weak_citations": weak}, ok=ok)


_INTRO = r"(?:a|an|one|at least one|one or more|a plurality of|plurality of|two|two or more|each|another)"
# Definite phrases that are claim idiom, not references back to an element.
_IDIOMS = {"group consisting", "same", "following", "other", "extent", "case", "art", "invention",
           "method", "system", "apparatus", "device", "claim", "claims", "present"}
_STOP |= set("towards toward between through within without across over under against along about after "
             "before during among around beyond via using based".split())


def _chain(claim, by_number) -> list:
    seen, order, stack = set(), [], [claim]
    while stack:
        c = stack.pop()
        if c.number in seen:
            continue
        seen.add(c.number)
        order.append(c)
        stack.extend(by_number[d] for d in c.depends_on if d in by_number)
    return order


def cmd_antecedent(args: argparse.Namespace) -> int:
    """Heuristic antecedent-basis check. Advisory: a human confirms each flag."""
    claims = support_check.parse_claims(_read(args.claims))
    by_number = {c.number: c for c in claims}
    flags = []
    for claim in claims:
        prior_text = " ".join(c.text for c in _chain(claim, by_number) if c.number != claim.number).lower()
        own = claim.text.lower()
        # Lookahead, so one match never swallows the next article ("the spring biases the seat").
        for match in re.finditer(r"\b(the|said)\s+(?=((?:[a-z][a-z-]*\s+){0,2}[a-z][a-z-]*))", own):
            words = []
            for w in match.group(2).split():
                if w in ("the", "said", "a", "an", "of", "by", "to", "in", "on", "at", "is", "as"):
                    break
                words.append(w)
            if not words or " ".join(words[:2]) in _IDIOMS or words[0] in _IDIOMS:
                continue
            before = own[: match.start()] + " " + prior_text
            # The noun phrase may end at any of its first three words ("the token carries" ends at
            # "token"). Flag only when no candidate head was introduced earlier, so a following verb
            # can never be mistaken for the noun.
            heads = [w for w in words if w not in _STOP and len(w) >= 4]
            if not heads:
                continue
            introduced = any(
                re.search(rf"\b{_INTRO}\s+(?:[a-z-]+\s+){{0,3}}{re.escape(h)}s?\b", before)
                or (match.group(1) == "the" and re.search(rf"\b{re.escape(h)}s?\b", before))
                for h in heads
            )
            if introduced:
                continue
            flags.append({"claim": claim.number, "phrase": f"{match.group(1)} {' '.join(words)}"})
    unique = {(f["claim"], f["phrase"]): f for f in flags}
    return _emit({"claims": len(claims), "flags": list(unique.values()),
                  "method": "heuristic: a definite article with no earlier indefinite introduction in "
                            "the claim or the claims it depends on"}, ok=not unique)


def cmd_claims_format(args: argparse.Namespace) -> int:
    claims = support_check.parse_claims(_read(args.claims))
    numbers = [c.number for c in claims]
    problems = []
    if numbers != list(range(1, len(numbers) + 1)):
        problems.append({"problem": "claims are not numbered 1..n consecutively", "numbers": numbers})
    for c in claims:
        for d in c.depends_on:
            if d >= c.number:
                problems.append({"claim": c.number, "problem": f"depends on claim {d}, which is not earlier"})
            if d not in numbers:
                problems.append({"claim": c.number, "problem": f"depends on claim {d}, which does not exist"})
    independents = [c.number for c in claims if c.independent]
    return _emit({"claims": len(claims), "independent": independents, "problems": problems}, ok=not problems)


# -- gates and review ------------------------------------------------------------------------


def cmd_confirm(args: argparse.Namespace) -> int:
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    parts = [f"# Confirmed embodiments\n\nConfirmed at Gate 2 by **{args.by}**, {stamp}. Only what is below "
             "goes into the specification. Candidate status is lifted by this gate and by nothing else.\n"]
    for reply in args.replies:
        kind = "drafting"
        parts.append(f"\n---\n\n## From `{Path(reply).name}`\n\n{_deliverable(reply, kind).strip()}\n")
    _write(args.out, "\n".join(parts))
    return _emit({"sources": len(args.replies), "written": args.out})


def cmd_review_package(args: argparse.Namespace) -> int:
    out = Path(args.out).expanduser()
    out.mkdir(parents=True, exist_ok=True)
    (out / "description.md").write_text(_read(args.description), encoding="utf-8")
    (out / "claims.md").write_text(_read(args.claims), encoding="utf-8")
    (out / "figures.md").write_text(_deliverable(args.figures, "drafting"), encoding="utf-8")
    (out / "registry.md").write_text(_deliverable(args.registry_reply, "drafting"), encoding="utf-8")
    written = ["description.md", "claims.md", "figures.md", "registry.md"]
    if args.abstract:
        (out / "abstract.md").write_text(_read(args.abstract), encoding="utf-8")
        written.append("abstract.md")
    (out / "README.md").write_text(
        "# Review package\n\nFinished text only: description, claims, figure descriptions and the numeral "
        "registry. No drafting rationale, no earlier phases, no pre-drafting risk report, no discussion. "
        "Review it as an examiner or opponent would receive it.\n", encoding="utf-8")
    return _emit({"written": [str(out / w) for w in written]})


def cmd_merge(args: argparse.Namespace) -> int:
    from ecosystem import loopback

    findings = loopback.aggregate(Path(args.review_dir).expanduser(), write=True)
    counts: dict[str, dict[str, int]] = {}
    for f in findings:
        counts.setdefault(f.category, {}).setdefault(f.severity, 0)
        counts[f.category][f.severity] += 1
    return _emit({"findings": len(findings), "consensus": sum(1 for f in findings if getattr(f, "consensus", False)),
                  "by_category": counts, "written": str(Path(args.review_dir).expanduser() / "findings.json")})


def _load_findings(path: str) -> tuple[dict, list[dict]]:
    raw = json.loads(_read(path))
    items = raw.get("findings", raw) if isinstance(raw, dict) else raw
    return (raw if isinstance(raw, dict) else {"findings": items}), items


def cmd_apply_rulings(args: argparse.Namespace) -> int:
    raw, items = _load_findings(args.findings)
    rulings_raw = json.loads(_read(args.rulings))
    rulings = {r["id"]: r for r in (rulings_raw.get("rulings", rulings_raw) if isinstance(rulings_raw, dict) else rulings_raw)}
    missing = []
    for item in items:
        r = rulings.get(item["id"])
        if r:
            item["ruling"] = r.get("ruling")
            item["ruling_reason"] = r.get("reason")
            if r.get("severity") and r.get("severity") != item.get("severity"):
                item["severity_original"] = item.get("severity")
                item["severity"] = r["severity"]
        elif item.get("severity") in SEVERE:
            missing.append(item["id"])
    raw["findings"] = items
    _write(args.out, json.dumps(raw, indent=2) + "\n")
    tally: dict[str, int] = {}
    for item in items:
        tally[item.get("ruling") or "unruled"] = tally.get(item.get("ruling") or "unruled", 0) + 1
    return _emit({"rulings": tally, "severe_without_ruling": missing, "written": args.out}, ok=not missing)


def _routable(item: dict) -> bool:
    if item.get("severity") not in SEVERE:
        return False
    ruling = item.get("ruling")
    if ruling == "upheld":
        return True
    if ruling == "unclear":
        return item.get("severity") == "critical"  # a possible claim-killer is never waved through
    return False


def cmd_route(args: argparse.Namespace) -> int:
    _, items = _load_findings(args.findings)
    state_path = Path(args.state).expanduser()
    state = json.loads(state_path.read_text()) if state_path.exists() else {"cycles": {}, "formal_passes": 0}
    by_cat: dict[str, list[dict]] = {}
    for item in items:
        if _routable(item):
            by_cat.setdefault(item["category"], []).append(item)
    step_findings: dict[str, list[str]] = {}
    routed, capped = [], {}
    for category, found in by_cat.items():
        cap = args.formal_cap if category == "formal" else args.cap
        used = state["formal_passes"] if category == "formal" else state["cycles"].get(category, 0)
        if used >= cap:
            capped[category] = [f["id"] for f in found]
            continue
        routed.append(category)
        for step in ROUTES[category]:
            chosen = found
            if category == "enablement" and step == "x-p5-revise":
                chosen = [f for f in found if f.get("claim_refs") or f.get("suggested_target") == "P5"]
            if chosen:
                step_findings.setdefault(step, []).extend(f["id"] for f in chosen)
    steps = [s for s in STEP_ORDER if s in step_findings]
    narrowing = [f"{f['id']}: {f.get('least_narrowing_action', '')}" for f in by_cat.get("support", [])
                 if "narrow" in (f.get("least_narrowing_action", "") + f.get("attack", "")).lower()]
    plan = {"routed_categories": routed, "steps": [{"step": s, "owner": STEP_OWNER[s], "finding_ids": step_findings[s]}
                                                   for s in steps],
            "capped": capped, "review_required": bool(capped), "narrowing_for_human": narrowing,
            "cycles_before": dict(state["cycles"]), "formal_passes_before": state["formal_passes"]}
    if args.commit:
        for category in routed:
            if category == "formal":
                state["formal_passes"] += 1
            else:
                state["cycles"][category] = state["cycles"].get(category, 0) + 1
        state.setdefault("history", []).append({"at": dt.datetime.now(dt.timezone.utc).isoformat(), **plan})
        _write(state_path, json.dumps(state, indent=2) + "\n")
    return _emit(plan)


def cmd_report(args: argparse.Namespace) -> int:
    from ecosystem import report

    _, items = _load_findings(args.findings)
    order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    items.sort(key=lambda f: (order.get(f.get("severity"), 9), f.get("category", ""), f.get("id", "")))
    model_fields = set(contracts.Finding.model_fields)
    findings = [contracts.Finding.model_validate({k: v for k, v in i.items() if k in model_fields}) for i in items]
    rulings = [i.get("ruling") for i in items]
    lines = [f"# {args.title}", "", *report._counts_table(findings), ""]
    if any(rulings):
        tally: dict[str, int] = {}
        for r in rulings:
            tally[r or "not adjudicated"] = tally.get(r or "not adjudicated", 0) + 1
        lines += ["**Adjudication.** Every critical and high finding was checked against the text by the "
                  "Adjudicator after the owning drafter's rebuttal: " +
                  ", ".join(f"{k} {v}" for k, v in sorted(tally.items())) + ". Only upheld findings (and "
                  "unclear critical ones) were sent back for revision; every finding is reported.", ""]
    for severity in ("critical", "high"):
        chosen = [(f, i) for f, i in zip(findings, items) if f.severity == severity]
        lines += [f"## {severity.capitalize()} findings ({len(chosen)})", ""]
        for f, i in chosen:
            lines += report._finding_section(f)
            if i.get("ruling"):
                lines += ["", f"**Ruling** {i['ruling']} — {i.get('ruling_reason') or ''}"]
            lines.append("")
    rest = [i for i in items if i.get("severity") in ("medium", "low")]
    lines += [f"## Medium and low findings ({len(rest)})", "",
              "| Id | Severity | Area | Title | Claims | Ruling |", "|---|---|---|---|---|---|"]
    lines += [f"| {i['id']} | {i['severity']} | {i['category']} | {i['title']} | {', '.join(i.get('claim_refs') or [])} | "
              f"{i.get('ruling') or '—'} |" for i in rest]
    _write(args.out, "\n".join(lines) + "\n")
    return _emit({"findings": len(items), "written": args.out})


# -- run records -----------------------------------------------------------------------------


def cmd_mark(args: argparse.Namespace) -> int:
    line = {"at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "stage": args.stage,
            "event": args.event, "note": args.note}
    target = Path(args.matter).expanduser() / "timeline.jsonl"
    with target.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(line) + "\n")
    return _emit({"recorded": line})


def cmd_scorecard(args: argparse.Namespace) -> int:
    matter = Path(args.matter).expanduser()
    run = matter / "runs" / args.run
    events = [json.loads(l) for l in (matter / "timeline.jsonl").read_text().splitlines() if l.strip()] \
        if (matter / "timeline.jsonl").exists() else []
    starts: dict[str, str] = {}
    stages = []
    for e in events:
        if e["event"] == "start":
            starts[e["stage"]] = e["at"]
        elif e["event"] == "end" and e["stage"] in starts:
            a, b = dt.datetime.fromisoformat(starts[e["stage"]]), dt.datetime.fromisoformat(e["at"])
            stages.append({"stage": e["stage"], "minutes": round((b - a).total_seconds() / 60, 1)})
    total = None
    if events:
        total = round((dt.datetime.fromisoformat(events[-1]["at"]) - dt.datetime.fromisoformat(events[0]["at"]))
                      .total_seconds() / 3600, 2)
    rounds = []
    for fj in sorted(run.glob("review/r*/findings.adjudicated.json")) or sorted(run.glob("review/r*/findings.json")):
        _, items = _load_findings(str(fj))
        sev: dict[str, int] = {}
        rul: dict[str, int] = {}
        for i in items:
            sev[i["severity"]] = sev.get(i["severity"], 0) + 1
            rul[i.get("ruling") or "unruled"] = rul.get(i.get("ruling") or "unruled", 0) + 1
        rounds.append({"round": fj.parent.name, "findings": len(items), "by_severity": sev, "rulings": rul,
                       "consensus": sum(1 for i in items if i.get("consensus"))})
    answers = matter / "intake" / "answers.md"
    card = {"matter": matter.name, "run": args.run, "wall_hours": total, "stages": stages, "review_rounds": rounds,
            "inventor_answers_received": answers.exists() and answers.stat().st_size > 50}
    md = [f"# Scorecard — {matter.name} / {args.run}", "", f"**Wall-clock:** {total} h", "",
          "| Stage | Minutes |", "|---|---|", *[f"| {s['stage']} | {s['minutes']} |" for s in stages], "",
          "| Review round | Findings | Critical | High | Upheld | Rejected | Unclear | Consensus |",
          "|---|---|---|---|---|---|---|---|"]
    md += [f"| {r['round']} | {r['findings']} | {r['by_severity'].get('critical', 0)} | {r['by_severity'].get('high', 0)} | "
           f"{r['rulings'].get('upheld', 0)} | {r['rulings'].get('rejected', 0)} | {r['rulings'].get('unclear', 0)} | "
           f"{r['consensus']} |" for r in rounds]
    out = Path(args.out).expanduser() if args.out else run / "scorecard.md"
    _write(out, "\n".join(md) + "\n")
    _write(out.with_suffix(".json"), json.dumps(card, indent=2) + "\n")
    return _emit({**card, "written": str(out)})


def cmd_export(args: argparse.Namespace) -> int:
    written = export.export_markdown(Path(args.source).expanduser(), Path(args.out).expanduser(), args.title)
    return _emit({"written": [str(p) for p in written]}, ok=len(written) == 2)


def main() -> int:
    parser = argparse.ArgumentParser(prog="pc", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    def add(name, *specs):
        p = sub.add_parser(name)
        for spec in specs:
            flag, _, extra = spec.partition(":")
            if extra == "req":
                p.add_argument(flag, required=True)
            elif extra == "many":
                p.add_argument(flag, nargs="+", required=True)
            elif extra == "flag":
                p.add_argument(flag, action="store_true")
            elif extra.startswith("int="):
                p.add_argument(flag, type=int, default=int(extra[4:]))
            elif extra.startswith("default="):
                p.add_argument(flag, default=extra[8:])
            else:
                p.add_argument(flag)
        return p

    add("contract", "--kind:req", "--reply:req", "--write-envelope")
    add("terms", "--locked:req", "--reply:req", "--kind:req")
    add("lock-terms", "--reply:req", "--out:req")
    add("strip", "--reply:req", "--kind:req", "--out:req")
    add("registry", "--reply:req", "--out:req")
    add("numerals", "--registry:req", "--description:req", "--claims:req")
    add("support", "--description:req", "--claims:req", "--out")
    add("support-map", "--description:req", "--claims:req", "--map:req")
    add("antecedent", "--claims:req")
    add("claims-format", "--claims:req")
    add("confirm", "--replies:many", "--out:req", "--by:default=Orchestrator (auto-unattended)")
    add("review-package", "--description:req", "--claims:req", "--figures:req", "--registry-reply:req", "--abstract",
        "--out:req")
    add("merge-findings", "--review-dir:req")
    add("apply-rulings", "--findings:req", "--rulings:req", "--out:req")
    add("route", "--findings:req", "--state:req", "--cap:int=2", "--formal-cap:int=2", "--commit:flag")
    add("findings-report", "--findings:req", "--title:req", "--out:req")
    add("mark", "--matter:req", "--stage:req", "--event:req", "--note")
    add("scorecard", "--matter:req", "--run:req", "--out")
    add("export", "--source:req", "--out:req", "--title:default=")
    args = parser.parse_args()
    handlers = {
        "contract": cmd_contract, "terms": cmd_terms, "lock-terms": cmd_lock_terms, "strip": cmd_strip,
        "registry": cmd_registry, "numerals": cmd_numerals, "support": cmd_support, "support-map": cmd_support_map,
        "antecedent": cmd_antecedent, "claims-format": cmd_claims_format, "confirm": cmd_confirm,
        "review-package": cmd_review_package, "merge-findings": cmd_merge, "apply-rulings": cmd_apply_rulings,
        "route": cmd_route, "findings-report": cmd_report, "mark": cmd_mark, "scorecard": cmd_scorecard,
        "export": cmd_export,
    }
    try:
        return handlers[args.cmd](args)
    except Exception as exc:  # a crash must never read as a pass
        print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}))
        return 2


if __name__ == "__main__":
    sys.exit(main())
