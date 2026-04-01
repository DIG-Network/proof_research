# Notes

- Ran with **`timeout 14400`** at shell; observed **exit 247** ~**5085 s** — **SIGKILL** class, **not** **124**.
- **Unbounded** memo **still** **OOM-killed** **before** **75M** **cap** **on** **this** **host** **(** **slower** **than** **12M** **LRU** **~8** **min** **)**.
