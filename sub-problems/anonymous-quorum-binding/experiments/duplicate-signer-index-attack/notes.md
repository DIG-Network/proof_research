# Notes

- Orthogonal to **016** (missing `K` vs leaf-sum): here `K` **matches** the multiset sum; the bug is **cardinality of the support** of `S`, not the aggregate field.
- Orthogonal to **013** (lied `k̂`): no separate count field — the **list** `S` is padded by repetition.
- **011** / `r1-baseline` already encodes the fix (`len(set(S)) == len(S)`); this experiment names the failure mode for implementers who only check `len(S) >= t`.
