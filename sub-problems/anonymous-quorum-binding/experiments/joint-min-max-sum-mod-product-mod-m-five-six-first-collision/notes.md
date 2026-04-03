# Notes

- **observation:** At `M=2`, `Σ mod 2` is parity of subset size (here 5 vs 6 are both odd), and `Π mod 2` is parity of the count of even weights in the subset; the witness uses `min=1`, `max=6` and matches both residues across shells.
- **insight:** Exact **093** injectivity is **fragile** under **any** uniform mod fold that identifies odd 5-sets with odd 6-sets on the sum coordinate while allowing product parity to align — **M=2** is the minimal modulus for that phenomenon here.
- **dead_end (for this toy):** Treating `(min,max,Σ mod M,Π mod M)` as a threshold witness without additional **Link** structure does not separate `|S|=5` vs `6` for small `M`; first collision already at **2**.
- **question:** For **larger** `n` or **different** public weights, does the **first** collision modulus for this quadruple fold ever exceed **2**, or is parity always the first glue?
