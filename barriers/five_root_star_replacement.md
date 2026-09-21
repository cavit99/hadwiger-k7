# Replacing a density-one side by a boundary star can destroy 4-lightness

**Status:** explicit counterexample to an unqualified replacement rule;
written proof with a separate hash-pinned internal audit. This does not refute
the stronger rooted helper target or Conjecture 21.

For a five-rooted graph with root set X, put
`rho4(G)=|E(G)-E(G[X])|-4|V(G)-X|`. For a nonroot set Y,
`rho4(G,Y)` counts edges with at least one endpoint in Y, minus `4|Y|`.
The graph is 4-light when every nonroot set with at most four external
neighbours has nonpositive density.

## Construction

Let `X={r1,r2,r3,r4,r5}` be independent, and let the nonroots be
`{v,a,b,y}`. The edge set consists exactly of:

- all five edges from v to X, and the edge vb;
- the six edges from `{a,b}` to `{r1,r2,r3}`, and the edge ab;
- the five edges from y to `S={v,a,b,r4,r5}`.

These disjoint lists contain eighteen edges. There are four nonroots,
so `rho4(G)=18-4*4=2`. The singleton side `{y}` has boundary S and
density `5-4=1`. Its boundary centre v is not an original root.

**Claim.** Every nonempty nonroot set has at least five external
neighbours. In particular G is internally five-connected and 4-light.

**Proof.** A set containing v has all five roots in its boundary.
A set containing y and at least one of a,b also has all five roots
in its boundary. The singleton `{y}` has the five neighbours in S.
The remaining possibilities are `{a}`, `{b}`, and `{a,b}`; their
boundary orders are respectively five, six, and five. These cases
exhaust all nonempty nonroot subsets. QED

The side is linked to the original roots outside its interior: the
five vertex-disjoint paths are `r1-a`, `r2-b`, `r3-v`, and the two
trivial paths at r4 and r5. Thus the example retains an actual external
five-linkage, not just a boundary of order five.

## Replacement and failure

Delete y and add the boundary star with centre v and leaves
`a,b,r4,r5`; call the result H. Only va is a new edge, because vb,
vr4, and vr5 already exist. The replacement is also a rooted minor:
contracting vy gives exactly H, with the merged vertex named v.

There are fourteen edges and three nonroots in H, so its global
density remains `rho4(H)=14-4*3=2`. However, `{a,b}` now has boundary
`{r1,r2,r3,v}`. Its incident edges are ab, the six edges to
`{r1,r2,r3}`, and va,vb. Therefore

`rho4(H,{a,b})=9-4*2=1>0`.

Consequently H is not 4-light. A density-one side, a boundary-rooted
star, an external five-linkage, and preservation of global density
do not suffice to preserve 4-lightness under this replacement.

## Unaffected scope

In G, the set `{a,b}` has boundary `{r1,r2,r3,v,y}` and ten incident
edges, so its density is two. The corresponding root five-separation
is proper: r4 and r5 lie outside its closed side. Thus this example
does not satisfy a proposed additional exclusion of proper root
five-separations whose right-hand sides have density at least two.
It supplies no counterexample to a replacement theorem retaining all
minimal-counterexample hypotheses, or to the stronger helper theorem.
