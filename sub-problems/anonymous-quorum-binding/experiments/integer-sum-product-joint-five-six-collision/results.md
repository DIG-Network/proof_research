# Results — exact integer (Σw, Πw), 5-shell vs 6-shell

## Outcome: **PASS**

- **Cross-shell** **key** **collisions** **(same** **integer** **sum** **and** **product** **of** **w_i=i+1):** **37** **pairs** **(5-set,** **6-set).**
- **Sample** **key:** **sum=27,** **prod=1680**
  - **5-set** **indices** **(0,4,5,6,7)** **→** **weights** **(1,5,6,7,8)**
  - **6-set** **indices** **(0,1,2,3,6,9)** **→** **weights** **(1,2,3,4,7,10)**

## Corollary (same argument as **062**)

Matching **integer** **sum** **and** **product** **⇒** **matching** **(Σ mod M,** **Π mod M)** **for** **every** **M** **≥** **2.** **So** **this** **joint** **tag** **cannot** **separate** **the** **two** **shells** **via** **modular** **compression** **either.**

## Script

`script.py` **—** **prints** **`COLLISION_COUNT`** **and** **one** **witness,** **then** **`PASS`.**
