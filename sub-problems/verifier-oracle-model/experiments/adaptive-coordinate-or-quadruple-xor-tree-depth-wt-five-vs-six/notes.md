# Notes

- **Arity ladder:** On **(10,{5,6})**, each step **pair → triple → quadruple** XOR **as a primitive internal split** has dropped **`min_d`** by **one** so far (**5 → 4 → 3**). **Coordinate-only** stays at **10** (**045**).
- **Cost:** **210** quad splits vs **120** triples per node; **d=3** still **< 0.4 s** here — state/cache shape stayed favorable vs naive fear of blow-up.
- **Next (not run):** **Weight-5** parity splits **C(10,5)=252** — same ladder; **hypothesis:** **`min_d` might reach 2** or **stay 3**. **Weight-6** is global parity **popcount mod 2** on **10** bits; on **{5,6}** masks it **might** separate in **one** node (**5 odd, 6 even**) — **worth** a **small** **experiment** **(** **coord + full parity** **)** **without** **enumerating** **all** **5-sparse** **forms** **first**.
- **Caveat:** Toy **decision-tree** **complexity** **only**; **not** **a** **`Link`** **primitive**.
