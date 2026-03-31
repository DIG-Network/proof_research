# Results — tropical-min-pool-summary-quorum-collision

**Outcome:** PASS

**Parameters:** **n = 10**, **t = 6**, **public** **costs** **c_i = i** **for** **i = 0,…,9**.

**Summary:** **h(S) = min_{i ∈ S} c_i** **(tropical** **⊕** **over** **the** **active** **set** **with** **weights** **c_i)**.

**Witnesses:** **S_a = {0,1,2,3,4}** **(|S_a| = 5)**, **S_b = {0,5,6,7,8,9}** **(|S_b| = 6)**.

**Observed:** **h(S_a) = h(S_b) = 0** **(argmin** **index** **0** **lies** **in** **both)** **while** **|S_a| < t ≤ |S_b|**.

**Command:** `python script.py` → exit 0.
