# Seven-connected `K_{4,4}` closure frontier

**Status (2 September 2026):** T44 is the sole active completion target.  It is
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
16. [For a nonsingleton blocker, the seven-resource inequalities imply a
    five-support six-boundary inequality; either a closing bond exists or a
    minimum support-full bond side opposite the distinguished `a`-neighbour
    has one of three explicit block forms, with a sharper path outcome when
    it sees `b`](../results/hc7_k44_five_support_bond_reduction.md).
17. [Every bond splitting three supports is terminal; this eliminates the
    four-connected nonsingleton case and every three-component
    three-cut](../results/hc7_k44_three_support_bond_and_threecut_reduction.md).
18. [At a surviving two-component three-cut, the five supports have one of
    two exact incidence types and each support meets the cut in at most one
    vertex; a smallest three-support component has a four-connected
    triangle-boundary torso](../results/hc7_k44_two_component_threecut_support_normal_form.md).

If the four bags span `C`, the tetrahedral exception is impossible: its
total portal coverage is four, while seven-connectivity forces
`|N_S(C)|>=7`.  The consolidated internal [cold
audit](../results/hc7_k44_closure_local_normal_forms_audit.md) covers and
hash-pins the five local statements it names.  The other promoted results
above have their own adjacent hash-pinned internal audits.

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

Put `D=partial X` and, for `Z subseteq X`, define
`N_D(Z)=N_G(Z) cap D`.  The earlier sufficient two-helper criterion asks for
disjoint adjacent connected sets `U,V subseteq X`, oriented so that `U` sees
`a`, and an `h_0 in H` with

```text
|H-(N_D(U) union {b,h_0})|
  + |H-(N_D(V) union {h_0})| <= 1.
```

The two-helper construction then gives a `K_7^-` model with twenty quotient
contacts.  Although the original criterion does not require the sets to cover
`X`, the audited [spanning-extension and split-count
corollary](../results/hc7_k44_spanning_two_helper_split_count.md) shows that
every positive pair can be enlarged, without increasing either defect, to a
connected partition `X=U dotcup V`.

For such an ordered spanning partition, let `s(U,V)` be the number of the five
`K`-resources whose supports meet both sides, and put `epsilon_b(U,V)=1` when
`V` misses `b`, and zero otherwise.  The exact optimized defect is

```text
min_{h_0 in H} defect(U,V;h_0)
  = max(0,4-s(U,V)+epsilon_b(U,V)).
```

Thus the numerical two-helper criterion is equivalent to

```text
s(U,V) >= 3+epsilon_b(U,V).
```

There are exactly two modes: `V` sees `b` and at least three `K`-supports
split, or `V` misses `b` and at least four split.  This equivalence concerns
that sufficient two-helper inequality, not target existence itself.  It
remains useful bookkeeping for the hostile screen below, but the
`b`-independent three-support construction later in this section supersedes
it as the live terminal threshold.

A targeted local screen checks the full labelled formula through blocker
order six and, independently, every three-connected graph-atlas host through
order seven against the spanning-bisection subformula.  A second screen
checks both the full and the stronger anchored negations on all 422 eligible
minimum-degree-four hosts of order eight.  It also checks all 16 connected
four-regular hosts of order nine, ten four-connected planar hosts of order
nine, and six sharp three-cut join perturbations.  Every formula is UNSAT.
These are audited bounded results with Z3 as the decisive trust boundary;
there is no independently checkable UNSAT certificate and no unbounded
inference.  Counts, graph6 digests, exact formulas and reproduction commands
are in the [spanning-split hostile
screen](experiments/k44_literal_spanning_split_search/README.md).

For `d in D`, put `R_d=N_X(d)`.  Minimum-blocker strictness implies

```text
q(W)=|N_X(W)|+|{k in K:R_k meets W}| >= 6
```

for every nonempty proper connected `W subset X`.

