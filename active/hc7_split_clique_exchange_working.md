# Exchanges in a maximal deficient partition

**Status:** working proof, not independently audited. This develops the
[split-clique construction](hc7_split_clique_construction_working.md).
It does not close that neighbourhood case or HC7. Its input is the
unaudited oriented strengthening recorded there.

## Setup and a whole-region exchange

Let G be seven-connected and K7-minor-free, with
`N(u)=P dotunion D`, where P is a triangle and D a four-clique, anticomplete
to one another. Put `M=G-({u} union D)`. Fix `r in D` and `Q=D-{r}`.
Suppose `M=A dotunion B`, where both parts are connected and meet P,
A contacts every Q vertex and misses r, and B contacts every D vertex.
Choose A inclusion-maximal among partitions with these properties.

**Exchange.** There is no connected nonempty `X subset B` which touches A
and for which `B-X` is connected, meets P and contacts every Q vertex.

Indeed, if X misses r, moving X to A gives a larger admissible A. All
r-neighbours in M remain in `B-X`. If X contacts r, use the seven bags

    {u},  ({q}: q in Q),  {r} union X,  A,  B-X.

The enlarged r bag is connected. It contacts A through X, and `B-X`
through an edge from X, since B is connected. The two helpers contact
one another through their distinct P vertices. Every remaining contact
comes from Q being a clique, the original r-Q edges, the two Q-full
helpers, and u being adjacent to P and D. Thus these are disjoint K7
bags. No quotient or induction is used.

Consequently, if `x in B` touches A and K is any component of `B-x`
which meets P, then K misses a Q vertex. Otherwise `X=B-K` is connected
through x and the exchange applies. In particular all B-neighbours of
some Q vertex lie in `B-K`.

## The block containing two P vertices

Assume B contains two P vertices p,q. A contains the third. Let K be the
block of B containing pq; bridge edges count as blocks. For `x in K`,
write L_x for x together with all components of `B-V(K)` attached at x.
Each such component has one attachment to K, and the sets L_x are
pairwise disjoint. Say x owns a label d in Q if every B-neighbour of d
lies in L_x. Every label has a B-neighbour and therefore has at most one
owner. Let Z be the owner vertices and I the set of owned labels.
Then `|Z| <= |I| <= 3`.

Every vertex of K touching A belongs to Z. To see this, delete such a
vertex x. The component containing `K-x` contains a P vertex, since
p,q are both in K. The exchange shows that it misses a Q label, whose
B-neighbours consequently all lie in L_x.

There is no off-K component attached at a nonowner x. If such a
component H had an A-neighbour y, apply the same exchange at y: the
component of `B-y` containing K meets P, so a Q label has all its
B-neighbours in H. This makes x an owner. Otherwise H has no
A-neighbour, and its outside G-boundary is contained in `{x} union D`,
of order at most five, contradicting seven-connectivity. Here H contains
no P vertex, so it has no u-neighbour.

Now put `Y=V(K)-Z`. No vertex of Y touches A. There are no off-K
components at its vertices, and no owned Q label contacts Y. Hence

    N_G(Y) subseteq Z union (Q-I) union {r,u}.

The right side has order at most five. If Y were nonempty, this would
separate it from A. Thus `V(K)=Z`: the block K is an edge or a triangle,
and every vertex owns a Q label.

## In the triangular case every arm is a path

Suppose `K={p,q,z}` is a triangle. Each core vertex x owns exactly one
label d_x, and every Q label is owned. The set L_x contacts no Q vertex
other than d_x.

Every component H of `B-V(K)` at x has an A-neighbour. In fact

    N_G(H) subseteq {x} union N_A(H) union {d_x,r},

so it has at least four distinct A-neighbours. Since `B-H` is connected
and meets P, the exchange forces H to contain every B-neighbour of some
Q label. That label must be d_x. There is therefore at most one such
component H at x; if it exists, x itself does not contact d_x. If there
is no component, x is the unique B-neighbour of d_x.

