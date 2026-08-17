# Lo minors survive every elementary one-step reduction

**Status:** internal deductions audited GREEN conditional on Lo, Theorem
1.3.  Its primary-source statement was checked against arXiv:2603.27973v1,
which remains an unrefereed version-one preprint; the repository has not yet
reconstructed every figure-based terminal certificate in Lo's proof.  This
is a global structural side theorem for the six-connected density route.  It
does not prove the six-connected `4n` extremal target or the `K_7^-`
six-colour conjecture.

## Theorem

Let `G` be a six-connected simple graph with `n>=8` vertices and at least
`4n-9` edges.  Each of the following graphs is five-connected, non-planar,
and has minimum degree at least five:

1. `G-v`, for every vertex `v`;
2. the simple graph `G/e` obtained by contracting any edge `e`; and
3. `G-e`, for every edge `e`.

Consequently, every one of these graphs contains both a `K_6^-` minor and a
`K_{3,4}` minor.

Here `K_6^-` is obtained from `K_6` by deleting one edge.

## Proof

Put `m=|E(G)|`.  We first prove the connectivity assertions.

For a vertex `v`, a cut of order at most four in `G-v` would, together with
`v`, be a cut of order at most five in `G`.  Hence `G-v` is five-connected.

Now contract an edge `xy` to a vertex `w`, and call the resulting simple
graph `H`.  Suppose that `S` is a cut of `H` with `|S|<=4`.  If `w` is not
in `S`, the same set separates `G`.  If `w` is in `S`, then

\[
                 (S-\{w\})\mathbin\cup\{x,y\}
\]

separates `G` and has order at most five.  Both alternatives contradict
six-connectivity.  Thus `H` is five-connected.

Finally, let `H=G-xy`.  Suppose that `S`, with `|S|<=4`, separates `H`.
The ends `x,y` do not belong to `S`, since otherwise `G-S=H-S` would be
disconnected.  Adding the single edge `xy` must join all components of
`H-S`; hence there are exactly two, say `A` and `B`, with `x` in `A` and
`y` in `B`.  Neither component is a singleton.  Indeed, if `A={x}`, then
all neighbours of `x` in `G` lie in `S\cup\{y\}`, contrary to
`d_G(x)>=6`; the argument for `B` is symmetric.  It follows that
`S\cup\{x\}` is a cut of `G` of order at most five, again a contradiction.
Therefore `G-xy` is five-connected.

All three graphs consequently have minimum degree at least five.  It
remains to prove non-planarity.  Deleting a vertex removes at most `n-1`
edges.  Contracting an edge removes that edge and one copy of each edge to
a common neighbour, again at most `n-1` edges in total.  Thus, in either
case, the resulting graph has `n-1` vertices and at least

\[
       m-(n-1)\ \ge\ 3n-8\ >\ 3(n-1)-6
\]

edges, so it is non-planar.  The edge-deleted graph has at least
`4n-10>3n-6` edges and is non-planar as well.

Lo's Theorem 1.3 states that every four-connected non-planar graph of
minimum degree at least five contains `K_6^-` as a minor, and also contains
`K_{3,4}` unless it is isomorphic to `K_6`.  Each graph above is
five-connected and has at least seven vertices, so none is `K_6`.
Applying that theorem proves both minor conclusions. \(\square\)

## Sharpness of the density entrance

The additive constant `-9` is best possible for the assertion about every
vertex deletion.  Let `I` be the icosahedron and let

\[
                         Q=K_1\vee I.
\]

The graph `I` is a five-connected planar triangulation with twelve vertices
and thirty edges.  Therefore `Q` is six-connected and

\[
             |V(Q)|=13,\qquad |E(Q)|=42=4|V(Q)|-10,
\]

but deleting the universal vertex leaves the planar graph `I`.

Moreover, `Q` has no `K_7^-` minor.  In any putative model, remove the at
most one branch set containing the universal vertex.  If that branch set
is present, the six remaining branch sets lie in `I` and form either a
`K_6` model or a `K_6^-` model, according as the missing pair of the
`K_7^-` model uses the removed branch set.  Both minors are non-planar.  If
the universal vertex is unused, the whole model lies in `I`.  Every case
contradicts planarity.

Thus the one-edge improvement from `4n-10` to `4n-9` is precisely where
every vertex deletion is forced into Lo's non-planar regime.  At the
campaign's `4n` threshold, all three kinds of elementary one-step reduction
carry both unavoidable minors.

## Exact implication for the current route

Suppose in addition that `G` has no `K_7^-` minor.  For every vertex `v`,
Lo supplies a `K_6^-` model in `G-v`, but no such model can have all six
branch sets adjacent to `v`: otherwise those six branch sets together with
`{v}` form a `K_7^-` model.  Similarly, every edge contraction contains a
`K_6^-` model, but every such model is obstructed from lifting through the
corresponding vertex split to seven branch sets with at most one missing
adjacency.

Accordingly, the remaining issue is not existence of a near-`K_6` minor
after a first reduction.  It is the rooted compatibility of that minor
with the deleted vertex or contracted edge.  The adjacent
[one-apex icosahedral counterexample](../barriers/hc7_k7minus_unrooted_k6minus_augmentation_barrier.md)
shows why the unrooted conclusion alone cannot perform this lift.

## Primary source

- O.-H. S. Lo,
  [*A characterization of graphs with no `K_{3,4}` minor*](https://arxiv.org/abs/2603.27973v1),
  Theorem 1.3.

As of 17 August 2026 the cited record is arXiv version 1, submitted 30
March 2026, with no journal reference or later revision located.  The
elementary deductions above are complete once Theorem 1.3 is accepted; this
note is not an independent proof or full certificate audit of that external
theorem.