The audited [three-support bond and three-cut
reduction](../results/hc7_k44_three_support_bond_and_threecut_reduction.md)
changes the terminal threshold.  The two-helper formula by itself asks for
four split supports when the second helper misses `b`, but a different
literal-core allocation uses all seven boundary-rooted bags, the two bond
shores and the unused core vertex.  A six-row proof gives at least twenty quotient
contacts whenever **any three** `K`-supports split, regardless of the
`a,b` distribution.  A dependency-free exact check corroborates all 160
core-colour and owner assignments; the written table is the unbounded proof.
Thus target-freeness gives the global restriction

```text
every bond of X splits at most two K-supports.
```

Choose the distinguished vertex `p`, and among all bonds
`X=U dotcup V` with `p in V` and `U` meeting all five `K`-supports, minimize
`|U|`.  The earlier minimum-side theorem now has

```text
2 <= |M| <= s(U,V) <= 2.
```

All triangle and claw forms disappear.  The graph `X[U]` is an induced path,
the two split supports have unique `U`-vertices at its ends, and the other
three supports lie wholly in `U`.  Their path hulls have positive length and
are pairwise edge-disjoint.  Every vertex of `U` meets `V`; each path end has
at least three neighbours in `V`, and every internal vertex at least two.
Every subpath is a bond and satisfies the exact split-count formula in the
promoted theorem.  In every bipolar order of `X`, the five support intervals
have depth at most two and their interval-intersection graph is a forest.

The same result eliminates the entire four-connected nonsingleton case.  In
an abstract four-connected graph satisfying `q>=6`, with each of its five
supports of order at least two, the three internal support hulls give an
acyclic parity triple.  Chen--Ding--Yu--Zang supply a
three-support bond or a facial obstruction.  In the latter outcome, the
audited Euler inequality supplies an off-face support; replacing one pair
gives a second acyclic triple which cannot lie on a facial cycle sharing at
least three vertices with the first.  Hence every such four-connected graph
has a three-support bond, contrary to the global restriction above.

Every nonsingleton survivor therefore has connectivity exactly three.  For
every three-cut `T`, each component of `X-T` meets `U-T`.  Both possible
three-component profiles are impossible.  In the exceptional profile, one
component bond splits the three non-component-exclusive supports.  In the
equality profile, two-linkages from pairs in the three component-exclusive
supports to two vertices of `T` combine into a bond splitting all three.
Thus every three-cut leaves exactly two components.

The audited [two-component support normal
form](../results/hc7_k44_two_component_threecut_support_normal_form.md)
classifies such a cut `T`, with components `P,Q`.  Each support meets `T` in
at most one vertex, and exactly one or two supports meet both components.
If two do, the other three are wholly contained in `P` or `Q` with a `1+2`
distribution.  If one does, two further supports occur on each component
side; at most one on each side meets `T`, and any two such cross-side
cut contacts use the same vertex of `T`.

Choose a minimum-order component `P`, over all three-cut components meeting
exactly three supports, and put `T=N_X(P)`.  The torso

```text
X[P union T] + K_T
```

is four-connected.  Exactly one or two of the three incident supports are
wholly contained in `P`; the others have vertices outside `P`.  Every
connected subset of `P` retains the corresponding three-support
six-boundary inequality.  In addition, every choice of a two-element pair
in a whole support on each original component and a cross-component pair in
a bridge support is weakly linkable in the sense of
Chen--Ding--Yu--Zang.  This is a universal family of obstructions, not one
fixed inconvenient triple.

The exact nonsingleton obligation is now the **triangle-boundary torso
bisection lemma**: find a nonempty connected set inside `P` whose torso
complement is connected, which meets every externally continuing support
and splits every support wholly contained in `P`.  This set is exactly one
shore of a global bond splitting all three incident supports.  The proof
cannot use only the torso connectivity and local inequality: at least one
retained global input must enter.  Available inputs include the global
at-most-two-split bond restriction, complementary-support provenance, the
two supports outside the torso, the minimum path, and the distinguished
`a,b` incidence.

