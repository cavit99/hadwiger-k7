# The exterior of a degree-eight cycle-and-triangle neighbourhood

**Status:** written proof; the adjacent audit records its separate internal
verdict at the exact source hash. This is a
restriction on a hypothetical counterexample, not a proof of Conjecture 19.
All graphs are finite and simple, and set neighbourhoods are external.

**Theorem.** Let `G` be seven-connected with minimum degree at least eight
and no `Q=K_7^=` minor. Suppose a degree-eight vertex `v` has neighbourhood
`C union A`, where `C=(0,1,2,3,4,0)` is a five-cycle, `A={r,s,t}` is a
triangle, and at most one edge joins `C` to `A`. Put `J=G-{v,r,s,t}` and
`B=G-N[v]=J-C`. Then:

1. Every vertex of `B` has at most two neighbours on `C`; if there are
   two, they are consecutive on the cycle.
2. Every component of `B` contacts all three vertices of `A`.
3. `B` is nonempty and connected, and contacts all five vertices of `C`.

We use [connected-triple contraction closure, Corollary 6](../active/hc7_companion_contraction_closure.md)
at SHA-256 `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`,
and [the five-root wheel theorem and Corollary 4](hc7_five_root_wheel.md)
at SHA-256 `f0fbab79d23d8079b91ff1a812b83db96059aa4fb0024c809b1037f3f533f62a`.
Both inputs have separate adjacent internal audits. The latter gives
four-connectivity of `J` here.

## 1. Individual cycle contacts

If `x in B` contacts nonconsecutive cycle vertices, relabel them `0,2`.
Contract the connected triple `{x,0,4}` to `z`. The vertices `z,1,2,3`
span a diamond: `z` contacts `1,2,3` through `01,x2,43`, and `12,23`
remain edges. All four are neighbours of the surviving vertex `v`.
Thus the quotient has a literal `K_5^-`, contrary to contraction closure.
Every three cycle vertices contain a nonconsecutive pair, proving part 1.
Extra contacts only strengthen this contradiction. This is a single
contraction of original vertices, with no iteration assumption.

Every cycle vertex has at most six neighbours in `N[v]`, so has a
neighbour in `B`. In particular `B` is nonempty. Four-connectivity of
`J` implies that each component of `B` has at least four distinct cycle
neighbours: otherwise its at most three neighbours on `C` separate it
from a surviving cycle vertex.

## 2. Every component contacts the triangle

Suppose a component `L` of `B` misses `t`. Let
`H=G[L union C union {r,s}]`, with these seven vertices outside `L`
as prescribed roots. Every vertex of `L` retains its original degree,
at least eight. Indeed it has no neighbour at `v,t` or in another
component of `B`. Every nonempty `X subseteq L` has at least seven
external neighbours in `H`: its neighbourhood is unchanged from `G`,
where `v` survives outside it and seven-connectivity applies.

The vertex `t` has at least five neighbours in `J`, at most one on `C`,
and none in `L`. Choose a different component `O` of `B` meeting `t`.
It contacts at least four cycle vertices. Choose two disjoint cycle
edges so that the resulting three connected cycle pieces, of orders
`2,2,1`, are all contacted by `O`. If `O` misses one cycle vertex, place
that vertex in a two-vertex piece; otherwise any such matching works.

Contract those two edges in `H`. The three cycle roots form a triangle.
Every nonroot degree drops by at most two, and every nonroot-set boundary
drops by at most two. Thus the five resulting roots and the nonroots
`L` satisfy the rooted-wheel theorem: boundary at least five and degree
at least six. Lift its rooted wheel through the two fixed, disjoint
cycle-edge preimages.

The connected bag `D=O union {t}` is disjoint from this model and `{v}`.
It contacts the `r,s` bags through `tr,ts`, and all three cycle bags
through the chosen contacts of `O`. The bag `{v}` also contacts all
five bags through their original roots, and contacts `D` through `vt`.
These seven bags give `K_2 join W_4=Q`, a contradiction. Relabelling
`r,s,t` proves part 2.

## 3. Combining components

