# Notes — quadruple `r=3` scan at n=7

## observation

- Baselines match prior wrappers: `coord_only min_d=7`, `coord_plus_full_xor min_d=1`.

## dead_end

- **Four** independent **`r=3`** parities on top of **full `r=2`** still **do not** yield **`min_d=2`** at **n=7** — **`0/52360`** witnesses.

## question

- Does **five** triples (or mixing **`r=4`** sparse XOR) ever hit **`min_d=2`** before resorting to the **full multi-arity union** (**`r=2..5`**, **112** splits)? **Combinatorics** blow up fast (**`C(35,5)=324632`**).

## analogy

- **Rank / parity-check** intuition: the **`n=7`** shell separation may require **more** than **four** triple-parity “views” **or** **higher**-arity XOR—not just **more** copies of the **same** arity.
