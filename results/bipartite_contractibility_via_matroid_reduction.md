# Bipartite contractibility by graphic-matroid reduction

**Status:** computation-free written proof, with separate internal audits
at the exact source hashes recorded beside this file. Internal audits are
not external peer review. No implication to Hadwiger's conjecture is claimed.

All graphs are finite. The target graphs and host graphs are simple;
projection graphs may have parallel edges. An `H`-scheme with injective
root map `rho:V(H)->V(G)` consists of one simple path `P_uv` for every
`uv in E(H)`, joining `rho(u)` to `rho(v)`, containing no other prescribed
root internally, and satisfying the following intersection condition:
any collection of paths with a common vertex has a common target endpoint.

A rooted `H`-minor model consists of pairwise disjoint nonempty connected
vertex sets `C_v`, with `rho(v) in C_v` and an edge between `C_u,C_v` for
each target edge `uv`.

## Theorem

**Theorem.** Every finite simple bipartite graph is contractible: every
`H`-scheme in a finite graph `G` contains an `H`-minor rooted at every
prescribed root.

The only external theorem used is Edmonds' matroid union rank formula.
The component contraction in Lemma 2 is the main proof step.
It does not use the disputed Biswal--Lee--Rao prefix construction.

## 0. Root-preserving colour normalization

**Lemma 0.** Every `H`-scheme has a root-preserving minor with a proper
map `f` to `V(H)` fixing the root labels, in which every scheme path
uses only its endpoint colours. The minor can be taken to be the union
of those paths and the isolated prescribed roots.

**Proof.** Delete unused edges and nonroot vertices. Give each root its
own target label. For each nonroot `x`, choose as `f(x)` an endpoint
common to all target edges whose paths use `x`; the scheme condition
ensures that such an endpoint exists. Hence every path uses only its
endpoint labels. Contract each connected component induced by one label.
These components are disjoint and each contains at most one prescribed
root. Retain the resulting edges between different labels, giving a
properly coloured root-preserving minor. The image of `P_uv` is a walk
using only labels `u,v`; removing closed excursions gives a simple path
between their root images. No other root can occur, since it has a
different label. Any collection of the resulting paths meeting at a
vertex shares that vertex's label as a target endpoint. Delete vertices
and edges not used by the new paths, retaining isolated roots. QED

This is the part of [1, Lemma 3.3] needed here, proved directly without
its additional minimum-nonroot-degree normalization.

## 1. A consequence of the matroid union rank formula

Let `J` be finite. For each `j in J`, let `M_j` be a finite multigraph
with edge labels in a subset `E_j` of a common finite ground set `E`;
labels are distinct within each `M_j`. Regard its graphic matroid as a
matroid on `E` by declaring labels outside `E_j` to be loops. Write
`r_j` for its rank function. In particular, if `M_j` has vertex set `W_j`,
then

`r_j(X) = |W_j| - c_j(X)`,

where `c_j(X)` is the number of components of the spanning graph with
edge labels `E_j cap X`, including isolated vertices.

**Lemma 1.** Put

`R = max sum_j |I_j|`,

where the sets `I_j subseteq E_j` are pairwise disjoint and each is a
forest in `M_j`. There is a set `X subseteq E` with

`R = |E-X| + sum_j r_j(X)`.

For any maximizing family `(I_j)` and any such `X`, each
`I_j cap X` spans every component of `M_j(X)`.

**Proof.** The displayed minimum formula is Edmonds' matroid union rank
formula [2]. Choose a minimizing set `X` and a maximizing disjoint family
`(I_j)`. Since the family is disjoint and its members are independent,

`R = sum_j |I_j-X| + sum_j |I_j cap X|`

`  <= |E-X| + sum_j r_j(X) = R`.

Equality forces `|I_j cap X|=r_j(X)` for every `j`: each individual term
is at most its corresponding rank, and equality holds in their sum.
A forest contained in `M_j(X)` of that rank is a spanning tree in each
nontrivial component of `M_j(X)`, with isolated vertices retained. QED

