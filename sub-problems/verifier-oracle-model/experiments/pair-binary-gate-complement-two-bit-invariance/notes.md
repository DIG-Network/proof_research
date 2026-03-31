# Notes

- **Unsticking:** After binding-side mod-\(M\) scalar summaries (050 product, 052 square sum), this iteration stayed on **verifier-oracle-model** with a **classification** experiment (no new backtracking blow-up).

- **Structure:** Gates invariant under \((a,b)\mapsto(1-a,1-b)\) are exactly those constant on each orbit of that involution: \(\{(0,0),(1,1)\}\) and \(\{(0,1),(1,0)\}\). There are **four** Boolean functions with that symmetry (choose output on each orbit): constants \(0,1\), XOR, XNOR. Among the “standard” four-variable set \(\{\mathrm{AND},\mathrm{OR},\mathrm{XOR},\mathrm{XNOR}\}\), only the affine-linear pair XOR/XNOR appear.

- **Next verifier directions:** (i) **Mixed** trees (AND at some nodes, XOR at others) — equivariance is **path-dependent**; no single global involution kills the whole transcript. (ii) **Ternary** or **parity-of-three** probes if we ever formalize a larger oracle alphabet. (iii) Binding follow-up from 052: joint \((\sum w_i \bmod M_1,\ \sum w_i^2 \bmod M_2)\) collision search for \(|S|\in\{5,6\}\), \(n=10\).
