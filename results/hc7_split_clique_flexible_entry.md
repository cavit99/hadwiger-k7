# A flexible fixed colour class in the split-clique neighbourhood

**Status:** written proof with a
[separate internal audit](hc7_split_clique_flexible_entry_audit.md). This gives an
unconditional entry to a two-root list obstruction in the selected
neighbourhood case. It does not close that case or prove `HC_7`.

## 1. Statement and notation

Let G be a finite simple graph which is not six-colourable, whose every
proper minor is six-colourable, and which has no K7 minor. Suppose
`N_G(u)=P dotunion D`, where P induces a triangle, D induces a four-clique,
and P is anticomplete to D. Seven-connectivity is not needed below.

There are `p in P` and an independent set `B={p} union I`, where
`I subseteq V(G)-N_G[u]`, with the following properties. Put

`A=P-{p}={a,b}`, `K=G-({u} union B)`,

and let X be the component of `K-D` containing the edge ab.

1. K has two proper five-colourings, both assigning colour i to `d_i`
   for `D={d_1,d_2,d_3,d_4}`. One gives a colour five and the other gives
   b colour five. In each colouring the other A vertex has a colour in
   `{1,2,3,4}`. Both colourings extend to G-u by giving all of B colour six.
2. Every proper five-colouring of K uses all five colours on `A union D`.
3. Define lists on X by

   `L(v)={1,2,3,4,5}-{i:vd_i in E(G)}`,

   and additionally delete colour five from L(a) and L(b). The list
   instance `G[X],L` is uncolourable. Every inclusion-minimal induced
   uncolourable subgraph Z contains both a and b, is connected, contacts
   every vertex of D, and satisfies `d_Z(v)>=|L(v)|` for every `v in Z`.

The input for the minor constructions is the
[audited bipartite contractibility theorem](bipartite_contractibility_via_matroid_reduction.md).
The argument that a list obstruction contacts all four roots adapts the
[three-contact proof](hc7_split_clique_three_contact.md) to a
subgraph which need not be a component of `K-D`.

## 2. Choosing a flexible deleted class

Choose any `p in P`, six-colour the proper minor G/up, and give its
contracted vertex colour six. Expand the quotient colouring to a proper
colouring c of G-u by giving p colour six. Its sixth colour class B is
independent, meets `N_G(u)` only at p, and is anticomplete to p outside p.
In particular `B-{p}` lies in the exterior.

The restriction to `K=G-({u} union B)` is a five-colouring. Every
five-colouring of K must use five colours on `A union D`: otherwise
restore B in colour six and give u a missing colour. Normalise D to
colours one to four. Since A is an edge, write its vertices as
`a_5,b_j`, with `j in {1,2,3,4}`. Thus c has root colours

`p_6,a_5,b_j,d_1,d_2,d_3,d_4`.

If K has a five-colouring fixing D in which a avoids five, then b has
five, and this colouring together with c gives the required pair.
Suppose instead that a has colour five in every such colouring of K.

For each i, a and d_i are in one component of the graph induced by
colours five and i in K. Otherwise exchange those two colours on the
component containing a. This fixes D and gives a colour i, contrary to
the assumed forced colour. Choose a simple a--d_i path in each layer.

Let B* be the entire colour-five class of c, and put
`K*=G-({u} union B*)`. This class is independent and meets `N_G(u)` only
at a. The remaining palette is `{1,2,3,4,6}`, and every colouring of K*
using this palette and fixing D must give p or b colour six, by the
same extension argument.

If p had colour six in every such colouring of K*, then for each i the
same component exchange would force a p--d_i path in the six--i layer
of the original colouring c. Together with the four a--d_i paths these
would form a K2,4 scheme with shores `{a,p}` and D. Indeed, its six
roots have different colours; each path uses only its endpoint colours;
and the colour of any common vertex identifies a root incident with
every target edge whose path contains that vertex. No other root can be
internal to a path. All paths avoid u.

Bipartite contractibility supplies the six disjoint prescribed-root
bags. The actual edge ap and the actual edges of D give the contacts
within the two shores. The six bags are therefore a K6 model, and the
singleton bag `{u}`, adjacent to every prescribed root, completes K7.
This contradicts the hypothesis.

