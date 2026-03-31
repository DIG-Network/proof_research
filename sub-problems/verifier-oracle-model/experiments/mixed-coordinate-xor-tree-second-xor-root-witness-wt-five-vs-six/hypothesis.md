# Hypothesis — second feasible pair-XOR at root (n=10, wt {5,6}, depth 5)

## Analogy pass

1. **Abstract structure:** **067** **/** **069** **pick** **the** **first** **lex** **pair-XOR** **(** **(0,1)** **)** **that** **admits** **a** **depth-4** **completion** **on** **both** **sides** **of** **the** **462-set.** **If** **another** **(** **i,j** **)** **also** **works** **at** **the** **root,** **the** **prover** **could** **ship** **a** **different** **π_tree** **with** **the** **same** **feasibility** **semantics** **(** **066** **).**

2. **Where else:**
   - **Alternative** **optima** **in** **shortest-path** **/** **A\*** **(** **multiple** **minimum-cost** **first** **moves** **).**
   - **Non-deterministic** **grammar** **derivations** **for** **the** **same** **string** **(** **ambiguity** **).**
   - **SAT:** **multiple** **decision** **orderings** **leading** **to** **the** **same** **or** **different** **models.**

3. **Machinery:** **Enumerate** **(** **i,j** **)** **in** **lex** **order;** **test** **`exists_tree`** **on** **children** **with** **budget** **d−1;** **if** **≥2** **hits,** **commit** **root** **to** **the** **second** **hit** **and** **complete** **subtrees** **with** **067’s** **`witness(S,** **d−1)`** **(** **coord-first** **principal** **variation** **).**

4. **Transfer candidate:** **PASS** **with** **JSON** **≠** **067** **⇒** **tie-break** **choice** **matters** **for** **audited** **plans.** **FAIL** **/** **INCONCLUSIVE** **if** **<2** **feasible** **XOR** **roots** **⇒** **root** **XOR** **is** **essentially** **pinned** **here.**

## Falsifiable claim

**At** **least** **two** **distinct** **pair-XOR** **splits** **(** **i<j** **)** **of** **the** **full** **wt∈{5,6}** **domain** **admit** **depth-≤5** **perfect** **trees** **when** **used** **as** **the** **root** **query,** **and** **the** **second** **such** **split** **yields** **a** **nested** **witness** **not** **byte-identical** **to** **067.**