When H exists, its union with x is an induced path from x to a unique
B-neighbour of d_x. Here are the block details. Root its block tree at x.
For every cutvertex, each component farther from x is root-free and has
outside B-boundary one vertex. Seven-connectivity therefore makes it
touch A. The exchange then forces it to contain every B-neighbour of
d_x. There can be only one such component, and no d_x-neighbour can lie
before it. Thus the block tree is a path, with all d_x-neighbours in
its terminal block.

In a nonterminal block, remove its two attachment vertices from its
vertex set, leaving Y. A vertex of Y is not a B-cutvertex; deleting it
retains P and all Q contacts. The exchange therefore forbids an A-edge
at that vertex. There is also no d_x-contact there. Consequently
`N_G(Y)` is contained in the two attachment vertices together with r.
Seven-connectivity makes Y empty, so the block is an edge.

In the terminal block, let a be its attachment towards x. Any other
vertex touching A must be the unique B-neighbour of d_x; otherwise its
deletion again permits the exchange. Thus there is at most one such
vertex t. If it exists, deleting a,t from the block leaves a set with
outside boundary contained in `{a,t,r,d_x}`, of order at most four.
If it does not exist, deleting a leaves a set with boundary contained
in `{a,r,d_x}`. Seven-connectivity excludes either nonempty set. The
terminal block is therefore the edge at, with t the unique B-neighbour
of d_x. This also covers a single-edge arm.

Consequently `B union Q` is an induced triangular-prism subdivision
with caps `{p,q,z}` and Q, and three rails from x to d_x. The p and q
rails have nonempty interiors because P is anticomplete to D. The z
rail may be the single edge `z d_z`. The connected remainder A contains
the third P vertex and is anticomplete to r. The original r-neighbours
are all on the prism. These are actual paths and contacts, not edges
introduced by a completion.

## Remaining obligation

This is a stronger normal form, not a K7 construction. The shifted cap
contains z instead of the third P vertex, which lies in A. Thus the
previous two-triangle theorem cannot simply be reapplied: its cap
anticompleteness may fail on the z rail, and a root-free set containing
the third P vertex can lose its u-neighbour when passing to
`G-{u,r}`. The edge-core case and the case where B contains only one P
vertex also remain. Root expansion in the exchange is a single explicit
minor construction; no later quotient inherits seven-connectivity or
chromatic criticality.

## Further block reduction and a cross-label exchange

The following extension also applies when B contains only one P vertex.
Root the block tree of B at its P clique (or its sole P vertex). For a
nonroot block K let a be its attachment towards P. A core vertex
`x != a` touching A must own all B-neighbours of some Q label in the
forward region attached at x: apply the exchange to the component of
`B-x` containing P. Distinct such forward regions are disjoint.
There are therefore at most three owner gates Z in `K-{a}`. A forward
component at a nonowner has no A-neighbour, by the same argument; its
outside boundary is then contained in its attachment and D, impossible.

Put `Y=V(K)-({a} union Z)`. It has no A-neighbour or forward component.
If I is the set of labels owned at Z, then

    N_G(Y) subseteq {a} union Z union (Q-I) union {r}.

This has at most five vertices, since `|Z| <= |I| <= 3`. No P vertex
lies in Y. Seven-connectivity therefore makes Y empty. For a root
block containing the sole P vertex p, the same proof uses p in place
of a. Consequently **every block of B has at most four vertices**.
In particular B has treewidth at most three. This does not assert that
B is a tree or bipartite: a four-vertex block may be a four-cycle, a
diamond or a K4, and triangles are also allowed.

Every pendant component pointing away from P touches A, since otherwise
its outside boundary is contained in one attachment and D. The exchange
forces such a component to contain all B-neighbours of some Q label.
Disjoint pendant components consume distinct labels, so there are at
most three root-away leaf branches. This bound concerns branches of the
rooted block structure, not the number of subdivision vertices.

There is a valid transition between different missing labels which keeps
all D roots singleton. Suppose L is a connected root-free pendant region
of B, touches A and contains all B-neighbours of an owned label d. Assume
that `B-L` contacts every label in `Q-{d}`, and that r has neighbours
both in L and in `B-L`. Then

    A' = B-L,       B' = A union L

