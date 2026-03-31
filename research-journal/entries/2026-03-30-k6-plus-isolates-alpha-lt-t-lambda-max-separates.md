# 2026-03-30 — k6-plus-isolates-alpha-lt-t-lambda-max-separates

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/k6-plus-isolates-alpha-lt-t-lambda-max-separates/`

**Context:** `verifier-oracle-model`

**Hypothesis (summary):** **G = K_6** **∪** **4K_1** **on** **n=10**, **t=6**, **α(G)=5<t**; **S_a** **(5** **verts)** **independent** **⇒** **λ_max=0**; **S_b** **(6** **verts)** **contains** **edge** **⇒** **λ_max=1**.

**Outcome:** **PASS**

**Key finding:** **Positive** **control** **for** **digest** **“**α(G)** **<** **t**” **—** **forced** **internal** **edge** **at** **quorum** **can** **separate** **λ_max** **from** **the** **sub-threshold** **independent** **witness**; **complements** **025**/**027** **(α** **≥** **t** **collapse)** **and** **026** **(full** **clique** **host)**.

**Implications:**

- **Spectral** **straw** **models** **should** **explicitly** **relate** **committed** **G** **to** **α(G)** **vs** **t**.
- **Remaining** **open:** **expander** **/** **d-regular** **random**, **and** **constant** **features** **beyond** **λ_max** **under** **collision** **pressure**.

**Analogy pass summary:** **Ramsey** **/** **core–periphery** **/** **threshold** **access** **on** **dense** **core** — **seed:** **α** **<** **t** **forces** **hitting** **an** **edge**.
