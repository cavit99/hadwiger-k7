# Three-colour boundary flexibility does not force a rooted K4

**Status:** explicit unaudited counterexample to a proposed intermediate
statement, with a direct written proof. It is not a
counterexample to the original critical-host case or to HC7.

The selected host and completion criterion remain those of the
[split-clique construction](../active/hc7_split_clique_construction_working.md):
construct a `K7` minor or a six-colouring in the original host with
`N(u)=P dotunion D`, where `P=K3` and `D=K4` are anticomplete.

## The attempted local reduction

In a six-colouring of `G-u`, suppose `p in P` and `d in D` share colour
zero. Let `a in P-{p}` and `c in D-{d}` have colours one and two.
The graph `L` induced by these three colour classes has four roots
`p,a,d,c` inducing exactly the two edges `pa,dc`.

No proper three-colouring of L can use only two colours on these four
roots: replacing the three-colour layer by that colouring would leave
at most five colours on `N(u)` and extend over u.

Suppose additionally that a and d lie in different zero-one components,
and p and c lie in different zero-two components. Swapping the component
of d or the component of p separately gives colourings whose unique
repeated root pairs are `ad` and `pc`, respectively, in addition to the
original pair `pd`.

The proposed inference was that this boundary-colouring language forces
a `K4` minor rooted at the four roots. It is false, even if all four
possible single repeated cross-pairs occur and both missing-component
conditions hold in the original colouring.

## Six-vertex counterexample

Take roots `p,a,d,c` and two other vertices `x,z`. The edges are exactly

    pa, px, ax, dc, dz, cz, xz.

Thus the graph consists of the two triangles `pax` and `dcz`, joined
by the bridge `xz`. The roots induce exactly `2K2`.

It has no ordinary `K4` minor, hence no rooted one. For example, the
three bags `{p,a,x}`, `{x,z}`, `{z,d,c}`, in that order, are a width-two
path decomposition. Equivalently, its two nontrivial blocks are triangles
and its only other block is a bridge.

In any proper three-colouring, x has the third colour missing from
`{p,a}`, and z has the third colour missing from `{d,c}`. If the four
roots used only two colours, those two unordered pairs would use the
same two colours, so x and z would have the same colour. Their edge
forbids this. Thus both two-pair boundary patterns are excluded.

Every possible single repeated cross-pair is nevertheless realised:

| Repeated pair | p | a | d | c | x | z |
| --- | --- | --- | --- | --- | --- | --- |
| pd | 0 | 1 | 0 | 2 | 2 | 1 |
| ad | 0 | 1 | 1 | 2 | 2 | 0 |
| pc | 0 | 1 | 2 | 0 | 2 | 1 |
| ac | 0 | 1 | 2 | 1 | 2 | 0 |

Each row is checked directly on the two triangles and the bridge.
The first row also has the two required missing connections: its
zero-one components containing a and d are `{p,a}` and `{d,z}`, while
its zero-two components containing p and c are `{p,x}` and `{d,c}`.

## Exact correction to simultaneous Kempe switching

Put `X=component_{0,1}(d)` and `Y=component_{0,2}(p)`. An initial
attempt asserted that X and Y must intersect, because otherwise their
swaps could be performed simultaneously. Disjointness is insufficient.
A colour-one vertex in X and a colour-two vertex in Y both become zero;
an edge between them makes the combined recolouring improper.

The correct forced contact is: X and Y intersect at a zero-coloured
vertex, **or** an edge joins a colour-one vertex of X to a colour-two
vertex of Y. If neither occurs, the simultaneous swaps are proper and
remove zero from the four roots, yielding the forbidden extension.

The example realises the second alternative: `X={d,z}`, `Y={p,x}` and
`xz` is precisely the obstructing edge. It also realises the forced new
singleton-root connections after each individual switch. Swapping X
produces the zero-two path `p-x-z-c`; swapping Y produces the zero-one
path `a-x-z-d`. Thus retaining these coupled switch responses does not
repair the proposed local rooted-minor inference.

## Remaining global allocation

Either kind of forced contact gives an actual p--d path in `X union Y`,
avoiding a and c. But its nonzero vertices can belong to the other
singleton-colour path systems. A sufficient whole-host construction is
a p--d connected set disjoint from a rooted `K2,3` model on
`P-{p},D-{d}`. The five rooted bags are pairwise adjacent using the
original two cliques. Adjoining the p--d set gives a `K6` model, and
adjoining `{u}` gives `K7`.

The bipartite contractibility theorem supplies that rooted `K2,3` from
its bichromatic paths, but does not preserve an independently chosen
p--d path. The first unsupported inference remains their simultaneous
allocation. The six-vertex example defeats only the three-colour local
repair; it has neither the original host's connectivity nor its
proper-minor colouring hypotheses. Further progress must use contacts
through the remaining colour classes while retaining their ownership.
