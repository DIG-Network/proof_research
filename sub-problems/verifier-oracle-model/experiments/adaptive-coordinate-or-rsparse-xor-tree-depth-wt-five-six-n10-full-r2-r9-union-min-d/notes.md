# Notes

## observation

Parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-five-six-n10/script.py` was upgraded to match the `n=11` CLI: **`--union-rs`**, **`--skip-baseline`**, **`--r-single`**, **`--lru-maxsize`**, **`--baseline-only`**, and LRU-capped memo in `min_depth_for_language`.

## insight

**`min_d=2`** on the full XOR union now anchors at **`n=10`** (**1012** splits); oracle narrative can cite **`n∈{10,11,12,13,14}`** jointly.

## question

**`n=9`**, **`{4,5}`** full union (**`r=2..8`**) is the next downward step if the ladder continues.
