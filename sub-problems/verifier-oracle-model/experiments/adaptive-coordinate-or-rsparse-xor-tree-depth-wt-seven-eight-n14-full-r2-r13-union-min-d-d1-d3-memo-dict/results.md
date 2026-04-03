# Results

**Outcome:** PASS

**Command:** `python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-full-r2-r13-union-min-d-d1-d3-memo-dict/script.py`

**Measured:**

- `total_splits=16368` (full `r=2..13` XOR union + coord splits in parent DP).
- `d=1 feasible=False` (~0.107 s); `VmRSS_after_d=1_kb=60092`.
- `d=2 feasible=True` (~0.126 s); `min_d=2`.
- End-to-end `dp_sec` ~0.234 s (parent prints after both probes).
- `VmRSS_peak_kb=68332`.

**Interpretation:** The full combined language already admits a **depth-2** refuting decision tree on this `{7,8}` shell. The earlier **`d=3`-only** full-union PASS was **not** depth-minimal; it stopped at the first tested depth without establishing `min_d`.
