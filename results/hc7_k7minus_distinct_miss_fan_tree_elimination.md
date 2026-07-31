# Contracted-star responses and fan-tree completion for distinct misses

**Status:** written proof with a computer-assisted finite completion;
[separate internal audit GREEN](hc7_k7minus_distinct_miss_fan_tree_elimination_audit.md).
The retained standard-library verifier is
[`hc7_k7minus_distinct_miss_fan_tree_completion_verify.py`](hc7_k7minus_distinct_miss_fan_tree_completion_verify.py).

Let `K_7^-` denote `K_7` with one edge deleted.  The main theorem eliminates
the complete **distinct nonadjacent-miss** case at an exceptional
degree-eight vertex.  It does not address distinct adjacent misses, the
one-nonfull case, or the both-full case.

## 1. A reusable contracted-star response

### Lemma 1 (contracted-star response path)

Let `q>=2`, let `G` be `(q+1)`-chromatic, and suppose every proper minor of
`G` is `q`-colourable.  Let `u` be a vertex, and let
`J` be a nonempty independent subset of `N(u)` such that

\[
                         |N(u)-J|=q-1.
\]

For every nonedge `rs` of `G[N(u)-J]`, there is an `r`--`s` path whose open
interior lies in one component of `G-N[u]`.

#### Proof

Contract the connected star `G[\{u\}\cup J]` to one vertex.  This is a
proper minor because `J` is nonempty.  Pull a `q`-colouring of that minor
back only to `G-u`; all vertices of `J` then have one common colour, say
`0`.

Put `R=N(u)-J`.  Every vertex of `R` avoids colour `0`.  Moreover, all
other `q-1` colours occur on `R`: if one were absent, it would be absent
from all of `N(u)` and could be assigned to `u`.  Since `|R|=q-1`, the
vertices of `R` therefore have pairwise distinct colours.

Let `r,s` be nonadjacent vertices of `R`.  If they belonged to different
components of the subgraph induced by their two colours, interchange those
colours on the component containing `r`.  The old colour of `r` would then
be absent from `N(u)`, so it could be assigned to `u`, again contradicting
the chromatic number of `G`.  Thus a bichromatic `r`--`s` path exists.

Choose such a path shortest.  Its internal vertices avoid `J`, whose colour
is `0`, and avoid `R`, where `r` and `s` are the unique vertices with the
two path colours.  Its open interior is consequently contained in
`G-N[u]`.  Since it is connected, it lies in one component of that graph.
\(\square\)

## 2. The exact common-six reduction

Assume from now on that

\[
 \kappa(G)\ge7,\qquad \chi(G)=7,\qquad
 \chi(M)\le6\text{ for every proper minor }M\text{ of }G,\qquad
 K_7^-\npreccurlyeq G.                                      \tag{H}
\]

Let `u` be an exceptional degree-eight vertex, put `X=N(u)`, and suppose
`G-N[u]` has exactly two components `E,F` with

\[
 N_X(E)=X-\{x\},\qquad N_X(F)=X-\{y\},\qquad
 x\ne y,\qquad xy\notin E(G).                               \tag{1}
\]

Write `Z=X-\{x,y\}` and `H=G[Z]`.  The established exceptional-neighbourhood
and distinct-miss reductions give

\[
 \alpha(G[X])=3,\qquad K_4\not\subseteq G[X],\qquad
 K_4\npreccurlyeq H,\qquad
 K_4^-\npreccurlyeq H-z\quad(z\in Z).                       \tag{2}
\]

### Corollary 2 (dynamic elimination of the parity boundary)

\[
                              \alpha(H)\le2.                 \tag{3}
\]

#### Proof

If `J` were an independent triple in `Z`, apply Lemma 1 with `q=6`.
The five vertices of `X-J` include the nonadjacent pair `x,y`, so the lemma
gives an `x`--`y` path whose open interior lies in `E` or in `F`.  The path
is nontrivial.  It cannot lie through `E`, because `E` has no neighbour
`x`, and it cannot lie through `F`, because `F` has no neighbour `y`.
This contradiction proves (3). \(\square\)

In particular, Corollary 2 eliminates the exact `3K_2` boundary underlying
the earlier even/odd trace-language obstruction.  It uses a named
star-contraction colouring and its Kempe response, not arbitrary static
trace coverage.

### Lemma 3 (the two remaining common-six graphs)

Under (2)--(3), `H` is isomorphic to either

\[
                     K_3\mathbin{\dot\cup}K_3
\]

or that graph with one edge joining the two triangles.

#### Proof

By `R(3,3)=6`, the six-vertex graph `H` contains a triangle `A`; let `B` be
the other three vertices.  A vertex of `B` has at most one neighbour in
`A`, since two such neighbours together with `A` give a literal `K_4^-`
after deleting either other vertex of `B`.  If two vertices `b,c` of `B`
were nonadjacent, their sets of neighbours in `A` would have union of order
at most two.  A vertex of `A` missed by both would make an independent
triple with `b,c`, contrary to (3).  Hence `B` is also a triangle.

