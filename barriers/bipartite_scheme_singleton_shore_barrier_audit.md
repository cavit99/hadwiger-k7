# Independent internal audit: both root shores may require expansion

**Status:** separate internal mathematical audit; 4 September 2026.
**Verdict:** GREEN for the stated unbounded barrier theorem.
This is an internal agent audit, not external peer review.

## Exact revisions

Audited [theorem](bipartite_scheme_singleton_shore_barrier.md), whole-file SHA256:

```text
456b9ea984326cee119843a8d5d1d9dda51c0307604727bfab3c3af0ab01d1bf
```

Read and rerun the [certificate checker](../active/experiments/bipartite_contractibility/singleton_shore_obstruction.py),
whole-file SHA256:

```text
9e360f5f751a2b0086cbf5c7b08ecd38f1bd2743d19fdbb697fe0b0b2e93aa16
```

## Independent proof checks

1. For every `n>=3`, each displayed path has ten distinct vertices and
   alternates its endpoint colours. Its nine edges occur in no other path.
   Nonroot vertices of type `x,X` occur on two paths and have degree four;
   types `Y,Z,y,z` occur on `n` paths and have degree `2n`. Intersecting
   paths share the endpoint named by the common vertex's colour. Counts
   `2n^2+6n` and `9n^2` are correct.
2. If every `a_i` is singleton, each opposite branch set must meet every
   `N(a_i)`. These are disjoint sets of order `n`. There are exactly `n`
   opposite branch sets, so each takes exactly one vertex of each set.
   This exhausts all `X` vertices, even when colour mixing is permitted.
3. Fix an opposite branch set. Its `n` selected `X` vertices have neighbours
   only in `S={Y_i,Z_i}` and the unavailable `a_i` roots. Every `Z_i` has
   at most two selected `X` neighbours, and every `Y_i` at most one.
   There are no edges inside `S`.
4. The remainder of the branch set is nonempty because it contains its
   prescribed `b` root. Identifying that entire remainder to an auxiliary
   vertex preserves connectedness even if the remainder is disconnected.
   The proof correctly makes no claim that this is a minor operation.
   After deleting loops and repeated edges, each selected `S` vertex has
   degree at most two, and every edge is incident with `S`.
5. With `s` selected vertices of `S`, this connected auxiliary graph has
   `n+s+1` vertices and at most `2s` edges. Therefore `s>=n`. Disjointness
   of the `n` branch sets requires `n^2` vertices of `S`, exceeding `2n`
   precisely in the stated range. Reversing the paths and interchanging
   uppercase and lowercase symbols proves the opposite-shore assertion.
6. The diagonal prefixes and suffixes are connected disjoint five-vertex
   branch sets containing their roots. All required adjacencies are the
   edges `Y_i y_j`. Thus the host itself has the claimed rooted model.

## Reproduction and trust boundary

Ran the checker through the project environment with `--order 3`, `4`
and `5`. All checks passed, giving graph orders `36,56,80` and edge counts
`81,144,225`. Both obstruction certificates and the explicit rooted models
were verified. These runs check the construction, not an exhaustive search
over branch sets; the written counting proof establishes the exclusion
for every `n>=3`.

No unresolved mathematical gap was found. The theorem refutes singleton
roots on an entire shore in the original scheme graph, including both
complete-colour and terminal-only projected-tree variants. It does not
refute bipartite contractibility, models expanding both shores, or a rooted
reduction whose subsequent lifting expands original roots. It proves no
statement about T44, Conjecture 21, `HC_7` or comparative significance.
