# Results — rogue-key-aggregate-collision

**Outcome:** **PASS**

## Construction

- `n = 6`, strict majority `t = 4`.
- `pk = [1, 1, 5, 5, 5, 5]`.
- `S₁ = (0, 1, 2, 3)`, `S₂ = (0, 1, 4, 5)` — both of size `4`, distinct, strict majorities.
- `Agg(S₁) = Agg(S₂) = 12`.

## Counts

- `W = 22` strict-majority subsets; **`U = 6`** distinct majority subset sums for this `pk` (so **`U ≪ W`**).

## Interpretation

1. **Complements Entry 007:** Random honest-looking keys can give `U = W`; **adversarial registration** can still force **`U ≪ W`** and **aggregate collisions** between **different** quorums.
2. **Reinforces Entries 002 / 004:** Soundness cannot rely on “`K` uniquely identifies the signing coalition” without **`Link(C, K)`** plus **key-registration rules** (e.g. PoP, uniqueness policies) appropriate to the real group setting.

## Script

`python script.py` — assertions; exit code 0.
