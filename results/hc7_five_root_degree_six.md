# Five rooted bags with unrestricted degree-six nonroots

**Status:** written proof; a separate internal audit is recorded beside it.
This is a rooted-model theorem. Conjecture 19 and HC7 remain open.

Graphs are finite and simple; set neighbourhoods are external. A rooted
model has disjoint connected bags containing the prescribed roots separately.

**Theorem.** Let `S={b,c,r,s,t}` be five distinct roots of `F`, with
`rst` a triangle and `D=V(F)-S` nonempty. Suppose every nonempty
`X subseteq D` has at least five neighbours, and every vertex of `D`
has degree at least six. Call a triangle root `u` admissible if there
is an S-rooted model with every pair of bags adjacent except possibly
one of `ub,uc`. At least two of `r,s,t` are admissible.

Equivalently, for any prescribed pair of triangle roots, one can choose
the sole possible missing-edge endpoint from that pair. The models for
different admissible roots may differ. In particular, `F` has an
S-rooted `K_5^-`. No bound on the number of degree-six vertices and no
actual five-connectivity assumption are imposed.

## Input

We use the exact [Norin–Totschnig Theorem 8](https://arxiv.org/html/2507.03244v1#S2)
recorded in the [five-root almost-clique source](hc7_five_root_almost_clique.md),
SHA-256 `de183e350c412739c05a744e811304454ba90856efee9e097813c70617bba9cd`;
its [audit](hc7_five_root_almost_clique_audit.md) has SHA-256
`dc7db3d391ef2701516d64dd32e7546d40e2e4171406193f17d8feadcc4abb47`.
For a graph `J` with four roots `Z`, at least one holds:

1. There is a Z-rooted `K_4` model.
2. There is an order-two trisection whose two specified open parts each
   contain exactly one root. All pairwise intersections are the same
   two-set, and distinct open parts have no edges between them.
3. There is a separation `(A,E)` with `Z subseteq A`, separator order
   at most three, `|E-A|>=2`, and `|Z intersect E|<=2`.
4. The graph has a plane drawing with all four roots on one face.

The primary statement was inspected for the cited source. No fresh primary
inspection is claimed here. The following reductions and facial count are
proved for the present degree-six class.

## 1. Root-preserving reductions

Suppose the theorem fails. Fix two inadmissible labelled triangle roots
and choose such a counterexample minimizing `|D|`. Minimum degree six
forces `|D|>=2`. If `D={p,q}`, both vertices are adjacent to every other
vertex. The bags `{b,p},{c,q},{r},{s},{t}` form a rooted `K_5`, a
contradiction. Thus `|D|>=3`.

Every root sees `D`, by applying the boundary hypothesis to `D` itself.
If a root `a` has exactly one D-neighbour `p`, contract `ap` and keep
its root label. For any surviving nonroot set, old `a` was not in its
boundary. Its boundary is unchanged except that `p`, when present,
is replaced by the merged root. Every surviving nonroot degree is
unchanged for the same reason. The nonroot set remains nonempty, all
five labels remain distinct, and the root triangle remains literal.
Any admissible designated model lifts through this fixed connected
preimage. A smaller counterexample is impossible. Hence every root has
at least two D-neighbours.

We also exclude the following configuration: `b,c` have precisely the
same two D-neighbours `p,q`. Contract the disjoint edges `bp,cq`, keeping
the two labels. Neither old `b` nor old `c` neighbours a surviving
nonroot; its old neighbours `p,q` are replaced by distinct new roots.
Every surviving nonroot degree and set boundary is therefore unchanged.
At least one nonroot remains, and the degree hypothesis itself excludes
an order-one nonroot set. The root triangle and both designated labels
survive, and models lift through disjoint fixed preimages. This again
strictly decreases `|D|` within the counterexample class.

## 2. Each bad root forces a cofacial drawing

Fix either inadmissible triangle root `u`, and call the other two `s',t'`.
Put `J=F-u`, with roots `Z={b,c,s',t'}`. Every nonempty subset of `D`
has at least four neighbours in `J`; its degrees may drop to five.
Apply the recorded four-root alternative.

Its small rooted separation contradicts this boundary bound.

In a rooted `K_4` model, regard the b/c bags as adjacent helpers full to
the s'/t' bags. A contact from either helper to `u`, together with the
literal edges `us',ut'`, makes `u` admissible. Consequently `u` misses
both helpers in every such model. Maximize their union `M`, then minimize
the other two bags. Each of these bags has exactly one actual port into
`M`: two ports permit choosing distinct contacts to the two helpers and
a minimal tree through these ports and the prescribed root. A nonroot
port is a leaf. Moving it into its contacted helper preserves the other
contact and supplies the first through the old tree edge, enlarging `M`.
The literal edge `s't'` preserves the contact between the other bags.

No unused component meets `M`, since it could be absorbed. Thus `N_J(M)`
consists of at most two actual ports. Since `u` misses `M`, the nonroot
set `M-{b,c}` has at most four neighbours in `F`. It is empty. The b/c
bags are singleton and all their D-neighbours are among the two ports.
The normalization makes both ports nonroots and gives precisely the
excluded common-two-neighbour configuration. This rules out this outcome.

In a trisection, each specified open part is its sole root: any nonroots
there would have at most three neighbours in `J`. Let `P` be the common
two-set. All nonroots lie in the third closed part. If `P` contained a
root, the nonempty set `D-P` would have at most three neighbours, in
`P` and the two nonisolated roots. Hence both members of `P` are nonroots.
The literal edge `s't'` prevents either end from being an isolated open
root. Those roots are therefore `b,c`, each with precisely the two
D-neighbours in `P`. The same reduction rules out this outcome.

Only the planar alternative remains. Moreover, `J` is two-connected.
After deleting at most one vertex, every component contains a nonroot:
each retained root originally had at least two D-neighbours. For the
nonroot set `X` of a component, its neighbourhood in `J` is contained
in that component's roots and the deleted vertex. The internal-four
bound forces at least three roots into each component. Two components
are impossible. With no deletion the same argument proves connectivity.
The distinguished facial boundary is consequently a cycle containing
all four roots.

## 3. Two cofacial responses contradict the degree sum

For each root `a in S`, put `k_a=|N_F(a) intersect D|`, and write

`K=sum_{a in S} k_a`,     `e_D=e(F[D])`.

All five numbers `k_a` are at least two. The nonroot degree sum gives

`2e_D+K >= 6|D|`.

For the drawing obtained for a bad root `u`, let `h` be the number of
nonroots on the distinguished facial cycle and put
`t_u=e(F[S-{u}])`. Euler's formula, accounting for this face's length
`4+h`, gives

`e(J) <= 3|D|+5-h`.

The cycle's four roots have eight incidences with cycle edges. At most
`2h` of these meet nonroots, so at least `4-h` cycle edges join two
roots. They are distinct edges counted by `t_u`; thus `t_u>=4-h`.
Subtracting these forced root edges yields

`e_D+K-k_u = e(J)-t_u <= 3|D|+1`.

Combining this with the nonroot degree sum gives `2k_u>=K-2`.
Apply this inequality to the two fixed bad roots `u,w`. If `z` is
the third triangle root, their sum implies

`k_z+k_b+k_c <= 2`.

Its left side is at least six, a contradiction. There cannot be two
inadmissible triangle roots, proving the theorem. All reductions above
strictly decreased nonroot order and preserved every designated model
on lifting. QED

The conclusion supplies five rooted bags. It does not reserve a disjoint
sixth helper, retain an arbitrary prescribed missing-edge endpoint, or
complete the remaining two-triangle critical-host construction.
