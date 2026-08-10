# Internal audit: five-centre two-cut response reduction

**Verdict:** **GREEN.**

**Audited theorem:**
[`hc7_k7minus_five_centre_two_cut_reduction.md`](hc7_k7minus_five_centre_two_cut_reduction.md)

**Audited SHA-256:**
`1917b5e3d183d44a2d905d2628272d10e4bc6f7ae0768b43cab0e9462b83332a`

The only changes from the frozen revision checked line by line were moving
the theorem into `results/` and replacing its pending-audit status text by
the link to this GREEN audit.  Its statement and mathematical proof are
unchanged.

This is a separate internal mathematical audit, not external peer review.
The audit reconstructed every contraction, colouring pullback, minor-model
restriction, and edge count in the displayed revision.

## 1. Exact cut geometry

Deleting `Z` and then `{p,q}` deletes exactly the seven-set
`S=Z union {p,q}` from `G`, so the components of `F-{p,q}` are precisely
the components of `G-S`.  Each such component has full neighbourhood `S`:
otherwise its neighbourhood would be a cut of order at most six separating
it from another component, contrary to seven-connectivity.

The hypotheses of the audited critical seven-cut capacity theorem are
exactly present.  Its three-component conclusion would make every proper
three-colouring of `G[S]` have class sizes `3,2,2`.  The partition

```text
Z | {p} | {q}
```

is proper regardless of the boundary edges, because `Z` is independent and
the other two blocks are singletons.  Its class sizes are `5,1,1`, so three
components are impossible.  There are therefore exactly two.

If `pq` were an edge, the exact reflection lemma applies on each side to
that same partition.  The opposite full component carries the block `Z`,
while the adjacent singleton vertices `p,q` are the retained clique.  The
two reflected colourings have the same exact boundary partition, align by a
permutation of the six colours, and glue.  This correctly proves that `pq`
is absent.  The two-component clause of the capacity theorem says that
`G[S]` nevertheless has an edge; independence of `Z` then makes it a
centre--pole edge.

The imported capacity source and its audit have matching SHA-256

```text
d4d650fee168fc2ff0e00a3b7b0faed6ff674ba8cd3c06c263f63c4170656f34
```

for the theorem revision used here.

## 2. Response nonemptiness and orientation

For complementary components `L,R`, the set `R union Z` is connected:
`R` is connected and every centre has a neighbour in `R`.  Contracting a
spanning tree of this set is a proper minor operation.  The contraction
vertex is adjacent to both poles.  Pulling a six-colouring back only to
`G[L union S]` is proper: the five independent centres receive the
contraction colour, every centre--`L` or centre--pole edge is represented
at the contraction vertex, and both poles avoid that colour.  Thus each
response set is nonempty.

A common equal or distinct response would give the same exact boundary
partition on both closed sides.  Colour-name alignment and gluing would
six-colour `G`.  Since both response sets are nonempty subsets of a two-type
set, they are opposite singletons.

The chromatic lower bounds use genuinely disjoint palettes.  A
three-colouring of the equal-response component together with three fresh
boundary colours would realize the forbidden distinct response.  A
four-colouring of the distinct-response component together with two fresh
boundary colours would realize the forbidden equal response.  Hence the
displayed bounds `4` and `5` are valid.

In a distinct-response colouring, a Kempe swap separates the poles only if
they lie in different components of their two-colour subgraph.  Such a swap
would produce the forbidden equal response.  Therefore the asserted
bichromatic pole path exists, and its internal vertices lie in the open
component because the other boundary vertices have the centre colour.

## 3. Equality-side critical-edge packet

The set `D union Z` is connected for the same fullness reason as above.
After contracting it to `x`, the minor has vertex set `C union {p,q,x}`
and `x` is adjacent to both poles.  Every six-colouring pulls back to a
permitted colouring of the closed `C`-side, so the poles must be equal.
Consequently adding `pq` destroys six-colourability.  Conversely, a
six-colouring of the proper minor plus one new colour on one pole is a
seven-colouring after `pq` is added.  Thus `M_C+pq` is exactly
seven-chromatic, `M_C` is exactly six-chromatic, and `pq` is a critical
edge.

