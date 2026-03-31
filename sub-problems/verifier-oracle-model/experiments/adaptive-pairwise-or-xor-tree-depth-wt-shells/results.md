# Results: pairwise OR / XOR adaptive trees on wt {T−1, T} shells

## Outcome: **PASS**

## Computed min depths (exhaustive backtracking; XOR skips search when `n = 2T − 1`)

| op | (n, T) | Domain | Min depth | vs n | vs AND (048) |
|----|--------|--------|-----------|------|----------------|
| OR | (5, 3) | 20     | **6**     | > n  | = AND (6)      |
| XOR | (5, 3) | 20    | **—**     | **impossible** | — |
| OR | (6, 4) | 35     | **9**     | > n  | AND was **6**  |
| XOR | (6, 4) | 35    | **3**     | < n  | AND was **6**  |

## XOR impossibility when `n = 2T − 1`

If `n = 2t − 1`, complement `x ↦ x ⊕ (1,…,1)` maps weight `t−1` ↔ `t`. For any `i < j`, `(x⊕1)_i ⊕ (x⊕1)_j = x_i ⊕ x_j`, so **every** pairwise-XOR answer is **invariant** under complement. Any two masks that are complements of each other follow the **same** root-to-leaf path in an XOR-pair-only tree, but lie in **different** weight shells — **no** perfect classifier exists.

Here `(5,3)` satisfies `5 = 2·3 − 1`.

## Interpretation

- **OR** is a **poor** **non-coordinate** **probe** **here:** **(6,4)** **costs** **depth** **9** **>** **AND’s** **6** **and** **>** **n.**
- **XOR** **is** **orthogonal** **to** **the** **045** **story:** **when** **the** **complement** **symmetry** **applies,** **it** **is** **useless** **for** **this** **threshold** **gap;** **when** **not** **(6,4),** **it** **can** **separate** **in** **depth** **3** **≪** **n** **(here** **parity** **of** **|x|** **differs** **between** **3** **and** **4,** **and** **pair** **XORs** **suffice** **to** **recover** **it** **adaptively).**

## Reproducibility

```bash
python script.py
python script.py --op xor --n 6 --t 4
```
