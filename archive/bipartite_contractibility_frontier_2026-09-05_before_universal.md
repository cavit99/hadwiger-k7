<!-- Frozen snapshot before promotion of universal bipartite contractibility on 5 September 2026. Contemporary status assertions below are historical; current status belongs only to ../RESEARCH_LEDGER.md. Relative links have been adjusted for this archive location. -->

# Bipartite graph contractibility frontier

**Status:** conjectural target; no proof of the universal statement.
This is the sole primary research target following the user-authorized
4 September 2026 pivot. The authoritative status is the
[research ledger](../RESEARCH_LEDGER.md).

## Target

> Every finite simple bipartite graph is contractible: for every such graph
> `H` and every `H`-scheme in a finite graph `G`, there is an `H`-minor in
> `G` rooted at the designated vertices of `H`.

An `H`-scheme consists of one path `P_uv` for each edge `uv` of `H`, with
ends `u,v` and no other root internally; any collection of paths with a
common vertex has a common endpoint in `H`. A rooted minor is a family of
pairwise disjoint connected sets `C_v`, each containing its designated
root `v`, with `C_u` adjacent to `C_v` for every edge `uv` of `H`.

It suffices to prove the target for every `K_{n,n}`. Every finite bipartite
graph embeds as a subgraph of some `K_{n,n}`, and contractibility is
subgraph-closed by Kündgen--Pelsmajer--Ramamurthi [1, Lemma 2.2]. This is
an unbounded target, not an assertion derived from finite searches.

## Direct proved inputs and first missing steps

The [audited even-subdivision theorem](../results/even_subdivision_contractibility.md)
proves the target whenever one bipartition class has maximum degree two.
Its component-incidence argument packs disjoint spanning trees in a family
of graphic matroids: each nonroot vertex used as an edge label occurs in
at most two projections, and every component away from its root meets at
least two projected paths.

For a general coloured bipartite scheme, label sets must instead be
defined by actual membership in the scheme paths. A vertex of colour `b`
need not lie on every path incident with `b`. At degree three a label may
occur in three projections. The proved component bound is still one half
of the deleted-label incidence count; it no longer implies the matroid
union inequality. Keeping all vertices of each `A` colour in its named
branch set, and every `B` root singleton, is an additional restriction.
Its failure would not refute rooted contractibility.

The [degree-three theorem](../results/degree_three_bipartite_weak_contractibility.md),
with its [separate GREEN audit](../results/degree_three_bipartite_weak_contractibility_audit.md),
now proves a stronger conclusion with fewer prescribed roots: if every
vertex of `B` has degree at most three, every scheme contains an `H` minor
retaining all original `A` roots. Thus every such target, including every
`K_{3,n}`, is weakly contractible. This is an unbounded terminal theorem.

Its recursive step moves a `B` root to a nonroot lying on all its incident
paths, truncates those paths, and deletes the old root. Other paths avoid
the new root; the abstract target and every `A` root are preserved. Host
order strictly decreases. When no such vertex remains, every `B` nonroot
has exactly two path memberships, so actual-membership packing applies.
The original `B` roots are not preserved by this argument.

The [audited root-forcing reduction](../results/bipartite_weak_to_rooted.md)
proves that universal weak and universal rooted bipartite contractibility
are equivalent. Pendant four-cycles of different multiplicities force an
unrooted model of an enlarged target to respect every original root.
The enlarged target depends on the host and can have arbitrarily large
degrees. Therefore the degree-three theorem does not supply the universal
weak hypothesis of this reduction.

The principal new proof possibility is universal weak contractibility
with roots allowed to move, followed by the proved root-forcing reduction.
After removing vertices lying on every path at their colour, the first
case beyond the degree-three theorem has a nonroot on three of the four
paths incident with its colour. Moving that root then requires a new
connection for the fourth path; it is not the proved truncation step.
The full six-root `K_{3,3}` problem remains a separate useful diagnostic.
Neither bounded path lengths nor bounded host order settle either route.

## Audited obstruction to keeping one shore singleton

**Barrier/counterexample to an intermediate claim:** the
[written construction](../barriers/bipartite_scheme_singleton_shore_barrier.md)
and its [separate internal audit](../barriers/bipartite_scheme_singleton_shore_barrier_audit.md)
prove that, for every `n>=3`, a coloured `K_{n,n}`-scheme on `2n^2+6n`
vertices has a rooted model but no model in which either entire root shore
is singleton. This allows arbitrary colour mixing and unused vertices.
Thus neither a more favourable global orientation nor replacing spanning
trees by trees connecting only required terminals repairs that strategy.
The displayed successful model expands roots on both shores.

