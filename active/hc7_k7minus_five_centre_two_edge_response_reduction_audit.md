# Internal audit: two-edge response reduction

**Verdict:** GREEN.  A separate cold reading checked the deleted-edge
vertex-cover criterion, all contraction signatures, both directions of the
five-centre flip theorem, the Boolean monotonicity and the stable-completion
conclusion.  One initial omission about unused contraction images was
repaired by making the completion model spanning before the source was
pinned.

This is internal mathematical review, not external peer review.

**Audited source:**
[`hc7_k7minus_five_centre_two_edge_response_reduction.md`](hc7_k7minus_five_centre_two_edge_response_reduction.md)

**Source SHA-256:**

```text
4092d11254dde49f17961ac091f1a479fb4f719babebe0eb271d9fba6fb32b68
```

## 1. Deleted-edge traces

For a colouring of `Q-E_0`, the only possible monochromatic edges of `Q`
are those in `M(c)`.  Its restriction outside `A` is proper exactly when
`A` covers `M(c)`.  Extension of the exact induced boundary partition would
glue to a `q`-colouring of `Q`, so every such exterior trace is rejected on
the closed `A`-side.

Two disjoint covers of a nonempty edge set must contain opposite ends of
every edge.  This proves the common-crossing characterization and makes
three pairwise disjoint traces impossible for one fixed deletion colouring.

## 2. Contraction signatures

Colouring `Q/e` and expanding gives the singleton signature `\{e\}` while
the retained edge `f` stays proper; the symmetric signature follows in the
same way.  Contracting two disjoint edges, or all three vertices of an
induced two-edge path, gives the double signature.  If the path lies in a
triangle, the retained chord would also be monochromatic, so the double
signature is impossible.  The source's condition is exact.

## 3. Five-centre flip equivalence

For every nonempty contraction set `I`, the graph `M_C/I` is a proper minor
of `G` and is six-colourable; adding `pq` gives chromatic number at most
seven.

If `H_I` is six-colourable, expanding `I` makes precisely its edges
monochromatic.  The contractibility condition prevents any undeleted edge
from being hidden inside a contraction class.  The artificial edge makes
`p,q` distinct.  Expanding `x` only to the independent boundary block `Z`
gives the modified `C`-shore partition

\[
                         Z\mid\{p\}\mid\{q\}.
\]

This aligns with a permitted unmodified colouring of the distinct-response
`D`-shore and glues to the stated full-host edge-deletion colouring.

Conversely, the labelled full-host colouring restricts to the modified
`C`-shore.  Identifying `Z` as `x`, contracting exactly the monochromatic
selected edges and restoring the proper edge `pq` colours `H_I`.  The two
directions therefore preserve all five centres and the pole orientation.

If `I` is a flip, every larger contraction set is a flip because its graph
is a minor of `H_I`.  The three listed patterns are exactly the upward-
closed subsets of the nonempty two-element Boolean square.

## 4. Stable completion models

Stability and the seven-colour upper bound give `chi(H_I)=7`.  Global
vertex-minimality of `G` forces `H_I` to contain a `K_7^-` minor.  The graph
`H_I` is connected.  Absorbing every component outside an arbitrary model
into one adjacent branch set makes the model spanning, so each contraction
image belongs to a branch set.  Expanding its preimage gives the asserted
one-edge or two-edge co-bagging in `M_C+pq`.

The audit confirms the stated limit: the artificial pole edge and the
contracted opposite side may still obstruct lifting this completion model
to `G`.  No cross-edge pair, branch closure, Conjecture 21 or `HC_7` is
claimed.
