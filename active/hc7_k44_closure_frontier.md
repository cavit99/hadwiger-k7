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
8. [Every such atom is in fact a singleton, and every crossing blocker has
   exact one-resource overlap with a bipartite order-seven
   boundary](../results/hc7_k44_positive_atom_elimination.md).
9. [Every connected tight shore has an actual bipartite `3`-by-`4`
   boundary; a minimum nonsingleton crossing blocker is three-connected of
   minimum degree at least four and has two exact three-cut
   profiles](../results/hc7_k44_tight_boundary_and_minimum_blocker.md).
10. [An adjacent singleton edge has an exact contraction cut with a complete
    two- versus three-component trace
    dichotomy](../results/hc7_k44_adjacent_singleton_contraction_trace.md).
11. [The two-component whole-shore trace has exact unbalanced separator and
    balanced endpoint-miss
    profiles](../results/hc7_k44_adjacent_singleton_shore_split_profiles.md).
12. [The two one-endpoint miss types cannot coexist in the balanced
    `2+2` split](../results/hc7_k44_balanced_shore_split_one_sidedness.md).
13. [Every unbalanced or balanced two-component literal-shore split yields
    an explicit `K_7^-` minor](../results/hc7_k44_two_component_shore_split_elimination.md).
14. [Every three-component whole-shore trace yields an explicit `K_7^-`
    minor](../results/hc7_k44_three_component_trace_elimination.md).
15. [In the core-concentrated two-component trace, every rooted `K_5` has
    joint endpoint-contact rank at most three; failure of the exact
    two-helper split returns a new proper connected separator
    side](../results/hc7_k44_core_concentrated_joint_contact_reduction.md).

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

The audited contraction obstruction is exact.  For a three-contractible
edge `uv`, contraction fails the boundary system precisely when a nonempty
set `X subseteq V(C)-{u,v}` is tight and has both `u,v` in its boundary.
This includes disconnected and co-spanning witnesses; sets containing the
contracted vertex preserve their preimage boundary and weight.

If no terminal configuration and no safe edge exists, the audited
all-edge-atom theorem reduces a minimum tight atom to a singleton `A={a}`.
Its exact neighbourhood is a bipartite `3`-by-`4` seven-cut.  For a crossing
three-contractible edge `ab`, every connected tight blocker has normal form

```text
partial X = {a,b} dotcup K,    |K|=5,
```

and meets `N_G(a)` in exactly the exterior vertex `b`.  The blocker boundary
is another bipartite `3`-by-`4` seven-cut.

### 4.1 Nonsingleton minimum blocker

Choose `X` of minimum order among the connected tight blockers of `ab` and
put `H={b} dotcup K`.  If `X` is nonsingleton, the new minimum-blocker theorem
proves all of the following:

```text
G[X] is three-connected,    delta(G[X])>=4;
every k in K has at least two neighbours in X;
some p in N_X(a) has X-p full to H and |N_K(p)|<=2.
```

Moreover, deleting any three-cut leaves at most three components.  In the
three-component case either two `K`-resources meet all three components and
the other three are component-exclusive, one per component; or one component
contains every `X`-neighbour of both `a,b`, exactly three `K`-resources are
not supported wholly inside a single component and meet that component, and
each other component owns one of the remaining resources and meets at least
two of the first three.

The explicit closing criterion is now a bisection problem.  Find disjoint
adjacent connected sets `U,V subseteq X`, orient them so that `U` sees `a`,
and find `h_0 in H` with

```text
|H-(N_D(U) union {b,h_0})|
  + |H-(N_D(V) union {h_0})| <= 1,    D=partial X.
```

The two-helper construction then gives a `K_7^-` model with twenty quotient
contacts.  This **minimum-degree-four boundary-bisection lemma** is the exact
nonsingleton residue.

A targeted local screen checks the full labelled formula through blocker
order six and, independently, every three-connected graph-atlas host through
order seven against the spanning-bisection subformula.  All instances are
UNSAT.  This is audited bounded evidence with Z3 as the decisive trust
boundary; it is not an unbounded inference.

