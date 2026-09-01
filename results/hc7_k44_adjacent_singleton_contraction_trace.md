# Exact contraction trace of an adjacent singleton pair

**Status.** Written unbounded reduction; the adjacent audit identifies the
exact checked revision.  This theorem does not close the adjacent-singleton
case, the literal case of T44, T44, Conjecture 21, or `HC_7`.

## 1. Theorem

Let `G` be a vertex-minimal seven-connected `K_7^-`-minor-free graph
containing a specified literal `K_{4,4}` on vertex set `S`.  Vertex-minimal
means that no graph with fewer vertices has all three properties.  Let
`a,p in V(G)-S` be adjacent.

Then `ap` belongs to an exact seven-cut

\[
                       E=\{a,p\}\mathbin{\dot\cup}T,
                       \qquad |T|=5.                 \tag{1}
\]

The graph `G-E` has two or three components.  If it has three components,
then there is a literal shore `S_i` and an exterior vertex `x` such that

\[
                       E=\{a,p,x\}\mathbin{\dot\cup}S_i.           \tag{2}
\]

Moreover,

\[
                       \Delta(G[E])\le3,             \tag{3}
\]

and the opposite shore `S_{1-i}` meets at least two components of `G-E`.

If `G-E` has two components `C_0,C_1`, then `G[E]` has no `K_5` minor and
exactly one of the following core-distribution alternatives holds.

1. The set `S-T` meets both components.  There is a literal shore `S_i`
   and a vertex `x` such that

   \[
                         T=S_i\mathbin{\dot\cup}\{x\},             \tag{4}
   \]

   and both components meet `S_{1-i}-\{x\}`.
2. All of `S-T` lies in one component, say `C_0`.  The graph
   `G[C_0 union T]` has a `T`-rooted `K_5` model, and `G[E]` has a proper
   bipartition of orders three and four extending the literal shores on
   `E cap S`.  The vertices `a,p` have opposite colours.  For every such
   rooted model, each of `a,p` has a neighbour in at most three of its five
   branch sets.  In particular,

   \[
   |N_G(a)\cap T|\le3,\qquad |N_G(p)\cap T|\le3,
   \qquad |N_G(a)\cap T|+|N_G(p)\cap T|\le5.                     \tag{5}
   \]

   If `a,p` have a unique common neighbour `b`, then `b notin T`.

Consequently, when the adjacent singleton blocker `X={p}` occurs in the
audited literal-exterior reduction, vertex-minimality reduces its
contraction response to the two-component dichotomy above or to the
three-component trace:

1. a two-component trace with either the forced literal-shore split (4) or
   the universal rooted-contact bound (5); or
2. the three-component trace (2)--(3), with one whole literal shore on the
   boundary and the other shore split across at least two full components.

## 2. The contraction cut

Contract `ap` and simplify parallel edges.  The quotient still contains
the specified literal `K_{4,4}` on `S` and is still target-free, because it
is a minor of `G`.  If it were seven-connected, it would contradict the
choice of `G`.

Let `z` be the contracted vertex and let `U` be a cut of the quotient of
order at most six.  Necessarily `z in U`; otherwise the same set would cut
`G`.  The preimage

\[
                         (U-\{z\})\cup\{a,p\}         \tag{6}
\]

cuts `G` and has order at most seven.  Seven-connectivity makes its order
exactly seven, proving (1).  This is the standard contraction/cut
equivalence, included here to fix the quantifiers.

The audited
[seven-cut component theorem](hc7_k7minus_seven_cut_three_component_bound.md)
says that `G-E` has at most three components; it has at least two because
`E` is a cut.  It also gives (3) in the three-component case.

## 3. A five-rooted literal-core model

We use the following elementary fact.

### Lemma 3.1

Suppose that a component `D_0` of `G-E` contains all of `S-T`.  Then
`G[D_0 union T]` has a `T`-rooted `K_5` model.  If `G-E` has two further
components, then `G` contains a `K_7` minor.

#### Proof

Every component of `G-E` is adjacent to every vertex of `E`; otherwise six
vertices of `E` would still separate it.  Apply the audited
[closed-shore rooted-connectivity lemma](hc7_closed_shore_rooted_connectivity.md)
to the component `D_0`, the separator `E`, and the five roots `T`.  The pair

\[
                         (G[D_0\cup T],T)             \tag{7}
\]

is internally five-connected.

Put `I=T cap S` and use the roots in `I` as trivial paths.  In the graph
after deleting `I`, a separator of `T-I` from `S-I` of order below
`5-|I|`, together with `I`, would define a rooted separation of (7) of
order below five; a core target survives because `|S|=8`.  Menger's theorem
therefore gives `5-|I|` further disjoint paths, saturating `T-I` and ending
at distinct vertices of `S-I`.  Together these are five disjoint paths from
the roots in `T` to five distinct core vertices.  Trim each nontrivial path
at its first core vertex.

Any five distinct vertices of a literal `K_{4,4}` root a `K_5` minor using
the other three core vertices.  Indeed, if `h` selected vertices lie in
`S_0`, add the `h-1` unused vertices of `S_1` to distinct selected
`S_0`-rooted bags, and add the `4-h` unused vertices of `S_0` to distinct
selected `S_1`-rooted bags.  Exactly one pure bag remains on each shore,
so all five bags are pairwise adjacent.  Glue the five paths to these core
bags.  The result is a `T`-rooted `K_5` model in `G[D_0 union T]`.

