# Notes

- **Prime-order group:** If `pk_i = g^{sk_i}` with random independent `sk_i`, multiset addition in the exponent corresponds to **integer sum of scalars** mod `q`; collisions mod `q` are a different event than integer overflow in ℤ — this script stays in ℤ for clarity.
- **Rogue keys:** An adversary registering `pk` could try to force `Agg(S₁) = Agg(S₂)` for `|S₁| ≠ |S₂|`; that is orthogonal to the honest-random regime tested here.
- **Entry 006:** Keep both lessons — (i) anonymity does not need injective `π` on subsets; (ii) **structured** integer models can exaggerate aggregate ambiguity.