The first false inference would be to require a singleton shore as a
normal form for all coloured schemes. A smallest useful repair must
allow expansion on both shores, or supply a root-preserving reduction
whose lift does so. The construction refutes neither repair and is not a
counterexample to the primary target.

## Two uniform cases and a failed induction

**Written deduction from the audited packing lemma.** Suppose a coloured
bipartite `H`-scheme has every nonroot on one host bipartition in exactly
two scheme paths. It has a rooted `H` minor, even if those target colours
have degree greater than two. To see this, form the same projections, but
label an edge by a nonroot only when it actually lies on the corresponding
path. Each label occurs in exactly two projections; the projected paths
partition the labels, cover the colour class, and every nonroot of the
other shore lies on at least two projected paths. All hypotheses of the
audited packing lemma hold. This is a scheme-specific deduction, not
contractibility of an additional target class.

**Written deduction from matching.** If every nonroot of each colour lies
on every path incident with that colour, any bipartite target also has a
rooted model. Choose a minimum vertex cover `W` of the target and let
`S=V(H)-W`. A maximum matching saturates `W` and matches its vertices to
`S`: its size is `|W|` by König's theorem, and covering every matching edge
with exactly `|W|` vertices forces exactly one cover vertex on each edge.
For each matching edge `sw`, put `V(P_sw)-{s}` in `C_w`, and leave roots
in `S` singleton. The matching paths are disjoint, each `C_w` contains
all vertices of colour `w`, and every edge incident with `S` is witnessed
at its root. If both ends of a target edge lie in `W`, its scheme path is
covered by their two branch sets and supplies a contact. Isolated roots
are retained. This also follows from the complete-support specialization
of [1, Lemma 6.1]. The unproved case mixes partial and full path support.

**Recorded negative finding / route nonclosure.** A proposed induction
splits off one path through a degree-six nonroot, obtains a rooted model
in the new graph, and replaces its virtual edge by the original two-edge
path. The last step need not preserve disjointness. For an explicit example,
take roots `v,w,b_0,b_1,b_2` and nonroots `x,z,y_0,y_1,y_2`, with paths
`v y_j x b_j` and `w y_j z b_j` for `j=0,1,2`. This is a coloured
`K_{2,3}`-scheme. Split off `y_j x b_j` to the edge `y_j b_j` and let
`{j,k,l}={0,1,2}`. In the split graph the branch sets

`C_v={v,y_k}`, `C_w={w,y_l}`, `C_bj={b_j,y_j}`,
`C_bk={b_k,x}`, `C_bl={b_l,z}`

are connected, disjoint, and have all required adjacencies. Restoring the
virtual edge inside `C_bj` would reuse `x` from `C_bk`. There is an
obstructed returned model for each split choice. This does not refute an
existential choice of a liftable split and model: the original graph is
contractible. The smallest repair is a joint split-and-model existence
lemma with a proved exchange resolving this conflict. Choosing a split,
then an arbitrary model, is a different quantifier order.

Splitting a triple intersection into pair intersections using only its
three original paths is not a coloured-scheme reduction either. Every
replacement vertex shared by at least two of those paths has their common
root colour; proper colouring forbids an edge joining two such vertices.
With no other paths and every replacement nonroot shared, the three
segments must still pass through a single common vertex. A monochromatic
chain merely contracts back under coloured normalization. A successful
replacement must alter additional paths or prove a global recolouring.

A target perfect matching supplies disjoint scheme paths, and each other
scheme path meets only matching paths sharing one of its endpoints.
However, splitting each selected matching path once between its two roots
is an extra requirement on a rooted model. No proof was found that
optimizing lengths among the supplied matching paths makes that requirement
sufficient. The missing step is a joint rerouting of the selected paths
and the rest of the scheme preserving every root-to-root requirement and
the common-endpoint intersection condition. Individual path shortening
without that preservation is not a well-founded scheme reduction.

## Literature and odd-path-strip attempts

**Written deduction and audited barrier to a proposed proof.**
Biswal--Lee--Rao [2, Lemma 3.2] state that an integral flow for any
bipartite demand graph of minimum degree two forces that graph as a minor
if paths for independent demand edges do not intersect. Under this
intersection convention the flow is a scheme: pairwise intersecting
edges in a bipartite graph have a common endpoint, and a root internal
to a nonincident path would, by its degree at least two, create an
independent-edge intersection. Conversely a scheme has no such
intersections. Together with root forcing, the universal flow assertion
would prove the primary target. It is not a weaker substitute for it.

The [audited seven- and eight-vertex constructions](../barriers/bipartite_flow_prefix_construction.md)
refute intermediate Lemmas 3.5 and 3.6 of the supplied prefix proof.
One proposed branch set is disconnected in the first example; two
proposed branch sets overlap in the second. Both hosts have explicit
rooted `C_4` models. The first unsupported inference excludes a suffix
vertex from another prefix at the same root. No counterexample to the
intended main minor statement is established.

