# Analogy pass

## 1. Abstract structure

**092** **showed** **on** **(10,{5,6})** **that** **one** **total** **XOR** **splits** **the** **two** **Hamming** **shells.** **Consecutive** **integers** **k** **and** **k+1** **always** **have** **opposite** **parity,** **so** **popcount(x) mod 2** **labels** **wt=k** **vs** **wt=k+1** **disjointly** **on** **{0,1}ⁿ** **—** **no** **cryptographic** **content,** **but** **the** **verifier-oracle** **line** **should** **record** **it** **as** **the** **general** **pattern** **behind** **`min_d=1`** **when** **full** **parity** **is** **allowed.**

## 2. Analogues

1. **Single-bit** **syndrome** **separating** **even** **/** **odd** **weight** **cosets** **in** **binary** **codes.**
2. **Parity** **track** **in** **RAID** **/** **checksum** **designs.**
3. **Handshaking** **lemma** **(** **n** **odd** **)** **in** **graph** **theory** **—** **different** **theorem,** **same** **“parity** **is** **a** **perfect** **classifier** **for** **a** **pair** **of** **integer** **types”** **flavour.**

## 3. Machinery

**Exhaustive** **shell** **enumeration** **via** **`itertools.combinations`** **for** **small** **n** **;** **tautology** **check** **for** **larger** **n** **(** **no** **2ⁿ** **scan** **).**

## 4. Transfer seed

**H:** **For** **all** **tested** **(n,k),** **partition** **by** **⊕ᵢ xᵢ** **splits** **shell** **k** **from** **shell** **k+1** **exactly** **on** **the** **union** **domain.**

---

# Formal hypothesis

**Lemma** **(** **regression** **):** **Fix** **n≥1,** **0≤k<n.** **Let** **S = {x∈{0,1}ⁿ : |x|∈{k,k+1}}.** **Define** **π(x)=⊕ᵢ xᵢ.** **Then** **π⁻¹(0)∩S** **=** **{x:|x|=k}** **if** **k** **even** **else** **{x:|x|=k+1},** **and** **π⁻¹(1)∩S** **is** **the** **other** **shell** **(** **equivalently** **both** **restricted** **sides** **are** **`pure_bits`** **-** **pure** **for** **the** **{k,k+1}** **predicate** **).**

**Script** **verifies** **via** **explicit** **masks** **for** **n≤N_MAX** **and** **checks** **k⊕(k+1)=1** **for** **n≤N_TAUTO.**
