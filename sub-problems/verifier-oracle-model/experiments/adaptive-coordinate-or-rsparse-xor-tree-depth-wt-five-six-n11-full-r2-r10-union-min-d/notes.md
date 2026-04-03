# Notes

## observation

The parent driver `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-five-six-n11/script.py` was aligned with the `n=12` implementation: **`--union-rs`**, **`--skip-baseline`**, **`--r-single`**, **`--lru-maxsize`**, **`--baseline-only`**, and LRU-capped memo in `min_depth_for_language`. This makes `n=11` a drop-in analogue of the `n=12..14` union-min-d wrappers.

## insight

**`min_d=2`** on the full XOR union now has a certified anchor at **`n=11`** (**2035** splits), so oracle wording can cite **`n∈{11,12,13,14}`** jointly for this structural fact (same majority-relative shell geometry).

## question

Whether **`n=9`** or **`n=10`** admit the same full-union **`min_d`** pattern is open; smaller `n` may need a separate driver port if we continue the ladder downward.