No restriction on the number of graphs containing a label is imposed.

## 2. Contracting simultaneously spanned components

Suppose `H` is bipartite with parts `(A,B)`, and the underlying host `G`
is the union of an `H`-scheme together with its isolated roots. Suppose
also that a proper map `f:V(G)->V(H)` fixes the root labels and every
`P_ab` uses only colours `a,b`. These assumptions are weaker than the
usual normalized coloured-scheme assumptions: no minimum nonroot degree
is needed in this section.

For `a in A`, put `W_a=f^{-1}(a)`. Put

`E = {x in V(G): f(x) in B and x is not a prescribed root}`.

For every actual occurrence of `x in E` on `P_ab`, insert in `M_a` an
edge labelled `x` between its two neighbours on that path. Both neighbours
have colour `a` and are distinct, since `P_ab` is simple. The vertex set
of `M_a` is `W_a`. A label occurs at most once in each `M_a`: its colour
identifies `b`, and there is only one target edge `ab`.

Suppressing the internal `B` vertices of `P_ab` and deleting its terminal
root `rho(b)` gives a path in `M_a` starting at `rho(a)`. These projected
paths cover `W_a` and the edges of `M_a`. Hence each `M_a` is connected;
for an isolated target vertex it is its one-vertex graph. Every `x in E`
is a nonloop edge in at least one projection.

**Lemma 2.** Let `X subseteq E`. Suppose there are pairwise disjoint
sets `F_a subseteq X cap E_a` such that `F_a` spans every component of
`M_a(X)` and is a forest. Then `G` has a root-preserving minor `Q` that
contains an `H`-scheme. If `X` is nonempty, this minor has fewer vertices
than `G`.

**Proof.** For each component `K` of `M_a(X)`, define the following
vertex set in the original host:

`D_(a,K) = V(K) union {x in F_a: the edge labelled x belongs to K}`.

The tree of labels allocated to `K` lifts to two-edge paths through those
actual host vertices. It connects all vertices in `V(K)`, so `D_(a,K)`
is connected. This is also true for an isolated component, whose set is
its singleton vertex.

All the sets `D_(a,K)` are pairwise disjoint. Their `A` vertices belong
to distinct components of distinct colour classes, and the added `B`
vertices are drawn from the pairwise disjoint forests `F_a`, with each
label allocated to just one component. They contain no `B` root and
no `B` vertex outside `X`. Each contains at most one prescribed `A`
root, since it uses only one `A` colour and there is just one root of
that colour.

Contract each `D_(a,K)` to a vertex `d_(a,K)`, and delete every vertex
of `X` not allocated to a forest. Retain all prescribed `B` roots and
all vertices of `E-X` as separate vertices. Delete unwanted edges. In
particular, retain an edge from `d_(a,K)` to a surviving `B` vertex `y`
whenever the original graph has an edge from a vertex of `V(K)` to `y`.
Call this minor `Q`. Its vertices have the proper colouring that gives
`d_(a,K)` colour `a` and every surviving `B` vertex its original colour.
The retained edges all join opposite shores. The root of `a` is the
vertex representing its component; every `B` root is unchanged. Thus
the root map is injective, and these contractions specify a
root-preserving minor model of `Q` in `G`.

We check paths explicitly, including the use of deleted labels. Fix
`ab in E(H)` and traverse the original path `P_ab`. Map each `A` vertex
to its component in `M_a(X)`. A traversal `u x v` with `x in X` has
`u,v` in the same component, because the corresponding projected edge
has label in `X`. It can be replaced by a walk from `u` to `v` entirely
inside their allocated connected set `D_(a,K)`. This replacement uses
only the labels allocated to that component. It does not use `x`
unless `x` was allocated there, and never uses a label already allocated
to another component. After contraction the replacement is just one
vertex.

