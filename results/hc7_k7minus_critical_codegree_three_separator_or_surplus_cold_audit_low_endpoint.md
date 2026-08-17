# Independent cold audit: critical codegree-three separator or surplus

**Audited source:**
[`hc7_k7minus_critical_codegree_three_separator_or_surplus.md`](hc7_k7minus_critical_codegree_three_separator_or_surplus.md)

**Source SHA-256:**
`fb2083fff6087ea3b192a63800b1aa0e1f7f496d47524e452964f616a12b79e0`

**Verdict:** **GREEN for the two stated theorems.**  This is an independent
cold proof audit, not external peer review.  The argument is
computation-free.  I found no hidden endpoint-degree assumption.  I did
independently check the strengthened pole-symmetric separator conclusion:
the same absent model contact yields actual separators whose boundaries
contain either prescribed pole.  Thus the specified endpoint `v` can always
be retained; in Theorem 2 this endpoint has degree eight.

## 1. Chromatic entrance and the `K_6` model

For `H=G-{v,x}`, deleting two vertices from a seven-chromatic graph gives
`chi(H)>=5`, while proper-minor six-colourability gives `chi(H)<=6`.
Suppose a five-colouring exists.  If one colour has no common neighbour of
`v,x`, move every `v`-neighbour of that colour to a new sixth colour, give
`v` the vacated colour and give `x` the new colour.  The moved vertices form
an independent set and none is adjacent to `x`; every old-colour neighbour
of `v` was moved.  The resulting colouring is proper on every edge of `G`.
Hence each of the five colours would require a distinct common neighbour,
contrary to codegree at most four.  Therefore `chi(H)=6`.

The deletion of two vertices from a seven-connected graph is
five-connected.  The proved `t=6` case of Hadwiger's conjecture consequently
supplies a `K_6` minor in `H`, without any density or endpoint-degree input.
To make it spanning, take a component of the vertices outside the six bags.
Connectedness of `H` gives an edge from that component to an existing bag;
absorbing the whole component into that bag preserves connectedness and all
six clique adjacencies.  Iteration exhausts `V(H)`.  This checks both the
Hadwiger substitution for the former Norin--Totschnig density step and the
spanning-model quantifier.

The palette source at SHA-256

```text
2b0c30b9d8566f6da4959df145bf0f527249bf887dfa844d19a98e524080a9f2
```

assumes seven-connectivity, seven-chromaticity, proper-minor
six-colourability and `chi(G-{v,x})=6`; it has no endpoint-degree
hypothesis.  Its use in item 3 is therefore exact.

## 2. Every spanning model has a genuinely mixed branch set

Fix an arbitrary spanning `K_6` model.  If the connected set `{v,x}` met
five of its six bags, it and the six clique bags would be seven connected
branch sets with at most one missing adjacency.  Target exclusion therefore
gives

```text
|C_v union C_x|<=4.
```

Let `W=N(v) cap N(x)`, where `3<=|W|<=4`.  If two vertices of `W` lie in one
bag, they themselves are distinct `v`- and `x`-neighbours in that bag.
Otherwise the vertices of `W` lie in distinct common-contact bags.  Under
the contrary assumption that no common bag contains distinct pole
neighbours, the two nonempty pole-neighbour sets in each common bag must be
the same singleton.  Those singletons are exactly the members of `W`.

At most four of the five saturated non-pole colours occur on `W`.  Choose
an absent colour.  Its selected neighbour at each pole cannot be a common
vertex, cannot lie in an old common bag, and the two selected neighbours
cannot lie together in a new bag; each possibility would put distinct pole
neighbours in one common-contact bag.  They therefore occupy two distinct
exclusive bags.  The contact union has order at least `|W|+2>=5`, contrary
to the preceding bound.  This verifies the codegree-three and codegree-four
cases, uniformly for every spanning model.

## 3. Split, missing contacts and separator

