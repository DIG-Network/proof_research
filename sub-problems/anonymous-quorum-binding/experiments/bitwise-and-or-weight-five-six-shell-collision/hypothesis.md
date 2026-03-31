# Analogy pass

## 1. Abstract structure

**Threshold** **binding** **toys** **map** **each** **subset** **S** **⊂** **[n]** **to** **a** **small** **public** **fingerprint** **h(S).** **If** **the** **same** **h** **arises** **for** **some** **|S|=t−1** **and** **some** **|S|=t** **witness,** **h** **cannot** **by** **itself** **certify** **“at** **least** **t** **signers”** **in** **that** **model.**

## 2. Analogues

1. **Multiplicative** **/ ** **bitwise** **fingerprints** **in** **hashing** **—** **AND/OR** **mix** **information** **nonlinearly** **unlike** **Σ** **w.**
2. **Idempotent** **semirings** **(** **(ℕ,∧,∨)** **on** **bit** **representations** **)** **—** **different** **algebra** **than** **034** **additive** **mod.**
3. **063** **joint** **(Σ,Π)** **—** **already** **collapsed** **across** **shells;** **bitwise** **ops** **are** **another** **“compact”** **combine** **of** **labels.**

## 3. Machinery

**Enumerate** **all** **5**- **and** **6**-**subsets** **of** **[0..9],** **weights** **w_i=i+1.** **Define** **h_and(S)=⋀_{i∈S} w_i,** **h_or(S)=⋁_{i∈S} w_i** **(** **integer** **bitwise** **).** **Compare** **image** **sets** **across** **shells.**

## 4. Transfer seed

**Hypothesis:** **At** **least** **one** **of** **h_and,** **h_or** **shares** **a** **value** **between** **the** **|S|=5** **and** **|S|=6** **families** **(** **cross-shell** **collision** **)** **—** **so** **neither** **is** **a** **shell** **separator** **alone** **(** **same** **pattern** **as** **034,** **050,** **061** **)** **.**

---

# Formal hypothesis

**H:** **For** **n=10,** **w_i=i+1,** **there** **exist** **S₅,** **S₆** **with** **|S₅|=5,** **|S₆|=6** **such** **that** **h_and(S₅)=h_and(S₆)** **and** **similarly** **for** **h_or** **(** **possibly** **different** **witness** **pairs** **).**

**Falsification:** **Empty** **intersection** **of** **images** **for** **either** **summary** **(** **would** **mean** **that** **summary** **alone** **separates** **the** **two** **shells** **on** **this** **toy** **).**

**Outcome:** **PASS** **—** **both** **h_and** **and** **h_or** **share** **values** **across** **|S|=5** **vs** **6** **(** **see** **`results.md`** **).**