One tempting local step is genuinely false.  The explicit
[minimum-path transversal barrier](../barriers/hc7_k44_minimum_path_internal_transversal_barrier.md)
satisfies the path, attachment and boundary hypotheses but has no bond which
simultaneously separates a prescribed `p` from a prescribed `R_b` vertex and
splits the three prescribed internal supports.  It has many other
three-support bonds and is four-connected, so it does not refute the present
theorem or the triangle-boundary torso bisection lemma.  A proof must use the
global
at-most-two-split restriction, may change the selected triple, and should use
the actual three-cut.

Nor can one contract the two components immediately and finish from the
mandatory root incidences alone.  The exact [two-component quotient
barrier](../barriers/hc7_k44_two_component_quotient_completion_barrier.md)
has the `2+1+2` support distribution and both distinguished roots on the
three-support component, yet its thirteen-vertex literal-core quotient has
exact `K_7^-` contact optimum nineteen.  It deliberately fails support
multiplicity, `q>=6`, and the minimum-path conclusion, so it is not a
counterexample to the live theorem.  It proves that the next step must retain
the uncontracted component structure supplied by those hypotheses.

Even the selected four-connected torso is not sufficient in isolation.  The
exact [stripped-torso
barrier](../barriers/hc7_k44_three_support_torso_bisection_barrier.md) is
`K_5` with one whole and two external supports; all three local scores equal
six, but any set meeting both external traces contains the whole support.
It lacks the complementary component, the two remaining supports, and the
global at-most-two-split bond restriction, minimum path, and distinguished
incidences, so it does not refute the live torso bisection lemma.

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
The proof retains a fixed spanning rooted model and marked data: either a
two-part tree split of `R` with endpoint anchors, or a two-part split of one
rooted branch bag, together with a named rooted bag anticomplete to the
deficient part `Y` and the relevant endpoint/root ownership.

The theorem supplies no upper bound on `|N_G(Y)|`.  The verified
[order-three incidence barrier](../barriers/hc7_k44_core_concentrated_bisection_incidence_barrier.md)
satisfies every relative boundary inequality, fullness, unique common
endpoint incidence, the degree-seven counts, and joint contact rank three,
but every disjoint connected endpoint-anchored pair has total defect at
least two.  This is a local incidence counterexample only, not an ambient
seven-connected host; it shows that the boundary inequalities alone cannot
force the required split.  It does not refute the possibility of selecting
an order-seven returned separator; five of its six proper nonempty sides are
already tight.  It shows only that the listed local incidence data do not
produce the target-making one-defect split.

The literal completion is therefore reduced to the nonsingleton
triangle-boundary torso bisection lemma and elimination of the entire
singleton core-concentrated profile.
For the singleton profile, obtaining an order-seven marked separator is only
a milestone: no theorem currently turns that certificate into the target or
a safe contraction.  For a larger returned boundary, no descent/rerouting
theorem with a strictly decreasing complexity is known.  The known `W_5`
profile still shows that a bare weighted-`K_4` assertion is false and that the
triangle exit is indispensable.  Neither remaining literal theorem is
closed, so the weighted splitter theorem, literal branch, and T44 remain open.

### 4.3 Cold-start handoff

A new agent should treat the following as the exact live theorem pair.

