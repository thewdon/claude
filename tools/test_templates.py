#!/usr/bin/env python3
"""Regression test: the guide's §20 templates must pass the guide's own validator, before and after setup.

Usage: python3 tools/test_templates.py [guide-path]
Builds a Tier 2 workspace from §20.4-§20.9, §20.8b, §20.15 in a temp dir, fills author fill-ins mechanically,
validates, simulates `setup` from the questionnaire mappings, and validates again with --after-setup.
"""
import os, re, shutil, subprocess, sys, tempfile
GUIDE = sys.argv[1] if len(sys.argv) > 1 else "ICM-Methodology-Guide.md"
t = open(GUIDE, encoding="utf-8").read()
HERE = os.path.dirname(os.path.abspath(__file__))
S = tempfile.mkdtemp(prefix="icm-tpl-")


def blocks_after(h, n=1):
    i = t.index(h); out = []
    for _ in range(n):
        j = t.index("```markdown", i) + len("```markdown\n"); k = t.index("\n```\n", j); out.append(t[j:k]); i = k
    return out
ws = os.path.join(S, "ws")
def w(p,c):
    p=os.path.join(ws,p); os.makedirs(os.path.dirname(p),exist_ok=True); open(p,"w").write(c)
def fill(c, stage=None, prev=None):
    c=c.replace("[NN]_[stage-name]",stage or "x").replace("[NN-1]_[prev]",prev or "00_none")
    c=c.replace("Class: [creative | analytic | build | linear]","Class: creative")
    c=re.sub(r"`stages/01_\[[^\]]*\]/CONTEXT.md`","`stages/01_intake/CONTEXT.md`",c)
    c=c.replace("[NN]_[name]","03_final").replace("03_[name]","03_final")
    c=re.sub(r"\[(?!Checkpoint \d+\])(?![ x]\])([A-Za-z][^\]\n]*)\](?!\()", "filled", c)
    return c
w("CLAUDE.md",fill(blocks_after("### 20.4 Tier 2 `CLAUDE.md`")[0]))
w("CONTEXT.md",fill(blocks_after("### 20.5 Root `CONTEXT.md`")[0]))
w("PROGRESS.md",fill(blocks_after("### 20.9 `PROGRESS.md`")[0]))
w("setup/questionnaire.md",fill(blocks_after("### 20.7 Setup questionnaire")[0]))
w("setup/new-run.md",fill(blocks_after("### 20.15 `setup/new-run.md`")[0]))
w("_shared/voice.md",blocks_after("### 20.8 Voice file")[0])
dod,rules,assets=blocks_after("### 20.8b Factory stubs",3)
w("_shared/definition-of-done.md",dod); w("_shared/rules.md",rules); w("_shared/assets.md",assets)
sc,final_hc,auto_hc=blocks_after("### 20.6 Stage `CONTEXT.md`",3)
stages=["01_intake","02_draft","03_final"]
for i,s in enumerate(stages):
    c=fill(sc,s,stages[i-1] if i else "00_none")
    if s=="03_final": c=c[:c.index("## Human check")]+final_hc
    w(f"stages/{s}/CONTEXT.md",c)
    for d in ["references","output"]: w(f"stages/{s}/{d}/.gitkeep","")
    w(f"stages/{s}/references/filled.md","ref\n")
w("stages/01_intake/input/.gitkeep","")
for d in ["scripts","_archive/runs"]: w(f"{d}/.gitkeep","")
w(".gitignore",".env\n")

def run(*extra):
    r = subprocess.run([sys.executable, os.path.join(HERE, "validate_workspace.py"), ws, *extra], capture_output=True, text=True)
    print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr)
    return r.returncode, r.stdout


code1, out1 = run()
q = open(os.path.join(ws, "setup/questionnaire.md")).read()
pairs = [(n, f) for n, fs in re.findall(r"^- `\{\{([A-Z0-9_]+)\}\}` → (.+)$", q, re.M) for f in re.findall(r"`([^`]+)`", fs)]
for a, b, f in re.findall(r"Derived: `\{\{([A-Z0-9_]+)\}\}`.*?`\{\{([A-Z0-9_]+)\}\}` → `([^`]+)`", q):
    pairs += [(a, f), (b, f)]
for n, f in pairs:
    p = os.path.join(ws, f)
    if os.path.isfile(p):
        s = open(p).read().replace("{{" + n + "}}", "- value" if n.endswith("S") else "value-" + n.lower())
        open(p, "w").write(s)
code2, out2 = run("--after-setup")
shutil.rmtree(S, ignore_errors=True)
ok = code1 == 0 and code2 == 0 and "WARN" not in out1 + out2
print("TEMPLATES OK" if ok else "TEMPLATES FAIL\n" + out1 + out2)
sys.exit(0 if ok else 1)
