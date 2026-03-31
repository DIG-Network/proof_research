# Hypothesis

**H:** If the toy “signature check” used inside `Verify(C, m, π)` **does not** include the purported message **`m`** in its domain (e.g. it verifies **`σ = H("BAD"|K)`** only), then **the same** **`(K, σ)`** pair verifies for **multiple** distinct messages **`m`**.

Equivalently: **message binding** is a **separate** interface obligation from **quorum / `Link`** binding; omitting **`m`** from the verified relation yields **trivial cross-message malleability** even if Merkle / cardinality checks are perfect.

**Falsification:** Under the flawed relation, two distinct messages cannot both pass with one fixed **`σ`**.

**Expected outcome:** **PASS** (flawed relation is unsound for message intent); **sound** relation **`H("SIG"|m|K)`** fixes **`m`**.
