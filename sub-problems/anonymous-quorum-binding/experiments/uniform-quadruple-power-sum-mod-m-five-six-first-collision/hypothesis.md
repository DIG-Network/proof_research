# Hypothesis — first uniform M for quadruple power-sum shell collision (n=10, w_i=i+1)

## Analogy pass

1. **Abstract structure:** **065** **found** **the** **smallest** **`M≥2`** **such** **that** **some** **5-set** **and** **6-set** **agree** **on** **`(Σw^k`** **mod** **`M)`** **for** **`k=1,2,3`** **with** **the** **same** **`M`** **each** **time.** **Adding** **a** **fourth** **moment** **asks** **whether** **the** **first** **collision** **modulus** **moves** **or** **stays** **at** **the** **parity** **barrier.**

2. **Where else:**
   - **Moment** **problems** **in** **statistics:** **higher** **moments** **can** **be** **redundant** **under** **coarse** **(** **modular** **)** **measurement.**
   - **Syndrome** **dimensions** **in** **coding:** **extra** **parity** **checks** **that** **are** **linearly** **dependent** **mod** **`M`.**
   - **Feature** **engineering:** **adding** **a** **derived** **feature** **that** **is** **deterministic** **from** **existing** **ones** **does** **not** **refine** **the** **partition.**

3. **Machinery:** **Exhaustive** **`C(10,5)`** **and** **`C(10,6)`** **power** **sums** **`p1..p4`;** **scan** **`M`** **ascending** **for** **key** **`(p1%M,…,p4%M)`** **collision** **across** **shells.**

4. **Transfer candidate:** **If** **`M=2`** **remains** **first** **with** **the** **same** **or** **an** **equivalent** **witness,** **the** **fourth** **uniform** **moment** **does** **not** **delay** **the** **065** **collapse** **—** **encoding** **the** **binding** **vector** **must** **use** **independent** **information** **mod** **`M`,** **larger** **`M`,** **or** **non-moment** **structure.**

## Falsifiable claim

**There** **exists** **`M≥2`** **(** **smallest** **found** **by** **lex** **scan** **)** **such** **that** **two** **distinct** **subsets** **of** **sizes** **5** **and** **6** **share** **`(p1%M,p2%M,p3%M,p4%M)`** **for** **`w_i=i+1`.** **(** **Script** **reports** **that** **`M`** **and** **witnesses** **;** **expect** **`M=2`.)**
