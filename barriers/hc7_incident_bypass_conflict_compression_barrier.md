# The coupled-bypass conflict graph need not simplify by Kempe normalization

**Status:** written infinite barrier; separate internal audit GREEN in
[`hc7_incident_bypass_conflict_compression_barrier_audit.md`](hc7_incident_bypass_conflict_compression_barrier_audit.md).
This is a barrier to a local inference, not a counterexample to `HC_7`.
Its seven-connected instance contains an explicit `K_7` minor and is not
minor-critical.

## 1. Inference refuted

The following data do not force the simultaneous-switch conflict set to be
a singleton, a matching, a star, connected, or otherwise simpler than an
arbitrary bipartite graph:

1. two incident deleted edges with nonadjacent outer ends;
2. the three equality signatures

   \[
                       (=,\ne),\quad(\ne,=),\quad(=,=),
   \tag{1.1}
   \]

   with no all-proper signature;
3. one common double-contraction colouring with the exact central trace;
4. two named bichromatic component switches giving the opposite one-edge
   responses; and
5. extremality under Kempe interchanges which preserve the central
   equality.

The construction below realizes any prescribed nonempty bipartite graph as
the conflict set.  A positive theorem must additionally use `K_7`-minor
exclusion, the unit response for every conflict edge supplied by full
minor-criticality, or the literal order-eight column geometry.

## 2. Construction

Let `q>=3`, and let `R` be a nonempty finite bipartite graph with fixed
bipartition `(X,Y)`.  Define `M_R` on

\[
             \{s,a,b,p,r\}\mathbin{\dot\cup}X
                              \mathbin{\dot\cup}Y          \tag{2.1}
\]

by the edges

\[
                  sa,sb,sp,sr,ar,bp,                    \tag{2.2}
\]

all edges

\[
                 ax,rx\quad(x\in X),
                 \qquad by,py\quad(y\in Y),             \tag{2.3}
\]

and exactly the edges of `R` between `X` and `Y`.  There are no other
edges.  Let `C` be a disjoint clique of order `q-3` and put

\[
                              G_{q,R}=M_R\vee C.           \tag{2.4}
\]

For `q=3`, the clique is empty.  Mark

\[
                              e=sa,\qquad f=sb.           \tag{2.5}
\]

The outer ends `a,b` are nonadjacent.

Call a proper `q`-colouring of `H=G_{q,R}-{e,f}` **central** when it gives
`s,a,b` one common colour.

## 3. Exact colouring behaviour

### Theorem 3.1

For every `q>=3` and every nonempty bipartite `R`, the graph `G_{q,R}`
has the following properties.

1. `chi(G_{q,R})=q+1`.
2. Simultaneously contracting `e,f` gives an exactly `q`-chromatic graph.
3. On `H=G_{q,R}-{e,f}`, all three signatures in (1.1) occur, while the
   all-proper signature does not.
4. In every central colouring `kappa`,

   \[
       \kappa(s)=\kappa(a)=\kappa(b),
       \qquad
       N_{G_{q,R}}(s)\cap\kappa^{-1}(\kappa(s))=\{a,b\}.
                                                               \tag{3.1}
   \]
5. The two named bichromatic response components are disjoint, and their
   simultaneous-switch conflict graph is exactly `R`.
6. Every Kempe interchange which carries one central colouring to another
   changes only the global palette names.  Hence central-colouring
   minimization cannot change the isomorphism type or size of `R`.

#### Proof

The graph `M_R` is not three-colourable.  In a hypothetical
three-colouring, the triangles `sar` and `arx` force `s` and every
`x in X` to have one colour.  Symmetrically, `sbp` and `bpy` force `s`
and every `y in Y` to have one colour.  An edge of the nonempty graph `R`
then has equal-coloured ends.  On the other hand,

\[
       a=b=0,\qquad p,X=1,\qquad r,Y=2,
       \qquad s=3                                      \tag{3.2}
\]

is a proper four-colouring.  Thus `chi(M_R)=4`, and additivity of
chromatic number under graph join proves item 1.

Delete `e,f`.  With three distinct base colours `0,i,j`, put

\[
       s=a=b=0,\qquad p,X=i,qquad r,Y=j,              \tag{3.3}
\]

