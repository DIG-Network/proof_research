# Results — mixed coordinate + pair-XOR decision trees (n=10, wt {5,6})

## Outcome: **PASS**

- **Domain:** **all** **462** **masks** **x∈{0,1}^10** **with** **popcount** **5** **or** **6** **(t=6** **toy:** **one-below-quorum** **vs** **quorum).**
- **Allowed** **internal** **nodes:** **branch** **on** **x_i** **or** **on** **x_i⊕x_j** **(i<j).** **Leaves** **must** **be** **pure** **(single** **weight** **class).**
- **Minimum** **depth** **D_mix** **=** **5** **(** **exhaustive** **memoized** **existence** **test;** **depths** **1–4** **impossible,** **depth** **5** **succeeds** **).**
- **Comparison:** **045** **—** **coordinate-only** **minimum** **depth** **=** **n** **=** **10.** **Mixed** **gates** **cut** **worst-case** **adaptive** **depth** **by** **half** **in** **this** **model.**

## Script

`script.py` **prints** **`min_depth_found`** **and** **`STRICT_IMPROVEMENT`.**
