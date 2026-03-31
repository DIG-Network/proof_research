# Hypothesis — injective SHA256 on XOR-root + 067-child family (d=5)

## Analogy pass

1. **Abstract structure:** **070** **listed** **45** **feasible** **root** **pairs** **(** **i,j** **)** **and** **071** **showed** **a** **unique** **minimum** **digest** **—** **but** **uniqueness** **of** **the** **minimum** **does** **not** **imply** **all** **45** **digests** **differ.** **If** **two** **distinct** **roots** **yielded** **the** **same** **canonical** **JSON** **(** **or** **same** **hash** **)** **the** **prover** **could** **swap** **roots** **without** **changing** **`π_tree`** **bytes** **—** **weaker** **than** **070’s** **observed** **hash** **difference** **for** **(0,1)** **vs** **(0,2).**

2. **Where else:**
   - **Injective** **labeling** **in** **graph** **isomorphism** **certificates** **—** **distinct** **structures** **should** **map** **to** **distinct** **normal** **forms.**
   - **Hash** **as** **fingerprint** **in** **dedup** **stores** **—** **collision** **analysis** **for** **bounded** **domains.**
   - **Coding:** **constant-weight** **codes** **with** **distinct** **syndromes** **for** **each** **message.**

3. **Machinery:** **Enumerate** **feasible** **(** **i,j** **),** **build** **witness,** **`sha256(json)`** **and** **optionally** **raw** **`json.dumps`** **string;** **compare** **`|set(hashes)|`** **to** **45.**

4. **Transfer candidate:** **PASS** **if** **45** **distinct** **digests** **⇒** **each** **feasible** **root** **choice** **is** **separated** **by** **this** **fingerprint** **(** **empirical** **on** **this** **toy** **).** **FAIL** **if** **collision** **—** **print** **witness** **pairs** **for** **debug.**

## Falsifiable claim

**Let** **F** **be** **the** **set** **of** **feasible** **pair-XOR** **roots** **at** **depth** **≤5** **(** **as** **in** **070** **).** **For** **each** **(** **i,j** **)** **∈** **F** **let** **h(i,j)** **=** **SHA256** **of** **canonical** **JSON** **of** **the** **XOR-root+067-child** **tree.** **Then** **|** **{** **h(i,j)** **:** **(** **i,j** **)** **∈** **F** **}** **|** **=** **|** **F** **|** **(** **injective** **on** **this** **finite** **family** **).**
