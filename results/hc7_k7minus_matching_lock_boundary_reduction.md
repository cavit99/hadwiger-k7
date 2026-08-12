# Boundary reduction for matching-edge Kempe locks

**Status:** written unbounded proof;
[separate internal audit GREEN](hc7_k7minus_matching_lock_boundary_reduction_audit.md).
This note bounds the separator returned by an unlocked matching-edge
colouring, and gives a precise normal form when every alternate palette is
locked.  It does not prove the `K_7^-` six-colour conjecture or `HC_7`.

## 1. Setting

Let `G` satisfy

\[
 \chi(G)=7,\qquad
 \chi(J)\leq 6\text{ for every proper minor }J,
 \qquad \kappa(G)\geq 7,
 \qquad K_7\npreccurlyeq G.                         \tag{1.1}
\]

The live application also excludes a `K_7^-` minor.  Only the weaker last
hypothesis in (1.1) is used below.  We use the established cases `HC_6`,
Mader's exact extremal bound, and Jorgensen's equality classification in
the same form as the audited large-boundary response theorem.

For a nonempty connected set `Y`, call `N_G(Y)` an **actual boundary** if

\[
                 V(G)-N_G[Y]\ne\varnothing.          \tag{1.2}
\]

Thus `Y` is one connected side of a genuine separation and is adjacent to
every literal member of its boundary.

## 2. Every large actual boundary strictly descends

### Theorem 2.1 (large actual-boundary singleton descent)

Let `Y` be a nonempty connected set with actual boundary

\[
                         S=N_G(Y),\qquad b=|S|.       \tag{2.1}
\]

If `b>=10`, there is a vertex `w outside S` such that

\[
                         7\leq d_G(w)<b.              \tag{2.2}
\]

Moreover, `N_G(w)` is itself an actual boundary.  For every edge `wx`, a
proper six-colouring of `G-wx` induces a boundary partition on `N_G(w)`
which extends through the edge-deleted singleton side and through `G-w`,
but is rejected by the intact singleton side `G[N_G[w]]`.

#### Proof

First observe that

\[
                         K_6\npreccurlyeq G[S].        \tag{2.3}
\]

Indeed, the connected set `Y` is adjacent to every literal vertex of `S`.
It would therefore complete a `K_6`-minor model in `G[S]` to a `K_7`
model.  By `HC_6`, (2.3) implies that `G[S]` is five-colourable.

Put `n=|V(G)|`.  Suppose every vertex outside `S` had degree at least `b`.
Seven-connectivity gives degree at least seven at every vertex of `S`.
The strict form of Mader's bound in this host is

\[
                         |E(G)|\leq5n-16.             \tag{2.4}
\]

Consequently

\[
       b(n-b)+7b\leq 2|E(G)|\leq10n-32.              \tag{2.5}
\]

For `b=10`, (2.5) reads `10n-30<=10n-32`, a contradiction.  For
`b=11`, it gives `n<=12`, whereas (1.2) and `Y ne empty` give
`n>=b+2=13`.  If `b>=12`, rearranging gives

\[
 (b-10)n\leq b^2-7b-32=(b-10)(b+3)-2.               \tag{2.6}
\]

Thus `n<=b+2`.  Again `n>=b+2`, so equality holds and the two sides
outside `S` are singleton vertices.  They are nonadjacent.  Five-colour
`G[S]` and give both singleton vertices one fresh sixth colour.  This
contradicts `chi(G)=7`.

Hence some `w outside S` satisfies `d_G(w)<b`; seven-connectivity gives
the lower bound in (2.2).  The vertex `w` belongs to one component of
`G-S`, and a different component is disjoint from `N_G[w]`.  Thus
`N_G(w)` is an actual boundary.

Let `x` be a neighbour of `w` and six-colour the proper minor `G-wx`.
The ends `w,x` have one colour, since otherwise restoring `wx` would
six-colour `G`.  Restriction gives proper colourings of `G-w` and of the
edge-deleted singleton side.  If the resulting equality partition on
`N_G(w)` extended through the intact singleton side, align colour names
and glue it to the colouring of `G-w`; this would again six-colour `G`.
The intact side therefore rejects the partition. `\square`

The only new observation relative to the existing large-boundary theorem
is (2.3).  A boundary arising as the full neighbourhood of a connected
side is automatically `K_6`-minor-free; five-colourability of the boundary
is enough for the equality case in the density calculation.

### Corollary 2.2 (finite boundary-order endpoint)

