# Notes: joint-min-max-sum-mod-product-mod-m-five-six-first-collision-n12

## observation

First cross-shell collision again at **M=2** with key **`(1,6,1,0)`** — same witness indices as **094** on the embedded **`n=10`** prefix; larger **`n=12`** universe does not change the lex-first hit.

## insight

The collision is supported entirely inside **`{0,…,5}`**; extra validators **`6..11`** are irrelevant for this **first-`M`** statistic — any extension of the weight line preserves the same minimal **parity** obstruction once **(min,max)=(1,6)** is feasible for both shell sizes.

## dead_end

Not applicable (PASS).

## question

Whether **exact** `(min,max,Σ,Π)` stays injective on **C(12,5)∪C(12,6)** for **`w_i=i+1`** is **not** tested here (093 was **n=10** only).
