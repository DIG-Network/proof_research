# Notes — mixed-coordinate-xor-tree-witness-xor-first-wt-five-vs-six

## Implementation

- **`exists_tree`:** **Same** **as** **066** **(** **`recurse_children(exists_tree, S0, S1, depth_remaining)`** **with** **child** **depth** **decrement** **inside** **`recurse_children`** **).**
- **`witness_xor_first`:** **Pair-XOR** **loops** **before** **coordinate** **loops** **at** **every** **node.**

## Finding

- **JSON** **equality** **with** **067** **implies** **the** **root** **(** **and** **entire** **tree** **)** **is** **unchanged** **—** **likely** **because** **no** **coordinate** **root** **split** **is** **feasible** **at** **d=5,** **and** **(0,1)** **is** **the** **first** **feasible** **XOR** **under** **lex** **order** **whether** **we** **scan** **coords** **or** **XORs** **first** **in** **the** **witness** **constructor.**

## Next

- **Force** **a** **different** **witness** **(** **e.g.** **second** **successful** **XOR** **at** **root** **if** **enumerated** **)** **or** **a** **smaller** **hand-built** **instance** **where** **coord** **and** **XOR** **both** **win** **at** **the** **root** **to** **separate** **tie-breaks.**
