# Notes

- **insight:** `min_d=2` tightens the verifier-oracle story for this slice: the “hard” part was **menu completeness** (union of all `r`), not **depth** beyond 2 once the full XOR library is available.
- **observation:** Memory footprint remains modest (~68 MB peak) with `--memo-dict` for this full union at `d≤3`.
- **question:** For other shells or `n`, does full `r=2..n-1` union typically drop `min_d` below prior single-`d` probes, or is `n=14` `{7,8}` special?
