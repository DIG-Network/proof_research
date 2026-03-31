# Notes

- **Generalization (same counting):** For thresholds **t** and **t−1** on **n** bits, after observing **k** coordinates with **z** ones on the probe set, extensions need **(t−1−z)** and **(t−z)** ones on **R = n−k** free coordinates. Ambiguity at a leaf requires both **0 ≤ t−1−z ≤ R** and **0 ≤ t−z ≤ R**. With **k ≤ n−t**, **R ≥ t**, and **z ≤ k**, one sufficient pattern for **both** to hold is the same style as here when **t−z ≤ R** and **t−1−z ≥ 0** (automatic if **z ≤ t−1**). Tighten per **(n, t, k)** for future query-budget lemmas.

- **Adaptive vs non-adaptive:** Any root-to-leaf path that queries at most **4** **distinct** indices yields a leaf labeled by some **(Q, p)** with **|Q| ≤ 4**. No further “branching magic” removes the **(Q, p)** ambiguity unless the model allows **queries that are not coordinate projections** (e.g. parities — see **021**).

- **Next probes:** (1) Same counting for **|Q| = 5** at **n=10, t=6** — expect **some** **(Q, p)** to separate because **R = 5** can block **6 − z** when **z** is small. (2) Document **minimum k** such that **some** **non-adaptive** **Q** **of** **size** **k** **separates** **all** **patterns** (stronger than **existential** collision per **Q**).
