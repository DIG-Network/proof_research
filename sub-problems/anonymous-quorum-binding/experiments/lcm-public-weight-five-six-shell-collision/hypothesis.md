# Analogy pass

## 1. Abstract structure

We need a **public fingerprint** of a hidden subset `S` that could, in a larger protocol, certify `|S| ≥ t`. If the same fingerprint arises on `|S| = t−1` and `|S| = t`, that statistic cannot **alone** separate quorum from sub-quorum.

## 2. Analogues (outside “known crypto”)

1. **Divisibility lattice** — **GCD** is the meet; **LCM** is the join on `ℕ` under divisibility (for the support of prime factors). Dual operations often carry complementary but still coarse information.
2. **Order statistics on partially ordered sets** — In a product of chains, meet/join summaries collapse many different antichains to one value (same “bottleneck” pathology as tropical min).
3. **089 (gcd toy)** — Showed `gcd` and `(gcd, Σw)` both alias across `|S|∈{5,6}` for `w_i=i+1`, `n=10`. **LCM** is the natural dual symmetric function in the same encoding.

## 3. Machinery in those domains

- **Lattice:** Compute `lcm_{i∈S} w_i` (join in divisibility for the multiset of prime exponents capped by max exponent in `S`).
- **Poset:** Same formula; implementation via iterative `lcm(a,b)=ab/gcd(a,b)`.
- **089:** Enumerate `C(10,5)` and `C(10,6)`; compare image sets and joint keys with `Σw`.

## 4. Transfer seed

Test whether **join-side** summary `h_lcm(S)` and joint `(h_lcm(S), Σw(S))` still admit **cross-shell collisions** on the same `(n,w_i)` instance as **087–089**.

---

# Formal hypothesis

**H1:** `Im(h_lcm)` on `|S|=5` intersects `Im(h_lcm)` on `|S|=6` (at least one shared LCM value).

**H2 (stronger):** Joint key `(h_lcm, Σw)` has at least one cross-shell collision.

**Falsification:** Disjoint images (or disjoint joint keys) on `C(10,5) ∪ C(10,6)`.

**Expected:** **PASS** — dual to gcd branch; LCM is still a low-degree symmetric statistic of the multiset `{w_i : i∈S}`.
