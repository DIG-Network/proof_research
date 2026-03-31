# 2026-03-30 — mixed-coordinate-xor-tree-witness-xor-first-wt-five-vs-six

- **Experiment:** `sub-problems/verifier-oracle-model/experiments/mixed-coordinate-xor-tree-witness-xor-first-wt-five-vs-six/`
- **Context:** verifier-oracle-model (**alternate** **tie-break** **after** **067** **/** **digest** **hint** **).

## Hypothesis tested

**Same** **feasibility** **as** **066,** **but** **emit** **a** **witness** **by** **scanning** **pair-XOR** **splits** **before** **coordinate** **splits** **at** **each** **node** **—** **expect** **either** **a** **different** **plan** **or** **documented** **collapse** **to** **067.**

## Outcome: **PASS**

**Depth-5** **witness** **valid** **(** **leaf** **sum** **462** **).** **Byte-identical** **JSON** **tree** **to** **067** **(** **`fc` / `fc.exe`** **on** **exported** **bodies** **).**

## Key finding

**On** **(n=10,** **wt{5,6}),** **XOR-first** **vs** **coord-first** **witness** **construction** **does** **not** **change** **π_tree:** **first** **feasible** **structure** **is** **the** **same** **(** **all-XOR** **internals,** **31** **nodes** **).**

## Implications

- **Tie-break** **sensitivity** **must** **be** **tested** **on** **instances** **where** **multiple** **root** **splits** **are** **simultaneously** **feasible** **—** **not** **assumed** **from** **this** **toy** **alone.**
- **Erratum** **(** **067** **):** **`exists_tree`** **must** **call** **`recurse_children(..., depth_remaining)`** **not** **`depth_remaining-1`** **(** **see** **067** **`notes.md`** **).**

## Analogy pass summary

**Alternate** **PV** **in** **games** **/** **SAT** **heuristics** **—** **implemented;** **observed** **degeneracy** **(** **same** **line** **)** **on** **this** **position.**
