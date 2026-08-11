# Internal audit of the simultaneous five-triangle barrier

**Status:** separate hash-pinned internal audit.

**Verdict:** **GREEN.**  The displayed ten-vertex graph is seven-connected,
has the stated proper colouring, rainbow triangles, six common bichromatic
components, and five individual rooted `K_5` models, but has neither a
separator of order at most six nor the asserted simultaneous rooted `K_5`
model.  The deterministic checker exhausts every possible placement of the
ten vertices in such a rooted model.  The source correctly limits the
counterexample to the static common-component implication and does not claim
to realize a five-centre contraction-critical host.

## Audited revisions

This audit checks
`hc7_all_rainbow_common_components_multiroot_barrier.md` at SHA-256

```text
7e4a425274767b6978099fdf5530e4cfe50488a2bc8589c953431dd97273938d
```

and its deterministic checker
`hc7_all_rainbow_common_components_multiroot_barrier_verify.py` at SHA-256

```text
19d9bf3150b216c83b247bb012937fe464d1aeaf067c2b7e54d85244054bab17
```

## 1. Construction and colouring

The checker constructs exactly the complete five-partite graph with parts

```text
{p,v}, {q,u}, {a0,a1}, {b0,b1}, {c0,c1}
```

and deletes only `pq`.  Its five displayed colour classes are therefore
independent and give a proper colouring.  Each nominated `T_j` contains one
vertex from each of the last three parts, so it is both a triangle and
rainbow in the three `gamma` colours.

For each `gamma_i`, the graph induced by its two vertices and either pole
colour class is complete bipartite.  Hence the component containing `p`, and
respectively the component containing `q`, contains both contacts of that
`gamma_i` colour.  The path `p-u-v-q` also verifies the stated
`beta`--`delta` pole connection.

## 2. Exact connectivity

Both nominated poles have degree seven.  Deleting all seven neighbours of
`p` leaves `p` isolated from the surviving edge `vq`, so the vertex
connectivity is at most seven.

For the lower bound, after deleting at most six vertices at least four
vertices remain.  Choose a surviving vertex `r` outside `{p,q}`.  It is
adjacent to every survivor except possibly its unique same-part mate.  If
that mate remains, any third vertex joins the pair except for the single
possible exceptional choice caused by the deleted edge `pq`.  There are at
least two choices of a third vertex, so a nonexceptional one supplies a
two-edge path.  Thus every deletion of at most six vertices leaves a
connected graph.  This proves `kappa(H)=7`, and in particular excludes every
separator of order at most six.

The checker independently enumerates every deleted set of orders zero
through six and tests connectivity, then verifies the seven-vertex upper
cut at `p`.

## 3. The five individual rooted models

For each displayed triangle, the bags

```text
{p,u}, {v,q}, and the three triangle singletons
```

are disjoint and connected.  The edge `uv` joins the two pole bags, every
triangle singleton is adjacent to both pole bags, and the triangle supplies
the remaining three contacts.  These are valid `p,q,T_j`-rooted `K_5`
models.  The checker tests every bag's connectivity and every pairwise bag
contact for all five triangles.

## 4. Exclusion of a simultaneous model

If three disjoint non-pole bags each meet one three-vertex triangle, that
triangle has exactly one vertex in each bag.  Comparing `T_1` with `T_2`,
`T_3`, and `T_5` forces, up to permuting the three bags,

```text
{a0,a1} in one bag,
{b0,b1} in a second bag,
{c0,c1} in the third bag.
```

Each forced pair is independent.  Each of the three disjoint bags therefore
needs a further vertex to connect its pair.  The rooted vertices `p,q` are
unavailable, all six `a,b,c` vertices have already been forced into their
respective bags, and only `u,v` remain.  Two vertices cannot provide three
disjoint bags with one additional connecting vertex each.  Hence no such
simultaneous rooted model exists.

The finite search is exhaustive rather than merely confirmatory.  The union
of the five triangles is all six `a,b,c` vertices, so every one of those
vertices must belong to exactly one of the three non-pole bags.  The checker
enumerates all `3^6` assignments and retains exactly those distributing each
triangle across all three bags.  It then assigns each of `u,v` independently
to one of the three non-pole bags, the `p`-bag, the `q`-bag, or no bag.
These six choices per remaining vertex cover every possible rooted minor
model because unused vertices are permitted.  It finally tests connectivity
of all five bags and all ten pairwise bag contacts.  No assignment succeeds.

## 5. Exact scope

The construction refutes only the implication stated in Section 1 of the
source: seven-connectivity plus the six common pole--contact bichromatic
components does not force the simultaneous five-triangle rooted model or a
separator of order at most six.  It deliberately supplies no abstract
degree-eight centres, private-contact allocation, opposite-shore colouring
response, proper-minor criticality, or unique-owner completion model.
Accordingly it is not a counterexample to the main conjecture or to any
later theorem using those additional hypotheses.

## Verification

The pinned checker was run as

```text
python3 barriers/hc7_all_rainbow_common_components_multiroot_barrier_verify.py
```

and returned

```text
GREEN: common components do not force a simultaneous five-triangle model
```
