# A full-helper partition in the two-triangle case

**Status:** written proof; a separate internal audit is recorded in the adjacent audit. The final
two-region allocation below is unproved. No global colouring conclusion is claimed.
All graphs are finite and simple; write `Q=K_7` with two independent edges deleted.

**Theorem.** Let `G` be seven-connected, `delta(G)>=8`, and `Q`-minor-free.
Suppose `d(v)=8` and `N(v)=A dotcup B dotcup {x,y}`, where `A,B` are
triangles and `xy` is an edge. Additional edges are allowed. Put
`H=G-v-B`. Then `H` is three-connected, `delta(H)>=6`, and it has a
connected partition `V(H)=U dotcup Y` such that both parts contact every
vertex of `B`, exactly two vertices of `A` belong to `U`, and the third
vertex of `A` and `x` belong to `Y`.

## Inputs and initial helpers

We use [contraction closure, Corollary 3](hc7_companion_contraction_closure.md),
SHA-256 `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`:
every vertex outside the literal four-clique `{v} union B` has at most
two neighbours in that clique. Thus `delta(H)>=6`; deleting its four
vertices from the seven-connected host also gives three-connectivity.

The [rooted-helper input and singleton normalization](hc7_companion_helper_construction.md),
SHA-256 `0c1ac8052f7734d8d0267381c030e177bd70010eded63d15fdca8c0db6d1f375`,
record Norin--Totschnig, Lemma 12, and the written normalization in Lemma 3.
Both sources have adjacent audits pinned to these revisions. The exact external
input is: internal four-connectivity at four roots and `e(F)>=4|F|-9`
give two adjacent connected helpers, each contacting all four root bags.
In a five-connected host the root bags can be singletons and the helpers
can partition their complement. No fresh primary-source inspection is asserted here.

Put `F=G-v` and take roots `B union {x}`. Since `delta(G)>=8`,
`e(F)>=4|G|-8=4|F|-4`; `F` is six-connected. The input therefore gives
connected parts `P,R` partitioning `H-x`, each contacting `x` and every
vertex of `B`. If `A` is split between them, adjoin `x` to the part
containing exactly one `A` vertex. The other part is `U`, and the enlarged
part is `Y`, as required.

## The global donation reduction

Otherwise interchange the parts so that `A subseteq P`, and put `Y=R+x`.
There are three paths, one from each vertex of `A` to `Y`, disjoint outside
`Y`; endpoints in `Y` may coincide. To see this, give vertices of `P`
capacity one, vertices of `Y` capacity greater than three, and the three
source arcs capacity one. A cut of capacity at most two removes at most
two vertices or source roots of `P`. An `A` root and all of `Y` survive
and remain connected by three-connectivity of `H`. Thus a flow of value
three exists. Every source root is saturated, so no other `A` root occurs
internally. Stop each path at its first vertex of `Y`.

The three disjoint path portions in connected `P` extend to a connected
partition `P=P_0 dotcup P_1 dotcup P_2`: repeatedly attach an unassigned
vertex adjacent to an assigned part. Each `P_i` contains its own `A` root
and contacts `Y`. The three parts are pairwise adjacent through the literal
triangle `A`.

If the contact graph between these parts and `B` has a perfect matching,
the six corresponding bags contain two triangles and their matching.
The bags `Y` and `{v}` are adjacent and full to all six: use `x in Y`
for their mutual contact. Contract one matching edge. Its bag is universal
to the other four core bags, which form a four-cycle using the two remaining
matching edges and the two within-triangle edges. These five core bags form
`W_4`; adding the two full adjacent bags gives `K_2 join W_4=Q`, a contradiction.

Call `b in B` private to `P_i` if `P_i` contacts `b` and the other two
parts do not. If all three parts had private roots, those roots would be
distinct and give a perfect matching. Hence some `P_i` has no private root.
Adjoin that entire part to `Y`. It is connected to `Y`; the other two parts
remain connected through their `A` edge and still contact every vertex of
`B`. This proves the theorem. All operations are partitions, unions or
specified disjoint contractions in the fixed host; no induction on a
quotient or preservation of quotient criticality is invoked. QED

## Exact remaining completion

For such a partition, suppose `U=U_1 dotcup U_2` is a connected partition
separating its two `A` roots, each part contacts at least two roots of `B`,
and their combined contacts cover `B`. The parts are adjacent through
their `A` edge. With the singleton triangle `B` they form a rooted `W_4`:
the possible two cross omissions have different ends on both sides.
Both `Y` and `{v}` are adjacent and full to these five bags, so they give
`Q`. The same conclusion applies after any simultaneous reselection that
retains these explicit disjoint bags and contacts.

Maximizing `Y` subject to the theorem does not yet prove this split exists.
A component of `U-w` containing neither retained `A` root may own a private
`B` contact. Absorbing it into `Y` can destroy the required fullness of `U`,
even when it contacts `Y`. Thus a cutvertex of `U` is not an actual cutvertex
of `H`. A compatible reverse transfer from `Y`, or another complete
construction, remains required; no decreasing exchange has been proved.
