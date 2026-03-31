# Analogy pass

## 1. Abstract structure

**090** showed **coord + triple-XOR** achieves **`min_d=4`** on **(10,{5,6})** while **066** (**pair-XOR**) needs **5**. The natural arity ladder asks whether **weight-4** **F₂** parity splits at a single node shrink depth again.

## 2. Analogues

1. **LDPC / parity-check matrices** — rows of increasing Hamming weight change which error patterns are detectable in one check.
2. **Decision tree complexity** — richer split families reduce depth until the concept class is separated.
3. **Affine hyperplane arrangements** — in **F₂¹⁰**, **4-sparse** linear forms are a larger discrete family than **3-sparse**.

## 3. Machinery

Same **462-bit** memoized **`exists_tree`** as **090**, with **C(10,4)=210** precomputed partitions for **x_i⊕x_j⊕x_k⊕x_l**.

## 4. Transfer seed

**H:** Either **`min_d=3`** (**strict** improvement over **090**) or **`min_d=4`** (**quadruple** splits **do not** beat **triple** on this instance). **`min_d≥4`** is guaranteed because **090**’s language is a **subset** (**omit** **4-XOR** nodes) and **090** had **d=3** false.

---

# Formal hypothesis

Exhaustive **`exists_tree`** on the full **462-set** with **coord + all 4-XOR** nodes yields **`min_d ∈ {3,4}`** (and not higher than **4**).
