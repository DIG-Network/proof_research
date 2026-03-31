# Results: partial-view-z-interval-formula-regression

## Outcome

**PASS**

## Closed form (fixed **n**, **k** = **|Q|**, **R** = **n** − **k**)

Let **z** **∈** **{0,…,k}** **be** **the** **number** **of** **ones** **on** **Q.** **A** **completion** **with** **total** **Hamming** **weight** **w** **exists** **iff**

**max(0,** **w** **−** **R)** **≤** **z** **≤** **min(k,** **w).**

Write **I(w)** **=** **that** **integer** **interval** **∩** **[0,k].**

For **the** **pair** **wt** **=** **t** **−** **1** **vs** **wt** **=** **t** **(prior** **experiments** **t** **=** **6):**

| **Cell** | **Condition** **on** **z** |
|----------|----------------------------|
| **both** | **z** **∈** **I(t−1)** **∩** **I(t)** |
| **only_wt5** | **z** **∈** **I(t−1)** **\** **I(t)** |
| **only_wt6** | **z** **∈** **I(t)** **\** **I(t−1)** |
| **neither** | **z** **outside** **I(t−1)** **∪** **I(t)** |

**Per** **fixed** **Q:** **#patterns** **in** **cell** **=** **Σ_{z** **in** **cell}** **C(k,z)** **(sums** **to** **2^k).**

**Global** **(all** **Q,** **all** **p):** **multiply** **each** **per**-**Q** **count** **by** **C(n,k).**

## Checks run

- **Per**-**Q** **weights** **sum** **to** **2^k** **for** **(10,6,6)** **and** **(10,9,6).**
- **Global** **formula** **=** **brute** **for** **(10,6,k),** **k** **=** **4…9** **(journal** **037–042).**
- **Spot** **(n,k,t):** **(7,3,4),** **(8,5,5),** **(12,6,7),** **(15,10,8),** **(6,2,3),** **(9,9,5).**

## Interpretation

**The** **coordinate**-**probe** **“z**-**band”** **classification** **is** **a** **pure** **counting** **identity;** **future** **oracle**-**model** **notes** **can** **cite** **this** **file** **instead** **of** **re**-**enumerating** **small** **cases.**
