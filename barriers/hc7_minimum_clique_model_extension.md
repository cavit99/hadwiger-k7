# A minimum K6 model can conceal every useful extension

**Status:** explicit counterexample with a written proof and a
[separate internal audit](hc7_minimum_clique_model_extension_audit.md).
No computation or external existence theorem is a premise.
Put `Q=K7−2K2`, with independent missing edges.

## Exact failure

There is a six-connected graph F containing K7 as a minor such that, for
**every** K6 model minimising the number of used vertices:

1. no bag can be split into two connected bags giving Q while the other
   five bags remain fixed;
2. every component outside the model contacts exactly four model bags.

Thus no tie-break among minimum models, including minimising the sum of
squared bag sizes, guarantees either a split or an exterior component
contacting five bags. The construction does not refute the unrooted
six-connected K6-to-Q conjecture. It requires an extension to leave the
minimum used vertex set; it does not exclude such an extension.

## A locally planar six-connected graph

Let R have vertex set `Z_1320 × Z_22`, with edge differences
`±(1,0), ±(0,1), ±(1,1)`. The sixty vertices `(22j,0)`, `0≤j<60`,
have pairwise graph distance at least 22: their first coordinates have
cyclic distance at least 22, and each edge changes that coordinate by
at most one.

The graph R is six-connected. After deleting at most five vertices,
choose an untouched row and column. Their union is a connected
backbone. Any other component avoids that row and column and their
adjacent rows and columns, since those vertices have neighbours on the
backbone. Cutting along the backbone therefore lifts such a component
to a finite set X in the triangular lattice, with all its lattice
neighbours representing distinct actual torus vertices. There are at
least six outside neighbours: two above a highest-row vertex, two below
a lowest-row vertex, one left of a leftmost-column vertex and one right
of a rightmost-column vertex. The last two lie between the extreme rows,
so all six are distinct. All would have to be deleted, a contradiction.

Every connected subgraph of R on at most 21 vertices is planar. Lift a
spanning tree to the triangular lattice. Each remaining edge closes a
fundamental cycle of length at most 21, less than either torus period;
its two coordinate increments are therefore zero, rather than nonzero
multiples of those periods. The lift is consistent on every edge and
embeds the subgraph in the planar triangular lattice.

## Construction

Let S be the once-subdivided K6, with original vertices `v_0,…,v_5`
and subdivision vertex `z_ij` on each edge `v_i v_j`. Thus `|S|=21`.
For each four-subset U of `{0,…,5}`, let S_U be its once-subdivided K4,
and take a disjoint copy R_U of R. Join each of the ten vertices of S_U
to six private vertices from the displayed sixty in R_U, using every
one exactly once. Add no further edges. This defines F on 435,621 vertices.

To check six-connectivity, delete a set Z of at most five vertices.
Every R_U remains connected, and every surviving vertex of S_U retains
a neighbour in R_U. At least one original vertex survives. All surviving
original vertices belong to one component: any pair lies in a common U.
Every R_U containing a surviving original vertex joins that component.
If all four original vertices indexed by U were deleted, at most one
further vertex was deleted. Choose a surviving `z_ab` with `a,b∈U`, and
a surviving original `v_c`. A four-set V containing `a,b,c` gives the
connection `R_U–z_ab–R_V–v_c`. Thus every R_U is in the same component.
Every remaining subdivision vertex retains a neighbour in one of them.
This proves that F is six-connected.

## Every minimum model is confined to S

Consider any vertex set Y of size at most 21. Each component of
`F[Y∩R_U]` is planar and contains at most one attachment vertex, by the
distance bound. It therefore meets the remainder of `F[Y]` through at
most one edge to a single vertex of S. These are planar pendant pieces.
A clique minor of order at least three cannot straddle a one-vertex
separation: bags avoiding the separating vertex on opposite sides would
be nonadjacent. Trimming such pieces shows that any K6 minor of `F[Y]`
must have a model in `S[Y∩S]`.

Every K6 model in S uses all 21 vertices. A bag containing no original
vertex is a singleton subdivision vertex and has at most two contacts,
so each bag contains one of the six original vertices. Such a bag is a
star consisting of its original vertex and incident subdivision vertices.
The contact between the bags containing `v_i,v_j` requires `z_ij`; hence
all fifteen subdivision vertices are used. Conversely, assigning each
subdivision vertex to either endpoint gives a K6 model on all of S.

It follows that every minimum K6 model in F has union exactly S and
has these star bags. Any connected split of a star has a singleton leaf
on one side. That leaf contacts only one of the other five old bags,
so the split cannot give Q. Moreover R_U contacts exactly the four bags
whose original vertices are indexed by U: every subdivision vertex of
S_U belongs to one of those same bags. These are all exterior components.

## The host nevertheless contains K7

With indices modulo six, put `U_i={i,i+1,i+2,i+3}` and
`B_i={v_i}∪V(R_U_i)`. These six sets are connected and disjoint. For
each pair i,j, either `j∈U_i` or `i∈U_j`, giving their required contact.
Choose `T={0,1,3,4}`, which differs from all six U_i, and put

`D=V(R_T) ∪ {z_ab : a,b∈T}`.

The set D is connected and avoids every B_i. Since `|T∩U_i|≥2`, a
subdivision vertex indexed by a pair in this intersection belongs to D
and has a neighbour in R_U_i. Thus D contacts every B_i, giving K7.

This counterexample concerns the two stated terminals for minimum
models. Its explicit K7 minor rules out treating it as a counterexample
to C19, HC7 or the unrooted augmentation candidate. In particular a
successful argument may enlarge or replace the original model.
