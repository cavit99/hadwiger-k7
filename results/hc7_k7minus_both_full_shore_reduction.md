# Both-full shore reduction at an exceptional degree-eight vertex

**Status:** written host reductions and a computer-assisted finite boundary
classification; separate internal mathematical and computational audits
GREEN for this revision.  The retained verifier is
[`hc7_k7minus_both_full_shore_reduction_verify.py`](hc7_k7minus_both_full_shore_reduction_verify.py).
This result does not prove shore allocation, the `K_7^-` six-colour
conjecture, or `HC_7`.

Let `G` satisfy

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G.                         \tag{H}
\]

Let `u` be an exceptional degree-eight vertex, put `X=N_G(u)`, and suppose
`G-N_G[u]` has exactly two components `E,F`, both adjacent to every vertex
of `X`.  Put `H=G[X]`.  The exceptional-neighbourhood theorem gives

\[
                         \alpha(H)=3,
              \qquad    K_4\not\subseteq H.            \tag{1}
\]

A connected subgraph disjoint from `X` is **`X`-full** when it is adjacent
to every literal vertex of `X`.  For a subgraph `P` of `G-X`, let
`\mu_X(P)` be the maximum number of pairwise vertex-disjoint connected
`X`-full subgraphs in `P`.

## 1. The correct terminal rooted object

### Lemma 1 (shore-confined rooted near-model completion)

Let `I\subseteq X` be an independent triple and put `R=X-I`.  Suppose one
closed shore, say `G[R\cup E]`, contains five pairwise disjoint connected
bags `(B_r:r\in R)`, with `r\in B_r`, among which at most one pair is
nonadjacent.  Then `G` contains a `K_7^-` minor.

#### Proof

The seven branch sets are

\[
                         \{u\}\cup I,\qquad F,\qquad (B_r:r\in R). \tag{2}
\]

The first set is connected through `u`, and it is adjacent to `F` through
`I`.  Both are adjacent to every rooted bag: the first through `ur`, the
second through the full-shore contact at `r`.  Thus the only possible
missing adjacency in (2) is the one already allowed among the five rooted
bags. \(\square\)

Accordingly, a shore-confined rooted `K_5^-` is terminal; a full rooted
`K_5` is more than is needed.

## 2. Every two-vertex deletion is diamond-minor-free

### Lemma 2 (diamond-deletion lemma)

For every two-set `Z\subseteq X`,

\[
                            K_4^-\npreccurlyeq H-Z.       \tag{3}
\]

#### Proof

Write `Z=\{z_E,z_F\}`.  If `B_1,\ldots,B_4` were the bags of a `K_4^-`
model in `H-Z`, then

\[
        \{u\},\qquad E\cup\{z_E\},\qquad F\cup\{z_F\},
        \qquad B_1,\ldots,B_4                         \tag{4}
\]

would form a `K_7^-` model.  The first three sets are connected and
pairwise adjacent: `u` sees both anchors, while each full component sees
the opposite anchor.  Each is adjacent to every boundary bag, and at most
one boundary-bag adjacency is absent.  This contradicts (H). \(\square\)

No critical-colouring or connectivity hypothesis is used in Lemma 2.

## 3. Exact finite boundary reduction

For an independent triple `I\subseteq V(H)`, put `R_I=V(H)-I` and define

\[
 q_H(I)=\binom52-|E(H[R_I])|,
 \qquad \lambda(H)=\min_I q_H(I).                     \tag{5}
\]

### Theorem 3 (computer-assisted order-eight classification)

Up to isomorphism, exactly 15 graphs of order eight satisfy all of

1. `\alpha(H)=3`;
2. `H` has no literal `K_4`; and
3. `H-Z` has no `K_4^-` minor for every two-set `Z`.

Their `\lambda` distribution is

\[
              \#\{\lambda=5,6,7,8\}=1,7,5,2.          \tag{6}
\]

