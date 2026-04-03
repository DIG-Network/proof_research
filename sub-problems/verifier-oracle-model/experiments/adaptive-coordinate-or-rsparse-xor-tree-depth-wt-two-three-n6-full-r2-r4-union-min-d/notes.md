# Notes

## observation

For **`n=6`**, shells **`{2,3}`** (**`C(6,2)+C(6,3)=35`**) align with the same weight pattern as **`n=7`**; union **`r=2..4`** is the natural **`n-2`** cap (**`r=5`** would be full parity on 6 bits and is excluded from the sparse XOR menu).

## insight

The ladder now supports citing **`n∈{6,…,14}`** for **`min_d=2`** on **`coord + ⋃_{r=2}^{n-2} XOR_r`** for these shell families (with **`n=6`** using **`{2,3}`** only).

## question

Whether **`n=5`** with **`{2}`** only (**`C(5,2)=10`**) still admits **`min_d=2`** on **`r=2..3`** is the next downward step if the narrative needs **`n≥5`**.
