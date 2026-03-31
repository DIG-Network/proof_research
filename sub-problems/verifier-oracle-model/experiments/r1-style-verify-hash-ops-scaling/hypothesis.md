# Hypothesis

**H:** In the **sound R1-style** interface (journal **011**), verifying **one** signer’s Merkle inclusion against fixed `C` costs **\(1\)** leaf hash plus **`depth(n)`** internal-node hashes along the path, where **`depth(n) = \lceil \log_2 n \rceil`** for a balanced binary tree over **`n`** leaves (power-of-**2** leaves assumed as in prior experiments).

For strict-majority signing set size **`t = \lfloor n/2 \rfloor + 1`**, a verifier that checks **all** **`t`** paths therefore performs **`t \cdot (1 + \mathrm{depth}(n))`** SHA-style compressions in this toy accounting model — **\(\Theta(n \log n)\)** when **`t = \Theta(n)`**, **not** **`O(1)`**.

**Falsification:** The closed form disagrees with a direct loop count for small **`n`**.

**Non-claim:** This counts **only** Merkle recomputation from given **`(pk_i, \text{path})`**; it ignores **`SigVerify`** cost and any other checks. It is a **verifier-oracle** / **standard compute** hygiene datum paired with **012** (proof bits).
