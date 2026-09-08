# Regions full to one terminal set force a paired clique

**Status:** written proof with a [separate internal audit](paired_clique_one_sided_regions_audit.md).
The theorem concerns arbitrary finite host order. The proposed paired
almost-clique conclusion with only `k-2` regions remains open.

All graphs are finite and simple. A set is **full to** R if every vertex
of R has an actual neighbour in it. A **paired clique** for disjoint
k-vertex sets R,S consists of k disjoint connected pairwise adjacent
bags, each containing exactly one R vertex and one S vertex. The pairing
is free. Write `kappa_G(R,S)` for the maximum number of vertex-disjoint
R--S paths with distinct endpoints.

The proof strengthens the [full-region theorem](paired_clique_full_regions.md)
by allowing the regions to own the S terminals and requiring fullness
only to R. It repeats the cut-chain argument with its changed endpoint
conditions, rather than assuming that a region containing a terminal is
an admissible input to the earlier theorem.

| Prior proof mechanism | Source SHA-256 | Adjacent audit SHA-256 |
|---|---|---|
| [Full-region theorem](paired_clique_full_regions.md), Sections 2--4 | `78121803cfc368cf0ff2e367d87dfc6747fbe888b0f3f5e994abdfe83ac5b8da` | `fcac8b3ce460886ed52f0862cfddac28451df6a8280bc30b06622c63119c74ad` |

## Theorem

Let `k>=2`, let R,S be disjoint k-vertex sets in G, and suppose
`kappa_G(R,S)>=k`. Suppose `H_1,...,H_(k-1)` are disjoint connected
vertex sets avoiding R, each full to R, such that

`S subset H_1 union ... union H_(k-1)`

and every region contains at least one vertex of S. Then G has a paired
clique for R,S. No connectivity assumption on the whole graph is needed.

### 1. Reductions and allowed contractions

Suppose otherwise, choosing k minimum and then `|V(G)|` minimum.
A full k-linkage uses all terminals as its ends, so it has no terminal
internally. Exactly one region contains two S vertices; all others
contain one.

A singleton region is therefore `{s}` for some `s in S`. In a fixed
full linkage let r be the R end of the path ending at s. Delete r and s.
The other `k-1` paths and `k-2` regions satisfy the smaller theorem.
Here `k>=3`, since when `k=2` the only region contains both S vertices.
The resulting paired clique together with `{r,s}` is a paired clique:
rs is an edge because `{s}` is full to R, and s sees the R vertex in
every other bag. Both reserved terminals were deleted before induction.
Thus no region is a singleton in the counterexample.

A component outside R and the regions can be absorbed into a region
it contacts. If it contacts no region, its boundary is contained in R,
and every full linkage avoids it: entering and leaving it would put an
R terminal internally on a linkage path. Delete such a component.
Consequently the regions may be assumed to cover `V(G)-R`.

Call a region edge **permitted** if it does not join two S vertices.
Contracting a permitted edge preserves the two terminal sets, with an
S endpoint, if present, retaining its name. It preserves the regions,
their S membership and their fullness to R. If a k-linkage survives,
minimum order gives the required quotient model. Its lift uses the
fixed connected two-vertex preimage; this contains at most one S vertex
and no R vertex, so all terminal ownership is preserved. Hence every
permitted contraction lowers the linkage number below k.

### 2. Separators may contain S, but never R

For a permitted edge uv in `H_j`, Menger's theorem gives a quotient
separator of size at most `k-1`. It contains the contracted vertex,
since otherwise it would give a smaller separator in G. Lifting it
gives a separator C of size exactly k containing u,v.

C meets every other region. An untouched region contains an untouched
S terminal and is full to a surviving R terminal; an R terminal survives
because u,v are outside R and only `k-2` further vertices are deleted.
That region would give a path avoiding C. The `k-2` remaining regions
use the entire remaining cut budget. Thus C has no R vertex and has
exactly one vertex in every other region. It may contain S vertices.

Fix a full linkage `P_1,...,P_k`, oriented from R to S. Each such cut
meets every path once. Each non-S region vertex has a neighbour in its
region, and its incident region edges are permitted. It therefore lies
on the linkage. The S vertices are its endpoints already, so the
linkage spans G. The ends of every permitted region edge lie on
different paths; the same holds for an S--S edge since the S endpoints
are distinct.