1. **Nonsingleton triangle-boundary torso bisection.**  Work under the
   hypotheses and conclusions of the [three-support bond
   reduction](../results/hc7_k44_three_support_bond_and_threecut_reduction.md).
   Choose a three-cut `T`; it has exactly two components `P,Q`, both meeting
   the sequential minimum support-full path.  By the [two-component support
   normal form](../results/hc7_k44_two_component_threecut_support_normal_form.md),
   each support meets `T` at most once and the supports have one of two
   incidence types: two bridge supports plus a `1+2` distribution of three
   component-contained supports, or one bridge support plus two supports on
   each component side with the stated common-cut-vertex restriction.
   Over all three-cut/component pairs whose component meets exactly three
   supports, select one with minimum component order; its triangle-boundary
   torso is four-connected.  Find inside it a connected
   nonseparating set meeting every externally continuing support and
   splitting every whole support.  The global bond restriction, the two
   complementary supports, exact subpath formula, bipolar interval forest,
   distinguished `a,b` incidence, and minimum-path attachment bounds are
   available.  The [minimum-path transversal
   barrier](../barriers/hc7_k44_minimum_path_internal_transversal_barrier.md)
   only forbids prescribing one fixed support triple and anchor separation;
   a proof may choose the triple and use both sides of the actual cut.
   The [quotient-only barrier](../barriers/hc7_k44_two_component_quotient_completion_barrier.md)
   additionally forbids contracting both components before exploiting
   `q>=6`, support multiplicity, and the path attachments.
   The [stripped-torso barrier](../barriers/hc7_k44_three_support_torso_bisection_barrier.md)
   shows that four-connectivity and the local three-support inequality alone
   are also insufficient.
2. **Singleton core-concentrated completion.**  Prove that no target-free
   graph satisfies the hypotheses of the [joint-contact and separator
   theorem](../results/hc7_k44_core_concentrated_joint_contact_reduction.md).
   Its marked separator certificate is the current input.  Two possible next
   milestones remain unproved: an exact-seven marked-certificate completion,
   and a larger-boundary descent/rerouting theorem with a declared strictly
   decreasing complexity.  Equality by itself is not a proved terminal
   condition, and no descent monovariant has been established.

Only after both literal residues close does the separate nonliteral
model-trace rotation theorem in Section 5 become the remaining T44
obligation.

For re-entry, run

```bash
uv run python3 tools/research_index.py check
uv run python3 tools/research_index.py report
uv run python3 tools/research_index.py verify
```

Then inspect
`.cache/research/context_hc7.target.k44_sevenconnected_closure.md`.  The
generated pack is a retrieval aid; this frontier, `active/INDEX.md`, and the
ledger remain authoritative.

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
critical host needed for Conjecture 21.  The audited
[critical safe-contraction theorem](../results/hc7_k44_critical_safe_contraction.md)
gives a first sharp distinction in the literal case.  If the specified
literal core has exterior order at least seven, its exterior contains a safe
three-contractible edge.  Otherwise the singleton-atom theorem would produce
a degree-seven vertex with a bipartite `3`-by-`4` neighbourhood, contradicting
Dirac's neighbourhood-independence inequality.

This does not create an induction.  Contracting the safe edge gives a
six-colourable proper minor, not another seven-contraction-critical host, and
the quotient is not asserted to remain seven-connected.  The universal
literal residues can therefore reappear after the first contraction.  The
useful critical-host datum attached to that edge is a six-colouring of
`G-uv` in which `u,v` have the same colour and are joined in each of the five
corresponding bichromatic subgraphs.  These five paths are not asserted to
be mutually disjoint or otherwise compatible.

More generally, for an internal branch edge `uv`, there are two structural
responses:

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
- Do not restart generic donor minimisation without a theorem preserving the
  marked rooted model and boundary labels; the [boundary-first donor
  route](hc7_k7minus_five_centre_minimal_donor_gate.md) records the failure of
  the unlabelled minimisation class.
- Palette synchronization belongs only to the conditional critical-host
  refinement in Section 7; universal T44 supplies no colouring response to
  synchronize.
- Static branch-set contact profiles and one split-edge theta counts are not
  terminal certificates.  The [core-concentrated incidence
  barrier](../barriers/hc7_k44_core_concentrated_bisection_incidence_barrier.md)
  and [shortcut-certificate barriers](../barriers/hc7_k44_shortcut_certificate_barriers.md)
  record their exact limited scopes.
- A T44 counterexample must be checked independently for seven-connectivity,
  a `K_{4,4}` model and absence of every `K_7^-` minor model.
- Conjecture 21 is not declared proved until the literal completion, the
  nonliteral lift, the application of the Kawarabayashi--Toft theorem and
  two independent internal final audits are all present.
