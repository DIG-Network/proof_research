# Notes — joint-min-max-sum-product-quadruple-pow2-fib-primes-n51-55-scan

- **observation:** Hypothesis “at least one of pow2 / Fibonacci / primes collides in `[51,55]`” is **false**; all three schedules remain collision-free on exact **`K`** through **`n=55`** in this scan.
- **observation:** With **101**+**102**, the band **`n∈[11,55]`** is now covered for these three schedules without cross-shell collision.
- **question:** Whether collisions ever appear for **Fibonacci** or **first-n primes** at larger **`n`** is open; **pow2** weights grow so fast that **`Π w`** on 6-subsets may eventually force numerical / key-space behavior worth a separate scaling note.
- **dead_end (local):** Searching only **`[51,55]`** does **not** produce a witness — **negative** evidence only.