is an admissible oriented partition with missing label d. The first
part is connected, meets P, misses d and contacts `D-{d}`; the second
is connected, meets P and is D-full. All these are original host sets.
The transition interchanges the two P multiplicities.

This operation has no automatic decreasing parameter. If the starting
A was maximum over all labels, it gives only

    |A| >= |B|-|L|.

The transition can reverse which side is large; it is not a valid
induction merely because a pendant region was moved. A successful use
must supply an additional monotone quantity or complete the original
host construction directly.

The same ownership argument bounds the total cycle rank. At a block
with distinguished vertex a towards P, every other block vertex owns
a nonempty subset of Q in its forward region. These subsets are disjoint.
Only labels owned in that region can be owned farther down it: a label
with a neighbour outside the region cannot have all its B-neighbours in
any smaller forward region. Separate forward components likewise consume
disjoint nonempty label subsets.

A four-vertex block therefore uses all three labels, one at each of
its three forward gates. No later block can contain a cycle, since that
would need at least two forward owner gates. Its own cycle rank is at
most three. If there is no four-vertex block, a non-edge block is a
triangle. Its two forward gates split the available labels into two
nonempty subsets; with only three labels, at most one continuation can
retain two labels and contain one further triangle. No third triangle
is possible. Since cycle ranks add over blocks, in all cases

    e(B)-|B|+1 <= 3,       hence e(B) <= |B|+2.

If B contains two P vertices, its root block is an edge or triangle.
A triangular root block spends all three labels at its three vertices,
so its arms are paths. An edge root block divides the labels into two
nonempty owned groups; at most one group has two labels, allowing at
most one further triangle. Thus in this case the stronger bound is
`e(B)-|B|+1 <= 1`. These are actual-edge bounds on B, not bounds on a
selected spanning subgraph.

## Where a two-P partition can still resist the label switch

The triangular-root-block case admits the suffix switch: take the last
r-neighbour on a nontrivial one-label rail, and the suffix through its
unique Q-neighbour. It contains one r-neighbour and leaves another
outside, because r has at least three M-neighbours and at most one root
block vertex can meet r. The switched deficient side contains both
original B roots. Enlarging it to an inclusion-maximal deficient side
keeps those two roots, so its full complement has exactly one P root.

For an edge root block pq, a forward component carrying just one owned
label is a path, by the same block argument as above. Other, unowned
labels can have neighbours on that path, but they also have neighbours
outside its forward region. A suffix from its last r-neighbour therefore
loses only its owned label and gives the same switch. The switch also
works after either branch of a two-label component has separated into
one-label regions. If r has several neighbours in such a region, choose
the last one; if it has just one, its other M-neighbours are outside.

The only remaining location for all r-neighbours is consequently the
initial common stem of a component owning two Q labels, attached at one
of p,q. This stem ends at the first branching block or first Q-neighbour.
The last stem vertex may itself contact Q. The other P endpoint owns
the third Q label, which misses the whole stem. The ownership budget
allows at most a triangular branching block; the two outgoing regions
there carry different labels. No r-neighbour can lie strictly past a
first Q-contact on an unbranched stem, since its suffix would preserve
that earlier contact and lose at most the other label.

This is a working reduction, not a construction completing the residue.
In particular moving an A-connector across the stem must retain the two
owned Q contacts in a connected remainder of A. The available four or
more A-neighbours per internal stem vertex do not by themselves prove
that simultaneous retention.

Contraction-criticality does give one additional restriction here. Write
`k=|N_M(r)|`, so `d_G(r)=k+4`. If k were three, its neighbours on the
induced stem would contain an independent pair. The third Q label misses
both vertices, giving an independent triple in `N_G(r)`. This contradicts
Dirac's bound `alpha(G[N(r)]) <= d_G(r)-5=2` for a seven-contraction-critical
host. Thus this common-stem residue has `d_G(r)>=8`. This does not
exclude it or justify restarting the degree-seven argument at r.
