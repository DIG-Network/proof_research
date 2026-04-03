# Hypothesis

**Claim:** For `n=5`, with the **weight-2-only** mask shell (`C(5,2)=10` masks), the mixed language **coord + ⋃_{r=2}^4 XOR_r** still has **minimum certificate depth `min_d = 1`**.

**Rationale:** The recent FAIL at **`{2,3}` shell + union `r=2..4`** showed **`min_d=2`**, while **`{2}` + `r=2..3`** had **`min_d=1`**. This ablation **holds the shell at `{2}`** and **extends the union to `r=2..4`** (25 XOR splits, matching the arity-menu shape used at `n=6`). If **`min_d` stays 1**, then the jump to depth 2 is **not** explained by adding **`r=4` splits alone**; it implicates the **enlarged mask shell** (weight-3 masks) interacting with the union.

## Analogy pass (mandatory)

1. **Abstract structure:** A discrete language (coordinate splits ∪ families of parity splits over a mask alphabet) has a **minimal decision-tree depth** over the full subset lattice. Changing either the **alphabet** (which masks exist) or the **split menu** (which XOR arities are available) can alter that depth; we want to know **which change** is responsible for a observed depth bump.

2. **Analogous domains:** (i) **VC-dimension / teaching dimension** — which concept class fragments first when adding a new hypothesis versus adding a new dimension of variation. (ii) **Circuit depth** — adding a layer of gates vs widening fan-in can both increase depth, but blame attribution differs. (iii) **Statistical models** — **main effect vs interaction**: two factors together produce a qualitative change that neither produces alone.

3. **Machinery in those domains:** Shattering arguments; structural lower bounds via communication complexity; **interaction plots** / ANOVA-style decomposition of which term causes a threshold crossing.

4. **Seed for this test:** Treat **mask shell** and **XOR-union arity set** as **two factors** and run a **one-factor-at-a-time** ablation on the factor that was confounded in the prior experiment (**union extended** vs **shell extended**).

**Falsification:** Observing **`min_d=2`** here would mean **r=4 alone** (at fixed `{2}` shell) suffices for the depth-2 phenomenon, weakening the “shell-dependent / weight-3 interaction” story.
