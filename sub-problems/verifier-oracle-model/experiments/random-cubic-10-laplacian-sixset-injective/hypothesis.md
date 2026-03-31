# Hypothesis: some random 3-regular n=10 host has injective 6-set Laplacian spectra

## Analogy pass

1. **Abstract structure**  
   **032** showed **full** **sorted** **induced** **Laplacian** **spectra** **can** **coincide** **for** **two** **quorum** **6**-**sets** **on** **Petersen** **—** **symmetry** **/ ** **isomorphic** **induced** **patterns** **are** **the** **suspect** **mechanism.** **We** **ask** **whether** **removing** **that** **highly** **symmetric** **host** **(same** **degree** **sequence,** **still** **3-regular** **expander-like** **toy)** **can** **make** **the** **210** **spectra** **pairwise** **distinct** **—** **i.e.** **the** **map** **S ↦ spec(L(G[S]))** **injective** **on** **C(10,6)** **for** **some** **labeled** **G**.

2. **Where else this structure appears**  
   - **Graph canonization / Nauty:** **Distinguishing** **vertices** **by** **the** **multiset** **of** **k**-**neighborhood** **types** **—** **sometimes** **injective,** **sometimes** **not.**  
   - **Statistical identifiability:** **Parameters** **recoverable** **iff** **the** **observation** **map** **is** **injective** **on** **the** **parameter** **set.**  
   - **Coding:** **Syndrome** **map** **injective** **on** **codewords** **below** **Gilbert–Varshamov** **—** **here** **“codewords”** **are** **6**-**subsets** **and** **“syndrome”** **is** **continuous** **spectrum.**

3. **Machinery**  
   Random **graph** **models** **break** **global** **automorphisms** **generically;** **exhaustive** **bucket** **test** **on** **210** **subsets** **gives** **a** **concrete** **finite** **check.**

4. **Transfer candidate**  
   **`networkx.random_regular_graph(3, 10, seed)`** **—** **reproducible** **simple** **cubic** **samples** **(faster** **than** **hand-rolled** **configuration** **reject** **loops).** **Exhaust** **seeds** **0..N−1** **and** **test** **injectivity** **of** **S ↦ spec(L(G[S]))** **on** **all** **6**-**subsets.**

## Falsifiable claim

**Claim:** There exists an integer **seed** in **`[0, N)`** (**N = 100 000** **in** **script)** such that **G = random_regular_graph(3, 10, seed)** **has** **all** **C(10,6)=210** **sorted** **induced** **Laplacian** **spectra** **on** **|S|=6** **pairwise** **distinct** **(eigenvalues** **rounded** **to** **8** **decimals,** **same** **convention** **as** **032).**

**PASS** ⇒ **at** **least** **one** **“asymmetric”** **random** **cubic** **host** **admits** **injective** **full** **Laplacian** **6**-**vector** **summary** **on** **quorum** **subsets** **in** **this** **model.**  
**FAIL** ⇒ **no** **such** **host** **in** **seeds** **0..N−1** **—** **evidence** **collisions** **persist** **for** **generic** **labeled** **cubics** **in** **this** **sample** **(not** **only** **Petersen** **automorphisms).** **Observed** **in** **run:** **N = 100 000.**
