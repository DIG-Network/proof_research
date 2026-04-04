# Hypothesis — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-quintuple-r3-random-sample-200`

## Analogy pass

1. **Abstract structure:** We probe whether adding a **fifth** independent `r=3` XOR parity to **coord + full `r=2`** can ever yield **`min_d=2`** at **n=7**, **`{2,3}`**. This is a finite “constraint rank” question: does five triple-parities suffice for a depth-2 certificate when four did not (exhaustive **`C(35,4)`**)?

2. **Where else this structure appears:**
   - **Linear algebra over GF(2):** parity splits are affine halfspaces; depth is a certificate complexity measure.
   - **Group testing / covering:** each split is a test; we ask whether a small test battery can identify a structured subset.
   - **Boolean function complexity:** majority-like slices may require increasing “parity depth” as ambient dimension grows.

3. **Machinery in those domains:** rank / dimension arguments; random sampling as a cheap probe before exhaustive enumeration over **`C(35,5)=324632`** five-tuples.

4. **Transfer seed:** If **random** **`200`** five-tuples find **any** **`min_d=2`**, that motivates targeted / exhaustive **`C(35,5)`** search. If **none**, it is **evidence** (not proof) that the **`min_d=3`** obstruction may persist at arity **5** as well.

## Falsifiable claim

Among **200** uniformly random **unordered** **5-tuples** of triple indices **`0..34`**, **at least one** yields **`min_d=2`** for **coord + full `r=2` + those five `r=3` XOR splits**.

**Opposite outcome:** **all 200** sampled five-tuples have **`min_d=3`** (`witness_min_d2_count=0`).
