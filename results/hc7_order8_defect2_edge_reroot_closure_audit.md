# Independent internal audit of the defect-two rerooting closure

**Verdict:** **GREEN** for the exact theorem revision

```text
be6b422467b4e6e640f0c00c068d0379893c92913a7467d5f40067a590a9e3ae  results/hc7_order8_defect2_edge_reroot_closure.md
```

This is a separate internal mathematical audit, not external peer review.
Three cold checks independently examined the rerooted vertex partition,
the generic selected-response hypotheses, the two connected-subgraph
witnesses and the final defect-profile exhaustion.  No unresolved
assumption or gap remains at the stated scope.

## 1. Audited inputs

The proof composes the following promoted results at their current
GREEN-audited revisions:

```text
e689c96686a936c27e58c2cba22d699c62ad649092eebfcdfc9c5db95a8e7b5a  results/hc7_generic_exact7_response_restart.md
f9af9b8edc55af116151cc7c7e3b4d30532fb44c338faee6239b888f36297feb  results/hc7_singleton_exact7_terminal_normal_form.md
9fa601e3e8a1d29dc9de239029809379e92b9187750034d590ea4989dad48667  results/hc7_order8_nearfull_edge_triangle_closure.md
```

The first source supplies Definition 1.1 and Lemma 1.1, the second supplies
the packing-one conclusion in Theorem 2.1, and the third supplies the
defect-at-most-one closure in Corollary 6.2.

## 2. Exact rerooted partition

Let the defect-two endpoint be `v`, with other endpoint `w` and missed
vertices `r,s`.  Collective `S`-fullness of the two-vertex component forces
the edges `wr,ws`.  Because `G-N[u]` has exactly the two components `E,F`,
the endpoint `v` has no neighbour outside its mate and the old boundary.
Therefore

\[
 N_G(v)=\{w\}\mathbin{\dot\cup}(S-\{r,s\}),
 \qquad d_G(v)=7.
\]

For the new boundary `T=N_G(v)`, deletion of the closed neighbourhood of
`v` leaves exactly

\[
                         G[F\cup\{u,r,s\}].
\]

This graph is nonempty and connected: `F` is connected and meets `r`, and
the edges `ur,us` join both old missed vertices through `u`.

## 3. Generic response and packing contradiction

The partition with operated shore `{v}`, boundary `T` and opposite open
shore `G-N[v]` satisfies the generic exact-seven definition literally:
the operated shore is connected, both open shores are nonempty and
anticomplete, `T=N_G(v)` has order seven, and `vw` is a selected crossing
edge.  Every proper minor is six-colourable, so a six-colouring of `G-vw`
exists.  Lemma 1.1 supplies the required legal/rejected boundary response;
no order-eight colour label or operation provenance is silently retained.

The singleton theorem consequently gives packing number one on the new
anti-neighbourhood.  On the other hand,

\[
                        G[F\cup\{r\}],\qquad G[\{u,s\}]
\]

are vertex-disjoint connected subgraphs there.  For each vertex of
`S-{r,s}`, the first has a contact through the `S`-full component `F` and
the second through `u`.  At `w`, their contacts are the edges `wr,ws`.
Both subgraphs are therefore full to `T`, contradicting packing number
one.  Their possible adjacency is irrelevant: the packing theorem requires
vertex-disjointness, not anticompleteness.

## 4. Exhaustion and trust boundary

For either endpoint `x`, componenthood gives

\[
                             d_G(x)=9-|\Delta_x|.
\]

Seven-connectivity forces \(|\Delta_x|\le2\).  The promoted near-full theorem
excludes the case in which both defects have order at most one, while the
new rerooting theorem excludes every remaining profile.  Thus Corollary 3.1
eliminates the entire aligned two-vertex exterior-component branch.

The proof does not force an aligned component to have order two, treat a
different small-shore shape, close the minimum-boundary two-full-component
interface, prove the general bounded-interface composition theorem, or
prove `HC_7`.  The optional seven-vertex one-anchor census is not used and
creates no computational dependency for this result.
