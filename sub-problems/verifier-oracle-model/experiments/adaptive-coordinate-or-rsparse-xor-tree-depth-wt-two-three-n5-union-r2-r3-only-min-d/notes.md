# Notes

- **Observation:** Same **20-split** union size as `{2}` shell + `r=2..3`, but here the shell is `{2,3}` — depth rises from **1** to **2** purely from the **mask alphabet**, not from adding `r=4`.
- **Insight:** The earlier contrast (`{2}`+`r=2..4` vs `{2,3}`+`r=2..4`) correctly blamed **shell expansion**, but **`r=4` was never the minimal sufficient ingredient** — it is **dispensable** once weight-3 masks are present.
- **Next:** No urgent follow-up on this `n=5` slice; narrative for verifier-oracle-model can cite this for sharper attribution.
