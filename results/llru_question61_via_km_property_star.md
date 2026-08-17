# Lafferty--Liu--Rolek--Yu Question 6.1 from property `(*)`

**Status.** Complete proof, with primary-source semantics checked.  The
argument answers Question 6.1 of Lafferty--Liu--Rolek--Yu affirmatively.
Its strongest immediate published consequence is an improved connectivity
threshold for contraction-critical graphs, not a new `HC_7` theorem.

## 1. The rooted five-cluster theorem

### Theorem 1.1 (four literal root edges complete partial routing)

Let `G` be a finite simple graph.  Let `v_1,...,v_5` be distinct vertices
with

\[
             \left|E\bigl(G[\{v_1,\ldots,v_5\}]\bigr)\right|\geq4.
\]

For `i in [5]`, let `V_i subseteq V(G)` be pairwise disjoint sets with
`v_i in V_i`.  Suppose that, whenever `v_iv_j` is **not** a literal edge,
there is a `v_i`--`v_j` path contained in `G[V_i union V_j]`.  Then `G` has
a rooted `K_5` model at `v_1,...,v_5`: there are pairwise disjoint connected
sets `B_1,...,B_5`, with `v_i in B_i`, which are pairwise adjacent.

### Corollary 1.2 (Lafferty--Liu--Rolek--Yu Question 6.1)

The same conclusion holds if the displayed edge hypothesis is replaced by

\[
             \alpha\bigl(G[\{v_1,\ldots,v_5\}]\bigr)\leq2.
\]

Assume also that the paths are available for every pair, as in that
question.  Indeed, the
complement of a five-vertex graph of independence number at most two is
triangle-free, so it has at most six edges; the original graph has at least
four.  This is exactly an affirmative answer to Question 6.1 of
Lafferty--Liu--Rolek--Yu (their question assumes equality `alpha=2`).

### Proof

Discard every vertex outside `V_1 union ... union V_5`.  For each `i`,
contract every connected component of `G[V_i]` to one vertex, and call the
resulting simple quotient `Q`.  Colour a quotient vertex with colour `i`
when its contracted component lies in `V_i`.  This is a proper five-colouring
of `Q`: two distinct components of `G[V_i]` have no edge between them.

Let `t_i` be the quotient vertex representing the component of `G[V_i]`
which contains `v_i`.  The set

\[
                             T=\{t_1,\ldots,t_5\}
\]

is a transversal of the quotient colouring.  For every nonedge `v_iv_j`,
the given path maps under the contractions to a `t_i`--`t_j` walk using only
colours `i,j`; after deleting repetitions it contains such a path.  Thus the
routing graph contains every edge of

\[
                     K=\overline{G[\{v_1,\ldots,v_5\}]},
\]

where the five abstract vertices of `K` are identified with `T`.  The
literal-root hypothesis gives `|E(K)|<=10-4=6`.

Kriesell--Mohr Theorem 7 says that every graph on five vertices with at most
six edges has property `(*)`.  Here `K` is a spanning subgraph of the
routing graph.  The definition of property `(*)` therefore gives
pairwise disjoint connected quotient bags `D_1,...,D_5`, with `t_i in D_i`,
such that `D_i,D_j` are adjacent whenever `t_it_j in E(K)`.

They are in fact pairwise adjacent.  If `t_it_j in E(K)`, this is the
certificate adjacency just obtained.  Otherwise `v_iv_j` is a literal edge
of `G`, so its surviving quotient edge `t_it_j`, whose ends lie in
`D_i,D_j`, supplies the adjacency.

Finally lift the quotient contractions.  A quotient vertex `x` represents a
connected component `C_x` of one of the graphs `G[V_i]`; replace each
`D_i` by

\[
                             B_i=\bigcup_{x\in D_i} C_x.
\]

The `B_i` are disjoint.  Each is connected because `D_i` is connected and
every quotient edge is the image of an original edge between the
corresponding components.  The same observation lifts every adjacency
between quotient bags.  Moreover, `t_i in D_i` implies `v_i in B_i`.
Thus `B_1,...,B_5` are the required rooted `K_5` model. `square`

## 2. Exact source audit

The imported source is:

> Matthias Kriesell and Samuel Mohr, *Kempe Chains and Rooted Minors*,
> arXiv:1911.09998v2, 29 November 2022.

The precise source statements used above are:

1. Their notation section (paper pp. 2--3) defines a rooted
   `H`-certificate as pairwise disjoint connected bags `V_t` with `t in V_t`
   and the prescribed bag adjacencies.
2. Their routing graph `H(G,C,T)` has an edge `st` exactly when `s,t` lie in
   one Kempe chain, i.e. one component induced by their two colour classes
   (paper p. 3).
