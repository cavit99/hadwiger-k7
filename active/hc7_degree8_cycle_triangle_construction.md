# Reserved neighbours in the degree-eight cycle-and-triangle case

**Status:** written proof; the adjacent audit records its separate internal
verdict at the exact source hash. These are
conditional constructions for Conjecture 19, not a proof of that conjecture
or `HC_7`. No novelty or external peer-review claim is asserted.

All graphs are finite and simple. Write `Q=K_7^=` for the complete graph
on seven vertices with two independent edges deleted. Let `G` be
seven-connected with `chi(G)=7`, every proper minor six-colourable, and
no `Q` minor. Suppose `d_G(v)=8` and its neighbourhood contains the
cycle `0,1,2,3,4,0` and the vertex-disjoint triangle `a0,a1,a2`.
Extra edges are allowed. Put `F=G-v`, `S={0,2,a0}` and
`T={1,3,4,a1,a2}`, and assume explicitly that `S` is independent.

The only minor-extraction input is
[universal bipartite contractibility](../results/bipartite_contractibility_via_matroid_reduction.md),
at SHA-256 `3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`,
with two adjacent independent audits. The critical hypotheses are explicit
here; the [audited companion reduction](hc7_companion_helper_construction.md),
at SHA-256 `0c1ac8052f7734d8d0267381c030e177bd70010eded63d15fdca8c0db6d1f375`,
explains their place in the campaign. This construction requires no
unproved seven-edge routing property.

## 1. A rooted five-clique avoiding the triangle's third vertex

**Theorem 1.** There is a rooted `K_{2,3}` model in `F`, with its
two-root shore `a1,a2` and three-root shore `1,3,4`, avoiding `S`.
Every such model extends to a `T`-rooted `K_5` model avoiding `v,a0`.

**Proof.** Contract the connected star `{v} union S` to `w` and
six-colour this proper minor. Expanding only `S` with the colour of `w`
gives a proper colouring of `F`, since `S` is independent. The five
vertices of `T` have five different colours, all different from `w`:
otherwise the neighbours of `v` use at most five colours and we could
colour `v`, contradicting `chi(G)=7`.

Let `C` be the whole colour class containing `S`, and put `H=F-C`.
Every five-colouring of `H` assigns distinct colours to `T`; otherwise
colour `C` with colour six and give `v` a colour missed by `T`.
In particular, in the inherited colouring any two vertices of `T` lie
in the same component of their two colours: a Kempe swap on just one
of their components would violate this forced distinctness.

Choose such bichromatic paths for the six cross-pairs between
`{a1,a2}` and `{1,3,4}`. They avoid `C` and all other roots. At any
shared vertex its colour identifies a common target endpoint, so they
form a genuine bipartite scheme in `H`. The input supplies the required
rooted model. Denote its bags by `Y1,Y2,X1,X3,X4`, respectively.

The unused vertex `0` can be added to `X4` through the edge `04`, and
the unused vertex `2` to `X3` through `23`. The edges `01,21,34` now
complete the three `X` bags to a triangle. The edge `a1a2` completes
the two `Y` bags. All six cross-contacts survive, giving the rooted
`K_5`. These enlargements are connected and disjoint and avoid `a0,v`.
QED

## 2. The weaker helper condition that would be terminal

**Theorem 2.** For any rooted `K_{2,3}` model as in Theorem 1, if a
connected set `D` in `F` avoids all five bags, contains `a0`, and
contacts at least two of `X1,X3,X4`, then `G` contains `Q`.

**Proof.** The set `D` contacts `Y1,Y2` through `a0a1,a0a2`, and
contacts `v` through `a0v`. There are three cases.

1. If `D` contains neither `0` nor `2`, complete the rooted `K_5` as
   in Theorem 1. The bag `D` contacts at least four of its five bags.
   Adding `D` and `{v}` therefore gives `K_7^-`, hence `Q`.
2. If `D` contains `2` but not `0`, add `0` to `X4`. The five root
   bags have every contact except possibly `X1-X3`. The edges `21,23`
   make `D` adjacent to both ends of that possible missing pair. Its
   only possibly missing root contact is `X4`, so after adding `{v}`
   the possible missing pairs are `X1-X3` and `D-X4`, which are
   independent. If `D` contains `0` but not `2`, interchange `0,2`
   and `4,3` in this argument.
3. If `D` contains both, take a minimal tree inside `G[D]` spanning
   `a0,0,2`. One of `0,2` is a leaf, since every leaf of a minimal
   three-terminal tree is a terminal. Suppose it is `0`. Transfer
   its pendant segment, excluding the first branching or other marked
   vertex, into `X4` through `04`. The remaining tree is connected
   and contains `a0,2`; it contacts `X1,X3` through `2`, and contacts
   the enlarged `X4` through the old cut edge of the tree. It also
   retains both `Y` contacts. The five root bags miss only possibly
   `X1-X3`, so these bags, the remaining tree and `{v}` give
   `K_7^-`. The case with leaf `2` is symmetric.

Every transfer has fixed disjoint preimages and retains the five roots.
Extra contacts can be deleted when taking the target minor. QED

## 3. Exact remaining obligation

For every model in Theorem 1, let `D` be the component of `F` outside
its five bags containing `a0`. Target exclusion and Theorem 2 force
`D` to contact at most one `X` bag. Consequently it contains neither
`0` nor `2`. Its entire neighbourhood in `G` lies in `Y1,Y2`, at most
one `X` bag, and `{v}`. This is an actual separator of order at least
seven: `D` is nonempty and either untouched cycle-root bag survives
outside both `D` and its neighbourhood.

The unresolved step is choosing a model for which this component has
two cycle-bag contacts, or deriving a valid decreasing exchange from
its failure. Three bag labels and `v` are not four actual cut vertices.
No upper bound of six on this boundary is proved. Deleting arbitrary
returned bags does not preserve the connectivity needed for a new
linkage; separate choices of the model and an `a0`--`2` path cannot
be combined without verifying vertex ownership.
