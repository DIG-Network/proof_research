# Notes — clique-induced-adjacency-max-eigenvalue-recovers-size

- **Not a cryptographic result:** The verifier never gets a magic `λ_max` oracle for **G[S]** without knowing **S** or receiving **Ω(|S|²)**-ish structure; this is a **combinatorial positive control** sharpening **025**.
- **Design takeaway:** **Independence number** / **where quorums can sit** in **G** matters: **thick independent sets** ⇒ **spectral collapse**; **clique host** ⇒ **λ_max ∝ |S|** in this toy.
- **Link to main problem:** A **commitment** `C` would need to **pin** a **host graph** (or equivalent interaction pattern) such that **honest** quorums cannot **evade** edges **and** such that **π** makes **λ_max** (or a **constant** proxy) **checkable** — still absent; **026** only shows **when** the **spectral** statistic **would** be informative **if** realized.
