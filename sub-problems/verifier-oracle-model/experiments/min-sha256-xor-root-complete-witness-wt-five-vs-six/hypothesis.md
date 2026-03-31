# Hypothesis — min-SHA256 pins a unique XOR root? (n=10, wt {5,6}, d=5)

## Analogy pass

1. **Abstract structure:** **070** **showed** **45** **feasible** **pair-XOR** **roots** **each** **compatible** **with** **depth** **≤5** **when** **subtrees** **use** **067’s** **`witness`.** **To** **bind** **`π_tree`** **without** **revealing** **the** **prover’s** **order** **of** **discovery,** **one** **standard** **trick** **is** **a** **public** **tie-break** **—** **e.g.** **minimal** **digest** **under** **a** **fixed** **serialization.**

2. **Where else:**
   - **Consensus** **/** **leader** **election:** **break** **symmetry** **with** **minimal** **VRF** **output** **or** **minimal** **hash** **of** **a** **candidate.**
   - **Merkle** **proof** **canonicalization** **in** **blockchains:** **sort** **siblings** **or** **pick** **min** **encoding** **so** **verifiers** **agree.**
   - **SAT** **model** **enumeration:** **“minimal** **model”** **under** **a** **total** **order** **on** **literals** **—** **unique** **if** **no** **ties.**

3. **Machinery:** **Totally** **order** **SHA256** **hex** **strings** **(** **=** **lex** **on** **bytes** **of** **digest** **)** **or** **order** **canonical** **JSON** **bytes** **before** **hash;** **count** **how** **many** **feasible** **roots** **hit** **the** **minimum.**

4. **Transfer candidate:** **If** **exactly** **one** **(** **i,j** **)** **minimizes** **`sha256(json.dumps(tree,** **sort_keys=True,** **...))`**, **then** **`π_tree`** **can** **be** **pinned** **by** **that** **rule** **within** **this** **restricted** **family** **(** **XOR** **root** **+** **067** **subtrees** **).** **Ties** **⇒** **the** **min-hash** **rule** **is** **still** **ambiguous** **here.**

## Falsifiable claim

**Let** **F** **be** **the** **set** **of** **pair** **indices** **(** **i<j** **)** **such** **that** **the** **full** **462-set** **splits** **by** **`x_i⊕x_j`** **at** **the** **root** **and** **both** **sides** **admit** **`exists_tree(...,** **4).** **For** **each** **(** **i,j** **)** **∈** **F,** **build** **the** **nested** **witness** **with** **067** **`witness`** **on** **each** **non-empty** **child** **(** **depth** **budget** **4** **).** **Let** **h(i,j)** **=** **SHA256** **of** **canonical** **JSON** **(** **same** **as** **070** **).** **Claim:** **|{** **(** **i,j** **)** **∈** **F** **:** **h(i,j)** **=** **min_{F}** **h** **}|** **=** **1** **(** **unique** **minimizer** **).**