Starting from an actual boundary of order at least ten, repeated application
of Theorem 2.1 terminates with an actual response boundary of order seven,
eight or nine.  The first new boundary and every later one is a
singleton-side response, and every step strictly lowers the boundary order.
The same conclusion holds when the starting boundary already carries a
response: if its order is at most nine, retain it; otherwise start the
iteration.

If the terminal order-nine boundary was produced by Theorem 2.1, it is
`N_G(w)` for a degree-nine vertex `w` with nonempty exterior.  The audited
degree-nine boundary-alignment theorem then gives one of the following.

1. There is an operation-aligned response boundary of order seven or
   eight.
2. There are `x in N_G(w)` and a component `C` of `G-N_G[w]` such that
   `N_G(C)=N_G(w)`, both `C` and `{w}` are full to this nine-set, every
   six-colouring of `G-wx` has `{x}` as an exact boundary block, and
   `G[N_G(w)-{x}]` is `K_5`-minor-free and four-colourable.

#### Proof

The boundary orders are positive integers and decrease whenever they are
at least ten.  The response assertion at each new boundary is Theorem 2.1.
If the last step produces order nine, its singleton vertex has degree nine
and has a vertex outside its closed neighbourhood.  Apply the audited
degree-nine boundary-alignment theorem. `\square`

An initial response boundary of order nine need not be a singleton
boundary, so the second paragraph does not apply to it.  This distinction
is essential in the matching-edge application.

## 3. Consequence for an unlocked matching-edge response

Let `e=ab` and `f=cd` be vertex-disjoint edges, put

\[
                         H=G-\{e,f\},                 \tag{3.1}
\]

and let `phi` be a six-colouring of `H` with

\[
  \phi(a)=\phi(b)=\alpha,\qquad \phi(c)\ne\phi(d).   \tag{3.2}
\]

There is no six-colouring of `H` in which both pairs have distinct
colours.  Say that the pair `a,b` is **unlocked in the palette
`{alpha,beta}`** if its ends lie in different components of the subgraph
of `H` induced by those two colours.

### Theorem 3.1 (bounded endpoint of an unlocked transition)

If `a,b` is unlocked in some alternate palette, then at least one of the
following holds.

1. There is a response-bearing actual boundary of order seven or eight.
2. There is a response-bearing actual boundary of order nine arising from
   one of the two crossed bichromatic components.
3. The sharp degree-nine full-component configuration in
   Corollary 2.2(2) occurs.

The colourings on the exterior of the boundary in outcome 2 are the common
literal restriction of the two opposite singleton responses.

#### Proof

Let `D_a,D_b` be the two bichromatic components containing `a,b`.
Interchanging their two colours separately and using the absence of an
all-proper signature shows that each contains exactly one of `c,d`, both
omitted edges run between the components, and switching either component
gives the opposite singleton response.

The two components cannot both dominate.  If they did, the only edges
between them would be the independent edges `e,f`; domination would force
each component to consist of their two endpoints.  They would form a
four-cycle.  Contract that cycle.  The resulting proper minor is exactly
six-chromatic: a five-colouring could be expanded over the two independent
pairs of the cycle using one fresh sixth colour.  A spanning `K_6` model
in the contraction, supplied by `HC_6`, lifts to five foreign bags, each
adjacent to both dominating components.  The two components and those
five bags form a `K_7` model, a contradiction.

Choose a nondominating component `D`.  Then `N_G(D)` is an actual boundary,
and the two response colourings agree literally on `G-D`; their common
partition is rejected by the intact `D`-side.  If its order is at most
eight, outcome 1 holds; if it is nine, outcome 2 holds.  If it is at least
ten, apply Corollary 2.2.  This gives outcome 1 or 3, except that an
intermediate descent may first terminate at order seven or eight, which is
again outcome 1. `\square`

Thus the formerly unbounded separator has been reduced to order at most
eight, one exact order-nine transition, or the audited sharp degree-nine
pole residue.  The argument does not preserve the original matching-edge
labels after a density descent.

## 4. The all-lock normal form

Assume now that `a,b` are joined in the `alpha`--`beta` subgraph of `H`
for every `beta ne alpha`.  Let `K_beta` denote the component containing
both ends.

### Theorem 4.1 (all locks dominate or return the bounded endpoint)

For every alternate colour `beta`, at least one of the following holds.

1. There is a response-bearing actual boundary of order seven or eight.
2. The set `N_G(K_beta)` is a response-bearing actual boundary of order
   nine.
3. The sharp degree-nine full-component configuration in
   Corollary 2.2(2) occurs.
4. The set `K_beta` is dominating and satisfies

\[
 \chi(G[K_\beta])=3,\qquad
 4\leq\chi(G-K_\beta)\leq5,
 \qquad K_6\npreccurlyeq G-K_\beta.                  \tag{4.1}
\]

