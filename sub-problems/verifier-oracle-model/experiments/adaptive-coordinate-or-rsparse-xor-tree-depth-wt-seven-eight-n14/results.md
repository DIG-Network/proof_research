# Outcome: INCONCLUSIVE (partial `min_d(r)` row; heavy `r` / unions not finished)

## Baseline (`--baseline-only`, `--lru-maxsize 4000000`)

- **Domain:** `n=14`, `|S| ∈ {7,8}`, `|masks| = C(14,7)+C(14,8) = 6435`, majority `t=8`.
- **coord-only:** `min_d = 14` (probed `d=1..14`; `d=14` feasible).
- **coord + full 14-XOR:** `min_d = 1` (`d=1` feasible).
- **Wall time (automation host):** coord-only phase ~137 s; full-XOR phase negligible.

**H1 (hypothesis.md):** confirmed for the baseline slice.

## Single-arity row (`--skip-baseline --r-single r`, default LRU 4M)

Completed shards (PASS printed by script; baseline not re-run):

| r | XOR splits | min_d | notes |
|---|------------|-------|-------|
| 13 | 14 | 2 | fast |
| 12 | 91 | 3 | |
| 11 | 364 | 4 | |
| 10 | 1001 | 3 | dp ~46 s |
| 9 | 1001 | — | **`d=3` still open:** **`timeout 1200` (20 min)** and **`timeout 5400` (90 min)** on **`d=3` only** via **`--d-min 3 --d-max 3`**, **`--lru-maxsize 0`**, **`--skip-baseline`** — no feasibility line (exit **124**). Prior **`d=1,2`** known **false** from full sweep start. |
| 8 | 3003 | 3 | dp ~397 s |
| 7 | 3432 | 2 | |
| 6 | 3003 | 3 | dp ~419 s |
| 5 | 2002 | **≥3** | **`d=2` decided false (2026-04-01):** **`--skip-baseline --r-single 5 --d-min 2 --d-max 2 --lru-maxsize 0`** → **`d=2 feasible=False`**, **`dp_sec≈14`**. **`d=3`** still **open** here (**prior `timeout 2400` on `d=3`**). |
| 4 | 1001 | **≥3** | **`d=2` decided false (2026-04-01):** **`--skip-baseline --r-single 4 --d-min 2 --d-max 2 --lru-maxsize 0`** → **`d=2 feasible=False`**, **`dp_sec≈2.8`**. Prior full-row timeouts were deeper-**`d`** probes, not **`d=2`** isolation. |
| 3 | 364 | **≥3** | **`d=2` decided false (2026-04-01):** **`dp_sec≈0.43`**. |
| 2 | 91 | **≥3** | **`d=2` decided false (2026-04-01):** **`dp_sec≈0.03`**. |

**Prefix actually known:** `r=13..6` only, in order of increasing `r` index in the full row:

`min_d(13)=2, min_d(12)=3, min_d(11)=4, min_d(10)=3, min_d(9)=?, min_d(8)=3, min_d(7)=2, min_d(6)=3`.

**Update (2026-04-01):** **`r=5`:** **`d=2` false** (**fast**); **`d=3`** still **not** **decided** on this track (**timeouts**).

Equivalently, scanning `r=2..13` left-to-right, positions **`r=2..4`:** **`d=2` false** ⇒ **`min_d≥3`** (**fast** **shards**, **2026-04-01**); **`r=5`:** **`d=2` false**, **`d=3` open**; **`r=9`:** **`d=1,2` false**; **`d=3` not decided** within **90 min** wall on **`d=3`-only** run (**unbounded** memo). **Automation note:** **`r=5` `d=3`** did not finish within **`timeout 300`** (**5 min**) on one cron host (**exit 124**).

## Unions (all `--skip-baseline`, LRU 4M)

| probe | outcome |
|-------|---------|
| `2,3,4` | **`timeout 600`** — stuck `d=3` |
| `2,3,4,5` | **`timeout 7200` (2 h)** — stuck `d=3` |
| `2..13` (full union via default script path) | **not run** |

## Comparison to `n=13`, `{7,8}` (resolved PASS)

Canonical **`n=13`** row: `7,5,4,3,3,3,4,3,4,3,2` for `r=2..12`.

The **completed tail** `r∈{6,7,8,10,11,12,13}` on **`n=14`** does **not** match that suffix pattern from **`n=13`** (different lengths and indexing). A full apples-to-apples comparison requires finishing **`r=2..5`** and **`r=9`**.

## Why INCONCLUSIVE (not FAIL)

- No counterexample to the **parity / baseline** story: **full `n`-XOR** still gives **`min_d=1`**.
- No proof that the interior row **cannot** be completed; runs hit **time / exploration** limits on the largest DP subproblems (low `r`, unions).

## Next steps

1. **Dedicated host** with **large RAM** and **multi-hour** wall-clock for **`r=5,9`** **`d=3`** and **union** probes (**`--lru-maxsize 0`**). **`r∈{2,3,4}`** **`d=2`** is **decided**; interior **`min_d`** values for **`r=2..4`** still need **`d≥3`** completion runs if the full row is desired. **`r=9` `d=3`** exceeded **90 min** on a prior host even when **skipping** **`d=1,2`** (**`--d-min 3`**).
2. Optional: **disk-backed** or **distributed** memo (prior **`disk-memo-microbench`** was negative for this DP shape — sharding preferred).
3. If **`n=14`** row stabilizes, compare to **`n=13`** and **`n=12 {6,7}`** for scaling trends.
