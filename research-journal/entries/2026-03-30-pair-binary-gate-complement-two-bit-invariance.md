# 2026-03-30 — `pair-binary-gate-complement-two-bit-invariance`

**Context:** `sub-problems/verifier-oracle-model`  
**Experiment:** `sub-problems/verifier-oracle-model/experiments/pair-binary-gate-complement-two-bit-invariance/`

## Hypothesis tested

Among standard 2-bit gates, only XOR and XNOR are invariant under simultaneous negation of both inputs \(f(a,b)=f(1-a,1-b)\); hence XOR/XNOR-only pair decision trees have identical transcripts under global complement \(x\mapsto x\oplus\mathbf{1}\).

## Outcome

**PASS**

## Key finding

Exhaustive check: AND/OR/NAND/NOR fail; XOR and XNOR pass. This packages the **049** mechanism (global complement fixes every pair-XOR/XNOR answer) as a **finite gate taxonomy**, not only a search artifact.

## Implications

- Treat **XOR** and **XNOR** as the **\(Z_2\)-equivariant** pair alphabet under global complement; **AND/OR** break that symmetry at individual nodes (depth behavior remains separate, per 048/049).
- **Next:** mixed-gate trees or binding joint-mod summary (052 notes).

## Analogy pass summary

**Domains:** Ising \(Z_2\) even observables; common-mode rejection in differential readouts; unate vs binate Boolean classification. **Seed:** classify gates by \((a,b)\mapsto(1-a,1-b)\) orbits.
