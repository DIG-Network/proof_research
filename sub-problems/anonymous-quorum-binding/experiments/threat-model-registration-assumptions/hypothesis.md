# Hypothesis

**H:** The research journal’s conclusions split cleanly across **two** registration regimes:

1. **Honest / unmanipulated key distribution** (IID random scalars or standard keygen): aggregate **injectivity** on majority subsets is plausible in toy models (Entry **007**); attacks that rely only on **structured small** integers (Entry **006**) are misleading for this regime.

2. **Malicious key registration** (adversary chooses `pk_i` subject to appearing in `Commit(V)`): **aggregate collisions** between distinct strict majorities are **constructible** in the integer toy (Entry **008**); any soundness story must assume **mitigations** (PoP, delinearized aggregation, or explicit **`Link`**) or state **malicious-registration exclusion**.

**Falsification:** Show that Entries **006–008** cannot be classified along these two axes without contradiction.

**Scope:** Organizational clarity for future experiments — not a new cryptographic theorem.
