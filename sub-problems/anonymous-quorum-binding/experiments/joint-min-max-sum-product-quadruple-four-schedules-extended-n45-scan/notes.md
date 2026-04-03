# Notes — joint-min-max-sum-product-quadruple-four-schedules-extended-n45-scan

## observation

- **Triangular** schedule **`w_i = (i+1)(i+2)/2`** first exhibits a **5-vs-6** cross-shell collision on exact **`K=(min,max,Σ,Π)`** at **`n=36`** (witness in **`results.md`**).

## observation

- **`2^i`**, **Fibonacci prefix**, and **first-`n` primes** remain **collision-free** on **`K`** for **5** vs **6** for every **`n` from 11 through 45** in this exhaustive scan.

## insight

- **Ordering** of **onset** (among schedules probed so far on this **`K`**): **linear** **`i+1`** fails at **`n=11`** (**097**); **squares** at **`n=31`** (**099**); **triangular** at **`n=36`** (**101**); **pow2 / Fib / primes** still **open** beyond **`n=45`**.

## question

- At what **`n`** (if any) do **`2^i`**, **Fibonacci**, or **primes** first collide? **Runtime** grows roughly as **`C(n,5)+C(n,6)`** per **`n`**; **`n=50`** is the next natural band if compute allows.

## dead_end

- None for the **sub-problem** as a whole; this experiment **refines** the **toy** **schedule** landscape only.
