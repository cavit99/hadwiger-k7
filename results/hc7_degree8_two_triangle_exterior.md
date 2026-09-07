# The exterior of a degree-eight two-triangle neighbourhood

**Status:** written proof; the adjacent audit records its separate internal
verdict at the exact source hash. These are
structural restrictions, not a proof of Conjecture 19 or HC7.
Graphs are finite and simple; set neighbourhoods are external.

**Theorem.** Let `G` be seven-connected, with minimum degree at least
eight and no `Q=K_7^=` minor. Suppose `d(v)=8` and `N(v)` contains
disjoint triangles `A={a0,a1,a2}`, `B={b0,b1,b2}` and the edge `xy`.
These are spanning subgraphs; all additional edges are allowed.
Then `W=G-N[v]` is nonempty and connected and contacts all eight
vertices of `N(v)`.

## Inputs and a degree-free wheel

We use the separately audited
[contraction closure, Theorem 1 and Corollary 3](../active/hc7_companion_contraction_closure.md),
SHA-256 `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`.
In particular `G` has no literal `K_5^-`; a vertex outside `N[v]`
has at most two contacts to either triangle, and two contacts to `A`
forbid every further contact in `N(v)-A`, symmetrically for `B`.
The latter is Corollary 3 applied to the literal four-clique `{v} union A`.

We also use the [five-root almost-clique theorem](hc7_five_root_almost_clique.md),
SHA-256 `de183e350c412739c05a744e811304454ba90856efee9e097813c70617bba9cd`:
internal five-connectivity, a prescribed triangle and nonroot minimum
degree seven give five rooted bags with at most one missing contact,
incident with a triangle root designated in advance. Its adjacent audit
records the separate internal verdict. Only its degree-seven version is used here.

**Lemma 1.** Let `S={b,c,r,s,t}` be five roots of `F`, with `rst` a
triangle and at least two nonroots. If every nonempty nonroot set has
at least five external neighbours, then `F` has the rooted wheel of
[the five-root wheel theorem](hc7_five_root_wheel.md),
SHA-256 `f0fbab79d23d8079b91ff1a812b83db96059aa4fb0024c809b1037f3f533f62a`.
No separate degree hypothesis is needed.

**Proof.** While at least three nonroots remain, use that theorem's
root-preserving reduction whenever a triangle root has only one neighbour
outside the triangle. That neighbour is a nonroot. Absorbing it preserves
every surviving nonroot-set boundary exactly, all five roots and the
root triangle; nonroot order strictly decreases. If the reduction stops
above order two, every triangle root has at least two outside neighbours.
The original proof that `(F-{r,s,t})+bc` is two-connected, its connected-
prefix ordering, and its first-prefix construction now apply unchanged;
none of those steps uses a degree assumption.

It remains to handle two nonroots `p,q`. Each has degree at least five.
If they are nonadjacent, each sees all five roots. Assign one to each
of the `b,c` bags; their root contacts give adjacency and full triangle
contacts. If they are adjacent, each sees at least four roots and their
combined root neighbours cover all five. They therefore cannot both
miss the same root. Assign them to different roots `b,c` with both
attachment edges present; failure of both assignments would mean both
miss `b` or both miss `c`. Each enlarged bag sees at least two triangle
roots, their combined contacts cover the triangle, and `pq` joins them.
This is the required rooted wheel. Reverse the fixed root contractions
to lift it, preserving disjointness and all five roots. QED

## Every component contacts all eight roots

Every component of `W` has at least seven distinct neighbours in `N(v)`,
by seven-connectivity, with `v` surviving outside its boundary.
Every vertex of either triangle has at most six neighbours in `N[v]`:
it has at most one neighbour in the other triangle, since two give a
diamond in `N(v)` and hence a literal `K_5^-` with `v`. Each of `x,y`
has at most four neighbours in `N[v]`. Thus all eight roots have a
neighbour in `W`, which is nonempty.

Suppose a component `L` misses `a0`. The side
`H=G[L union (A-{a0}) union B union {x,y}]` retains every neighbour of
each vertex of `L`. Its nonroot degrees are at least eight, and each
nonempty subset of `L` has boundary at least seven. Contract `a1a2`
and `xy`. A nonroot loses at most one neighbour: seeing both `a1,a2`
forbids any contact to `x,y`, by the input above. Nonroot boundaries
drop by at most two. The five roots, consisting of triangle `B` and
the two contracted pairs, satisfy the almost-clique theorem.

