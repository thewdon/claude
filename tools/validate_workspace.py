#!/usr/bin/env python3
"""Reference validator for ICM workspaces (mechanical subset of ICM-Methodology-Guide.md §17).

Usage:
  python3 tools/validate_workspace.py <workspace-root> [--after-setup] [--run <run-id>] [--status] [--solo]

  --after-setup  also fail if any setup placeholder remains (§10.3 step 9)
  --run ID       resolve <run-id> in Inputs paths and require working inputs to exist (V1)
  --status       print the pipeline status (§9.5): PENDING / DRAFT / AUDITED / APPROVED / STALE
  --solo         one-owner workspace (§1.5): gate/reviewer fields are optional

Checks implemented: V1 V2 V3 V3b V4 V5 V6 V7 V8 (vague words) V10 V11 V14 V15 W9, R-L0-03, R-XREF-01 in L3.
Checks NOT implemented (need judgment): W1 W4 W5 W7 V9 V12 V13 and every "concrete act" quality call.
Exit code 1 if any FAIL. WARN lines are advisory.
"""
import os, re, sys

args = sys.argv[1:]
if not args or args[0].startswith("-"):
    sys.exit(__doc__)
root = os.path.abspath(args[0])
AFTER, STATUS, SOLO = "--after-setup" in args, "--status" in args, "--solo" in args
RUN = args[args.index("--run") + 1] if "--run" in args else None

FAIL, WARN = [], []
PH = re.compile(r"\{\{([A-Z0-9_]+)\}\}")
COND = re.compile(r"\{\{\?([A-Z0-9_]+)\}\}")
ANY_PH = re.compile(r"\{\{[?/]?[A-Z0-9_]+\}\}")
FILLIN = re.compile(r"\[(?!Checkpoint \d+\])(?![ x]\])([A-Z][^\]\n]{1,80})\](?!\()")
STAGE_DIR = re.compile(r"^\d\d[a-z]?[_-][a-z0-9-]+$")
ALLOWED = {"Inputs", "Process", "Checkpoints", "Audit", "Verify", "Outputs", "Human check",
           "When to Loop Back", "Source of Truth", "Source of truth", "Source of Truth at Each Stage"}
UPPER_OK = {"CLAUDE.md", "AGENTS.md", "CONTEXT.md", "PROGRESS.md", "README.md", "SKILL.md",
            "STATUS.md", "PRD.md", "FILE-MAP.md", "LICENSE", ".gitkeep", ".gitignore", ".env"}
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv"}
CODE_EXT = {".py", ".ts", ".tsx", ".js", ".jsx", ".json", ".csv", ".sh", ".css", ".html", ".yml", ".yaml"}


def rel(p): return os.path.relpath(p, root)
def read(p): return open(os.path.join(root, p), encoding="utf-8", errors="replace").read()
def exists(p): return os.path.exists(os.path.join(root, p))


def walk(include_archive=False):
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS and (include_archive or rel(os.path.join(d, x)) != "_archive")]
        yield d, dirs, files


def md_files():
    for d, _, files in walk():
        for f in files:
            if f.endswith(".md"):
                yield rel(os.path.join(d, f))


