# Independent internal audit: two-component three-cut support normal form

**Verdict: GREEN.**  At the exact revision identified below, the
set-Menger bond-extension lemma and the complete support-incidence
classification are correct under their stated hypotheses.  The small-torso
support bound and the Cartesian family of weakly linkable parity triples are
also valid.  The minimum three-support component has a four-connected
triangle-boundary torso, and the final torso bisection is exactly equivalent
to a component-side three-support bond.  Supports meeting only the
three-cut are explicitly accounted for and then excluded.  This is a
separate internal mathematical audit, not external peer review.

**Audited source:**
[`hc7_k44_two_component_threecut_support_normal_form.md`](hc7_k44_two_component_threecut_support_normal_form.md)

**Audited source SHA-256:**
`8840a94e131a9e7272f39786f84ab092cbbe42ba96444a5db31ff11191bb3347`

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

## 4. Small torso separations and parity triples

In Lemma 3.1, the torso adds edges only within `T`.  Because `W` lies in
`P`, its connectivity as a component of the torso minus `Z` is therefore
also connectivity in `X`.  It has no neighbour in `Q`, and any neighbour in
`P union T` outside `Z` would belong to the same torso component.  Hence
`N_X(W) subseteq Z`.  The nonempty component `Q` remains outside
`W union N_X(W)`, so three-connectivity gives `|N_X(W)|>=3`; the hypothesis
`|Z|<=3` gives equality.  Applying (1) to the nonempty proper connected set
`W` now forces at least three indexed supports to meet it.  Every such
support is in `S_P`, so if `|S_P|=3`, all three meet `W`.  No incidence with
`T`, including a shared cut vertex, is counted as an incidence with `W`.

The minimization in Theorem 3.2 is nonempty in the continuing target-free
nonsingleton-blocker setting of Section 2.  The preceding audited theorem
supplies a three-cut and says that each such cut has two components;
Theorem 1.2 then supplies a component meeting exactly three supports in
either incidence type.  Finiteness permits a minimum-order choice.

For that choice, the torso `Y=X[P union T]+K_T` is three-connected.  After
deleting at most two vertices, at least one cut vertex remains.  If a
component of the surviving part of `P` had no neighbour in `T` outside the
deleted set, its whole neighbourhood in `X` would lie in those at most two
deleted vertices, contrary to three-connectivity.  Every surviving
component of `P` therefore attaches to the surviving clique on `T`.

Now let `Z` be a three-cut of `Y`.  Since `Y-T=P` is connected, `Z` is not
`T`, so `T-Z` is nonempty and lies in one component `C_0` of `Y-Z`.  Every
other component `W` lies in `P`.  Three-connectivity of `Y` gives
`N_Y(W)=Z`; no added torso edge is incident with `W`, and no edge joins
`P` to the other component `Q` of `X-T`, so also `N_X(W)=Z`.  In `X-Z`,
the connected set `Q` joins `C_0` through the nonempty set `T-Z` and joins
no other component.  Thus `Z` is a three-cut of `X`, and the components of
`Y-Z` outside `C_0` are exactly the remaining components of `X-Z`.

The audited two-component conclusion leaves exactly one such `W`.  Lemma
3.1 makes it meet all three members of `S_P` and no support outside
`S_P`.  Because `Z` has order three but differs from `T`, it contains a
vertex of `P`; hence `|W|<|P|`.  The pair `(Z,W)` belongs to the original
minimization domain and contradicts minimality.  Therefore `Y` has no
three-cut.

The required order condition for four-connectivity is also satisfied.  In
the literal-blocker application, `delta(X)>=4` is supplied by the audited
input, so a component `P` with neighbourhood exactly `T` cannot be a
singleton.  Equivalently, it also follows from the abstract hypotheses:
if `d_X(v)=3`, then (1) makes `v` belong to at least three supports, and
the singleton bond splits all of them because every support has order at
least two.  Thus `|V(Y)|=|P|+3>=5`.  Together with three-connectivity and
the absence of a three-cut, this proves that `Y` is four-connected.

The whole-support alternatives are exhaustive.  On the three-support side
of the two-bridge type, its one component-local support is whole and both
bridge supports have vertices outside `P`.  In the one-bridge type, the
bridge support is external, at least one side support is whole, and the
other is whole exactly when it avoids `T`.  This gives respectively one or
two whole supports, with every remaining member of `S_P` external.  Finally,
for connected `W subseteq P`, no support outside `S_P` meets `W`, no edge
joins `W` to `Q`, and adding `K_T` changes no edge incident with `W`.
Consequently (8) is exactly the original inequality (1), not a weakened
torso estimate.

The supports in Corollary 3.3 exist in both normal-form types: Theorem 1.2
provides a support wholly contained in each component and at least one
support meeting both.  They are three distinct indexed supports.  The three
chosen parity sets all have order two.  Moreover,

\[
 (A_P\mathbin\triangle A_Q\mathbin\triangle\{x,y\})\cap P
                 =A_P\mathbin\triangle\{x\},
\]

which has odd order, whether or not `x` belongs to `A_P`.  Thus the full
symmetric difference is nonempty, and the quadruple is both nontrivial and
acyclic in the Chen--Ding--Yu--Zang terminology.  This argument permits
overlap between distinct indexed supports; no disjointness of the three
pairs is assumed.

