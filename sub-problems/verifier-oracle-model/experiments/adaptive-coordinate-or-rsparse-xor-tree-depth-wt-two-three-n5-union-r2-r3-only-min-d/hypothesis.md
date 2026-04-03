# Hypothesis

**Outcome (2026-04-03):** **PASS** — union `min_d=2` with only `r=2,3` (see `results.md`).

**Claim (pre-run):** For `n=5` with mask shell weights `{2,3}` (20 masks), the language **coordinate splits** plus **XOR union only over arities `r=2` and `r=3`** (20 XOR splits, same count as weight-2-only shell with `r=2..3` union) still has **`min_d = 2`**.

**Falsification:** Parent reports `min_d = 1` for `coord + XOR_2 ∪ XOR_3` on this shell.

## Analogy pass

1. **Abstract structure:** Factorial ablation on a two-knob design (mask alphabet vs XOR-arity menu). We hold split-count at 20 while varying whether `r=4` parity tests are present.

2. **Analogous domains:** (a) **ANOVA / interaction** in discrete experiments — separate main effects of “more masks” vs “more test types”. (b) **Feature ablation** in ML — does performance drop when removing one feature group? (c) **Minimal sufficient statistic** — what is the smallest menu that already encodes the hardness?

3. **Machinery:** Controlled comparison at matched menu size; parse optimizer output for `min_d`.

4. **Transfer seed:** Prior work showed `{2,3}` + `r=2..4` has `min_d=2` while `{2}` + `r=2..4` has `min_d=1`, implicating the weight-3 extension. This experiment asks whether **`r=4` XOR splits are necessary** for that bump or whether **weight-3 masks alone** (with only `r=2,3`) already force depth 2.

## Memory / lineage

- **Parent driver:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5/script.py`.
- **Builds on:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-full-r2-r4-union-min-d` (`min_d=2` with 25 splits).
- **Contrasts:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5-shell2-union-r2-r4-min-d` (`{2}` + `r=2..4` → `min_d=1`).
