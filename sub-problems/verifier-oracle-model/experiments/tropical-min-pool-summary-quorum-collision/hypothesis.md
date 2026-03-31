# Hypothesis: min-only tropical summary collides across quorum if same argmin lies in both sets

## Analogy pass

1. **Abstract structure**  
   The verifier sees a **single scalar** computed from active indices **S** and **public** **per-index** **weights** **c_i**, using **only** a **min** **(tropical** **⊕)** **over** **participants** **—** **no** **cardinality**, **no** **full** **list** **of** **S**. We ask whether **k ≥ t** **can** **be** **read** **off** **from** **this** **summary** **alone**.

2. **Where else this structure appears**  
   - **Tropical** **/** **min-plus** **algebra:** **Value** **of** **a** **tropical** **linear** **functional** **depends** **only** **on** **the** **minimum** **slack** **support**.  
   - **Bottleneck** **optimization** **/** **shortest-path** **substructure:** **Optimal** **cost** **often** **determined** **by** **one** **tight** **constraint**, **ignoring** **the** **rest** **of** **the** **active** **set**.  
   - **Robust** **statistics:** **min** **is** **extremely** **non-injective** **as** **a** **data** **summary**.

3. **Machinery in those domains**  
   **Tropical** **varieties** **encode** **piecewise-linear** **geometry**; **here** **we** **only** **need** **the** **one-dimensional** **projection** **min_i∈S** **c_i**.

4. **Transfer candidate**  
   **Distinct** **costs** **c_0** **<** **c_1** **<** **⋯** **<** **c_{n−1}**. **If** **both** **S_a** **(sub-quorum)** **and** **S_b** **(quorum)** **contain** **the** **global** **argmin** **index** **0**, **then** **min_{i∈S_a}** **c_i** **=** **min_{i∈S_b}** **c_i** **=** **c_0** **regardless** **of** **|S|**.

## Falsifiable claim

**Claim:** **n = 10**, **t = 6**, **c_i = i**, **S_a = {0,1,2,3,4}**, **S_b = {0,5,6,7,8,9}**. **Define** **h(S) = min_{i∈S} c_i**. **Then** **|S_a| < t ≤ |S_b|** **and** **h(S_a) = h(S_b) = 0**.

**Interpretation if PASS:** **Constant-size** **tropical-style** **“** **best** **participant** **cost** **in** **the** **coalition** **”** **does** **not** **encode** **quorum** **—** **parallel** **to** **023** **(lossy** **count** **bit)** **and** **021** **(linear** **pools)**, **different** **semiring**.

**If FAIL:** **Arithmetic** **mistake**.