If there are two further components `D_1,D_2`, the two bags

\[
                         D_1\cup\{a\},
                         \qquad D_2\cup\{p\}          \tag{8}
\]

are disjoint and connected.  Fullness makes each adjacent to all five
rooted bags, and the edge `ap` makes them adjacent to one another.  The
seven bags form a `K_7` model.  \(\square\)

## 4. The two-component normal form

Suppose that `G-E` has components `C_0,C_1`.  First, `G[E]` has no `K_5`
minor.  Otherwise its five branch sets, together with the two connected
bags `C_0,C_1`, form a `K_7^-` model: fullness makes each component bag
adjacent to all five branch sets, and the sole allowed missing contact is
between the two components.

Suppose next that `S-T` meets both components.  No opposite-shore pair of
core vertices can lie in different components, because such a pair has a
literal core edge.  Hence all of `S-T` lies in one literal shore, say
`S_{1-i}`.  The whole opposite shore `S_i` is contained in `T`; since
`|T|=5`, there is a vertex `x` with

\[
                         T=S_i\mathbin{\dot\cup}\{x\}.
\]

Both components meet `S-T=S_{1-i}-\{x\}`, proving the first alternative.

Otherwise all of `S-T` lies in one component, say `C_0`.  Lemma 3.1 gives
a `T`-rooted `K_5` model in `G[C_0 union T]`.

We first colour the boundary.  Put

\[
                         I=E\cap S,\qquad B=E-S.
\]

The closed-shore lemma applied with all seven roots in `E` makes
`(G[C_0 union E],E)` internally seven-connected.  Use the roots in `I` as
trivial paths.  Since

\[
                         |S-E|=|B|+1,
\]

Menger's theorem gives `|B|` disjoint paths from the distinct roots in `B`
to distinct vertices of `S-E`.  Indeed, after deleting `I`, a separator of
order below `|B|` together with `I` would be a rooted separation of order
below seven; one of the `|B|+1` target vertices survives.  Trim the paths at
their first core vertices.  The trivial and nontrivial paths give seven
disjoint `E`-rooted bags with distinct core representatives and leave one
core vertex unused.

Colour each root by the shore of its representative.  The colour classes
have orders three and four and extend the literal shores on `I`.  The
colouring is proper on `G[E]`.  Otherwise let `uv` be a same-colour edge and
discard the rooted bag at any `q in E-{u,v}`.  The six retained bags have
six core representatives and leave two core vertices unused: the original
unused vertex and the representative formerly assigned to `q`.  Using
these two vertices, extend the six rooted bags to a `K_6` minus a two-edge
matching, prescribing the `u,v` bags as one of the two pure same-shore
pairs.  The edge `uv` repairs that missing pair, so the six bags have at
least fourteen contacts.  The other component `C_1` is a seventh connected
bag adjacent to all six retained roots, giving at least twenty contacts.
This contradiction proves the boundary colouring.

Since `a,p` are exterior and adjacent, they have opposite colours.  The
opposite class of either vertex contains the other one, so their possible
neighbours in `T` have respective upper bounds two and three, in some
order.  This proves all three inequalities in (5).  If `a,p` have the
unique common neighbour `b`, then `b in T` would put the triangle `apb`
inside the bipartite graph `G[E]`; hence `b notin T`.

Now consider any `T`-rooted `K_5` model `(B_t:t in T)` in
`G[C_0 union T]`.  If `p` had a neighbour in at least four of its branch sets,
then the seven bags

\[
                    (B_t:t\in T),\qquad C_1\cup\{a\},\qquad\{p\}
\]

would have at least

\[
                              10+5+1+4=20
\]

contacts.  Here fullness makes `C_1 union {a}` adjacent to all five rooted
bags, the edge `ap` joins the two additional bags, and the assumed four
contacts come from `p`.  This is a `K_7^-` minor.  Thus `p` meets at most
three rooted bags.  Interchanging `a,p` and using the bag
`C_1 union {p}` proves the same assertion for `a`.  Since each rooted bag
contains its distinct root in `T`, the degree bounds (5) follow.  This
proves the two-component dichotomy.

## 5. The three-component normal form

Suppose `G-E` has three components and `G` has no `K_7` minor.  If `T` did
not contain an entire literal shore, then `S-T` would meet both shores and
would induce a connected complete bipartite graph.  It would therefore lie
in one component of `G-E`, contrary to Lemma 3.1.  Thus

\[
                         T=S_i\cup\{x\}              \tag{9}
\]

for one shore `S_i` and one further vertex `x`.

The vertex `x` is not a core vertex of the opposite shore.  Otherwise its
four literal neighbours in `S_i` would all lie in `E`, giving
`d_{G[E]}(x)>=4`, contrary to (3).  Hence `x` is exterior and (2) follows.

Finally, if the opposite shore `S_{1-i}=S-T` lay in one component of
`G-E`, Lemma 3.1 would apply again.  It must meet at least two components.
This completes the proof.  \(\square\)

## 6. Exact scope

The theorem uses vertex-minimality only to force the contraction cut (1).
It does not assume contraction-critical chromatic structure.  The
three-component conclusion is a trace theorem, not a target-free example.
The two-component case is reduced to the literal-shore split or to the
universal three-bag rooted-contact bound in Section 4.  Those two profiles
and the shore-split three-component trace remain open.
