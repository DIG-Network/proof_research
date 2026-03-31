# Sub-problem: verifier oracle model and definitional barriers

## Question

Under a **precisely defined** verifier model (what the verifying algorithm may depend on besides `(C, m, π)`), what are necessary conditions on `|π|`, the structure of `Commit`, or auxiliary public parameters for sound threshold verification when individual `pk_i` are unavailable at verify time?

## Threat model hook

- **Verifier:** May depend **only** on `(C, m, π)` and **public** parameters fixed at setup — not on the full list `pk_1..pk_n` if those are disallowed by the main problem.
- **Registration:** Results that reason about “aggregate key” ambiguity (e.g. integer toy models) must say whether keys are **honest random** vs **maliciously chosen**; see journal entries **006–008** and experiment `threat-model-registration-assumptions`.

## Why this blocks the main problem

Without a clear model, “compact verification” is ambiguous. If the model is too weak, the main objective may be **impossible**; if too strong (e.g. hidden access to full key list), it violates the main constraints.

## Deliverable

Either:
- A formal **impossibility sketch** in a stated model (ideal functionality + communication bounds), or
- A proof that a stated relaxation of the model is **necessary** for any construction.

## Non-goals

- Producing a full construction for the main problem (that belongs in main track after this sub-problem closes).
