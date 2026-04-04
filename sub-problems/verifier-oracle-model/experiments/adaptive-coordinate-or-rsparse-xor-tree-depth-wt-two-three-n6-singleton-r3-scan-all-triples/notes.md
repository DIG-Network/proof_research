# Notes — n=6 singleton r=3 scan

- **Uniformity:** All 20 lex-ordered triples behaved identically (`min_d=3`); there is no “special” triple index at `n=6` in this regime (contrast with `n=5` where every singleton worked).
- **Interpretation:** Larger mask shell / coordinate set likely requires **more** than one triple split to emulate the discriminating power of the full `r=3` menu when paired with all pair parities.
- **Implementation:** Parent `n=6` driver now mirrors `n=5`’s `--union-r3-indices` so wrappers can shard or singleton-test triple XORs without pulling in all `C(6,3)=20` splits at once.
- **Next (optional):** Scan **pairs** of triple indices (`k=2`) or minimal `k` such that `min_d=2` with full `r=2` fixed — bridges gap between `n=5` singleton sufficiency and `n=6` full union.
