# A `K_{1,1,3}` scheme does not reserve a second rainbow triangle

**Status:** barrier/counterexample to an intermediate claim; separate
hash-pinned internal audit **GREEN** in
[`hc7_k113_second_triangle_reservation_barrier_audit.md`](hc7_k113_second_triangle_reservation_barrier_audit.md).
This is not a counterexample to the five-centre theorem, the `K_7^-`
six-colour conjecture, or `HC_7`.

## 1. Refuted statements

Let `H=K_{1,1,3}` have singleton parts `p,q` and stable part
`{a,b,c}`.  The following proposed strengthening of contractibility is
false:

> Suppose a properly coloured graph contains an `H`-scheme on roots
> `p,q,a,b,c`, and also contains a disjoint second triangle
> `a',b',c'` in the corresponding three stable-root colours.  Then the
> rooted `H`-minor may be chosen so that its stable branch set rooted at
> each `u in {a,b,c}` contains `u'`.

Even the following weaker reserved-complement version is false:

> The rooted model may be chosen disjoint from `{a',b',c'}` so that the
> branch set rooted at each `u` is adjacent to `u'`.

Thus the coloured scheme used in the all-rainbow five-centre row cannot,
by contractibility alone, be made to absorb or remain simultaneously
adjacent to a second labelled contact triangle.

## 2. Ten-vertex construction

For every vertex `u in V(H)`, take two vertices `u^1,u^2`.  For every
edge `uv in E(H)`, add the edge `u^r v^s` exactly when `r=2` or `s=2`.
Finally add all three edges on each of

\[
                         T=\{a^1,b^1,c^1\},
             \qquad      T'=\{a^2,b^2,c^2\}.
\tag{2.1}
\]

Call the resulting graph `J`.  Colour `u^1,u^2` with colour `u`.  This is
a proper five-colouring.  The five roots are

\[
                         p^1,q^1,a^1,b^1,c^1,
\tag{2.2}
\]

and `T'` is a disjoint second triangle in the three corresponding stable
colours.

For every edge `uv of H`, the path

\[
                         u^1-v^2-u^2-v^1
\tag{2.3}
\]

is bichromatic.  Inside the subgraph before the two triangles are added,
these seven paths give the standard `H`-scheme in which every scheme path
is bichromatic.  In particular, each of `p^1,q^1` lies in the appropriate
bichromatic component with every vertex of `T`, and they lie in one
`p`--`q` bichromatic component.  That subgraph is the graph `M'(H)` of
Kuendgen--Pelsmajer--Ramamurthi; `J` is obtained by adding the two triangle
edge sets in (2.1).

## 3. Failure of both conclusions

The only neighbours of `a^1` outside `T` are `p^2,q^2`; the analogous
statement holds for `b^1,c^1`.  Consequently, any connected set that

- contains both `a^1` and `a^2`, and
- is disjoint from `p^1,q^1,b^1,b^2,c^1,c^2`

must contain at least one of `p^2,q^2`.  The same conclusion holds after
cyclically permuting `a,b,c`.  Three pairwise disjoint stable branch sets
containing the three prescribed pairs would therefore require three
distinct vertices from the two-set `{p^2,q^2}`.  This is impossible, so
the first proposed strengthening fails.

For the weaker statement, keep all of `T'` outside the model.  The exact
neighbourhood of `a^2` is

\[
                   \{p^1,p^2,q^1,q^2,b^2,c^2\}.
\]

A branch set rooted at `a^1` and adjacent to `a^2` cannot contain
`p^1,q^1`, which are the two singleton roots, or `b^2,c^2`, which are
reserved in `T'`.  It must therefore contain `p^2` or `q^2`.  The same
two-vertex capacity bound applies to `b` and `c`.  Hence at most two of
the three stable bags can have their prescribed adjacency to `T'`,
disproving the weaker statement as well.

## 4. Scope

The construction isolates the exact failure of a **scheme-only**
inference.  It has neither the seven-connectivity nor the critical-host,
exact-cut, full-shore, centre-degree, or five-centre incidence hypotheses
of the live problem.  In particular, it does not show that those host
hypotheses cannot force the desired second-triangle placement by a
different argument.

What it excludes is a direct upgrade of the
Kuendgen--Pelsmajer--Ramamurthi contractibility theorem: preserving five
labelled roots does not also preserve or control three additional labelled
vertices.  A valid continuation must spend additional host geometry, such
as centre-private contacts, full-shore connectedness, or a separation
forced when the two available connector vertices are insufficient.
