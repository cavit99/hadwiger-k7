# A clean response bypass at a six-vertex topological `K_5`

**Status:** written proof.  A separate audit is recorded in
[`hc7_height6_topological_clean_bypass_audit.md`](hc7_height6_topological_clean_bypass_audit.md).
This is a local operation-response theorem, not the height-six
topological-transversal theorem and not a proof of `HC_7`.

## 1. Setup

Let `G` satisfy

\[
 \chi(G)=7,
 \qquad
 \chi(H)\le 6\quad\text{for every proper minor }H\text{ of }G.
 \tag{1.1}
\]

Suppose that six distinct vertices

\[
                         a,b,c,d,e,w
\]

contain a subdivision of `K_5` whose branch vertices are
`a,b,c,d,e` and whose only subdivided segment is

\[
                              a-w-b.                  \tag{1.2}
\]

Assume also that `ab` is not an edge.  This last condition is automatic
when the subdivision is a shortest six-vertex `TK_5` in `G-P` and `P`
meets every literal `K_5` of `G`.

Put

\[
                         K=G-\{aw,wb\}.               \tag{1.3}
\]

For a colouring of `K`, record whether the ends of `aw` and `wb` have
equal or different colours.

## 2. Exact response table

### Lemma 2.1

The graph `K` has six-colourings with each of the signatures

\[
                  (=,\ne),\qquad(\ne,=),\qquad(=,=), \tag{2.1}
\]

and it has no six-colouring with signature `(ne,ne)`.

Moreover, the proper minor obtained by contracting the path `a-w-b` has
chromatic number exactly six.

### Proof

A six-colouring of `G/aw` expands to a six-colouring of `K` in which
`a,w` have equal colours and `w,b` have different colours.  Contracting
`wb` gives the opposite signature, and contracting both edges gives
`(=,=)`.  All three contractions are proper minors, so (1.1) supplies the
colourings.

A colouring with signature `(ne,ne)` would remain proper after both
deleted edges were restored, contrary to `chi(G)=7`.

Finally, if `G/aw/wb` were five-colourable, expand its contracted vertex
to `a,w,b`, leave `a,b` in the old colour, and give `w` a fresh sixth
colour.  Since `ab` is absent, this would six-colour `G`.  Thus the double
contraction is exactly six-chromatic. \(\square\)

## 3. Saturation or an exterior bypass

Fix a six-colouring `kappa` obtained from `G/aw/wb`, expanded over `K`,
and write

\[
                    \kappa(a)=\kappa(w)=\kappa(b)=0. \tag{3.1}
\]

For an alternate colour `gamma`, call a half-edge `aw` or `wb`
**`gamma`-linked** when its ends lie in one component of the subgraph of
`K` induced by colours `0,gamma`.

### Theorem 3.1 (clean topological response fork)

At least one of the following holds.

1. One of `aw,wb` is `gamma`-linked for every one of the five colours
   different from `0`.
2. There are two distinct alternate colours `i,j` and an `a-b` path `R`
   in `K-w` such that

   \[
               V(R)-\{a,b\}\subseteq
               V(G)-\{a,b,c,d,e,w\}.                 \tag{3.2}
   \]

   The path lies in the union of one `{0,i}`-component through `a`, one
   `{0,j}`-component through `b`, and at most one edge between those
   components.  Interchanging colours on the first component gives a
   six-colouring of `G-wb`, while interchanging colours on the second
   gives a six-colouring of `G-aw`.

Thus the bypass in outcome 2, both opposite one-edge responses, and all
five linkage tests come from one fixed double-contraction colouring.

### Proof

Apply the audited incident-edge saturation-or-bypass theorem to the two
edges `wa,wb`, with common endpoint `w` and nonadjacent outer endpoints
`a,b`.  For every alternate colour, at least one half-edge is linked.  It
already gives outcome 1 unless neither half-edge is linked for all five
alternate colours.

It remains to prove the extra cleanliness in outcome 2.  The vertices
`c,d,e` form a triangle and each is adjacent to both `a` and `b`.
Consequently they receive three distinct nonzero colours under `kappa`.
If `q` is one of these vertices and `gamma=kappa(q)`, then

\[
                              a-q-b                    \tag{3.3}
\]

puts `a,b` in one `{0,gamma}`-component.  Since at least one of `aw,wb`
is `gamma`-linked, `w` belongs to that same component.  Hence both
half-edges are `gamma`-linked.

Therefore a colour witnessing failure of universal linkage on either
half-edge must be one of the two alternate colours not used on `c,d,e`.
If neither half-edge is universally linked, the incident-edge theorem
chooses these two distinct colours, say `i,j`, and returns an `a-b` path
avoiding `w` from the corresponding two named bichromatic components.
Neither component can contain `c,d,e`, because their colours are the
other three alternate colours.  This proves (3.2).  The two component
switches and their opposite one-edge response colourings are exactly
those supplied by the incident-edge theorem. \(\square\)

## 4. Exact contribution and limitation

For a shortest six-vertex `TK_5`, outcome 2 is stronger than an arbitrary
rerouting: it is a response-coupled bypass whose interior avoids the whole
selected support.  It is therefore suitable input to a whole-family
exchange argument.

The theorem does not select a new two-vertex transversal, prove that the
bypass avoids other selected supports, align half-edge contractions across
several subdivisions, or increase the global pair height.  The adjacent
[static height-six barrier](../barriers/hc7_height6_topological_transversal_static_barrier.md)
shows that those global conclusions cannot follow from the small-support
family and `K_7`-minor exclusion alone.

## 5. Dependency

- [Bichromatic saturation or a bypass at two incident critical edges](hc7_shared_interface_bichromatic_bypass.md), Theorem 1.1.
