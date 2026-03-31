# Results: elementary-symmetric-adjacent-mod-collision

## Outcome

**PASS**

## Identity (Pascal)

For integers **t ≥ d ≥ 1:**

**C(t,d) − C(t−1,d) = C(t−1, d−1).**

**Corollary** **(modular** **threshold** **toy):** **If** **the** **verifier** **only** **sees** **e_d(S) = C(|S|,d)** **mod** **M,** **then** **values** **for** **|S|=t−1** **and** **|S|=t** **agree** **mod** **M** **iff** **M** **divides** **C(t−1,d−1).**

## Checks

- **Brute** **equality** **for** **t** **∈** **[2,39),** **d** **∈** **[1,** **min(t,15)].**
- **Regression:** **d=2** **gives** **C(t−1,1)=t−1** **(matches** **046).**

## Example **t=6** **(sizes** **5** **vs** **6)**

| **d** | **Δ = C(t−1,d−1)** | **Nontrivial** **M** **with** **M|Δ** **(≤30)** |
|-------|---------------------|--------------------------------------------------|
| **1** | **1** | **none** |
| **2** | **5** | **5** |
| **3** | **10** | **2,** **5,** **10** |
| **4** | **10** | **2,** **5,** **10** |
| **5** | **5** | **5** |
| **6** | **1** | **none** |

## Interpretation

**Any** **fixed** **unweighted** **degree-d** **symmetric** **summary** **of** **|S|,** **reduced** **mod** **M,** **has** **a** **clean** **arithmetic** **characterization** **of** **when** **it** **fails** **to** **separate** **t−1** **vs** **t** **signers** **—** **still** **not** **`Link`,** **but** **a** **single** **family** **subsuming** **046.**
