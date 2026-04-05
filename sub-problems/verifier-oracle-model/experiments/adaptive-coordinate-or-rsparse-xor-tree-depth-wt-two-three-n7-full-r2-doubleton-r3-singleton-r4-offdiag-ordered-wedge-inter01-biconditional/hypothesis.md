# Hypothesis: ordered wedge characterizes `min_d=2` on `|T_i∩T_j|∈{0,1}`

## Abstract structure

We fix the same adaptive language as prior `n=7` doubleton-triple + singleton-quartic scans: coordinate splits, full `r=2` XOR menu, **two** distinct `r=3` XOR splits (indexed `i<j` as an unordered pair of triples), and one `r=4` XOR split defining `Q`. For each cell we compute `min_d` by the parent DP. Off-diagonal structure at depth `2` resisted symmetric templates; the next structural knob is **order**: the first triple index may play a different role than the second.

## Analogy pass

1. **Core relationship:** A decision tree’s minimal depth depends on how parity questions partition the state space. When two structured queries overlap, the “first vs second” child in an AND-of-splits semantics can break symmetry that made symmetric difference look universal.

2. **Analogous domains:**
   - **Directed graphs vs undirected:** reachability and cuts change when edges gain orientation; here `(i,j)` orients which triple is “primary.”
   - **Ordered vs unordered hypothesis tests:** sequential testing statistics depend on order even when the unordered multiset is fixed.
   - **Schubert cells / flags:** a flag is an **ordered** tower of subspaces; which subspace comes first is part of the data, not quotiented away.

3. **Machinery in those domains:** oriented cuts, sequential likelihood ratios, Bruhat order on flags.

4. **Transfer candidate:** Use the **ordered wedge** already successful as one chart on the `|∩|=2` stratum (with complement-symdiff), but now test whether **alone** it biconditionally characterizes `min_d=2` on the thinner `|∩|∈{0,1}` stratum:

   \[
   W_{i,j} = (T_i \setminus T_j) \cup \bigl([7] \setminus (T_i \cup T_j)\bigr).
   \]

## Falsifiable claim

Restrict to `i<j` and `s=\mathrm{popc}(T_i\cap T_j)\in\{0,1\}`. Then

\[
\min\_d = 2 \iff Q_{\text{mask}} = W_{i,j}.
\]

(If `s=0`, note `W_{i,j}=\overline{T_j}` as bitmasks when `T_i\cap T_j=\emptyset`.)

## Memory / prior context

- Symmetric difference biconditional on this stratum **failed** (`…-offdiag-symdiff-inter01-biconditional`).
- On `|∩|=2`, `min_d=2` matched a **disjunction** `{W, complement(symdiff)}`, not wedge alone.

Parent experiment path: `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-doubleton-r3-singleton-r4-structure-scan` (PASS enumeration).
