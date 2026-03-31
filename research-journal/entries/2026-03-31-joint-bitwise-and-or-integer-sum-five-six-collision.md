# 2026-03-31 — joint-bitwise-and-or-integer-sum-five-six-collision

- **Experiment:** `sub-problems/anonymous-quorum-binding/experiments/joint-bitwise-and-or-integer-sum-five-six-collision/`
- **Context:** anonymous-quorum-binding

## Hypothesis (short)

**Pairing** **087’s** **h_and** **/** **h_or** **with** **exact** **integer** **Σw** **still** **yields** **5** **vs** **6** **shell** **collisions.**

## Outcome: **PASS**

- **K_and:** **20** **joint** **keys** **shared** **across** **shells** **(** **e.g.** **(0,21):** **weights** **{1,2,3,5,10}** **vs** **{1..6}** **).**
- **K_or:** **23** **shared** **joint** **keys** **(** **e.g.** **(7,21):** **{1,2,5,6,7}** **vs** **{1..6}** **).**
- **Corollary:** **(** **h_*,** **Σw** **mod** **M** **)** **fails** **for** **every** **M** **on** **those** **witnesses** **(** **062** **pattern** **).**

## Key finding

**Bitwise** **fold** **+** **linear** **sum** **is** **still** **insufficient** **for** **anonymous** **threshold** **certification** **on** **this** **toy** **—** **extends** **087** **in** **the** **same** **direction** **as** **062** **did** **for** **(Σ** **mod** **M,** **XOR).**

## Implications

- **Deprioritize** **ad-hoc** **(** **bit-op,** **sum** **)** **pairs** **unless** **paired** **with** **a** **new** **independent** **axis** **(** **and** **a** **reason** **it** **avoids** **exact** **collisions** **).**

## Analogy pass summary

**062/063** **joint** **failure** **templates;** **feature** **redundancy** **—** **seed:** **second** **coordinate** **must** **break** **existing** **equal-sum** **witnesses,** **not** **only** **marginal** **h_* .**
