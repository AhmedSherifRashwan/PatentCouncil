"""PatentCouncil tools: the IP Filing Ecosystem's deterministic checks, callable by Paperclip agents.

Run with the IPFE environment so the checks are the runner's own code, not a copy:

    uv run --project ~/IP-Filing-Ecosystem python ~/PatentCouncil/tools/patent_tools.py <command> ...

Commands
  contract  --kind KIND --reply FILE [--write-envelope FILE]
                                              validate a reply against its output contract; optionally
                                              save the validated json envelope (review replies need it)
  merge-findings --review-dir DIR             merge both reviewers' envelopes into DIR/findings.json
                                              (dedupe + consensus, the runner's own aggregate)
  findings-report --findings FILE --title T --out FILE
                                              readable findings report from a findings.json
  terms     --locked FILE --reply FILE --kind KIND
                                              check a reply's Deliverable against the terminology lock
  support   --description FILE --claims FILE [--out DIR]
                                              deterministic claim-support check (advisory)
  export    --source FILE --out DIR [--title T]
                                              render markdown to Word and PDF

KIND is the prompt's `kind:` frontmatter: analysis, drafting, compose, revise, formal-fix, review or prose.
Every command prints one JSON object. Exit code 0 = passed, 1 = check failed, 2 = could not run.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from ecosystem import contracts, export, support_check, terminology


def _read(path: str) -> str:
    return Path(path).expanduser().read_text(encoding="utf-8")


def cmd_contract(args: argparse.Namespace) -> int:
    try:
        parsed = contracts.parse_reply(_read(args.reply), args.kind)
    except contracts.ContractError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}))
        return 1
    env = parsed.envelope.model_dump(mode="json") if parsed.envelope is not None else None
    if args.write_envelope and env is not None:
        Path(args.write_envelope).expanduser().write_text(json.dumps(env, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "repairs": parsed.warnings, "sections": sorted(parsed.sections),
                      "envelope_written": bool(args.write_envelope and env is not None),
                      "envelope": env}, default=str))
    return 0


def _counts(findings: list) -> dict:
    out: dict[str, dict[str, int]] = {}
    for f in findings:
        out.setdefault(f.category, {}).setdefault(f.severity, 0)
        out[f.category][f.severity] += 1
    return out


def cmd_merge(args: argparse.Namespace) -> int:
    from ecosystem import loopback

    findings = loopback.aggregate(Path(args.review_dir).expanduser(), write=True)
    print(json.dumps({"ok": True, "findings": len(findings),
                      "consensus": sum(1 for f in findings if getattr(f, "consensus", False)),
                      "by_category": _counts(findings),
                      "written": str(Path(args.review_dir).expanduser() / "findings.json")}))
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    from ecosystem import report

    raw = json.loads(_read(args.findings))
    items = raw.get("findings", raw) if isinstance(raw, dict) else raw
    findings = [contracts.Finding.model_validate(item) for item in items]
    order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    findings.sort(key=lambda f: (order.get(f.severity, 9), f.category, f.id))
    lines = [f"# {args.title}", "", *report._counts_table(findings), ""]
    for severity in ("critical", "high"):
        chosen = [f for f in findings if f.severity == severity]
        lines += [f"## {severity.capitalize()} findings ({len(chosen)})", ""]
        for f in chosen:
            lines += report._finding_section(f) + [""]
    rest = [f for f in findings if f.severity in ("medium", "low")]
    lines += [f"## Medium and low findings ({len(rest)})", "",
              "| Id | Severity | Area | Title | Claims | Specification |", "|---|---|---|---|---|---|"]
    lines += [f"| {f.id} | {f.severity} | {f.category} | {f.title} | {', '.join(f.claim_refs)} | "
              f"{', '.join(f.spec_refs)} |" for f in rest]
    Path(args.out).expanduser().write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "findings": len(findings), "written": args.out}))
    return 0


def cmd_terms(args: argparse.Namespace) -> int:
    locked_text = _read(args.locked)
    table = terminology.parse_locked(locked_text)
    parsed = contracts.parse_reply(_read(args.reply), args.kind)
    envelope = parsed.envelope if isinstance(parsed.envelope, contracts.DraftingEnvelope) else None
    report = terminology.check_output(parsed.deliverable or parsed.body_md, envelope, table, args.kind)
    print(json.dumps({"ok": not report.blocked, "locked_terms": len(table),
                      "violations": [v.model_dump() for v in report.violations],
                      "drift": [d.model_dump() for d in report.drift],
                      "warnings": [w.model_dump() for w in report.warnings]}, default=str))
    return 1 if report.blocked else 0


def cmd_support(args: argparse.Namespace) -> int:
    report = support_check.check_support(_read(args.description), _read(args.claims))
    out = {}
    if args.out:
        json_path, md_path = support_check.write_support_check(report, Path(args.out).expanduser())
        out = {"json": str(json_path), "markdown": str(md_path)}
    print(json.dumps({"ok": report.ok, "unsupported_count": report.unsupported_count,
                      "paragraphs": report.paragraphs, "written": out,
                      "method": report.method}, default=str))
    return 0 if report.ok else 1


def cmd_export(args: argparse.Namespace) -> int:
    written = export.export_markdown(Path(args.source).expanduser(), Path(args.out).expanduser(), args.title)
    print(json.dumps({"ok": bool(written), "written": [str(p) for p in written]}))
    return 0 if written else 1


def main() -> int:
    parser = argparse.ArgumentParser(prog="patent_tools", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("contract"); c.add_argument("--kind", required=True); c.add_argument("--reply", required=True)
    c.add_argument("--write-envelope")
    m = sub.add_parser("merge-findings"); m.add_argument("--review-dir", required=True)
    r = sub.add_parser("findings-report"); r.add_argument("--findings", required=True)
    r.add_argument("--title", required=True); r.add_argument("--out", required=True)
    t = sub.add_parser("terms"); t.add_argument("--locked", required=True); t.add_argument("--reply", required=True)
    t.add_argument("--kind", required=True)
    s = sub.add_parser("support"); s.add_argument("--description", required=True); s.add_argument("--claims", required=True)
    s.add_argument("--out")
    e = sub.add_parser("export"); e.add_argument("--source", required=True); e.add_argument("--out", required=True)
    e.add_argument("--title", default="")
    args = parser.parse_args()
    handler = {"contract": cmd_contract, "terms": cmd_terms, "support": cmd_support, "export": cmd_export,
               "merge-findings": cmd_merge, "findings-report": cmd_report}[args.cmd]
    try:
        return handler(args)
    except Exception as exc:  # the caller must never mistake a crash for a pass
        print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}))
        return 2


if __name__ == "__main__":
    sys.exit(main())
