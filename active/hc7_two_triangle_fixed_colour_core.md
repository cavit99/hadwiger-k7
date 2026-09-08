# A fixed colour core in the two-triangle case

**Status:** written deductions with a separate internal audit. The global
minor construction remains open. These are constraints on a hypothetical
critical host, not a proof of Conjecture 19 or a significance claim.

All graphs are finite and simple. Write `Q=K_7-2K_2`, with independent
deleted edges. Suppose `G` is seven-connected, `delta(G)>=8`, has no
`Q` minor, has chromatic number seven, and every proper minor is
six-colourable. Suppose `d(v)=8` and

`N(v)=A dotcup B dotcup {x,y}`,

where `A,B` are triangles and `xy` is an edge. Additional edges are
allowed. The inputs are
[contraction closure, Corollary 6](hc7_companion_contraction_closure.md),
SHA-256 `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`,
and, only for the rooted four-bag conclusion below,
[bipartite contractibility](../results/bipartite_contractibility_via_matroid_reduction.md),
SHA-256 `3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`.
Both have adjacent audits. No new literature input is used.

## 1. Force four named neighbours into one colour

There are `a in A` and `b in B` such that `{a,b,x,y}` induces only
the edge `xy`. Indeed, contracting the triangle `B` and retaining
the four-clique `{v} union A` shows that there is at most one edge
between `A,B`: two distinct A endpoints would give a literal `K_5^-`
in that quotient. The symmetric argument handles two distinct B
endpoints; thus two distinct cross-edges are impossible. Contracting
`xy` similarly shows that its two endpoints collectively see at most
one vertex of each triangle. At least two choices in each triangle
therefore avoid both `x,y`, and the at most one cross-edge cannot
forbid all four pairs of choices.

**Proposition 1.** There is a six-colouring of `G-xy` in which
`v` has colour `0` and `a,b,x,y` all have colour `1`.

**Proof.** Contract the connected set `{v,a,b,x,y}` and six-colour
the proper minor, giving its merged vertex colour `1`. Expand to
`G-v-xy`, giving all four retained vertices colour `1`. The only
edge among them in `G` was `xy`, now absent; every other incident
edge is represented in the quotient. This is a proper colouring.
The four vertices of

`T=(A-{a}) union (B-{b})`

avoid colour `1` and use at most four colours. One of the five other
colours is absent from `N(v)`; name it `0` and assign it to `v`.
This proves the proposition. The quotient has order `|G|-4` and its
single merged preimage is the specified connected set; the operation
is used only to obtain a colouring, not as an induction class. QED

Fix the resulting classes `C0,C1`, and define the following **fixed**
graphs, even when their remaining vertices are recoloured:

`K=G-(C0 union C1)`,
`J=(G-C0)-xy`.

The set `T` lies in `K`. The only edge of `G[C1]` is `xy`, and
`C0` is independent.

## 2. Constraints on every colouring of the fixed core

**Proposition 2.** The following assertions hold.

1. `chi(K)=4`, `chi(J)=5`, and `chi(J+xy)=6`.
2. Every proper five-colouring of `J` gives `x,y` the same colour.
3. In every proper four-colouring of `K`, each of `N_K(x),N_K(y)`
   meets all four colours.

**Proof.** The fixed colouring gives the indicated upper bounds on
`K,J`; giving `x` a new colour gives the upper bound on `J+xy`.
If `K` were three-colourable, use a fourth colour on `C0`, a fifth
on `C1-{x}`, and a sixth on `x` to six-colour `G`. If `J` were
four-colourable, recolour `x` with a fifth colour and restore `C0`
in a sixth. If `J+xy` were five-colourable, restore `C0` in a sixth.
All three possibilities contradict `chi(G)=7`, proving (1).
The same restoration proves (2). For (3), restore `C0,C1` in colours
`0,1` after any four-colouring of `K`. If `x` missed a core colour,
assigning it that colour would repair the sole monochromatic edge
`xy` and six-colour `G`. The argument for `y` is identical. QED

## 3. A complete alternative, with its ownership limits

**Proposition 3.** At least one of the following two conclusions holds.

* Every four-colouring of `K` makes the four vertices of `T` rainbow.
  In this case `K` contains a `T`-rooted `K_4` minor.
* There is a proper six-colouring of `G-v-xy` and five simple `x-y`
  paths, one using colours `1,i` for each `i=0,2,3,4,5`, all in this
  one colouring. Consequently `G-v` contains an `xy`-rooted `K_{2,5}`
  minor with an additional edge between its two prescribed bags.
  The five other bags may be singleton vertices, one of each colour
  other than `1`; they are not asserted to be the vertices of `T`.

**Proof.** In the first case fix a four-colouring of `K`. Any two
vertices of `T` lie in the same component on their two colours:
otherwise swapping the component containing just one makes their
colours equal on `T`. In particular choose the four bichromatic paths
between `A-{a}` and `B-{b}`. They form a properly endpoint-coloured
`K_{2,2}` scheme. No other root can be internal, and every collection
of intersecting paths shares the endpoint given by the intersection's
colour. Bipartite contractibility gives its rooted model. The two
literal within-triangle edges complete a rooted `K_4`, avoiding both
entire classes `C0,C1`.

Otherwise four-colour `K` so `T` uses at most three core colours,
and restore `C0,C1` in colours `0,1`. For every core colour `i`,
the vertices `x,y` lie in the same `1,i` component of `G-xy`:
swapping one endpoint's component would properly six-colour `G`.
Choose these four paths. They avoid `v`, whose colour is `0`.

A core colour `d` is absent from `T`. Recolour only `v` with `d`;
this is still proper on `G-xy`. The same interchange argument now
gives a `1,0` path from `x` to `y`, avoiding `v`. Both colourings
agree on `G-v`, so all five selected paths have the asserted common
colouring. Their intersections away from colour `1` are disjoint.

Project the five paths onto their colour-`1` vertices: suppress every
other-coloured vertex, retaining it as the label of the resulting
edge. Each label occurs on exactly one projected edge, because its
colour selects one simple path. The projection union is connected.
Choose a spanning tree and remove one edge of its `x-y` path. Its
two components lift to disjoint connected bags rooted at `x,y`,
using only their own forest-edge labels. Each of the five projected
`x-y` paths has an edge crossing the two components. Its label is
unused by the forest and is an actual vertex adjacent to both lifted
bags. Choose one for each colour; these five vertices are distinct.
They give the claimed rooted `K_{2,5}`. The original edge `xy`
supplies the additional contact in `G-v`. QED

The first conclusion does not make the rooted four bags simultaneously
adjacent to two disjoint bags through `x,y`. Proposition 2's assertion
about neighbourhood colours does not establish those model contacts.
In the second conclusion the two forest bags can absorb `a,b` or vertices
of `T`; neither the original triangle contacts nor named leaves survive
automatically. Thus neither conclusion currently supplies `Q`. Choosing
the paths and connected bags jointly with the remaining actual host is
the outstanding global construction. No roots from independent models
are combined, and no new quotient is assumed contraction-critical.
