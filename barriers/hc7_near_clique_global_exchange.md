# Near-clique transfers and the remaining global allocation

**Status:** written proof; separate internal audit at the source hash
recorded in the adjacent audit. The
transfer below is a minor construction. The examples refute weakened
centroid hypotheses, not the seven-connected augmentation target. Nothing
here proves Conjecture 19, Conjecture 21, or `HC_7`.

Write `K_7^vee` for `K_7` minus two incident edges and `K_7^=` for
`K_7` minus two independent edges. All graphs are finite and simple.

## 1. Exact one-donor transfer

**Proposition.** Suppose `(D,T,U_1,U_2,U_3,B,C)` is a `K_7^vee` model:
the six bags other than `D` are pairwise adjacent, and `D` contacts
`T,U_1,U_2,U_3`. Assume `G` has no `K_7^=` minor. Partition `T` into
nonempty connected sets `X,Y` with an edge between them. Suppose there is
a `D`--`X` path whose internal vertices lie outside all seven model bags.
Put

```text
D' = D union X union {internal vertices of that path},
g  = number of bags among B,C adjacent to D',
L  = {V in {U_1,U_2,U_3,B,C} : Y is not adjacent to V},
l  = |L|.
```

If `l<=g`, then exactly one of the following nonterminal cases holds:

* `g=l=0`: `(D',Y,U_1,U_2,U_3,B,C)` is another `K_7^vee` model,
  with the same deficient bag label.
* `g=l=2`: the same seven sets form a `K_7^vee` model whose deficient
  bag is `Y` and whose two missing neighbours are the bags in `L`.

Every other case with `l<=g` gives a `K_7^=` minor.

**Proof.** A contact from `D` to `B` or `C` would already give `K_7^-`,
which contains `K_7^=` by deleting a suitable further edge. Thus both
contacts are absent. The seven new sets are connected and disjoint.
The `X`--`Y` edge supplies `D'`--`Y`; the old three `D`--`U_i`
contacts survive. All other core bags are unchanged. The missing contacts
are exactly the `2-g` remaining `D'`--`B,C` contacts and the `l`
contacts from `Y` to `L`.

There are therefore `2-g+l` missing contacts. If `g>l`, there is at most
one, giving `K_7^-` or `K_7`. If `g=l=1`, let `H` be the one bag among
`B,C` not adjacent to `D'`, and write `L={V}`. We cannot have `V=H`:
the original `T`--`H` contact, absent from `Y`, would have its end in
`X`, giving `D'`--`H`. Hence the two missing edges `D'H` and `YV`
are independent, giving `K_7^=`. The cases `(0,0)` and `(2,2)` have
precisely the incident missing edges stated above. QED

This is an explicit unrooted minor construction. Original bags other than
`T` retain all their vertices; the donor's prescribed root, if any, is
not asserted to remain in `Y`. A deficient-bag rotation may change the
two missing labels. Neither nonterminal case supplies a decreasing
well-founded parameter, and the proposition asserts nothing when `l>g`.

## 2. The centroid weakening is false

A **contact centroid** of a core-bag tree is a vertex such that every
component after deleting it contains at most two of that bag's five
selected inter-core contact ends, counted with multiplicity.

**Counterexample.** A `K_6` model with contact centroids `Z` need not
yield `K_7^=` even when `G-Z` is connected, every centroid has two
distinct neighbours outside `Z`, and restoring any single centroid gives
a two-connected graph.

Let `G=K_4 join (2K_2)`, with core `u_1,u_2,u_3,u_4` and pairs
`ab,cd`. Use the six bags

```text
{u_1,c}, {u_2,d}, {u_3}, {u_4}, {a}, {b}.
```

For the first two bags select the mutual contact `cd`, their contacts to
`u_3,u_4` at `c,d`, and their contacts to `a,b` at `u_1,u_2`.
Use the six edges among `u_3,u_4,a,b` for the remaining contacts. Thus
`c,d` each carry three selected ends, and `u_1,u_2` each carry two.
The contact centroids are `Z={c,d,u_3,u_4,a,b}`. Their complement is
the edge `u_1u_2`, and every centroid is adjacent to both ends.

The graph has no `K_7^=` minor. It is the union of the two cliques
`{u_1,u_2,u_3,u_4,a,b}` and `{u_1,u_2,u_3,u_4,c,d}`, intersecting
in a four-clique. A five-connected minor cannot straddle this clique
separation: at most four branch sets meet the separator; deleting their
labels would separate any labels wholly on opposite sides. All remaining
labels therefore lie on one side, and the separator clique reconnects
the truncated crossing bags there and replaces any contacts on the other
side. The minor would occur in a six-vertex clique, which is impossible.
Here `K_7^=` is five-connected: deleting at most four vertices leaves a
connected complete graph minus a matching, whereas its minimum degree is
five. This also proves the claimed minor exclusion without enumeration.

The displayed `K_6` model spans `G`, so it has no disjoint deficient bag.
The weaker connected-complement/two-neighbour assertion fails even with
such a bag: add a vertex `v` adjacent exactly to `u_1,a,b`, use core bags
`{u_1,c},{u_2},{u_3},{u_4},{a},{b}` and deficient bag `{d}`.
Choose centroid `c` in the first bag using its three `u_2,u_3,u_4`
contacts. The complement of the six centroids is the connected graph on
`u_1,d,v`; every centroid has two outside neighbours. This graph is still
`K_7^=`-free, since the added four-clique meets the previous graph in
the triangle `u_1ab`, and the same clique-separation argument applies.

## 3. Exact global obligation

Seven-connectivity retains more than these weakened conditions: for every
`I subseteq Z`, the graph `G-(Z-I)` is `(|I|+1)`-connected. The first
example fails when two outside vertices and four centroids are deleted,
leaving the nonadjacent pair `a,c`. A global allocation or reduction must
use the corresponding mixed-deletion constraints, or prove a sufficient
replacement. The transfer proposition supplies no such recurrence.
