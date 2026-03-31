# Notes

- **(2,3)** is the **smallest** lex pair with **gcd=1** (skip **(2,2)**). Collision is **immediate** in the coprime-restricted scan — **no** delay vs unrestricted **054** beyond skipping the non-coprime **(2,2)** row.
- **Mechanism:** First coordinate still **parity** of **Σw**; second is **Σw² mod 3**, which matches **1** for both witnesses (same as **055**’s mod-3 quadratic residue line, but here **M₁=2** so the pair is coprime).
- **Next:** **min(M₁,M₂) ≥ 4** with **gcd=1** (e.g. **(4,5)** onward), or **triple** **(Σw, Σw², Σw³)** mod coprime triple, if we want to see the first collision **move** off this witness in a bounded window.
