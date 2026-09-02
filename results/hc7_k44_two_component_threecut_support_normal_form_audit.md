# Independent internal audit: two-component three-cut support normal form

**Verdict: GREEN.**  At the exact revision identified below, the
set-Menger bond-extension lemma and the complete support-incidence
classification are correct under their stated hypotheses.  Supports meeting
only the three-cut are explicitly accounted for and then excluded.  This is
a separate internal mathematical audit, not external peer review.

**Audited source:**
[`hc7_k44_two_component_threecut_support_normal_form.md`](hc7_k44_two_component_threecut_support_normal_form.md)

**Audited source SHA-256:**
`3188d74bcf396ae77c1f1bc3ee8b55cfb013a1c35418cf432e2ecd1ac03b510f`

## 1. The three-pair bond lemma

Deleting `r` from the three-connected graph `X` leaves a two-connected
graph.  Set-Menger applied between each selected pair and `{s,t}` therefore
gives two vertex-disjoint paths with distinct initial and terminal vertices.
After each path is trimmed at its first member of `{s,t}`, its interior lies
in the component where its selected endpoint lies: before reaching `s` or
`t`, it cannot leave that component of `X-{r,s,t}` because `r` has been
deleted.

The paths from `P` and `Q` ending at `s` form one connected set, and those
ending at `t` form another.  The two sets are disjoint: within a component
this follows from the linkage, and between components their interiors are
disjoint.  They place opposite members of both component pairs, as well as
`s,t`, in opposite sets.

If the two sets are not adjacent, a shortest path between them has all its
internal vertices outside both.  Splitting those internal vertices at any
edge of the path enlarges the two sets to disjoint connected adjacent sets
without moving a specified vertex.  Their union is connected.  Hence every
component of the still unused induced subgraph has an edge to that union;
assigning each such component wholly to a side it meets preserves the
connectivity of both sides and every prescribed separation.  The result is
a spanning bond, so Lemma 1.1 is valid.

## 2. Component bonds and exclusion of cut-only supports

For either component `P` of `X-T`, its neighbourhood is all of `T`.
Otherwise at most two vertices would separate it from the other component.
Thus every cut vertex has a neighbour in each component, which proves that
every partition in (3) has two connected shores.

Applying (1) to `P` and `Q` gives

\[
                         |I_P|\ge3,\qquad |I_Q|\ge3.
\]

The component bond splits at most two supports.  Therefore among the at
least three supports meeting `P`, one is not split and is contained wholly
in `P`; similarly a distinct support is contained wholly in `Q`.  Their
order-two hypotheses supply the two pairs used in Lemma 1.1.

If any indexed support contained two cut vertices, applying Lemma 1.1 to
those two vertices and to the two whole component supports would produce a
bond splitting three distinct supports.  Hence every support meets `T` in
at most one vertex.  In particular, a support contained entirely in `T`
would have order at most one, contrary to the standing order-at-least-two
hypothesis.  This is the exact point at which all cut-only supports are
excluded; none is silently assigned to `P` or `Q` in the subsequent count.

## 3. Incidence classification

The inclusion-exclusion lower bound remains valid even before using the
cut-only exclusion:

\[
 |B|=|I_P|+|I_Q|-|I_P\cup I_Q|
      \ge |I_P|+|I_Q|-5\ge1.
\]

Every member of `B` meets both component shores and is split by their bond,
so `|B|<=2`.

If `|B|=2`, these two supports exhaust the split allowance for both
component bonds.  Any other support meeting `P` must consequently be wholly
contained in `P`, and similarly for `Q`.  A remaining support cannot avoid
both components because that would make it cut-only.  The inequalities
`|I_P|,|I_Q|>=3` require at least one of the three remaining supports on
each side, so their distribution is exactly `1+2`.

If `|B|=1`, none of the other four supports meets both components, and none
is cut-only.  They therefore partition into supports meeting `P` but not
`Q` and supports meeting `Q` but not `P`.  The same two lower bounds force
exactly two of each.  On the `P`-side, if both supports also met `T`, the
component bond would split them together with the member of `B`; hence at
most one meets `T`, and at least one is wholly contained in `P`.  The
argument for `Q` is identical.

Finally, suppose a `P`-side support meets `T` at `t_P` and a `Q`-side
support meets it at `t_Q`.  Their cut vertices are unique by the preceding
argument.  If `t_P` and `t_Q` were distinct, the bond in (3) with
`J={t_Q}` would split the member of `B`, the `P`-side support across
`P,t_P`, and the `Q`-side support across `Q,t_Q`.  These are three distinct
indexed supports, contradicting the bond hypothesis.  Thus `t_P=t_Q`.
This proves every assertion of Theorem 1.2 without assuming that supports
avoid or are disjoint on `T`.

## 4. Accepted input and exact scope

The literal-blocker application accepts the adjacent GREEN result
[`hc7_k44_three_support_bond_and_threecut_reduction.md`](hc7_k44_three_support_bond_and_threecut_reduction.md)
at source SHA-256
`4007a05f71be45b16df65637806bffd241fd3da3cb9905b0764e73b818ecb9db`.
It supplies three-connectivity, support order at least two, the
six-boundary inequality, the universal prohibition on a bond splitting
three supports, and the fact that every surviving three-cut has exactly two
components.  These match all hypotheses of Theorem 1.2.

The result classifies, but does not eliminate, the two-component cut.  Its
two remaining incidence types are exactly:

1. two supports meet both components, and the other three are wholly
   component-contained with a `1+2` distribution; or
2. one support meets both components, with two further supports on each
   component side, at most one of each pair meeting the cut, and any
   cut-meeting supports from opposite sides using the same cut vertex.

The theorem imposes no stronger conclusion on how the supports meeting both
components intersect `T`, beyond the general one-cut-vertex bound, and it
does not eliminate either type.  The sequential minimum-path structure and
the distinguished `a,b` incidences remain additional data for the next
step.  The singleton-blocker branch remains separate.  No finite computation
is used, and the result does not prove the literal `K_{4,4}` case of T44,
T44, Conjecture 21, or `HC_7`.
