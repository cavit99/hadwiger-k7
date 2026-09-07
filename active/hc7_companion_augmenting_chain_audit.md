# Internal audit: simultaneous near-clique transfers

**Verdict: GREEN.** The conditional implication, Theorems 1--2 and
Proposition 3 are valid at the source revision below. This is a separate
internal mathematical audit, not external peer review or a proof of the
global structural target, Conjecture 19 or `HC_7`.

**Audited source:** [simultaneous transfers](hc7_companion_augmenting_chain.md)

**Whole-source SHA-256:**
`fc9a69159af8e9c1f53961614fc2a049da5ad2be52bf4daee3e0f2dc5ce6e944`.

The complete construction was first checked at
`1221ef767137d17f2e770f5c2c22d26859361c23efe26613c243c508eb90442a`.
The final revision also permits any nonempty donor subset, adds the
conditional colouring implication, and updates the status wording. Those
changes were checked in this audit. No finite enumeration supports the
verdict.

## Strongest inferences checked

1. Each donor is partitioned into connected nonempty parts. Its old
   connectivity supplies an actual edge between the parts, so the connected
   union `W` contacts every remainder. The original vertex `v` retains
   every untouched `T_j` contact. All seven proposed bags are disjoint;
   no path through an already owned vertex is used.
2. `L` is the exact noncontact graph after all donations, including
   remainder--remainder pairs. If `W` still misses a hole `H`, every
   donor--`H` contact must remain in the donor remainder: an edge from
   the donated part would make `W` contact `H`. Thus the possible single
   core loss is independent of the remaining hole. If both holes are
   gained, the asserted matching condition on `L` gives precisely the
   allowable two independent missing contacts. Extra edges can be deleted.
3. In Theorem 2, restoring the other donors whole can only restore core
   contacts. Every loss in the single-donor move is incident with its
   remainder and belongs to `L`, whose degree there is at most one.
   Direct adjacency to `v` makes the single donated bag connected. The
   same remaining-hole argument proves independence of the two possible
   losses. The proof does not require two or more donors.
4. In Proposition 3 the initial six core bags have every required contact;
   `x_1u_3` supplies the contact absent from `y_1u_3`. The only legal
   single donations are `x_1` and `y_2`. The first loses `y_1u_3` and
   gains no hole; the second loses the three contacts from `x_2` to
   `u_3,u_4,c` and gains both holes. Each quotient has three missing
   contacts. The opposite halves cannot join `v` through unowned vertices,
   since the model spans the graph. Joint donation gives the connected
   bag `v,x_1,x_2`; its missing contact with `c` is independent of the
   sole core loss `y_1u_3`. This refutes only the restriction to the
   specified one-donor constructions, not arbitrary models of this host.

## Conditional implication and scope

Minor-minimal non-six-colourability gives all proper minors six-colourable
and chromatic number exactly seven by vertex deletion and restoration.
The complete graph `K_7` is excluded by the forbidden companion minor.
The noncomplete contraction-critical connectivity input and NT Theorem 4
therefore give the hypotheses of the proposed structural theorem in this
same host. Its conclusion would contradict companion-minor exclusion.
No density theorem, quotient criticality, or branch-set lifting is used.

This citation assessment uses the previously checked statements in the
[critical reduction](hc7_k7minus_critical_to_sixconnected_4n_reduction.md)
(SHA-256 `ac3a9fcf81549c9bb3f7a6e789b240040b1f63bf40cae59b4ac61fbd8981d0a2`)
and [frontier audit](hc7_k44_critical_global_construction_audit.md).
The primary literature was not freshly inspected during this audit.

No gap was found in the stated constructions. Existence of a terminal
allocation in every seven-connected host remains unproved. Donor roots
may move, seven-connectivity is not used in the local constructions, and
no decreasing parameter or induction through temporary losses is supplied.
