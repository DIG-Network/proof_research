# Results — relaxation-ladder

**Outcome:** **PASS** (documentation / taxonomy); **INCONCLUSIVE** on existence of **R7**

## Summary

The scripted ladder lists **R1–R6** as **standard** repairs that each **conflict** with at least one clause of `main-problem/problem-statement.md` (compact `π`, verifier input, no SNARK, no trusted setup, no TEE). **R7** is the **placeholder** for a hypothetical compliant construction.

## Interpretation

- This does **not** prove impossibility: **R7** may exist or may not.
- It **organizes** prior experiments: **002–005** motivate why **R1–R5** are the usual “escape hatches” engineers reach for.
- **Entry 009** (threat model) layers **on top**: even **R7** must state **registration** assumptions (**007** vs **008**).

## Script

`python script.py` — prints ladder; asserts only **R7** marked `main_compliant`; exit 0.