3. Definition 1 (paper p. 4) says that `K` has property `(*)` when, whenever
   a copy of `K` is a spanning subgraph of the routing graph, there is a
   rooted certificate for that copy of `K`.
4. Theorem 7 (paper p. 14) says verbatim in substance: every graph on five
   vertices and at most six edges has property `(*)`.
5. Corollary 1 (paper pp. 15--16) uses the same complement mechanism: a
   connected five-vertex transversal has at least four literal edges, so its
   missing-edge graph has at most six edges; Theorem 7 supplies those missing
   adjacencies and the literal root edges supply the rest.

There are two semantic points which prevent hidden gaps.

* The hypothesis in property `(*)` is only that `K` be a **spanning
  subgraph** of the routing graph.  It need not equal that routing graph.
  Hence taking `K=overline{Q[T]}` inside the complete routing graph is legal.
* A property-`(*)` certificate may mix quotient colours.  Question 6.1 asks
  only for disjoint connected rooted bags, not that the output bag for
  `v_i` remain inside the original `V_i`.  Thus this mixing is legal, and the
  component-contraction lift above returns exactly the requested object.

The question source is:

> Michael Lafferty, Runrun Liu, Martin Rolek and Gexin Yu,
> *Connectivity of contraction-critical graphs*, arXiv:2509.07144v1,
> Question 6.1 (paper p. 14).

Its hypotheses and conclusion agree term-for-term with Corollary 1.2,
except that it writes `alpha({v_1,...,v_5})=2` rather than the harmlessly
stronger `<=2` formulation above.

## 3. Strongest direct published consequence

Immediately after Question 6.1, Lafferty--Liu--Rolek--Yu state that an
affirmative answer improves the first bullet of their Theorem 1.3 to:

> Every `k`-contraction-critical graph is eight-connected for `k>=11`.

Their published Theorem 1.3 currently gives the threshold `k>=17`.  Thus
Theorem 1.1, inserted at the point explicitly identified by the authors,
lowers that threshold from 17 to 11.  This is the strongest consequence
which follows directly from their stated proof architecture.  It is a broad
result about contraction-critical graphs, but it concerns chromatic numbers
at least eleven.

## 4. Novelty and priority

The rooted five-cluster statement appears as an open question in the 2025
Lafferty--Liu--Rolek--Yu preprint, but the proof mechanism substantially
predates that question.  It is already latent in Kriesell--Mohr Theorem 7
and especially their Corollary 1.  The only preprocessing needed here is to
contract the monochromatic components of the five prescribed sets.  A
responsible priority claim is therefore:

*new observation/application resolving Question 6.1 from existing
Kriesell--Mohr machinery*, not a new rooted-minor technology theorem.

No claim of priority over Kriesell--Mohr's complement-certificate method is
warranted.  A release should notify both author groups and search later
versions/citations before claiming that the implication has not already been
noticed.

## 5. Direct relevance to the `HC_7` campaign

The theorem does not by itself close a current `HC_7` branch.

1. The published contraction-critical consequence begins at `k=11`, not
   `k=7`.
2. In the remaining adjacent-degree-eight-true-twin normal form, the common
   boundary is an induced `C_7`.  Here the sharpened edge formulation does
   apply to the *literal roots*: any five consecutive boundary vertices
   induce `P_5` and hence exactly four edges.  The missing hypothesis is
   two-packet routing for each of the six nonliteral pairs of those roots.
   Property `(*)` converts that routing into the model; it does not create
   the routing.
3. In the critical host, `F=G-{a,b}` is six-chromatic.  A six-colouring
   obtained from the contraction/deletion at the twin edge uses exactly five
   colours on the `C_7` boundary.  If its multiplicities are
   `(2,2,1,1,1)`, one can choose one boundary representative of each colour
   which spans at least four cycle edges.  In the only other pattern,
   `(3,1,1,1,1)`, every transversal spans at most three.  Even in the first
   pattern, ordinary criticality does not say that the five selected roots
   lie in the same two-colour component for every colour pair; an optimal
   colouring need not be a Kempe colouring.  Thus applying Theorem 1.1 here
   without an additional simultaneous-Kempe lemma would be circular.
4. If a six-colouring of `F` uses all six colours on `C_7`, then some five
   consecutive boundary vertices are rainbow, so again their literal graph
   is `P_5`.  The same complete-routing gap remains.
5. In a degree-eight neighbourhood outside the pure-cycle row, finding five
   roots of independence number at most two can produce a rooted `K_5` once
   the five two-colour routing sets are available.  Turning that rooted model
   into `K_7^-` still requires an additional exterior/two-centre connector,
   which the theorem does not supply.