Consequently K* has a colouring fixing D in which p avoids six and b
has six. Together with c restricted to K*, this is the desired pair
for the deleted class B*. Rename the deleted vertex a as p, interchange
colour names five and six, and rename the other two P vertices as a,b.
This proves assertions 1 and 2. No comparison of colourings of distinct
minors or edge-response assumption is used.

## 3. The minimal list obstruction

Suppose X had an L-colouring. Retain either chosen five-colouring on
`K-X`. Every neighbour of X outside X lies in D, and the lists enforce
properness across that boundary. This would five-colour K with only
colours one to four on `A union D`, contrary to assertion 2. Hence an
inclusion-minimal induced uncolourable Z exists.

If a were absent from Z, restrict the five-colouring in assertion 1
which gives a colour five and b another colour. It respects all lists
on Z. The other colouring handles the absence of b. Thus `A subseteq Z`.
Disconnected Z would have an uncolourable component, contradicting
minimality. If `d_Z(v)<|L(v)|`, an L-colouring of Z-v would leave an
available colour at v, again a contradiction. These prove all asserted
properties except the four contacts.

Call a colouring of `G[Z union D]` compatible if it uses colours one to
five and gives d_i colour i. Such colourings exist by restricting either
chosen colouring of K. Every compatible colouring uses colour five at
one of a,b, since otherwise its restriction to Z would be an L-colouring.

Suppose Z misses some vertex of D. In a compatible colouring write
the two A colours as five and j. If Z missed `d_i` with `i != j`,
interchange five and i on all of Z. This is still compatible: Z has no
neighbour at d_i, and the other fixed D colours are unchanged. Neither
A vertex would then have colour five. It follows that Z misses exactly
one D vertex, namely d_j, and that every compatible colouring gives A
precisely the pair of colours five,j.

Relabel j as four, put `Q=D-{d_4}`, and choose one of the two original
G-u colourings, naming the A vertices `a_4,b_5` in this paragraph. For
each `q_i in Q`, there are a--q_i and b--q_i paths in `G[Z union Q]`
using colours four,i and five,i, respectively. Otherwise interchanging
the component containing the corresponding A vertex gives a compatible
colouring of `G[Z union D]` whose A colours are not precisely four,five.
The fixed Q root of colour i is not in that component, and Z has no
edge to d_4, so the exchange fixes all D colours.

In the original G-u colouring, p and q_i are joined in the six--i
layer for every `i in {1,2,3}`. If not, exchange the component containing
p. The boundary `N_G(u)` has only p in colour six and only q_i in
colour i. The exchange would leave colour six absent from that boundary
and hence six-colour G. Choose these three paths simple.

The resulting nine paths lie in `G-{u,d_4}` and form a K3,3 scheme
with shores P and Q: their prescribed roots have six distinct colours,
each path uses only its endpoint colours, and each common vertex has
the colour of a shared endpoint. Bipartite contractibility therefore
gives six disjoint rooted bags. The literal P and Q triangle edges
complete K6, and `{u}` completes K7, a contradiction. Thus Z contacts
all four vertices of D.

The six paths inside Z were forced by the list obstruction itself.
Their component exchanges are only tests of compatible colourings of
`G[Z union D]`; they are not asserted to extend through `X-Z`. The
three paths from p use one actual colouring of the entire original G-u.
This distinction permits the extraction even when Z is a proper subset
of X.

## 4. Exact remaining obligation

The construction is available without a two-exception edge response.
It supplies two whole-K colourings with the same deleted class, and it
places every four-clique contact inside a minimal list obstruction.
It does not supply an edge h for which the entire `X-h` is L-colourable,
or an original-host edge-deletion colouring preserving this class.

In particular an L-colouring of Z-v need not extend through `X-Z`.
Contracting Z does not preserve its lists or the chosen exterior
colouring, and Z is not claimed to inherit minor criticality. No
reduction to a smaller induction instance has been made. Closing the
whole case still requires a six-colouring of G or seven compatible
connected bags in the original G, with all omitted vertices and
boundary constraints accounted for.
