# ICM Methodology Guide

An AI-consumable specification of Jake Van Clief's **Interpretable Context Methodology (ICM)**. ICM is a way of running AI work through numbered folders and plain markdown files instead of agent frameworks. The guide is the basis for building our own skills and workflows.

| File | What it is |
|---|---|
| `ICM-Methodology-Guide.md` | The guide. Part I is the operating core an agent uses while working; Part II is the reference appendix (rationale, examples, source conflicts, evidence, extensions register, rule index, sources). |
| `tools/validate_workspace.py` | A reference validator for the mechanical checks in §17. |
| `tools/build_rule_index.py` | Regenerates the §A6 rule index and checks cross-references. Run it after every edit. |
| `tools/test_templates.py` | Regression test: the §20 templates must pass the validator, before and after a simulated setup. |

Every rule carries a source tag. Tags such as `[A]`, `[R]`, `[P]`, `[F]` mark Jake's material. `[EXT]` marks a convention we added to close a gap; those are listed in §A5 for review before adoption.
