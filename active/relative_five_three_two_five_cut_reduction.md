# Five-cut reduction for the relative three--two linkage target

**Status:** written reduction with a
[separate internal audit](relative_five_three_two_five_cut_reduction_audit.md)
for a conjectural target. This does
not prove the linkage target, the four-cut C19 case, HC7, or an independently
substantiated NT-comparable theorem.

All graphs are finite and simple. Neighbourhoods are external. Let
`T=U dotcup V`, where `|U|=3` and `|V|=2`, and put `D=V(F)-T`.
The target asserts that, if `|D|>=2`, every nonempty subset of D has at
least five neighbours and every vertex of D has degree at least six, then
there are disjoint connected vertex sets A,B with `A intersect T=U` and
`B intersect T=V`. The two-nonroot endpoint is included explicitly below.

## Reduction

If this target is false, choose a counterexample with minimum `|D|`,
allowing all choices of the five labelled roots and their three--two
partition. Then:

1. `|D|>=3`, D is connected, and every root has at least two D-neighbours.
2. Every nonempty proper `X subset D` has at least six neighbours.
3. Adding all edges on T makes F six-connected.
4. No three-set `P subset D` makes `F-(V union P)` have exactly
   three components, each containing one U root, including root-only
   components.

Assertion 3 concerns a graph with virtual root edges; it is not a
linkage conclusion in F.

## Endpoints and a thin root

There is no instance with one nonroot: it would have degree at most five.
With two nonroots p,q, each has degree six and is adjacent to the other
and all five roots. Thus `U union {p}` and `V union {q}` are the required
sets. A counterexample therefore has at least three nonroots.

The boundary of all D is exactly T. If D is disconnected, each of its
components has boundary exactly T. Each component with T satisfies the
same hypotheses and has fewer nonroots, so its two carriers contradict
minimality. Hence D is connected.

Suppose a root r has just one D-neighbour p. Contract rp, retaining r as
the label of its two-vertex preimage. No other nonroot is adjacent to r,
so every surviving nonroot degree is unchanged. For a subset of the
surviving nonroots, a boundary vertex p, when present, is replaced by r;
r was not already in that boundary. Thus its boundary cardinality is
also unchanged. The smaller instance has the same five distinct root
labels and the same partition. Its carriers lift through the connected
preimage `{r,p}`, a contradiction. Every root therefore has at least two
D-neighbours.

## A largest five-boundary side

Suppose there is a nonempty proper subset of D with boundary of size
five. Each of its components has that same boundary: each component's
boundary is contained in the given five-set and has size at least five.
Choose a connected proper set X of maximum order among all such sets,
and write `S=N_F(X)`, with `|S|=5`.

Every nonroot port `p in S intersect D` has at least two neighbours
outside `X union S`. Indeed, if it had at most one, then

`N_F(X union {p}) = (S-{p}) union (N_F(p)-(X union S))`.

The five-neighbour condition forces the second set to be a singleton
`{q}` and the displayed boundary to have size five. The larger set is
connected. If it is proper in D, it contradicts the choice of X. If it
is all of D, then `S-{p}` consists of four original roots and q is the
fifth original root. That fifth root has p as its unique D-neighbour,
contradicting the preceding paragraph.

Form the outer graph `F'=F-X+K_5(S)`, retaining the original root set T
and its original partition. Every surviving nonroot outside S retains
its degree, because it has no neighbour in X. Every nonroot in S has
four clique neighbours in S and at least two neighbours outside
`X union S`, so its degree in F' is at least six.

The five-neighbour condition also survives. For a nonempty
`Y subset D-X` disjoint from S, its neighbourhood is unchanged. If Y
meets S, then

`N_F(X union Y) subseteq N_{F'}(Y)`:

all of `S-Y` is adjacent in F' to any vertex of `Y intersect S`, and
all remaining old boundary edges survive. The left side has size at
least five. Thus F' is a smaller instance of the target. Its nonroot set
is nonempty since X is proper, and cannot have order one by its degree
bound; it therefore has at least two vertices.