The final JACM PDF was also checked: the same prefix argument appears on
p. 13:11. Its preceding display reverses the intersection wording; the
construction note explicitly distinguishes that apparent typographical
error from the substantive failures under the intended arXiv v2 convention.
No corrected proof was found in the bounded search. The external main
statement is therefore not used as a verified proof input here.

This does not invalidate spectral or separator conclusions. For example,
[Bonnet et al., Lemma 2 and Appendix B](https://arxiv.org/html/2512.01587v1#A2)
give a separate transfer for specially chosen twice-subdivided clique
demands, and [Kolbe--Spalding-Jamieson, Proposition 3.4](https://arxiv.org/html/2608.27179)
use a separate local-lemma construction. Those special demand families
do not settle universal bipartite contractibility. The new degree-three
theorem is an independent proof; priority remains qualified because the
broader BLR assertion was already published.

**Recorded negative findings / route nonclosure.** Reducing an odd target
path by suppressing two of its internal roots does produce a smaller
scheme, but ordinary contractibility of that smaller target gives no
preservation of the removed roots on the required connection. Thus this
is not a proved reduction of the odd-theta question to the even-subdivision
theorem. A direct cover-and-matching construction works for odd strips
with one nonroot per internal colour; no reduction of arbitrary multiplicity
to that case was obtained, and no new target contractibility is claimed.

Fleiner's [Theorem 6.3](https://egres.elte.hu/tr/egres-01-01.pdf), pp. 16--17,
on matroid kernels was checked as a possible exchange tool. It supplies
ordered matroid spanning, not connected sets at specified roots or the
ordered internal roots of a strip. The first unsupported inference would
be to treat root-connected support choices as the matroidal choice needed
there, or to lift a kernel while silently retaining those root conditions.
A specifically defined encoding and a rooted lifting theorem are still
required. No application of Fleiner's theorem is promoted here.

## Finite diagnostics

The [experiment description](../active/experiments/bipartite_contractibility/README.md)
records a deterministic 30-sample search using variable path supports and
lengths. Every sampled scheme had an independently checked rooted model.
There is no exhaustive or unbounded conclusion. The actual obstacle is
still construction for arbitrary schemes, not a lack of small examples.

## External inputs and search boundary

- [1, Lemma 3.3] permits root-preserving reduction to a coloured scheme.
  Its paths alternate endpoint colours and are edge-disjoint, and every
  nonroot lies on at least two paths [1, Remark 3.2].
- `K_{3,3}` is already weakly contractible [1, Theorem 5.3]. The new
  degree-three theorem retains any one of its prescribed shores, but the
  full rooted diagnostic still requires all six original roots.
- Every bipartite graph is already `M'`-contractible [1, Corollary 7.6].
  Thus the model having one additional vertex of each colour and all
  paths of length three cannot refute the target. A useful hostile search
  must permit varied colour multiplicities and longer paths.
- The full target addresses [1, Section 8, Question 4]. A proof would still
  require independent specialist assessment of novelty and significance;
  it has no proved implication to T44, Conjecture 21 or `HC_7` here.

## Completion standard

A positive completion is a proof constructing the rooted model for every
finite scheme, with every reduction preserving its exact hypotheses and
strictly decreasing an explicitly stated well-founded parameter. A negative
completion is an explicit valid scheme and a rigorous certificate that its
host has no prescribed rooted model. An obstruction to a restricted
packing method is recorded only as a barrier to that intermediate claim.
Further normal forms alone do not meet the intended research standard.

## Preserved work

- [Minimal manuscript of the even-subdivision theorem](../paper/even-subdivision-contractibility/main.tex).
- [T44 technical frontier](../active/hc7_k44_closure_frontier.md): a preserved
  conditional route, with local residues, induction-class closure and
  nonliteral branch-set preservation still open.

## References

[1] A. Kündgen, M. J. Pelsmajer and R. Ramamurthi, *Finding minors in graphs
with a given path structure*, Journal of Graph Theory 79 (2015), 30--47,
[primary preprint](https://arxiv.org/pdf/1207.6141),
[DOI](https://doi.org/10.1002/jgt.21812).

[2] P. Biswal, J. R. Lee and S. Rao, *Eigenvalue bounds, spectral
partitioning, and metrical deformations via flows*, Journal of the ACM
57(3) (2010), Article 13, [DOI](https://doi.org/10.1145/1706591.1706593),
[primary preprint, v2](https://arxiv.org/pdf/0808.0148v2).
