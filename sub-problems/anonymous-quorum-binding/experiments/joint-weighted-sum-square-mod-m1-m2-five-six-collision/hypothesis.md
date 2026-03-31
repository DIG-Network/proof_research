# Hypothesis: joint \((\sum w_i \bmod M_1,\ \sum w_i^2 \bmod M_2)\) still collides across \(|S|=5\) vs \(6\)

## Analogy pass

1. **Abstract structure:** Map each hidden subset \(S \subseteq [n]\) to a **small** **tag** in a finite abelian group (here \(\mathbb{Z}_{M_1} \times \mathbb{Z}_{M_2}\)) using **two** **fixed** **public** **statistics** of the selected indices. Ask whether tags can coincide for **different** **cardinalities** straddling quorum threshold \(t\) while \(n\) is fixed.

2. **Where else does this structure appear?**
   - **Sufficient statistics:** A **2-dimensional** statistic can be injective on a family of distributions or fail if the family is too rich — classical **curved exponential** vs **non-identifiable** **mixtures**.
   - **CRT / simultaneous congruences:** Two residues jointly constrain an integer only up to \(\mathrm{lcm}(M_1,M_2)\) if the statistics are **linear** in one underlying total; here we mix **degree-1** and **degree-2** power sums.
   - **Coding:** **Syndrome** pairs from two parity checks; **minimum** **distance** **analog** = whether **5-** **vs** **6-subset** **patterns** **share** **a** **syndrome**.

3. **Machinery in those domains:** Moment matching up to modular reduction; Chinese remainder thinking; counting degrees of freedom vs number of constraints.

4. **Transfer seed:** Entries **034**/**052** show **single** modular **linear** or **quadratic** power-sum folds hit collisions at **\(M=2\)** for \(n=10\), \(|S|\in\{5,6\}\), **public** **\(w_i=i+1)\)**. **Joint** **\((\sum w_i \bmod M_1,\ \sum w_i^2 \bmod M_2)\)** is the next **“dimensionality shift”** in the same toy line — test whether **small** **\(M_1,M_2\)** **still** **allow** **cross-cardinality** **aliases**.

## Formal claim

Let \(n=10\), weights \(w_i=i+1\) for \(i\in\{0,\ldots,9\}\). For non-empty \(S\subseteq\{0,\ldots,9\}\) define
\[
h_{M_1,M_2}(S) = \Bigl(\sum_{i\in S} w_i \bmod M_1,\ \sum_{i\in S} w_i^2 \bmod M_2\Bigr).
\]

**H1:** There exist **5-subset** \(F\) and **6-subset** \(G\) with \(h_{M_1,M_2}(F)=h_{M_1,M_2}(G)\) for some **small** **\((M_1,M_2)\)** (search lexicographic \(M_1,M_2 \ge 2\); report **first** hit).

**H2 (null for this script):** If no hit appears below a cap (e.g. \(M_1,M_2 \le B\)), report **INCONCLUSIVE** / **no collision in range** — the script is tuned to **find** **early** **collisions** **first**.

The experiment **PASS**es as **negative** **evidence** for this **2D** **modular** **threshold** **certificate** **if** **H1** **holds** **with** **small** **moduli** **(same** **convention** **as** **034/050/052).**
