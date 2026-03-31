# Entry 048 — adaptive-pairwise-and-tree-depth-wt-five-vs-six

**Date:** 2026-03-30  
**Context:** `sub-problems/verifier-oracle-model`  
**Experiment:** `experiments/adaptive-pairwise-and-tree-depth-wt-five-vs-six/`

## Hypothesis tested

Non-coordinate **pairwise AND** adaptive decision trees might **beat** the **045** coordinate worst-case depth (`n` on `(10,6)` wt shells) by using **nonlinear** probes `x_i ∧ x_j`.

## Outcome: **PASS**

## Key finding

Exhaustive min-depth backtracking on small threshold toys:

- **(n,t)=(5,3):** domain 20 masks, **min depth = 6 > n** — **strictly worse** than **n** coordinate reads.
- **(n,t)=(6,4):** domain 35 masks, **min depth = 6 = n** — **no** **improvement** over coordinate worst case on this instance.

**(10,6)** not computed (too heavy). The optimistic **depth < n−1** claim for the full toy is **unsupported**; small instances show AND-only trees **do not** **sharpen** **045** **and** **can** **cost** **more** **than** **n** **rounds.**

## Implications

- **Digest** **`verifier-oracle-model`:** extend **oracle** thread: **pairwise** **AND** **is** **not** **a** **cheap** **drop-in** **replacement** **for** **coordinate** **probes** **in** **this** **separation** **problem.**
- **Next:** try **other** **oracle** **alphabets** **(OR,** **parity** **on** **pairs,** **etc.)** **or** **formalize** **query** **cost** **separate** **from** **depth.**

## Analogy pass summary

**Domains:** property testing / Walsh degree-2 monomials; conjunction tests in group testing; nonlinear gate bases in decision trees. **Seed:** AND as **interaction** **probe** **might** **shortcut** **hidden-bit** **arguments** **—** **refuted** **on** **(5,3)/(6,4)** **by** **exact** **search.**