The symmetric argument shows that the edges between `A` and `B` form a
matching.  If there were two such edges, delete the third vertex of `A` and
contract the edge joining the two retained vertices of `A`.  Together with
the three singleton vertices of `B`, this is a `K_4^-` model, contrary to
(2).  Thus there is at most one edge between the two triangles. \(\square\)

## 3. Fan trees in the two exterior components

### Lemma 4 (terminal-respecting tree contraction)

Let `C` be connected, let `T` be nonempty, and let `(P_t:t\in T)` be
pairwise disjoint nonempty connected subgraphs of `C`.  There are pairwise
disjoint connected subgraphs `(Q_t:t\in T)`, with `P_t\subseteq Q_t`, whose
contact graph contains a tree on the labelled set `T`.

#### Proof

Contract each `P_t` to a distinct marked vertex and take a tree in `C`
connecting all marked vertices.  While an unmarked vertex remains, contract
an edge incident with it, propagating the other endpoint's marked label
when there is one.  No marked--marked edge is contracted, so two labels are
never identified.  The final graph is a tree on the marked vertices, and
the preimages of its vertices are the required connected subgraphs.
\(\square\)

For `v\in\{x,y\}`, put

\[
                    M_v=\{z\in Z:vz\notin E(G)\}.             \tag{4}
\]

### Lemma 5 (two fan-tree minors)

There are pairwise disjoint connected subgraphs

\[
                (P_z:z\in M_x)\subseteq F
\]

and a tree `T_x` on `M_x` such that `P_z` is adjacent to `x` and `z`, and
`P_z` is adjacent to `P_w` whenever `zw\in E(T_x)`.  Symmetrically, there
are such subgraphs

\[
                (Q_z:z\in M_y)\subseteq E
\]

and a tree `T_y` on `M_y`, with every `Q_z` adjacent to `y` and `z`.
When a marked set has order at most one, use the graph on that set with no
edges.

#### Proof

Each of `M_x,M_y` meets both boundary triangles: otherwise the corresponding
portal together with one triangle would be a literal `K_4` in `G[X]`.
The graph `G-u` is six-connected: a separator of order at most five in
`G-u`, together with `u`, would contradict seven-connectivity of `G`.
The fan lemma therefore gives six paths from `x` to the six distinct
vertices of `Z`, pairwise disjoint except at `x`.  Use the edge `xz`
itself whenever it is present.

For `z\in M_x`, the remaining `x`--`z` path is nontrivial and has no other
vertex of `Z`.  Its first internal vertex cannot lie in `E`, which misses
`x`, and cannot be `y`, since `xy` is absent.  It therefore lies in `F`.
The path cannot subsequently leave `F` through `E`, through `y`, or through
another vertex of `Z`; hence its entire open interior lies in `F`.
These open interiors are nonempty, connected, and pairwise disjoint.
Apply Lemma 4 inside the connected component `F`.  Each resulting marked
subgraph still contains the corresponding open path, so it remains adjacent
to both `x` and `z`.  This gives `T_x` and the subgraphs `P_z`.

The argument with `y,E` in place of `x,F` gives `T_y` and the subgraphs
`Q_z`. \(\square\)

## 4. Finite rooted completion

Label the two triangles of `H` by `012` and `345`; in the second type let
the unique joining edge be `03`.  For `A_x=N_Z(x)` and `A_y=N_Z(y)`, form
the **static quotient** `\Gamma(H,A_x,A_y)` on

\[
                        Z\cup\{x,y,u,e,f\}.
\]

It retains `G[X\cup\{u\}]`, makes `e` adjacent precisely to
`Z\cup\{y\}`, and makes `f` adjacent precisely to `Z\cup\{x\}`.  It has
no other edge incident with `e` or `f`.  Contracting `E` and `F` whole
shows that this quotient is a minor of `G`.

For trees `T_x,T_y` supplied by Lemma 5, form the corresponding
**two-fan-tree graph** from `H` as follows:

- retain `xz` for `z\in A_x` and replace every missing `xz` by
  `x p_z, p_z z`;
- add `p_zp_w` for every edge `zw` of `T_x`;
- make the symmetric construction with `y,q_z,T_y`; and
- retain `u` adjacent to every vertex of `X`.

Lemma 5 shows that this graph is a minor of `G`.

### Lemma 6 (computer-assisted finite completion)

Suppose `H` is one of the two graphs in Lemma 3 and
`G[X]` has independence number three and no literal `K_4`.  Then either

