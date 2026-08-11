# The boundary-first donor gate and its exact nonclosure

**Status:** written theorem and recorded route nonclosure; separate
hash-pinned internal audit in the adjacent
[`_audit.md`](hc7_k7minus_five_centre_minimal_donor_gate_audit.md) note.
This note does not prove the `K_7^-` six-colour conjecture or close the
two-cut branch.

This note tests the proposed minimal-donor continuation of the audited
[unique-owner separator reduction](hc7_k7minus_five_centre_owner_nonedge_connector.md).
It proves a fixed-trace core theorem, identifies the exact effect of
boundary-first minimisation, and records why the proposed
connector-or-trace gate is not recursive with the present inputs.

Throughout, let `G` satisfy the critical-host hypotheses

\[
 \kappa(G)\ge 7,\qquad \delta(G)\ge 8,\qquad
 \chi(G)=7,
\]

every proper minor of `G` is six-colourable, and
`K_7^-` is not a minor of `G`.  Fix five independent degree-eight centres
`Z`, a two-cut of `G-Z`, and a target-free unique-owner model supplied by
the preceding reduction.

## 1. Two distinct donor classes

Let `U` be a bag of one of the spanning seven-bag models used in the
unique-owner reduction.  A **geometric model donor** is a nonempty proper
connected set `Y` contained in `U` such that

\[
                  G[U-Y]\text{ is connected}
        \quad\text{and}\quad N_G(Y)\text{ is a vertex cut}.       \tag{1.1}
\]

The proof of Proposition 3.6 in the unique-owner note returns a more
restricted object: its donor retains a designated model and a named far
bag.  A fixed-operation attempt may further choose a boundary edge and one
six-colouring after deleting that edge.  Call the resulting comparison
object a **labelled gate donor**.  This term does not assert that the new
colouring retains the original equal/distinct `pq` response.  Every
labelled gate donor is based on a geometric model donor, but the converse
is not proved.

This distinction is essential.  If the comparison class is restricted to
labelled gate donors, the model and colouring provenance survive but
there is no proved upper bound on `|N_G(Y)|`.  If the class is enlarged to
all geometric model donors, degree-eight singletons give an upper bound of
eight, but the labelled response need not survive.  The proposed gate
requires both conclusions at once.

## 2. Singletonisation does not respect boundary-first order

### Lemma 2.1 (a co-connected singleton exists)

Suppose `Y` satisfies (1.1), and suppose a nonempty connected set `V`
outside `U` is anticomplete to `Y`.  Then some vertex `v` of `Y` satisfies

\[
                 G[U-v]\text{ is connected},
        \qquad N_G(v)\text{ is a vertex cut}.                    \tag{2.1}
\]

#### Proof

Join a spanning tree of `G[Y]` to a spanning tree of `G[U-Y]` by one edge.
If `Y` is a singleton, use its only vertex.  Otherwise choose a leaf `v`
of the first tree different from the endpoint of the joining edge.  The
combined tree with `v` deleted spans `U-v`, so `G[U-v]` is connected.

The set `V` is anticomplete to `v`.  After deleting `N_G(v)`, the singleton
`{v}` and the nonempty set `V` lie in different components.  Thus
`N_G(v)` is a vertex cut.  \(\square\)

The lemma does **not** imply

\[
                         |N_G(v)|\le |N_G(Y)|.                    \tag{2.2}
\]

Neighbours of `v` inside `Y` are not counted in `N_G(Y)`.  The failure is
sharp even for a minimum cut.  For `k>=1`, glue two copies of `K_{k+2}`
along a common `K_k` called `T`, and let `A` be the two vertices belonging
only to the first copy.  Put `U=A union {t}` for any `t in T` and `Y=A`.
Then

\[
            N_G(Y)=T,\qquad |N_G(Y)|=k,
        \qquad d(v)=k+1\quad(v\in Y).                            \tag{2.3}
\]

