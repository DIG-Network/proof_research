# Hypothesis — one explicit witness tree exists for mixed coord + pair-XOR (n=10, wt {5,6})

## Analogy pass

1. **Abstract structure:** **066** **certified** **existence** **of** **a** **depth-5** **perfect** **separator** **tree** **via** **memoized** **Boolean** **DP** **without** **recording** **which** **splits** **realize** **it.** **Reproducibility** **/ ** **audit** **requires** **at** **least** **one** **constructive** **certificate** **(** **nested** **query** **plan** **).**

2. **Where else:**
   - **SAT** **/ ** **SMT** **models:** **satisfiability** **witness** **vs** **mere** **YES.**
   - **Game** **trees** **in** **combinatorial** **search:** **principal** **variation** **from** **the** **root.**
   - **Compiler** **optimization:** **existence** **of** **IR** **lowering** **vs** **emitting** **the** **chosen** **instruction** **sequence.**

3. **Machinery:** **Replicate** **066’s** **probe** **order** **(coordinates** **0..n−1** **then** **pair** **XORs** **lex** **on** **(i,j)).** **DFS** **`build_witness(S,d)`** **returns** **JSON-nested** **node** **or** **`None`.** **Empty** **child** **sets** **are** **leaves** **(** **`pure(())`** **in** **066** **logic** **).**

4. **Transfer candidate:** **If** **`build_witness(full,5)`** **non-`None`,** **PASS** **—** **verifier-oracle** **story** **is** **not** **only** **existential.** **If** **unexpected** **`None`**, **FAIL** **(** **implementation** **bug** **or** **order** **mismatch** **with** **`exists_tree`** **).**

## Falsifiable claim

**There** **is** **a** **depth-≤5** **mixed** **tree** **(** **internal** **nodes** **x_i** **or** **x_i⊕x_j** **)** **separating** **wt** **5** **vs** **6** **on** **n=10,** **and** **the** **script** **prints** **one** **nested** **witness** **matching** **066’s** **split** **priority.**