The three-cut profiles alone do **not** justify keeping their components
intact in the bisection.  The exact route-nonclosure is the graph

```text
X_0 = K_3[Q] join (K_2[W_1] dotcup K_2[W_2] dotcup K_2[W_3]).
```

Let `Q={t_0,t_1,t_2}`.  On the boundary
`D={a,b,c_1,c_2,e_1,e_2,e_3}`, give `a` the sole neighbour `t_0`, give each
of `b,c_1,c_2` all six vertices in the three `W_i`, and give `e_i` precisely
the two neighbours in `W_i`.  This profile is three-connected with minimum
degree four, satisfies every relative boundary inequality and strict
minimum-blocker inequality, has all five `K`-resources multiply attached,
and has the special vertex `p=t_0`.  The three-cut `Q` realizes the first
audited component profile exactly.

Any nondegenerate spanning bisection which keeps each `W_i` intact has three
exclusive-resource misses across its two sides.  Omitting one `h_0` removes
only one, leaving defect two and hence only nineteen guaranteed quotient
contacts.  This does not refute the bisection lemma: splitting a component
closes immediately, for example `V={v_1}`, `U=X_0-{v_1}`.  It refutes only
the attempted inference from the component profile to a
component-respecting bisection.

The natural **intra-component nonseparating-transversal** repair is itself
false at the level of all audited local data.  The explicit order-nine
[polarized profile](../barriers/hc7_k44_intra_component_transversal_barrier.md)
uses the same graph `K_3 join (3K_2)`, but gives `a` the support
`{t_0,r_1,r_2,r_3}`, gives `b,c_1` the three `l_i`, gives `c_2` the three
`r_i`, and gives `e_i` both vertices of `W_i`.  A connected subset of one
`W_i` seeing `b,c_1,c_2,e_i` must equal `W_i`, after which its complement
misses `e_i`.  Thus there is no component-local witness.  This profile is
an abstract incidence counterexample to that inference; it is not known to
occur in an ambient seven-connected blocker.

The full bisection still closes the polarized profile.  Take

```text
U={t_0,l_1,l_2},    V=X-U,    h_0=c_2.
```

Then `U,V` are connected and adjacent, `U` sees `a,b` and three of the five
`K`-resources, and `V` is `H`-full.  The two defects are one and zero.

The requirement that `U` see `b` is nevertheless redundant.  A second
order-nine profile on the same graph gives `a` all six `W_i` vertices,
gives `b` only `t_2`, gives `c_1,c_2` the left and right triples, and gives
`e_i` both vertices of `W_i`.  It satisfies every audited local hypothesis
but has no component-local witness and no `H`-full-complement witness whose
first side sees `b`.  The same choice

```text
U={t_0,l_1,l_2},    V=X-U,    h_0=c_2
```

closes once the unnecessary `b` requirement is removed.  The crossing edge
`ab` supplies that helper contact for free.  More precisely, when `V` is
`H`-full, the bisection criterion is equivalent to requiring `U` to see `a`
and at least three of the five `K`-resources.

The exact unresolved nonsingleton subcase is therefore **support transfer**:
`V` is not `H`-full, so the resources supported wholly on `U` must be
coordinated with the single omitted resource `h_0`.  The explicit profiles
refute only the stronger repairs, not the full bisection lemma, weighted
splitter theorem, or T44.

### 4.2 Singleton blocker and its contraction trace

If `X={p}`, then `a,p` are adjacent degree-seven exterior vertices with
unique common neighbour `b` and disjoint literal-core label sets.  In a
vertex-minimal target-free host, contraction of `ap` returns an exact cut

```text
E={a,p} dotcup T,    |T|=5.
```

The complement has two or three components.  With three components, one
literal shore and one exterior vertex form `T`; the opposite shore meets at
least two components and `G[E]` is subcubic.  With two components, either:

