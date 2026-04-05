# Hypothesis — off-diagonal `|∩|∈{0,1}`: symmetric difference only (`n=7`)

## Abstract structure

Same **`22050`** grid: **coord + full `r=2` + two `r=3` XOR splits (`i<j`) + one `r=4` XOR split `Q`**. Prior work falsified a **global** patchwork that used **`Q = symdiff(T_i,T_j)`** for **`s∈{0,1}`** together with a wedge rule for **`s=2`** (**`…-offdiag-patchwork-inter012-template`**, FAIL). A **narrower** test (**`…-offdiag-symmetric-diff-predicate`**) required **`s=1`** only and also failed.

**Claim under test (new stratum):** Restrict to **`i<j`** with **`s = |T_i ∩ T_j| ∈ {0,1}`** ( **`13475`** cells: **`315×35`** for **`s=1`**, **`70×35`** for **`s=0`** ). Within this union stratum,

> **`min_d = 2`  ⇔  `Q_mask = T_i ⊕ T_j`** (as 7-bit masks; equality is only possible when **`popc(symdiff)=4`**, hence **`s=1`**).

For **`s=0`**, **`symdiff`** has **six** bits so **`Q` (a 4-set) can never equal it**; the biconditional predicts **no** **`min_d=2`** witnesses on the **`s=0`** sub-stratum. Any observed **`min_d=2`** with **`s=0`** falsifies the hypothesis immediately.

## Analogy pass

1. **Abstract structure:** On a **stratified finite fiber**, test whether a **single algebraic template** (**XOR of two 3-sets**) **exactly** coincides with a **computational depth** threshold (**`min_d=2`**) after **isolating** an **intersection-size** regime.

2. **Where else:** (i) **Syndrome decoding** — **error pattern** as **symmetric difference** of **supports**. (ii) **Boolean analysis** — **parity / XOR** as **canonical** combination of **sparse** literals. (iii) **Matroid** **circuit** **exchange** — **symmetric difference** of **dependent** **3-sets** **tracks** **overlap** **geometry**.

3. **Machinery:** **Finite** **enumeration**; **bitmask** **equality**; **cardinality** **obstructions** (**`s=0`** **vs** **4-subset** **`Q`**).

4. **Transfer candidate:** **Patchwork** **already** **suggested** **`symdiff`** **for** **`s∈{0,1}`** **globally** **failed** **when** **glued** **to** **`s=2`** **wedge** — **test** **the** **`s∈{0,1}`** **piece** **in** **isolation** **as** **a** **standalone** **biconditional**.

## Memory / prior-art in-repo

- **FAIL:** **`…-offdiag-patchwork-inter012-template`** — **full-grid** **patchwork** **not** **`min_d=2`** **biconditional**; **includes** **`s=2`** **wedge** **branch**.
- **FAIL:** **`…-offdiag-symmetric-diff-predicate`** — **`s=1` ∧ Q=symdiff** **does** **not** **match** **all** **`min_d=2`** **off-diagonal** **(** **`|∩|=2`** **counterexamples** **)** **and** **has** **false** **positives** **`md=3`**.
- **PASS:** **`…-structure-scan`** — **off-diagonal** **`min_d=2`** **count** **`1190`** **on** **full** **grid**.

## Falsifiable statement

Exhaust **`i<j`**, **`s∈{0,1}`**, all **`k`**. Let **`D = T_i ⊕ T_j`**. Report:

- **`min_d=2`** **but** **`Q≠D`**
- **`Q=D`** **but** **`min_d≠2`**

Nonempty **either** **side** **⇒** **FAIL**. **Additionally**, any **`min_d=2`** **with** **`s=0`** **⇒** **FAIL** **(** **immediate** **)**.
