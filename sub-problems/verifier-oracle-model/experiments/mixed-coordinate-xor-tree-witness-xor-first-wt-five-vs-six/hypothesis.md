# Hypothesis — XOR-first witness for mixed coord + pair-XOR (n=10, wt {5,6})

## Analogy pass

1. **Abstract structure:** **067** **printed** **one** **depth-5** **witness** **using** **the** **same** **split** **priority** **as** **066’s** **existential** **DP** **(** **coordinates** **before** **pair-XOR** **).** **Tie-breaking** **is** **arbitrary** **once** **many** **splits** **are** **feasible** **—** **like** **choosing** **a** **principal** **variation** **in** **game** **trees** **vs** **an** **alternate** **line** **that** **still** **refutes** **the** **opponent.**

2. **Where else:**
   - **Chess** **/** **Go** **PV** **vs** **secondary** **variations** **at** **the** **root.**
   - **SAT** **solvers:** **first** **decision** **heuristic** **vs** **model** **rotation.**
   - **Compiler** **codegen:** **instruction** **selection** **order** **when** **multiple** **patterns** **match.**

3. **Machinery:** **Keep** **`exists_tree`** **identical** **to** **066** **(** **coord** **then** **XOR** **—** **canonical** **feasibility** **).** **Define** **`witness_xor_first(S,d)`** **that** **scans** **all** **pair-XOR** **splits** **(** **lex** **(i,j)** **)** **before** **any** **coordinate** **split,** **still** **gating** **on** **`exists_tree`** **children.**

4. **Transfer candidate:** **If** **a** **valid** **witness** **emerges** **with** **different** **root** **/** **gate** **mix** **than** **067,** **PASS** **—** **proves** **π** **representation** **is** **not** **unique** **and** **tie-break** **affects** **audited** **query** **plans** **even** **when** **D_min** **is** **fixed.**

## Falsifiable claim

**There** **exists** **a** **depth-≤5** **feasible** **witness** **under** **XOR-first** **principal-variation** **order** **that** **differs** **(** **e.g.** **root** **gate** **type** **or** **JSON** **shape** **)** **from** **067’s** **coord-first** **witness,** **or** **the** **first** **feasible** **split** **coincides** **(** **document** **sameness** **).**