Every other step along `P_ab` is an edge from an original `A` vertex
to a surviving `B` vertex, and supplies one of the retained edges of
`Q`. Equivalently, remove the occurrences of `X` from the path, replace
its `A` vertices by component vertices, and suppress consecutive repeated
component vertices. The result is a walk in `Q` joining the new roots
of `a,b`, using only colours `a,b`. Delete closed excursions to obtain
a simple path. No other root is internal: a vertex of another `A`
root has another colour, and the only `B` root on the original walk
was its terminal root `rho(b)`.

Do this independently for all target edges. Every resulting path uses
only its endpoint colours. Consequently, paths meeting at a component
vertex of colour `a` all have common endpoint `a`, and paths meeting
at a surviving vertex of colour `b` all have common endpoint `b`.
This verifies the scheme intersection condition. The intermediate walks
before contraction need not themselves be a scheme; that is not used.

Finally, if `X` is nonempty, some label of `X` is a nonloop in a
projection, so `sum_a r_a(X)>0`. The forests have exactly this many
edges. At least one allocated edge connects two distinct `A` vertices
through its label, so at least one contracted set has at least three
vertices. All other operations are contractions or deletions. Therefore
`|V(Q)|<|V(G)|`. QED

## 3. Proof of the theorem

We use strong induction on the host order, for a fixed bipartite target
`H`. Remove isolated target vertices and their roots first, and restore
them as their original singleton branch sets afterwards. No scheme path
meets those roots. Empty targets cause no difficulty.

Lemma 0 gives a root-preserving minor with a proper colouring fixing the
roots and scheme paths using only the colours of their endpoints.
Its order is at most the original host order. It is enough to find the
required rooted model in this normalized host and compose the
root-preserving minor models.
Write `G` for this host for the rest of the induction step.

Choose the orientation `(A,B)` of a bipartition so that the number
`N_A` of nonroots with colours in `A` is at most the number `N_B` of
nonroots with colours in `B`. The bipartition can be reversed at each
induction step; no target root is moved by reversing it.

Form the projection graphs from Section 2. Their total rank is

`sum_(a in A) r_a(E) = sum_(a in A) (|W_a|-1) = N_A`,

and `|E|=N_B`. Let `R` be the maximum size of a disjoint union of
projection forests, as in Lemma 1.

If `R=N_A`, every forest in a maximizing family `I_a` must have full
rank in its projection. Define

`C_a = W_a union I_a`, and `C_b = {rho(b)}`.

The spanning trees lift to connected sets, their disjoint labels ensure
that all these sets are disjoint, and they retain every root. The last
edge of each `P_ab` joins `rho(b)` to a vertex of `W_a`, and supplies
every required target contact. This is a rooted model.

Otherwise `R<N_A<=N_B=|E|`. Choose a minimizing set `X` supplied by
Lemma 1. It cannot be empty, because the matroid union expression at
the empty set is `|E|`, which is strictly greater than `R`. For a
maximizing family `I_a`, put `F_a=I_a cap X`. Lemma 1 verifies exactly
the simultaneous spanning hypothesis of Lemma 2. That lemma supplies a
strictly smaller root-preserving minor `Q` containing an `H`-scheme.

The induction hypothesis applies to that scheme, giving a rooted `H`
model in `Q`. Lift each branch set by replacing its vertices with their
disjoint connected preimages in `G`. Connectivity, disjointness, all
required contacts and every prescribed root are preserved. Compose this
lift with the initial normalization lift. The only recursive application
uses a host of strictly smaller order, so the induction is well-founded.
This completes the proof. QED

## 4. Relation to the existing barriers and prior results

The component reduction can expand roots on one shore, and its recursive
application can reverse the orientation and expand roots on the other
shore. Thus the lifted model need not leave either entire original root
shore singleton. The construction does not assert the normal form refuted
by the [singleton-shore barrier](../barriers/bipartite_scheme_singleton_shore_barrier.md).

