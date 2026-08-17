# Independent cold audit: full-exterior contraction terminal

**Verdict:** **GREEN** at the authoritative frozen source revision

```text
a88e8a0610696f3fda5b0222884ac45878fe250273c37828349743d1b3e4ac00
  active/hc7_k7minus_full_exterior_contraction_terminal.md
```

This is an independent internal mathematical audit, not external peer
review.  The audit uses the current tightened `|C|=2` and first-transition
wording in the displayed revision, not the earlier draft hash.

The current theorem SHA-256 is
`fd6d5f640cea29c90754cf2b2e67d0f11fb8276b13225aff9e6b982f182fb1e2`.
The only later edits record the completed adjacent audits in its status and
dependency paragraphs; no hypothesis, conclusion, proof step, identity, or
scope claim changed.

## 1. Imported adjacent-pair terminal

The only non-elementary input was checked at the frozen revisions

```text
8f83354b67632d21e558f7ab86ee16958cfe25f6a478b8f81a83555fbe7cce31
  active/hc7_k7minus_adjacent_exterior_pair_elimination.md
3cc0380f6b7567252c51129e9ffda4b4145b7e9285beaca6abefe13f2016bec4
  active/hc7_k7minus_adjacent_exterior_pair_elimination_cold_audit.md
2fa83c339c36504d8fae1fed1aab99fdcfa6397bae36b1c5e1e99246ba2bf55c
  active/experiments/sixconnected_codegree2_two_vertex_verify.py
```

The current adjacent-pair audit SHA-256 is
`fd156b2409eff3e8c9fb2e10c78b1a7b5277837a39c41542333bc7dafaf1b8cb`;
the later audit edit only records the source's GREEN status and current
metadata-only hash.

Its Corollary 2 says precisely that the connected full exterior cannot be
partitioned into two nonempty connected parts joined by an edge when the
resulting quotient remains six-connected.  The local `K_6^-` exclusion
needed there follows from the target exclusion and singleton centre, so no
extra hypothesis is missing in the present application.

## 2. Connectivity under one contraction

The elementary inequality used throughout is exact:

```text
kappa(F/xy)>=k-1
```

when `F` is `k`-connected and the quotient has at least `k` vertices.  A
cut of order at most `k-2` avoiding the contracted vertex lifts unchanged;
a cut containing it lifts after replacing that vertex by `x,y`, increasing
the order by one to at most `k-1`.  In both cases it would contradict
`k`-connectivity of `F`.  All quotients in the proof have at least the
required order because the fixed centre and eight-vertex neighbourhood
already contribute nine vertices.

## 3. Maximal exterior contraction and its order

If `|C|=2`, connectedness makes its two singleton parts an adjacent
two-block partition whose quotient is the original seven-connected graph,
contrary to the imported corollary.  Hence the proof starts with
`|C|>=3`.  Contracting any first exterior edge gives a six-connected graph
by the preceding inequality.  If that contraction produced exactly two
exterior images, its two connected branch sets would form the same
forbidden partition; the tightened source now states this transition
explicitly.

At every later stage, exterior images are the connected bags of a
partition of the original `C`.  Their quotient remains connected, retains
an edge between any two bags merged next, remains anticomplete to `v`, and
is full to `J`.  A first six-connected stage with two bags would therefore
again violate the adjacent-pair corollary.  A one-bag stage cannot be
reached, because its immediately preceding six-connected stage would have
two bags.  Thus every maximal continuation terminates with `|R|>=3`.
Finiteness makes termination immediate, and the reasoning does not depend
on either the first edge or subsequent choices.

The terminal graph `H` is at least six-connected and target-free by minor
transitivity.  If it were at least seven-connected, contracting any edge
of the connected graph `H[R]` would again leave a six-connected graph,
contradicting maximality.  Hence `kappa(H)=6` exactly.

## 4. Every remaining edge yields a full six-cut

For `ab in E(H[R])`, maximality says `H/ab` is not six-connected, while
the contraction inequality gives five-connectivity.  Therefore
`kappa(H/ab)=5`.  Let `X` be a minimum five-cut and `z` the contracted
vertex.  If `z` were not in `X`, contracting `ab` in the connected graph
`H-X` would leave `(H/ab)-X` connected.  Thus `z in X`, and

```text
S_ab=(X-{z}) union {a,b}
```

has order six with `H-S_ab=(H/ab)-X` disconnected.

For a component `D` of `H-S_ab`, all its neighbours lie in `S_ab`.
Another component exists, so `N_H(D)` is a genuine vertex cut separating
`D` from a surviving vertex.  Six-connectivity gives
`|N_H(D)|>=6`, while containment in the six-set gives the reverse
inequality.  Hence `N_H(D)=S_ab`, including adjacency to both `a` and
`b`.  No unstated nontriviality or side-size assumption enters this step.

## 5. Density and excess identities

Contracting an edge with `t_i` common neighbours deletes the edge itself,
identifies exactly `t_i` duplicate edge pairs, and removes one vertex.
Consequently

```text
(|E|-4|V|)_{i+1}-(|E|-4|V|)_i=3-t_i,
```

which sums to equation (1).  Since `v` is anticomplete to every exterior
image, every common neighbour of a contracted exterior edge lies in
`R_i union J`; applying the same edge count to
`E(H_i[R_i]) union E_{H_i}(R_i,J)` proves equation (2).

The exact decomposition

```text
V(H_i)={v} dot_union V(J) dot_union R_i,
E(H_i)=E(J) dot_union E(v,J) dot_union E(H_i[R_i])
       dot_union E_{H_i}(R_i,J)
```

uses `|J|=|E(v,J)|=8` and gives

```text
|E(H_i)|-4|V(H_i)|=rho_i+|E(J)|-28,
```

so equation (3) is exact.  Finally, partitioning vertices into the
six-set `S_ab` and the components of its deletion, with no edges between
distinct components, gives

```text
|E(H)|-4|V(H)|=|E(H[S_ab])|+sum_j eta(D_j)-24,
```

which is equation (4).

## 6. Scope verdict

No contraction-order, transition, connectivity, separator-lift,
fullness, common-neighbour, or density-accounting defect was found.  The
separator is correctly asserted only in the terminal quotient: lifting a
contracted separator vertex can enlarge it in the original graph.  The
source also correctly leaves coefficient-four density uncontrolled through
the cumulative term `sum_i(t_i-3)` and does not claim that the terminal
normal form itself is impossible.
