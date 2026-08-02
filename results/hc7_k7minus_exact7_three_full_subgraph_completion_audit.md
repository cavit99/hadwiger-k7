# Internal audit: exact three-full-subgraph `K_7^-` completion

**Verdict:** GREEN for the stated theorems and explicit branch-set
constructions; the result is nonterminal for the full exact `(1,2)` host.

**Audited source:**
[`hc7_k7minus_exact7_three_full_subgraph_completion.md`](hc7_k7minus_exact7_three_full_subgraph_completion.md)

**SHA-256:**
`7c791436c697f4cbc04dd6f1881dee2b159a9bb63efa18c2a46606da9257a793`

## 1. Static quotient equivalences

The reverse implications are literal.  A `K_4^-` model on the boundary,
together with the displayed anchored universal branch sets, gives seven
connected disjoint sets with at most the one missing adjacency inherited
from that boundary model.

For necessity, enlarging a model to span the connected quotient is valid.
If `r` branch sets contain added universal vertices, the other `7-r` branch sets lie
wholly in the literal boundary and inherit at most one missing mutual
adjacency.

For `J_0(H)`, the cases `r<=2` leave two literal vertices outside four
selected boundary branch sets.  In the `r=2` case, one branch set contains
two of the three independent added vertices and therefore needs a boundary
vertex for connectedness.  For `r=3`, zero boundary anchors would leave
three missing universal-vertex adjacencies, while at least two anchors give
the conclusion immediately.

The sole delicate case has exactly one anchor.  The two unanchored universal
branch sets consume the permitted missing adjacency, so the four boundary
branch sets form a `K_4` model on six vertices.  Their size pattern is
`3,1,1,1` or `2,2,1,1`.  In a nonsingleton branch set, at least two vertices
can be deleted without disconnecting what remains.  The sets of other
branch sets contacted exclusively through those candidate vertices are
disjoint; among three other branch sets, one candidate is therefore
exclusive to at most one.  Its deletion leaves a `K_4^-` model on at most
five vertices.  Together with the universal-branch-set anchor, this gives the required
two avoided literal vertices.

For `J_1(H)`, `r<=2` leaves a fifth boundary branch set.  At `r=3`, an
unanchored universal-vertex configuration would retain both nonedges incident with
`p_0`, so at least one boundary anchor exists.  The four boundary branch
sets avoid it and form a `K_4^-` model.  These arguments prove both stated
equivalences without a finite search.

## 2. Host lift and boundary consequence

The shortest path between the two rich-side full connected subgraphs can
be absorbed into one of them while preserving connectedness, disjointness,
fullness, and their mutual adjacency.  The `J_1` model therefore lifts
literally.  The resulting vertex-deleted `K_4^-` exclusion is not claimed
as new: it was already proved one-way in the connected-rich diamond
deletion lemma.

The displayed three-colour consequence is also a synthesis of existing
inputs.  Three full connected subgraphs give the nine-edge bound, the
vertex-deleted diamond exclusion rules out a literal `K_4`, and the cited
elementary four-critical argument gives `chi(G[S])<=3`.  The critical
two-component theorem supplies an edge and hence the lower bound two.

## 3. Terminal constructions

Lemma 3 has exactly seven branch sets: three full connected subgraphs each
absorb one of the three other vertices of `M union {x,y}`, `X union {o}` is the
fourth, and the triangle `K` supplies three singleton sets.  Boundary
fullness supplies every adjacency involving the first three sets.  The
fourth is adjacent to them through `o` and to at least two triangle
singletons by hypothesis.  Only its adjacency to the third triangle vertex
may be absent.

For Lemma 4, the sets `Q union {m_1}`, `P_1 union {m_2}`, and `P_2` are
mutually adjacent and each is adjacent to `W union {x,y}` by boundary
fullness.  All three meet every triangle singleton.  Again only one
adjacency from the operated support to the triangle may be absent.  These
first two constructions are explicit `K_7^-` models.

Lemma 5 uses three full connected subgraphs anchored at the three vertices
of `M`, two adjacent operated supports anchored at `x,y`, and the two
vertices of `K` as singletons.  Fullness supplies every adjacency involving
the first three branch sets.  The hypotheses supply the support--support
edge, the edge inside `K`, and all but at most one support--`K` adjacency.
The seven displayed sets therefore form a `K_7^-` model.

## 4. Scope and unresolved point

The audit found no proof that an operation-generated support must have the
two named triangle contacts required by Lemma 3 or Lemma 4.  Seven-
connectivity may instead route all additional attachments through the two
rich full subgraphs.  Nor does a returned small separation automatically
identify the neighbourhood of a named exceptional degree-eight vertex.

Accordingly the result may be cited for the two exact quotient
characterizations, their literal lift, and the two terminal constructions.
It may not be cited as an elimination of exact `(1,2)`, a six-colouring of
the general host, or an exceptional anti-neighbourhood descent.
