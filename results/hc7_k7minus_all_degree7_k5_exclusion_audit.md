# Internal audit: all-degree-seven `K_5` exclusion

Audited file:
`results/hc7_k7minus_all_degree7_k5_exclusion.md`.

Audited SHA-256:

```text
e2e5f5dc6c4456413e306c7844771157c5f3d9663553c1170e33a298a8148bf5
```

**Verdict:** **GREEN** for the exact revision above.

This is a separate internal mathematical audit, not external peer review.
It reconstructed the private-triangle theorem from its stated hypotheses,
checked every Kempe interchange and clique recolouring, verified both
explicit `K_7^-` branch-set constructions, and checked the all-degree-seven
and tight-layer corollaries.

## 1. Scope and exact dependencies

Theorem 1 uses only:

- `chi(G)=7`, hence `G` is not six-colourable;
- six-colourability of the private-edge deletion `G-a_ix`;
- a literal `K_5` `A`;
- the five triangular external neighbourhoods `T_a=N_G(a)-A`; and
- connectedness of `G-A`.

It does not use density equality, a second literal `K_5`, the former
equality-host matching and overlap structure, five-connectivity after clique
deletion, Hall's theorem, or finite enumeration.  The proof needs only the
one selected edge deletion to be six-colourable, although the proper-minor
hypothesis is natural for the critical-host application.

Theorem 7 uses the audited exact degree-seven neighbourhood theorem at
SHA-256

```text
04e085032a096ef3fd508ca4ee287ef82417a718ae3d95646ae4cbd0b911ed2e
```

Corollary 8 additionally uses the audited three-literal-`K_5` exclusion at
SHA-256

```text
5b5e399122b996186e861f5075e7808c8e6fe4353082256ee12d5074499d2574
```

The latter theorem's non-two-apex hypothesis follows from `chi(G)=7`: a
two-apex graph is six-colourable by the Four Colour Theorem and two fresh
colours on the deleted vertices.

## 2. Initial colouring and the edge-critical fork

Deleting `a_ix` produces a proper minor, so the selected six-colouring
exists.  Its endpoints must have the same colour `p`; otherwise restoring
the edge would colour `G`.  The clique `A` uses five distinct colours.  If
its absent colour `q` did not occur on `T_{a_i}`, assigning `q` to `a_i`
would be legal.  Thus the triangular palette is exactly `\{p,q,r\}`.

For a fixed `a_j`, if either `p` or `q` were absent from `T_{a_j}`, assigning
that colour to `a_j` and `c_j` to `a_i` would give five distinct available
clique colours and make the restored edge proper.  Hence both colours occur.

If the component `P_j` of `H[p,c_j]` containing `x` missed `T_{a_j}`, a
`p,c_j` interchange on `P_j` would remove `p` from `T_{a_i}`.  The miss
protects `c_j` at `a_j`, and every other retained clique colour lies outside
the interchanged pair.  Assigning `p` to `a_i` would therefore six-colour
`G`, proving the required reach.

If `p,q` do not both occur on `T_{a_h}`, a missing one is available there.
If some third colour `s_j` differs from `r`, then `r` is available at
`a_j`.  Assigning the missing colour to `a_h`, `r` to `a_j`, and `c_j` to
`a_i` proves the stated two-way palette fork.

In the common-palette branch, a different `p,c_j` component through the
`p`-vertex of another indexed triangle misses both `T_{a_i}` and
`T_{a_j}`.  Swapping it, assigning `p` to its owner, and assigning the
owner's old colour to `a_i` preserves all other clique colours and makes
the restored edge proper.  This checks the four-triangle reach of every
`P_j`.

## 3. Symmetric components and the common-four model

The `q,c_j` arguments for `Q_j` have the same component-disjointness and
list-availability checks.  A miss of `T_{a_j}` protects its owner colour,
while swapping the component through the unique `q`-vertex of `T_{a_i}`
removes `q` there.

For distinct indices `j,l`, the sets `P_j` and `Q_l` are connected and
vertex-disjoint because their colour sets `\{p,c_j\}` and `\{q,c_l\}` are
disjoint.  Both meet the same four private triangles, which also supply an
edge between the two sets.

