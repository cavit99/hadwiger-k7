# A matching quotient and coupled colourings in the two-triangle case

**Status:** written deductions; separate internal audit at the source hash
recorded beside this file.
The whole two-triangle case, Conjecture 19 and HC7 remain open.

All graphs are finite and simple; set neighbourhoods are external.
Let `Q=K_7-2K_2`, with independent deleted edges. Assume that `G` is
seven-connected, has minimum degree at least eight and chromatic number
seven, has no `Q` minor, and every proper minor is six-colourable. Let
`d(v)=8` and `N(v)=A dotcup B dotcup {x,y}`, where `A,B` are triangles
and `xy` is an edge. Additional neighbourhood edges are allowed.

We use [contraction closure, Corollaries 3 and 6](hc7_companion_contraction_closure.md),
source SHA-256 `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`,
with [audit](hc7_companion_contraction_closure_audit.md) SHA-256
`26b2f5ad7226c7bb3f194cac8523f043d7ae6ca955036249f04ddc9fb6d94394`.
We also use the [two-triangle exterior theorem](../results/hc7_degree8_two_triangle_exterior.md),
source SHA-256 `e51564c9ffd857d15eb3d1de9c5cfa4ce9b9bfac514ac3188ac5379e2a745776`,
with [audit](../results/hc7_degree8_two_triangle_exterior_audit.md) SHA-256
`5ff953f5f2b019fee85fb810af8619bae929f8dbd12559ccb01a6f4b1fbeb50d`.
Thus `W=G-N[v]` is nonempty, connected and contacts every vertex of `N(v)`.

## 1. The actual matching quotient

**Theorem 1.** Label `A={a,a1,a2}` and `B={b,b1,b2}` so that
`a1,a2,b1,b2` are anticomplete to `{x,y}`. Set

`M={a1a2,b1b2,xy}`, `H=G/M`, and `F=H-v`.

Write `p,q,z` for the three contracted vertices, respectively, and
`S={p,q,z,a,b}`. Then:

1. `chi(H)=6`, `N_H(v)=S`, and `F` is four-connected and `Q`-minor-free.
2. Every vertex of `W` has degree at least seven in `F`;
   `d_F(p),d_F(q),d_F(z)>=6` and `d_F(a),d_F(b)>=5`.
3. Either `chi(F)=6`, or `chi(F)=5` and every five-colouring of `F`
   assigns distinct colours to all five vertices of `S`.
4. If `emptyset != X subseteq W` and `|N_F(X)|=4`, then
   `N_F(X)={p,q,z,t}` for some `t in W-X`. Moreover
   `N_G(X)={a1,a2,b1,b2,x,y,t}` exactly.

**Proof.** The labels can be chosen as asserted. Indeed, contracting
`xy` and retaining the four-clique `{v} union A` shows that `x,y`
collectively contact at most one A vertex; otherwise the quotient has
a literal `K_5^-`. The same holds for B. There is also at most one
A--B edge: contracting B excludes two distinct A endpoints, and
contracting A excludes two distinct B endpoints, by the same literal
exclusion. Two distinct cross-edges would violate one of these statements.

Consequently the six endpoints of `M` induce either `3K_2` or
`P_4 disjoint-union K_2`. In particular there is an independent set
`T` choosing exactly one endpoint of each edge of `M`: take a part
of a bipartition of that induced graph, choosing the isolated edge's
orientation arbitrarily. The possible cross-edge need not be absent.

The proper minor `H` is six-colourable. If it were five-colourable,
expand each contracted pair in its assigned colour, and then give all
vertices of `T` a new sixth colour. Their independence makes this
proper on `G`; all other incident edges were represented in `H`.
Keep v's old colour, which differs from the colours of all its other
neighbours in `H` and from the new colour. This contradicts `chi(G)=7`.
Thus `chi(H)=6`, and the displayed five vertices are precisely its
neighbours of v.

If `C` is a cut of `F` of order at most three, expand each pair vertex
of `C` to its two endpoints and adjoin v. This would separate `G`.
Its order is `|C|+k+1`, where `k` is the number of pair vertices in `C`.
It is at most six unless `C={p,q,z}`. In that sole exception,
`F-C=G[W union {a,b}]` is connected, by the exterior theorem.
Hence no such cut exists. The fixed pair preimages also lift any
minor of `F` to `G`, so `F` is `Q`-minor-free.