The graph `X` is three-connected and hence two-connected, so Theorem 1.2 of
Chen--Ding--Yu--Zang applies in exactly the form recorded in the audited
five-support bond reduction.  A feasible parity bond meets each two-element
set oddly on both shores, so it separates the two members of each pair and
splits the three distinct supports.  The universal prohibition on a bond
splitting three supports excludes that alternative.  The quadruple is
therefore weakly linkable for every permitted choice of the two whole
supports, bridge support, local pairs, and bridge endpoints.

The word "simultaneously" in the source is a universal quantifier over this
Cartesian family.  It does not assert that the different quadruples share a
single weak-linkage witness; their witnesses may depend on the choices.

## 5. Localized completion equivalence

Let `A subset P` satisfy the triangle-boundary torso bisection conditions.
It is connected, and each whole support is split because it meets both `A`
and `P-A`.  Each external support is also split: it meets `A`, while by
definition it has a vertex outside `P` and hence outside `A`.  Thus all three
members of `S_P` are split.

The other shore is connected in the original graph.  Starting with the
connected graph `Y-A`, replace every artificial edge of `K_T` used by a path
with a path through `Q`.  The component `Q` is connected and every vertex of
`T` has a neighbour in `Q`, by Theorem 1.2(1).  These replacements avoid
`A subset P`; adjoining the remaining vertices of `Q` preserves
connectivity.  Hence `X-A` is connected, so `(A,X-A)` is a bond splitting
the three supports.

Conversely, suppose a bond splitting `S_P` has a shore `A subset P`.
Splitting a whole support says exactly that it meets both `A` and `P-A`.
For an external support, splitting together with `A subset P` says that it
meets `A`; its required vertex outside `P` already lies in the other shore.
To see that `Y-A` is connected, take paths in the connected graph `X-A`
between vertices of `Y-A`.  There are no edges from `P` to `Q`, so every
maximal excursion of such a path through `Q` has both ends in `T`; replace
that excursion by the corresponding edge of the added triangle.  Thus all
vertices of `Y-A` remain mutually connected.  This proves both directions
of the equivalence in Section 4 without assuming that an artificial
triangle edge was originally present in `X`.

The linked stripped-torso barrier has also been checked.  Its graph is
`K_5` with `P={u,v}`, whole support `{u,v}`, and external supports
`{u,t_1}` and `{v,t_2}`.  It is four-connected, all three local scores are
six, and meeting both external supports forces `A=P`, which cannot split
the whole support.  The dependency-free verifier reports

```text
PASS order=5 connectivity=4 local_scores=6,6,6
PASS candidate_bisections=0
NOTE stripped local torso claim only; global support provenance is absent
```

This example lacks `Q`, the other two indexed supports, the required global
incidence provenance, and the minimum-path data.  It therefore refutes only
the implication from four-connectivity and (8) to the bisection, not the
stated global triangle-boundary torso bisection lemma.

## 6. Accepted inputs and exact scope

The literal-blocker application accepts the following adjacent GREEN
results.

| input | source SHA-256 |
|---|---|
| [`hc7_k44_three_support_bond_and_threecut_reduction.md`](hc7_k44_three_support_bond_and_threecut_reduction.md) | `4007a05f71be45b16df65637806bffd241fd3da3cb9905b0764e73b818ecb9db` |
| [`hc7_k44_five_support_bond_reduction.md`](hc7_k44_five_support_bond_reduction.md) | `687034d01f4b1a9784585aa9596def4439939f17efc6ecd0d0530c2c95aa7773` |

The first supplies three-connectivity, support order at least two, the
six-boundary inequality, the universal prohibition on a bond splitting
three supports, and the fact that every surviving three-cut has exactly two
components.  These match all hypotheses of Theorem 1.2.  The second records
and audits the precise parity-bond dichotomy used in Corollary 3.3.

The result classifies, but does not eliminate, the two-component cut.  Its
two remaining incidence types are exactly:

1. two supports meet both components, and the other three are wholly
   component-contained with a `1+2` distribution; or
2. one support meets both components, with two further supports on each
   component side, at most one of each pair meeting the cut, and any
   cut-meeting supports from opposite sides using the same cut vertex.

The theorem imposes no stronger conclusion on how the supports meeting both
components intersect `T`, beyond the general one-cut-vertex bound, and it
does not by itself eliminate either incidence type.  Lemma 3.1 supplies a
local support lower bound for small torso separations; Corollary 3.3 shows
that every member of the full Cartesian parity family is weakly linkable.
The minimum-side argument strengthens the local setting to a
four-connected triangle-boundary torso, but the checked `K_5` barrier shows
that this connectivity and inequality (8) alone do not force the required
bisection.

The exact remaining nonsingleton statement is the triangle-boundary torso
bisection lemma of Section 4, equivalently the existence of a bond splitting
three supports with one shore contained in the selected minimum component.
Any proof must use retained global information absent from the stripped
barrier, such as support provenance through the complementary component or
the sequential minimum-path data.  The simultaneous weak-linkability
family is another exact expression of the same global residue; excluding
one fixed parity triple without those constraints is insufficient.

The distinguished `a,b` incidences remain additional data for that step,
and the singleton-blocker branch remains separate.  No finite computation
is used, and the result does not prove the literal `K_{4,4}` case of T44,
T44, Conjecture 21, or `HC_7`.
