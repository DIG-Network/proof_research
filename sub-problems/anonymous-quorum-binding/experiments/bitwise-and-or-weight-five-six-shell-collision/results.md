# Outcome: **PASS**

## Hypothesis

**Cross-shell** **collisions** **exist** **for** **both** **integer** **bitwise** **AND** **and** **OR** **of** **public** **weights** **w_i=i+1** **over** **S** **(** **n=10,** **|S|∈{5,6}** **).**

## Counts

| Summary | Distinct values on \|S\|=5 | Distinct on \|S\|=6 | Shared values (5∩6) |
|---------|---------------------------|---------------------|----------------------|
| **h_and** | 3 | 1 | **1** |
| **h_or** | 5 | 3 | **3** |

## Witnesses

- **h_and:** **value** **0** **—** **5-set** **indices** **(0,1,2,3,4)** **(** **weights** **1..5** **):** **1** **&** **2** **=** **0** **⇒** **full** **AND** **is** **0.** **6-set** **(0..5)** **(** **weights** **1..6** **)** **also** **AND** **to** **0** **(** **same** **reason** **).**
- **h_or:** **value** **7** **—** **same** **index** **pairs** **as** **above** **(** **5-set** **OR** **=** **7,** **6-set** **OR** **=** **7** **).**

**Interpretation:** **Neither** **h_and** **nor** **h_or** **can** **serve** **as** **a** **standalone** **anonymous** **threshold** **certificate** **on** **this** **toy** **(** **same** **morals** **as** **034** **/** **050** **/** **061** **)** **—** **idempotent** **bit** **folding** **collapses** **across** **the** **5** **vs** **6** **shell** **boundary.**

## Script

`python script.py` **→** **exit** **0,** **prints** **PASS.**
