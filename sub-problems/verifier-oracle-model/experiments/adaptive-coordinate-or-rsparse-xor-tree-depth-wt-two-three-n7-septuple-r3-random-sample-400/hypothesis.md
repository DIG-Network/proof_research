# Hypothesis — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-septuple-r3-random-sample-400`

## Analogy pass

1. **Abstract structure:** After exhaustive **`C(35,6)`** sextuples yielded **no** **`min_d=2`** witness for **coord + full `r=2` + six `r=3`** XOR splits at **`n=7`**, **`{2,3}`**, the next finite rung is **seven** triple-parities (**`C(35,7)=6724520`** unordered septuples). A **random sample** is a cheap probe before committing **~hours** of wall time to full enumeration.

2. **Where else this structure appears:**
   - **Combinatorial search / rare witnesses:** sample before exhaustive closure when the universe is **O(10⁶)**.
   - **Coding / parity tests:** each split is a linear test; depth-2 feasibility is a structured satisfiability question.
   - **Phase transitions in constraint satisfaction:** adding a seventh independent parity may or may not cross a feasibility threshold—empirics precede proof.

3. **Machinery in those domains:** Monte Carlo witness search; power analysis only after a **positive** hit; if **all** samples fail, exhaustive scan remains the proof obligation (as for quintuples → full **`C(35,5)`**).

4. **Transfer seed:** If **any** of **`400`** random septuples achieves **`min_d=2`**, we have a **constructive** anchor for targeted / full **`C(35,7)`** search. If **none**, we gain **evidence** (not proof) consistent with “**seven** sparse triples still **insufficient**,” analogous to the **six**-tuple closure.

## Falsifiable claim

Among **400** uniformly random **unordered** **7-tuples** of triple indices **`0..34`**, **at least one** yields **`min_d=2`** for **coord + full `r=2` + those seven `r=3` XOR splits**.

**Opposite outcome:** **all 400** sampled septuples have **`min_d=3`** (`witness_min_d2_count=0`).
