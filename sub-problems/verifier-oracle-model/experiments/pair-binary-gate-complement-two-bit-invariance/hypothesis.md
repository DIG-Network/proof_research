# Hypothesis: two-bit gates invariant under simultaneous input complement

## Analogy pass

1. **Abstract structure:** A verifier’s atomic probe is a Boolean function \(f(x_i,x_j)\) of two bits. Global vector complement \(x \mapsto x \oplus \mathbf{1}\) flips every coordinate, hence flips both arguments of every pair query together. If \(f(a,b)=f(1-a,1-b)\) for all \(a,b\in\{0,1\}\), then the entire transcript of such pair queries is invariant under that global involution — the mechanism behind entry 049 when complement also swaps the two Hamming shells.

2. **Where else does this structure appear?**
   - **Physics:** observables even under spin flip (Ising \(Z_2\) symmetry) — only symmetric combinations of local spins survive the quotient.
   - **Signal processing:** AC coupling removes DC; differential readouts cancel common-mode offsets — same algebra as XOR vs AND on pairs.
   - **Boolean logic synthesis:** negative unate vs binate gates under De Morgan / input polarity.

3. **Machinery:** Classify 2-input gates by the involution \((a,b)\mapsto(1-a,1-b)\) on \(\{0,1\}^2\).

4. **Transfer seed:** Enumerate standard gates (AND, OR, XOR, XNOR / equality) for two-bit complement invariance; predict which pair-oracle alphabets inherit 049-style global-complement orbits on every query node.

## Formal claim

For \(f:\{0,1\}^2\to\{0,1\}\), define **two-bit complement invariance** as \(\forall a,b:\ f(a,b)=f(1-a,1-b)\).

**H1:** Among \(\{\mathrm{AND},\mathrm{OR},\mathrm{XOR},\mathrm{XNOR}\}\), exactly XOR and XNOR satisfy this property. (The script also checks NAND and NOR.)

**H2:** Under global \(x\mapsto x\oplus \mathbf{1}\), any decision tree whose internal nodes use only XOR or only XNOR on pairs has the same root-to-leaf path for \(x\) and \(x\oplus\mathbf{1}\) (hence 049 applies when weights swap across shells). AND/OR nodes can break that orbit at individual queries (though 048 shows depth can still be large).

The script exhaustively checks all \((a,b)\) for each named gate.
