# Notes

- **Signer anonymity:** This baseline **reveals** `S` (and implies **Ω(t log n)** bits) — incompatible with the “hide cosigners” goal unless `S` is replaced by a ZK layer (excluded SNARK path) or **R7**.
- **Merkle shape:** Power-of-2 padding is for script simplicity; production trees use standard padding rules — asymptotics unchanged.
- **Malicious keys:** Same **rogue-key** caveats as **008** apply if `pk_i` are adversarial; this demo uses **honest** structured integers.