Let `alpha` be the common pole colour and `delta` the colour of `x`.  For
every other palette colour `beta`, the poles lie in one
`alpha`--`beta` component; otherwise a Kempe swap gives a six-colouring in
which the added edge is proper.  The four colours outside
`{alpha,delta}` give four paths avoiding `x`, hence with internal vertices
in `C`.  Two paths with different second colours can share only
`alpha`-coloured vertices and cannot share an edge.  The packet conclusion
has exactly the stated strength; vertex-disjointness is not claimed.

## 4. Rooted infeasibility and full-packing restriction

If the five-rooted graph were feasible, its pole path `P` and the component
`K` of its deletion containing all five centres would be disjoint connected
sets.  They are adjacent through the centre--pole boundary edge established
in Section 2.  Contracting spanning trees of `K` and `P` and deleting unused
vertices of `C` gives a proper minor while leaving `D` untouched.  The two
contraction images receive different colours.  Expanding the literal
boundary on the `D`-side therefore gives all centres one colour and both
poles one common different colour.  Every boundary and `D`-boundary edge is
represented in the minor, so the pullback is proper.  This contradicts the
distinct response of `D`.

For two disjoint connected `S`-full subgraphs `P_1,P_2` in `C`, the sets

```text
P_1 union Z,       P_2 union {p,q}
```

are connected and disjoint.  They are adjacent through the same
centre--pole edge.  Their contractions give the identical forbidden
equal-response pullback on `D`.  Since `C` itself is one connected
`S`-full subgraph, this proves `mu_S(C)=1` exactly.

## 5. Du--Li--Xie--Yu specialization

The primary statement checked was Du--Li--Xie--Yu, *Linkages and removable
paths avoiding vertices*, Theorem 1.2.  For an `m`-rooted graph it gives,
in the infeasible outcome, a terminal-avoiding collection `mathcal X` with

```text
|N(X)| <= m+1
```

for every member and

```text
e(mathcal G / mathcal X)
    <= (m+1)v(G / mathcal X) - m^2/2 - 3m/2 - 1,
```

where `mathcal G/mathcal X` completes all pairs among the `m+2` terminals
except the pole pair.  This is exactly the theorem used, with `m=5`; its
constant is `21` and its neighbourhood threshold is `6`.

Every nonempty collection member is disjoint from the terminals and hence
lies in `C`.  Since `C,D` are anticomplete, its neighbourhood in the rooted
graph is its full neighbourhood in `G`.  A bound of six would separate the
nonempty member from `D`, contradicting seven-connectivity.  Thus there is
no nonempty member; an empty-set member, if formally retained, has no effect
on the quotient.  The quotient is therefore `H`.

The completed seven-terminal graph is `K_7-pq`, with exactly twenty terminal
edges.  With `v(H)=c+7`, the primary bound becomes

```text
e(G[C]) + e_G(C,S) + 20 <= 6(c+7)-21,
```

which is precisely `e(G[C])+e_G(C,S)<=6c+1`.

## 6. Degree bound and the order-five terminal row

All neighbours of a vertex of `C` lie in `C union S`, so minimum degree
eight gives

```text
2e(G[C]) + e_G(C,S) >= 8c.
```

Subtracting the Du--Li--Xie--Yu bound gives `e(G[C])>=2c-1`.  This exceeds
the complete-graph bound for `c<=4`.  If `c=5`, literal-`K_5` exclusion
forces exactly nine internal edges, hence `G[C]` is `K_5^-`.  The imported
order-seven component theorem applies with the same cut `S` and opposite
component `D`, yielding an explicit `K_7^-` minor.  Its current theorem and
audit share SHA-256

```text
39fbb29038292795bcdf5eb46ddbb1710efd46a9529b5495e8d9292d94f29517
```

so the conclusion `|C|>=6` is justified.

## 7. Verdict and scope

The theorem is correct under exactly its displayed hypotheses.  No
unresolved assumption or unsupported contraction, colouring pullback,
packing inference, or edge count was found.

The result does not eliminate components of order at least six and does not
derive the conditional support-five normal form.  Its remaining-gap
paragraph accurately limits the claim to the response-oriented,
rooted-infeasible, packing-one shore with the stated chromatic and density
constraints.
