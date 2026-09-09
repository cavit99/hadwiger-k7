# A missing pair is fixed across a Q-free transfer

**Status:** written proof with a separate internal audit. Put
`Q=K7-2K2`, with independent deleted edges. All graphs are finite and simple.
This strengthens the earlier
[missing-pair overlap](hc7_near_k7_rotation_pair_overlap.md) for the
Conjecture 19 target. It does not prove that conjecture.

## 1. Transfers with arbitrarily many components

**Theorem.** Let `F1,...,F5,X,W` be pairwise disjoint nonempty connected
vertex sets in G. The five F sets are pairwise adjacent, and X is adjacent
to W. Let Z be disjoint from all seven sets. Suppose:

- `G[X union Z]` and `G[W union Z]` are connected;
- the exact sets D,E of F labels missed by X,W each have order two;
- Z contacts every F row whose label lies in `D union E`.

If G is Q-minor-free, then `D=E={a,b}`. All Z-to-Fa and Z-to-Fb contacts
lie in one component K of `G[Z]`. Every other Z component may be absorbed
into X while retaining its exact missing pair and its adjacency to W.
After this absorption, K is connected and contacts X,W,Fa,Fb.

**Proof.** Every component of `G[Z]` contacts both X and W, by the two
connected-union hypotheses.

If `D intersect E={t}`, choose a Z component K contacting Ft. Use

`X, W, K union Ft, Fi (i != t)`.

These are seven disjoint connected bags. The merged bag contacts X,W
through K and the four other rows through Ft. The only missing pairs
are X to the row in `D-{t}` and W to the row in `E-{t}`. Those row
labels differ, so the bags give Q.

Suppose D,E are disjoint. If distinct Z components K,L contact some
row of D and some row of E respectively, absorb K into X and L into W.
Together with the five unchanged rows these bags have at most one hole
at each enlarged centre, with different row ends. They contain Q.
Otherwise all Z components contacting a D row or an E row are the same
component K: the two nonempty families of such components cannot have
distinct members. Thus K contacts all four rows in `D union E`.
Now `X union W, K, F1,...,F5` are seven connected disjoint bags. The first
bag is full to the rows, K contacts at least four, and the two bags are
adjacent. This gives K7 minus at most one edge, which contains Q.

Consequently `D=E={a,b}`. Distinct Z components contacting Fa and Fb
would again be absorbed into different centres, leaving independent
holes. Thus the two nonempty component families are the same singleton
{K}. Every other component misses Fa,Fb and contacts X, so its absorption
preserves connectedness, the exact missing pair and the XW contact.
K still contacts both centres and both missing rows. QED

The statement covers disconnected transfers when both connected-union
hypotheses and the XW contact hold. It does not supply those hypotheses
for an arbitrary proposed exchange.

## 2. An actual separator through three whole row bags

**Theorem.** Suppose the five rows form a clique model, X,W are connected
and adjacent, disjoint from each other and the rows, and both centres
miss exactly Fa,Fb. Let K be a disjoint
connected set contacting X,W,Fa,Fb. If G is Q-minor-free, there is a
vertex `p in K` such that

`G - ({p} union the three rows other than Fa,Fb)`

has no path from `X union W` to `Fa union Fb`.
All vertices outside the displayed sets are allowed in those paths.

**Proof.** Delete the three common rows, contract X,W,Fa,Fb to four
distinct vertices x,w,a,b, and retain every other vertex and edge.
Apply the vertex form of Menger's theorem between `{x,w}` and `{a,b}`.

Two vertex-disjoint paths would use all four auxiliary vertices as
endpoints. Their interiors avoid every original row and centre bag.
Lift the paths and add each interior to its source centre. If x is
joined to a and w to b, the enlarged centres miss at most Fb and Fa
respectively; the other pairing reverses these assignments. The five
unchanged clique rows and the two enlarged centres therefore give Q.
Connectedness and disjointness follow from the two paths; the old XW
edge preserves the centre contact.

There is at least one source-to-target path through K. Hence absence of
two disjoint paths gives a separator consisting of one vertex p.
It cannot be one of x,w,a,b: after deleting any one of these, K still
joins a surviving source and target. It must lie in K, since deleting
a vertex outside K and the four auxiliary vertices leaves all four
joined through K. Thus p is an actual uncontracted vertex of G.

Any path in G avoiding p and the three deleted rows would descend to
a source-to-target walk in the auxiliary graph, contradicting this
separator. This proves the asserted separation in the full host. QED

## 3. Consequence and remaining obligation

The [single-gate rotation datum](hc7_near_k7_rotation_edge.md) satisfies
Section 1. In a Q-free host its missing pair is therefore unchanged;
along a chain with five fixed literal rows, that pair is fixed as actual
bags. Section 2 also replaces the local prescribed-pair path problem
by an unordered linkage and an actual separator. Frame-changing moves
can still change the deficient pair.

All displayed models are literal unions of disjoint host sets. The first
construction merges a row with a transfer component; the others preserve
the five row sets. They assert no transport of a six-colouring or of
additional prescribed roots inside transferred sets. No induction or
strictly decreasing model parameter is used.

The separator contains three **whole bags**, not three vertices. In a
seven-connected host it must have order at least seven, so their union
has at least six vertices; it need not give a small cut. Converting this
separation into Q still requires a justified split or transfer through
those rows, or compatible colouring information on its actual boundary.
Fixed row labels do not provide that construction.
