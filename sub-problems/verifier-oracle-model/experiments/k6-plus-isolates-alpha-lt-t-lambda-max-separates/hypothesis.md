# Hypothesis: K_6 plus four isolates — α < t forces λ_max > 0 at quorum

## Analogy pass

1. **Abstract structure**  
   Entries **025**/**027** collapse **(λ_max, λ_min)** when **α(G) ≥ t** allows **quorum** and **sub-quorum** **inside** one **large** **independent** **set** (**empty** induced **adjacency**). After **027**, the digest **open** **line** asks what happens when **α(G) < t** so **every** **|S| ≥ t** **must** **contain** **an** **internal** **edge**. We test whether **that** **forces** a **one-float** **λ_max** **gap** **across** **t** **for** **explicit** **witness** **sets**.

2. **Where else this structure appears**  
   - **Ramsey / Turán:** **Bounding** **α(G)** **forces** **edges** **in** **large** **subgraphs** — same **pigeonhole** **as** **“**6** **pigeons**, **5** **holes**” **for** **quorum** **vs** **clique** **core**.  
   - **Percolation / core–periphery:** A **dense** **core** **plus** **sparse** **periphery** — **large** **enough** **samples** **hit** **the** **core** **twice**.  
   - **Access structures:** **Threshold** **t** **on** **participants** **intersects** **every** **“**high**-**connectivity**” **region** **once** **α** **is** **small**.

3. **Machinery in those domains**  
   **Independence** **number** **calculation**; **induced** **subgraph** **spectrum** **for** **disjoint** **union** **K_2** **∪** **4K_1**.

4. **Transfer candidate**  
   **G = K_6** **∪** **4K_1** (**n=10**): **α(G)=5** **(four** **isolates** **+** **one** **clique** **vertex)**. **t=6** **⇒** **α < t**. **S_a** **=** **four** **isolates** **+** **one** **clique** **vertex** **⇒** **independent**, **λ_max=0**. **S_b** **=** **four** **isolates** **+** **two** **adjacent** **clique** **vertices** **⇒** **induced** **K_2**, **λ_max=1**.

## Falsifiable claim

**Claim:** With **G** **as** **above** **on** **vertices** **0–3** **isolates**, **4–9** **a** **K_6**, **t=6**, **S_a = {0,1,2,3,4}**, **S_b = {0,1,2,3,4,5}**, we have **λ_max(A(G[S_a])) = 0** **and** **λ_max(A(G[S_b])) = 1**.

**Interpretation if PASS:** **Positive** **control** **matching** **digest** **“**α(G)** **<** **t**” **—** **forced** **edge** **at** **quorum** **can** **lift** **λ_max** **off** **zero** **while** **sub-quorum** **witness** **stays** **independent**; **pairs** **with** **026** **(clique** **host)** **and** **contrasts** **025**/**027**.

**If FAIL:** **Bug** **in** **adjacency** **construction** **or** **eigen** **computation**.
