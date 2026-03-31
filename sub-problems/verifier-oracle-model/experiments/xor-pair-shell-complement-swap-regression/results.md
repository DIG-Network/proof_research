# Results: complement shell swap ⇔ n = 2T − 1, XOR-pair tree regression

## Outcome: **PASS**

## Lemma (algebraic)

Fix **n, T** with **1 ≤ T−1 < T ≤ n.** Write **f(w) = n − w** **(complement** **effect** **on** **Hamming** **weight).** **Then** **f** **exchanges** **T−1** **and** **T** **iff** **n = 2T − 1.**

*Proof sketch:* **Need** **{n−(T−1), n−T} = {T−1, T}.** **If** **n−(T−1)=T** **and** **n−T=T−1,** **both** **give** **n=2T−1.** **Other** **assignments** **of** **the** **two** **values** **to** **the** **two** **preimages** **force** **either** **a** **contradiction** **or** **an** **identity** **on** **{T−1,T}** **(not** **a** **swap),** **ruled** **out** **by** **T−1 < T** **and** **integer** **arithmetic** **(checked** **in** **code** **for** **n∈[3,24],** **all** **valid** **T).**

Together with **049:** **pair** **XOR** **queries** **are** **invariant** **under** **x ↦ x⊕1,** **so** **when** **f** **swaps** **the** **two** **shells,** **no** **perfect** **XOR-only** **decision** **tree** **exists.**

## Computational regression

- **`xor_pairwise_impossible(n,T)`** **≡** **`(n == 2T−1)`** **verified** **for** **n∈[2,19],** **all** **valid** **T.**
- **`complement_swaps_two_shells(n,T)`** **≡** **`(n == 2T−1)`** **verified** **for** **n∈[3,24],** **all** **valid** **T.**
- **XOR** **backtracking** **(max** **depth** **80,** **n ≤ 6):** **tree** **exists** **iff** **`not`** **impossible** **flag.**
- **Spot** **(n,T)=(5,3):** **impossible** **⇒** **no** **tree** **through** **depth** **100** **(universe** **2⁵).**

## Scope note

This **does** **not** **claim** **that** **n=2T−1** **is** **the** **only** **obstruction** **to** **XOR-pair** **trees** **for** **all** **(n,T)** **—** **only** **that** **the** **049** **symmetry** **mechanism** **is** **exactly** **the** **shell-swap** **case,** **and** **the** **shortcut** **matches** **exhaustive** **search** **on** **the** **tested** **small** **grid.**

## Reproducibility

```bash
python script.py
```
