"""Paragraph-level edits to a numbered description, so a fix pass never re-types a 30,000-word text.

The fix pass replies with edit blocks inside its `### Description` deliverable section:

    @@ REPLACE [0042]
    <the new text of paragraph 0042; several paragraphs allowed>
    @@ AFTER [0042]
    <one or more new paragraphs or #### headings, inserted after 0042>
    @@ DELETE [0042]

Inserted paragraphs are numbered `[0042a]`, `[0042b]`, so every paragraph reference in the review, the rulings
and the assessment stays valid while the matter is open. `renumber` makes the numbering continuous for the
filed text and returns the old-to-new map, which `remap_refs` applies to anything that cites paragraphs.
"""

from __future__ import annotations

import re

PARA_RE = re.compile(r"^\[(\d{3,5})([a-z]*)\]\s*")
EDIT_RE = re.compile(r"^@@\s*(REPLACE|AFTER|DELETE)\s*\[(\d{3,5}[a-z]*)\]\s*$", re.M | re.I)
UNNUMBERED = ("#", "|", "- ", "* ", "```", ">")


def blocks(text: str) -> list[str]:
    return [b.strip() for b in re.split(r"\n[ \t]*\n", text.strip()) if b.strip()]


def _is_prose(block: str) -> bool:
    return not (block.startswith(UNNUMBERED) or re.match(r"^\d+\.\s", block))


def parse_edits(deliverable: str) -> list[tuple[str, str, str]]:
    """[(op, paragraph id, body)] in reply order."""
    found = list(EDIT_RE.finditer(deliverable))
    out = []
    for i, m in enumerate(found):
        end = found[i + 1].start() if i + 1 < len(found) else len(deliverable)
        body = deliverable[m.end():end]
        stop = re.search(r"^#{2,3}\s", body, re.M)  # the next deliverable section (### Change Log) or H2 ends it
        if stop:
            body = body[:stop.start()]
        body = re.sub(r"\n?@@\s*END\s*$", "", body.strip(), flags=re.I).strip()
        out.append((m.group(1).upper(), m.group(2), body))
    return out


def _clean_new(body: str) -> list[str]:
    """New paragraphs arrive without numbers; strip any the drafter added anyway."""
    return [PARA_RE.sub("", b) for b in blocks(body)]


def apply_edits(description: str, edits: list[tuple[str, str, str]]) -> tuple[str, dict]:
    items = blocks(description)
    ids = [(m.group(1) + m.group(2)) if (m := PARA_RE.match(b)) else None for b in items]
    used_suffix: dict[str, int] = {}

    def next_id(anchor: str) -> str:
        base = re.match(r"\d+", anchor).group(0)
        existing = sum(1 for i in ids if i and i.startswith(base) and i != base)
        n = max(used_suffix.get(base, 0), existing) + 1
        used_suffix[base] = n
        suffix, k = "", n
        while k:
            k, r = divmod(k - 1, 26)
            suffix = chr(97 + r) + suffix
        return base + suffix

    applied, missing = [], []
    for op, pid, body in edits:
        if pid not in ids:
            missing.append(f"{op} [{pid}]")
            continue
        at = ids.index(pid)
        new = _clean_new(body)
        if op == "DELETE":
            items.pop(at)
            ids.pop(at)
        elif op == "REPLACE":
            if not new:
                missing.append(f"REPLACE [{pid}] (empty)")
                continue
            items[at] = f"[{pid}] {new[0]}" if _is_prose(new[0]) else new[0]
            ins_items, ins_ids = [], []
            for b in new[1:]:
                nid = next_id(pid) if _is_prose(b) else None
                ins_items.append(f"[{nid}] {b}" if nid else b)
                ins_ids.append(nid)
            items[at + 1:at + 1] = ins_items
            ids[at + 1:at + 1] = ins_ids
        else:  # AFTER
            ins_items, ins_ids = [], []
            for b in new:
                nid = next_id(pid) if _is_prose(b) else None
                ins_items.append(f"[{nid}] {b}" if nid else b)
                ins_ids.append(nid)
            # after the anchor and after anything already inserted after it
            pos = at + 1
            while pos < len(ids) and ids[pos] and re.fullmatch(re.escape(re.match(r"\d+", pid).group(0)) + r"[a-z]+", ids[pos]):
                pos += 1
            items[pos:pos] = ins_items
            ids[pos:pos] = ins_ids
        applied.append(f"{op} [{pid}]")
    return "\n\n".join(items) + "\n", {"applied": len(applied), "missing_anchor": missing}


def renumber(description: str) -> tuple[str, dict[str, str]]:
    out, mapping, n = [], {}, 0
    for b in blocks(description):
        m = PARA_RE.match(b)
        if m or _is_prose(b):
            n += 1
            new = f"{n:04d}"
            if m:
                mapping[m.group(1) + m.group(2)] = new
            out.append(f"[{new}] {PARA_RE.sub('', b)}")
        else:
            out.append(b)
    return "\n\n".join(out) + "\n", mapping


def remap_refs(text: str, mapping: dict[str, str]) -> str:
    if not mapping or all(k == v for k, v in mapping.items()):
        return text

    def sub(m: re.Match) -> str:
        return f"[{mapping.get(m.group(1), m.group(1))}]"

    def sub_pilcrow(m: re.Match) -> str:
        raw = m.group(2)
        key = re.sub(r"^(\d+)", lambda d: d.group(1).zfill(4), raw)
        new = mapping.get(key)
        if new is None:
            return m.group(0)
        return m.group(1) + (new if raw.startswith("0") else str(int(new)))

    text = re.sub(r"\[(\d{3,5}[a-z]*)\]", sub, text)
    return re.sub(r"(¶\s?)(\d{1,5}[a-z]*)", sub_pilcrow, text)
