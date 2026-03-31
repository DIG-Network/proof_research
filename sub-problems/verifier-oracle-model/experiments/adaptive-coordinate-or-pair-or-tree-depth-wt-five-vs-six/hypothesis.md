# Hypothesis — mixed coordinate + pair-OR depth (n=10, wt {5,6})

## Analogy pass

1. **Abstract structure:** **066** showed that mixing **axis-aligned** probes (**x_i**) with **one** **nonlinear** **2-bit** **probe** (**x_i ⊕ x_j**) can **shrink** **adaptive** **decision** **depth** on a **fixed** **Hamming** **shell** **pair.** **049** **catalogued** **pure** **pair-OR** **vs** **pair-XOR** **on** **several** **(n,T)** **but** **not** **the** **mixed** **coordinate** **+** **OR** **regime** **on** **the** **(10,5/6)** **toy.**

2. **Where else:**
   - **Circuit** **complexity:** **monotone** **gates** **(OR)** **vs** **linear** **(parity/XOR)** **—** **different** **symmetry** **groups.**
   - **Sensor** **fusion:** **binary** **“any** **alarm”** **(OR)** **vs** **single** **bit** **line** **(coordinate)** **vs** **difference** **(XOR).**
   - **Branching** **programs:** **allowed** **predicate** **set** **changes** **reachable** **leaf** **complexity.**

3. **Machinery:** **Same** **memoized** **`exists_tree(S,d)`** **as** **066:** **try** **coordinates** **0..n−1** **then** **pair** **ORs** **(i,j)** **lex;** **child** **recursion** **mirrors** **empty-branch** **short-circuit.**

4. **Transfer candidate:** **If** **`D_{coord∨OR} < 10`** **(coordinate-only** **045)** **then** **OR** **helps** **like** **XOR** **in** **066;** **if** **`D ≥ 10`** **or** **much** **worse** **than** **066’s** **5,** **we** **learn** **OR’s** **adaptive** **power** **on** **this** **shell** **pair** **is** **weak** **relative** **to** **XOR** **under** **this** **tie-break.**

## Falsifiable claim

For **n=10** and domain **popcount ∈ {5,6},** **there** **exists** **a** **perfect** **separator** **tree** **with** **internal** **nodes** **x_i** **or** **(x_i ∨ x_j).** **Primary:** **the** **script** **prints** **the** **minimum** **depth** **d** **(** **or** **FAIL** **up** **to** **n** **).** **Secondary** **(** **partial** **):** **certify** **small** **d** **infeasible** **—** **the** **memoized** **DP** **for** **pair-OR** **fans** **out** **far** **more** **than** **066’s** **XOR** **mix,** **so** **full** **min-d** **may** **need** **a** **large** **time** **budget** **or** **compiled** **search** **(** **script** **supports** **`--budget-seconds`** **/** **`--d-min`** **).**

## Outcome (certified)

**PASS** **—** **exact** **minimum** **depth** **=** **10.** **Exhaustive** **DP** **rules** **out** **d** **≤** **9;** **045** **+** **language** **monotonicity** **(** **coord** **⊂** **mixed** **)** **gives** **feasibility** **at** **d** **=** **10.** **See** **`results.md`.**
