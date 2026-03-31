# Outcome: **PASS**

## Claim

For **n=10,** **w_i=i+1,** **both** **joint** **fingerprints**

- **K_and(S)** **=** **(h_and(S),** **Σ_{i∈S}** **w_i),**
- **K_or(S)** **=** **(h_or(S),** **Σ_{i∈S}** **w_i)**

**(** **exact** **integers** **)** **have** **cross-shell** **collisions:** **some** **|S|=5** **and** **|S|=6** **share** **the** **same** **tuple.**

## Counts

| Joint key | Distinct on \|S\|=5 | Distinct on \|S\|=6 | Cross-shell shared keys |
|-----------|----------------------|----------------------|-------------------------|
| **K_and** | 28 | 25 | **20** |
| **K_or** | 42 | 31 | **23** |

## Sample witnesses

- **K_and** **=** **(0,** **21):** **5-set** **indices** **(0,1,2,4,9)** **(** **weights** **1,2,3,5,10** **),** **6-set** **(0,1,2,3,4,5)** **(** **1..6** **).** **Both** **AND** **→** **0,** **sum** **21.**
- **K_or** **=** **(7,** **21):** **5-set** **(0,1,4,5,6)** **(** **1,2,5,6,7** **),** **same** **6-set** **as** **above.** **OR** **=** **7,** **sum** **21.**

## Corollary (**062** **pattern**)

**For** **any** **M** **≥** **2,** **(** **h_*,** **Σw** **mod** **M** **)** **agrees** **on** **those** **witness** **pairs** **(** **same** **integer** **sum** **⇒** **same** **residue** **mod** **M** **;** **same** **h_*** **).** **So** **this** **joint** **does** **not** **repair** **shell** **separation** **by** **adding** **modular** **sum** **on** **top** **of** **087.**

## Script

`python script.py` **→** **exit** **0,** **PASS.**
