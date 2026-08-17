# Audit of Lo elementary-minor robustness

**Verdict:** **GREEN for the internal deductions, conditional on the cited
external theorem; AMBER as a full import audit.**  Lo's exact statement is
verified at the primary source, but its version-one proof includes finite
figure cases not all independently reconstructed in this repository.

This audit checks the exact theorem revision

```text
active/hc7_k7minus_lo_elementary_minor_robustness.md
SHA-256 989b26475e5e3062cc880a1e2aba735b1c1b707e4e32f72aca553a2b337583dc
```

The current source SHA-256 is
`cc8769328f460c087cdb3c390cea4a094856ed54b7c0bc9bbba8b4bd782f49d5`.
The later edits only make the external-preprint trust boundary explicit;
the theorem statement, internal proof, arithmetic and scope are unchanged.

No mathematical gap remains in the deductions from Lo's Theorem 1.3, the
sharpness example, or the target-sensitive interpretation.  This audit does
not replace an independent proof audit of Lo's new preprint.  The result is
a side theorem: it does not prove the six-connected `4n` target, Conjecture
21, or `HC_7`.

## Primary-source check

Lo's arXiv paper was checked at version 1.  Its Theorem 1.3 states that
every four-connected non-planar graph of minimum degree at least five has a
`K_6^-` minor, and also has a `K_{3,4}` minor unless it is isomorphic to
`K_6`.  This is exactly the external implication used in the audited note;
the note does not import any part of Lo's structural characterisation.

Primary source: O.-H. S. Lo,
[*A characterization of graphs with no `K_{3,4}` minor*](https://arxiv.org/abs/2603.27973v1),
arXiv:2603.27973v1, Theorem 1.3.

The visible record on 17 August 2026 has no journal reference, acceptance
notice, or later arXiv revision.  The `K_6^-` part of Lo's proof ultimately
uses displayed finite extension certificates; not every one has been
rebuilt here.  Accordingly the verdict above is conditional, not a claim
of full independent validation of the imported preprint.

## Connectivity checks

Let `G` be six-connected.

1. If a set of at most four vertices separates `G-v`, adjoining `v` to
   that set separates `G`.  Hence `G-v` is five-connected.
2. Let `w` be the vertex obtained by contracting `xy`.  A cut of order at
   most four in the simple contraction lifts unchanged when it avoids `w`,
   and lifts to `(S-{w}) union {x,y}` when it contains `w`.  Either lift
   has order at most five and separates `G`.  Thus the contraction is
   five-connected.
3. Suppose `S`, with `|S|<=4`, separates `G-xy`.  Neither end of `xy` lies
   in `S`, since otherwise restoring `xy` changes nothing.  Restoring one
   edge can connect the graph only when there are exactly two components,
   one containing each end.  Neither component is a singleton: otherwise
   an end of `xy` has at most `|S|+1<=5` neighbours in `G`.  Removing `S`
   and either end therefore separates `G` with at most five vertices.
   Hence `G-xy` is five-connected.

All three reduced graphs have enough vertices for these connectivity
claims, and five-connectivity gives minimum degree at least five.

## Edge-count and Lo checks

Deleting a vertex removes at most `n-1` edges.  Passing to a simple edge
contraction removes the contracted edge and at most `n-2` duplicate edges,
again at most `n-1`.  Each resulting `(n-1)`-vertex graph therefore has at
least

```text
4n-9-(n-1)=3n-8>3(n-1)-6
```

edges and is non-planar.  Edge deletion leaves at least `4n-10` edges,
which is greater than `3n-6` for `n>=8`.  Thus all three graphs meet Lo's
connectivity, non-planarity and minimum-degree hypotheses.  Their orders
are at least seven, so none is the sole `K_{3,4}` exception `K_6`.

This proves both asserted minor conclusions for every vertex deletion,
simple edge contraction and edge deletion.

## Sharpness and target exclusion

For the icosahedron `I`, the standard facts

```text
|V(I)|=12,  |E(I)|=30,  kappa(I)=5,  I planar
```

give `Q=K_1 join I` order thirteen, size forty-two and connectivity six.
Thus `|E(Q)|=4|V(Q)|-10`, whilst deleting the universal vertex leaves the
planar graph `I`.  This proves the claimed sharpness of the `4n-9`
entrance for the every-vertex-deletion assertion.

The exclusion of a `K_7^-` minor from `Q` is also correct.  After removing
the at most one branch set containing the apex, six bags would remain in
`I` and form a `K_6` or `K_6^-` model.  If the apex is unused, the whole
model lies in `I`.  Each possibility contradicts planarity.

The adjacent barrier and its checker were pinned and rerun:

```text
barriers/hc7_k7minus_unrooted_k6minus_augmentation_barrier.md
SHA-256 ddfb0f8088c6bcabf761e6bc6bdaf3843d2d5162325d0e386c3084badddc3d93

barriers/hc7_k7minus_unrooted_k6minus_augmentation_barrier_verify.py
SHA-256 403c58e95d772f8af07bddc3954e9971a443ee5df2afb834f32a83efe37ac7ad
```

The current barrier SHA-256 is
`53bcd543589cd94408d103390c0cb1509d6bf14202847d7b90dc829d05dc0425`.
The only later change records this GREEN check in its status paragraph; the
construction, proof, checker, and scope are unchanged.

The checker returned GREEN and verified the graph parameters and the
displayed `K_6^-` branch-set certificate.  Its use is supplementary: the
unbounded target exclusion follows from the written planarity argument.

## Final assessment

Every connectivity lift, edge bound, order exception and model argument is
valid at the stated endpoints, including `n=8`.  The density constant is
sharp for the deletion claim.  GREEN persists with no qualification beyond
the scope limitation already stated in the theorem.
