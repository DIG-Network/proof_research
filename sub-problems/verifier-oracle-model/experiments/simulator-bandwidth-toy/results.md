# Results — simulator-bandwidth-toy

**Outcome:** **PASS** for **H1** / **H3** (conceptual separation); **INCONCLUSIVE** for any general lower bound on `|π|`; **H2** supported in the toy model (`U < W` ⇒ `⌈log₂ U⌉ ≪ log₂ W` for labeling **aggregates**, not subsets)

## Scripted observations

- For **affine linear** integer keys `pk_i = 1000 + 13 i` and small `n ∈ {6,8,10}`, enumeration found **`U < W`** already (e.g. `n = 6`: `W = 22`, `U = 16`; `n = 10`: `W = 386`, `U = 75`) — many distinct majority subsets **collapse** to the same integer aggregate **sum**.
- For **structured** keys `pk_i = 2^i` at `n = 10`, the script observed **`U = W = 386`** and **did not** find a majority-subset collision in this run (collision search may miss pathological cases; different `n` may differ).
- For `n = 64`, **only** `W` and `log₂(W)` are reported (full enumeration of subsets omitted) — reminder that **subset count** is huge; still **no** automatic implication for minimal `|π|` under **anonymous** acceptance.

## Interpretation

1. **Anonymity (H1):** Many distinct quorums may yield the **same** accepting transcript; pigeonhole on `W` does **not** force `|π| ≥ log₂ W`.
2. **Specifying `K` (H2):** If the protocol’s honest artifact must **pin** a particular aggregate among **`U`** possibilities, **lossless** naming needs `~log₂ U` bits in the worst case over `S` — but a **single group element** already does that in real groups; the bottleneck remains **`Link(C, K)`**, not `K`’s bit-length.
3. **Simulator metaphor (H3):** Bandwidth pressure from “many subsets” shifts to **proving** the `F_Link` predicate, consistent with Entries **002–005**.

## Script

`python script.py` — small-`n` enumeration + collision search; exit code 0.
