# Internal audit: degree-seven clique incidence under `K_7^-` exclusion

**Verdict:** GREEN.

**Audited theorem SHA-256:**
`8378b1920987284abf3ff33d476d28efee5c9a13659afe7a192febaacb3d501f`.

This is a separate internal mathematical audit, not external peer review.

## Hypothesis matching

The theorem states seven-connectivity explicitly.  Its chromatic assumptions
are exactly those required by the two repository inputs.  Exclusion of a
`K_7^-` minor implies exclusion of a `K_7` minor, so the non-`K_7` outcome of
Theorem 3.5 in the matching-language result is available.

The dependency revisions checked were:

| result | SHA-256 |
|---|---|
| degree-seven anti-neighbourhood connectivity | `a73429c60377546d55f9578a7795eb45634a98fdc87d84604ee62865880a90f3` |
| exact matching languages and rooted-model theorem | `7fda58a909aabf5a49c32be513ebc598695c448855a4a8bede3ae1efdc63314a` |

The first makes `G-N[v]` nonempty and connected.  With
`a,b` a boundary nonedge, Theorem 3.5 of the second supplies five disjoint,
connected, pairwise adjacent bags rooted at `N(v)-\{a,b\}`.

## Local proof check

Dirac's inequality gives `alpha(G[N(v)])<=2`.  If the seven-vertex
neighbourhood `H` were `K_4`-free and had maximum degree at most three,
its complement would be triangle-free with minimum degree at least three.
The five-cycle and seven-cycle incidence counts exclude every odd cycle,
so the complement is bipartite.  Its part sizes are three and four, forcing
a `K_4` in `H`.  Hence `Delta(H)>=4`.

A maximum-degree vertex cannot be universal by `R(3,3)=6`.  After choosing
a nonneighbour, it contacts at least four of the five remaining roots.  The
seven displayed branch sets therefore miss at most one required adjacency.
Zero missing adjacencies gives `K_7`, which also contains `K_7^-`; one gives
`K_7^-` directly.  No branch set is reused.

## Trust boundary

The theorem does not address degree-eight vertices and does not prove the
`K_7^-` six-colour conjecture.  The optional seven-vertex census is not a
dependency.
