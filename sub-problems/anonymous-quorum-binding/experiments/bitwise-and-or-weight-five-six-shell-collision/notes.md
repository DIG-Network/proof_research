# Notes

- **h_and** **on** **the** **6-shell** **collapses** **to** **a** **single** **value** **(** **0** **)** **here** **—** **six** **distinct** **weights** **from** **{1,…,10}** **always** **include** **a** **pattern** **that** **drives** **AND** **to** **0** **(** **e.g.** **presence** **of** **both** **even** **and** **odd** **with** **incompatible** **low** **bits** **after** **full** **meet** **).** **So** **cross-shell** **collision** **is** **extreme** **(** **entire** **6-shell** **maps** **to** **one** **fingerprint** **).**
- **h_or** **is** **less** **degenerate** **but** **still** **has** **three** **shared** **values** **with** **the** **5-shell.**
- **Next** **encoding** **tries** **if** **needed:** **bitwise** **XOR** **of** **all** **w_i** **(** **related** **to** **061** **on** **indices** **not** **weights** **)** **or** **mixed** **(h_and,** **h_or)** **joint** **—** **likely** **still** **collides** **given** **061/062.**
