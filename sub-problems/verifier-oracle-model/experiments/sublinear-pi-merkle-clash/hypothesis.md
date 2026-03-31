# Hypothesis

**H:** Fix **strict majority** `t = ⌊n/2⌋ + 1` and the **M1** accounting from Entry **003** / `vc-opening-budget`: each of `t` signers carries an independent Merkle inclusion path of **`Θ(λ · log n)`** bits. Then total **`|π|`** for that pattern is **`Θ(n · λ · log n)`** bits.

**Corollary (tested numerically):** For large `n`, **`|π|_M1`** exceeds any budget of the form **`B(n) = λ · (log₂ n)^k`** with **fixed** `k` and sufficiently large `n` (e.g. **`k = 2`**, **`λ = 256`**), since **`n / polylog(n) → ∞`**.

**Falsification:** Find `n ≥ 64` where `t · bits_per_path ≤ λ · (log₂ n)²` under the same `bits_per_path` model as `vc-opening-budget/script.py`.

**Relation:** Entry **011** shows **M1-style** proofs **work** for soundness; this experiment quantifies why they are **not** **sublinear** in `n`.
