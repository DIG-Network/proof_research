# Notes

- **observation:** Complementary 1001-index menu `1,3,…,2001` does **not** close `d=3` at `12e7/8M`; same qualitative outcome as `0,2,…,2000`.
- **observation:** `r=9` DP is faster than `r=5` on this menu (~860 s vs ~976 s), consistent with prior `r=9` vs `r=5` asymmetry on full menus.
- **dead_end (local):** Swapping to the odd-start interleaved half of the XOR index list is **not** sufficient to obtain a `d=3` decision at this budget — same as even-start interleave.
- **question:** Does a **larger** `exists_tree` budget or a **larger** host change the outcome for either coset, or is `d=3` genuinely unreachable for these `r` values under this DP?
