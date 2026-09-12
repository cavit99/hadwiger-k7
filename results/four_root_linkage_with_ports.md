# Four-root linkages with additional boundary vertices

**Status:** written proofs with a [separate exact-source internal audit](four_root_linkage_with_ports_audit.md).
These are inputs to the relative three--two linkage target. They do not
prove that target, C19, HC7 or an NT-comparable theorem.

All graphs are finite and simple. Neighbourhoods are external. A prescribed
two-linkage consists of vertex-disjoint paths joining two specified pairs
of four distinct roots.

We use Norin--Totschnig, [arXiv:2507.03244v1, Theorem 13](https://arxiv.org/html/2507.03244v1).
If every nonempty nonroot subset has at least four neighbours, its
root-free separation alternative is impossible. Absence of a prescribed
two-linkage therefore gives a disc drawing with the roots in alternating
order. Delete root--root edges and add the four boundary-cycle edges
outside the disc. With d nonroots, Euler's bound is `e<=3d+1` for the
graph after deleting root--root edges. No simple original facial walk is assumed.

## 1. A degree-sum criterion

Let R be four roots, and partition the other vertices into a nonempty
set X and a set P of k vertices. Suppose every nonempty subset of X
has at least `k+4` neighbours. Write rho for the number of edges between
R and its complement. If

`sum_{x in X} d(x) + rho >= 6|X|+3k+3`,

then every prescribed two-linkage on R exists.

**Proof.** Delete root--root edges, which do not affect these hypotheses.
Fix a pairing and suppose its linkage is absent. Whenever a nonempty
connected subset Q of the remaining P vertices has at most three
neighbours, delete Q and complete its neighbourhood to a clique, again
deleting root--root edges. The number of remaining P vertices strictly
decreases, so the process terminates.

Each operation preserves absence of the linkage. At most one of two
disjoint paths can use a new edge in a clique on at most three vertices:
two such paths would require four distinct clique vertices. Replace that
path's segment from its first to its last clique vertex by a path through
the connected Q. The other path is unchanged. Reversing the operations
lifts both paths through disjoint original sets, retaining all four roots.

Count X-degrees and root-to-nonroot incidences throughout. Eliminating Q
loses at most `3|Q|` from this sum, since there are at most that many
edges from Q to its complement. Added edges cannot decrease it; newly
added root--root edges contribute nothing. If m ports remain, the sum
is therefore at least `6|X|+3m+3`. Each remaining port has degree at
least four, or its singleton would be eligible for elimination. Hence

`2e >= 6|X|+7m+3`.                                  (1)

Every nonempty nonroot set Y in the resulting graph has at least four
neighbours. If `Z=Y intersect X` is nonempty, each original neighbour
of Z outside P remains either a neighbour of Y or a vertex of Z; the
latter cannot have been a neighbour of Z. Thus the original boundary
of Z is contained in `N(Y) union P`, and `|N(Y)|>=4` follows.
If Y contains only ports, a component of Y with at most three neighbours
would contradict termination. Every component of X originally contacted
all roots and ports, by the boundary hypothesis. Its root edges remain,
so the resulting graph is connected.

The cofacial bound gives `2e<=6(|X|+m)+2`, contradicting (1). This proves
the criterion. The eliminations reduce only the finite port set; all
positive lifts use connected deleted sets with at most three boundary
vertices. No colouring or chromatic-criticality preservation is asserted.

## 2. A pair path and a disjoint arm using three ports

Let H have vertex set `X dotcup {u,v1,v2} dotcup P`, where `|P|=3`
and `|X|>=2`. Suppose every nonempty subset of X has at least six
neighbours, every X vertex has degree at least six, the X-neighbourhoods
of v1 and v2 are disjoint, and u has at least two X-neighbours.

If `|X|>=3`, there are vertex-disjoint paths consisting of a
`v1--v2` path and a `u--b` path for some `b in P`. The u-path has
all its internal vertices in X. The v-path may use vertices of
`P-{b}`, and avoids u. If `|X|=2`, then for each j and each b in P
there are disjoint connected carriers with exact six-root intersections
`{u} union (P-{b})` and `{vj,b}`, avoiding the other V root.

The permission for the v-path to use other ports is essential. The
path barrier to a pair path confined to X does not refute this statement.

### The four-root problem

Every component of H[X] is full to the six roots. If there are two
components, one supplies a v1--v2 path and another a u--b path, for
any chosen b. Thus assume X is connected. Delete all edges between
the six roots; proving the assertion in this subgraph suffices and
does not change any X degree or X-subset boundary.

Add a new vertex a adjacent precisely to P, and regard
`{u,a,v1,v2}` as four roots. Call the resulting graph G. A linkage
`u--a, v1--v2` in G gives the required paths: truncate the u--a
path at its first P vertex. The other path avoids a and that port.
Suppose, for a contradiction, that this two-linkage is absent.

Any nonroot set meeting X has at least four neighbours in G. Indeed,
write it as `Z union Q`, where nonempty `Z subset X` and `Q subset P`.
The six neighbours of Z lose at most `|Q|` vertices when Q is included.
If Q is nonempty, a is a new boundary neighbour. The resulting lower
bound is six for empty Q and `7-|Q|>=4` otherwise.

Put `k_p=|N_H(p) intersect X|`. Every k_p is positive. The only
nonroot sets that could have at most three neighbours consist of
ports with at most two X-neighbours.

### Eliminating ports of small degree

For every port p with `k_p<=2`, delete p and complete its neighbourhood
`{a} union (N_H(p) intersect X)` to a clique. Do this sequentially.
There are no P--P edges, so a port's neighbourhood is unchanged by
operations at other ports.

This operation preserves absence of the prescribed two-linkage.
To see the positive lift, its clique boundary has at most three vertices.
Two disjoint paths cannot both use a new clique edge, since that would
require four distinct boundary vertices. If one path uses new edges,
replace its segment between its first and last boundary vertices by
the two-edge path through p. This remains disjoint from the other path.
If neither uses a new edge, neither path changes. Reversing the operations
gives a simultaneous lift through distinct deleted ports.

Let G' be the resulting graph. Every nonempty nonroot set of G' still
has at least four neighbours. Here is a direct verification. For such
a set Y with nonempty `Z=Y intersect X`, start with the at least six
original neighbours of Z. A neighbour can disappear only if it is a
retained port included in Y or a suppressed port touching Z. These
are distinct members of the original three-set P, so at most three
neighbours disappear. If any disappears, a is a new boundary neighbour
of Y: it is adjacent to every retained port and to every X-neighbour
of a suppressed port. Thus the boundary has size at least four.
If Y is port-only, each of its retained ports has a and at least three
X-neighbours, all outside Y. This also gives at least four neighbours.

The graph remains connected: X is connected, all original roots touch
X, and a retains a port neighbour or gains an X-neighbour. Therefore
cofacial consequence stated above applies: with d' nonroots and E
edges, it gives `E<=3d'+1`.

### The degree and face count

Write `d=|X|`, `e=e(H[X])`, and
`A=|N_X(u)|+|N_X(v1)|+|N_X(v2)|`. Thus `A>=4`.
Let m be the number of retained ports, `Klo` and `Khi` the sums of
k_p over suppressed and retained ports, respectively, and t the number
of distinct X-neighbours of suppressed ports. Let f be the number of
new X--X edges added by the suppression operations. Then

`2e+A+Klo+Khi >= 6d`,

whereas G' has exactly

`E=e+f+A+Khi+t+m`

edges. There are no edges between its four roots. Its `d+m` nonroots
and the cofacial bound therefore give

`A+Khi-Klo+2t+2f <= 4m+2`.                         (1)

If m=0, then t is at least three. Otherwise the nonempty set consisting
of X minus these at most two neighbours would have boundary contained
in those neighbours and `{u,v1,v2}`, of order at most five. Since
`Klo<=6` and `A>=4`, the left side of (1) is at least four, exceeding
its right side two.

If m=1, there are two suppressed ports and `Klo<=2t`. Since
`Khi>=3` and `A>=4`, the left side is at least seven, exceeding six.

If m=2, there is one suppressed port, so `t=Klo>=1`. Also `Khi>=6`.
The left side is at least eleven, exceeding ten.

Finally let m=3. No port was suppressed, so (1) says `A+Khi<=14`,
with `Khi>=9`. If both V roots had at least two X-neighbours, then
`A>=6`, a contradiction. Thus one V root has a unique X-neighbour x.
In the graph now being drawn, that V root is pendant: all six-root
edges were deleted at the start.

Contract this pendant edge in the common-face drawing. The four roots
remain distinct and cofacial. The new V root can be adjacent to u,
but not to the other V root, by the disjoint-neighbourhood hypothesis,
and not to a, whose neighbours are precisely P in this case. Thus at
most one root--root edge is created. Delete it if present, writing
`c in {0,1}` for the number deleted. The new graph has `d+2` nonroots
and `E-1-c` edges. The cofacial bound gives

`E <= 3d+8+c`.

Here `E=e+A+Khi+3`. Combining this with the original X-degree bound
yields `A+Khi<=10+2c<=12`, contradicting `A+Khi>=13`.
This completes the proof for `|X|>=3`.

### The two-vertex endpoint

If `X={x,y}`, each vertex has at most the other X vertex, u, the three
ports and one V root as neighbours. Degree at least six forces xy and
all edges from X to `u union P`, and each X vertex has exactly one V
neighbour. Since both V roots touch X, their owners are opposite.
For v_j with owner x and any b in P, take

`{vj,x,b}` and `{u,y} union (P-{b})`.

These are connected and disjoint, with the stated exact root ownership.
