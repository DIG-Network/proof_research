# Notes

- **Observation:** At `n=11`, `|C(11,5)|=|C(11,6)|=462` and each shell maps **injectively** into `K`-space (`462` distinct keys per shell), yet **one** key is **shared** across shells — a **single** collision witness, not a large family.
- **Contrast (096):** The `n=12` witnesses `{1,5,6,8,m}` vs `{1,2,3,4,10,m}` for `m∈{11,12}` **cannot** occur at `n=11` (no weight `12`). The `n=11` witness uses the **maximum** weight `11` on **both** sides and is a **different** geometric pattern.
- **Implication:** Any narrative that “injectivity breaks when the universe reaches **twelve** weights” is **too strong**; the break happens already at **eleven** validators for this quadruple and weight schedule.
- **Next:** If tightening “minimal `n`” further under variant weights matters, scan other `w_i` schedules; for this linear `i+1` model, the **`10→11`** step is the **first** cross-shell merge.
