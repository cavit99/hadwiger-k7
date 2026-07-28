# Internal audit: seven-cut component contraction under `K_7^-` exclusion

Audited file: `results/hc7_k7minus_seven_cut_contraction.md`.

Audited SHA-256:

```text
3a746698ba61603ccbdc236d79afd5a4ba1f860c84a987b168f25cd962a00586
```

**Verdict:** **GREEN** for the exact revision above.

This is a separate internal mathematical audit, not external peer review.
The cold audit checked this revision, including the seven-vertex
ten-edge lemma, by reconstructing its proof and by an independent exhaustive
scan of all labelled seven-vertex graphs.

## 1. Full component neighbourhoods and the quotient

For every component `C_i` of `G-S`, its neighbourhood is contained in the
seven-set `S`.  If it missed a boundary vertex, that neighbourhood would be
a cut of order at most six separating `C_i` from another component.
Therefore `N(C_i)=S`.

Contracting the components produces exactly

\[
                              I_r\vee G[S].
\]

No adjacency between contracted component vertices is introduced, and all
boundary adjacencies are retained.

For any seven-vertex graph `R`,

\[
                  \kappa(I_r\vee R)=
                  \min\{7,r+\kappa(R)\}.
\]

A cut smaller than seven must delete every independent join vertex and then
disconnect `R`; deleting all seven vertices of `R` supplies the other cut.

## 2. Finite core constructions

Every case in Claim 2 was reconstructed.

- For `r=2`, five-connectivity gives at least eighteen boundary edges,
  safely above Mader's `K_5`-minor-free maximum of fifteen.  A `K_5` model
  and the two independent join vertices give `K_7^-`.
- For `r=3`, four-connectivity gives at least fourteen edges.  At fourteen,
  the complement is `C_7` or `C_3 dotcup C_4`, and all adjacencies among
  the five displayed branch sets check.  At fifteen, the deletion-pair sum
  is `10*15=150`, so a five-vertex remainder has at least eight edges and
  hence a `K_4` minor by Mader's sharp bound.  The three remaining
  apex-containing bags form an actual `K_7` with it.
- For `r=4`, the breadth-first count in minimum degree three and girth at
  least six is valid: the two endpoints of an edge, four first neighbours,
  and eight distinct forward neighbours would require fourteen vertices.
  A cycle of length at most five leaves two vertices for the two merged
  join bags; contracting the cycle to a triangle gives the other three
  bags.  Only the two pure join vertices may be nonadjacent.
- The `r=5` and `r>=6` constructions use respectively two pure join
  vertices, three or four merged join-boundary bags, and two adjacent
  singletons or one further boundary singleton.  Bag counts, disjointness,
  connectivity, and all required adjacencies are correct.

These constructions justify `r<=5` and, through the connectivity formula,
`kappa(G[S])<=6-r`.

The separate seven-vertex lemma was also checked case by case.  Avoiding
`K_4^-` makes the maximum-degree vertex's neighbourhood induce a matching,
and avoiding `K_{2,3}` limits every anti-neighbour to two contacts there.
The degree-four and degree-three counts exhaust all remaining cases and
force a house, `K_4^-`, or `K_{2,3}`.  An independent scan of all
`2^21` labelled graphs, treating these as not necessarily induced
subgraphs, found maximum edge count exactly nine when all three are
excluded.  This computation is corroboration; the written degree proof is
the logical basis of the claim.

## 3. Sharper boundary conclusions

For `r=2`, any boundary `K_5` model combines with the two pure contracted
components to give `K_7^-`.

For `r=3`, a literal boundary `K_4^-` combines with three merged component
bags.  A house and `K_{2,3}` each contract to `K_4^-` on five vertices,
leaving two boundary vertices for two merged bags and one pure component
bag.  These constructions verify the bound of nine boundary edges.

For `r=4`, a boundary path `x-y-z`, three additional boundary vertices,
one pure contracted component, and three merged component-boundary bags
give seven branch sets missing at most the adjacency `xz`.  Thus the
boundary contains no path of length two and has maximum degree at most one.

For `r=5`, any boundary edge supplies the two adjacent singleton bags in
the explicit construction.  Hence the boundary is edgeless.

## 4. Published input and trust boundary

The only external facts are Mader's sharp `p=4,5` minor extremal bounds

\[
                    (p-2)n-\binom{p-1}{2},
\]

with the correctly cited 1968 source.  All other minor models are explicit;
no computation is used.

The theorem does not say that component contraction preserves
seven-connectivity.  Instead it proves that preservation would force the
forbidden minor.  It supplies no strict density-preserving descent and does
not prove the global `4n-5` extremal target.
