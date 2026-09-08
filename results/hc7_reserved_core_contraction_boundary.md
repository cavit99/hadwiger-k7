# A boundary obstruction to contracting two triangle roots is terminal

**Status:** written proof; separate exact-source internal audit recorded beside it.
This excludes the specified boundary configuration, not the remaining
two-triangle case. Graphs are finite and simple, and boundaries are external.
Write Q for K7 with two independent edges deleted.

**Theorem.** Let G be seven-connected, have minimum degree at least eight,
and have no Q minor. Suppose d(v)=8 and

`N(v)=A dotcup B dotcup {x,y}`,

where A,B are triangles and xy is an edge. Write `A={a,A1,A2}` and
`B={b,B1,B2}`, with `{a,b,x,y}` inducing only xy, and put `W=G-N[v]`.
Let M be a connected set containing A1,A2, avoiding `B union {v,a,x,y}`,
and contacting each of b,x,y. Let C be a connected subset of W, disjoint
and anticomplete to M, and contacting B2. Then there is no nonempty
connected `X subseteq C` with

`N_G(X)={a,x,y,b,B1,s,t}`

for distinct `s,t in W-X`. No colouring assumption or previously retained
B-root path is needed. In particular the statement applies when C is a
connected residual component full to B behind a maximised reserved core.

## Inputs

The proof uses [the five-root degree-six theorem](hc7_five_root_degree_six.md),
source SHA-256 `289c5ad015b6c392ea69e8e26e15eba54b4eba7cb155789edd76b3dbb5c9f9a4`,
and its [separate audit](hc7_five_root_degree_six_audit.md),
SHA-256 `6f13ffd37126c78a697b5752574fe06b6fd13b68dabb0d63e4e39d76a8f1d065`.
For five roots containing a literal triangle, nonroot degree at least six
and nonroot-set boundary at least five give a rooted K5-minus-edge.
At least two triangle roots are admissible as the triangle endpoint of
the sole possible hole, whose other endpoint is a nontriangle root.

The final boundary corollary also uses
[the tight-boundary exclusion, Lemma 1](hc7_two_triangle_two_responses.md),
source SHA-256 `f190c8e63df3d12b301440280babeee611db897a5542216f2d074314fb5a6b18`,
and its [audit](hc7_two_triangle_two_responses_audit.md),
SHA-256 `e6d22369b0e860fde909aefe9e48491497769e72edfa8ff37eaa5024abb48e54`.
An exterior four-boundary in `G-v-B` containing an A vertex cannot
contain x or y. No additional external theorem is used beyond elementary
connectivity consequences and the two cited written deductions.

## Two outside configurations

Suppose X exists and put `L=G-{v,a,b,x,y}`. Deleting five vertices from
a seven-connected graph leaves a two-connected graph: deleting one more
vertex still leaves a connected graph. The sets M and X survive in L,
and `N_L(X)={B1,s,t}`. Neither s nor t lies in M, because X misses M.
Also B2 lies outside X and its boundary.

Let Z be the component of `L-(X union {B1})` containing M, and T the
component containing B2. We construct disjoint connected sets E and P,
where E contains M, P contains B2 and one port, and both avoid X and
the vertices a,x,y,b,B1. The port used by P is called s.

If Z=T, first choose a B2-to-X path with all internal vertices in C.
Such a path exists because C is connected and contacts B2. Since B2
misses X, its first contact with `{s,t}` precedes its first X vertex.
Retain the prefix through that port, calling it s. This prefix avoids
M and has no vertex in X. Next choose a B2-to-M path wholly in Z and
retain only its prefix before its first M vertex. Let P be the union
of these two prefixes and let E=M. The union is connected through B2,
avoids M,X,B1 and the five deleted vertices, and has an actual edge to
E. It may contain t; this causes no problem in the packet below.

Suppose instead Z and T are different. Since `L-B1` is connected,
every component of `L-(X union {B1})` contains s or t: otherwise it
would have no edge to X or any other surviving component. Thus there
are exactly two components, each containing one port. Relabel so that
`s in T` and `t in Z`. Let E be the component of `Z-t` containing M.
Its actual L-boundary is contained in `{t,B1}`. Indeed it has no edge
to X, since the only possible outside endpoints were B1,s,t. The
two-connectivity of L therefore forces E to contact B1. Choose a B2-to-s
path P wholly in T. Then E and P are disjoint and avoid X,B1 and the
five deleted vertices. In this case E is not required to contact P.

In both cases E contains M, so it contacts a through the A triangle,
contacts b,x,y by hypothesis, and has a v neighbour. In the first case
it also contacts P; in the second it contacts B1.

## The fresh packet and its original-host lift

Use the five disjoint connected root preimages

`{b}`, `{B1}`, `P`, `{a}`, `{x,y}`,

with P labelled B2. Retain the literal B-triangle edges, whose third
endpoint lies in P, and contract P and xy. The nonroots are exactly X.
Retain their induced edges and their boundary edges to a,x,y,b,B1,s;
omit all X--t edges, even if t belongs to P. All other vertices outside
the five root preimages and X are absent from this auxiliary graph.

Every X vertex loses at most two neighbours: one from omitting t and
one from identifying x,y. Thus its auxiliary degree is at least six.
For every nonempty `Y subseteq X`, v lies outside Y and its boundary,
so seven-connectivity gives `|N_G(Y)|>=7`. The same two operations lose
at most two boundary vertices. All other old boundary vertices are
retained distinctly, except that s is represented by its P root.
Hence every nonempty nonroot set has at least five auxiliary neighbours.
The five-root theorem applies with triangle B and other roots a,xy.

Lift its five branch sets through the fixed preimages above. They are
disjoint from E and v. The singleton v is full to all five through
their actual roots b,B1,B2,a and x, and it contacts E. The set E is
full to the a-rooted, xy-rooted and b-rooted bags. In the first case its
edge to P also gives the B2 contact, so its only possible omission is
B1. In the second case it contacts B1 and may miss only B2.

Choose an admissible B centre different from that possible omitted
root, using the theorem's two-centre conclusion. Its possible core
hole and E's possible omission have disjoint ends. The five lifted
core bags, E and v therefore form Q, a contradiction. QED

## Consequence for the proposed edge contraction

Suppose additionally that p1,p2 are distinct vertices of W outside C
and M, and `N_G(C) subseteq {a,x,y} union B union {p1,p2}`.
In `F=G[C union B union {p1,p2}]/bB1`, designate the four roots
`bB1,B2,p1,p2`. Every nonempty subset of the nonroot set C has at least
four F-neighbours.

Otherwise its boundary has order exactly three: deleting a,x,y and
identifying b,B1 can lose at most four of its seven original boundary
vertices. Equality forces all five vertices a,x,y,b,B1 onto the old
boundary, with exactly two further vertices s,t. The same holds for
any connected component X of that set, by seven-connectivity.
If one of s,t is B2, the H-boundary in `H=G-v-B` has order four and
contains a,x,y, contrary to the pinned tight-boundary exclusion.
Otherwise s,t lie in W and the theorem applies. This proves the
four-neighbour assertion.

This repairs that boundary condition only. A rooted model in F still
owns both b and B1 in its merged-root preimage; it cannot automatically
be used as a model in the original reservation that excludes b. The
remaining simultaneous allocation and the whole two-triangle case are open.
