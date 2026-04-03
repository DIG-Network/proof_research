# Results: joint-min-max-sum-mod-product-mod-m-five-six-first-collision-n12

**Outcome:** PASS

## Measured

- **n:** 12 (indices `0..11`, weights `w_i = i+1` so `1..12`)
- **Shells:** |S| = 5 vs |S| = 6
- **Tag:** `K_M = (min w, max w, Σ w mod M, Π w mod M)`
- **Scan:** `M = 2, 3, …` until first cross-shell key collision
- **first_collision_M:** 2
- **Witness key K_2:** `(1, 6, 1, 0)`
- **5-set (indices):** `(0, 1, 2, 4, 5)` → weights `1,2,3,5,6` → min 1, max 6, sum 17 ≡ 1 (mod 2), product 180 ≡ 0 (mod 2)
- **6-set (indices):** `(0, 1, 2, 3, 4, 5)` → weights `1..6` → min 1, max 6, sum 21 ≡ 1 (mod 2), product 720 ≡ 0 (mod 2)

## Hypothesis

**H:** First collision modulus is **M = 2**. **Confirmed.**

## Interpretation

Same **first** collision floor as **n=10** (**094**); witness pair is **identical** on the shared index prefix (weights `1..6` pattern). Increasing **n** to 12 does not delay the **M=2** cross-shell merge for this joint tag.
