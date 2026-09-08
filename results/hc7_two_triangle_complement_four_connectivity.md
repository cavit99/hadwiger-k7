# Four-connectivity of the two-triangle complement

**Status:** written proof; two separate internal audits are recorded beside it. This is a
structural conclusion about the remaining two-triangle configuration,
not a proof that this configuration cannot occur.

All graphs are finite and simple. Let `Q` be `K_7` minus two independent
edges. A contact means an actual edge between two disjoint connected
vertex sets; additional contacts are harmless.

**Theorem.** Suppose `G` is seven-connected, `delta(G)>=8`, `G` has no
`Q` minor, and `d(v)=8`. Suppose
`N(v)=A dotcup B dotcup {x,y}`, where `A,B` are literal triangles and
`xy` is an edge; additional edges are allowed. Then `H=G-v-B` is
four-connected. The analogous conclusion holds with `A,B` exchanged.

The sole packaged proof input is
[separator allocation](hc7_two_triangle_separator_allocation.md),
SHA-256 `283444e901f18ec60f461eca91e158806a45e2b42394d6a87e5b54134c7b4b2b`.
Its Theorems 1--2 give the side structure and four-connected minimal
torso. Its Section 3 supplies the rooted almost-clique model and the
actual-port normalization used below. Those inputs have their own
stated dependencies and adjacent internal audits. No finite enumeration
or proper-minor colouring hypothesis is used here.

## 1. Enlarge and normalize the two rooted bags

Suppose `H` has a three-cut. Choose a cut `T` minimizing its A-side `L`.
The input gives exactly two components `L,O` of `H-T`, containing
`A-T` and `{x,y}-T`, respectively; each is full to
`{v} union B union T`. Also `T` meets `N(v)` at most once, and
`K=H[L union T]+K_3(T)` is four-connected.

Choose `t3 in T-A`; write the other cut vertices as `t1,t2`.
All three A vertices lie in `L union {t1,t2}`. Write `B={b0,b1,b2}`.
On `G[L union B union {t1,t2}]`, the input gives a rooted five-bag
model with every contact except possibly one of `b0-t1,b0-t2`.
Regard that model as lying in the larger graph
`F*=G[L union T union B]`.

Among all such models in `F*`, maximize the union `W` of the two
T-rooted bags, then minimize the three B-rooted bags. The same
actual-port argument applies in this larger graph: the `b0` bag is
the singleton `b0`; each other B bag `P_i` is a path from `b_i` to
one actual port `p_i`, and that port contacts both T bags. Every edge
from `P_i` to `W` has its endpoint in `P_i` equal to `p_i`. An unused
component cannot contact `W`, since it could be absorbed. Here a port
may equal its prescribed B root. These conclusions concern the actual
graph `F*`, without adding torso edges to a branch set.

For completeness, the optimization preserves the allowed model class.
For a B bag contacting both T bags at distinct vertices, a minimal
tree through its root and contact vertices has a nonroot contact leaf.
Transfer that leaf to its contacted T bag: the other contact and the
old tree edge retain both required B contacts. This enlarges `W`.
Thus there is only one contact vertex; minimizing the bag leaves the
root-to-port path. In the designated `b0` bag, moving a nonroot port
to either contacted T bag preserves an old allowed hole or creates
exactly one allowed hole, so maximality makes that bag singleton.
Literal B-triangle edges preserve the three B-to-B contacts throughout.

The actual boundary of `W` inside the torso `K` is contained in
`{p1,p2,t3} intersect V(K)`: `b0` is outside `K`, and only the added
T-clique edges may supply an extra boundary vertex `t3`. Since `K`
is four-connected and `W` is nonempty,

`V(K)-W subseteq {p1,p2,t3}`.                         (1)

Since `t3` is not an A vertex, (1) puts at least one A vertex in `W`.
Consequently `v` contacts a T bag. The opposite component `O` is
disjoint from the entire model and is adjacent to `v` and to each
of its five bags through the prescribed B or T root.

A full core gives `Q`, as do two T bags contacted by `v`. If the
core's sole hole is incident with the T bag contacted by `v`, that
hole and the missing contact from `v` to the other T bag are
independent, again giving `Q`. We may therefore name the bags `U,V`,
rooted at `t1,t2`, so that `U` contacts all three B bags, `v` contacts
`U` and misses `V`, and the sole core hole is `V-b0`.

In fact `A subseteq U`. One A vertex already lies in `U`. Another
A vertex outside `W` has its literal A-edge into `U`, so it cannot
be unused and must be the common port of a non-designated B bag.
Move this port into `V`. The old root-path edge retains `V`'s contact
with that B bag; only `U`'s contact to it may be lost. This loss and
the old `V-b0` hole have different B ends. Both T bags now meet `v`,
and `O,v` are full adjacent apices over the five bags, giving `Q`.
No A vertex lies in `V`, because `v` misses it. This proves the claim.

## 2. Three A regions and their actual exits

