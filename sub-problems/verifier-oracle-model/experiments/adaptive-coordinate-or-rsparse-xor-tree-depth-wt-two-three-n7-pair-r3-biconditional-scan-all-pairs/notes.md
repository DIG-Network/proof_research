# Notes — n=7 exhaustive two-triple scan

## Combinatorics check

- Disjoint unordered pairs of **3-subsets** of **`[7]`** with **empty** intersection: choose **6** vertices (**`C(7,6)=7`**), then split into two disjoint triples (**`C(6,3)/2 = 10`**). Total **`7×10=70`**, matching **`violations=70`** in the biconditional test (predicate “disjoint ⇒ `min_d=2`” fails on **all** **70**).

## Contrast with n=6

- At **n=6**, **10/190** pairs had **`min_d=2`** (exactly the **10** complementary **3+3** partitions).
- At **n=7**, **extra** ground element: **two** triples can be **disjoint** without **partitioning** **`[7]`** — and **even** those **70** “**6-point**” disjoint pairs **still** sit at **`min_d=3`** here.

## Next steps (for future sessions)

- Characterize **what** **extra** XOR splits (or unions) are needed to recover **`min_d=2`** at **n=7** if at all on this shell.
- Optional: enumerate **`min_d`** distribution for **intersecting** pairs (here uniformly **3**).
