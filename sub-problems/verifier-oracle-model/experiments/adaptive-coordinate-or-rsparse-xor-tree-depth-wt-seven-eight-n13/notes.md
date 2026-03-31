# Notes

- **Domain** **growth** **:** **3003** **masks** **vs** **1716** **for** **`(12,{6,7})`** **—** **coord-only** **DP** **to** **`d=13`** **completed** **in** **~31** **s** **wall** **here** **(** **acceptable** **for** **baseline** **)** **.**

- **Parity** **:** **Full** **13-XOR** **still** **gives** **`min_d=1`**, **consistent** **with** **094** **/** **`n=12`** **baseline** **.**

- **Next** **:** **Single-arity** **`r`** **sweep** **should** **use** **fresh** **processes** **per** **`r`** **(** **`--skip-baseline`**) **—** **mirror** **`n=12`** **shard** **pattern** **for** **large** **`C(13,r)`** **(** **e.g.** **`r=6,7`** **have** **1716** **splits** **each** **)** **.**
