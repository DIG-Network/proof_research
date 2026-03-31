# 2026-03-31 — gcd-public-weight-five-six-shell-collision

- **Experiment:** `sub-problems/anonymous-quorum-binding/experiments/gcd-public-weight-five-six-shell-collision/`
- **Context:** anonymous-quorum-binding

## Hypothesis (short)

**Subset** **gcd** **of** **w_i=i+1** **(** **and** **joint** **with** **Σw** **)** **admits** **5** **vs** **6** **shell** **collisions.**

## Outcome: **PASS**

- **h_gcd:** **only** **two** **values** **on** **5-shell,** **one** **on** **6-shell** **(** **always** **1** **);** **shared** **value** **1.**
- **J=(gcd,Σw):** **20** **cross-shell** **joint** **keys** **(** **same** **count** **as** **088** **K_and** **joint** **here** **).**

## Key finding

**gcd** **is** **too** **coarse** **on** **this** **weight** **range** **for** **|S|=6** **—** **parallel** **to** **087** **(** **h_and** **collapse** **on** **6-shell** **)** **but** **via** **divisibility** **not** **bits.**

## Implications

- **Scalar** **gcd** **of** **fixed** **public** **1..10** **weights** **is** **not** **a** **threshold** **separator** **;** **pairing** **with** **Σw** **does** **not** **repair** **(** **088** **pattern** **).**

## Analogy pass summary

**Divisibility** **meet** **vs** **bitwise** **meet;** **063** **multiplicative** **thread** **—** **seed:** **encoding** **change** **after** **bitwise** **line** **still** **hits** **immediate** **collapse** **/** **collision.**
