# Hypothesis: adaptive coordinate trees need depth **n** to separate **wt=5** **vs** **6** **(n=10)**

## Analogy pass

1. **Abstract structure.** **A** **binary** **decision** **tree** **reads** **coordinates** **of** **a** **hidden** **vector;** **two** **inputs** **that** **agree** **on** **every** **queried** **variable** **before** **the** **leaf** **cannot** **be** **told** **apart** **—** **same** **as** **active** **learning** **with** **axis-aligned** **splits.**

2. **Where else.** **PAC** **learning** **depth** **of** **threshold** **functions;** **twenty** **questions** **with** **restricted** **question** **class;** **comparison** **trees** **for** **sorting** **(lower** **bounds** **via** **adversarial** **input** **pairs).**

3. **Machinery.** **If** **x,** **y** **differ** **only** **at** **coordinate** **j,** **any** **query** **i≠j** **returns** **the** **same** **bit** **for** **both** **—** **they** **follow** **the** **same** **path** **until** **j** **is** **queried.** **Adjacent** **Hamming** **layers** **wt** **5** **and** **6** **contain** **such** **pairs** **for** **every** **j.**

4. **Transfer seed.** **037** **(non-adaptive** **|Q|≤4)** **does** **not** **by** **itself** **prove** **the** **adaptive** **depth-4** **claim** **in** **the** **digest;** **this** **search** **certifies** **the** **stronger** **statement** **min** **depth** **=** **n** **for** **coordinate-only** **trees** **on** **this** **domain.**

## Falsifiable claim

**Backtracking** **with** **memoization** **reports** **`exists_tree(full,** **d)** **=** **False** **for** **d** **=** **1..9** **and** **True** **for** **d** **=** **10,** **where** **`full`** **is** **all** **10**-**bit** **masks** **with** **weight** **5** **or** **6.**

**Expected:** **PASS.**
