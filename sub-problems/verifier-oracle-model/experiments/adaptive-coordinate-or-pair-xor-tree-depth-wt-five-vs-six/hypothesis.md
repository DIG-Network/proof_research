# Hypothesis — mixed coordinate + pair-XOR trees beat depth n on wt {5,6}

## Analogy pass

1. **Abstract structure:** **045** **showed** **coordinate-only** **adaptive** **trees** **need** **worst-case** **depth** **n=10** **to** **separate** **Hamming** **wt** **5** **vs** **6** **on** **{0,1}^10** **(pair** **of** **masks** **differing** **only** **at** **one** **unqueried** **bit** **forces** **that** **bit).** **049** **showed** **pair-XOR-only** **trees** **can** **be** **shallow** **for** **(n,T)=(6,4)** **but** **are** **impossible** **when** **n=2T−1** **(here** **n=10,** **T=6** **gives** **9≠10,** **so** **XOR-only** **is** **not** **ruled** **out** **by** **that** **lemma** **—** **actually** **n=10,** **t=6** **⇒** **2t−1=11≠10,** **complement** **lemma** **does** **not** **apply** **to** **XOR-only** **for** **5** **vs** **6).** **Mixed** **gates** **are** **the** **natural** **next** **knob** **in** **the** **digest** **“Next”** **line.**

2. **Where else:**
   - **Decision** **tree** **ensembles** **/ ** **oblique** **splits:** **allowing** **non-axis-aligned** **cuts** **can** **reduce** **depth** **vs** **axis-only.**
   - **Circuit** **complexity:** **AC⁰** **with** **both** **variables** **and** **⊕** **of** **two** **variables** **as** **literals** **—** **richer** **local** **basis.**
   - **Medical** **testing** **panels:** **combine** **single-marker** **and** **difference** **scores** **to** **split** **cohorts** **faster.**

3. **Machinery:** **Same** **backtracking** **as** **045** **/** **049,** **but** **at** **each** **internal** **node** **the** **split** **may** **be** **either** **x_i** **or** **x_i⊕x_j** **(i<j).** **Memoize** **on** **(sorted** **tuple** **S,** **depth_remaining).** **Binary** **search** **/** **increment** **d** **from** **1** **to** **find** **minimum** **depth** **of** **a** **perfect** **separator** **tree.**

4. **Transfer candidate:** If **min** **depth** **<** **n,** **PASS** **positive** **—** **mixed** **pair-local** **F₂** **probes** **+** **coordinates** **strictly** **help** **the** **verifier-oracle** **toy** **vs** **045.** If **still** **n,** **FAIL** **for** **“beat** **axis** **depth”** **but** **still** **data** **(** **no** **gain** **from** **this** **mix** **in** **worst** **case** **).**

## Falsifiable claim

Let **D_mix** **be** **the** **minimum** **depth** **of** **any** **adaptive** **binary** **tree** **that** **splits** **the** **462** **masks** **with** **wt∈{5,6}** **into** **pure** **leaves,** **where** **each** **internal** **node** **is** **either** **branch** **on** **x_i** **or** **on** **x_i⊕x_j.** **Hypothesis** **for** **PASS** **(positive** **surprise):** **D_mix** **≤** **9.** **Opposite** **(null):** **D_mix** **=** **10** **(same** **as** **coordinate-only).**