### 3. The cut chain with S endpoints allowed

Consider all separating vectors choosing one vertex of each path,
excluding its R endpoint but allowing its S endpoint. The all-S vector
is a member and is their coordinatewise maximum. Since the linkage
spans G, a vector separates exactly when no edge joins a strict prefix
to a strict suffix. This characterisation proves closure under
coordinatewise minimum and maximum: a crossing edge for either new
vector crosses one of the two original cuts.

Take a maximal chain of these cuts. Every region vertex appears on it.
For a non-S vertex use a permitted-edge cut containing it; for an S
vertex use the maximum cut S. If the chain skipped a position z between
consecutive cuts `C<D`, a cut Z containing z would give the strictly
intermediate cut `(Z maximum C) minimum D`. The extreme cuts rule out
skipping a position before or after the chain. A vertex's occurrence
indices therefore form a nonempty interval.

The intervals of the ends of every region edge overlap. For an S--S
edge they both contain the maximum cut S. Otherwise a permitted-edge
cut Z contains both ends. If u's last occurrence precedes v's first,
the next cut after u disappears puts u in a strict prefix. The actual
edge uv prevents v from lying in a strict suffix, so this next cut is
v's first occurrence. Projecting Z between these consecutive cuts
gives a strict intermediate cut containing both u and v, a contradiction.

Every chain cut meets every region: R is uncut, and an untouched region
contains an uncut S terminal and is full to R. With `k-1` regions and k
cut vertices, each region has at most two occurrences at any chain index.
Its interval intersection graph is a forest. Indeed, an interval on a
cycle with smallest right endpoint and its two cycle neighbours would
all contain that endpoint. The connected actual region is a spanning
subgraph of this forest, by the edge-overlap argument, so it equals the
forest and is a tree. Any two of its vertices occurring in a common
chain cut are therefore actually adjacent.

Let f_i be the first vertex of `P_i` after its R endpoint; it may be an
S endpoint. The minimum of cuts containing each f_i is
`F={f_1,...,f_k}`. Thus F is a cut on the chain. Every region neighbour
of an R terminal belongs to F: a later neighbour would lead along its
path to S while avoiding F. Exactly one region occurs twice in F and
every other region once. The two paths represented in the same region
are adjacent by the preceding paragraph. For paths represented in
different regions, at least one region occurs only once; the R endpoint
of the other path is full to it and so sees its unique vertex in F.
The k paths are pairwise adjacent, the required contradiction.

This proves the theorem. All reductions either delete explicitly
reserved terminals before decreasing k, or decrease host order with
fixed connected preimages containing at most one terminal of either set.

## Consequences and the remaining boundary

The earlier two-sided theorem follows immediately for `k>=2`: assign
the k S terminals to its `k-1` full nonterminal regions, at least one to
each, and adjoin them. Each enlarged region is connected and full to R.
The `k=1` case is simply a path.

Here is the precise one-sided construction for a terminal-containing
cut in the `k-2`-region problem. Let `k>=3`, let R,S have size k, and
let `H_1,...,H_(k-2)` be disjoint connected nonterminal regions full to
both sets, with a full k-linkage. Suppose an R--S separator is

`C={r,u,v,w_2,...,w_(k-2)}`,

where `r in R`, uv is an actual edge of `H_1`, and `w_j in H_j`.
Let A be the union of components of `G-C` containing an R vertex.
It contains all of `R-{r}` and no S vertex. Set `K=C-{r}`.
For each region retain its vertices in A and its vertices in K.
These retained sets are connected: each component of a region minus
its cut vertices attaches to a cut vertex, and in `H_1` the two cut
vertices are joined by the actual edge uv. They are full to `R-{r}`;
all neighbours there of an R vertex lie in A or K. They cover K and
each contains at least one K vertex.

The original linkage paths other than the one beginning at r, truncated
at their first C vertex, give `k-1` disjoint `R-{r}`--K paths in
`G[A union K]`. The theorem supplies a paired `(k-1)`-clique there.
Its bags have fixed disjoint preimages, each owning one old R terminal
and one actual cut port. This is a valid side replacement. It does not
by itself allocate the remaining r--S path or prove the proposed
`k-2`-region paired almost-clique theorem.
