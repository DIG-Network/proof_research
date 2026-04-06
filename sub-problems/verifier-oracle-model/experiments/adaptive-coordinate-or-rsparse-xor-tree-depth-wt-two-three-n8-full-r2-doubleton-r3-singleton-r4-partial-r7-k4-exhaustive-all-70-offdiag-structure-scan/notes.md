# Notes

- **Observation:** Saturation is **independent** of *which* four `r=7` splits are kept—all **70** choices give the same **`107800`** depth-2 count on the stratum.
- **Implication:** For this shell, **`K=4`** is already past any hypothetical “subcritical” window for `r=7`; the next structural knob is **`K∈{1,2,3}`** exhaustive scans or **partial** `r=5` / `r=6` submenus (session-state already flagged).
- **Performance:** Per-menu wall times **~14–32 s** (variance likely cache / LRU locality); full **70** menus **~1233 s** total on this host.
- **Dead end (local):** Searching for **`0 < stratum_min_d2 < 107800`** inside **exhaustive** **`K=4`** `r=7` submenus — **ruled out** (finite proof).