Choose a different component `O` meeting `a0`, which exists by the
preceding degree observation. The connected bag `D=O union {a0}` is
disjoint from this side and contacts the two paired roots. Among the
three `B` roots it can miss at most one, since `O` sees at least seven
of the original eight roots. Designate a different `B` root for the
almost-clique theorem before applying it. Its possible missing pair
and the possible missing pair from `D` have disjoint ends. The vertex
`v` contacts all five rooted bags and `D`, giving `Q`.

The same argument excludes missing a root of `B`. If `L` instead
misses `x`, retain `L union A union B union {y}` and contract the
triangle `A` to one root. A nonroot has at most two `A` neighbours,
so loses at most one neighbour; boundaries drop by at most two.
Apply the almost-clique theorem to triangle `B` and the two other
roots. Choose `O` meeting `x`. Now `D=O union {x}` contacts the
contracted `A` root and the `y` root, using `xy` for the latter.
It can miss only one `B` root; designate another and finish as before.
Interchange `x,y` for the remaining case. Every component is therefore
full to all eight roots. The contractions have fixed disjoint root
preimages, and all choices of `O` precede the model application.

## Converting all actual boundary ports simultaneously

Suppose there are distinct full components `L,O`. We first exclude any
nonempty `X subseteq L` with `|N_G(X)|=7`. Put

`Z=N_G(X) intersect N(v)`, `P=N_G(X) intersect L`, `M=N(v)-Z`.

If `|Z|=m`, then `|P|=p=7-m` and `|M|=p+1`. In
`K=G[(L-X) union M]` there are `p` vertex-disjoint paths from all
vertices of `P` to distinct vertices of `M`. For otherwise the
vertex-path separator alternative gives a set `C` of order less
than `p` separating `P` from `M`. Let `Y` be the vertices reachable
from `P-C` in `K-C`. It avoids `M-C` and lies in `L-X`. Every actual
exit from `X union Y` lies in `Z union C`: the ports outside `C`
are reachable, no new missing root is reached, and `L` has no edge
to another component or to `v`. This is a boundary of order at most
six, with `v` surviving outside, a contradiction. The case `p=0`
uses no paths.

Stop each path at its first vertex of `M` and contract it to that
root. No path uses a vertex of `Z`, another port, or another `M` root
internally. Its only vertex adjacent to `X` is its own port: any
other such vertex would itself belong to `P`. Each old port is thus
replaced by a different previously nonadjacent root. Consequently
every subset of `X` retains exactly its old boundary cardinality.

The seven boundary labels are now distinct original neighbours of
`v`. Any seven of the eight contain a whole `A` or `B` triangle.
Keep five labels including that triangle and delete the other two
labels from this side. Every nonempty subset of `X` still has
boundary at least five. Also `|X|>=2`, since a singleton with boundary
seven would contradict the original minimum degree eight. Lemma 1
supplies a rooted wheel; expand its root preimages along the disjoint
paths to lift it.

Exactly one neighbour `h` of `v` was unused by all seven boundary
preimages. The bag `O union {h}` is connected and avoids the lifted
model. It and `{v}` contact all five bags through their actual roots
and contact each other through `vh`. This gives `Q`, a contradiction.

## Completing the multiple-component case

It follows that every nonempty subset of `L` has boundary at least
eight in `G`. Thus `F=G[L union A union {b0,b1}]` has internal
five-connectivity at its five displayed roots: only `b2,x,y` have
been deleted from any such boundary. The component `L` has at least
two vertices. A singleton full to all eight roots would give a
literal `K_5^-` on that vertex, `v` and triangle `A`.

Apply Lemma 1 in `F`. The disjoint bag `O union {b2}` and `{v}`
are adjacent and full to its five rooted wheel bags. Once again
`K_2 join W_4=Q`. Hence two components are impossible; the same
argument excludes any larger number. This proves the theorem.

The construction has no unproved minor lift: each boundary port is
assigned its own disjoint path to an unused prescribed root, and the
seventh-root omission leaves an actual neighbour for the exterior
helper. A compatible global model inside the remaining single component
is still required for Conjecture 19.
