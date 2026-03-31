# Notes

- `F_Link` here uses a witness `S` **visible to the ideal**. In the **anonymous** target, the real protocol must hide `S` from the verifier while still realizing the same **semantic** predicate — that is exactly the “efficient `Link` without revealing indices” gap.
- **UC framing (next step):** Environment + adversary + simulator: real world gives `(C, m, π)`; ideal world gives `(C, m)` to `F_Sign` / `F_Link` with simulator fabricating `π`. Sublinear `π` imposes bandwidth on the simulator — not modeled in this script.
- Witness size `|S|` in the ideal is `Ω(t)` field elements if indices listed; **compressing** the witness is the engineering problem under excluded SNARKs.
