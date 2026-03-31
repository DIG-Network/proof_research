# Notes

- **vs `(10,{5,6})` arity ladder (066 / 090 / 091 / 093 / 092):** On `n=10`, pair→triple→quad→pentuple gave strict `5→4→3→2` before adding global parity (`min_d=1`). On `n=9` with `{5,6}`, **triple, quad, and pentuple all plateau at `min_d=3`**; only `r=8` (octuple) reaches `2` without the full `n`-XOR. So shrinking `n` while fixing shell *weights* **collapses** the fine-grained arity steps seen on the canonical 462-mask row.

- **Interior bump:** `r=6` is worse (`4`) than `r∈{3,4,5,7}` (`3`), same qualitative pattern as **097** `min_d(6)=4` on `(9,{4,5})`.

- **Unions:** Including `r=5` drops union `r∈{2,3,4}` from depth `3` to `2`; full `r≤8` union does not improve past `2` (still need `r=8` or the full XOR gate for `2` in the single-arity column).

- **Quorum semantics:** Do not read this as “threshold `t−1` vs `t`” for `n=9`; both weights are ≥ `t=5`. Comparison to **066–093** is about **same Hamming shells, smaller ambient `n`**.
