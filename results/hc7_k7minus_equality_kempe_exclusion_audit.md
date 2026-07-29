# Internal audit: Kempe-component allocation excludes the critical `4n-5` equality layer

Audited file:
`results/hc7_k7minus_equality_kempe_exclusion.md`.

Audited SHA-256:

```text
127bdbbf35c7048e93ac042c306165d85b348ae0b40c688fe953afd8ab17edc6
```

**Verdict:** **GREEN** for the exact revision above.

This is a separate internal mathematical audit, not external peer review.
It checked every Kempe interchange and subsequent recolouring, every claim
that a distinct bichromatic component misses a private triangle, both
explicit branch-set constructions, and the strict density corollary.

## 1. Scope and exact dependencies

The hypotheses are exactly those of the equality reduction:
seven-connectivity, seven-chromaticity, six-colourability of every proper
minor, and exclusion of a `K_7^-` minor.  Equality is assumed only after the
previously proved density lower bound has been invoked.

The principal dependency is
`results/hc7_k7minus_equality_connectivity_reduction.md` at SHA-256

```text
9a3e167b4b5be1d1ff9dbafb16a0e7ed6130fc58ad947603a246fa5022c88307
```

Its GREEN audit covers the literal `K_5` `A`, its five pairwise disjoint
private triangles, connectedness of `H=G-A`, and Proposition 9 with the exact
palettes and rooted `p,c_j` components used here.
The dependency's mathematical content is unchanged; its new revision only
records that this theorem subsequently closes the equality layer.

The density corollary also uses
`results/hc7_k7minus_five_exceptional_vertices_reduction.md` at SHA-256

```text
604d11d4276ce6a3c57a8375d702624a1c364b5123f122b7e9e3dc18d11bf8f4
```

which proves `|E(G)|>=4|V(G)|-5` under the same hypotheses.  No new external
theorem or finite enumeration enters the audited proof.

## 2. Symmetric `q,c_j` components

In Lemma 1, `Q_j` contains the unique `q`-coloured vertex of `T_{a_i}` and
that triangle contains no `c_j`.  Swapping `q,c_j` on `Q_j` therefore removes
`q` from the whole triangle.  Under the assumed miss, `T_{a_j}` is unchanged,
so its owner retains `c_j`; every other retained clique colour lies outside
the swapped pair.  Assigning the formerly absent colour `q` to `a_i` makes
the restored edge `a_ix` properly coloured `q,p`, giving the asserted
contradiction.

In Lemma 2, a distinct `q,c_j` component through `q_{a_t}` misses both
`T_{a_i}` and `T_{a_j}`.  Their unique `q`-vertices lie in `Q_j`, and their
rigid palette `{p,q,r}` contains no `c_j`.  The same palette makes
`T_{a_t}` free of `c_j`, so the swap removes `q` there.  Assigning `q` to
`a_t` and `c_t` to `a_i`, while retaining the other clique colours, is a
proper six-colouring.  Thus every symmetric component reaches all four
rigid triangles.

## 3. Common four-triangle branch

For distinct indices `j,l`, the connected sets `P_j` and `Q_l` have colour
sets `{p,c_j}` and `{q,c_l}`.  These palettes are disjoint, so the sets are
vertex-disjoint.  Proposition 9(4) and Lemma 2 put their respective `p`- and
`q`-vertices in each rigid triangle, and a triangle edge gives adjacency
between the two sets.

If the fifth triangle misses their union, a shortest path to the union,
stopped at its first hit, can be added to the hit set without destroying
connectedness or disjointness.  One resulting set meets all five triangles,
the other meets the four rigid triangles, and their original adjacency
remains.  With the five singleton bags from `A`, all branch-set adjacencies
are present except possibly the edge from the fifth owner to the set not
enlarged.  This is an explicit `K_7^-` model, or a `K_7` model containing
one, so the rigid branch is excluded.

## 4. Component reach in the all-five branch

The palette bookkeeping is exact.  Every private triangle has palette
`{p,q,s_a}`.  Its owner colour is absent, so `s_{a_h}` is one of the three
`c`-colours and `s_{a_j}!=c_j`; failure of the rigid branch gives an index
`u` with `s_{a_u}!=r`.

For `a_t` in `J-{a_j}`, a distinct `p,c_j` component through `p_{a_t}`
misses `T_{a_i}` and `T_{a_j}` because their unique `p`-vertices lie in
`P_j` and neither triangle contains `c_j`.  If `s_{a_t}!=c_j`, then
`T_{a_t}` is also free of `c_j`, so swapping removes its `p`.  Assigning
`p` to `a_t` and `c_t` to `a_i` is valid, retains five distinct available
clique colours, and makes `a_ix` proper.  The `q,c_j` argument is identical.

For `a_t=a_h`, the same swap removes `p` or `q` from `T_{a_h}`.  Assign that
colour to `a_h`, assign `c_u` to `a_i`, assign `r` to `a_u`, and retain the
other two indexed owner colours.  The choice `s_{a_u}!=r` makes `r`
available.  If `u=j`, no owner retains `c_j`; otherwise the component miss
protects `c_j` at `a_j`.  The component also misses `T_{a_i}`, so `c_u`
remains available there, and the restored edge has colours `c_u,p`.  This
checks both the `p` and `q` assertions of Lemma 4.

## 5. Allocation and the all-five branch-set model

The three counts of occurrences of the `c`-colours among the third colours
sum to at most four, so some `c_l` occurs at most once.  For the other two
indices `j,k`, the union `X=P_j union P_k` is connected because both
components contain `x`, while `Y=Q_l` is connected.  Their possible colour
sets `{p,c_j,c_k}` and `{q,c_l}` are disjoint.

On every private triangle, the third colour cannot equal both `c_j` and
`c_k`; Lemma 4 therefore puts its `p`-vertex in `X`.  Thus `X` meets all
five triangles.  The same lemma puts the `q`-vertex in `Y` except possibly
on the one triangle whose third colour is `c_l`.  Every nonexceptional
triangle supplies an `X`--`Y` edge.  With the five owner singletons, at most
one branch-set adjacency is missing, again giving an explicit `K_7^-`
minor.

## 6. Equality exclusion and strict density

Proposition 9(3) exhausts the two palette outcomes, and the preceding
constructions exclude both.  Therefore no equality host exists.  Since the
audited density theorem gives the integer inequality
`|E(G)|>=4|V(G)|-5`, excluding equality yields
`|E(G)|>=4|V(G)|-4`.

## 7. Trust boundary

No unresolved mathematical assumption remains in the stated
equality-exclusion theorem or strict density corollary.  The result does not
prove a standalone bond theorem for five-connected graphs, nor does it
literally construct two connected subgraphs each meeting all five private
triangles.  One connected set may miss one triangle.  The full critical-host
hypotheses make that missing contact harmless because a `K_7^-` model permits
one missing branch-set adjacency.  The theorem eliminates every equality
host rather than proving the wider two-transversal statement.
