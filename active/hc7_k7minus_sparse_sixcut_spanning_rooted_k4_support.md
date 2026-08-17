# Spanning rooted-`K_4` support and the exact-six portal gate

**Status:** proved local structural lemmas.  They identify the exact
omitted-root obstruction left by a shore-confined rooted `K_4` model.  They
do not bound the excess of either of the two supporting branch bags.

Let `G` be a six-connected graph, let `S` be a six-vertex cut, and let `C`
be a component of `G-S`.  Fix

```text
Z=S-{p,q},            |Z|=4,
```

and suppose that `G[C union Z]` has a `Z`-rooted `K_4` model.  A
**portal** of a subgraph disjoint from the model is a model vertex adjacent
to that subgraph.

## Lemma 1 (spanning four-bag normalisation)

There is a `Z`-rooted `K_4` model with branch bags

```text
M_z,   z in Z,
```

such that

```text
C union Z = disjoint union_{z in Z} M_z.              (1)
```

### Proof

Start with any such model and put `M` equal to the union of its four bags.
The set `M intersect C` may initially be empty only when the required six
adjacencies are all boundary edges.  In that degenerate case choose a root
`z in Z` and a neighbour `v in C` of `z` (such a neighbour exists because
`C` is `S`-full), and absorb `v` into `M_z`.  Thus in all cases we may first
arrange that `M intersect C` is nonempty.

Every component `D` of `C-(M intersect C)` has an edge to `M intersect C`,
because `G[C]` is connected.  Assign `D` to one model bag which it meets.
The enlarged bag is connected, the four bags remain disjoint, and none of
the six model adjacencies is lost.  Assigning all such components gives
(1).  \(\square\)

## Lemma 2 (two-bag support of each omitted root)

Assume that, for every `x in S`, the closed shore

```text
G[C union (S-{x})]
```

has no `(S-{x})`-rooted `K_5^-` model.  In every spanning model from
Lemma 1, each of `p,q` is adjacent to at most two of the four model bags.

### Proof

Suppose, for example, that `p` is adjacent to three of the bags.  Retain
the four pairwise adjacent model bags and add the singleton bag `{p}`.
The singleton is adjacent to at least three of the four old bags, so among
the five bags at most one pair is nonadjacent.  They form a
`(Z union {p})`-rooted `K_5^-` model in `G[C union Z union {p}]`, contrary
to the hypothesis with the omitted root `q`.  The argument for `q` is the
same.  \(\square\)

The proof needs no disjoint fan.  A single connected set containing `p`
and meeting three old bags is already the fifth branch bag; routes inside
that set may share arbitrary vertices.

## Lemma 3 (four actual portals return an exact six-cut)

Let `(M_z:z in Z)` now be any, not necessarily spanning, rooted model, and
put `M=union_z M_z`.  In

```text
J=G[C union Z union {p}],
```

let `R` be the component of `J-M` containing `p`.  Suppose that
`R-{p}` is nonempty and that `R` has at most four portals in `M`.  Then:

1. `R` has exactly four portals, say the set `A`;
2. every component `L` of `R-{p}` is adjacent to both `p` and `q`; and
3. for every such `L`,

```text
N_G(L)=A union {p,q}.                                  (2)
```

In particular, each `L` is an exact six-fragment.  If the rooted
five-models are excluded as in Lemma 2, all four portals lie in at most two
of the rooted-`K_4` bags.

### Proof

Fix a component `L` of `R-{p}`.  No vertex of `C-(M union R)` is adjacent
to `L`, since such an edge would put that vertex in the same component of
`J-M` as `p`.  The four roots in `Z` belong to `M`, and `q` is the only
boundary vertex absent from `J`.  Hence, if `A_R` denotes the portal set of
`R`,

```text
N_G(L) subseteq A_R union {p,q}.                       (3)
```

The set `L` is a nonempty proper subset of `V(G)`, and vertices in either
of the other components of `G-S` lie outside `L union N_G(L)`.
Six-connectivity therefore gives `|N_G(L)|>=6`.  The right side of (3) has
order at most six.  Equality holds throughout.  Thus `|A_R|=4`, every
portal is adjacent to `L`, and both `p,q` are adjacent to `L`, proving
(2).  The last assertion follows from the same connected-fifth-bag
argument as Lemma 2, applied to `R`.  \(\square\)

## Consequence for the sparse three-component route

Contracting four spanning bags makes Lemma 2 look like a separator of
order two in a four-vertex quotient.  That quotient separator does **not**
lift to two vertices of `G`: either supporting bag may be arbitrarily
large.  Lemma 3 is the sharp conclusion available when normalisation does
reduce the number of actual portals to four.  Six-connectivity then makes
the return tight, of order six, rather than contradictory.

Thus the remaining density problem is precisely to control excess stored
inside two supporting bags or across a chain of the exact six-fragments in
(2).  Ordinary Menger arithmetic alone does not supply that control.
