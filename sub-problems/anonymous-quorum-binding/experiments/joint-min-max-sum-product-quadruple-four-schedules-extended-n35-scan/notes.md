# Notes — joint-min-max-sum-product-quadruple-four-schedules-extended-n35-scan

## observation

Runtime ~40s for full scan on this host; dominant cost is **`n=35`** shells (**`C(35,5)+C(35,6)`** key inserts per schedule).

## insight

**Product** coordinate **`Π w`** grows extremely fast for **`2^i`** and **primes**; **Fibonacci** and **triangular** are milder but still yielded **no** cross-shell key overlap through **`n=35`**. This contrasts **099** (**squares**, collision at **`31`**) and **097** (**linear**, **`11`**).

## question

Does **`pow2`** or **primes** ever admit a 5-vs-6 collision on this **`K`**, and at which minimal **`n > 35`**? **Brute force** may need a larger **`n_hi`** or a smarter search if **`n*`** is large.

## dead_end

None identified for the **weight-schedule** family as a whole — only **negative** evidence in **`[11,35]`**.