In the present host, `G-X` has the three `X`-full components
`\{u\},E,F`.  The audited three-full-component clique odd-cycle-transversal
theorem excludes eight of the 15 boundary graphs.  Exactly seven remain:

```text
GCOcaO  GCOcbO  GCOcbW  GCOe`W  GCOebW  GCQQV?  GCQR@O
```

Their `\lambda` values, in the same order, are

```text
8  7  7  7  6  6  8
```

For every minimizing triple in every survivor, the five-vertex reserve is
respectively

\[
 \begin{array}{c|c}
 \lambda(H)&H[R_I]\\ \hline
 6&P_5\\
 7&P_3\mathbin{\dot\cup}K_2\\
 8&2K_2\mathbin{\dot\cup}K_1.
 \end{array}                                           \tag{7}
\]

#### Reproducible verification

Run

```text
.venv/bin/python results/hc7_k7minus_both_full_shore_reduction_verify.py
```

The verifier streams all 12,346 unlabelled order-eight graphs from `geng`,
checks (1) directly, and tests (3) by an exact deletion/contraction recursion
for `K_4^-`.  It independently enumerates every clique odd-cycle
transversal and every independent triple.  The sorted 15-code and seven-code
digests are

```text
6e2633b0f4999a1d09fb98f38f7c268044cada0095be8e84aa4b8fe72d879ebe
bf063de64c772c1c9c1c83cba7dc39d11bb9c214f3e101595889fe63f25861a0
```

The finite theorem classifies only the literal boundary.  The reduction
from the unbounded host to its hypotheses is Lemma 2 and the written
three-full-component colouring theorem.

## 4. Dynamic demand and packet restrictions

Fix an independent triple `I\subseteq X` and put `R=X-I`.  Contract the
three edges from `u` to `I` to one vertex and six-colour the resulting
proper minor.  Pulling the colouring back to `G-u` makes `I` one colour
class on `X`.  Since `I` is maximal in `H`, no vertex of `R` has that
colour.  All six colours must occur on `X`, or the colouring would extend
to `u`; hence the five vertices of `R` receive the other five colours
distinctly.

For a nonedge `rs` of `H[R]`, the two roots lie in one bichromatic
component.  Otherwise swapping the two colours on the component containing
`r` removes its old colour from `X`, again allowing `u` to be coloured.
No internal vertex of an `r-s` bichromatic path lies in `X`, so its
interior is contained in `E` or in `F`.  For this fixed colouring, let
`A_E,A_F` be the sets of reserve nonedges admitting such a path through
the indicated component.  Thus

\[
                  E(\overline{H[R]})=A_E\cup A_F.       \tag{8}
\]

### Lemma 4 (actual shore support must remain mixed)

Let `2\le q=q_H(I)\le7`.  If one of `A_E,A_F` has at least `q-1` members,
then
`G` contains a `K_7^-` minor.  Consequently, for every minimizing triple
of a surviving type with `\lambda=6` or `7`, every star-contraction
colouring satisfies

\[
                         2\le |A_E|,|A_F|\le q-2.       \tag{9}
\]

#### Proof

Suppose, by symmetry, that `A_E` contains a set `D` of `q-1` demands.
Delete the colour class of `I` and restrict the fixed colouring to the
five rainbow roots and `E`.  For each pair in `D`, its roots remain in the
same bichromatic component of this five-coloured graph.  Since
`|D|=q-1\le6`, Kriesell--Mohr Theorem 7 supplies five disjoint connected
rooted bags adjacent across every pair in `D`.

Every edge of `H[R]` is a literal edge between its two rooted bags.  Thus
the five bags have all ten pairwise contacts except possibly the one
reserve nonedge not selected into `D`.  They form a shore-confined rooted
`K_5^-`, and Lemma 1 gives a `K_7^-` minor.

In a surviving host both shore-support sets therefore have order at most
`q-2`.  Equation (8) then gives

\[
 |A_E|\ge q-|A_F|\ge2,
 \qquad |A_F|\ge q-|A_E|\ge2,
\]

which proves (9). \(\square\)

### Lemma 5 (two packets and a reserve path)

Let `I\subseteq X` be an independent triple, put `R=X-I`, and suppose
`H[R]` contains a three-vertex path `a-b-c`.  If one exterior component
`P` contains two disjoint connected `X`-full subgraphs `P_1,P_2`, then
`G` contains a `K_7^-` minor.

#### Proof

Let `d,e` be the other two roots.  Inside the closed `P`-shore use the five
rooted bags

\[
        \{a\},\quad\{b\},\quad\{c\},
        \quad P_1\cup\{d\},\quad P_2\cup\{e\}.         \tag{10}
\]

They are connected and pairwise adjacent except possibly for
`\{a\},\{c\}`.  Fullness supplies every contact involving a packet bag,
including the contact between the two packet bags through the opposite
root.  Lemma 1 completes (10) with the other exterior component. \(\square\)

### Lemma 6 (four full subgraphs and a boundary triangle)

If `H` contains a triangle and `G-X` contains four pairwise disjoint
connected `X`-full subgraphs, then `G` contains a `K_7` minor.

#### Proof

Let `T` be a boundary triangle.  Choose four distinct anchors from the five
vertices of `X-T`, one for each full subgraph, and unite each subgraph with
its anchor.  These four connected bags form a clique: either member of a
pair sees the other's anchor.  They are adjacent to the three singleton
vertices of `T`, which themselves form a clique.  These are seven branch
sets of a `K_7` model. \(\square\)

### Corollary 7 (exact both-full packet residue)

For each of the seven boundary types in Theorem 3,

\[
                         \mu_X(E)=\mu_X(F)=1.           \tag{11}
\]

#### Proof

For `\lambda=6,7`, choose a minimizing triple.  The corresponding reserve
in (7) contains a `P_3`.  Lemma 5 shows that neither exterior component can
have packing number at least two.  Each component is itself connected and
`X`-full, so both packing numbers equal one.

For `\lambda=8`, each of the two classified boundary graphs contains a
triangle.  If `\mu_X(E)+\mu_X(F)\ge3`, those exterior packets together with
the singleton full subgraph `\{u\}` give four disjoint `X`-full connected
subgraphs in `G-X`.  Lemma 6 gives a `K_7` minor, contrary to (H).  Since
each packing number is positive, both equal one. \(\square\)

## 5. Exact gain and limitation

The both-full case has therefore collapsed from 2,076 exceptional
neighbourhoods to seven named boundary types, and every survivor has the
exact full-subgraph packing vector

\[
                          (\mu_X(\{u\}),\mu_X(E),\mu_X(F))=(1,1,1). \tag{12}
\]

This is an unbounded host reduction with one finite boundary census.  It
does not construct a shore-confined rooted `K_5^-`.  The accompanying
[shore-allocation barrier](../barriers/hc7_k7minus_shore_allocation_barrier.md)
shows that all 15 diamond-deletion types admit a balanced abstract
two-shore demand labelling under every independent-triple rotation.  Lemma
4 adds the genuine colouring information available now: on a `\lambda=6`
or `7` survivor, each actual fixed response still has at least two demands
supported through each shore.  Thus the next valid theorem must use
compatibility among changing proper-minor colouring responses, or the
topology left after deleting a rooted model; boundary counting and one
fixed response cannot provide the allocation.

## Inputs

- [exceptional-neighbourhood completion](hc7_k7minus_exceptional_neighbourhood_completion.md)
- [three-full-component boundary classification](hc7_order8_three_component_boundary_classification.md)
- [four full boundary subgraphs and a triangle](hc7_four_boundary_full_subgraphs_triangle_completion.md)
- [Kriesell--Mohr rooted-minor conversion](hc7_k7minus_degree7_clique_incidence.md)
- [critical proper-minor hypotheses](../active/hc7_k7minus_seven_exceptional_frontier.md)
