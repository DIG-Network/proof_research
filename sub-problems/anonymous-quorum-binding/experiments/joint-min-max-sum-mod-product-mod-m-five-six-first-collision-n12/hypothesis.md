# Hypothesis: joint mod fold at n=12 (extension of 094)

## Context

Experiment **094** (`joint-min-max-sum-mod-product-mod-m-five-six-first-collision`) for **`n=10`**, **`w_i=i+1`**, shells **|S|∈{5,6}**, key  
`K_M(S) = (min w, max w, (Σ w) mod M, (Π w) mod M)`  
found **first** 5-vs-6 cross-shell collision at **`M=2`**.

Session follow-up: stress **larger universe** **`n=12`** (indices `0..11`, weights `1..12`) with the **same** tag and scan order.

## Analogy pass (mandatory)

1. **Abstract structure:** Coarse quotient map on a union of fixed-size shells; **first** modulus where two shells share a key. Scaling **n** changes shell cardinalities and weight range but **parity** of sum/product mod 2 may remain the dominant **first** gluing mechanism.

2. **Analogous domains:** (i) **Coarse graining** in statistical mechanics — when does binning first merge two macrostates? (ii) **Image compression** — when does downsampling first alias two textures? (iii) **Modular coding** — when does the **smallest** modulus in a family first create a cross-codebook collision?

3. **Machinery:** First-hit scans over **M**, **2-adic** / parity reasoning for **M=2**, counting arguments for when **M=2** is unavoidable vs escapable.

4. **Transfer candidate:** For **linear** weights **`1..n`**, **M=2** often collapses **Σ** and **Π** to **parity** classes; **extrema** `(min,max)` are still exact integers. Expect **first collision** may remain **`M=2`** if a 5-set and 6-set can match **(min,max)** and both **odd Σ mod 2** and **even Π mod 2** (or analogous parity pattern). **Falsifiable** by scan finding **first_hit_M > 2**.

## Falsifiable claim

**H:** For **`n=12`**, **`w_i=i+1`**, shells **5** and **6**, the **smallest** integer **`M≥2`** such that some 5-subset and some 6-subset share the same **`K_M`** is **`M=2`**.

If the lex scan finds **first collision at M>2**, **H** is **FAIL**. If **first is M=2**, **H** is **PASS**.

## Parent

Extends **094** (same statistic, **n=10**); same family as **093** (exact quadruple at n=10) in spirit — here **n** is increased only for the **modular** joint tag.
