# Independent audit of the one-path marked-scheme counterexample

**Verdict: GREEN.** This cold audit checks
[the source](hc7_one_path_marked_scheme.md) at whole-source SHA-256
`7b6ee34368f1b8d6828d5291e9559b05c192b22ad148671a7c69e4aec810b768`.
This is a separate internal mathematical audit, not external peer review.
The final source differs from the initially audited `c532321d...` revision
only in its status wording.

## Strongest inference checks

- **Actual scheme.** The seven specified cross-edges give the partial
  bipartite scheme at all six distinct roots. Their proper endpoint
  colours agree at every meeting vertex. The equal-coloured markers
  `0,2` are outside its path union, and every listed auxiliary cycle,
  triangle and apex edge is present. Extra edges of the host do not
  become unproved scheme paths.
- **All minor models.** The independent set `S={0,2,a0}` has the
  stated degrees `3,3,4`. Since `Q` has minimum degree five, none can
  be a singleton branch set. A connected bag containing `k>=1` of
  these vertices therefore contains at least one other vertex, and
  contributes at least `k` to its contraction cost. Each unused member
  of `S` contributes one deletion. These contributions are disjoint.
  The identity `unused + sum(|bag|-1)=9-7=2` holds for every seven-bag
  model, including models with unused vertices. The required cost of
  at least three is a contradiction; no enumeration or assumption
  about a chosen contraction sequence is involved.
- **Scope.** Deleting `S` leaves exactly the claimed join, which is
  five-colourable. Its colouring extends independently over the three
  vertices, each of degree at most four. Thus the example has minimum
  degree three and is five-colourable; it does not satisfy the actual
  seven-connected, minimum-degree-eight critical-host hypotheses.

The two-path repair is precisely the Section 5 statement of the linked
[marked-scheme theorem](../results/hc7_marked_k33_scheme_completion.md),
checked at SHA-256
`fb55cc00b52e0f3fb6f6e547f08b29ed6aae37cb25c4176a7c7fb96ada05dc2f`.
The counterexample proof is self-contained and does not depend on that
positive theorem. No gap or unresolved hypothesis was found in the
stated negative claim; the critical-host construction remains open.