Deleting an edge of the `a-b` path in a spanning tree of the mixed bag gives
two nonempty connected adjacent pieces with the nominated pole-neighbours
on their prescribed sides.  After adjoining `v` and `x`, the two split bags
are adjacent through `vx`; the five foreign model bags remain pairwise
adjacent.  Only the ten split-bag--foreign-bag pairs can be absent.  At most
one absence would be a `K_7^-` model, so at least two are absent.

For an absent pair on the `p` side, the piece `X_p` and its pole-adjoined
version `{p} union X_p` are both connected and anticomplete to the relevant
foreign bag.  Thus both displayed open neighbourhoods in Theorem 1 are
actual separators.  The first contains `p` because `X_p` contains the
nominated `p`-neighbour; the second contains the other pole through the
edge `vx`.  Whichever side has the absent contact, one of the two boundaries
therefore contains the specified endpoint `v`; in the critical-host
application this is the degree-eight endpoint.

Seven-connectivity gives order at least seven for either boundary.  The
equality-fullness proof also applies separately to either one.  Its defining
connected set is a component after deleting its full open neighbourhood,
and the anticomplete foreign bag lies in another component.  If any
component missed one of the seven boundary vertices, its own neighbourhood
would have order at most six and would separate it from another surviving
component.

These checks use literal host adjacencies.  No quotient contact is silently
treated as an edge, and no claim that the separator has order at most seven
is made.

## 4. The codegree-at-most-two surplus branch

The frozen critical-host inputs give a degree-eight vertex `v`,
seven-connectivity and `|E(G)|>=4|V(G)|`.  The frozen generic low-codegree
theorem supplies an incident edge `vx` with codegree at most three.

For codegree `c<=2`, contraction deletes one vertex and exactly `1+c`
edges.  Thus, for `Q=G/vx`,

```text
|E(Q)|=|E(G)|-1-c
      >=4|V(G)|-3
       =4|V(Q)|+1.
```

Edge contraction lowers connectivity by at most one, so `Q` is
six-connected; it is target-free as a minor of `G`.  It is six-colourable
by proper-minor minimality.  A five-colouring would expand the contraction
vertex to two equal-coloured ends and then give the degree-eight end `v` a
new sixth colour, producing a six-colouring of `G`.  Hence `chi(Q)=6`.

In any six-colouring of `Q`, the contraction vertex is adjacent to all
seven vertices of `T=N_G(v)-{x}`.  Its colour is absent from `T`.  If any
of the other five colours were absent, assigning that colour to `v` after
splitting the contraction vertex would properly colour the restored edge
and every other edge at `v`.  All five colours therefore occur on `T`.
This verifies the `+1` density and palette claims exactly.

## 5. Pole-symmetric separator check

Retain an absent contact on the `p` side and let `q` be the other pole.  The
source considers both

```text
N_G({p} union X_p).
```

The set `{p} union X_p` is connected and remains anticomplete to the same
foreign bag, so its neighbourhood is an actual separator.  The edge `pq`
puts `q` in that boundary, while the nominated pole-neighbour puts `p` in
`N_G(X_p)`.  Consequently every single absent contact gives two actual
separators: one whose boundary contains `p`, and one whose boundary contains
`q`.  This proves the source's strengthened conclusion and, in Theorem 2,
the guaranteed inclusion of the degree-eight endpoint.

This observation does **not** bound either separator above by seven, so it
does not terminalise Theorem 2.

## 6. Frozen inputs and external trust boundary

The four repository hashes printed in the source match the local files.
The critical-host and generic low-codegree inputs have adjacent GREEN
audits.  The former bounded-endpoint split is not needed for the new proof,
but its displayed hash also matches.

The sole new external input is the proved `t=6` case of Hadwiger's
conjecture, N. Robertson, P. Seymour and R. Thomas, *Hadwiger's conjecture
for `K_6`-free graphs*, Combinatorica **13** (1993), 279--361.  Its
contrapositive is precisely the use made here: every six-chromatic graph
has a `K_6` minor.

The audited result remains a reduction.  The cold audit certifies neither
the positive-surplus six-connected extremal statement nor an upper bound on
the returned separator.
