# Notes

- **BLS multisignature** literature addresses **rogue-key** attacks via **proof-of-possession** or **delinearized** aggregation; this toy uses **ℤ** only to exhibit **subset ambiguity** with **no** algebraic coupling to a forged signature.
- A full model would ask: given **honest** PoP, can adversary still force `PK(S₁) = PK(S₂)` for `S₁ ≠ S₂` in **𝔾**? That is a separate hardness / protocol question — not decided here.
- **Policy:** If the main problem assumes **honest keygen** only, state it explicitly; otherwise **`Link`** and registration hygiene are both in scope.
