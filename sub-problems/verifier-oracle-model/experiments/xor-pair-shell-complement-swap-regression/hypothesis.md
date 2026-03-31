# Hypothesis: when complement swaps exactly the two shells ⇔ n = 2T − 1 (XOR pair-tree obstruction)

## Analogy pass

1. **Abstract structure:** A hidden Boolean vector **x** is queried only through **pairwise XORs** **x_i ⊕ x_j** along an adaptive tree. The verifier’s target predicate is **|x| ∈ {T−1, T}.** **Global** **complement** **x ↦ x ⊕ 1** **induces** **|x| ↦ n − |x|.**

2. **Where else does this structure appear?**
   - **Involution** **symmetry** **in** **puzzle** **games** **(lights** **out,** **necklace** **inversion)** **—** **orbits** **pair** **states** **that** **look** **different** **to** **the** **player** **but** **are** **equivalent** **under** **a** **hidden** **symmetry.**
   - **Gauge** **transformations** **/ ** **quotienting** **in** **physics** **—** **observables** **invariant** **under** **a** **group** **action** **cannot** **distinguish** **gauge-related** **configurations.**
   - **Fourier** **on** **F₂ⁿ:** **characters** **with** **even** **support** **are** **orthogonal** **to** **all-ones;** **pair** **XORs** **span** **even-support** **directions** **—** **ties** **to** **049’s** **parity** **story.**

3. **Machinery:** **Orbit-stabilizer** **reasoning;** **quotient** **information** **by** **G-invariant** **queries;** **linear** **algebra** **over** **F₂** **for** **which** **functionals** **see** **complement.**

4. **Transfer seed:** **049** **asserted** **impossibility** **when** **n = 2T − 1** **because** **complement** **swaps** **T−1** **↔** **T** **while** **every** **pair** **XOR** **is** **complement-invariant.** **This** **experiment** **(i)** **proves** **algebraically** **that** **“swap** **the** **two** **shells”** **iff** **n = 2T − 1** **(for** **0 ≤ T−1 < T ≤ n),** **and** **(ii)** **regresses** **the** **implemented** **shortcut** **against** **exhaustive** **XOR** **min-depth** **search** **on** **a** **small** **grid.**

## Formal claims

**Lemma (shell swap):** For integers **n, T** with **1 ≤ T−1 < T ≤ n,** **the** **map** **w ↦ n−w** **exchanges** **T−1** **and** **T** **iff** **n = 2T − 1.**

**H1:** **The** **code** **flag** **`xor_pairwise_impossible(n,T)`** **(n == 2T−1)** **matches** **the** **lemma** **for** **all** **tested** **(n,T).**

**H2:** **When** **the** **flag** **is** **true,** **exhaustive** **backtracking** **finds** **no** **finite-depth** **perfect** **XOR-pair** **tree** **(returns** **`None` / ** **no** **solution** **up** **to** **large** **depth** **cap).** **When** **false** **and** **n ≤ N_max,** **a** **tree** **exists** **within** **the** **depth** **cap** **(positive** **min** **depth).**
