# Rooted helpers for the companion six-colouring conjecture

**Status:** written proofs. The adjacent audit records its independent
internal verdict at an exact source hash. The remaining simultaneous
construction is a conjectural target; Conjecture 19 is not proved.

All graphs are finite and simple. Write `K_7^=` for `K_7` with two
independent edges deleted, and `K_t^-` for `K_t` with one edge deleted.
A `Z`-rooted two-helper model has four connected disjoint root bags,
one containing each vertex of `Z`, and two further connected disjoint
bags `U,V`. Each helper contacts every root bag, and `U,V` contact each
other. Root-root contacts are not part of this definition.

## 1. Audited input and the missing-edge extension

We use [the rooted-helper closure](../results/hc7_k7minus_degree7_rooted_helper_closure.md)
at SHA-256
`6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67`,
whose [adjacent audit](../results/hc7_k7minus_degree7_rooted_helper_closure_audit.md)
pins that revision. It records Norin--Totschnig, Lemma 12, in this exact
form: if `(F,Z)` is internally four-connected, `|Z|=4`, and
`e(F)>=4|V(F)|-9`, then a `Z`-rooted two-helper model exists. Its Lemma 1
places an additional specified vertex `x` in a helper when
`(F,Z union {x})` is internally five-connected.

**Theorem 1.** Let `G` be six-connected of order `n`, let `d_G(v)=d>=5`,
and suppose `G[N(v)]` contains a `K_4^-` subgraph. If
`e(G)>=4n+d-13`, then `G` contains a `K_7^=` minor.

**Proof.** Choose the four vertices `Z` of that subgraph and any
`x in N(v)-Z`. The graph `F=G-v` is five-connected, and
`e(F)>=4|V(F)|-9`. The two audited inputs therefore give four root bags
and adjacent helpers, one of which contains `x`. Add the singleton bag
`{v}`. The only possibly missing contacts are the missing root-root edge
of `K_4^-` and the edge from `{v}` to the helper not containing `x`.
These pairs have disjoint ends. Every literal root edge survives because
its ends remain in their prescribed bags. This gives the required minor.
All constructions take place in `G`; no quotient connectivity is asserted.
QED

**Corollary 2.** Suppose `G` is seven-connected, `chi(G)=7`, every proper
minor of `G` is six-colourable, and `G` has no `K_7^=` minor. Then `G`
contains no `K_5^-` subgraph. In particular every neighbourhood contains
no `K_4^-` subgraph.

**Proof.** Absence of `K_7^=` implies absence of `K_7^-`. Corollary 3 of
the audited input therefore gives `delta(G)>=8` and `e(G)>=4n`.
Put `q=e(G)-4n>=0`. If a five-set spans `K_5^-`, each of its three
vertices incident to all four others has a `K_4^-` in its neighbourhood.
The contrapositive of Theorem 1 gives `d(w)>=q+14` at each such vertex.
Their contributions to `sum_w(d(w)-8)=2q` are at least `3(q+6)>2q`,
while every other contribution is nonnegative. This contradiction proves
the assertion. A `K_4^-` in `N(v)` together with `v` is `K_5^-`. QED

For a degree-eight vertex in this corollary, `alpha(G[N(v)])<=3` as well:
an independent four-set could be contracted with `v` as a star, and a
six-colouring of that proper minor would expand to a six-colouring of
`G`, since the other four neighbours together with that set use at most
five colours. Thus the surviving order-eight neighbourhood is
diamond-free in the subgraph sense, not merely induced-diamond-free.

## 2. In five-connectivity the helpers can span the nonroots

**Lemma 3.** Let `F` be five-connected and let `|Z|=4`. If a `Z`-rooted
two-helper model exists, there is one whose root bags are the four
singletons `Z` and whose helpers partition `V(F)-Z`.

**Proof.** Maximize `|U union V|`, and subject to this minimize the total
order of the four root bags. These are finite optimizations in the fixed
host. In a root bag `R_i`, the set `P_i` of vertices adjacent to a helper
has exactly one member. Indeed, if it had two, choose distinct ends
`a,b` contacting `U,V`, respectively. A minimal tree connecting its root,
`a,b` spans the root bag by the secondary optimization. One of `a,b` is
a leaf different from the root. Move that leaf into the helper it meets.
The old tree edge preserves that helper's contact with the remaining
root bag, and the other chosen end preserves the other contact. This
strictly increases the helper union, a contradiction.

No component outside all six bags contacts a helper, since it could be
absorbed into that helper. Consequently the external neighbourhood of
`U union V` is contained in the four vertices in the sets `P_i`.
If its complement had more than four vertices, deleting these at most
four neighbours would separate a remaining outside vertex from the
nonempty helper union, contradicting five-connectivity. The complement
already contains the four prescribed roots. It is therefore exactly `Z`,
and each root bag is its singleton root. QED

## 3. The exact remaining support allocation

**Proposition 4.** Let `G` be seven-connected, let `d(v)=8`, and let
`Z subseteq N(v)` span a four-cycle. Put `F=G-v`,
`J=F-Z`, and `S=N(v)-Z`. Suppose there is a two-helper model rooted at
`Z`. If it can be chosen with each helper intersecting `S`, then `G` contains
a `K_7^=` minor. This conclusion also holds if `S` contains an edge `ab`
and `Z subseteq N(a) union N(b)`.

**Proof.** In the first case `{v}`, `U,V` form three mutually adjacent
bags, each adjacent to all four root bags. The literal cycle edges give
`K_3 join C_4=K_7^=`.

For the second case use Lemma 3. If both spanning helpers intersect `S`, apply
the first case. Otherwise interchange them so `S subseteq U`. Let `W`
be the component of `J-{a,b}` containing `V`. It contains all the old
`V` contacts with the four roots. If `W` were disjoint from `S`, deleting the six
actual vertices `Z union {a,b}` in `G` would separate `W` from `v`:
its only possible neighbour outside its component, besides those six
vertices, is `v`, which has no neighbour in `W`. This contradicts
seven-connectivity. Hence `W` intersects `S`. The connected set `{a,b}` also
intersects `S` and contacts all four roots by hypothesis. It has an edge to
`W`, since `J` is connected and `W` is a component after deleting only
`a,b`. Thus `{a,b}`, `W` are disjoint adjacent helpers, both intersecting `S`.
The first construction applies. QED

In the critical host of Corollary 2, the density hypothesis supplying the
model in Proposition 4 holds: `e(G-v)>=4n-8=4|V(F)|-4`. The unresolved
case is a connected bipartition `J=U dotcup V` with each side contacting
all four roots but all four vertices of `S` in one side. Here `J` is
two-connected, `G-Z` is three-connected, vertices of `J-S` have degree
at least four in `J`, and vertices of `S` have degree at least three there.
No theorem yet redistributes these supports while retaining all eight
root-helper contacts and connected, disjoint helpers. Nor has every
surviving degree-eight neighbourhood been shown to contain a four-cycle.
The results above do not close that case or the global conjecture.
