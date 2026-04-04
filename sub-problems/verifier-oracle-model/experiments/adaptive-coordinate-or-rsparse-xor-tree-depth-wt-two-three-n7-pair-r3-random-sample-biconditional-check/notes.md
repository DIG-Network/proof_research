# Notes

- **Failure mode:** **Disjoint** **r=3** pairs are **necessary** for **`min_d=2`** at **n=6** (complementary **3+3**), but at **n=7** **disjoint** is **not sufficient**: many sampled disjoint pairs still need **depth 3**.
- **Interpretation:** The **“one vertex left out”** configuration changes which parity / coordinate certificates exist; the **DP** language may need **more** than **two** **r=3** splits (or **r>3** / union menus) to reach **depth 2** when the triples do not partition **[7]**.
- **Next probes (not run here):** Exhaustive **595** check (heavy); or characterize **which** disjoint pairs achieve **`min_d=2`** vs **3**; or compare to **full** **`r=2..5`** union baseline (**n=7** already has **`min_d=2`** with the large menu — this experiment isolates **minimal** **two-triple** languages).