Three components already give `K_7`. Their cycle-neighbour sets, each
of order at least four, have a common vertex `c`. Partition the cycle
into the singleton `{c}` and the two consecutive two-vertex paths left
after deleting `c`. Assign a different component to each piece. Every
component meets its assigned piece. The three resulting connected,
disjoint bags form a triangle through the cycle edges and are all full
to the literal four-clique `{v,r,s,t}`, giving `K_7`. Thus there are at
most two components.

Suppose there are exactly two, `L,O`, and `L` misses a cycle vertex `a`.
Choose distinct `b,c` among their common cycle neighbours; there are at
least three choices. Consider `F=G[L union {b,c,r,s,t}]`. Part 1 implies
that each nonroot loses at most two neighbours, so has degree at least
six. For nonempty `X subseteq L`, its original boundary differs from
its boundary in `F` only at the three omitted cycle vertices. One of
those, `a`, has no `L` contact. Consequently a boundary of order at
most four in `F` would yield an actual boundary of order at most six
in `G`, with `v` surviving outside. The rooted-wheel theorem applies.

Choose `d in N_C(O)-{b,c}` and put `D=O union {d}`. This connected bag
avoids `F` and is full to its five rooted bags: part 2 supplies the
triangle contacts, and `O` contacts `b,c`. It contacts `{v}` through
`d`, while `v` contacts every rooted wheel bag. Again this gives `Q`.
Hence in a two-component case both components contact all of `C`.

Now `{r} union L`, `{s} union O`, and `{v,t}` are three disjoint
connected pairwise adjacent bags, each full to `C`. Contract any cycle
edge to turn `C` into a four-cycle. The resulting seven bags give
`K_3 join C_4=Q`, the final contradiction. Thus `B` is connected;
the earlier degree observation shows that it contacts every cycle
vertex. All constructions use disjoint components and specified root
preimages, so no branch-set ownership is reused. QED

**Corollary.** The induced graph `G[B]` has minimum degree at least five.

**Proof.** Corollary 3 of the same contraction-closure input says every
vertex outside the four-clique `{v,r,s,t}` has at most two neighbours
in it. It also forbids an edge from a cycle vertex to a vertex with
two neighbours in `A`, since every cycle vertex neighbours `v`.
Thus a vertex of `B` meeting `C` has at most one `A` neighbour and at
most two `C` neighbours. A vertex of `B` missing `C` has at most two
`A` neighbours. Every vertex of `B` therefore loses at most three
neighbours on deleting `N[v]`, proving the corollary. QED

**Cutvertex corollary.** If `q` is a cutvertex of `G[B]`, every component
of `G[B]-q` contacts at least two vertices of `A`.

**Proof.** Suppose a component `L` meets at most one triangle root. Its
boundary lies in `{q} union C union N_A(L)`, so seven-connectivity forces
`N_A(L)={r}` and `N_C(L)=C`. Put `K=B-L`, which is connected, and let
`M=C-N_C(K)`. If `|M|>=2`, the set `L union M` has boundary contained
in `{q,r,v} union (C-M)`, together with at most one additional triangle
root, from the possible cross-edge. The other triangle root survives
outside this boundary. Seven-connectivity gives `8-|M|+epsilon>=7`,
where `epsilon<=1` counts the additional root. Thus `|M|<=2`; equality
requires a cross-edge from `M` to some `a in {s,t}`. Choose this `a` in
the equality case, and either of `s,t` otherwise; write `b` for the other.

The root `a` has a neighbour in `K`: its degree is at least eight, it
has at most four neighbours in `N[v]`, and it misses `L`. Consequently
`L union {r}`, `K union {a}` and `{v,b}` are three disjoint connected
pairwise adjacent bags. The first and third contact every cycle vertex.
The second contacts at least four, using the cross-edge if `|M|=2`.
Contract a cycle edge covering its possible missed vertex. The four
cycle bags and the three displayed bags give `K_3 join C_4=Q`, a
contradiction. This proves the corollary with all ownership explicit. QED

The remaining construction must work inside this single connected
exterior with all eight boundary contacts. Connectedness and these
contacts alone do not yet provide the three compatible helper bags.
