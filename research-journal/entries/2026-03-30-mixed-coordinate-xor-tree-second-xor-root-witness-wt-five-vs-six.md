# 2026-03-30 — mixed-coordinate-xor-tree-second-xor-root-witness-wt-five-vs-six

- **Experiment:** `sub-problems/verifier-oracle-model/experiments/mixed-coordinate-xor-tree-second-xor-root-witness-wt-five-vs-six/`
- **Context:** verifier-oracle-model (**witness** **multiplicity** **/** **tie-break** **after** **069** **collapsed** **to** **067**).

## Hypothesis tested

**Enumerate** **lex** **pair-XOR** **roots** **on** **full** **wt∈{5,6}** **domain;** **if** **≥2** **feasible** **at** **depth** **budget** **5,** **take** **the** **second** **and** **complete** **with** **067’s** **`witness(S,** **d−1)`** **—** **expect** **JSON** **≠** **067.**

## Outcome: **PASS**

**45** **feasible** **root** **XOR** **pairs;** **second** **=** **(0,2).** **Depth** **5,** **leaf** **sum** **462.** **`sha256(json)`** **≠** **`sha256(`** **067** **default** **witness** **).**

## Key finding

**On** **(n=10,** **wt{5,6}),** **multiple** **valid** **depth-5** **mixed** **trees** **exist** **with** **different** **canonical** **nested** **witnesses;** **069’s** **collapse** **was** **tie-break** **/** **search-order** **specific,** **not** **a** **uniqueness** **theorem** **for** **`π_tree`.**

## Implications

- **Any** **sound** **interface** **that** **treats** **`π_tree`** **as** **a** **binding** **commitment** **must** **fix** **a** **canonicalization** **rule** **(** **or** **accept** **equivalence** **classes** **).**
- **Further** **stress:** **other** **nodes** **(** **not** **only** **root** **)** **may** **also** **admit** **alternate** **feasible** **splits** **—** **not** **enumerated** **here.**

## Analogy pass summary

**Multiple** **shortest-path** **first** **moves** **/** **ambiguous** **grammars** **—** **confirmed:** **many** **feasible** **root** **XOR** **splits;** **second** **lex** **hit** **yields** **distinct** **witness.**
