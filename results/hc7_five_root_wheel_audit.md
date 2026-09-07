# Independent audit of the five-root wheel theorem

**Verdict: GREEN.** Theorem 1, Lemma 2 and Corollaries 3–4 hold at the
whole-source SHA-256
`f0fbab79d23d8079b91ff1a812b83db96059aa4fb0024c809b1037f3f533f62a`
of [the source](hc7_five_root_wheel.md). This is a separate internal
mathematical audit, not external peer review or a proof of Conjecture 19.

## Strongest inference checks

- **Exact boundary quantifier.** The hypothesis covers every nonempty
  nonroot set, not just components. It is equivalent to internal
  five-connectivity and ensures every prescribed root has a nonroot
  neighbour. A triangle root with one neighbour outside the triangle
  therefore has a unique such neighbour that is a nonroot.
- **Contraction and lift.** When that neighbour is absorbed into its
  triangle root, every surviving nonroot set has exactly the same boundary
  cardinality: the absorbed vertex is replaced by the merged root, and
  the old root was not already a neighbour. No surviving nonroot loses
  degree. All five root preimages remain distinct and connected; literal
  triangle contacts survive. The parameter is the strictly decreasing
  nonroot order. The degree bound initially gives at least two nonroots
  and forbids a reduction to one, so an empty terminal case cannot occur.
- **Actual connectivity.** In the augmented graph `J+bc`, a disconnected
  component, including after one vertex deletion, can be chosen to avoid
  both surviving end roots. It would have at most four actual neighbours
  in `F`. Thus `J+bc` is two-connected. The ear insertion proof preserves
  earlier and later neighbours and terminates by increasing ordered
  vertex count. No proper prefix or suffix uses the auxiliary end-edge.
- **Simultaneous allocation.** The first prefix contacting two triangle
  roots has a nonempty complement. If the complement contacted at most
  one, a triangle root would have only the pivot as a neighbour in `J`,
  contradicting the reduction's stopping condition. Both pieces therefore
  contact two roots, their union contacts all three, and actual `J`
  connectivity supplies their mutual edge. A common triangle neighbour
  is the hub; the other two admit the required distinct assignments.
  Reverse contractions preserve these contacts without reusing vertices.
- **Actual-cut application.** Every component beyond the seven-set in
  Corollary 3 is full to that set. In its selected side, a nonroot loses
  at most `v,a`, so retains degree six. A boundary of at most four there
  lifts to an actual cut of at most six separating a nonempty set from
  the other component. The wheel avoids that component and `v`; both
  extras meet every root and each other. Their join with the wheel has
  precisely the required two independent possible omissions.
- **Exterior connectivity.** In Corollary 4 every component beyond a
  hypothetical three-cut contains a surviving neighbour of `v`. Removing
  at most one vertex from the stipulated spanning two-connected neighbour
  graph leaves all such neighbours connected, a contradiction. The
  five-cycle supplies exactly this hypothesis in the stated application.

No finite computation or external rooted-minor theorem is needed for
any checked inference. The final source differs from the initially read
revision only by deletion of the standalone sharpness example; this was
verified by reconstructing and hashing that earlier source.

**Remaining obligations.** The result closes the specified separator
case. It does not construct the compatible helper in a four-connected
exterior, settle the proposed five-root density theorem, or prove
Conjectures 19/21 or HC7. No unresolved assumption or gap was found in
these stated claims.
