# Outcome: PASS

## Commands (parent script)

Path: `../adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`

Shared flags: `--skip-baseline --d-min 2 --d-max 2 --lru-maxsize 0`

| r | Command fragment | XOR splits | build_sec | dp_sec | d=2 feasible |
|---|------------------|------------|-----------|--------|--------------|
| 2 | `--r-single 2` | 91 | 0.071 | 0.027 | **False** |
| 3 | `--r-single 3` | 364 | 0.359 | 0.433 | **False** |
| 4 | `--r-single 4` | 1001 | 1.150 | 2.812 | **False** |

## Interpretation

For **`n=14`**, **`{7,8}`**, **coord + r-sparse XOR** alone at **`r∈{2,3,4}`**, separating the two shells at depth **`≤2`** is **impossible** (**`min_d ≥ 3`** for each of these single-arity menus).

## Ancillary probe (same host)

**`r=5`**, **`d=3`-only:** `timeout 300 python3 …/script.py --skip-baseline --r-single 5 --d-min 3 --d-max 3 --lru-maxsize 0` → **exit 124** (no **`d=3` feasibility** line within **300 s**).
