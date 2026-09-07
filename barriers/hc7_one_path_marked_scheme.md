# One additional marked-scheme connection is insufficient

**Status:** explicit counterexample; the adjacent audit records its separate internal verdict.
This refutes a weakening of the
[marked-scheme theorem](../results/hc7_marked_k33_scheme_completion.md),
not its proved two-connection conclusion or a critical-host assertion.
Write `Q=K_7^=` for `K_7` with two independent edges deleted.

**Construction.** Let `G` have the nine distinct vertices
`v,a0,a1,a2,0,1,2,3,4`. Its edges are exactly:

- the triangle on `a0,a1,a2` and the cycle `0,1,2,3,4,0`;
- all eight edges from `v` to the other vertices;
- all six edges from `{a1,a2}` to `{1,3,4}`; and
- the single additional edge `a0-1`.

Colour `a0,0,2` alike in `G-v`, and give each of `a1,a2,1,3,4`
its own different colour. This is proper. The seven displayed cross-edges
are a literal endpoint-coloured scheme for
`K_{3,3}-{a0-3,a0-4}`, rooted at `{a0,a1,a2}` and `{1,3,4}`.
Both markers are outside its path union. Thus the prescribed cycle,
triangle, apex and the one additional `a0-1` path are all present.

**Claim.** Nevertheless `G` has no `Q` minor.

**Proof.** The set `S={0,2,a0}` is independent, with degrees `3,3,4`.
Suppose seven disjoint connected bags form a `Q` model. If `u` vertices
are unused, the nine-vertex order gives

`u + sum_(i=1)^7 (|B_i|-1) = 2`.

No vertex of `S` can be a singleton bag, because every vertex of `Q`
has degree at least five. A bag containing `k>=1` vertices of `S`
must therefore contain a vertex outside `S`, by connectedness and
independence. It contributes at least `k` to `|B_i|-1`. Each unused
vertex of `S` contributes one to `u`. The three vertices of `S` thus
force the left side to be at least three, a contradiction. QED

**Scope and repair.** The graph is five-colourable: deleting `S` leaves
`K_3 join (K_2 union K_1)`, and its five-colouring extends over the
independent degree-at-most-four vertices of `S`. Its minimum degree is
three. It does not meet the critical host's connectivity, degree or
chromatic hypotheses. The proved theorem repairs this unrestricted
one-path assertion by adding `a0-3` or `a0-4`; a one-path argument in
the actual critical host would need substantive use of that extra data.
