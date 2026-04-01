# Notes

- **Dual to `r=10` was the wrong mental model for runtime:** same **1001** menu cardinality, opposite **DP** behavior at **5e7/8M**.
- **Interpretation:** the **parity / mask interaction** for **4-subset XOR** gates differs enough from **10-subset** gates that **state-space growth** and **memo churn** blow up — not visible from **C(n,r)** alone.
- **Next:** **`r=7`** (**3432** splits) for **>**3003 menu; or **larger budget / unbounded memo** on **`r=4`** if a **definite** **`d=3`** bit is needed; **`r=4`** is **not** a cheap stand-in for **`r=10`**.
