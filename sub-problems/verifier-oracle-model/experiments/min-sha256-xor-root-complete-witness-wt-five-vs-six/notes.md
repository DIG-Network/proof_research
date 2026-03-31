# Notes

- **070** proved **multiplicity** **of** **valid** **XOR-root** **+** **067-child** **plans** **(** **45** **).** **071** shows **a** **simple** **global** **tie-break** **—** **minimal** **SHA256** **of** **canonical** **JSON** **—** **picks** **a** **unique** **root** **(** **6,7** **)** **in** **that** **family** **on** **this** **toy.**

- **Caveats:** **(1)** **Only** **root** **forced** **to** **XOR;** **subtrees** **still** **follow** **067** **`witness`** **(** **coord-before-XOR** **at** **each** **internal** **node** **).** **Different** **subtree** **tie-breaks** **could** **add** **more** **JSON** **variants** **not** **scanned** **here.** **(2)** **Min-hash** **is** **not** **monotone** **in** **(** **i,j** **)** **—** **(** **6,7** **)** **wins** **over** **lex** **(** **0,1** **),** **(** **0,2** **),** **etc.**

- **Interface:** **If** **binding** **is** **required,** **specify** **either** **deterministic** **construction** **(** **067** **)** **or** **an** **explicit** **canonical** **map** **(** **e.g.** **min** **hash** **over** **a** **closed** **finite** **set** **)** **—** **they** **disagree** **here.**

- **Next** **(** **optional** **):** **Enumerate** **all** **depth-5** **mixed** **trees** **(** **not** **only** **XOR** **root** **)** **is** **likely** **infeasible;** **partial:** **scan** **internal** **ambiguity** **at** **fixed** **depth** **on** **smaller** **|** **S** **|** **.**
