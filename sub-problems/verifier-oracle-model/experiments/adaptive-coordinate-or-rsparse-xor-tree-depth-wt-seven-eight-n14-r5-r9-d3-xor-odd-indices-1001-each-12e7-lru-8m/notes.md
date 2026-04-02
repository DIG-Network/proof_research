# Notes

- **Naming:** Experiment folder says `odd-indices`; the actual index set is **even integers** `0,2,…,2000` (1001 entries). "Odd" was meant colloquially as "every other"; prefer "even-step" or "parity interleave" in prose.
- **Comparison:** Wall time per run ~941 s aligns with contiguous half-shard ~927–974 s from `*-12e7-each-lru-8m` experiments — interleaving did not materially shorten the DP.
- **Next:** If continuing witness hunt: try **odd-step** indices `1,3,…,2001` (the other 1001 coset), or a **different** structured 1001-subset (e.g. first/third blocks mod 3); or accept that `12e7/8M` is insufficient for any 1001-cut and need larger host / higher budget / new decomposition.
