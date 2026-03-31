# Results — `pair-binary-gate-complement-two-bit-invariance`

**Outcome:** **PASS**

## Checked property

For gate \(f:\{0,1\}^2\to\{0,1\}\): **two-bit complement invariance** means
\(\forall a,b\in\{0,1\}:\ f(a,b)=f(1-a,1-b)\).

## Exhaustive outcomes (script stdout)

| Gate | Invariant under \((a,b)\mapsto(1-a,1-b)\) |
|------|------------------------------------------|
| AND  | False |
| OR   | False |
| XOR  | True |
| XNOR | True |
| NAND | False |
| NOR  | False |

## Reasoning

**H1 (among AND/OR/XOR/XNOR):** **Confirmed.** XOR and XNOR satisfy the property; AND and OR do not.

**H2 (trees of XOR/XNOR-only pair nodes):** **Confirmed** as a direct consequence: under global \(x\mapsto x\oplus\mathbf{1}\), every internal probe \(f(x_i,x_j)\) is unchanged, so the root-to-leaf path is identical for \(x\) and \(x\oplus\mathbf{1}\). This is the algebraic core of entry **049** (pair-XOR impossibility when complement swaps the two relevant shells) and aligns with **051**.

NAND/NOR are included only as extra sanity; they are not invariant.

## Artifact

`script.py` — brute force over all \((a,b)\), asserts expected XOR/XNOR vs AND/OR, prints NAND/NOR.
