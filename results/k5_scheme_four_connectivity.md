# Closing the rainbow three-cut in a rooted K5 scheme

**Status:** written proof with two separate internal reviews recorded in
the adjacent audit. This closes the separator case below; it does not
prove K5 contractibility or the project's global objective.

All graphs are finite and simple. We use the properly coloured K5-scheme
definition and minimum-order convention of the
[separator theorem](../active/k5_scheme_separator_reduction.md). Its five original
roots have colours `a,b,c,d,e`; every demand path has its endpoint colours,
contains no other root internally, and the host is the union of the paths.

## 1. Statement and pinned inputs

**Theorem.** A minimum-order properly coloured K5-scheme without a fully
rooted K5 minor has no three-cut. Consequently every such counterexample
is four-connected.

By the separator theorem it suffices to exclude its sole remaining state:
`S={s_c,s_d,s_e}` is a rainbow three-cut containing no original root;
`G-S` has two components, with roots `R={c,d,e}` in a component `D`
and roots `a,b` in the other component. Write `J=G[D union S]`.

The inputs used here are the following written proofs and their separate
internal audits. The first input supplies only the already proved
separator normal form, not the theorem of this file.

| Input | Source SHA-256 | Adjacent audit SHA-256 |
| --- | --- | --- |
| [Separator theorem](../active/k5_scheme_separator_reduction.md), Sections 1–6 | `5d7dc02cc98cd96817f0919e46212a27cc3831c67a7b84cb950aebedcca4cf96` | `679e9a0efa4f9b57168c4111bb5aee804db6b4570a4979b5d78d70b9f52b18f3` |
| [Independent-set reduction](general_scheme_independent_set_reduction.md), Lemma 1 | `07fa0fc58284dba6f5ab180a64e92dd86f3829fd31494b8529f00fcaf7751e9f` | `f3b8137aec93dbf618a3c19a6f97b17fbb46a386a16cc7e6c9581927e271b76f` |
| [Matroid-union equality](bipartite_contractibility_via_matroid_reduction.md), Lemma 1 | `3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272` | `1c8ed74e98829690dc4c1fd6d44631454d330443dd33faea4435d35beb5cca06` |
| [Two full regions theorem](two_full_regions_paired_triangle.md) | `7659e3472a9710eed5e7e059c71ba9af4922f4bacd49bf66048c7df6a5078766` | `15eb754137fd49895a63210ca658c47ae8057f60a4d9d29a8be388d97d215f06` |

## 2. The six strands and the first rank inequality

For each `i in {c,d,e}`, the paths `P_ai,P_bi` have unique `s_i`-to-`i`
suffixes in `J`: `s_i` is their only possible boundary vertex. Call these
six paths `Q_i^a,Q_i^b`, oriented from `i` to `s_i`. They use only their
displayed two colours. Put `T=T_a union T_b`, where `T_a,T_b` are the
vertices in `D` of colours `a,b`, and write `n=|T|`.

Every vertex of `T` lies on at least two of its shore's three strands.
Indeed every nonroot of a minimum counterexample belongs to at least two
demand paths, and `P_ab` cannot enter `D`, since `S` has neither colour.
Also `T` is independent in the full host: an `a`–`b` edge would belong
to `P_ab`, and same-colour edges are absent.

Let `C_i` be the colour-`i` vertices used by the six strands. It includes
the two terminals `i,s_i`. Put

`E=(C_c union C_d union C_e)-(R union S)`, and `m=|E|`.

Vertices used only by the three triangle demands are not counted in `m`.
They will remain in the original graph throughout the final construction.
The forward projection on `C_i` has an edge labelled `t in T` between
its two neighbours on the appropriate strand. Each label occurs at most
once in that projection. The projection is connected: it is the union
of two projected `i`–`s_i` paths. Its rank is `|C_i|-1`, so the sum of
the three ranks is `m+3`. These are exactly the nonzero projection ranks
for the independent set `T` in the full K5-scheme. The independent-set
reduction and minimum order therefore give

`n < m+3`.                                                    (1)

## 3. Reverse packing and the full-region terminal

On vertex set `T_a`, form the reverse projection `M_a`: an occurrence
of `x in E` on an `a`-strand gives an edge labelled `x` between its two
`a`-neighbours. Define `M_b` similarly. A label occurs at most once in
each graph; absence means a loop in its graphic matroid. Deleting the
two terminal vertices of a strand and suppressing its internal C vertices
gives a nonempty projected path. The three such paths cover each `M_h`.

Each `M_h` is connected. Every component containing a vertex contains
at least two whole projected strands, because that vertex has at least
two strand memberships. Two different components would thus require
at least four of the three strands. The total reverse rank is `n-2`.

If disjoint forests attain this rank, each is a spanning tree of its
projection. Its base vertices together with its allocated actual labels
give a connected set in `J`. The two sets are disjoint, avoid `R union S`,
and each is adjacent to all six terminals through their strand-end edges.
Three disjoint `R`–`S` paths exist in `J`: apply three-connectivity of `G`
and truncate paths at their first visits to `S`. The two full regions
theorem gives three disjoint pairwise adjacent bags in `J`, each containing
one original root and one port. Their pairing may be permuted.

Replace `D` by the triangle on `S`. Together with the outside `a,b` path
and the six outside root-to-port prefixes, this gives a properly coloured
K5-scheme on a strictly smaller host, rooted at `a,b,s_c,s_d,s_e`.
Minimum order supplies its rooted model. Replace each port by its fixed
bag in `J`; all three added edges lift to actual bag contacts. An added
edge cannot be needed inside a branch set, since its ends are different
prescribed roots. The five lifted bags retain all five original roots.
Thus full reverse packing is terminal.

