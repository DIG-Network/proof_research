# Hypothesis — exhaustive partial r=5, K=2 (1540 menus), off-diagonal s012 stratum

## Analogy pass (mandatory)

1. **Abstract structure:** Fix the n=8 adaptive-coordinate / r-sparse XOR language shell through singleton r=4; vary only which two r=5 XOR splits are included. On the off-diagonal triple–triple–quad stratum with `|T_i ∩ T_j| ∈ {0,1,2}`, count how many cells have minimum XOR-tree depth 2 (`stratum_min_d2`). The random K=2 probe found a constant intermediate count (**7630**) across 16 draws—between K=1 exhaustive (**3850**) and full-menu saturation (**107800**).

2. **Analogous domains:** (i) Finite-sample versus population inference in statistics—exhaustive enumeration removes sampling bias. (ii) Verifying a conjectured plateau in computational physics by scanning the full discrete configuration space. (iii) Combinatorial design: checking whether a statistic is invariant under all choices of a small discrete structure.

3. **Machinery in those domains:** Full grid search / complete enumeration; symmetry reduction is not available here without theory—so brute force over **C(56,2)=1540** unordered pairs.

4. **Transferable seed:** Enumeration over all K=2 menus tests whether **7630** is **universal** (min = max) or whether some menus collapse to **0** or **107800**, sharpening the structural picture before any closed-form derivation (**2×3850−70=7630** vs **len(p4)=70**).

## Falsifiable claims

- **Primary (same exit semantics as prior scans):** At least one menu yields **`0 < stratum_min_d2 < 107800`** ⇒ script **exit 0** (PASS). If **every** menu yields **`stratum_min_d2 ∈ {0, 107800}`** ⇒ **exit 1** (FAIL).
- **Secondary (reported from aggregates):** Record **`min_stratum_d2_across_menus`** and **`max_stratum_d2_across_menus`**. If both equal **7630** for the full **1540** menus, the random sample’s plateau is **universal** on this stratum.

## Relation to prior experiments

- **`…-partial-r5-k1-exhaustive-all-56-offdiag-structure-scan`:** uniform **3850**.
- **`…-partial-r5-k2-random-trials-16-offdiag-structure-scan`:** **16/16** trials ⇒ **7630**; exhaustive **1540** was listed as next step.
- **`…-partial-r6-k2-exhaustive-all-378-offdiag-structure-scan`:** universal **107800** (no intermediate plateau).
