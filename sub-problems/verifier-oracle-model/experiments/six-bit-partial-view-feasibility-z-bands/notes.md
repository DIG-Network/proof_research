# Notes

- **Closed form:** For **|Q| = k**, **R = n − k**, targets **t−1** **and** **t**: **wt=t−1** **iff** **t−1−z ∈ [0,R]** **iff** **z ∈ [t−1−R, t−1]** **∩** **[0,k]**; **wt=t** **iff** **z ∈ [t−R, t]** **∩** **[0,k].** **Intersection** **gives** **“both”;** **symmetric** **differences** **give** **exclusive** **cells.**

- **Series** **(n=10,** **t=6):** **k=4** **⇒** **R=6** **⇒** **always** **both** **(037).** **k=5** **⇒** **R=5** **⇒** **only** **z=0** **breaks** **wt=6** **(038).** **k=6** **⇒** **R=4** **⇒** **two** **singleton** **endpoints** **z=0** **(neither)** **and** **z=6** **(only** **wt=6)** **plus** **z=1** **(only** **wt=5).**

- **Verifier** **story:** **Six** **probes** **with** **all** **zeros** **imply** **wt** **≤** **4** **—** **below** **both** **5** **and** **6** **(vacuous** **for** **5** **vs** **6** **game** **unless** **we** **also** **care** **about** **wt** **≤** **4).** **All** **ones** **on** **six** **fixed** **coordinates** **forces** **quorum** **if** **the** **true** **vector** **matches** **that** **prefix** **—** **but** **adaptive** **paths** **rarely** **hit** **these** **extremes** **uniformly.**

- **Next:** **k=7** **(R=3)** **band** **enumeration** **(entry** **040).**