## 4. A deficient reverse packing forces single intervals

Suppose instead that the maximum reverse packing size `q` is less than
`n-2`. Choose an inclusion-maximal minimizing set `X subseteq E` in the
matroid-union formula. Put `Y=E-X`, and let `k` be the total number of
components of `M_a(X)` and `M_b(X)`, including isolated base vertices.
The formula gives

`q=|Y|+n-k < n-2`, hence `k>|Y|+2`.                           (2)

Every `y in Y` joins different components in BOTH projections. Adding
`y` to `X` changes the union expression by `-1+delta_a+delta_b`, where
each rank increment is zero or one. An increment sum zero contradicts
minimality; sum one contradicts maximality of `X`. Thus both are one.

Intersect a projection component with each of its three projected
strands. A strand is split into exactly `|Y cap C_i|+1` maximal component
intervals: its Y-labelled edges cross components, and its X-labelled
edges stay inside components. Summing over all six strands gives exactly
`2|Y|+6` intervals. Every component meets at least two different strands,
so it contributes at least two intervals. Consequently

`2k <= 2|Y|+6`.

Together with (2), this forces `k=|Y|+3`. EVERY component meets exactly
two strands, in one interval in each. Moreover every one of its original
base vertices lies on BOTH strands, since it has at least two memberships.
Thus either of the two intervals contains all base vertices of the
component. Its full original strand segment has two distinct ends in
`Y union R union S` and only own-colour X vertices internally besides
those base vertices. Distinctness follows from simplicity of the strand.
Also `X` is nonempty: otherwise `k=n` and `Y=E`, contradicting (1).

## 5. Forward forests lifted directly to the original graph

Compress each interval only as auxiliary path data. Its component is a
label `K`; its two ends define an edge in a forward graph `N_i` on
`(Y cap C_i) union {i,s_i}` whenever that component supports strand `i`.
Each `K` is a nonloop in exactly two graphs. Each `N_i` is connected,
being the union of the two compressed `i`–`s_i` paths. Hence

`sum_i rank(N_i)=|Y|+3=k`.

Matroid union supplies a nonempty set `W` of component labels and disjoint
forests `F_i subseteq W` spanning every component of `N_i(W)`. If the
maximum packing is `k`, take all labels as `W`; otherwise take a minimizing
set, which is nonempty since its expression is less than `k`. Every label
is a nonloop somewhere, so the total forest rank on this `W` is positive.

For each component of `N_i(W)`, start with its actual C-coloured vertices.
For each allocated edge `K in F_i`, add the ORIGINAL colour-`i` strand
segment represented by that edge. These sets are connected: the forest
edges have been replaced by actual paths. Crucially, the segment contains
ALL original `a`- or `b`-base vertices of `K`. It contains no other C colour.

Sets for different `i` are disjoint. Their base vertices come from
different allocated labels, and their C vertices have different colours.
Sets for the same `i` may overlap in X vertices; merge intersecting sets.
The resulting connected sets still contain at most the one original root
of their C colour. Contract them to their own C colour. Retain every other
original C vertex, including all unclaimed X vertices and every vertex
used only by triangle demands. For a label `K in W` not allocated to any
forest, delete its original base vertices. Base vertices of labels outside
`W` remain individually in their original `a` or `b` colour.
All vertices outside these specified contractions and deletions are otherwise
unchanged.

This is an actual root-preserving minor operation in the ORIGINAL host;
the auxiliary compression is not asserted to be an intermediate minor.
At least one forest edge has positive rank and lifts to a path with two
distinct C ends and a nonempty set of base vertices. Thus order strictly
decreases, even after merging intersecting same-colour sets.

## 6. All ten original demands survive

On a cross-strand of colour pair `h,i`, consider any label `K in W`
supporting it. Its one whole interval has ends in the same component of
`N_i(W)`, so the lifted forward forest identifies those ends, regardless
of which forest owns `K`. Omit that entire interval. This omits every
deleted base vertex and every base vertex recoloured to a foreign C colour.
The single-interval property ensures there are no other occurrences of
those base vertices on that strand. Outside these omitted intervals,
base vertices retain colour `h` and original C vertices retain colour `i`.
Every surviving step is an actual edge between the relevant preimages.
The untouched outside prefix therefore completes an endpoint-coloured
walk for each of the six cross-demands.

The three C-triangle paths contain no `a` or `b` vertex. Every one of their
vertices was retained or contracted to its OWN C colour; hence each also
survives as an endpoint-coloured walk, including any outside excursion.
The `a,b` path avoids `D` and is untouched. Contract any remaining
monochromatic edges if necessary, and erase closed excursions from all
ten walks. Roots of different colours never merge, and no resulting path
contains a foreign root. Their common vertex colour certifies the entire
scheme intersection condition. We have a smaller properly coloured
K5-scheme with fixed disjoint connected preimages for all original roots.
Any rooted model there lifts by those preimages, contradicting minimum
order. This closes the deficient reverse case and proves the theorem.

No step assumes a universal raw-strip dichotomy whose full-region outcome
would have to lift across expanded terminals. The two possible conclusions
used here are an actual full-region terminal in the original host, or a
strictly smaller original-root-preserving K5-scheme. The case of a
four-connected minimum counterexample remains open.
