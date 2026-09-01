# Seven-connected `K_{4,4}` closure frontier

**Status (1 September 2026):** T44 is the sole active completion target.  It is
open.  No seven-connected counterexample has been found.  The literal-core
completion and the nonliteral branch-model lift are both still open, and no
result in this file proves Conjecture 21 or `HC_7`.

## 1. Primary target and exact consequence

### T44

> Every seven-connected graph containing a `K_{4,4}` minor contains a
> `K_7^-` minor.

Here, *target-free* means `K_7^-`-minor-free.

T44 would prove Norin--Totschnig Conjecture 21.  If that conjecture failed,
choose a minor-minimal non-six-colourable target-free graph `G`.  It is
seven-contraction-critical and hence seven-connected.  Kawarabayashi--Toft
prove that every seven-chromatic graph contains either a `K_7` minor or a
`K_{4,4}` minor.  The first alternative already contains `K_7^-`; T44 closes
the second.

Primary references:

- [Kawarabayashi--Toft, *Any 7-chromatic graph has K7 or K4,4 as a minor*](https://doi.org/10.1007/s00493-005-0019-1), Combinatorica 25 (2005), 327--353;
- [Norin--Totschnig, *Every graph with no `K_7^vee`-minor is 6-colorable*](https://arxiv.org/abs/2507.03244), especially their contraction-critical setup and Conjecture 21.

This implication uses the universal seven-connected theorem exactly as
stated.  A later critical-host strengthening may be useful proof machinery,
but it is not silently substituted for T44.

## 2. Computer-assisted finite evidence and reduced-family result

The first exact pass found no counterexample.

1. Every seven-connected graph through order eleven contains `K_7^-`,
   whether or not a `K_{4,4}` is specified.  At order eleven, complementation
   reduces the census to 10,946 unlabelled subcubic graphs.  Exactly 9,940
   complements are seven-connected; 9,844 contain a literal `K_{4,4}`.  All
   9,940 have independently validated seven-bag certificates.  Of the
   literal-core cases, 3,871 already contain the target as a subgraph and
   5,973 require contraction.
2. Every seven-connected member of the full-attachment non-clique seven-sum
   family

   ```text
   G = S join (L disjoint-union R),  |S|=7,
   ```

   with nonempty connected `L,R` is target-positive.  For outside orders two
   and three, seven-connectivity reduces respectively to the audited
   five-connected and minimum-degree-four double-cone theorems.  For orders
   four through seven, an exact search checks 105 edge-minimal cases.  Above
   seven, connected subgraphs of the two shores reduce to the order-seven
   row.
3. Exact one- and two-vertex branch-split probes found no global survivor.
   The sharp local survivors instead have low connectivity and refute only
   shortcut certificates.
4. The exact weighted-splitter formula has no survivor on the 1,619
   three-connected order-eight graphs left by the cubic-vertex reduction.
   Targeted small-atom probes are also UNSAT on all 16 connected
   four-regular graphs of order nine and on the 57 three-connected graphs
   among the 59 connected four-regular graphs of order ten.

Sources, counts, digests and reproduction commands are in
[`experiments/k44_closure_falsification/`](experiments/k44_closure_falsification/README.md).
The order-eleven conclusion is a computer-assisted finite result.  The
full-attachment conclusion is a written-unaudited reduction whose 105 base
cases are checked computationally.  The weighted-splitter runs use Z3 5.1.0
without an independently checkable UNSAT certificate; their exact encoding,
independent concrete-witness checker, counts and digests are preserved in the
[hostile-screen experiment](experiments/k44_literal_weighted_splitter/README.md).
None of these finite results implies T44.

The sharpest current near-miss is the tetrahedral literal profile

```text
N_H(p_s)=Q-{s},  s in Q,  |Q|=4.
```

Each shore-split orbit has a 19-contact seven-bag quotient and no
20-contact quotient.  The graph has order 12, 34 edges, connectivity four
and minimum degree four, so it is not a T44 counterexample.

## 3. Audited literal-core machinery

Let `H` be a literal `K_{4,4}` with core `S`, and let `C=G-S`.

The following results are promoted and separately internally audited.

1. [Four prescribed roots in a three-connected graph have a rooted
   `K_4^-` model](../results/rooted_k4minus_four_roots.md).
2. [The double cone over a five-connected graph forces `K_7^-`; a
   vertex-minimal nonliteral model has an exact seven-cut through every
   internal branch edge](../results/hc7_k44_branch_model_and_double_cone.md).
3. [Every exact seven-cut in a seven-connected target-free graph has an
   internal boundary vertex of degree at most
   three](../results/hc7_k44_fourconnected_seven_boundary_double_cone.md).
4. [In a seven-connected target-free literal host, the exterior is connected
   and has no separator of order at most
   two](../results/hc7_literal_k44_exterior_threeconnectivity.md).
5. [A triangle of exterior bags with four portals each is
   terminal](../results/hc7_k44_four_portal_triangle_completion.md).
6. [Four mutually adjacent exterior bags with three portals each are
   terminal except for the exact tetrahedral
   profile](../results/hc7_k44_three_portal_k4_tetrahedral_dichotomy.md).
7. [The exact obstruction to a safe weighted contraction reduces every
   complete blocker system to a tight atom of order at most
   three](../results/hc7_k44_weighted_splitter_small_atom_reduction.md).

If the four bags span `C`, the tetrahedral exception is impossible: its
total portal coverage is four, while seven-connectivity forces
`|N_S(C)|>=7`.  The consolidated internal [cold
audit](../results/hc7_k44_closure_local_normal_forms_audit.md) pins every
source and executable trust boundary.

## 4. Exact literal obligation

The exterior separator theorem does not itself produce the weighted model.
For a connected exterior set `X`, write

`w(X)=|partial_S(X)|`.

Seven-connectivity gives

`|N_C(X)|+w(X)>=7`

for every nonempty proper `X`, together with `w(C)>=7`.  The following
purely labelled trichotomy is sufficient and remains open:

1. three pairwise-touching disjoint connected exterior bags, each of weight
   at least four;
2. a spanning exterior `K_4` model whose four bags each have weight at
   least three; or
3. six disjoint connected exterior bags, each of positive weight, whose
   quotient has at least fourteen of the fifteen `K_6` contacts.

The first outcome closes by the portal-triangle theorem.  The second closes
by the portal-`K_4` dichotomy and global portal coverage.  In the third,
use the whole connected literal core as a seventh bag.  It meets all six
positive-weight exterior bags, so the quotient has at least `14+6=20`
contacts and is a `K_7^-` model.  This direct alternative avoids any new
branch-label ownership issue.

An exact bounded falsification test checks this trichotomy for every
three-connected unlabelled exterior through order seven and, for each
exterior, symbolically checks all `2^(8|C|)` core-incidence assignments.
All 157 graph instances are UNSAT.  Z3 is the decisive trust boundary and
no independently checkable UNSAT certificate is retained, so this is
evidence only, not an unbounded inference.  The source and exact output are
preserved in the [labelled-trichotomy
experiment](experiments/k44_literal_labelled_trichotomy/README.md).

The audited [weighted-splitter small-atom
reduction](../results/hc7_k44_weighted_splitter_small_atom_reduction.md)
now supplies a genuine unbounded intermediate theorem.  For a
three-contractible edge `uv`, contraction fails the boundary system exactly
when a nonempty set `X subseteq V(C)-{u,v}` is tight and has both `u,v` in
its boundary.  This includes disconnected and co-spanning witnesses; sets
containing the contracted vertex preserve their preimage boundary and
weight.

If no terminal triangle and no safe edge exists, the reduction produces a
spanning tree all of whose edges are three-contractible and a minimum tight
set `A` whose boundary contains a tree edge.  Writing `B=N_C(A)` and
`Q=L(A)`, it proves

```text
1 <= |A| <= 3,    4 <= |B| <= 7,    |Q| = 7-|B| <= 3.
```

Every tree edge incident with `A` has a connected tight companion blocker
`X`, and

```text
A subseteq N_C(X),
|partial A intersect partial X| <= 7-2|A|.
```

For a three-vertex atom and a crossing tree edge, the two seven-resource
boundaries meet in exactly the outside endpoint.  The companion set is
adjacent to all three atom vertices, its contacts in `B` form a set `P` with
`1<=|P|<=3`, and `lambda(A union X)=10-|P|`.  Terminal-freeness forces
`C-A` to have at most two components, with the sharper triangle/path
deficiency restrictions stated in the theorem.

The remaining **small transverse-atom completion lemma** is precise: exclude
the four atom shapes together with all companion blockers in a terminal-free
labelled exterior.  In the three-vertex case, the missing mechanism is a
rooted positive-weight partition inside the one or two components of `C-A`;
the one-resource overlap alone does not supply it.  Once this lemma is
proved, safe contraction and terminal lifting give induction from the
computation-free base through order six and close the literal branch.

The known `W_5` profile still shows that a bare weighted-`K_4` assertion is
false and that the triangle exit is indispensable.  The small-atom reduction
does not prove the weighted splitter theorem, the literal branch, or T44.

## 5. Exact nonliteral obligation

Assume T44 is false.  Choose a vertex-minimal counterexample and then a
`K_{4,4}` model
minimising its nontrivial bags and total branch-tree size.  Contracting an
internal branch edge preserves the displayed model and target-freeness; by
minimality it destroys seven-connectivity.  Equivalently, that edge lies in
an exact seven-cut.

The cut boundary is now sharply sparse in a local sense:
`delta(G[Z])<=3`.  This follows from a human seven-vertex double-cone theorem
and an independent exhaustive atlas audit.  It supplies a secondary cut of
order at most three inside `Z`, but does not decide how branch bags cross
that secondary cut.

This is a certificate, not a peel.  It does not imply that:

- a component of the cut lies inside the split branch bag;
- the cuts belonging to different branch edges are laminar;
- contracting either side preserves seven-connectivity;
- the eight branch labels survive a reconstruction; or
- the model can be made smaller.

The first safe trace statement is weaker.  If an exact cut meets at least
seven model bags, at most one complementary component can be disjoint from
the entire model; otherwise two such components are anticomplete near-full
model bridges and force the target.  A bag avoiding the cut lies in one
component, and opposite-shore avoiding bags lie in the same component.  A
component containing pieces of model bags is not an exterior bridge, so no
six-trace bound follows.

The desired lift is therefore a **model-trace rotation theorem**: for an
internal branch-tree edge and its exact seven-cut, either two genuinely
external near-full components close the target, or a labelled rerouting
strictly improves the chosen model.  The proof must split the trace by
shore and retain the four opposite-shore contacts during uncrossing.

## 6. Audited shortcut barriers

The [fat-triangle and split-theta barriers](../barriers/hc7_k44_shortcut_certificate_barriers.md)
show that neither seven units of local triangle linkage nor six alternate
paths around one split branch edge force the target in isolation.  These
graphs are not seven-connected.  Their role is to require global attachment
data in the literal exchange and nonliteral rotation steps.

## 7. Critical-host refinement, not a target pivot

If universal T44 stalls, the same model can be studied inside the exact
critical host needed for Conjecture 21.  For an internal branch edge `uv`,
there are two responses:

1. `G/uv` is not seven-connected, returning an exact two-shore seven-cut;
2. `G/uv` is seven-connected and six-colourable, equivalently `G-uv` has a
   six-colouring in which `u,v` receive the same colour.

A synchronization lemma combining that equal-colour response, the four
opposite-shore branch contacts and Kempe chains could rotate the model when
separator ownership alone cannot.  This is a conditional proof strategy;
T44 remains the sole declared target and is abandoned only after an actual
seven-connected target-free counterexample is independently verified.

## 8. Stop rules

- A false weighted trichotomy, portal census or proposed peel is recorded as
  RED and repaired; it is not a reason to abandon T44.
- A bounded search never supports an unbounded inference.
- A T44 counterexample must be checked independently for seven-connectivity,
  a `K_{4,4}` model and absence of every `K_7^-` minor model.
- Conjecture 21 is not declared proved until the literal completion, the
  nonliteral lift, the application of the Kawarabayashi--Toft theorem and
  two independent internal final audits are all present.