def section(text, name):
    m = re.search(rf"^## {re.escape(name)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else None


def header_status(path):
    """Gate status from YAML frontmatter or a '**Status:**' / 'status:' line, or a sidecar <file>.status."""
    side = path + ".status"
    if exists(side):
        return read(side).strip().split()[0].lower()
    try:
        head = read(path)[:1500]
    except Exception:
        return None
    m = re.search(r"^(?:\*\*)?status(?:\*\*)?:\s*\**\s*([a-z-]+)", head, re.M | re.I)
    return m.group(1).lower() if m else None


# ---------- entry file ----------
if not exists("CLAUDE.md") and not exists("AGENTS.md"):
    FAIL.append("INV-02 no CLAUDE.md or AGENTS.md at root")
entry = "CLAUDE.md" if exists("CLAUDE.md") else ("AGENTS.md" if exists("AGENTS.md") else None)
entry_text = read(entry) if entry else ""
n = len(entry_text.splitlines())
if n > 60:
    FAIL.append(f"V10 {entry} is {n} lines (limit ~60, target 30-50; §3)")
elif n > 50:
    WARN.append(f"V10 {entry} is {n} lines (target 30-50)")
if ANY_PH.search(entry_text):
    FAIL.append(f"R-L0-03 setup placeholder in {entry}")
if exists("CLAUDE.md") and exists("AGENTS.md") and read("CLAUDE.md") != read("AGENTS.md") and len(read("AGENTS.md").splitlines()) > 3:
    WARN.append("R-NAME-10 CLAUDE.md and AGENTS.md differ and AGENTS.md is not a one-line pointer")

# W9: every top-level folder is mentioned by the entry file or root CONTEXT.md
routing_text = entry_text + (read("CONTEXT.md") if exists("CONTEXT.md") else "")
for d in sorted(os.listdir(root)):
    if os.path.isdir(os.path.join(root, d)) and d not in SKIP_DIRS and not d.startswith("."):
        if d not in routing_text:
            FAIL.append(f"W9 top-level folder {d}/ is not routed from {entry} or CONTEXT.md")

# ---------- stages ----------
stage_root = os.path.join(root, "stages")
stages = sorted(x for x in os.listdir(stage_root) if STAGE_DIR.match(x)) if os.path.isdir(stage_root) else []
seps = {s[2] if s[2] in "_-" else s[3] for s in stages}
if len(seps) > 1:
    FAIL.append(f"R-NAME-01 mixed stage separators {sorted(seps)}")
status_rows = []
for i, s in enumerate(stages):
    cp = f"stages/{s}/CONTEXT.md"
    if not exists(cp):
        FAIL.append(f"INV-04 {cp} missing")
        continue
    t = read(cp)
    lines = len(t.splitlines())
    if lines >= 80:
        FAIL.append(f"V10 {cp} is {lines} lines (must be under 80)")
    heads = [h.strip() for h in re.findall(r"^## (.+)$", t, re.M)]
    for h in heads:
        if h not in ALLOWED:
            FAIL.append(f"V6 {cp} disallowed section '## {h}' (R-CTR-30)")
    for req in ("Inputs", "Process", "Outputs"):
        if req not in heads:
            FAIL.append(f"R-CTR {cp} missing ## {req}")
    if "Human check" not in heads:
        WARN.append(f"R-CTR-24 {cp} has no ## Human check (repo-style stages should gain one)")
    if not re.search(r"^Do NOT load", t, re.M | re.I):
        WARN.append(f"R-CTR-10 {cp} has no 'Do NOT load' line")
    hc = section(t, "Human check") or ""
    gate = re.search(r"Gate:\s*(blocking|auto-advance|final approval)", hc)
    if not SOLO and "Human check" in heads and (not gate or "Reviewer:" not in hc):
        FAIL.append(f"V15 {cp} Human check lacks 'Gate:' and/or 'Reviewer:' (use --solo for one-owner workspaces)")
    # V7 checkpoint step numbers
    proc = section(t, "Process") or ""
    steps = {int(x) for x in re.findall(r"^\s*(\d+)\.", proc, re.M)}
    cps = section(t, "Checkpoints")
    if cps:
        for row in re.findall(r"^\|\s*(\d+)\s*\|", cps, re.M):
            if int(row) not in steps:
                FAIL.append(f"V7 {cp} checkpoint after step {row}, which is not a Process step")
    aud = section(t, "Audit")
    if aud:
        for chk, cond in re.findall(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", aud, re.M):
            if chk.lower() in ("check", "-------") or set(chk) <= set("-: "):
                continue
            if re.search(r"\b(good|fine|appropriate|high quality|looks right)\b", cond, re.I):
                FAIL.append(f"V8 {cp} audit '{chk}' has a vague pass condition")
    elif gate and gate.group(1) != "auto-advance":
        WARN.append(f"V8 {cp} has no ## Audit (required for creative, analytic, build stages)")
    # V1 + V5 + V2
    inp = section(t, "Inputs") or ""
    inp_rows = "\n".join(l for l in inp.splitlines() if not re.match(r"\s*\**Do NOT load", l, re.I))
    paths = re.findall(r"`([^`]*(?:/|\.md|\.csv|\.json)[^`]*)`", inp_rows)
    for loc in paths:
        if loc.startswith(("~", "/", "http")):
            continue
        path = loc.replace("<run-id>", RUN) if RUN else loc
        optional = re.search(re.escape(loc) + r"[^\n]*optional", inp, re.I)
        if any(c in path for c in "<{*") or "..." in path:
            continue
        full = os.path.normpath(os.path.join(root, "stages", s, path))
        is_working = "/output/" in path or path.startswith("output/") or "input/" in path
        if (not is_working or RUN) and not os.path.exists(full) and not optional:
            FAIL.append(f"V1 {cp} input does not resolve: {loc}")
    if i > 0 and "../" + stages[i - 1] + "/output/" not in t:
        WARN.append(f"V5 {cp} does not read ../{stages[i - 1]}/output/ (fine only if it reads an earlier stage on purpose)")
    for m in re.findall(r"\.\./(\d\d[a-z]?[_-][a-z0-9-]+)/", t):
        if m in stages and stages.index(m) > i:
            FAIL.append(f"V2 {cp} points forward to {m} (R-XREF-01)")
    # status
    out_dir = os.path.join(stage_root, s, "output")
    files = [f for f in (os.listdir(out_dir) if os.path.isdir(out_dir) else []) if f not in (".gitkeep",) and not f.endswith(".status") and os.path.isfile(os.path.join(out_dir, f))]
    primary = [f for f in files if (header_status(f"stages/{s}/output/{f}") or "") not in ("", "generated")]
    if not files:
        st = "PENDING"
    elif primary:
        st = header_status(f"stages/{s}/output/{primary[0]}").upper()
        st = {"REVISED": "DRAFT", "FINAL": "APPROVED"}.get(st, st)
    else:
        st = "COMPLETE (no gate status in header)"
    status_rows.append((s, st, files[:3]))

# ---------- L3 bodies must not point into stages ----------
for f in md_files():
    top = f.split("/")[0]
    if top in ("_shared", "shared", "_config", "brand-vault", "design-system") and re.search(r"stages/\d\d[_-]", read(f)):
        WARN.append(f"R-XREF-01 {f} (L3) names a stage path: fine if purely descriptive, a violation if stages depend on it pointing back")
    if (top in ("_shared", "shared") or "/references/" in f) and re.search(r"<[a-z][a-z0-9-]+>", read(f)):
        WARN.append(f"V2 {f} contains a <per-run variable> in an L3 body")

# ---------- setup: V3, V4 ----------
qp = "setup/questionnaire.md"
used, conds_used = {}, {}
for f in md_files():
    if f == qp:
        continue
    tx = read(f)
    for nme in PH.findall(tx):
        used.setdefault(nme, set()).add(f)
    for nme in COND.findall(tx):
        conds_used.setdefault(nme, set()).add(f)
    for m in re.finditer(r"\{\{\?([A-Z0-9_]+)\}\}\s*\n(.*?)\{\{/\1\}\}", tx, re.S):
        if not m.group(2).lstrip().startswith("#"):
            FAIL.append(f"V4 {f} conditional {m.group(1)} does not wrap a whole section")
if AFTER:
    for nme, fs in sorted(used.items()):
        FAIL.append(f"V3 after setup: {{{{{nme}}}}} remains in {sorted(fs)}")
    for nme, fs in sorted(conds_used.items()):
        FAIL.append(f"V3 after setup: conditional {nme} markers remain in {sorted(fs)}")
elif exists(qp):
    q = read(qp)
    qnames = set(PH.findall(q))
    for nme in used:
        if nme not in qnames:
            FAIL.append(f"V3 {{{{{nme}}}}} has no question")
    for nme in conds_used:
        if nme not in q:
            FAIL.append(f"V3 conditional {nme} has no yes/no question")
    for nme in qnames:
        if nme not in used:
            FAIL.append(f"V3 question placeholder {{{{{nme}}}}} appears in no file")
    for nme, files in re.findall(r"^- `\{\{([A-Z0-9_]+)\}\}` → (.+)$", q, re.M):
        for f in re.findall(r"`([^`]+)`", files):
            if exists(f) and os.path.isfile(os.path.join(root, f)) and "{{" + nme + "}}" not in read(f):
                FAIL.append(f"V3 {{{{{nme}}}}} is mapped to {f} but not present there")
    for block in re.split(r"^### Q\d+:", q, flags=re.M)[1:]:
        if re.search(r"Type:\s*yes/no", block) and "- Files:" not in block:
            FAIL.append("V3 a yes/no question has no '- Files:' line (R-Q-12)")
elif used and not AFTER:
    WARN.append("placeholders exist but there is no setup/questionnaire.md")

# ---------- V3b author fill-ins ----------
for f in md_files():
    if f.startswith(("_meta/", "skills/")) or f == qp:
        continue
    body = re.sub(r"```.*?```", "", read(f), flags=re.S)  # examples inside code fences are formats, not fill-ins
    for m in FILLIN.findall(body):
        (WARN if "/references/" in f else FAIL).append(f"V3b {f} unfilled author fill-in [{m}]" + (" (in a reference file: fine if it is an output-format slot)" if "/references/" in f else ""))
        break

# ---------- V11 naming, .gitkeep ----------
for d, dirs, files in walk():
    for x in files + dirs:
        if x in UPPER_OK or x in SKIP_DIRS or x.startswith(("LICENSE", "NOTICE")):
            continue
        ext = os.path.splitext(x)[1]
        if ext in CODE_EXT and ext != ".md":
            continue  # code and data follow their own conventions (R-NAME-02 exceptions)
        if not re.fullmatch(r"[a-z0-9_.-]+", x):
            FAIL.append(f"V11 name not lowercase kebab-case: {rel(os.path.join(d, x))}")
    if not files and not dirs and rel(d) != ".":
        FAIL.append(f"R-NAME-14 empty folder without .gitkeep: {rel(d)}")

# ---------- V14 safety ----------
gi = read(".gitignore") if exists(".gitignore") else ""
if exists(".env") and ".env" not in gi:
    FAIL.append("V14 .env exists but is not in .gitignore")
KEY = re.compile(r"(sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[bp]-[A-Za-z0-9-]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY)")
for d, _, files in walk(include_archive=True):
    for f in files:
        p = rel(os.path.join(d, f))
        if f == ".env":
            continue
        try:
            if KEY.search(read(p)):
                FAIL.append(f"V14 possible secret in {p}")
        except Exception:
            pass

# ---------- report ----------
if STATUS and stages:
    print(f"Pipeline Status: {os.path.basename(root)}" + (f"   (run {RUN})" if RUN else ""))
    print("  " + "  ---->  ".join(f"[{s}]" for s, _, _ in status_rows))
    for s, st, fs in status_rows:
        print(f"    {s}: {st}" + (f"  ({', '.join(fs)})" if fs else ""))
for w in WARN:
    print("WARN", w)
for f in FAIL:
    print("FAIL", f)
print(f"\n{len(FAIL)} fail, {len(WARN)} warn" + ("" if FAIL else "  -> mechanical checks pass; now run the walk test (§17.1) by hand"))
sys.exit(1 if FAIL else 0)