The inner graph `F[X union S]`, with S as its five roots, retains every
neighbour and degree of X and every subset boundary in X. Also `|X|>=2`
by the degree bound, and `|X|<|D|`. Minimality applies to it for every
three--two partition of S.

## Simultaneous lift of the two carriers

Let A',B' be the carriers in F', and put
`S_A=A' intersect S`, `S_B=B' intersect S`. They are disjoint. Every
original root in S belongs to its correct carrier, so every unused
vertex of S is an original nonroot.

If `|S_A|,|S_B|<=3` and they are not both three, their prescribed sets
can be extended to a partition of S into sets of sizes three and two,
in one order or the other. Inner minimality gives disjoint connected
sets containing those parts. Adjoin the corresponding inner set to an
outer carrier whenever that carrier meets S. Every virtual edge used
inside that carrier has both ends in its own S-part and is replaced by
connectivity through its inner set. A carrier missing S used no virtual
edge and is left unchanged.

If one S-part has size at least four, the other has size at most one.
Adjoin X to the former carrier. The connected set X contacts every
vertex of S, so this replaces all its virtual edges. The other carrier
uses no virtual edge. This also covers an empty opposite S-part.

In both cases the resulting carriers are connected in the original F,
remain disjoint, and retain exactly U and V as their original roots.
This contradicts minimality. No proper nonempty subset of D can
therefore have boundary five.

## The completed graph and the remaining obligation

Let `F^+=F+K_5(T)`. Delete any set K of at most five vertices. If no
root survives, then `K=T` and the remainder is the connected graph D.
Otherwise all surviving roots lie in one component, because they form
a clique. Any other component Y lies in D. It cannot be all D, since
every original root has a D-neighbour. It would therefore be a proper
nonempty D-set with `N_F(Y) subseteq K`, contradicting the established
six-neighbour bound. Hence F+K5(T) is six-connected.

This does not license the virtual edges inside U for the desired
connected U-carrier. In particular it does not meet the hypothesis of
the existing Xie completion theorem, whose specified completion adds
the V edge and the six U--V edges, but not the three U edges. Cuts in
that smaller completion can still separate surviving U roots after
both V roots have been deleted. Eliminating those cuts or lifting a
permitted construction across them is the remaining proof obligation.

