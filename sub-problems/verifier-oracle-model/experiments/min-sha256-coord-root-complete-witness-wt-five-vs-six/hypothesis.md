# Hypothesis — min-SHA256 among **coordinate**-root + 067-subtree witnesses (d=5)

## Analogy pass

1. **Abstract structure:** **071** **fixed** **the** **root** **to** **pair-XOR** **and** **varied** **(** **i,j** **)** **—** **45** **feasible** **roots,** **unique** **min** **digest.** **The** **066** **/** **067** **language** **also** **allows** **coordinate** **splits** **`x_i`** **at** **internal** **nodes.** **Restricting** **the** **root** **to** **coordinate** **only** **defines** **another** **finite** **family** **of** **nested** **JSON** **witnesses** **(** **same** **child** **constructor** **067** **`witness`** **).**

2. **Where else:**
   - **Decision** **trees** **with** **categorical** **vs** **interaction** **features** **at** **the** **top** **split** **—** **different** **root** **families** **yield** **different** **model** **classes.**
   - **Syntax** **:** **clause** **ordering** **in** **CNF** **—** **same** **semantics,** **many** **surface** **forms** **unless** **canon.**
   - **API** **versioning:** **two** **compatible** **entry** **points** **(** **“by** **id”** **vs** **“by** **tag”** **)** **that** **must** **not** **be** **conflated** **without** **a** **spec.**

3. **Machinery:** **For** **each** **`i`** **∈** **`{0..n−1}`** **test** **`exists_tree(S0,** **d−1)`** **∧** **`exists_tree(S1,** **d−1)`** **after** **`split_coord(full,** **i)`;** **build** **`("C",** **i,** **…)`** **+** **`witness`** **on** **children;** **`sha256(json)`** **as** **071.**

4. **Transfer candidate:** **Report** **`feasible_coord_root_count`,** **`min_sha256`,** **`minimizer_count`,** **and** **whether** **min** **equals** **067** **default** **and** **/** **or** **071’s** **XOR-min** **hash** **—** **clarifies** **whether** **“global** **min** **over** **mixed** **root** **types”** **would** **need** **a** **union** **scan** **or** **stays** **in** **one** **family.**

## Falsifiable claims (script checks all)

**C1:** **The** **set** **`G`** **=** **`{** **i** **:** **coord** **root** **i** **feasible** **at** **d=5** **}`** **is** **non-empty.**

**C2:** **Among** **hashes** **`{** **h(i)** **:** **i** **∈** **G** **}`,** **the** **number** **of** **indices** **achieving** **`min`** **is** **recorded** **(** **unique** **min** **⇔** **count** **1** **).**

**Secondary** **(** **not** **required** **for** **PASS** **):** **Compare** **`min_coord`** **to** **hard-coded** **071** **XOR-min** **and** **067** **default** **from** **a** **single** **run** **of** **the** **same** **`witness`** **/** **JSON** **conventions.**
