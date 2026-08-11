# Internal audit: terminal split criterion for the concentrated `b=2` model

**Verdict:** **GREEN** for Theorem 2.1, Corollary 2.2, Proposition 3.1,
and the stated nonclosure.  This is a separate internal mathematical
audit, not external peer review.

## 1. Exact revision checked

The audited source
`hc7_k7minus_five_centre_b2_model_bag_split.md` has SHA-256

```text
2db555a93d3050a6f56317d9ce21cfc9205de5e8a207b5d5cb8f0d131fc85602
```

Its direct stable-bag concentration input was checked at source SHA-256

```text
a36c4ce68dfe6a08c21ba759eb363a2ac8bfccc59c1105ee953ac159aca1d910
```

with the adjacent GREEN audit at SHA-256

```text
5231731a24f64bc3e5bc4b6a29b17cb3e78178931cb2615723a79421c5320c9e
```

## 2. Splitting one model bag

Contract the two disjoint connected four-adjacent subgraphs `R_0,R_1`
inside the connected bag `U`, choose a spanning tree, and delete an edge
on the tree path between the two contracted vertices.  The resulting two
tree components expand to a partition `U=U_0 dotcup U_1` in which both
induced sides are connected, contain their prescribed `R_i`, and are
adjacent across the deleted tree edge.

Each `U_i` is adjacent to all four unchanged model bags because it contains
`R_i`.  Together with those four bags, `U_0,U_1` are six pairwise adjacent
connected sets.  The disjoint connected set `X` is adjacent to all four
unchanged bags and, because it had an edge to `U=U_0 union U_1`, to at
least one split side.  Adding `X` therefore gives seven branch sets with
at most the one missing adjacency from `X` to the other split side.  This
is an explicit `K_7^-` model.

## 3. Boundary and contact consequences

The contrapositive gives packing number one for four-adjacent connected
subgraphs in every model bag.  For either centre-clean bag, the spanning
model places all six or more neighbours from the stable-bag boundary bound
inside the other four bags, and model adjacency makes all four neighbour
classes nonempty.  This verifies Corollary 2.2 without strengthening the
boundary count into an unsupported split.

The six retained-centre-private contacts are distinct vertices in
`P union Q union B_1` and each is adjacent to its owner in `K`.  The pole
vertices `p in P` and `q in Q` are two further, distinct contacts with the
pole-incident centres in `K`; they lie outside `D`, so they are distinct
from the six private contacts.  Thus there are eight `K`-neighbours in the
three bags, and one bag contains at least three.

## 4. Scope

Neither six boundary vertices nor three `K`-contacts alone force the
two-subgraph split.  The source records this as the first open inference
and claims no rerouting theorem or closure of the `b=2` branch.  No
unresolved assumption or gap remains in the proved statements.
