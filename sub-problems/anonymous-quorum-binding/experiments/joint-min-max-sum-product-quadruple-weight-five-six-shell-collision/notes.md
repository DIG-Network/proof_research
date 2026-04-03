# Notes

- **Structural:** The failure of smaller summaries is not monotonic: **063** `(Σ,Π)` has cross-shell collisions, but pinning `(min,max)` alongside `(Σ,Π)` removes all 5-vs-6 ambiguity here.
- **Not a threshold proof:** Injectivity on `|S|=5` vs `6` does not give a compact **commitment-compatible** verifier by itself (still four integers, and **Link(C,K)** issues from prior entries remain).
- **Modular folding:** Not scanned in this run; expect small-modulus collapse to reappear if any coordinate is reduced mod `M` (same parity / CRT themes as **065**, **091**).
- **Next (optional):** Scan smallest `M` for `(min,max,Σ mod M, Π mod M)` cross-shell collision, or try `n>10` / other weight vectors to stress-test robustness.
