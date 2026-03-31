# Results

| Field | Value |
|-------|--------|
| **Outcome** | **PASS** (attack succeeds on flawed verifier) |
| **Model** | Same Merkle + toy `σ = H(SIG|m|K)` pattern as **011** / **r1-baseline**. |

## Setup

- `n = 8`, `t = 5`, `S` of size **5** with valid paths into `C`.
- `K_sum = Σ_{i∈S} pk_i`, `K_adv = K_sum + 999_999`, `σ = H_sig(m, K_adv)`.

## Verdicts

| Verifier | Enforces `K == Σ` opened keys? | Accepts `(S, paths, K_adv, σ)` |
|----------|---------------------------------|-------------------------------|
| Sound | Yes | **No** |
| Flawed | **No** | **Yes** |

## Interpretation

Merkle paths alone **membership-bind** the opened `pk_i` to `C`; they do **not** automatically bind a **separate** aggregate field `K` used in the signature equation. **011** already includes the sum check in the sound baseline — this experiment isolates that check as a **necessary** interface line item for `Link`-style consistency.
