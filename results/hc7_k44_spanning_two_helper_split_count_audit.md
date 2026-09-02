# Independent internal audit: spanning two-helper split count

**Verdict: GREEN.**  At the exact source revision pinned below, the spanning
extension, defect identity, and anchored sufficient condition are correct.
This is a separate internal mathematical audit, not external peer review.

**Audited source:**
[`hc7_k44_spanning_two_helper_split_count.md`](hc7_k44_spanning_two_helper_split_count.md)

**Audited source SHA-256:**
`9e139106b9f5c47d1c12b7b24436f1890b6f50aa31c293689b2cb1fb3945da54`

## 1. Accepted dependency

The source uses the following promoted result at the revisions shown.

| dependency | SHA-256 |
|---|---|
| [`hc7_k44_tight_boundary_and_minimum_blocker.md`](hc7_k44_tight_boundary_and_minimum_blocker.md) | `384150b962a3e86848622e78cd711fac3d27b1bfcedbc22a1ce8adb2d7127b90` |
| [adjacent audit](hc7_k44_tight_boundary_and_minimum_blocker_audit.md) | `f0f5ab26c066e7641059e6aa5f5961b0a8b437afb034675c5119e242c26d2faa` |

In particular, Lemma 4.1 of that result supplies the minor construction
from a two-helper defect at most one, while Theorem 1.1 supplies the boundary
normal form, boundary fullness, and the distinguished vertex `p` used in
the final section.

## 2. Spanning extension

Let `W` be a component of `X-(U_0 union V_0)`.  Since `X` is connected and
`U_0 union V_0` is nonempty, `W` has an edge to that union.  Assigning `W`
to a side it meets keeps that side connected.  Distinct such components
are disjoint and have no edges between them, so assigning every component
in this way gives disjoint connected sets covering `X`.  The original
`U_0`--`V_0` edge remains and keeps the two enlarged sides adjacent.

For each side, enlargement can only enlarge `N_D` of that side.  Each of
the two complements counted by `delta_{h_0}` can therefore only shrink,
for every fixed `h_0`.  This proves the asserted defect monotonicity.  It
also preserves `a in N_D(U_0)` whenever that hypothesis is present.
Consequently an arbitrary two-helper witness extends to a spanning one;
the converse is immediate because a spanning witness is already allowed
by the parent lemma.  The claimed no-loss reduction is exact.

## 3. Split-count identity

For a spanning partition, boundary fullness implies that every `k in K`
meets at least one side.  A split resource belongs to neither defect set in
(10), a resource supported on only `V` belongs only to `F_U`, and a resource
supported on only `U` belongs only to `F_V`.  The special resource `b` is
already supplied to the first helper through the boundary edge `ab`; it
therefore contributes exactly once, to `F_V`, precisely when `V` misses
it.  Hence `F_U,F_V` are disjoint and

\[
 |F_U|+|F_V|=5-s(U,V)+\varepsilon_b(U,V).
\]

Choosing `h_0` removes at most one contribution because the two sets are
disjoint, and removes exactly one whenever their union is nonempty.  When
the union is empty, the defect is already zero.  Thus the minimum is

\[
 \max\{0,4-s(U,V)+\varepsilon_b(U,V)\},
\]

exactly as stated.  Its value is at most one precisely when
`s(U,V)>=3+epsilon_b(U,V)`.  In particular, the four threshold cases are
sharp: `s=2` fails and `s=3` succeeds when `V` sees `b`, while `s=3` fails
and `s=4` succeeds when `V` misses `b`.  The zero-defect endpoint
`s=5, epsilon_b=0` is also handled correctly by the maximum in (8).

## 4. Anchored condition and exact scope

The parent theorem gives `p in N_X(a)` and makes `X-p` full to `H`; in
particular `N_X(b)-{p}` is nonempty.  In the stated conditional partition,
placing `p` in `U` makes `U` see `a`, and placing a `b`-neighbour distinct
from `p` in `V` makes `epsilon_b=0`.  Three split `K`-supports then meet
the exact threshold in (9).

The source correctly labels this as sufficient rather than equivalent.
Requiring the prescribed `p` can exclude other two-helper partitions, and
the anchored condition deliberately omits the valid mode
`epsilon_b=1, s=4`.

The result proves neither the existence of an anchored partition nor the
existence of any closing partition.  Its equivalence is solely with the
numerical hypothesis of the already promoted two-helper construction, not
with existence of a `K_7^-` minor.  No finite enumeration is used in this
deduction, and no conclusion about the weighted splitter theorem, literal
T44, T44, Conjecture 21, or `HC_7` follows from it alone.
