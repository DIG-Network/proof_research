# Notes

- **insight:** Both collisions follow one **parametric family**. For **`m ∈ {11,12}`**, compare  
  - **5-set** weights **`{1,5,6,8,m}`** (indices **`0,4,5,7,m−1`**), and  
  - **6-set** weights **`{1,2,3,4,10,m}`** (indices **`0,1,2,3,9,m−1`**).  
  Then **`min=1`**, **`max=m`**, **`Σ = 20+m`**, and **`Π = 240m`** on **both** sides (**`1·5·6·8·m = 240m`** and **`1·2·3·4·10·m = 240m`**). This family **cannot** occur at **`n=10`** because **`m ≤ 10`** leaves no room for **`{1,5,6,8,m}`** and **`{1,2,3,4,10,m}`** simultaneously as **distinct** valid templates with **`m=max`**. At **`n=12`**, **`m ∈ {11,12}`** fits.

- **structural:** **093** injectivity at **`n=10`** does **not** imply injectivity at larger **`n`**: enlarging the universe adds new subset patterns that can realize **algebraic** equalities of **`(min,max,Σ,Π)`** across **`|S|=5` vs `6`**.

- **next:** For **`n=12`**, richer exact statistics (**064**/**078** style) or different public weights would be needed if the goal is a **collision-free** joint tag on **`C(12,5)∪C(12,6)`**.
