# Notes

- **Monotonicity surprise:** Adding menus can only *decrease* minimal decision-tree depth in this DP model, so `stratum_min_d2` is monotone **nondecreasing** in the menu partial order. One might have hoped for a **long** intermediate interval of “some but not all” depth-2 witnesses. The scan shows that for `n=8` on this stratum, the first nontrivial high-arity **full** menu (any of `r=5`, `r=6`, or `r=7`) already saturates the stratum to **all** `min_d=2`.

- **Cheapest high menu (wall clock):** Full `r=7` only (`8` splits) was fastest per pass (~16.3 s); full `r=5` (`56` splits) slowest (~266.5 s). Split count correlates with wall time but **not** with `stratum_min_d2` — all six masks hit `107800`.

- **Wedge selector:** `stratum_pred=0` and `viol_d2_not_pred=107800` for every mask, consistent with quartics vs 3-set wedges — same structural obstruction as the full `r5–r7` FAIL, now seen to trigger as soon as **any** of those menus is present.

- **Next directions:** (1) **Partial** (non-full) submenu choices within a fixed arity — exponentially larger search. (2) A **different** certificate family for `n=8` not based on the n=7 wedge port. (3) Relate this “single full high-arity menu suffices for universal depth-2 on this stratum” to a formal **minimal sufficiency** statement in the planner/spec language if useful.