A vertex of W seeing both `a1,a2` has no other contact in `N(v)`:
Corollary 3 applied to `{v} union A` forbids all contacts outside A,
and a third A contact would give a literal `K_5^-`. Symmetrically
for `b1,b2`. Thus no W vertex loses a neighbour at two different
contractions in M. Deleting v loses none of its neighbours, giving
degree at least seven in F. The union of the outside neighbours of
each contracted pair has size at least seven before deleting v.
The other pair contractions cause no loss at its merged vertex:
the selected A/B vertices avoid x,y and there is at most one A--B edge.
This gives the lower bound six at p,q,z. The vertex a loses v and
one neighbour at `a1a2`, and possibly one at `xy`; it cannot lose one
at `b1b2`. Hence its degree is at least five; likewise for b.

Adding v increases chromatic number by at most one, so `5<=chi(F)<=6`.
If a five-colouring of F used at most four colours on S, it would
extend to v with a missing fifth colour, contradicting `chi(H)=6`.
This proves (3).

Finally, for X as in (4), v is not an original neighbour of X.
Expanding its four F-neighbours gives at most `4+k` original neighbours,
where `k<=3` counts paired neighbours. Seven-connectivity, with v
surviving outside this boundary, forces `k=3` and equality throughout.
All six pair endpoints and the fourth neighbour t are therefore actual
neighbours of X in G. If t were a or b, connectedness of W would
force `X=W`, contradicting its contact with the other root. Thus
`t in W-X`, proving (4). QED

## 2. All complementary actual-root schemes from one colouring

**Theorem 2.** In the `chi(F)=5` branch, fix any five-colouring f of F
and expand its pair vertices, obtaining one fixed five-colouring of
`G-v-M`. For every independent transversal T of M, the five actual
vertices `R_T=N(v)-T` have a properly endpoint-coloured `K_5` scheme
in `G-v-T`. In fact `chi(G-v-T)=5`, and every five-colouring of that
graph makes `R_T` rainbow and supplies such a scheme. The restrictions
of f give a simultaneous choice of colourings for all T, but the ten
paths chosen for different transversals need not agree.

**Proof.** The fixed restriction gives the five-colour upper bound.
A four-colouring of `G-v-T`, a fresh fifth colour on the independent
set T and a sixth on v would colour G. Hence `chi(G-v-T)=5`.
In any five-colouring, give T a sixth colour. If `R_T` used at most
four colours, v could take a missing old colour, again colouring G.
Thus `R_T` is rainbow. Consider two of its vertices, of colours i and j.
If their bichromatic components were different, swap the component
containing the first. No T vertex participates. Colour i would then
be absent from `N(v)`, allowing v to receive i and six-colouring G.
Thus they have a simple bichromatic path in `G-v-T`.

Choose one such path for each of the ten pairs. No other prescribed
root can be internal, because all five root colours are distinct.
At any intersection of paths, the vertex's colour labels a common
endpoint of all those demand edges. These are exactly the coloured
scheme conditions, with all five actual roots retained. QED

## 3. Exact scope of the reduction

The preimages are fixed throughout: p owns `{a1,a2}`, q owns `{b1,b2}`,
z owns `{x,y}`, and every other vertex is unchanged. H has `|G|-3`
vertices and F has `|G|-4`. This decrease is not an induction:
neither quotient is asserted seven-contraction-critical or to satisfy
the original degree and connectivity hypotheses.

The generic component-parity repair criterion is already in the
[legacy parity theorem](../results/hc7_kempe_component_odd_cycle.md),
with its adjacent older audit. It is not a new theorem here and is
not used as a dependency of Theorems 1 or 2.
The `chi(F)=6` branch is unresolved. In the other branch, a `K_5`
scheme is not asserted to supply its rooted minor: the proved universal
contractibility theorem applies to bipartite targets. Even a rooted
five-clique in F would need an ownership-safe expansion of a paired
root, or another simultaneous allocation, to give Q in G. Independently
chosen complementary schemes cannot be combined through shared nonroots.
Nor has four-boundary replacement been shown to preserve the fixed
colouring extensions and paired preimages needed for a closed reduction.
