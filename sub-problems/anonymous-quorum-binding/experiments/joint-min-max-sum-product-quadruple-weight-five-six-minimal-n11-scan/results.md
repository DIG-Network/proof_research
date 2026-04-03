# Results

**Outcome:** **PASS** (hypothesis confirmed: **minimal** `n > 10` with a **5-vs-6** cross-shell collision for exact `K=(min,max,Σ,Π)` and `w_i=i+1` is **`n=11`**, not `n=12`).

## Measurements

| `n` | `C(n,5)` | `distinct_K_5` | `C(n,6)` | `distinct_K_6` | `cross_shell_exact` |
|-----|----------|----------------|----------|----------------|---------------------|
| 11  | 462      | 462            | 462      | 462            | **1**               |

At `n=11`, both shells use **all** distinct keys internally (`462` each), but **one** key is shared across shells.

## Witness

- **Shared key:** `(min,max,Σ,Π) = (1, 11, 31, 2640)` (weights `1` and `11` are indices `0` and `10` in 0-based indexing).
- **5-set (indices):** `(0, 4, 5, 7, 10)` → weights `{1,5,6,8,11}`.
- **6-set (indices):** `(0, 1, 2, 3, 9, 10)` → weights `{1,2,3,4,10,11}`.

## Relation to **096** (`n=12`)

**096** exhibited **two** collisions at `n=12` with a closed-form family involving the top weights `11,12`. This scan shows cross-shell collisions already exist at **`n=11`**; **`n=12`** is **not** the first `n` where `K` fails to separate the `5`/`6` shells.

## Reasoning

Exhaustive enumeration over `C(11,5)` and `C(11,6)`; set intersection of key multisets (as sets of keys). `PASS` branch: `n=11` intersection nonempty ⇒ minimal `n` is **at most** `11`. Combined with **093** (`n=10`, intersection empty), minimal `n > 10` is **exactly** `11`.
