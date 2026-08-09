# Internal audit: tri-inseparable full-subgraph barrier

Audited file:
`barriers/hc7_k7minus_tri_inseparable_full_subgraph_barrier.md`.

Audited mathematical revision SHA-256:

```text
f61c7b21835006408700689393fe38a5c71906d469fdad0a756853b535188357
```

Promoted source SHA-256:

```text
2b5eed9089f00aee00b4271febf7a16a8ee986b246610ee1fc9eaf268d1648ad
```

The promoted source differs only in the opening status, which now links to
this audit, and the resulting line wrapping.  Its mathematical content is
unchanged.

**Verdict:** **GREEN** for both revisions above.

This is a separate internal mathematical audit, not external peer review.
The construction and each stated property were checked directly.  No
computer-assisted claim or external structural theorem is used.

## Construction, degrees and clique number

The four parts of `C=K_{2,2,2,1}` are
`{c_0,c_1}`, `{c_2,c_3}`, `{c_4,c_5}` and `{c_6}`.  Hence `c_0,...,c_5`
have five neighbours in `C`, while `c_6` has six.  Every point of the
displayed Fano system lies on three lines.  It follows that the first six
vertices of `C` have degree eight in `G` and `c_6` has degree nine.  Each
vertex of `D` has its two cycle neighbours and all seven neighbours in `S`,
and every vertex of `S` has three neighbours in `C` and five in `D`.
Therefore `delta(G)=8`, and every vertex of `U` has degree eight.

No clique meets both `C` and `D`, since these sets are anticomplete, and a
clique contains at most one vertex of the independent set `S`.  The clique
number of `C` is four.  A clique containing a vertex `s_i` and vertices of
`C` has order at most four because `s_i` has only three neighbours there.
Inside `D union S`, a clique has order at most three.  Thus `G` is
`K_5`-free.

## Connectivity and the exact cuts

Let `X` contain at most six vertices.  If `D-X` is nonempty, then
`(D union S)-X` is connected because both `D-X` and `S-X` are nonempty and
all edges between them are present.  When `|X cap C|<=4`, the graph `C-X`
is connected because `K_{2,2,2,1}` is five-connected.  The Fano incidence
graph between `C` and `S` has 21 edges and degree three at every vertex.
The vertices in `(X cap C) union (X cap S)` cover at most 18 of those
edges, so an edge from `C-X` to `S-X` remains.  When `|X cap C|>=5`, at
most one vertex of `S` was deleted, and every surviving vertex of `C`
retains at least two neighbours in `S-X`.  These observations make `G-X`
connected whenever `D-X` is nonempty.

If `D subseteq X`, all five vertices of `D` have been deleted and at most
one other vertex is absent.  The remaining part of `C` is connected, and
each remaining vertex of `S` retains a neighbour in it.  Hence `G-X` is
again connected.  This proves `kappa(G)>=7`.  Since the seven-set `S`
separates the nonempty connected sets `C` and `D`, `kappa(G)=7`.

Deleting the four vertices of `U` from a seven-connected graph leaves a
three-connected graph, so `H=G-U` is three-connected.  The sets `S` and
`T` are independent.  Moreover,

```text
G-S = C dotunion D,       H-T = C dotunion D,
```

and every boundary vertex has a neighbour in both components.  Thus these
are respectively exact order-seven and order-three cuts.  In particular,
each member of `T` has three neighbours in `C`.

## Mixed separations splitting `C`

Let a mixed cut of `C` use a vertex set `R` of order `k`, and suppose both
open sides are nonempty.  After deleting `R`, the remaining graph is
complete multipartite, has order `7-k`, and has no part larger than two.
For `k<=4`, its minimum degree and edge-connectivity are at least `5-k`.
The cut therefore contains at least `5-k` crossing edges and has mixed
order at least five.  For `k>=5`, the same conclusion is immediate from
the vertex part of the cut.  The `k=4` case, which is not needed for the
claimed exclusion of order-three separations, also follows directly from
the five-connectivity of `C`: at least one crossing edge remains.

If a mixed separation of `H` splits `C`, its separator vertices lying in
`C` and its separator edges with endpoints in the two open parts of `C`
form such a mixed cut.  This cut has order no larger than the original
mixed separator.  Consequently every mixed separation of `H` that splits
`C` has order at least five.  In particular, no mixed separation of order
at most three, and hence no tri-separation, splits `C`.

## Fano obstruction

The seven triples in the construction are the lines of the Fano plane.  To
check their non-two-colourability, suppose no line is monochromatic and
choose a colour used on at least four points.  If it is used on at least
five points, its point pairs determine at least ten distinct lines because
no line contains three points of that colour, contradicting the existence
of only seven lines.  If it is used on exactly four points, their six pairs
determine six distinct lines of colour type `2+1`.  The three pairs among
the other three points require three further distinct lines of the opposite
type.  This would require nine lines, again a contradiction.

If disjoint sets `P,Q subseteq C` were each adjacent to all of `S`, every
Fano line would meet both sets.  Colouring `P` and `Q` differently and then
colouring the remaining points arbitrarily would give the forbidden
two-colouring.  Thus no such disjoint sets exist.  This is stronger than
the stated failure of two disjoint connected subgraphs.

## Explicit `K_7` minor and scope

For `0<=i<=4`, each branch set `B_i={d_i,s_i}` is connected.  Distinct
sets `B_i,B_j` are adjacent through the edge `s_i d_j`.  The set
`P={c_0,c_1,c_6}` is connected through `c_6`, and
`Q={c_2,c_3,c_4,c_5}` is connected as `K_{2,2}`.  They are adjacent.  For
each `i=0,...,4`, the Fano line incident with `s_i` meets both `P` and `Q`,
so both are adjacent to `B_i`.  The seven disjoint branch sets therefore
form the asserted `K_7`-minor model.

The example satisfies every hypothesis of the implication in Section 1
and fails its conclusion.  Since it contains a `K_7` minor, it is not a
counterexample to the `K_7^-` six-colour conjecture.  Its scope is exactly
the claimed one: tri-inseparability and the stated local degree conditions
alone do not produce two disjoint boundary-full connected subgraphs.  It
does not address arguments that additionally use minor-criticality, the
exclusion of a `K_7^-` minor, or the fixed boundary-colouring data.
