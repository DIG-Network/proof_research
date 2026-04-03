# Notes

- **observation:** Last progress line at **38×10⁶** **`exists_calls`**; process died with **exit 247** before **40×10⁶** — matches **OOM/SIGKILL** pattern from **`session-state`** for the **10⁸** dict run.
- **insight:** **`VmRSS_kB`** tracks **`memo_dict_size`** ~1:1 in kB order of magnitude (~1 kB per dict entry is plausible with Python object overhead + big integers).
- **dead_end (host-local):** Pushing **`--memo-dict`** invocation budget into **5×10⁷** range on **~15 GB** class machines hits OOM before **`max_exists_calls`** trips — not a mathematical verdict on **`d=3`** feasibility.
- **question:** Does linear extrapolation (**~20 GB** at **5×10⁷** calls if trend holds) match a larger host, or does growth sublinearize after saturation?
- **next:** Prefer **XOR sharding** / **smaller dict budgets** / **LRU lines** per **`session-state`**; keep **`--progress-every`** for any long **`--memo-dict`** job to distinguish stall vs OOM vs **PARTIAL**.
