# Notes

- **observation:** **`C(7,2)+C(7,3)+C(7,4)=21+35+35=91`** XOR splits — same total-split count as **`r∈{2,3,5}`** (21+35+21) but a different geometry.
- **insight:** Depth-2 at **`n=7`** does **not** need **five-point** parities when **four-point** parities are available in full; the **`r=5`** rows in the **`r=2..5`** union experiment were **redundant** for **`min_d`** (at least for this DP witness).
- **question:** Minimal **subset** of the **91** splits that still yields **`min_d=2`** (feature selection / hitting set) — not computed here.
