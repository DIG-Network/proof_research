# Results: joint-min-max-product-weight-five-six-shell-collision

**Outcome:** PASS

**Setup:** \(n=10\), public weights \(w_i=i+1\) for indices \(0..9\). Shells \(|S|=5\) and \(|S|=6\).

**Statistic:** \(K(S)=(\min_{i\in S} w_i,\max_{i\in S} w_i,\prod_{i\in S} w_i)\) exact integers; \(K_M=(\min,\max,\prod\bmod M)\).

**Counts:**

| Metric | Value |
|--------|------:|
| Distinct \(K\) on 5-shell | 226 |
| Distinct \(K\) on 6-shell | 181 |
| Exact cross-shell keys \(\|K_5\cap K_6\|\) | 31 |

**Sample exact collision:** \(K=(1,7,840)\): five-set indices `(0,3,4,5,6)` vs six-set `(0,1,2,3,4,6)` (weights \(1,4,5,6,7\) vs \(1,2,3,4,5,7\); products both \(840\)).

**Modular fold:** Smallest \(M\ge 2\) with a cross-shell collision for \(K_M\) is **\(M=2\)**. At \(M=2\), **15** cross-shell joint keys. Sample: \((1,6,0)\): five-set `(0,1,2,3,5)` vs six-set `(0,1,2,3,4,5)`.

**Comparison to entry 091** (`min-max-sum-triple-weight-five-six-shell-collision`): Sum triple had **41** exact cross-shell keys and first mod collision at **\(M=2\)** with **25** shared \(K_M\) keys. Product triple has **fewer** exact collisions (**31**) but **same** first modulus **\(M=2\)** for the joint \((\min,\max,\cdot)\) fold.

**Conclusion:** Replacing **sum** by **product** in the \((\min,\max,\cdot)\) joint tag does **not** restore shell separation on this toy; multiplicative mass still admits many exact cross-shell witnesses, and **parity of \(\prod w_i\)** already merges shells at **\(M=2\)**, matching the 091 modulus floor.