and give the clique `C` its own `q-3` colours.  This is a proper
`q`-colouring `kappa` of `H` and proves (3.1).  It descends through the
simultaneous contraction.  Conversely, after contraction the base contains
the triangle formed by the contraction image, `r`, and any `x in X`.
Hence the contracted base is exactly three-chromatic, and its join with
`C` is exactly `q`-chromatic.  This proves item 2.

In (3.3), the `0,i` component through `a` is

\[
                              A=\{a\}\cup X,            \tag{3.4}
\]

and the `0,j` component through `b` is

\[
                              B=\{b\}\cup Y.            \tag{3.5}
\]

Switching `A` gives one proper one-edge response and switching `B` gives
the other.  Together with the central colouring these are the three
signatures in (1.1).  An all-proper colouring of `H` would restore both
marked edges and `q`-colour `G_{q,R}`, contrary to item 1.

The components `A,B` are disjoint.  Switching both makes every vertex of
`X union Y` colour zero, and their only cross-edges are exactly `E(R)`.
Thus the conflict graph is `R`, proving item 5.

It remains to check that another central colouring cannot simplify the
example.  In any three-colouring of the base part of `H` with `s,a,b`
equal, the triangles `arx` force all of `X` to use the nonzero colour
different from `r`; the triangles `bpy` do the same for `Y` and `p`; and
one edge of `R` forces the colours on `X,Y` to differ.  Up to swapping the
two nonzero colours, (3.3) is therefore the only central colouring.

The two-colour subgraph on the nonzero base colours is connected: `r`
sees all of `X`, `p` sees all of `Y`, and one edge of `R` joins the two
parts.  Its interchange is a global transposition.  A `0,i` or `0,j`
component interchange changes at least one of `s,a,b` without the others
and hence leaves the central class.  Every clique colour is joined to all
base vertices, so an interchange involving it is again a global palette
transposition; the same is true between two clique colours.  This proves
item 6 and completes the theorem. \(\square\)

## 4. A seven-connected instance is already terminal

### Proposition 4.1

The graph `G_{6,K_{3,3}}` is seven-connected and contains an explicit
`K_7`-minor model.

#### Proof

The base `M_{K_{3,3}}` is four-connected.  After deleting at most three
vertices, if both bipartition classes retain a vertex, the surviving
complete bipartite subgraph connects them, and every surviving member of
`a,r` or `b,p` attaches to the appropriate class; `s`, when present,
attaches to `a,b,p,r`.  If one entire three-vertex class is deleted, no
other vertex was deleted and the remaining displayed edges are connected.
Thus no set of at most three vertices disconnects the base.  Since `s` has
degree four, its connectivity is exactly four.

Now `G_{6,K_{3,3}}=M_{K_{3,3}}\vee K_3`.  After deleting fewer than seven
vertices, a surviving clique vertex joins every remaining vertex; if all
three clique vertices are deleted, at most three base vertices were also
deleted and the base remains connected.  Hence the join is
seven-connected.

Choose an edge `xy of K_{3,3}`.  The four sets

\[
                 \{s\},\qquad\{a\},\qquad\{r\},
                 \qquad\{b,x,y\}                         \tag{4.1}
\]

form a `K_4`-minor model in `M_{K_{3,3}}`: the last set is connected
through `b-y-x`, its contacts with the first three bags are `sb,ax,rx`,
and `sa,sr,ar` give the remaining adjacencies.  Adding the three singleton
vertices of the joined clique gives the asserted explicit `K_7`-minor
model. \(\square\)

## 5. Scope

The construction shows that neither shortestness nor Kempe extremality in
the common contraction colouring bounds the conflict graph.  For `q=6`
this remains true in a seven-chromatic, seven-connected graph.

It does not refute the active order-eight theorem.  The seven-connected
example is terminal through its displayed `K_7` minor.  When `R` has more
than one edge the construction is also not minor-critical: deleting one
edge of `R` leaves another edge and the same four-chromatic triangle
forcing.  It has no order-eight two-full-shore or latent-column structure.

Accordingly, the active proof must spend at least one omitted hypothesis:
`K_7`-minor exclusion through an explicit branch-set construction, the
full unit response table from minor-criticality, or a label-preserving use
of the order-eight columns.  Kempe normalization by itself cannot compress
the conflict set.
