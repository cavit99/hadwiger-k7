# Five prescribed roots containing a triangle give an almost-clique

**Status:** written proof; the adjacent audit records its separate internal
verdict at the exact source hash. This strengthens the rooted-wheel theorem.
No global colouring conjecture or density theorem is claimed here.
All graphs are finite and simple; neighbourhoods of sets exclude the sets.

**Theorem.** Let `S={b,c,r,s,t}` be five distinct vertices of `F`, with
`rst` a triangle and `B=V(F)-S` nonempty. Suppose every nonempty
`X subseteq B` has at least five external neighbours, and every vertex
of `B` has degree at least seven. Then `F` has five disjoint connected
bags, one containing each root, with every pair adjacent except possibly
`rb` or `rc`. At most one of those two contacts is missing. In particular,
this is an `S`-rooted `K_5^-` minor. The triangle root `r` can be designated
in advance; extra contacts are allowed.

## External input

We use [Norin–Totschnig, Theorem 8](https://arxiv.org/html/2507.03244v1#S2),
which states the Robertson–Seymour–Thomas rooted-four-model alternative
from their (2.6). The primary statement and the internal-connectivity
and trisection definitions were inspected on 7 September 2026.
For a graph `J` with four prescribed roots `Z`, at least one holds:

1. There is a `Z`-rooted `K_4` model.
2. There is an order-two trisection `(A_1,A_2,D)` such that each
   `A_i-D` contains exactly one root.
3. There is a separation `(A,D)` with `Z subseteq A`, separator order
   at most three, `|D-A|>=2` and `|Z intersect D|<=2`.
4. `J` has a plane drawing with all four roots incident with one face.

A trisection has common pairwise intersection `P`, here of order two,
and no edges between its three open parts. The model has disjoint
connected bags containing the four prescribed roots separately.

## Proof

Fix the designated root `r`. Suppose a counterexample exists and choose
one of minimum order.
The degree bound implies `|B|>=3`. Every root has a neighbour in `B`,
by applying the boundary hypothesis to `B` itself.

If a root `a` has exactly one nonroot neighbour `x`, contract `ax`,
retaining the root label `a`. For any surviving nonroot set, the old root
`a` was not a neighbour; its boundary is unchanged except that `x`, when
present, is replaced by the merged root. Every remaining nonroot degree
is unchanged for the same reason. All five roots remain distinct and the
root triangle survives. The new nonroot set is nonempty, and the strictly
smaller graph meets the theorem's hypotheses. Lifting its model through
`ax` is valid, a contradiction. Thus every root has at least two nonroot
neighbours.

We will also use the following two-root transfer. Suppose `b,c` have
exactly the same two nonroot neighbours `p,q`. Contract the disjoint
edges `bp,cq`, retaining labels `b,c`. Every surviving nonroot set has
its old boundary with `p,q` replaced by two distinct new roots: neither
old `b` nor old `c` was a neighbour of that set. Every surviving nonroot
degree is therefore unchanged. The triangle and its designated root survive, and there
is at least one remaining nonroot since `|B|>=3`. This gives a smaller
counterexample, which is impossible. The root preimages `{b,p},{c,q}`
are disjoint and connected, so the inductive conclusion lifts.

Put `J=F-r` and `Z={b,c,s,t}`. The pair `(J,Z)` is internally four-connected:
a nonempty root-free set with at most three neighbours in `J` would have
at most four in `F`. Every nonroot has degree at least six in `J`.
Apply the external four-root alternative.

**Rooted four-clique case.** In a rooted `K_4` model in `J`, regard the
`b,c` bags as adjacent helpers full to the `s,t` bags. If either helper
contacts `r` in `F`, the four clique bags together with `{r}` give all
contacts except possibly `rb` or `rc`: `r` also contacts the `s,t` bags
through its literal root edges. Thus every such model avoids this contact.

Choose a model maximizing the union `W` of its `b,c` bags, then minimizing
the total order of its `s,t` bags. Each of the latter bags has exactly one
actual vertex adjacent to `W`. If two ports existed, choose distinct ports
for the two helpers and a minimal tree joining them to the prescribed root.
A nonroot port is a leaf. Moving it into its adjacent helper retains the
other helper contact and supplies the first through the old tree edge,
while enlarging `W`. The literal edge `st` preserves the contact between
the two root bags during this operation, a contradiction.

No component outside the model contacts `W`, since it could be absorbed.
Hence `N_J(W)` consists of at most two actual ports, one in each other bag.
As `r` misses `W`, the nonroot set `W-{b,c}` has at most four neighbours
in `F`. It must be empty. The `b,c` bags are therefore singleton roots,
each adjacent to both ports and to no other nonroot. The normalization
forces both ports to be nonroots. The two-root transfer contradicts
minimality.

**Trisection case.** Write `P=A_1 intersect A_2 intersect D`. Each
`A_i-P` is exactly its one prescribed root: otherwise its nonroots have
boundary contained in `P` and that root, contradicting internal four-
connectivity. All nonroots lie in `D`. Since `|B|>=3`, the set `B-P` is
nonempty. Its neighbourhood in `J` lies in `P union (Z intersect D)`.
If `P` contained a root, this union would have order at most three,
because `Z intersect D` consists of the two nonisolated roots. Therefore
both ports are nonroots. The edge `st` prevents either `s` or `t` from
being an isolated open root, so the two open roots are `b,c`. Each has
at least two nonroot neighbours, all in `P`; both are adjacent to both
ports. Apply the two-root transfer again.

**Small rooted separation.** Outcome 3 contradicts internal four-
connectivity directly.

**Planar case.** The graph `J` is connected: a component containing
nonroots must contain all four roots, by applying the boundary condition
to its nonroots. Every root has a nonroot neighbour, so there is no
component consisting only of roots. In a drawing
with the four roots on one face, that face has boundary length at least
four, so Euler's formula gives `e(J)<=3|J|-7`.
On the other hand, the nonroots have degree at least six, `b,c` each
have at least two nonroot neighbours, and `s,t` each have at least two
nonroot neighbours in addition to their mutual edge. Consequently

`2e(J)>=6|B|+2+2+3+3=6|J|-14`.

Equality is forced throughout. In particular, `b,c` have degree two,
and the distinguished face has boundary length exactly four, with its
four distinct vertices exactly `Z`. Each of `b,c` therefore has two root
neighbours as well as its two nonroot neighbours, a contradiction.

All alternatives are excluded. The only reductions strictly decrease
`|B|`; they preserve every nonroot boundary inequality, nonroot degree,
prescribed root and root-triangle edge. Expanding connected contraction
preimages preserves all contacts in the returned model. QED

## Scope

The theorem guarantees nine contacts on five prescribed bags and controls
the triangle endpoint of the possible missing pair. It does not
supply a disjoint sixth helper full to those bags, establish the proposed
five-root density bound, or prove Conjectures 19/21 or HC7. The version
with nonroot minimum degree six and an unrestricted location of the
missing pair remains unproved here.

## Extension with at most five degree-six nonroots

**Theorem.** Retain the five roots, literal triangle, nonempty nonroot set
and boundary hypothesis of the theorem above. Suppose every nonroot has
degree at least six, and at most five nonroots have degree exactly six.
Then the same designated-`r` conclusion holds: the five rooted bags have
every contact except possibly one of `rb,rc`.

**Proof.** Choose a counterexample minimizing `|B|`. The degree bound
implies `|B|>=2`. If `|B|=2`, both nonroots are universal in the seven-vertex
graph. Add one to each of the `b,c` bags and keep `r,s,t` singleton. These
five bags form a rooted `K_5`, so a counterexample has `|B|>=3`.

The one-root absorption and simultaneous two-root transfer in the first
proof preserve every surviving nonroot degree exactly. They consequently
preserve the new degree bounds and cannot increase the number of degree-six
nonroots. Both strictly decrease `|B|`, preserve the five named roots and
the designated triangle, and lift through disjoint connected preimages.
A reduced graph with just one nonroot cannot arise: preservation would
give that vertex degree at least six in a graph of order six. Thus the
same reductions and the two-nonroot base apply. Normalize so that every
root has at least two nonroot neighbours.

Again put `J=F-r` and `Z={b,c,s,t}`. The boundary condition in `J` is
unchanged: every nonempty subset of `B` has at least four neighbours.
Each nonroot has degree at least six in `J`, except that at most five
may have degree five. The rooted four-clique, trisection and small
separation arguments in the first proof use only this boundary condition,
`|B|>=3`, and the normalized root neighbours. Their port arguments and
root transfers therefore apply without change. It remains to exclude
the cofacial planar alternative using the weaker degree sum.

The normalized graph `J` is two-connected. Indeed, after deleting at
most one vertex `z`, every component contains a nonroot: otherwise a
root in that component would have at most one nonroot neighbour in `J`,
contrary to normalization. If a component `C` has nonroot set `X`, then
`N_J(X)` is contained in `(C intersect Z) union {z}`. The boundary
condition forces `C` to contain at least three of the four roots.
There cannot be two such components. The same argument with no deleted
vertex proves connectivity.

In a cofacial drawing, the distinguished face boundary is therefore a
cycle containing the four roots and `h>=0` nonroots. Euler's formula gives

`2e(J)<=6|B|+10-2h`.

The sum of the nonroot degrees is at least `6|B|-5`. The roots have at
least eight incidences with nonroots. The facial cycle has eight
incidences at roots, of which at most `2h` join a nonroot; hence it supplies
at least `8-2h` root-root incidences. The literal edge `st` supplies two
root-root incidences in any event. Consequently the root degree sum is
at least `8+max(2,8-2h)`. Comparing the two degree sums with the planar
upper bound gives

`0 >= max(2h,6)-5 >= 1`,

a contradiction. This excludes the last alternative and proves the
extension. It supplies the same five bags; it does not supply a sixth
helper or any global colouring conclusion. QED
