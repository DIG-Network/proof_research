# Outcome: **PASS**

## What was checked

For each integer **n** from **1** through **18**, and each **k** with **0 ≤ k < n**, enumerate all masks of Hamming weight **k** and **k+1** on **n** bits (via `itertools.combinations`). For every such mask **x**, compute global XOR parity **π(x) = ⊕ᵢ xᵢ** (popcount mod 2). Assert:

- Every weight-**k** mask has **π(x) = k mod 2**.
- Every weight-**(k+1)** mask has **π(x) = (k+1) mod 2**.

Since **k** and **k+1** have opposite parity, the two shells are disjointly labeled by **π** on their union; equivalently, **π** induces a perfect split of **{x : |x| ∈ {k, k+1}}**.

For **n ∈ {19, 200}**, only the arithmetic fact **(k mod 2) ≠ ((k+1) mod 2)** was checked at sample **k** values (no full shell enumeration).

## Runtime

Full enumeration for **n = 1..18** completed in about **8 s** on the test host (script prints **PASS**).

## Conclusion

The “global parity separates adjacent Hamming shells” statement used conceptually in **092** holds in full generality on the tested range and is consistent with the trivial **k ⊕ (k+1) = 1** pattern for larger **n**.