1. the static quotient `\Gamma(H,A_x,A_y)` contains a `K_7^-` minor; or
2. for every pair of labelled trees `T_x,T_y`, the two-fan-tree graph has
   six pairwise disjoint connected branch sets, one containing each
   prescribed vertex of `Z`, with at least fourteen of their fifteen
   pairwise adjacencies.

#### Finite verification

Encode a neighbourhood in `Z` by a six-bit hexadecimal mask, with bit `i`
corresponding to vertex `i`.  Up to automorphisms of `H` and interchange of
`x,y`, the nonterminal static quotients are exactly:

| `H` | `(A_x,A_y)` masks | labelled tree pairs |
|---|---:|---:|
| `2K_3` | `(01,06)` | 2,000 |
| `2K_3` | `(03,05)` | 256 |
| `2K_3` | `(03,0c)` | 256 |
| `2K_3+03` | `(01,06)` | 2,000 |
| `2K_3+03` | `(02,05)` | 2,000 |
| `2K_3+03` | `(03,05)` | 256 |
| `2K_3+03` | `(03,06)` | 256 |
| `2K_3+03` | `(06,09)` | 256 |
| `2K_3+03` | `(06,30)` | 256 |

The verifier regenerates all `1,032` and `1,113` labelled valid portal
patterns for the two boundary types, respectively.  It reduces them to
`21` and `109` symmetry orbits, constructs and validates a connected
seven-bag certificate for every quotient-terminal orbit, and obtains the
three and six rows displayed above as the only survivors.

For every one of the `7,536` labelled tree pairs in those rows, it assigns
each portal and marked tree vertex to one of the six prescribed root bags
or leaves it unused.  It checks rooted connectivity, disjointness, and all
branch-set contacts directly, retaining a certificate with at least
fourteen contacts.  Thus the computation proves the stated rooted
`K_6^-` conclusion, rather than only a Boolean boundary classification.

Run

```text
python3 results/hc7_k7minus_distinct_miss_fan_tree_completion_verify.py
```

to obtain

```text
GREEN: distinct-miss fan-tree completion verified
bridge=0 labelled_valid=1032 valid_orbits=21 quotient_survivor_orbits=3 tree_pair_counts=(2000, 256, 256)
bridge=1 labelled_valid=1113 valid_orbits=109 quotient_survivor_orbits=6 tree_pair_counts=(2000, 2000, 256, 256, 256, 256)
mask_orbit_digest=1d653544a19aed2fac36589f1d113583fe29f7a2af58679e90b574558d9f3203
quotient_certificate_digest=cb251c5518e05b5b1ba79a9149600226777cee5e8677f6bf9a8af90b18b626c3
fan_tree_certificate_digest=5c19a21365f7380afef89b6164dcbee3752db001198cb04aa9270bc4aad33785
```

The finite domain consists only of the two proved boundary graphs, the two
literal portal masks, and labelled trees on at most five marked vertices in
the nine quotient-survivor orbits.  No bound is placed on the order of
`E`, `F`, or `G`; Lemma 5 is the written reduction from those arbitrary
connected components.

## 5. Elimination of the complete branch

### Theorem 7 (distinct nonadjacent misses are impossible)

Under (H), an exceptional degree-eight vertex with exactly two exterior
components cannot have the distinct nonadjacent attachment pattern (1).

#### Proof

Corollary 2 and Lemma 3 reduce `H` to the two graphs used in Lemma 6.
The exceptional-neighbourhood theorem supplies the remaining portal
hypotheses `\alpha(G[X])=3` and `K_4\not\subseteq G[X]`.

If the static quotient is terminal, its validated branch sets lift through
the contractions of `E` and `F` to a `K_7^-` model in `G`.  Otherwise,
Lemma 5 supplies some labelled trees `T_x,T_y`, and the second conclusion
of Lemma 6 supplies six connected branch sets rooted at the six literal
vertices of `Z`, with at most one missing adjacency.  The singleton
`\{u\}` is adjacent to every one of those bags through its literal root.
These seven branch sets form a `K_7^-` model in `G`, contrary to (H).
\(\square\)

## Scope and dependencies

Lemma 1 is an unbounded, reusable dynamic-colouring statement.  In this
application it eliminates every common-six boundary with an independent
triple, including the exact `3K_2` parity obstruction.  The fan-tree
construction and finite certificates then produce an explicit `K_7^-`
model for both remaining analytic boundary types.  This is not the
elimination of one isolated boundary graph and records no new static
barrier.

The host reduction uses:

- [exceptional-neighbourhood completion](hc7_k7minus_exceptional_neighbourhood_completion.md);
- [distinct-miss boundary reduction](hc7_k7minus_nonfull_attachment_reduction.md).

The theorem closes the distinct **nonadjacent**-miss branch only.  Distinct
adjacent misses already reduce to connected-rich `(1,2)` cuts and are not
claimed to be eliminated here.  The result proves neither the global
`K_7^-` six-colour conjecture nor `HC_7`.
