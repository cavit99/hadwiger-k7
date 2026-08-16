# Internal audit: *Every `K_{2,n}` is contractible*

**Verdict:** GREEN.

**Status:** DRAFT; ready for independent specialist review, not submission.

**Audited manuscript:** [`main.tex`](main.tex), dated 16 August 2026.

**Manuscript SHA-256:**
`8d1db4f812e805f0b50e2c1e8e4a5c01d87e909c0d671a5117a3347512c95a36`

**Bibliography SHA-256:**
`3253b5cdb49ad44b438cfcc095015df3a82ffd4eab12d39b6c9061802eeb5c35`

**Built PDF SHA-256:**
`43ece4082c7be634b28cb2701c0748e5a9adcb256547575af7e1a103f7b4e931`

These hashes identify the exact source, bibliography and inspected PDF.
This is a separate internal mathematical audit, not external peer review.

## 1. External inputs

The proof uses two published inputs.

1. Kündgen, Pelsmajer and Ramamurthi, Lemma 3.3 and Remark 3.2(1),
   (2) and (7): an `H`-scheme reduces to a coloured `H`-scheme in a
   root-preserving minor; colours alternate; every underlying edge belongs
   to one scheme path; and a degree-two root colour lies on both incident
   paths.
2. Edmonds' matroid union rank formula for two matroids on a common ground
   set.

Kündgen, Pelsmajer and Ramamurthi's Lemma 2.2 supplies the final subgraph
corollary.  Their Theorem 6.2 and Question 8.2 support the historical
statements in the introduction.

## 2. Proof check

For each of the two distinguished colour classes, every non-root leaf-colour
vertex defines one edge of an auxiliary multigraph.  Remark 3.2(7) puts that
vertex on both relevant scheme paths, so the two auxiliary multigraphs have
the same labelled edge set.  Suppression gives a family of paths through the
corresponding distinguished root.  The paths cover every auxiliary vertex,
and every non-root auxiliary vertex lies on at least two of them.

For an edge set `X`, counting incidences between these paths and the
components of the spanning subgraph on `X` gives

```text
c_j(X) <= |E-X|/2 + 1.
```

Adding the two inequalities is exactly the rank condition in Edmonds'
matroid union formula.  The union rank is the sum of the two graphic ranks,
and equality forces the two representing independent sets to be disjoint
bases.  They are therefore spanning trees of the two auxiliary multigraphs.

Lifting a selected auxiliary edge through its labelled scheme vertex makes
each distinguished branch set connected.  Disjoint tree labels keep the two
branch sets disjoint, while each degree-two root is a singleton adjacent to
both.  These branch sets give the required rooted `K_{2,n}` minor.  Composing
with the root-preserving reduction returns the model to the original scheme
graph.

The argument also covers `n=1`: the auxiliary multigraphs then have one
vertex and empty spanning trees.  Empty leaf-colour sets and trivial
projected paths are allowed explicitly.

## 3. Claim boundary

The manuscript proves that every `K_{2,n}` is contractible and, by subgraph
closure, that every bipartite graph with a part of order at most two is
contractible.  It does not claim publication priority, settle the `K_{3,3}`
part of Question 8.2, or prove that every bipartite graph is contractible.
The proof is unbounded and computation-free.

## 4. Editorial and build checks

The manuscript follows the repository's live `amsart` paper style and uses
British spelling throughout.  It has four letter-size pages and about 1,300
LaTeX-source words.  `latexmk` completed without undefined citations,
undefined references, box warnings or PDF-string warnings.  All fonts are
embedded.  Every page was rendered at 140 dpi and inspected; there is no
clipping, overlap or illegible material.

Independent human specialist validation remains necessary before
submission.