The graph `K-t3` is three-connected and contains all of `A` in `U`.
Take the vertices of `(K-t3)-U` as sinks. Give every vertex outside
`V` capacity one and every vertex of `V-{t3}` capacity three; each
A source has capacity one. There are three source-saturating paths.
Indeed, a cut of capacity at most two removes at most two vertices,
none in `V-{t3}`; an A source survives, and three-connectivity joins
it to the surviving sink `t2`. Vertex splitting and integral flow
therefore give the asserted paths. Distinct paths may end at the same
V vertex, but cannot use the same non-V sink.

Stop each path at its first vertex outside `U`, and discard this last
vertex to obtain three disjoint connected A-rooted prefixes inside
`U`. By (1), the exit is in `V-{t3}` or is one of the nonroot ports
`p1,p2` lying in `K-t3`. The only possible nonactual edge of `K-t3`
is `t1t2`; if used, it is the final edge of one prefix containing
`t1`. Thus all prefix edges retained inside `U` are actual edges.

Extend these prefixes to a connected partition of all of `U`, by
repeatedly assigning an unassigned vertex adjacent to an assigned part.
Call the part containing `t1` `A0`, and the other two `A1,A2`. Each
contains a distinct original A vertex, so the three parts are pairwise
adjacent by the original triangle. Put `D=O`.

The bag `D` contacts `A0`, `V`, all three B bags and `v`. The vertex
`v` contacts all three A parts and all B bags. Each B bag contacts at
least one A part, since `U` was full to the B bags. Each of `A1,A2`
has an actual exit to `V` or to a nonroot B port. Port exits of these
two parts are distinct. A possible virtual final edge occurred only
in the part `A0`; it supplies no asserted V contact for that part.

## 3. Explicit seven-bag models for every exit case

The following constructions use only actual contacts. A union mentioned
as a bag is connected by an indicated contact, and all bags in each
display are disjoint. The B bags always retain their original roots,
and hence their triangle and their contacts with `v,D`.

**No port exit.** Both `A1,A2` contact `V`. For each B bag select an
A part contacting it. Among `A1,A2`, choose `Aj` selected at most
once, and let `Ai` be the other part. Use

`X=A0 union Ai,  Y=Aj union V,  P0,P1,P2,D,{v}`,

where `P0={b0}`. Both unions are connected. All contacts hold except
possibly `X-Pk` for the at most one B bag selecting `Aj`, and `Y-P0`.
If that selected bag is `P0`, its contact with `Aj` supplies `Y-P0`.
Otherwise the two possible holes have distinct B ends. They are
therefore independent, giving `Q`.

**One port exit.** Relabel the non-designated B bags so the exit uses
`p1` in `P1`. Move this single leaf into `V`, writing
`V'=V union {p1}` and `P1'=P1-{p1}`. The path `P1'` is nonempty and
connected, and its old last edge gives `V'-P1'`. Both `A1,A2` now
contact `V'`. The bags `P0,P2` still contact A parts; only `P1'` may
have lost every A contact. Choose A neighbours for `P0,P2`.

If some `Aj` among `A1,A2` is chosen by neither, take
`X=A0 union Ai, Y=Aj union V'` and keep `P0,P1',P2,D,{v}`.
The only possible holes are `X-P1'` and `Y-P0`.
Otherwise the choices are distinct: say `P0` chooses `Ai` and `P2`
chooses `Aj`. Take

`X=A0 union Aj,  Y=Ai union P0,  V',P1',P2,D,{v}`.

The only possible holes are `X-P1'` and `v-V'`. In both alternatives
the displayed unions are connected and the two holes are independent.

**Two port exits.** Label them so `A1` contacts `p1 in P1` and `A2`
contacts `p2 in P2`. Choose `i in {1,2}` so `P0` contacts `A0` or
`Ai`, and let `j` be the other index. Keep `p_i` in its original
B bag and use

`X=A0 union Ai,  Y=Aj union V union {p_j},`
`P0, P_i, P_j-{p_j}, D, {v}`.

The first union is connected by the A triangle; the second uses the
actual contacts `Aj-p_j-V`. The shortened B bag is a nonempty path.
The bag `X` contacts `P0` by choice and `P_i` through the retained
fan exit to `p_i`. The bag `Y` contacts `P_i` through `V-p_i` and
the shortened `P_j` through the old path edge at `p_j`. Both `X,Y`
contact `v,D` and each other. Thus the only possible holes are
`X-(P_j-{p_j})` and `Y-P0`, which are independent.

Every case gives a `Q` minor, contradicting the standing hypothesis.
Thus `H` has no three-cut. Since the input already gives
three-connectivity, it is four-connected. Interchanging the two
triangles gives the symmetric statement. QED

## Scope

This eliminates the entire three-cut case of `G-v-B` under the stated
structural hypotheses. It does not yet exclude the two-triangle
neighbourhood or establish the requested global colouring theorem.
All expansions, port movements and final unions occur in `G`; no
virtual torso edge is used for branch-set connectivity.
