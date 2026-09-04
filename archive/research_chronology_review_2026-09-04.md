# Historical proof-route review through 2c17559

**Status:** historical internal review, frozen on 4 September 2026.
This records inspected repository snapshots and earlier failed inferences;
it is not a research-status ledger. Current status belongs only to
[`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md).

## Snapshot selection

The inspected endpoint was `2c17559e99e18e2727cbb0c828f3deb97491c4d9`.
The initial commit and approximately fortnightly snapshots were read with
`git show`, including their contemporary README, proof spine or active index,
and research ledger where one existed. Committer dates determine when a
snapshot entered history; author dates alone can misdate repository state.

| Date | Revision | Contemporary programme and outstanding implication |
|---|---|---|
| 13 July | `a14eb38` | A mature near-`K_7` programme already existed, with extensive pre-Git archives. The initial spine and its audit explicitly left arbitrary-model normalization, global rotation composition and the remaining separator families open. Rotations were already recognized as involutive, not descent. |
| 27 July | `df001e9` (and preceding freeze `9d72e68`) | The direct `HC_7` spine had moved to low-degree bounded interfaces and proper-minor colouring responses. Its global bridge-composition theorem remained open. The freeze preceded the shift toward `K_7^-` density. |
| 10 August | `92b8722` | Conjecture 21 was again primary after `932cb6a`. The arbitrary seven-connected `4n-2` target had discarded critical-colouring information. Five independent degree-eight centres and exact-cut structure did not solve simultaneous rooted allocation. |
| 24 August | `f85e51c` | No later main-line commit existed by this date. The independent `K_{2,n}` and five-root results were available; `n_8>=27+tau` and the six-connected `4n` route still had unclosed separator and allocation steps. |
| 2 September | `2c17559` | T44 was primary. Literal configurations had been eliminated, while singleton completion, nonsingleton support allocation and nonliteral ownership-preserving rotation remained open. |

The August 22 author dates on `5f6d2b8` and `3c42a94` conceal August 31
committer dates. Similarly, the `K_{2,n}` manuscript commit `59fb923` was
authored August 16 but committed August 31. The underlying theorem was
already present at the August 24 snapshot.

The initial commit cannot establish the project's pre-Git chronology. It
already contains an extensive archive and an explicit audit of the failure
to earn a special singleton/bipartite model from an arbitrary near-clique
minor. Its motivating goal was `HC_7`, with a fixed two-vertex
`K_5`-minor-free remainder as one sufficient endgame.

## Intervening failures checked more closely

The most consequential retraction is on a side branch, found through
`git log --all`, not just the ancestry of the inspected HEAD. Commit
`a850250` claimed the seven-connected `4n-2` theorem and Conjecture 21;
`15f824c` retracted them. The exact postmortem is retrievable as

```text
git show 15f824c:barriers/hc7_exact_six_boundary_degree_inference_failure.md
```

For a full six-cut `S` with `r` complementary components, the argument used
`d_{H-S}(s)>=r` and `d_H(s)>=6` to infer `d_{H[S]}(s)>=6-r`. This subtracts
one lower bound from another; an upper exterior-degree bound was needed.
Every subsequent boundary classification used that unsupported premise.
The finite verifier imposed the premise, and the internal audit repeated
the same inference. They did not independently validate the host reduction.

Other exact checkpoints illustrate the same preservation issue:

- The initial `archive/hadwiger_HC7_postaudit_nearK7.md` corrects the
  size-six colour-saturation reduction: the whole neighbourhood is
  inclusion-minimal saturating. Dropping the critical extension hypothesis
  silently changes the quantified problem.
- The initial `archive/hadwiger_c6_closure_spotcheck_counteraudit.md`
  refutes a portal-cofaciality claim under SPQR reflection with an explicit
  eight-vertex construction.
- `f0863d1` corrects the inference from failed opposite Kempe interchanges
  to opposite branch-set contacts.
- `13f3ff5` freezes near-model compression without preserved roots,
  prescribed paths and a comparable separator parameter.
- `57736cc` records that separate donor and deficient-bag minima do not
  give a common family closed under the required exchanges.
- `1d2a263` corrects an order-nine search which had added an unsupported
  second contact; `20ad515` then freezes the six-fan route because distinct
  exits need not give distinct retained-side attachments.
- `c0962bc` corrects an insufficient sparse-boundary target: obtaining
  `mu>=2` from `eta>=6` does not supply the required `eta<=5mu` inequality.

## Interpretation

These corrections do not retract the later theorems under their explicit
hypotheses. They explain why the number of eliminated local configurations
is a poor measure of progress toward the terminal conjecture. The repeated
missing argument preserves a complete colouring partition or a rooted
model through an operation, with a strictly decreasing parameter in the
same hypothesis class. An actual separator alone supplies neither.

The independent `K_{2,n}` and five-root theorems are different kinds of
output: their proofs terminate for arbitrary instances in their stated
classes. This motivates testing general packing and rooted-minor statements
alongside T44, without treating T44 as a mandatory destination. No claim
of external review or comparative publication significance is made here.