In the dominating case, all but at most one vertex of `G-K_beta` receive
one of the four colours outside `{alpha,beta}` under `phi`.  The possible
exception is an endpoint of `f`, and `f` runs between it and `K_beta`.

Consequently, if the first three outcomes have been excluded, the five
alternate palettes give five connected dominating three-chromatic
subgraphs containing the same pair `a,b`, each with a four- or
five-chromatic `K_6`-minor-free complement.

#### Proof

Suppose first that `K_beta` is not dominating.  Its neighbourhood is an
actual boundary.  The restriction of `phi` to `G-K_beta` is proper: the
only monochromatic restored edge is `e`, whose two ends lie in
`K_beta`, while `f` is proper.  The induced boundary partition is rejected
by the intact side, or it would glue to a six-colouring of `G`.  Apply
Theorem 2.1 and Corollary 2.2 exactly as in Theorem 3.1.

Suppose `K_beta` dominates.  The graph `H[K_beta]` is connected and
bipartite.  Its `a`--`b` paths have even length, so restoring the edge
`e` creates an odd cycle.  On the other hand, recolouring one end of `e`
with a third colour gives a proper colouring of `G[K_beta]`.  Hence
`chi(G[K_beta])=3`.

A `K_6` model in `G-K_beta`, completed by the connected dominating set
`K_beta`, would give a `K_7` model.  Thus the complement is
`K_6`-minor-free and `HC_6` gives `chi(G-K_beta)<=5`.  If it were
three-colourable, disjoint three-colour palettes on the two induced
subgraphs would six-colour `G`.  Hence `chi(G-K_beta)>=4`, proving (4.1).

Finally, a vertex outside `K_beta` coloured `alpha` or `beta` cannot have
an `H`-edge to `K_beta`, since that would put it in the same bichromatic
component.  Domination therefore forces every such vertex to be the
outside endpoint of the only other omitted edge `f`.  There is at most one
of them, and `f` crosses from it to `K_beta`. `\square`

## 5. Exact nonclosure

Theorem 4.1 converts the all-lock alternative into a host-level allocation
problem.  It does **not** solve that problem.

The first unsupported inference is

\[
 \begin{gathered}
 \text{a connected dominating three-chromatic lock component,}\\
 \text{a common co-bagged spanning `K_6` model, and an exact
 `K_7^vee` model}\\
 \Longrightarrow\\
 \text{a split meeting four prescribed foreign model bags on both sides.}
 \end{gathered}                                      \tag{5.1}
\]

Domination only says that each foreign bag has some neighbour in the lock
component.  It does not assign those neighbours to three disjoint branch
sets inside the component, nor to both sides of the split of the co-bagged
coordinate.  The five Kempe components may overlap in their
`alpha`-coloured vertices, and palette labels are not model-bag labels.
None of the proved linkage or signature statements supplies this missing
assignment.

There is a second, smaller anchoring loss.  Theorem 2.1 deliberately uses a
fresh edge-deletion colouring after choosing its low-degree singleton.
Its boundary need not retain either original matching edge, the exact
`K_7^vee` branch-set labels, or the original order-nine shore.  Therefore a
strict numerical boundary descent is not automatically a descent in the
labelled proof order.

The smallest repair theorem left by this note has two clauses.

> **Matching-lock allocation or labelled re-entry.**  In the common
> matching-square host, either an order-nine transition or sharp
> degree-nine pole response re-enters the order-at-most-eight argument with
> the required matching/model labels, or one of the five dominating lock
> components admits a split against the common model for which four foreign
> bags meet both sides (and hence gives an explicit `K_7^-` model).

Proving only that a lock component dominates, or only that its complement
has chromatic number four or five, is insufficient.  The missing content is
the literal allocation of model contacts or preservation of the labelled
response through the final boundary reduction.

## 6. Dependencies and scope

The density calculation uses the strict Mader--Jorgensen bound proved in
[`hc7_large_boundary_singleton_response_descent.md`](../results/hc7_large_boundary_singleton_response_descent.md).
The order-nine endpoint uses
[`hc7_tight_degree9_boundary_alignment.md`](../results/hc7_tight_degree9_boundary_alignment.md).
The crossed-component argument is also recorded, with a separate audit, in
[`hc7_k7minus_matching_forbidden_signature_kempe_coupling.md`](hc7_k7minus_matching_forbidden_signature_kempe_coupling.md).

All reductions above are unbounded in the orders of the connected sides.
No finite enumeration is used.  The label loss and implication (5.1) are
recorded negative findings, not counterexamples to the proposed repair
theorem.