There is, however, one exact direct handoff to the campaign's standard
generalized-Kempe machinery.

### Corollary 5.1 (degree-eight rooted `K_5` packet)

Let `G` be seven-contraction-critical, let `x` have degree eight and
`alpha(G[N(x)])=3`, and let `S subseteq N(x)` be an independent triple.  Put

\[
                              R=N(x)-S.
\]

If `e(G[R])>=4`, then `G-(S union {x})` has an `R`-rooted `K_5` minor.

#### Proof

Apply Rolek--Song, *Coloring graphs with forbidden minors*, JCTB 127
(2017), Lemma 1.7, with their parameters `k=7,s=1`.  Their proof contracts
`S union {x}` to a vertex `w` and takes a proper six-colouring with
`c(w)=1`.  Its five vertices in `R` receive the five distinct colours
`2,...,6`.  For every missing edge `uv` of `G[R]`, the proof constructs a
`u`--`v` path induced by the two colours `c(u),c(v)`, with all internal
vertices outside `N[x]`.

For each `r in R`, take as `V_r` the colour class `c^{-1}(c(r))`.  These
five sets are disjoint and contain their respective roots, and every missing
root pair has the required two-packet path.  Theorem 1.1 gives an `R`-rooted
`K_5` model.  None of its bags uses the colour-one vertex `w`; deleting `w`
from the contracted graph is exactly deleting `S union {x}` before the
contraction.  Hence the model lifts to `G-(S union {x})`. `square`

In the induced-`C_7` true-twin residue, take `x=a` and let `b` be its twin.
Every independent triple `S subseteq C_7` leaves

\[
                         R=\{b\}\cup(V(C_7)-S).
\]

The vertex `b` is universal in `G[R]`, so `e(G[R])>=4`; Corollary 5.1
applies for **every** such triple.  In the complement of the literal root
graph, `b` is isolated.  Consequently no property-`(*)` certificate
adjacency is required from the bag rooted at `b`.  Replace that bag by its
root singleton `{b}`.  This preserves all required certificate adjacencies
between the other four bags, while the four literal edges from `b` to their
roots supply every adjacency involving `{b}`.  Thus the other four bags
form a rooted `K_4` model on the vertices of `C_7-S`, disjoint from `{b}`.

This sharpens the remaining connector gap.  Adding `{a}` gives a `K_6`
model.  For `s in S`, both cycle neighbours of `s` lie outside `S`, so the
seven bags

\[
       \{a\},\ \{s\},\ \{b\},\quad
       \text{the four rooted cycle bags}
\]

already have every required adjacency except the two from `{s}` to the bags
rooted at its two nonneighbours in `C_7`.  If `{s}` has even one additional
edge to either of those two bags, the quotient is `K_7^-`.  Consequently,
in a target-free host, **every** such rooted model has each chosen `s`
avoiding both opposite bags.  The present theorem does not force the extra
contact, so this is a strictly sharper but still nonterminal seam
obstruction.

There is a useful spanning form of that obstruction.  Write the cycle as
`0,1,...,6,0` and take `S={0,2,4}`.  The graph

\[
                         H=G-\{a,b,0,2,4\}
\]

is connected (indeed, it is two-connected when `G` is seven-connected).
Starting with the rooted `K_4` model above, absorb every component outside
its four bags into an adjacent bag.  This produces a connected partition

\[
                       V(H)=B_1\dot\cup B_3\dot\cup B_5\dot\cup B_6
\]

whose bags are pairwise adjacent and satisfy `i in B_i`.  If `G` has no
`K_7^-` minor, the preceding seven-bag argument forces

\[
\begin{aligned}
 N_H(0)&\subseteq B_1\cup B_6,\\
 N_H(2)&\subseteq B_1\cup B_3,\\
 N_H(4)&\subseteq B_3\cup B_5.
\end{aligned}
\]

For example, a neighbour of `0` in `B_3` or `B_5` would supply one of the
two missing adjacencies and immediately give `K_7^-`; the other rows are
identical.  Thus the remaining induced-cycle case is not merely missing an
unspecified connector: it must support, for each of the seven independent
triples, a spanning rooted `K_4` partition with three prescribed two-bag
neighbourhood concentrations.  In the usual minimum-degree-eight host,
each left-hand side has at least four exterior neighbours.  No contradiction
with seven-connectivity is presently proved.

Accordingly this result is reusable and has a genuine broad consequence for
high-chromatic contraction-critical connectivity, but it does not meet the
campaign's Norin--Totschnig significance benchmark on its own.
