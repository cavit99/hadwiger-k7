# Five-vertex separators in the companion density problem

**Status:** written proof; the adjacent audit records a separate internal
verdict at the exact source hash.
The global density theorem below, Conjecture 19 and HC7 remain open.
All graphs are finite and simple. Put `Q=K_7^=`, with two independent
edges deleted from `K_7`.

**Global target (unproved).** Every five-connected `Q`-minor-free graph
`G` satisfies `e(G)<4|V(G)|`.

This would exclude the seven-connected, minimum-degree-eight critical
host. The results below restrict its five-vertex separators; they do not
prove the target or establish an induction class closed under contraction.

## 1. Exact rooted input and the fifth root

A pair `(F,S)` is internally `k`-connected here if no separation `(A,B)`
has `S subseteq A`, `B-A` nonempty and `|A intersect B|<k`.
The external input is [Norin--Totschnig, Lemma 12](https://arxiv.org/html/2507.03244v1#S2),
whose primary statement and rooted-connectivity definition were inspected,
as recorded in the
[audited rooted-helper source](../results/hc7_k7minus_degree7_rooted_helper_closure.md)
at SHA-256
`6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67`:
if `(F,Z)` is internally four-connected, `|Z|=4`, and
`e(F)>=4|V(F)|-9`, there are four disjoint connected `Z`-rooted bags and
two further disjoint connected helpers. Both helpers contact all four
root bags and each other. No root-root contacts are asserted.

**Lemma 1.** Suppose `(F,S)` is internally five-connected, `|S|=5`,
`Z=S-{s}`, and `e(F)>=4|V(F)|-9`. Then there is such a `Z`-rooted
two-helper model with `s` in a helper.

**Proof.** If `(F,Z)` is internally four-connected, use the input directly.
Otherwise a prohibited separation of order at most three has open side
exactly `{s}`: if it contained a nonroot, adjoining `s` to its separator
would contradict internal five-connectivity at `S`. Thus `d_F(s)<=3`.
The pair `(F-s,Z)` is internally four-connected, by the same separator
lift, and
`e(F-s)>=4|V(F)|-12=4|V(F-s)|-8`.
Apply the input there and restore `s`.

In `F`, maximize the helper union, then minimize the total root-bag order.
Each root bag has exactly one vertex adjacent to the helper union.
Indeed, two distinct ports can be chosen for the two helpers if there
are two ports at all. A minimal tree joining those ports and its prescribed
root has a nonroot port leaf. Moving it to its adjacent helper preserves
both helper contacts and the root, and enlarges the helper union.
No component outside all six bags contacts a helper, since it could be
absorbed. Thus the helper union has at most four actual external neighbours.
If `s` were outside it, these neighbours would give a prohibited rooted
separation at `S`. Hence `s` is in a helper. All moves preserve disjointness
and the four prescribed roots; the optimization is finite. QED

Internal five-connectivity at `S` alone does **not** imply internal
four-connectivity at `Z`. The possible low-degree fifth root is handled
explicitly above.

## 2. Full components and boundary models

Let `G` be five-connected and `Q`-minor-free, and let `S` be a five-set
such that `G-S` has components `C_1,...,C_r`, where `r>=2`.
Each component contacts every vertex of `S`: missing one would give a
cut of at most four vertices. The pair `(G[C_i union S],S)` is internally
five-connected, since any prohibited nonroot open side remains separated
from the rest of `G` by the same at-most-four vertices.

**Lemma 2.** The following restrictions hold without a density hypothesis:

- `r<=4`;
- if `r=3`, `G[S]` contains no diamond `K_4^-`;
- if `r=4`, `G[S]` induces a matching and isolated vertices.

**Proof.** Contracting each component gives distinct bags complete to the
five singleton roots. Five components would give `K_{5,5}`. Merge three
disjoint cross pairs in that model. The three merged bags are universal;
the remaining two bags on each shore form a four-cycle. These seven bags
give `Q=K_3 join C_4`.

For three components and a diamond on four roots, merge the fifth root
with one component. This is a universal bag. The other two components
contact it and all four diamond roots. The only possible missing pairs
are the diamond's missing pair and the pair of those two components;
they are independent, giving `Q`.

For four components and a path `a-b-c` on three roots, merge each of the
two other roots with a different component. Both resulting bags are
universal. The five remaining bags are `a,b,c` and two components. All
cross contacts and the path edges remain. Only `ac` and the pair of
remaining components may be missing, again giving `Q`. Thus `G[S]` has
maximum degree at most one. Every merge uses fixed disjoint connected
preimages and retains the displayed contacts. QED

## 3. The dense case has only diamond-free boundaries

**Theorem 3.** If, in addition, `e(G)>=4|V(G)|`, then every such five-set
`S` is diamond-free and hence `e(G[S])<=6`.

**Proof.** By Lemma 2, only `r=2` needs examination. Suppose `Z subseteq S`
spans a diamond, and put `s=S-Z`. Write `F_i=G[C_i union S]`.
If `e(F_i)>=4|V(F_i)|-9`, Lemma 1 gives a `Z`-rooted two-helper model
in `F_i` with `s` in a helper. The other component is disjoint from this
model and contacts all four root bags through their roots, as well as
the helper containing `s`. The literal diamond edges on `Z` survive.
These seven bags miss at most the diamond's missing pair and the contact
from the other component to the other helper. Those pairs are independent,
so they give `Q`, a contradiction.

Consequently `e(F_i)<=4|V(F_i)|-10=4|C_i|+10` for both sides. Since the
boundary edges are counted twice,
`e(G)=e(F_1)+e(F_2)-e(G[S])<=4|V(G)|-e(G[S])<4|V(G)|`,
a contradiction. Finally, a diamond-free five-vertex graph has at most
six edges: if it has a triangle, each other vertex has at most one
neighbour on it, giving at most `3+2+1=6`; if triangle-free, the elementary
triangle-free edge bound gives at most `floor(25/4)=6`. QED

## 4. Combining models across the actual boundary

Call a closed side `F_i` **heavy** when `e(F_i)>=4|V(F_i)|-9`.
This threshold is only sufficient for the following construction.

**Theorem 4.** Let `G` be five-connected, let `S` be a five-vertex cut
with `r>=2` components, and let `h` of its closed sides be heavy.
Each of the following conditions forces a `Q` minor:

- `r+h>=5`;
- `r+h=4` and `G[S]` contains a three-vertex path;
- `r+h=3` and `G[S]` contains a diamond.

**Proof.** If `r>=5`, the `K_{5,5}` construction of Lemma 2 applies.
If `r+h>5`, use only `5-r` heavy sides and treat the others as whole
components. Thus it suffices to consider `3<=r+h<=5`.
Put `k=7-r-h`, and choose `k` roots spanning `K_k` minus at most one
edge, as supplied by the corresponding hypothesis. Choose the `h`
distinct star centres outside those roots.

A heavy side supplies five disjoint connected bags, one for
each actual root in `S`, with a star centred at any prescribed `s in S`,
and a sixth bag adjacent to all five. These are exactly Lemma 1's four
root bags, the helper containing `s`, and the other helper.

For `h=0`, start with the five singleton root bags. Otherwise unite the
bags owning the same root across the different sides. Their only overlaps are at
that root, so all five resulting bags remain connected and disjoint.
Keep the free helper from every heavy side, and use the whole component
of every other side as a helper. All `r` helpers are disjoint and adjacent
to every root bag. Each selected star centre contacts all other root bags.

Contract disjoint cross pairs
between the remaining `r-2` roots and distinct helpers. These pairs are
connected and have fixed disjoint preimages. The resulting seven bags
consist of `r+h-2` universal bags, the chosen `k` root bags, and two
helpers. Only the missing root pair and the helper pair can be absent;
their ends are disjoint. This is `Q`. QED

Thus four components permit no heavy side. Three components permit at
most one, and if one is heavy the boundary is a matching. With two heavy
sides the boundary is also a matching. These are necessary conditions,
not a decomposition or a closed induction.

For two sides with neither heavy, the density hypothesis forces the exact
residue

`e(G[S])=0,  e(G)=4|V(G)|,  e(F_i)=4|V(F_i)|-10  (i=1,2)`.

Indeed, sum the two upper bounds and subtract the duplicated boundary
edges. Models obtained by choosing different centres **in the same side**
need not have compatible ownership; the proof only combines models from
different components.

## 5. A triangulated side gives the missing rooted model

**Lemma 5.** Let `P` be a planar triangulation and let `S` be a prescribed
set of `k>=4` vertices. There is a minor of `P` which is a planar
triangulation on exactly the `k` distinct prescribed roots.

**Proof.** While a nonroot `v` remains, its neighbours occur on a cycle
bounding the union of its incident triangular faces. Every chord between
neighbours lies on the other side of this cycle. Thus `P[N(v)]` is
outerplanar with that cycle as its boundary. Complete it to a triangulated
polygon. An ear has degree two in that completion, and hence also in
`P[N(v)]`, which already contains the boundary cycle. Choose that ear `u`.
The edge `uv` has exactly two common neighbours in `P`.

Contract `uv`, retaining any root at `u`. No two prescribed roots merge,
since `v` is a nonroot. The simple planar quotient has
`3|V(P)|-6-3=3(|V(P)|-1)-6` edges, so it is again a planar triangulation.
Host order decreases by one. Repeat until only the `k` roots remain.
Composing the fixed disjoint contraction preimages preserves every root
and lifts all edges of the final triangulation. QED

**Theorem 6.** Suppose a graph contains a planar triangulation `P`, five
specified vertices `S subseteq V(P)`, and two disjoint connected sets
outside `P`, each adjacent to every vertex of `S`. Then it contains `Q`.

**Proof.** Lemma 5 with `k=5` gives an `S`-rooted `K_5^-` model: a planar
triangulation on five vertices has nine edges. Add the two exterior sets
as separate bags. Both contact all five rooted bags through their actual
roots. Only the missing root pair and the exterior-bag pair may be absent;
they are independent. This gives `Q` without any need to choose which
root pair is missing. QED

In particular, consider two four-connected planar triangulations `P_1,P_2`
intersecting exactly in a stable five-set `S`, with a separate apex `h_i`
adjacent to all of `P_i` and no other added edges. Each apex piece is
five-connected, and their union remains five-connected because the pieces
share five vertices. Writing `p_i=|V(P_i)|`, the union has order
`n=p_1+p_2-3` and size
`(3p_1-6+p_1)+(3p_2-6+p_2)=4n`.
It contains `Q` by Theorem 6, using `P_1` and the two singleton apices.
This resolves that density-threshold family. No classification of arbitrary
five-cut sides or proof of the global density target is supplied.

## 6. Exact remaining induction gap

An edge with at most three common neighbours has
`e(G/uv)-4|V(G/uv)|=e(G)-4|V(G)|+3-|N(u) intersect N(v)|`.
Its contraction preserves `Q`-exclusion and strictly decreases order.
If five-connectivity fails, its endpoints lie in an actual five-cut of
`G`. Theorem 3 restricts that boundary but does not construct a target
across it or supply a smaller five-connected graph with a valid lift.
Completing the boundary to a clique is not an authorized minor operation.

A proposed replacement inequality `e(C)+e(C,S)<=4|C|+4` is
[refuted even when a full boundary apex preserves target exclusion](../barriers/hc7_companion_induction_shortcuts.md#3-a-full-boundary-apex-does-not-retain-a-sufficient-side-class).
The example retains internal five-connectivity at `S` and absence of a
five-rooted `K_6`, but the graph with that apex is only four-connected.
A valid reduction must retain stronger information from the original
ambient host, rather than substitute either of these weaker side classes.
Five-connectivity and a proper `K_6` minor alone also
[do not force the target](../barriers/hc7_companion_induction_shortcuts.md#4-five-connectivity-and-a-proper-six-clique-minor-are-insufficient):
the complement of an eight-cycle is an explicit counterexample.
