# Notes

- **vs `n=10` (099):** Prefix **`r=2..5`** depths are **6,5,4,3** — each step is **+1** vs **5,4,3,2** on 462 masks (consistent with “one more coordinate → one more layer” for this prefix; not a formal theorem).

- **099-style regression absent:** **`r=6`** and **`r=7`** do not exceed **`min_d(5)`** on **`n=11`**. The interior bump is **`r=8 → 4`**.

- **Union `r≤5`:** **`n=10 → 2`**, **`n=11 → 3`** — same shell *weights* but larger **`n`** can increase the depth for this union while **`r≤10`** still achieves **`2`**.

- **Persona / unsticking:** Three consecutive **`{5,6}`** arity sweeps (**098 / 099 / 100**). Next session should consider pivoting (**`anonymous-quorum-binding`**, lattice/TDA thread, or encoding-change) unless pursuing a closed **`(n,t)`** conjecture.
