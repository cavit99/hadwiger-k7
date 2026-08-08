# A triangle in a full false-twin boundary

**Status:** written proof with a separate hash-pinned internal audit.  This
is a computation-free closure theorem.  It does not prove the full
six-connectivity or seven-connectivity density target.

Throughout, `K_7^-` is obtained from `K_7` by deleting one edge.  We use
Norin--Totschnig, Lemma 12, in the following form: if `(F,Q)` is internally
four-connected, `|Q|=4`, and

\[
                       |E(F)|\ge 4|V(F)|-9,
\]

then `F` has a `Q`-rooted `K^*_{4,2}` model.  Such a model has four root
bags and two adjacent helper bags, each helper being adjacent to every root
bag.

## Theorem 1 (false-twin triangle closure)

Let `G` be a six-connected graph of order `n` with

\[
                         |E(G)|\ge 4n-7.
\]

Suppose that `x,y` are nonadjacent vertices with the same six-element
neighbourhood `S`.  If `G[S]` contains a triangle, then

\[
                         K_7^-\preccurlyeq G.
\]

### Proof

Let `a,b,c` span a triangle in `G[S]`, put

\[
                         Q=\{x,a,b,c\},
                         \qquad F=G-y.
\]

The set `Q` induces a `K_4`, because `x` is adjacent to every member of
`S`.  Deleting one vertex from a six-connected graph leaves a
five-connected graph.  Hence `(F,Q)` is internally four-connected.  Since
`d_G(y)=6`,

\[
 |E(F)|=|E(G)|-6
       \ge 4n-13
       =4|V(F)|-9.
\]

The rooted two-helper theorem therefore supplies a `Q`-rooted
`K^*_{4,2}` model in `F`.

Choose such a model maximising the total order of its two helper bags
`U,V`, and, subject to that, minimising the total order of the four root
bags.  For a root bag `R`, let `P_R` be the set of vertices of `R` having a
neighbour in `U` or `V`.  The standard leaf exchange shows that
`|P_R|=1`.  Indeed, if the two helpers had distinct contacts in `R`, replace
`R` by a minimal tree through its prescribed root and those contacts, and
move a non-root contact leaf into the corresponding helper.  The leaf's
tree edge preserves that helper's adjacency to the shortened root bag, and
the other contact preserves the second helper adjacency, contradicting the
choice of the model.  If there are not distinct contacts, both helper
contact sets are the same singleton.

No unused component can meet `U` or `V`, since it could be absorbed into
a helper.  Consequently

\[
             |N_F(U\cup V)-(U\cup V)|\le4.             \tag{1}
\]

If a vertex remained outside the helper union and these at most four
portals, the portals would separate it from the nonempty helper union in
the five-connected graph `F`.  Hence every vertex outside the helpers is
one of the four portals.  Each root bag is therefore a singleton, namely
its prescribed root.

Both helpers are adjacent to the singleton root `x`.  The only neighbours
of `x` in `F-Q` are the three vertices of `S-\{a,b,c\}`.  Thus each helper
contains a vertex of this three-set.  The singleton bag `\{y\}` is adjacent
to both helpers and to the three root bags `\{a\},\{b\},\{c\}`.  It is not
adjacent to the remaining root bag `\{x\}`.

The four singleton root bags and the two helper bags form a `K_6` model:
the root bags are pairwise adjacent through the literal `K_4=G[Q]`, and
all other adjacencies belong to the rooted model.  Adding `\{y\}` leaves
only the pair `xy` possibly nonadjacent.  These seven bags form a
`K_7^-` model.  \(\square\)

## Corollary 2 (the seven-boundary form)

Let `G` be seven-connected, let `R` be a seven-set, and suppose

\[
 G-R=A\mathbin{\dot\cup}\{x\}\mathbin{\dot\cup}\{y\},
 \qquad N_G(x)=N_G(y)=R,
 \qquad xy\notin E(G).
\]

If `|E(G)|\ge4|V(G)|-2`, then `G[R]` is triangle-free unless
`K_7^-\preccurlyeq G`.

### Proof

Delete `y` and repeat the proof of Theorem 1.  The resulting graph is
six-connected, and its edge count is

\[
 |E(G-y)|\ge4|V(G)|-9=4|V(G-y)|-5,
\]

which is stronger than the rooted threshold.  A triangle in `R`, together
with the root `x`, gives the same literal `K_4`; both helpers meet
`R` outside that triangle and hence meet the reinserted vertex `y`.
\(\square\)

## Scope

In the returned seven-cut row where a degree-seven boundary vertex `v` has
exactly two boundary neighbours `s,t`, the case where `s,t` are adjacent is
now closed: `vst` is a boundary triangle.  The nonadjacent case is not
covered.

## External source

Sergey Norin and Agnès Totschnig,
[*Every graph with no `K_7^\vee`-minor is 6-colourable*](https://arxiv.org/abs/2507.03244),
Lemma 12.
