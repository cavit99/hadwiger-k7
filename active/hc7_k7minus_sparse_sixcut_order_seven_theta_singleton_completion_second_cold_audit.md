# Second cold audit: order-seven theta singleton completion

**Verdict:** **GREEN** at the pinned revisions below.  This is a second
independent internal audit, not external peer review.

## Pinned artefacts

```text
093c25e97ff5e5d627d12915c551418cd0039f5fb1f745dc03bdeb64148d7d75
  active/hc7_k7minus_sparse_sixcut_order_seven_theta_singleton_completion.md
f24ef3026763a595f4fc3cd9f61fc482b05d9ed281e99fe48f02b987746f51ff
  active/experiments/sparse_sixcut_order_seven_theta_singleton/verify.py
```

The mathematical reconstruction was completed against theorem revision
`49e19c837650be8b1025a4d500ea64f5cc71b075658f7ab2d35d7947e1c2de48`
before consulting the adjacent first audit.  The theorem was then changed
only to record the completed cold-audit status; the mathematical statement,
proof, table, and verifier are unchanged at the current pinned revision.

## 1. Incidence reduction

After making the perfect boundary matching diagonal, an off-diagonal edge
`s_iw_j` is aligned precisely when `w_iw_j` is one of the seven theta
edges.  There are six diagonal incidences and at most two aligned
off-diagonal incidences per theta edge.  Thus aligned incidences account for
at most

```text
6+2*7=20
```

of the edges between `S` and `W`.  The threshold `21` therefore forces a
directed incidence `i -> j` on a nonedge `w_iw_j`.  Extra incidences can only
add bag contacts, so it is enough to treat the minimal graph containing the
diagonal matching and one such directed incidence.

The returned-cut arithmetic was also checked.  In the order-seven `i=1`
case, `C={u} union W`, the vertex `u` contributes six edges to `W`, and a
theta contributes seven.  If `b=e(C,S)`, then

```text
eta_S(C)=13+b-4*7=b-15.
```

Consequently `eta_S(C)>=6` is exactly the theorem's hypothesis `b>=21`.

## 2. Orbit and bag checks

The full automorphism groups of the three displayed theta graphs have
orders `4`, `2`, and `4`.  Their directed-nonedge orbits have sizes

```text
223: 2,2,2,4,2,4
124: 2,2,2,1,2,2,2,2,1
133: 4,4,4,4.
```

These are pairwise disjoint within each graph and total sixteen, the number
of directed nonedges of a seven-edge graph on six vertices.  Hence the
nineteen rows are exhaustive.  Simultaneously applying an automorphism to
the roots and their matched shore vertices preserves the diagonal matching
and every branch-set assertion.

I rebuilt every representative from the minimal edge set.  In `P(o;b)`, the
bag containing `u` is connected through `u` and contacts all four other bags.
In `F(o;a;b)`, every displayed folded bag is connected, and the bag containing
`u` again contacts all four others.  The possible missing contacts obtained,
in table order, were

```text
223: 23, [21]-4, 01, 14, [20]-5, 14
124: 35, 25, 13, 14, 23, 13, [10]-4, 35, 14
133: 12, 03, 25, 24.
```

Thus every row has five disjoint connected bags containing five distinct
roots and at least nine of the ten required contacts.  The bracketed entries
correctly refer to the folded bag, not to a sixth branch set.

## 3. Independent falsification and verifier review

As an adversarial check independent of the certificate table, I enumerated
all connected branch bags containing one prescribed root, allowed arbitrary
disjoint allocations or non-use of the seven vertices `W union {u}`, and
searched over every choice of omitted root.  This unrestricted search was
run on each minimal graph consisting of a theta, the diagonal matching, the
six `uW` edges, and one directed-nonedge incidence.  It found a punctured
rooted `K_5^-` model in all

```text
3*16=48
```

cases; no counterexample survived.  Together with monotonicity under adding
edges, this independently covers every boundary-incidence system satisfying
the theorem.

The supplied verifier was then inspected line by line.  Its minimal-graph
adjacency relation, `P` and `F` bag construction, connectivity search, root
placement, disjointness test, contact test, automorphism-orbit comparison,
and simultaneous relabelling all match the written argument.  Running it
without optimisation reproduced

```text
checked_models=34560
order-seven theta singleton completion: PASS
```

where `34560=3*6!*16`.  The checks are implemented with Python assertions,
so the recorded command should not be run with `python -O`.

## 4. Lift to the host graph and scope

Let the five rooted bags lie in the closed `C`-shore and omit `s_o`.  For
two other full components `A,D` of `G-S`, add

```text
A union {s_o},  D.
```

These bags are connected and disjoint from the five shore bags.  Fullness
makes both adjacent to every rooted bag, while a neighbour of `s_o` in `D`
makes them adjacent to each other.  The only possible missing contact is
therefore the one already allowed in the rooted `K_5^-` model, giving a
`K_7^-` minor.

No counting, orbit-coverage, branch-set, confinement, or lifting gap was
found.  The consequence is conditional on the exact order-seven `i=1`
theta return and two other full components.  It closes those three finite
theta rows; it does not prove the packet-weighted excess theorem, eliminate
the whole sparse three-component case, or meet the Norin--Totschnig
significance benchmark by itself.