Both `Y` and `U-Y` are connected, and each singleton from Lemma 2.1 has a
strictly larger boundary.  For `k=7` the graph is seven-connected.  This
example is target-rich and not contraction-critical; it refutes only the
abstract singleton-minimisation step.

Consequently a lexicographic choice in the order

\[
       \bigl(|N_G(Y)|,\ |Y|,\ \text{missed protected contacts}\bigr) \tag{2.4}
\]

cannot first replace `Y` by a singleton.  The first coordinate may become
worse.

## 3. What a fixed colouring does give

The next theorem is the exact trace statement available from a
boundary-first minimum.

### Theorem 3.1 (fixed-trace core inflation)

Let `(U,Y)` underlie a labelled gate donor, put `T=N_G(Y)`, and let `V` be
its named nonempty foreign bag anticomplete to `Y`.  Choose an edge
`e=yt` with `y in Y` and `t in T`, and fix a proper six-colouring `c` of
the proper minor `G-e`.  For `v in Y`, put

\[
        L(v)=[6]\setminus c\bigl(N_G(v)\cap T\bigr).             \tag{3.1}
\]

Let `K` be vertex-minimal subject to `K subseteq Y` and `G[K]` not being
`L`-colourable.  Then:

1. `y in K`, and `G[K]` is connected;
2. the only list violation of `c|K` is at `y`, where
   `c(y)=c(t) \notin L(y)`;
3. the partition induced by `c` on `N_G(K)` is legal on the exterior
   closed side and is rejected by the intact `K`-side; and
