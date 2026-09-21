# Finite probes of the two-helper candidate

**Status:** unpromoted computer-assisted finite evidence, 21 September 2026.
These probes preceded the [written theorem](../results/five_root_one_missing_contact.md)
and are not inputs to its proof. They do not prove Conjecture 21 or HC7.
The completion criterion remains HC7 or an original
result of comparable significance to Norin–Totschnig.

The retained [script](hc7_c21_helper_search.py) searches for seven disjoint,
nonempty connected bags, five containing their prescribed individual roots
and two avoiding all roots, with at least ten of the eleven root–helper and
helper–helper contacts. It also checks the stated 4-light condition over
**every** nonempty nonroot subset.

## Exact finite coverage

Every graph with five roots and **at most four nonroots**, satisfying
4-lightness and `rho4 >= 2`, passed the exact model search. Root–root edges
can be omitted: they contribute neither to `rho4`, to the lightness test,
to connectivity of a bag containing exactly one root, nor to a required
contact. The enumeration retains labelled nonroots and represents root
incidences up to permutation of the five roots. Thus the counts below are
representative instances, not counts of pairwise nonisomorphic graphs.

| Nonroots | All possible eligible rho values | Density-eligible instances | 4-light instances, all with models |
| --- | --- | ---: | ---: |
| 2 | 2–3 | 4 | 4 |
| 3 | 2–6 | 217 | 204 |
| 4 | 2–10 | 50,808 | 48,919 |

Zero or one nonroot cannot have `rho4 >= 2` in a simple graph. The three-
nonroot invocation below allows excess through ten, but values above six
are empty.

For each candidate helper pair, the solver enumerates all connected bags
containing one prescribed root and no other root, and solves their disjoint
packing problem. A candidate root bag may be discarded only if a contained
candidate uses no more vertices and misses no more helper contacts. The
helper pair is arbitrary among all disjoint connected nonroot subsets;
vertices may remain unused. Each returned model is checked separately with
explicit vertex sets, connectivity, ownership, disjointness and contacts.

A second solver independently enumerates assignments of each nonroot to
one of the seven bags or to an unused class. The two algorithms agreed on
105 fixed-seed examples with two through four nonroots. Positive and
negative sanity examples also check the contact threshold. The documented
[star-replacement graph](../barriers/five_root_star_replacement.md) has
`rho4=2` and passes lightness; its contracted graph has the independently
expected violating two-vertex subset of excess one.

## Selected larger probes

Two deterministic random runs used exactly `rho4=2`, three through eight
nonroots, and four internal graph families: random trees, cycles, arbitrary
random graphs, and two cliques sharing one vertex.

| Seed | Generated instances | 4-light instances, all with models |
| --- | ---: | ---: |
| 21092026 | 2,000 | 1,941 |
| 2109202602 | 20,000 | 19,502 |

These are selected probes, with possible repeated graphs. They establish no
coverage beyond their generated inputs and provide no evidence of a
counterexample. In particular, a surviving candidate does not validate any
contraction, induction-class closure or model-lifting step.

The `star` mode is a retained exploratory check of the small four-spoke
lemma considered during the construction: it checks all admissible `H,X,Z`
with `5 <= |H| <= 8`, `|H|+|X| <= 8`, independent `X`, non-X degree at least
four, X-degree at least `5-|X|`, and five-set `Z` containing X. It finds a
Z-rooted `K1,4` with centre root outside X in all 27,598 admissible triples.
This census is **not needed as a proof input**: a subsequent elementary
component argument proves the stronger range `|H|+|X| <= 9`.

## Reproduction

From the repository root:

```sh
UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache uv run python3 active/hc7_c21_helper_search.py sanity
UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache uv run python3 active/hc7_c21_helper_search.py exhaustive --nonroots 2 --max-excess 3
UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache uv run python3 active/hc7_c21_helper_search.py exhaustive --nonroots 3 --max-excess 10
UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache uv run python3 active/hc7_c21_helper_search.py exhaustive --nonroots 4 --max-excess 10
UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache uv run python3 active/hc7_c21_helper_search.py random --trials 2000 --seed 21092026
UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache uv run python3 active/hc7_c21_helper_search.py random --trials 20000 --seed 2109202602
UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache uv run python3 active/hc7_c21_helper_search.py star
```

The main solver uses the Python standard library. The optional `star` census
also invokes the installed nauty `geng` executable. Expected outputs contain
the counts above and no `COUNTEREXAMPLE` entry; sanity reports `pass`.
