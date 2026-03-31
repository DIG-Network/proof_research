# Notes

- **Unsticking follow-through:** After **087–089** on scalar summaries, this branch extends the **F₂** adaptive-tree line without another `w_i=i+1` variant.
- **Performance:** Triple splits add **120** options per node vs **45** pair-XOR; total wall time **~8.6s** for **d=1..4** — still cheap vs **082**/**085** deep searches because **d=4** succeeds early.
- **Interpretation:** The **066**/**084** “pair linear” optimum **5** is **not** the end of the story for **arbitrary** low-weight **F₂** parity probes at internal nodes: **weight-3** hyperplanes buy **one** depth level on **(10,{5,6})**.
- **Next ideas (not run here):** **Quadruple** XOR or richer **fixed-weight** **F₂** parity families — cost grows (**C(10,4)=210** arity-4 splits, etc.). **Explicit** **coord+pair+triple** **primitive** **set** **is** **a** **strict** **superset** **of** **066** **and** **of** **this** **experiment** **(** **pairs** **≠** **one** **triple** **node** **);** **d=3** **was** **false** **here** **and** **would** **remain** **false** **with** **pairs** **added** **(** **066** **⊂** **that** **language** **)** **⇒** **`min_d`≥4** **if** **unchanged** **from** **this** **run.**
- **Caveat:** Toy only; does not solve **`Link`** or main threshold verification.