A discarded label is not lifted as a virtual edge through its old vertex.
Its two ends are instead connected inside a specifically allocated
component tree before contraction. This is why the reduction avoids the
ownership conflict in the previously recorded arbitrary split-and-lift
attempt.

The argument does not use a finite enumeration or the condition that each
label belongs to at most two projections. The earlier packing theorem
establishes full spanning in one step under that condition. The proposed
universal argument instead uses the matroid union minimizing set to find
a proper reduction whenever full spanning fails.

The theorem includes fully rooted `K_{3,3}`, every `K_{m,n}`, and every
finite bipartite target without a degree or path-length bound. It resolves
the bipartite existence question in [1, Section 8, Question 4] positively
for contractibility. It also covers the entire bipartite portion of their
theta-graph question. These are scope deductions, not publication-priority
claims: the broader unrooted flow assertion below was already published.

## 5. The intended bipartite-flow assertion

**Corollary.** Let `H` be a finite simple bipartite graph of minimum
degree at least two. Inject its vertices into a finite host `G`, and
choose one simple path between the terminal images for each edge of `H`.
If paths corresponding to edges with four distinct endpoints are
vertex-disjoint, then `G` contains an `H`-minor rooted at all terminal
images.

**Proof.** A pairwise intersecting family of edges of a bipartite graph
has a common endpoint: after two distinct edges `ab,ac` are chosen, an
edge meeting both but avoiding `a` would have to be `bc`, which would
form a triangle. Thus every collection of paths meeting at a vertex has
a common target endpoint. Also no terminal `rho(v)` can be internal to
a path `P_ab` for a nonincident edge. At most one of `a,b` is a neighbour
of `v`, so the degree condition gives a neighbour `w` outside `{a,b}`.
The paths `P_vw,P_ab` would then meet at `rho(v)` although their target
edges have four distinct endpoints. The chosen paths are therefore an
`H`-scheme. Apply the theorem. QED

This independently proves the intended existence assertion of
Biswal--Lee--Rao [3, Lemma 3.2], and retains every terminal. It does not
validate their prefix construction: its intermediate Lemmas 3.5 and 3.6
remain refuted by the [audited explicit examples](../barriers/bipartite_flow_prefix_construction.md).
The corollary uses the intended independent-intersection convention,
not the apparently reversed wording in the published definition.
It makes no new claim about the downstream spectral estimates.

Publication priority and significance relative to Norin--Totschnig
require separate assessment. This theorem does not prove `HC_7`, T44,
or Conjecture 21.

## References

1. A. Kündgen, M. J. Pelsmajer and R. Ramamurthi, *Finding minors in graphs
   with a given path structure*, Journal of Graph Theory 79 (2015), 30--47,
   [primary preprint](https://arxiv.org/pdf/1207.6141),
   [DOI](https://doi.org/10.1002/jgt.21812). Definitions 1.1 and 2.1 give
   the scheme and contractibility terminology; Lemma 3.3 proves a
   stronger normalization than the self-contained Lemma 0 above.
2. J. Edmonds, *Matroid Partition*, reprinted with the author's
   introduction in *50 Years of Integer Programming 1958--2008* (2010),
   199--218, [DOI](https://doi.org/10.1007/978-3-540-68279-0_7),
   [primary author text](https://www.researchgate.net/profile/Jack-Edmonds-2/publication/226200830_Matroid_Partition/links/0deec51d1e5ee4de7b000000/Matroid-Partition.pdf).
   Theorem 1 and the following matroid-partition discussion, pp. 202--203,
   give the finite matroid union rank formula used in Lemma 1.
3. P. Biswal, J. R. Lee and S. Rao, *Eigenvalue bounds, spectral
   partitioning, and metrical deformations via flows*, Journal of the ACM
   57(3) (2010), Article 13, [DOI](https://doi.org/10.1145/1706591.1706593),
   [primary preprint v2](https://arxiv.org/pdf/0808.0148v2), Lemma 3.2.
