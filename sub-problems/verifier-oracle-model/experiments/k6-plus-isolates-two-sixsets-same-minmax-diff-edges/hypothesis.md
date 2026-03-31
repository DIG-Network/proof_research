# Hypothesis: two quorum-sized sets share (λ_max, λ_min) but differ in |E(induced)|

## Analogy pass

1. **Abstract structure**  
   **028** fixed **|S|** **at** **t** **and** **varied** **whether** **an** **edge** **appears**. Here **|S|=t** **is** **fixed** **and** **we** **ask** **whether** **a** **two-float** **adjacency** **summary** **determines** **even** **the** **number** **of** **internal** **edges** **—** **a** **step** **toward** **digest** **“constant** **summary** **collisions”**.

2. **Where else this structure appears**  
   - **Moment** **matching:** **Different** **laws** **share** **low** **order** **moments**.  
   - **Coarse** **observables** **in** **stat** **mech:** **Same** **pressure** **/** **bulk** **readouts** **from** **distinct** **microstates**.  
   - **Graph** **cospectrality** **lore:** **Extrema** **are** **weaker** **than** **full** **spectrum**.

3. **Machinery in those domains**  
   **Spectrum** **of** **disjoint** **unions:** **repeated** **±1** **from** **multiple** **K_2** **blocks** **still** **has** **λ_max=1,** **λ_min=−1** **as** **for** **a** **single** **K_2** **plus** **zeros**.

4. **Transfer candidate**  
   **Host** **G:** **four** **isolates** **0–3** **and** **three** **disjoint** **edges** **(4,5),** **(6,7),** **(8,9).** **Then** **S_1={0,1,2,3,4,5}** **induces** **one** **edge;** **S_2={0,1,4,5,6,7}** **induces** **two** **disjoint** **edges.** **Both** **yield** **(λ_max,λ_min)=(1,−1).**  
   **Note:** **The** **entry** **028** **host** **K_6∪4K_1** **cannot** **induce** **2K_2** **(any** **four** **core** **vertices** **form** **K_4),** **so** **this** **experiment** **uses** **a** **matching** **core** **to** **realize** **the** **pair.**

## Falsifiable claim

**Claim:** On **G** **as** **above**, **|S_1|=|S_2|=6**, **|E(G[S_1])|=1**, **|E(G[S_2])|=2**, **and** **λ_max,** **λ_min** **of** **A(G[S_i])** **agree** **pairwise** **(numerically)**.

**Interpretation if PASS:** **(λ_max,λ_min)** **is** **not** **injective** **on** **t**-**subsets** **even** **when** **internal** **edge** **count** **differs** **—** **constant** **two-float** **spectral** **summary** **underdetermines** **the** **induced** **pattern**.

**If FAIL:** **Construction** **or** **eigen** **bug**.
