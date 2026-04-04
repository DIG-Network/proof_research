# Notes

## observation

`min_d` for `coord + ⋃_{r=2}^{3} XOR_r` on `{2,3}` shell is **2** with 20 splits; dropping to **only `r=2`** moves `min_d` to **3** (10 splits).

## insight

**Generator minimality for XOR arity:** In this shell, depth-2 is not achievable from coordinate + **pair** XOR alone; **triple** XOR is a necessary ingredient in the union that achieved `min_d=2`.

## question

For the same shell, is there any **strict subset** of the 10 `r=3` splits that still achieves `min_d=2` with all `r=2` splits? (Not run here — would be a larger combinatorial search.)

## dead_end

None for this experiment (hypothesis was cleanly falsified).