4. either `K=Y`, or there is a nonempty proper connected set
   `Y' subsetneq Y` such that `G[U-Y']` is connected, `Y'` remains
   anticomplete to `V`, and

   \[
                         |N_G(Y')|>|T|                            \tag{3.2}
   \]

   whenever `(U,Y)` is lexicographically minimum in a comparison class
   containing every such donor-eligible subset.

#### Proof

If `c(y)` and `c(t)` were different, `c` would already be a six-colouring
of `G`.  Hence `c(y)=c(t)`.  The restriction of `c` to `Y-y` uses only
colours permitted by (3.1), while properness on every other edge incident
with `y` gives `c(y) \notin L(y)`.

If `G[Y]` were `L`-colourable, that colouring and `c` outside `Y` would
combine to six-colour `G`.  Hence `K` exists and contains `y`.  A
vertex-minimal non-list-colourable graph is connected.  Since `c` is
proper on every edge other than `e`, assertion 2 follows.

Deleting `K` removes the only possibly monochromatic edge `e`, so `c`
is proper on `G-K`.  It therefore supplies the asserted exterior boundary
partition.  If the same partition extended through `G[K union N_G(K)]`,
aligning colour names would give each vertex of `K` a colour absent from
all its external neighbours.  These lists are contained in the lists in
(3.1), contradicting the choice of `K`.  This proves assertion 3.

Suppose `K` is proper in `Y`.  Let `W` be the component of `G[U-K]`
containing the connected set `U-Y`, and put `K^*=U-W`.  The set `K^*` is
contained in `Y`, is connected, and has connected complement in `U`.
If `K^*` is proper in `Y`, take `Y'=K^*`.  If `K^*=Y`, take for `Y'` any
component of `G[Y-K]`.  In the latter case `W=U-Y`; every component of
`Y-K` and `W` attaches to the connected set `K`, so deleting the selected
component leaves `U-Y'` connected.

In both cases `Y'` is a nonempty proper connected subset of `Y`, its
complement in `U` is connected, and `V` remains a far side of
`N_G(Y')`.  It is therefore donor-eligible.  Lexicographic minimality
excludes `|N_G(Y')|<|T|`; equality is excluded by `|Y'|<|Y|`.  This gives
(3.2).  \(\square\)

Thus, whenever the comparison class is closed under the donor-eligible
subsets constructed above, the fixed trace does not produce a descent in
the boundary-first order.  It leaves one of two outcomes:

\[
 \boxed{
 \begin{array}{c}
 \text{the whole donor is a one-extra-colour list-critical core,}\\
 \text{or a smaller donor-eligible set has a strictly larger boundary.}
 \end{array}}                                                   \tag{3.3}
\]

The smaller set need not contain `K`, so it need not retain the fixed
trace.  The third coordinate in (2.4) cannot repair this: the strict change
has already occurred in the first coordinate.  If the labelled comparison
class is not closed under these subsets, even this comparison is
unavailable; that restriction weakens rather than repairs the gate.

## 4. The exact order-seven endpoint

Suppose a boundary-first minimum labelled gate donor has `|T|=7`.  The
donor `Y` is a component of `G-T`.  Corollary 2 of the separately audited
[three-component seven-cut exclusion](../results/hc7_k7minus_three_component_seven_cut_exclusion.md)
gives exactly one opposite component, and seven-connectivity makes both
components adjacent to every vertex of `T`.

The graph `G[T]` has no `K_5` minor.  Otherwise its five branch sets,
together with the two full complementary components, form an explicit
`K_7^-` minor whose only possible missing adjacency is between those two
components.  The established `t=5` case of Hadwiger's conjecture therefore
gives

\[
                              \chi(G[T])\le4.                    \tag{4.1}
\]

Contracting either full component together with any prescribed nonempty
independent block of `G[T]` shows that both closed-shore extension
languages meet every exact-block cylinder.  The audited
[split-boundary synchronisation theorem](../results/hc7_split_boundary_synchronization.md)
then gives a common partition whenever `G[T]` is split.  Hence every
target-free survivor has

\[
                 |T|=7,\qquad G[T]\text{ nonsplit}.              \tag{4.2}
\]

If `K=Y` in Theorem 3.1, the whole donor is the one-extra-colour core.  If
`K` is proper, the theorem exposes a smaller geometric donor but does not
retain the trace on it.  In a comparison class closed under that donor its
boundary has order at least eight; without closure, seven-connectivity gives
only order at least seven and no labelled-gate comparison is available.

This is not secretly a common-partition theorem.  The separately audited
[boundary-operation parity barrier](../barriers/hc7_exact7_separator_boundary_operation_parity_barrier.md)
has a full exact order-seven cut, disjoint shore languages, and all the
independent-block and boundary operations used above, but no common
partition.  Its open shores contain explicit `K_7` models and it is not
contraction-critical, so it is not a counterexample to the desired host
theorem.  It shows precisely that boundary minimality and the available
operations do not break nonsplit parity; target exclusion or full
criticality must do additional work.

## 5. What happens above order seven

If the comparison is restricted to labelled gate donors, no present
theorem bounds `|T|` from above.  The audited
[five-bag separator-excess barrier](../barriers/hc7_five_bag_separator_excess_barrier.md)
shows that seven-connectivity, `K_7`-minor exclusion, edge-maximality, and
labelled near-clique geometry alone permit supported separator order to be
arbitrarily large.  That family is six-colourable and does not satisfy the
critical-host assumptions; it identifies the colouring data which a
positive theorem must spend.

There is a further formal defect.  For `|T|>7`, Theorem 3.7 of the
unique-owner note gives only that `T` is an actual separator.  It does not
give exactly two components of `G-T`, nor does seven-connectivity make a
chosen far component adjacent to every vertex of `T`.  Thus a conclusion
phrased as operations on “the two full shores” is not available in this
case.

If instead the comparison class is enlarged to all geometric model donors,
then its minimum boundary order is at most eight.  Indeed, in every model
(3.14) of the unique-owner note the three ordinary owner bags have the form

\[
                       U_i=R_i\cup\{z_i\}
              \qquad(i\in\{c,d,e\}).                            \tag{5.1}
\]

For each such bag, `{z_i}` is connected, `U_i-z_i=R_i` is connected, and
`N_G(z_i)` is an actual separator of order eight.  The last assertion uses
the degree-eight hypothesis and the existence of at least 25 exceptional
vertices, which leaves a vertex outside `N_G[z_i]`.

Seven-connectivity now gives the exact dichotomy

\[
             \min |N_G(Y)|\in\{7,8\}.                            \tag{5.2}
\]

If the minimum is eight, the second coordinate of (2.4) forces `Y={v}`
for some degree-eight vertex `v`.  Hence `T=N_G(v)` is the familiar
exceptional-neighbourhood boundary.  It need not be the desired boundary
`Z union {r,s}`; for each guaranteed candidate `v=z_i` it contains none
of the other four selected centres.  The third coordinate may select a
different degree-eight singleton, so no stronger assertion is made.

This enlargement does not by itself retain a usable common response.  On
the singleton closed side `G[T union {v}]`, every six-colouring uses at
most five colours on `T`, since `v` is adjacent to every vertex of `T`.
On the opposite closed side `G-v`, every six-colouring uses all six colours
on `T`; a colour
missing from `N_G(v)` would extend to `v` and six-colour `G`.  Thus the two
unmodified shore languages are separated exactly by boundary block count.
Proper-minor operations may alter those languages, but no present theorem
lifts a common operated partition while retaining the unique-owner labels.

The exact-order-eight
[opposite-response Kempe barrier](../barriers/hc7_opposite_response_kempe_bridge_barrier.md)
confirms that rich proper-operation responses and a Kempe route through a
common deletion do not by themselves provide this lift.  That construction
contains an explicit `K_7` minor and is not minor-minimal, so again it is a
mechanism barrier rather than a host counterexample.

## 6. Decisive route nonclosure

The owner-nonedge connector remains terminal by Theorem 4.1 of the
unique-owner note.  In its absence, the proposed boundary-first
connector-or-trace gate does not close the two-cut branch.

The failure is a quantifier incompatibility:

\[
 \boxed{
 \begin{array}{c}
 \text{restrict donors to retain the model and chosen operation, and no}\\
 \text{boundary bound follows from the available inputs;}\\
 \text{in any donor class closed under the geometric comparison,}\\
 \text{a proper fixed-trace core exposes a smaller donor only}\\
 \text{by inflating the boundary and possibly losing the trace;}\\[2mm]
 \text{allow all geometric donors, and the minimum is seven or eight,}\\
 \text{but an order-eight singleton need not retain those labels.}
 \end{array}}                                                   \tag{6.1}
\]

At order seven, the surviving boundary is nonsplit and full.  The
fixed-trace core either fills the donor, or exposes a smaller geometric
donor whose boundary inflates when the comparison class is closed; in the
restricted class the trace comparison may simply be lost.  Above order
seven, the available theorem does not even give two full shores.  At the
broad order-eight endpoint, it is an exceptional-neighbourhood interface
whose two original extension languages have incompatible block counts.

Accordingly, repeating this boundary-first unlabelled minimisation supplies
no new terminal conclusion.  Sufficient genuinely new host-level repairs
include:

1. a **compatible two-donor theorem** retaining prescribed near-clique
   contacts and one fixed proper-minor response;
2. a theorem that nonsplit exact-seven parity forces an explicit
   `K_7^-` model in the unique-owner host; or
3. an operation-preserving transfer from a labelled donor to the
   neighbourhood of a named exceptional vertex.

The list is not asserted to be exhaustive.  The scoped finite experiments
favour the first possibility but do not prove it.  Without an additional
statement of this kind, the minimal-donor connector-or-trace mechanism is
decisively nonterminal.

## Claim status and dependencies

- Lemma 2.1, Theorem 3.1, and the deductions in Sections 4--6 are proved
  here and covered by the adjacent internal audit.
- The spanning model and its owner bags come from the separately audited
  unique-owner separator reduction.
- The exact seven-cut component statement, exceptional count, and
  degree-eight conclusions are separately audited critical-host inputs.
- The three cited barriers have separate GREEN internal audits and retain
  the limitations stated above.
- No construction in this note is a counterexample to the `K_7^-`
  six-colour conjecture, and no closure of the two-cut branch is claimed.
