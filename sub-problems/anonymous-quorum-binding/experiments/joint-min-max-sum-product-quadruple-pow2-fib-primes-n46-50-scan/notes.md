# Notes — joint-min-max-sum-product-quadruple-pow2-fib-primes-n46-50-scan

## observation

Runtime dominated by **`n=50`** (**`C(50,5)`** keys, **`C(50,6)`** six-set checks); full run ~**2.6** minutes in this environment.

## observation

**`n=50`** for **`pow2_2^i`** uses weights up to **`2^49`**; **Python** **int** **product** in **`quad`** is feasible but **heavy** — still completed without overflow issues.

## insight

Together with **101**, these three schedules show **no** **`K=(min,max,sum,product)`** 5-vs-6 collision for **every** **`n` from 11 through 50** (exhaustive per **`n`** in each scanned band).

## question

Does **any** of **`2^i`**, **Fibonacci**, **primes** ever admit such a collision at **some** **`n>50`**, or is there a **structural** reason for long-run separation (unclear from toy scan alone)?

## next steps

- Optional **`n=51..55`** continuation if shell-toy line stays active.
- **Verifier-oracle-model** track is independent (**session-state**).
