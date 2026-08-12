# Separate internal audit: the cross-signature pivot gate

**Verdict:** **GREEN for Lemma 2.1 and Theorem 3.1.**  The interaction
alternatives in Theorem 3.1 are exhaustive under the stated shared-pivot
hypothesis.  Sections 4--5 correctly identify two additional unproved
requirements and do not claim to close the matching row.

This is a separate internal mathematical audit, not external peer review.
It checks the exact source revision identified below.

## Exact revision

The audited source is
[`hc7_k7minus_cross_signature_pivot_gate.md`](hc7_k7minus_cross_signature_pivot_gate.md),
with SHA-256

```text
99bb8de11862040c14d884f6f3f53c6fb1276795d9a85a61c4f16e11c98be21f
```

The current source differs from the initially audited revision
`5dd1527bf3fb9358dd55115a3c23a6f91c8b9e09419282035cfb6c6faace5f82`
only in its status paragraph and audit link.  Its mathematical content is
unchanged.

The direct proved input is the audited
[matching common-state theorem](../results/hc7_k7minus_matching_square_common_state.md),
which puts the three realised signatures and the forbidden fourth signature
on one graph.  The selected-edge and all-lock results are used only to
describe the live application and the remaining route gap.

## 1. Static deficiency

The vectors in Lemma 2.1 refer only to adjacencies between fixed branch
sets and the two fixed pieces of one branch set.  Changing a colouring of
`H` changes none of those sets or adjacencies.  Thus the five deficiency
vectors are genuinely signature-invariant.  A profile attached instead to
a bichromatic component would depend on the colouring and would introduce
the existential-object mismatch recorded after the lemma.

## 2. Disjoint and equal palettes

At the shared `EE` pivot, switching `C_e` separates exactly the ends of
`e` and leaves the ends of `f` equal; switching `C_f` has the symmetric
effect.  For a monochromatic endpoint pair, a bichromatic component leaves
the pair equal precisely when it contains both ends or neither end.

If the two palettes are disjoint, their vertex sets are disjoint and every
edge between them retains colours from two disjoint palettes after both
switches.  Hence the switches commute as proper Kempe interchanges.  The
component which separates one pair prevents the other, disjoint-palette
component from containing either end of that pair: it cannot contain both
because one end already lies in the separating component, and it cannot
contain exactly one because its individual switch leaves the pair equal.
The combined colouring therefore has signature `PP`, a contradiction.

If the palettes are equal, `C_e` and `C_f` are components of the same
bichromatic induced subgraph.  They cannot be the same component because
one fixed switch cannot have both distinct signatures `PE` and `EP`.  If
they are distinct, they are disjoint and anticomplete in that bichromatic
graph.  Switching both is proper, and the same endpoint-containment
argument gives `PP`.  Equal palettes are therefore also impossible.

Two distinct two-element palettes which are neither equal nor disjoint
share exactly one colour.  This verifies items 1--2 of Theorem 3.1.

## 3. Exhaustiveness of the interaction alternatives

Write the palettes as

\[
                         \{s,x\},\qquad\{s,y\},
                         \qquad x\ne y.
\]

If the two components meet, every common vertex has a colour belonging to
both palettes, hence has colour `s`.  This is the first alternative in
item 3.

Suppose instead that the components are disjoint.  By the endpoint
argument above, their simultaneous interchange makes both selected pairs
proper.  Each individual whole-component switch is proper.  Hence a new
monochromatic edge can occur only between the two switched components.
Under the pivot colouring, a proper edge between them has one of the
colour pairs

\[
                         (s,y),\qquad(x,s),\qquad(x,y).
\]

After both switches the first two become `(x,s)` and `(s,y)`, while the
last becomes `(s,s)`.  Consequently, if there were no `x`--`y` edge
between the components, the simultaneous assignment would be a proper
`PP` colouring of `H`.  The universal absence of `PP` therefore forces
such an edge.  These cases exhaust intersection versus disjointness, so
item 3 is complete.  In fact the forced edge lies in `H`, and hence also
in `G`.

No commutation of unrelated `EP`, `PE` and `EE` colourings is used in this
argument; both switches have the same explicitly hypothesised base
colouring.

## 4. Exact remaining gaps

The currently proved signature language gives nonempty `EP`, `PE` and
`EE` colouring families, but does not give one `EE` colouring adjacent by
single Kempe interchanges to both singleton families.  Kempe equivalence
of the singleton families would still not by itself identify such a common
pivot.

Even if a shared pivot is supplied, Theorem 3.1 locates only an overlap or
edge between two bichromatic components.  That interaction may occur
inside one existing branch set or across an already represented model
adjacency.  It need not meet a deficient branch-set label and therefore
does not by itself increase the double-contact count.

The deficiency-aware shared-pivot statement in Section 5 is accordingly
an open repair theorem.  Its iteration remark is conditional on obtaining
a model-valid strict increase at each use.  The source does not present
the existence of the shared pivot, the model-monotone exchange, a bounded
labelled response, or a common shore partition as proved.

## Scope

The audited lemmas are unbounded and computation-free.  The source proves
a necessary interaction at a supplied common pivot and a precise route
nonclosure; it does not prove the cross-signature root-bag terminalisation
theorem, the matching row, the six-coordinate terminalisation theorem, or
the conjecture.
