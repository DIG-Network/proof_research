# Results: mod-m threshold alias gap-set scan

**Outcome:** `PASS`

## Definitions

- **n** validators, participation count **k ∈ [0, n].**
- **Threshold** **t** with **1 ≤ t ≤ n** (for strict majority toy, **t = ⌊n/2⌋ + 1**).
- **Crossing gaps** **D(n, t) = {k₂ − k₁ : 0 ≤ k₁ < t ≤ k₂ ≤ n}.**
- **Mod-m aliases** across the cut: **∃ k₁ < t ≤ k₂** with **k₁ ≡ k₂ (mod m)** (tested for **m ≥ 2**).

## Computed claims

1. **Majority** **t:** for **n = 2..30,** **D(n, t) = {1, …, n}.**
2. **Same** **n** **range:** **alias** **at** **m** **iff** **2 ≤ m ≤ n;** **first** **m** **with** **no** **alias** **is** **n + 1.**
3. **Regression** **(** **all** **thresholds** **):** for **n = 2..20** **and** **every** **t ∈ [1, n],** **D = {1,…,n},** **the** **same** **alias** **iff** **m ≤ n** **law** **holds,** **and** **first** **clean** **m = n + 1.**

## Proof sketch (why **D = {1,…,n}**)

Fix **d ∈ {1,…,n}.**

- If **d < t:** take **k₁ = t − d,** **k₂ = t.** Then **k₁ ∈ [0, t−1],** **k₂ ≥ t,** **k₂ − k₁ = d,** **k₂ ≤ n** **since** **t ≤ n.**
- If **d ≥ t:** take **k₁ = 0,** **k₂ = d.** Then **k₂ − k₁ = d,** **k₁ < t,** **k₂ ≥ t** **because** **d ≥ t,** **k₂ ≤ n** **because** **d ≤ n.**

Hence **every** **d ∈ {1,…,n}** **lies** **in** **D** **for** **any** **valid** **t** **(** **no** **majority** **assumption** **needed** **).**

**Mod-m:** **m ≤ n** **⇒** **m ∈ D** **⇒** **witness** **with** **gap** **m** **⇒** **k₁ ≡ k₂ (mod m).** **m = n + 1** **divides** **no** **element** **of** **{1,…,n}.**

## Relation to **081**

**081** **is** **the** **(** **n, t** **) = (10, 6)** **instance;** **this** **experiment** **generalizes** **the** **gap** **set** **and** **the** **“** **first** **clean** **modulus** **”** **law** **across** **n** **and** **(** **spot-checked** **)** **all** **t.**
