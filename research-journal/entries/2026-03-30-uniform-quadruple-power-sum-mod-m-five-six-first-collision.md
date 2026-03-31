# 2026-03-30 — uniform quadruple power sum mod M (5-set vs 6-set)

- **Experiment:** `sub-problems/anonymous-quorum-binding/experiments/uniform-quadruple-power-sum-mod-m-five-six-first-collision/`
- **Context:** anonymous-quorum-binding (**065** follow-up: add fourth power, single uniform **M** on **(p₁,…,p₄)**).

## Hypothesis tested

**M\*** = least **M≥2** with a **5-vs-6** collision on **(S₁,S₂,S₃,S₄) mod M** for **w_i = i+1**, **n=10**, where **S_k = Σ_{i∈S} w_i^k**. Expectation: **M\*** might exceed **2** if the fourth moment breaks parity-only collisions.

## Outcome: **PASS**

**M\*** **= 2**; **mod_key** **(1,1,1,1)**. **Witness:** **5-set** indices **(4,6,7,8,9)** → weights **(5,7,8,9,10)**, raw **(39, 319, 2709, 23683)**; **6-set** **(0,1,2,3,4,5)** → **(1,2,3,4,5,6)**, raw **(21, 91, 441, 2275)** — all four power sums agree mod **2**.

## Key finding

The **fourth** uniform modular moment does **not** delay the first **5-vs-6** shell collision: **M=2** still suffices (**parity** on every **S_k** for this witness pair), matching the **single-** and **triple-moment** uniform-modulus story (**034** / **065**).

## Implications

- **Four** fixed public power sums mod one **M** are not a threshold separator at the smallest nontrivial modulus for **w_i=i+1**, **n=10**.
- **Next:** **five** moments **k=1..5**, or non-uniform weights / per-coordinate moduli, to see if **M\*** moves.

## Analogy pass summary

Same **quantization / aliasing** thread as **065** — extra coordinate did not increase the **critical bin width** in this toy.
