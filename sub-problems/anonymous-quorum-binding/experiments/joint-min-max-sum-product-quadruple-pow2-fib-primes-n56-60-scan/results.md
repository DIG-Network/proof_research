# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n56-60-scan

**Outcome:** **FAIL** (hypothesis falsified)

**Setup:** Same as **101**–**103**: exact **`K(S) = (min w, max w, Σ w, Π w)`** on subset weights; shells **|S|=5** vs **|S|=6**; schedules **`pow2_2^i`**, **Fibonacci prefix**, **first `n` primes**; scan **`n ∈ [56,60]`** inclusive.

**Finding:** For **each** schedule, **no** cross-shell collision occurs for **any** **`n`** in **`[56,60]`**.

**Combined band (101 + 102 + 103 + this run):** **No** 5-vs-6 collision under exact **`K`** for these three schedules for **any** **`n ∈ [11,60]`**.

**Script output (verbatim):**

```
schedule='pow2_2^i' first_collision_n_in_[56,60]=NONE
schedule='fibonacci' first_collision_n_in_[56,60]=NONE
schedule='first_n_primes' first_collision_n_in_[56,60]=NONE
scan_range_n=[56,60] schedules=3
FAIL_no_schedule_collides_in_n56_to_60
FAIL
```

**Runtime note:** Wall time ~**9.4 minutes** on this host (dominated by **`C(n,6)`** growth at **`n≈60`**).