The precise external input is Shijie Xie, *6-Connected Graphs Are
Two-Three Linked*, October 2019 dissertation, Theorem 1.0.1 in the
[official thesis PDF](https://aco.gatech.edu/sites/default/files/images/xie_thesis.pdf).
The theorem number differs in another archived version. Its conclusion
is the required linkage in the original graph, under six-connectivity
of exactly the smaller completion just specified.

## Further normalisations

Continue with the same minimum counterexample, after the five-cut
reduction. For every root r, the graph induced by `N_D(r)` has no
isolated vertex. Indeed, if `p in N_D(r)` has no neighbour in that set,
contract rp, retaining root r. A surviving nonroot loses degree only
if it was adjacent to both r and p; no such vertex exists. Every
nonempty surviving nonroot set was a proper subset of D, so had at
least six neighbours, and identifying r,p loses at most one of them.
The smaller graph is an instance of the original class and its two
carriers lift through `{r,p}`, a contradiction.

The graph `F-V` is two-connected. After deleting a set K of at most one
vertex, suppose there are two components containing nonroots. For the
nonroot set X of either component,

`N_F(X) subseteq K union V union (U intersect component)`.

It is a proper D-subset, so at least three U roots must lie in each
component, which is impossible. Thus all surviving nonroots belong to
one component. A root-only component is also impossible: any root in
it would have all its at least two D-neighbours in K. Consequently the
remainder is connected, as asserted.

It follows that V is independent and its two roots have disjoint
D-neighbourhoods. An edge on V, or a common D-neighbour p, would give
a V-carrier of order two or three, respectively; the connected graph
`F-V`, or `F-V-p`, supplies the U-carrier.

Two roots with the same two-element D-neighbourhood `{p,q}` may also
be excluded. Contract one root with p and the other with q, preserving
both labels. Surviving nonroot degrees are unchanged: they saw neither
old root, and p,q have distinct replacement labels. Subset boundaries
are unchanged for the same reason. The two connected preimages are
disjoint, so the smaller-instance linkage lifts with its original
three--two partition.

## Three separate U-components behind a five-cut

**Claim.** In the above minimum counterexample there is no three-set
`P subset D` for which the components of `F-(V union P)` are three
components `C_1,C_2,C_3`, with `C_i intersect U={u_i}`. Components
consisting only of their U root are allowed in the statement.

This does not exclude a cut with a two--one distribution of U, or a
cut containing a U root.

Put `X_i=C_i-{u_i}`. Each nonempty connected component X of `F[X_i]`
has neighbourhood contained in the six-set `{u_i} union V union P`.
It is a proper D-subset, so is full to this six-set. All degrees of X
are retained in this side. Such X has at least two vertices, since a
singleton full to both V roots contradicts their disjoint
D-neighbourhoods. Also `C_i` is connected, and, when `X_i` is nonempty,
it is full to P even after a specified port of P is omitted.

We first give the two-path and planar calculations used in the claim.

### A two-path choice on any pair of ports

Fix a nonempty `X_i`, a V root `v_j`, and two distinct ports a,b in P.
There are disjoint paths from `{u_i,v_j}` to `{a,b}` in the induced
graph on these four roots and `X_i`, in one of the two assignments.
Their interiors avoid all five roots and the unused P port.

For the proof it suffices to use one connected component X of
`F[X_i]`. Every nonempty subset of X has boundary at least four in
this four-root graph: only the other V root and the other P port were
deleted. All four roots contact the connected X, and `|X|>=2`.
If the two paths did not exist, the set version of Menger's theorem
would supply a separator of order at most one between the source pair
and sink pair. Deleting a terminal leaves a surviving source and sink
joined through X. If the separator is a nonterminal w, every nonempty
component of `X-w` can contact only the source pair or only the sink
pair. Its boundary then lies in that pair together with w, of order at
most three, a contradiction. There is a nonempty component since
`|X|>=2`.

Call b **attainable for j on side i** if such paths exist with the
specified assignment `v_j--b` and `u_i--a` for some `a in P-{b}`.
The other P port is not used. The preceding argument shows that at
least two ports are attainable for each j.

### The cofacial edge bound

We use the Two Paths Theorem, as stated in Norin--Totschnig,
[arXiv:2507.03244v1, Theorem 13](https://arxiv.org/html/2507.03244v1).
For four distinct terminals with no prescribed two-linkage, its
root-free separation alternative is excluded if every nonempty
nonterminal subset has at least four neighbours. The remaining
alternative is a disc drawing with the four terminals in the
alternating order.

In particular, delete all edges between the four terminals. Suppose
the graph is connected, has d nonterminals, and has e edges with at
least one nonterminal endpoint. Add the four boundary-cycle edges
outside the disc. Euler's inequality for a simple connected plane
graph with outer cycle of length four gives

`e+4 <= 3(d+4)-7`, hence `e <= 3d+1`.

This uses neither two-connectivity nor a simple original facial walk.

For a fixed nonempty side, write X for all of `X_i`, write u for
`u_i`, and name `P={p,q,r}`. Set `d=|X|`, `e=e(F[X])`, and write
`k_z=|N_F(z) intersect X|` for a side root z. All six `k_z` are
positive. The original degree bound is

`2e+k_u+k_p+k_q+k_r+k_v1+k_v2 >= 6d`.                 (1)

If r is unattainable for j, identify p,q to a single terminal a and
delete the other V root. Any linkage `u--a, v_j--r` in this graph
lifts to the forbidden two paths: truncate the a-path at its final
edge to its actual p or q endpoint. No other path uses a. Thus this
four-root linkage is absent. Nonterminal boundaries are at least
four, since the deletion and identification lose at most two from
the original six. Writing
`t=|N_F(p) intersect N_F(q) intersect X|`, the cofacial bound gives

`e+k_u+k_p+k_q+k_r-t+k_vj <= 3d+1`.                 (2)

Identification here is an auxiliary graph operation for applying the
negative Two Paths Theorem; no arbitrary minor lift through a
disconnected p,q preimage is used. The positive path lift just given
is sufficient. The graph remains connected after root edges are
removed, because every component of X contacts all four terminals.

### Each port is attainable for at least one V root

Suppose r is unattainable for both V roots. Add (2) for j=1,2 and
subtract (1). This gives

`k_u+k_p+k_q+k_r-2t <= 2`, hence `k_u+k_r <= 2`.

Both terms are positive, so each is one. Unattainability of r also
implies that u has no edge to p or q: such an edge, together with a
path through a connected full component of X from `v_j` to r,
would give the required paths. If x is u's sole X-neighbour, then
`N_D(u)={x,r}`, since root D-degree is at least two. The no-isolated-
neighbour normalisation gives xr. Hence r's sole X-neighbour is x
too. But `X-{x}` is nonempty, since X cannot be a singleton full to
both V roots, and its boundary lies in `{x,p,q,v_1,v_2}`, of order
at most five. This contradicts the proper-six-boundary property.

### A missing port forces both opposite assignments

Suppose r is unattainable for root `v_2`. Then both prescribed
linkages

`u--p, v_1--q` and `u--q, v_1--p`

exist in the graph on X and their four endpoints. To prove the first,
suppose it fails. Deleting r and `v_2` leaves nonterminal boundary at
least four, so the cofacial inequality is

`e+k_u+k_p+k_q+k_v1 <= 3d+1`.                       (3)

Add (3) to (2) for j=2 and subtract (1). Thus

`k_u+k_p+k_q-t <= 2`.                              (4)

The second term `k_p+k_q-t` counts the X vertices adjacent to p or
q, and is positive. Consequently `k_u=1`, and p,q have the same sole
X-neighbour y. As above, u has no p or q edge, so if x is its sole
X-neighbour then `N_D(u)={x,r}` and xr is an edge.
The boundary of `X-{x,y}` lies within
`{x,y,r,v_1,v_2}`, which has order at most five. Therefore
`X subseteq {x,y}`. If x=y, X is a singleton full to both V roots,
which is impossible. Otherwise x can be adjacent only to y, u, r,
and at most one V root; its degree is at most four, contradicting
degree at least six. This proves the first assignment. Interchanging
p,q proves the second.

### Assembly when at most one U-component is root-only

First suppose all three `X_i` are nonempty. On side 1 at least two
ports are attainable for `v_1`, and on side 2 at least two are
attainable for `v_2`. Choose a common port b. The two V paths join
at b and otherwise lie in distinct sides. The U paths end at ports
in `P-{b}`. Adjoin the connected third side and these one or two
ports to the U paths; it joins them and contains `u_3`, while
avoiding b and both V paths. These are the desired carriers.

The same construction works if `C_3={u_3}` and u3 sees all three
ports. If this root-only component has exactly two D-neighbours,
name them p,q and write `P={p,q,r}`. If r is attainable for opposite
V roots on the two nonempty sides, join the two V paths at r; the
two U-path ports lie in `{p,q}` and are joined through u3.

Otherwise the preceding coverage property forces both sides to
have r attainable for exactly the same V root; relabel it `v_1`.
Thus r is unattainable for `v_2` on both sides. On side 1 take the
unordered two paths to the specified pair `{p,q}` for sources
`{u_1,v_2}`. Let b be the `v_2` endpoint and a the `u_1` endpoint.
The opposite-assignment lemma on side 2 gives paths `v_1--b` and
`u_2--a`. Join the V paths at b; join the U paths at a and add u3,
which is adjacent to a. This is a disjoint linkage with exact roots.

### Assembly with two root-only components

Suppose `C_1={u_1}`, `C_2={u_2}` and `X_3` is nonempty. Write
`A_i=N_D(u_i) subseteq P`; each has size at least two. Equal
two-element sets have already been excluded by simultaneous
contractions. Otherwise `A_1 union A_2=P`. Choose
`q in A_1 intersect A_2` and contract the connected set
`{u_1,q,u_2}` to a terminal a. The other three terminals are
`u_3,v_1,v_2`, and the remaining nonroots are `D-{q}`.

Every nonempty remaining nonroot set had boundary at least six;
merging three vertices loses at most two, so its new boundary is
at least four. Only the other two P vertices can lose degree:
each loses at most two. All other nonroots saw at most q in the
contracted set. Consequently, writing d for the new nonroot order,
the sum of their degrees is at least `6d-4`.

If the two-linkage `a--u_3, v_1--v_2` were absent, the cofacial
bound would imply that at most six edges join terminals to
nonterminals: subtract the nonterminal degree sum from twice
`e_D+e(D,terminals)<=3d+1`. In fact there are at least seven.
Terminal a sees both remaining P ports, since `A_1 union A_2=P`,
and also a nonroot in `X_3`, since q is full to that side. Terminal
u3 retains at least one D-neighbour. The two V roots together
retain at least three: originally each had at least two, and q
belonged to at most one of their disjoint D-neighbourhoods.
This is a contradiction. The resulting a--u3 path lifts using the
entire connected preimage of a, giving the original U-carrier.

Finally, if all three components are root-only, then D=P has order
three. Minimum nonroot degree six makes `F[D]` a path or triangle.
In the path case its two ends are each adjacent to all five roots,
and give disjoint U and V stars. In the triangle case every
nonroot misses at most one root. As every V root has at least two
D-neighbours, some nonroot b sees both V roots. Use b for the
V-carrier. The other two nonroots are adjacent and collectively
see every U root, since each U root has at least two D-neighbours.
They give the U-carrier. This completes the three-component claim.

## Inner port coverage by minimum-counterexample induction

In the same minimum counterexample, suppose nonempty `X subset D`
has all its neighbours in the six-set `{u} union V union P`, where
`u in U` and `P subset D-X` has order three. Then, for every port
`b in P`, at least one `v_j in V` has disjoint connected carriers
with exact roots `{u} union (P-{b})` and `{v_j,b}` in this side,
avoiding the other V root. The choice of j may depend on b.

Every X-subset retains its original boundary and degrees in the side;
its boundary has order at least six. Identify `v_1,v_2` to one
auxiliary root w. Nonroot degrees are unchanged, because their
V-neighbourhoods are disjoint. Every nonroot subset loses at most
one boundary vertex, so retains at least five neighbours. A singleton
X would be full to both V roots, which is impossible; hence
`2<=|X|<|D|`. The resulting five-root graph on
`X union {u,w} union P` is a smaller instance of the original
induction class. Apply minimality to its partition
`{u} union (P-{b})` and `{w,b}`.

The first carrier avoids w and is already an actual connected set
in the unmodified side. In the second carrier take a simple w--b
path. Only its first edge uses w; choose the actual V root from
which that edge arose, and retain the rest of the path unchanged.
This also covers a direct w--b edge. The lifted path avoids the
first carrier and the other original V root. No disconnected
preimage of w is used as a branch set.

This proves coverage of every port by at least one V choice. It
does not prescribe that choice or synchronise it with the port
and V root used by an outer construction; that allocation remains
unproved.

## Remaining scope

The conjectural relative three--two theorem is still unproved. The
new claim excludes the three-singleton-U distribution behind
`V union P`, with all root-only endpoints included. It does not
exclude a two--one U distribution, including a four-cut consisting
of V and two nonroots, or a five-cut of the smaller Xie completion
which also contains a U root. No HC7, whole C19,
or independently substantiated NT-comparable conclusion is asserted.

A [path construction](../barriers/relative_six_boundary_pair_and_arm.md)
refutes allocating both V roots in one side while retaining a disjoint
u--P arm, even with degree six and six-neighbour boundaries. The
two-side arm construction above avoids that false intermediate claim.

The induction class here retains the labelled linkage problem. Its
virtual completions are not asserted to preserve a given colouring or
critical-host hypothesis. Thus these normalisations cannot be imposed
directly on the original coloured side of a missed-root four-cut. A
proof of the whole relative linkage target would supply the required
application to its three--two boundary blocks.
