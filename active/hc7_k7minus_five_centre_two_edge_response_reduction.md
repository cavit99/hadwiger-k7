# Two-edge response reduction in the five-centre completion

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_five_centre_two_edge_response_reduction_audit.md`](hc7_k7minus_five_centre_two_edge_response_reduction_audit.md).
This note is the bounded two-edge-deletion test requested after the
single-edge paired-donor route nonclosure.  It proves an exact response
criterion and a three-entry contraction alternative in the five-centre
equality completion.  It does not supply the required pair of edges and
does not close the two-cut branch.

## 1. Which deleted edges can support simultaneous traces?

Let `Q` be a graph which is not `q`-colourable, let `E_0` be a nonempty
edge set, and let `c` be a proper `q`-colouring of `Q-E_0`.  Write

\[
 M(c)=\{uv\in E_0:c(u)=c(v)\}.                       \tag{1.1}
\]

This set is nonempty, since otherwise `c` would colour `Q`.

For a nonempty set `A subseteq V(Q)`, put `T_A=N_Q(A)`.  Say that `A`
has the **trace induced by `c`** if `c` is proper on `Q-A`, so induces a
proper equality partition on `T_A`, but that partition does not extend to
a proper `q`-colouring of `Q[A union T_A]`.

### Theorem 1.1 (deleted-edge vertex-cover criterion)

A nonempty set `A` has the trace induced by `c` if and only if `A` is a
vertex cover of `M(c)`.

Consequently, two disjoint nonempty sets `A_1,A_2` both have that trace if
and only if every edge of `M(c)` has one end in `A_1` and the other in
`A_2`.  No three pairwise disjoint sets can all have the trace induced by
one fixed deletion colouring.

#### Proof

The only edges on which `c` can fail to be proper in `Q` are those in
`M(c)`.  Its restriction to `Q-A` is therefore proper exactly when `A`
meets every edge of `M(c)`.

In that case, suppose the induced boundary partition extended through
`Q[A union T_A]`.  Rename the colours of the extension so that they agree
with `c` on the literal boundary blocks, and glue it to `c` on `Q-A`.
This would `q`-colour `Q`, a contradiction.  Thus the trace is rejected on
the closed `A`-side.

If two disjoint sets are both vertex covers, each edge of `M(c)` must have
an end in each set.  Its two ends are therefore split between the sets.
The converse is immediate.  A two-ended edge cannot meet three pairwise
disjoint vertex covers, proving the final assertion.  `\square`

For `E_0=\{e,f\}`, the genuinely new simultaneous case is therefore not an
arbitrary pair of donors: both monochromatic deleted edges must cross the
same two donor sets.  This is the exact two-edge analogue of the cross-edge
condition in the audited single-edge paired-donor theorem.

## 2. Response signatures supplied by contraction-criticality

Assume now that `Q` is `(q+1)`-contraction-critical.  A two-edge set
`\{e,f\}` is **simultaneously contractible for this purpose** if either the
edges are disjoint, or their union is an induced path of length two.

### Proposition 2.1 (the three nonempty signatures)

For any two distinct edges `e,f`, there is a proper `q`-colouring of
`Q-\{e,f\}` with `M(c)=\{e\}`, and another with `M(c)=\{f\}`.

If `\{e,f\}` is simultaneously contractible, there is also such a colouring
with

\[
                              M(c)=\{e,f\}.            \tag{2.1}
\]

#### Proof

Colour the proper minor `Q/e` and expand its contracted vertex.  The ends
of `e` receive one colour, while the retained edge `f` is proper.  This
gives the first signature; contracting `f` gives the second.

For disjoint edges, contract both edges and expand the two contracted
vertices.  For an induced two-edge path, contract its three vertices to
one vertex and expand.  In either case, the only internal edges of a
contracted vertex set which survive in `Q` are precisely `e,f`, so the
expanded colouring has (2.1).  `\square`

If the two edges form two sides of a triangle, the double signature is
impossible: monochromatic ends on both selected edges make the retained
third side monochromatic as well.  This is the sharp reason for the
hypothesis above, and it agrees with the existing same-bag
two-critical-edge barrier.

## 3. The labelled contraction square at a five-centre two-cut

Assume the setting of the audited five-centre two-cut reduction.  Thus

\[
 S=Z\mathbin{\dot\cup}\{p,q\},\qquad |Z|=5,           \tag{3.1}
\]

the component `C` has the equal response, the component `D` has the
distinct response, and contracting `D union Z` to `x` gives a proper minor
`M_C` such that

\[
                         \chi(M_C+pq)=7.               \tag{3.2}
\]

Choose two edges `e,f` in `G[C]` which are simultaneously contractible in
the sense of Section 2.  For `I subseteq \{e,f\}`, let

\[
                         H_I=(M_C/I)+pq,               \tag{3.3}
\]

where no contraction is made when `I` is empty.  Call a nonempty `I` a
**flip** if `H_I` is six-colourable, and **stable** otherwise.

### Theorem 3.1 (exact labelled two-edge response)

For every nonempty `I subseteq \{e,f\}`,

\[
                              \chi(H_I)\leq7.          \tag{3.4}
\]

Moreover, `I` is a flip if and only if `G-\{e,f\}` has a proper
six-colouring with all of the following properties:

1. the five vertices of `Z` form one monochromatic boundary block;
2. `p` and `q` have distinct colours, both different from the colour on
   `Z`; and
3. among `e,f`, precisely the edges in `I` have monochromatic ends.

Such a colouring is obtained by aligning the modified `C`-side with an
unmodified permitted colouring of the distinct-response `D`-side.  Thus it
retains the original five-centre labels and the original pole orientation.

The family of flips is upward-closed in the nonempty Boolean square.  Hence
the complete list of possibilities is:

1. a singleton flip, after which the double contraction is also a flip;
2. both singleton contractions are stable and the double contraction is a
   flip; or
3. all three nonempty contractions are stable.

The second case is the sole genuinely two-edge response: neither edge can
reverse the pole response alone, but their common deletion can reverse it
with both edges monochromatic.

#### Proof

The graph `M_C/I` is a proper minor of `G` and is six-colourable.  Adding
the single edge `pq` raises its chromatic number by at most one, proving
(3.4).

Suppose first that `H_I` is six-colourable.  Expand every contraction in
`I`.  The edges in `I` become monochromatic; an edge of `\{e,f\}-I`
remains proper.  The simultaneous-contractibility hypothesis ensures that
no undeleted edge is hidden inside a contracted vertex set.  Since `pq` is
an edge of `H_I`, its ends have distinct colours.  Replace `x` by the five
independent vertices of `Z` on the closed `C`-side.  This gives a proper
colouring of the modified `C`-side with boundary partition

\[
                         Z\mid\{p\}\mid\{q\}.         \tag{3.5}
\]

Choose a permitted colouring of the unmodified `D`-side, which has exactly
the same boundary partition.  Permute its colour names to agree on the
three literal blocks in (3.5), and glue.  This gives the asserted colouring
of `G-\{e,f\}`.

Conversely, restrict such a colouring to the modified `C`-side, identify
the monochromatic block `Z` as `x`, and contract the monochromatic edges in
`I`.  The edge `pq` is proper by item 2, so the result is a six-colouring of
`H_I`.

If `I` is a flip and `I subseteq J`, then `H_J` is a minor of `H_I`.
Hence `J` is a flip.  The three listed patterns are exactly the upward-
closed subsets of the nonempty two-element Boolean square.  `\square`

### Corollary 3.2 (the stable entries are completion models)

Assume in addition that `G` was chosen with the fewest vertices among all
counterexamples to the `K_7^-` six-colour conjecture.  If `I` is stable,
then `H_I` is seven-chromatic and contains a `K_7^-` minor.

The model may be chosen spanning in `H_I`.  When lifted back to `M_C+pq`,
each contracted component therefore lies within one branch set.  Thus a
stable entry gives the relevant one-edge or two-edge co-bagging.  The
artificial edge `pq` and the contracted vertex `x` still have to be treated
by the audited completion-model lift; stability is not by itself a minor
model in `G`.

#### Proof

By (3.4), stability means `chi(H_I)=7`.  The graph `H_I` has fewer vertices
than `G`.  If it were `K_7^-`-minor-free, it would be a smaller
counterexample, contrary to the choice of `G`.  Hence it has the asserted
minor.

The graph `H_I` is connected.  Starting with any model, assign each
component of the vertices outside its branch sets to one adjacent branch
set.  This enlarges the branch sets to a spanning model.  In particular,
every contraction image belongs to a branch set.  Expanding its preimage
inside that branch set proves the lifting statement.  `\square`

## 4. Verdict of the bounded test

The two-edge operation does repair one defect of the single-edge donor
programme: Theorem 3.1 preserves the literal block `Z`, the two poles and
their required distinct response.  It also gives the exact new case to
seek: two cross-edges between the same donor pieces for which both
singleton contractions are stable and their double contraction flips.

It does not manufacture those edges.  Nor does a stable contraction close
the argument, because its `K_7^-` model may still use the artificial pole
edge in the surviving same-bag placement.  The bounded experiment therefore
stops at this exact alternative.  Replacing it by three donors is ruled out
for one fixed deletion colouring by Theorem 1.1; enlarging the Boolean
operation beyond two edges is not justified without a new host-level
supply theorem.