If the fifth triangle misses their union, a shortest path to the union,
stopped at its first hit, has all internal vertices outside both sets.
Adding it to the hit set preserves connectedness and disjointness.  One set
then meets all five triangles and the other meets four.  Together with the
five singleton vertices of `A`, these are seven disjoint connected branch
sets with at most the one owner contact at the fifth triangle missing.
Their branch adjacency graph therefore contains `K_7^-`.

## 4. All-five-triangle reach and allocation

In the second palette outcome, every triangle has palette `\{p,q,s_a\}`.
The identities for the third colours follow because all owner edges except
`a_ix` remain present.  Failure of the common-four branch supplies an index
`u` with `s_{a_u}!=r`.

For `a_t` in `J-\{a_j\}`, a different `p,c_j` component through `p_{a_t}`
misses `T_{a_i}` and `T_{a_j}`.  Under `s_{a_t}!=c_j`, its own triangle is
also free of `c_j`; swapping and assigning `p` to `a_t` and `c_t` to
`a_i` would six-colour `G`.  The `q,c_j` proof is identical.

For `a_t=a_h`, the proof assigns the swapped colour to `a_h`, `c_u` to
`a_i`, and `r` to `a_u`.  The choice of `u` makes `r` available.  If
`u=j`, no clique vertex retains `c_j`; otherwise the component miss of
`T_{a_j}` protects it.  The component also misses `T_{a_i}`, and the
restored edge is proper.  This validates both versions of the component
reach claim.

The three occurrence counts of the `c`-colours sum to at most four, so one
colour `c_l` occurs as a third triangle colour at most once.  The union of
the other two `p`-components is connected through `x` and is disjoint from
`Q_l` by colour sets.  It meets every triangle; `Q_l` meets all but at most
one.  A nonexceptional triangle supplies their mutual edge.  With the five
owner singletons, this is again an explicit `K_7^-` model with at most one
missing adjacency.

## 5. Critical-host instantiation

If a degree-seven member `a` of an all-degree-seven clique `A` lay in a
second literal `K_5`, the exact neighbourhood theorem would make the two
cliques meet in `\{a,w\}` and give two anticomplete exclusive triples.
Both shared vertices have all their neighbours in the eight-vertex union.
If an outside vertex exists, the six exclusive vertices form a cut; if none
exists, seven-connectivity on eight vertices forces `K_8`.  Both outcomes
are impossible.

The first exact neighbourhood type therefore supplies five private
triangles.  A common vertex of `T_a,T_b` would be both adjacent and
nonadjacent to `a`, so the triangles are pairwise disjoint.
Seven-connectivity makes `G-A` connected.  Theorem 1 applies and gives the
forbidden minor.

## 6. Degree count and tight-layer conclusions

Every degree-seven vertex lies in a literal `K_5`, and there are at most two
such cliques.  Theorem 7 limits each to four degree-seven vertices, so
`n_7<=8`.  With

\[
                         s=\sum_{i\ge9}(i-8)n_i,
\]

degree summation gives

\[
                         2m=8n-n_7+s\ge8n-8,
\]

which is exactly `m>=4n-4`.

At equality, `n_7-s=8`; hence `n_7=8`, `s=0`, and the degree sequence is
`7^8 8^{n-8}`.  Both available literal `K_5`s are needed and each contains
exactly four degree-seven vertices.  Their degree-seven parts are disjoint,
so they are disjoint or meet only in their common degree-eight vertex.

For either clique, the four private triangles occupy twelve vertices and
are anticomplete to its degree-eight vertex `z`.  The four external
neighbours of `z` lie outside those triangles, giving `n>=5+12+4=21`.

## 7. Trust boundary

No unresolved mathematical assumption or recolouring gap remains in the
audited revision.  The result is unbounded and computation-free.  It proves
a critical-host density bound and exact equality structure; it does not
prove the bare seven-connected `4n-4` extremal theorem, the complete
`K_7^-` six-colour conjecture, `HC_7`, a standalone bond theorem, or two
full connected transversals.

The published inputs behind the two dependency theorems remain part of the
external specialist-review boundary.
