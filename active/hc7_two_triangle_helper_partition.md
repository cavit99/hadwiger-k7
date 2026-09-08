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

## A coupled colouring and deletion response

**Proposition.** In addition to the preceding theorem's hypotheses, suppose
`chi(G)=7` and every proper minor of `G` is six-colourable. Put
`q=e(G)-4|G|>=0`. After possibly interchanging `x,y`, one can choose
`a0 in A` nonadjacent to `x` such that

`d(x)+d(a0)<=q+16`.

The same choice supplies all the following conclusions:

1. A six-colouring of `G-v` has `a0,x` in one colour and uses five or six
   colours on `A union B`.
2. The graph `F=G-{v,a0,x}` is four-connected, has at least `4|F|-10`
   edges, and contains a two-helper model rooted at `B union {y}`.
3. In a model maximizing the helper union and then minimizing its root
   bags, every one of `v,a0,x` contacts that union in the original graph.
   At least one of the other two `A` roots belongs to a helper. If the
   other is outside the union, it is its root bag's unique contact vertex
   to the helpers and is adjacent to both of them.

**Proof.** Write `e_z=d(z)-8>=0`, so `sum_z e_z=2q`. Choose `x` with
`e_x<=e_y`. Literal `K_5^-` exclusion makes `x` adjacent to at most one
vertex of `A`. Among two nonneighbours in `A`, choose `a0` of smaller
degree, and call the other `a'`. These four comparison vertices are
distinct. Therefore

`2(e_x+e_a0)<=e_x+e_y+e_a0+e_a'<=2q`.

Contract the connected star `{v,a0,x}` and six-colour this proper minor.
Give the merged vertex colour zero and expand only to `G-v`, putting both
independent vertices `a0,x` in that colour. The other six neighbours of
`v` avoid zero and must use all five other colours: otherwise the colouring
extends to `v`. Exactly one pair among those six repeats. It cannot lie
within either remaining clique. If it involves `y`, the six vertices of
`A union B` are rainbow. Otherwise it is a cross-pair between `A-a0`
and `B`, and `A union B` uses exactly five colours. This proves (1).

Deleting three actual vertices gives four-connectivity of `F`. The only
edges within the deleted triple are `va0,vx`, so

`e(F)=e(G)-8-d(a0)-d(x)+2
     =4|F|+q+6-d(a0)-d(x)>=4|F|-10`.

For `Z=B union {y}`, at most four of the six root-root edges are present:
`B` is a triangle and `y` has at most one neighbour in it. Temporarily
complete `Z` to a clique. The resulting graph has at least `4|F|-8`
edges, remains internally four-connected at `Z`, and satisfies the
exact Norin--Totschnig Lemma 12 hypothesis recorded above. It has a
`Z`-rooted two-helper model. No added edge can be used internally by a
bag, since its ends are distinct prescribed roots in distinct bags; nor
can it realize a required helper contact, since helpers contain no root.
Deleting the added edges therefore preserves the model in `F`. This is
an inference about the returned model, not a claim that the augmented
graph is a minor of `G`.

Maximize the union `S` of the two helpers, then minimize the total root-bag
order. The port argument in the pinned spanning-helper lemma uses no
connectivity bound until its final spanning step: each root bag now has
exactly one actual vertex adjacent to `S`, and no unassigned component
contacts `S`. Write `P` for these four distinct ports. Thus `N_F(S)=P`.
Do not infer that the root bags are singleton in this four-connected host.

If some `d in {v,a0,x}` missed `S`, then `N_G(S)` would be contained in
`P union ({v,a0,x}-{d})`, of order at most six. Both `S` and the vertex
`d` survive outside this boundary, contradicting seven-connectivity.
This proves the three required contacts. The only neighbours of `v`
that can lie in `S` are the two remaining `A` vertices, so one lies there.
If the other is outside, their literal edge prevents it from being in
an unassigned component. In its root bag it is adjacent to `S`, and is
therefore that bag's unique port. Both helpers must contact that port.
All root and helper bags are disjoint subsets of the original deletion;
no colouring preservation of the returned model is asserted. QED

## The five-colour triangle state

**Proposition.** Retain the preceding critical-host hypotheses. If no
six-colouring of `G-v` makes `A union B` rainbow, the same response can
be labelled so that `a0,x` have colour zero, `a1,b0` share colour `alpha`,
and `a2,b1,b2,y` have the four distinct other colours
`gamma,delta,epsilon,zeta`. There is a connected `alpha,zeta` component
`C` containing `a1,b0,y`. It avoids the five roots

`R={a0,a2,b1,b2,x}`

and contacts each of them. Outside `C` and the whole colour-zero class
there is a rooted triangle at `a2,b1,b2`, with `b1,b2` singleton.

**Proof.** The preceding proposition supplies precisely the stated
five-colour alternative. If `a1,b0` were in different `alpha,zeta`
components, swap one component's colours. This introduces `zeta` on
`A union B` while retaining `alpha` at the other root, making its six
vertices rainbow, a contradiction. Their common component must also
contain `y`. Otherwise swapping it removes `alpha` from `N(v)`, permitting
that colour on `v` and contradicting `chi(G)=7`.

The component `C` avoids `R` by its two colours. Its contacts to `R`
are the actual edges from `a1` to `a0,a2`, from `b0` to `b1,b2`, and
from `y` to `x`. The singleton roots `a2,b1,b2` are pairwise bichromatically
connected: separating the two singleton occurrences would permit a Kempe
swap removing one colour from `N(v)`. Choose paths from `a2` to `b1`
and `b2` in their respective two colours. Their union with `b1,b2`
removed is a connected `a2` bag, disjoint from those two roots. It avoids
`C` and colour zero. The literal edge `b1b2` completes the rooted triangle.
No paths from different colourings are combined. QED

A rooted wheel on the five roots `R`, disjoint from `C`, would finish:
both `C` and `{v}` are adjacent and full to all five bags. The two bags
containing `a0,x` would need their mutual contact as well if each only
contacts two of the other three bags. Their roots are nonadjacent and
have the same colour, so this contact is not automatic. The six-colour
triangle alternative is also unclosed. In particular, no inference here
identifies `C` with one of the structurally returned helpers or reserves
the same vertices in both constructions.
