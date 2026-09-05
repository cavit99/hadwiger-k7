# Reduction nonclosures from the bipartite campaign

**Status:** recorded negative findings / route nonclosure, with explicit
counterexamples to the stated intermediate inferences. Recorded
5 September 2026. These are research provenance, not current status;
consult the [research ledger](../RESEARCH_LEDGER.md). The
[universal rooted theorem](../results/bipartite_contractibility_via_matroid_reduction.md)
bypasses both attempted shortcuts.

## Replacing a high-degree target vertex by a tree

**Attempted inference.** Replace each high-degree vertex on the `B` shore
of a bipartite target by a bipartite tree with `B` degrees at most three.
Extend the original incident scheme paths locally to the new prescribed
roots, apply the degree-three theorem preserving all `A` roots, and
contract the target trees in the returned model.

**First unsupported step:** the extended paths need not be a scheme for
the expanded target. Splitting a target endpoint can turn two old
incident edges into independent edges while their paths still intersect.
This fails before the minor-model lift can be invoked.

Here is an explicit instance. The original target and host are the star
with centre `b` and leaves `a_1,...,a_4`. Expand the target to the tree
whose edges are

```
a_1 b_1, a_2 b_1, b_1 c, c b_2, b_2 a_3, b_2 a_4.
```

Its bipartition is `A'={a_1,...,a_4,c}`, `B'={b_1,b_2}` and both `B'`
degrees are three. In the host add new vertices `b_1,b_2,c` and edges
`bb_1,bb_2,b_1c,cb_2`; use the displayed new vertices as prescribed roots.
The natural extension of the old path for `a_1b` is `a_1-b-b_1`, and
that for `a_3b` is `a_3-b-b_2`. These paths meet at `b`, but the expanded
target edges `a_1b_1` and `a_3b_2` have four distinct endpoints. Thus the
common-endpoint axiom fails. Declaring `b` an additional prescribed root
would instead violate the exclusion of foreign roots on these paths.

**Scope.** This refutes the specified automatic local path extension.
It does not rule out a more elaborate global gadget, globally rerouted
paths, or universal rooted contractibility. The degree-three theorem and
the written unrestricted weak-to-rooted equivalence remain valid.

**Smallest repair needed by this route.** For every input scheme, supply
an expanded target with `B` degrees at most three and a valid expanded
scheme, and prove that every model returned under the actual preserved
`A`-root constraints yields the required original rooted model with
disjoint branch sets. A graph-theoretic tree replacement of the target
alone proves neither assertion. The universal matroid proof makes this
gadget reduction unnecessary.

## A five-connected graph with a `K_6` minor need not have the next target

Let `J` denote `K_7` with two independent edges deleted; it has seven
vertices and nineteen edges. The following natural strengthening of a
possible extremal reduction is false:

> Every five-connected graph with a `K_6` minor contains a `J` minor.

**Counterexample with a written verification.** Let
`G=K_1 + complement(C_7)`, with cycle vertices `0,...,6` modulo seven
and apex `7`. Thus two distinct cycle vertices are adjacent in `G`
exactly when they are not consecutive on the cycle. The graph has eight
vertices and twenty-one edges. Each cycle vertex has degree five and the
apex has degree seven.

The graph is five-connected. If the apex survives a deletion it connects
all surviving vertices. If the apex is deleted together with at most
three cycle vertices, at least four cycle vertices remain. Their induced
complement of the cycle is connected: a disconnected partition would
require all pairs across its two nonempty parts to be edges of `C_7`.
Its maximum degree two forces each part to have size at most two; with
four surviving vertices the only possibility is a `K_{2,2}` subgraph of
`C_7`, which does not exist. Deleting the five neighbours of any cycle
vertex disconnects it, so the connectivity is exactly five.

A `K_6` model has branch sets

```
{0,3}, {1,5}, {2}, {4}, {6}, {7}.
```

The two doubletons are edges and the six sets have every pairwise
adjacency, directly from the definition of `G`.

There is no `J` minor. A seven-vertex minor model in an eight-vertex host
either omits one vertex, with all seven branch sets singleton, or uses
one doubleton branch set and six singletons. Vertex deletion leaves at
most sixteen edges. Contracting an edge `uv` leaves
`21-1-|N(u) intersect N(v)|` edges in the simple quotient. Every edge
has at least two common neighbours: an apex edge has four; an edge whose
cycle endpoints have cyclic distance two has three; one of distance
three has two. Thus every one-edge contraction leaves at most eighteen
edges. Further edge deletions cannot supply the nineteen required by
`J`. These cases exhaust all seven-branch-set models.

**First unsupported inference.** A `K_6` minor obtained from an extremal
argument cannot automatically be upgraded to `J` using five-connectivity
alone. Connectivity does not retain the density information needed for
such an upgrade.

**Scope.** This is not a counterexample to Norin--Totschnig Conjecture 20,
which assumes `e(G)>=4|V(G)|-9`: here the required bound is twenty-three,
whereas `e(G)=21`. It also says nothing negative about the bipartite
contractibility theorem, T44 or `HC_7`.

**Smallest repair needed by this route.** Prove a density-sensitive
upgrade retaining the full hypotheses: a five-connected graph other than
`K_6`, with at least `4|V(G)|-9` edges and a `K_6` minor, must contain a
`J` minor. That statement is a remaining theorem obligation, not a
consequence of the counterexample or of connectivity alone.

The exact external conjecture is in Norin--Totschnig,
[*Every graph with no `K_7^vee`-minor is 6-colorable*, Conjecture 20](https://arxiv.org/html/2507.03244v1).
The construction was also checked with NetworkX through the project
`uv` environment, but the finite computation is not needed for the
exhaustive written argument above.
