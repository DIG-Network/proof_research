# Analogy pass

## 1. Abstract structure

A **verifier-visible** **fingerprint** maps each signing subset **S** to a **small** **tuple** **(** **order** **statistics** **+** **one** **additive** **aggregate** **)** **of** **public** **weights** **`w_i`**. **Threshold** **soundness** **would** **require** **disjoint** **images** **for** **`|S|=t−1`** **vs** **`|S|=t`**.

## 2. Analogues (≥3)

1. **Sufficient** **statistics** **—** **(min,** **max,** **mean)** **compress** **a** **sample** **but** **lose** **threshold** **information** **unless** **the** **model** **is** **regular** **.**

2. **063** **(Σw,** **Πw)** **—** **two** **scalar** **summaries** **already** **collide** **across** **5** **/** **6** **shells** **.**

3. **087–088** **bitwise** **AND/OR** **—** **non-linear** **integer** **folds** **still** **fail** **shell** **separation** **alone** **or** **joint** **with** **Σw** **.**

## 3. Machinery

**Exhaustive** **`n=10`**, **`w_i=i+1`**, **shells** **5** **and** **6** **:** **key** **`K(S)=(min_{i∈S}w_i,` `max_{i∈S}w_i,` `Σ_{i∈S}w_i)`** **in** **ℤ³** **.** **Then** **`K_M=(min,` `max,` `Σ mod M)`** **for** **`M=2,3,…`** **until** **first** **cross-shell** **collision** **.**

## 4. Transfer seed

**Order** **statistics** **are** **natural** **“encoding** **change”** **from** **pure** **sums** **/** **products** **;** **if** **even** **`(min,max,Σ)`** **collides** **,** **ultrametric-style** **certificates** **based** **only** **on** **extrema+mass** **are** **ruled** **out** **for** **this** **toy** **.**

---

# Formal hypothesis

**H1:** **There** **exist** **5-set** **`S`** **and** **6-set** **`T`** **with** **identical** **`K(S)=K(T)`** **(** **exact** **integers** **)** **.**

**H2:** **The** **smallest** **`M≥2`** **such** **that** **`K_M`** **has** **a** **cross-shell** **collision** **satisfies** **`M`** **≤** **20** **(** **explicit** **scan** **)** **.**

**Falsification:** **No** **exact** **collision** **(** **unexpected** **)** **;** **or** **script** **error** **.**

---

# Outcome (post-run)

**PASS** — **41** **exact** **cross-shell** **keys** **`K=(min,max,Σw)`** **;** **first** **`K_M`** **collision** **at** **`M=2`** **(** **25** **shared** **`K_2`** **keys** **).**
