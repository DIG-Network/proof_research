# Notes — r=9 random XOR 400×3 (seeds 6, 7, 8)

- **Symmetry:** Completes a natural triple alongside `seeds012` on the same `C(14,9)=2002` index space; `r=5` already had `seeds012` and `seeds345`.
- **Pattern:** Every run hit **exactly** **8M** LRU misses after the `d=3` probe — same cap behavior as prior `r=9` random and shard negatives.
- **Scope:** Six independent random 400-menus for `r=9` (`{0,1,2}` + `{6,7,8}`) still do not establish full-menu infeasibility; they only strengthen the **small-menu** negative evidence band around parity-hard `r=9`.
