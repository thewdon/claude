#!/usr/bin/env python3
"""Regenerate the A6 Rule Index in ICM-Methodology-Guide.md and check section cross-references.

Usage: python3 tools/build_rule_index.py [path-to-guide]
The index is rebuilt from bold rule IDs (**R-AREA-NN ...**, **INV-NN**) in Part I.
Never edit the index by hand.
"""
import re, sys, pathlib

path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "ICM-Methodology-Guide.md")
text = path.read_text(encoding="utf-8")

START = "<!-- GENERATED from the bold rule IDs"
part1_end = text.index("# PART II: REFERENCE APPENDIX")
part1 = text[:part1_end]

section = ""
rows, seen = [], {}
kw_re = re.compile(r"\b(MUST NOT|MUST \(validation\)|MUST|SHOULD NOT|SHOULD|MAY|INFO)(?![A-Za-z])")
for line in part1.splitlines():
    h = re.match(r"^(#{2,3}) (\d+(?:\.\d+)*)\.? ", line)
    if h:
        section = "§" + h.group(2)
        continue
    inv = re.match(r"^\| \*\*(INV-\d+)\*\* \| \*\*([^*]+)\*\*", line)
    m = re.search(r"\*\*((?:R-[A-Z0-9]+-\d+[a-z]?))\b([^*]*)\*\*", line)
    if inv:
        rid, title, kw = inv.group(1), inv.group(2), "MUST"
    elif m:
        rid = m.group(1)
        title = kw_re.sub("", m.group(2)).replace("()", "").strip(" .:()")
        k = kw_re.search(m.group(2)) or kw_re.search(line)
        kw = k.group(1) if k else "-"
    else:
        continue
    seen.setdefault(rid, []).append(section)
    tags = " ".join(sorted(set(re.findall(r"\[(?:A|R|P|M|F|PB|O|V|SS|X|I|EXT)\b[^\]]*\]", line))))[:60]
    summary = re.sub(r"\s+", " ", re.sub(r"\*\*[^*]*\*\*", "", line)).strip(" -|")
    summary = re.sub(r"\[[^\]]*\]", "", summary).strip()[:110]
    if not title:
        title = summary[:60]
    rows.append((rid, kw, section, title[:70].replace("|", "/"), tags.replace("|", "/")))

dups = {k: v for k, v in seen.items() if len(v) > 1}
table = ["| ID | Keyword | Section | Title / gist | Sources |", "|---|---|---|---|---|"]
table += [f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |" for r in rows]
index = "\n".join(table) + f"\n\nTotal rules indexed: {len(rows)}."

# Replace everything between the GENERATED marker line and the next '---' separator.
s = text.index(START)
s_end = text.index("\n", s) + 1
e = text.index("\n---\n", s_end)
text = text[:s_end] + "\n" + index + "\n" + text[e:]
path.write_text(text, encoding="utf-8")

# Cross-reference check: every §N(.N) mentioned must exist as a heading.
heads = set(re.findall(r"^#{2,4} (§?A?\d+(?:\.\d+)*)", text, re.M))
heads = {h.lstrip("§") for h in heads}
heads |= set(re.findall(r"^## (A\d+)\.", text, re.M))
heads |= set(re.findall(r"^### (A\d+\.\d+)", text, re.M))
scrub = re.sub(r"\[(?:P|M|R|A|F|PB|O)[^\]]*\]", "", text)  # drop source-tag citations like [P §3.2]
refs = set(re.findall(r"§(A?\d+(?:\.\d+)*)", scrub))
missing = sorted(r for r in refs if r not in heads)
undefined = sorted(set(re.findall(r"\b(R-[A-Z0-9]+-\d+|INV-\d+)\b", text)) - set(seen))
print(f"undefined rule IDs referenced: {undefined or 'none'}")
print(f"rules indexed: {len(rows)}; duplicate IDs: {dups or 'none'}")
print(f"section refs: {len(refs)}; unresolved: {missing or 'none'}")
