# 2026-03-30 — min-max-sum-triple-weight-five-six-shell-collision

- **Experiment:** `sub-problems/anonymous-quorum-binding/experiments/min-max-sum-triple-weight-five-six-shell-collision/`
- **Context:** anonymous-quorum-binding

## Hypothesis (short)

**Joint** **verifier-visible** **triple** **(min w, max w, Σw)** **on** **w_i=i+1,** **n=10** **admits** **5-vs-6** **shell** **collisions** **;** **mod** **fold** **on** **Σ** **hits** **small** **M.**

## Outcome: **PASS**

- **Exact** **K:** **126** **distinct** **on** **5-shell,** **95** **on** **6-shell,** **41** **cross-shell** **shared** **keys.**
- **Sample** **exact** **collision:** **(1,7,22)** **—** **5-set** **weights** **1,3,5,6,7** **vs** **6-set** **1,2,3,4,5,7.**
- **K_M** **with** **Σ mod M:** **first** **collision** **at** **M=2** **(** **25** **shared** **K_2** **keys** **).**

## Key finding

**Extrema** **+** **sum** **is** **a** **natural** **“sufficient** **statistic”** **analogue** **but** **fails** **threshold** **separation** **on** **this** **toy** **;** **parity** **on** **Σ** **collapses** **shells** **immediately** **once** **min/max** **are** **fixed** **in** **the** **joint** **tag.**

## Implications

- **Do** **not** **rely** **on** **(min,max,Σ)** **alone** **as** **a** **public** **threshold** **witness** **for** **|S|∈{5,6}** **with** **weights** **1..10** **;** **contrasts** **with** **exact** **moment** **triple** **064** **(** **injective** **there** **).**
- **Any** **certificate** **that** **only** **reveals** **bounded** **information** **about** **support** **(** **extrema** **)** **plus** **one** **additive** **statistic** **needs** **a** **different** **functional** **than** **raw** **Σ** **or** **must** **avoid** **mod-2** **(** **and** **similar** **)** **collapse** **on** **the** **pair** **(** **064** **/** **065** **split** **).**

## Analogy pass summary

**Sufficient** **statistics** **/** **063** **(Σ,Π)** **/** **088** **(bitwise+Σ)** **—** **seed:** **order** **stats** **+** **mass** **as** **encoding** **change** **from** **moments** **;** **refuted** **on** **this** **instance.**
