# Results: pair-count-mod-m-threshold-collision

## Outcome

**PASS**

## Statistic

**h(S)** **=** **|{(i,j):** **i<j,** **i,j∈S}|** **=** **C(|S|,** **2)** **=** **|S|(|S|−1)/2.**

Depends **only** **on** **|S|** **(not** **which** **signers)** **for** **unweighted** **pairs.**

## Identity

For **t** **≥** **2:**

**C(t,2)** **−** **C(t−1,2)** **=** **t** **−** **1.**

**Proof** **sketch:** **t(t−1)/2** **−** **(t−1)(t−2)/2** **=** **(t−1)/2** **·** **(t** **−** **(t−2))** **=** **t−1.**

## Modular collision

**C(t−1,2)** **≡** **C(t,2)** **(mod** **M)** **⇔** **M** **|** **(t−1).**

## Exhibit **(t=6)**

| **Quantity** | **Value** |
|--------------|-----------|
| **C(5,2)** | **10** **≡** **0** **(mod** **5)** |
| **C(6,2)** | **15** **≡** **0** **(mod** **5)** |

**Any** **divisor** **M>1** **of** **t−1** **yields** **the** **same** **collision** **for** **sizes** **t−1** **and** **t.**

## Interpretation

**A** **single** **degree-2** **moment** **(pair** **count)** **reduced** **mod** **M** **does** **not** **by** **itself** **certify** **|S|** **≥** **t** **when** **M** **|** **(t−1)** **—** **parallel** **to** **034/035** **for** **linear** **summaries.**
