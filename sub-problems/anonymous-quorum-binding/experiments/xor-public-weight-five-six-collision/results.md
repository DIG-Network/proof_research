# Results — `xor-public-weight-five-six-collision`

**Outcome:** PASS (on hypothesis **“collision exists”**)

**Setup:** `n = 10`, `w_i = i+1`. **H(S) = ⨁_{i∈S} w_i** (bitwise XOR). Exhaust all **|S|=5** and **|S|=6**.

**Witness:**

| | indices | weights | H |
|--|---------|---------|---|
| 5-set | **(4, 5, 6, 8, 9)** | 5,6,7,9,10 | **7** |
| 6-set | **(0, 1, 2, 3, 4, 5)** | 1,2,3,4,5,6 | **7** |

**Command:** `python script.py`

**Note:** The **6-set** is again **(0..5)**; the **5-set** matches **057**’s **(4,5,6,8,9)** — **non-additive** **XOR** **does** **not** **evade** **this** **shell** **pair** **in** **the** **toy**.
