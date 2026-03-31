# Results: adaptive-coordinate-tree-depth-wt-five-vs-six

## Outcome

**PASS**

## Model

- **n = 10,** **domain** **D** **=** **{** **x** **∈** **{0,1}^10** **:** **wt(x)** **∈** **{5,** **6}** **}** **(|D|** **=** **462).**
- **Queries:** **read** **one** **coordinate** **x[i]** **(adaptive** **choice** **of** **i** **may** **depend** **on** **prior** **answers).**
- **Goal:** **leaf** **=** **subset** **of** **D** **with** **constant** **Hamming** **weight** **(correct** **5** **vs** **6** **label).**

## Computed **`exists_tree(D,** **d)`**

| **Max** **depth** **d** | **Perfect** **tree** **exists?** |
|-------------------------|----------------------------------|
| **1 …** **9** | **False** |
| **10** | **True** |

## Proof sketch (matches computation)

- **For** **each** **j** **∈** **[0..9],** **pick** **x** **with** **wt** **5** **and** **y** **=** **x** **⊕** **e_j** **with** **wt** **6** **(flip** **bit** **j).** **Then** **x[i]=y[i]** **for** **all** **i≠j.**
- **Along** **any** **root-to-leaf** **path** **that** **never** **queries** **j,** **x** **and** **y** **give** **identical** **answers** **⇒** **same** **leaf** **⇒** **impure** **leaf** **if** **both** **in** **D.**
- **So** **every** **correct** **tree** **must** **query** **j** **on** **the** **path** **for** **that** **pair;** **adversary** **chooses** **a** **pair** **whose** **distinguished** **index** **is** **queried** **last** **among** **{0..9}** **⇒** **need** **≥** **10** **queries** **worst** **case.**

## Relation to **037**

- **037:** **for** **fixed** **|Q|≤4,** **some** **wt=5** **and** **wt=6** **extensions** **share** **the** **same** **4**-**bit** **projection** **—** **non-adaptive** **collision.**
- **045:** **even** **with** **adaptivity,** **coordinate-only** **queries** **require** **depth** **10** **in** **the** **worst** **case** **to** **separate** **the** **full** **restricted** **domain** **D.**