1. all core vertices outside `T` lie in one component, which contains a
   `T`-rooted `K_5`; each of `a,p` meets at most three branch sets of every
   such model, and their total number of neighbours in `T` is at most five;
   or
2. `T` consists of a whole literal shore `S_0` and one vertex `x`, while
   both components meet the opposite shore.

The second case is now eliminated in full.  In an unbalanced split, the
exact small shore gives two endpoint-derived connected sets.  A path from
the common neighbour `b` to an unused opposite-shore core vertex gives a
third.  These sets form a triangle and are universal to four `S_0`-rooted
sets completed to `K_4^-`, for `3+12+5=20` contacts.

In a balanced `2+2` split, the audited one-sidedness theorem first excludes
coexistence of the two one-endpoint miss types.  If `R-F` is nonempty, either
one such component or a component missing both endpoints again supplies the
third member of a triangle universal to a `K_4^-` core.  If `R=F` consists
of the two split core vertices, their degree-seven neighbourhoods are exact.
A two-resource allocation closes every component of `D-(D cap S_1)`; the
last case `D=D cap S_1` contradicts disjointness of the endpoint label sets.
Thus every unbalanced and balanced shore split contains an explicit
`K_7^-` minor.

The three-component response is also eliminated uniformly.  Choose two
components meeting the opposite shore, remove one core vertex from each,
and choose a remaining connected component piece.  Each piece misses at
most one vertex of `E`, so the two removed core vertices repair all missed
`S_0` contacts and complete four core bags to `K_4^-`.  Distinct
representatives from `{a,p,x}` turn those two pieces and the untouched third
component into a triangle.  This covers all shore distributions
`3+1+0`, `2+2+0`, and `2+1+1`, again with twenty contacts.

Hence the **sole singleton residue** is the first two-component alternative:
all core vertices outside `T` lie in one component containing a
`T`-rooted `K_5`.  The new joint-contact theorem strengthens the two
separate contact bounds.  If `C_a,C_p` are the sets of model bags contacted
by `a,p`, then every such model satisfies

```text
|C_a union C_p| <= 3.
```

If either contact set has order three, it contains the other.  In particular,
the endpoint neighbour counts in `T` now total at most three, rather than
five.

There is also an exact target-producing split condition.  If the remote
component contains disjoint nonempty connected sets `U,V`, adjacent to
`a,p`, respectively, and the two endpoint-derived bags together miss at
most one of the five rooted bags, those two bags and the rooted `K_5` give
twenty contacts.  If this split is not obtained, a spanning-tree split of
the remote component—or, when its only endpoint neighbour is the common
neighbour `b`, of one rooted branch bag—returns a proper nonempty connected
set `Y` such that `N_G(Y)` is an actual separator.  Seven-connectivity gives

```text
|N_G(Y)| >= 7,
```

and equality makes every component of `G-N_G(Y)` full to the boundary.

The lower bound cannot simply be replaced by equality.  The verified
[order-three incidence barrier](../barriers/hc7_k44_core_concentrated_bisection_incidence_barrier.md)
satisfies every relative boundary inequality, fullness, unique common
endpoint incidence, the degree-seven counts, and joint contact rank three,
but every disjoint connected endpoint-anchored pair has total defect at
least two.  This is a local incidence counterexample only, not an ambient
seven-connected host; it shows that the boundary inequalities alone cannot
force the required bisection.  Notably, five of its six proper nonempty
sides are already tight, so a separator-based continuation remains viable.

The literal completion is therefore reduced to two explicit mechanisms:
the nonsingleton boundary-bisection lemma, and the singleton assertion that
one returned separator has order seven or supports compatible rooted
structure across a larger boundary.  The known `W_5` profile still shows
that a bare weighted-`K_4` assertion is false and that the triangle exit is
indispensable.  Neither remaining mechanism is closed, so the weighted
splitter theorem, literal branch, and T44 remain open.

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
