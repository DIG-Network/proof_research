# Results

| Field | Value |
|-------|--------|
| **Outcome** | **PASS** |
| **Type** | Information / decision-theoretic toy (not a full protocol). |

## Instance

- **n = 10** validators, strict majority **t = ⌊n/2⌋ + 1 = 6**.
- Summary **h(k) = k mod 2** where **k** is the number of signers (integer).

## Collision

| k | Quorum? (**k ≥ t**) | **h(k)** |
|---|----------------------|----------|
| **4** | **No** | **0** |
| **6** | **Yes** | **0** |

## Conclusion

No function of **h(k)** alone can implement **𝟙_{k ≥ t}** exactly — **lossy** **1-bit** quantization of the count **aliases** across the **threshold** cut.

## Contrast

The **full** integer **k** (or **⌈log₂(n+1)⌉** bits) **is** sufficient for any **k ≥ t** predicate; **021** concerned **many** **F₂** **parity** masks, while here a **single** **mod-2** count summary fails.
