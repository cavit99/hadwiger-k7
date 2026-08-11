# The cross-edge paired-donor gate and its exact nonclosure

**Status:** written theorem and recorded route nonclosure; separate
hash-pinned internal audit in the adjacent
[`_audit.md`](hc7_k7minus_five_centre_paired_donor_gate_audit.md) note.
The results are unbounded, but they do not close the five-centre two-cut
branch or prove the `K_7^-` six-colour conjecture.

This note runs the single-edge paired-donor continuation proposed after the
[one-donor gate](hc7_k7minus_five_centre_minimal_donor_gate.md).  It
identifies the only way one single-edge-deletion colouring can give two
genuine donor traces, proves the resulting joint response theorem, and
determines the exact effect of joint minimisation.  A single cross-edge
aligns the two traces, but it does not turn boundary inflation into overlap.
The present unique-owner reduction does not supply the required cross-edge
donor pair.  Common deletions of two or more edges are outside the theorem.

## 1. One operation can serve two donors only across their common edge

### Theorem 1.1 (cross-edge paired response)

Let `G` be non-six-colourable, let `e=y_1y_2` be an edge, and fix a proper
six-colouring `c` of `G-e`.  Let `Y_1,Y_2` be disjoint nonempty connected
vertex sets with `y_i in Y_i`, and put

\[
                         T_i=N_G(Y_i).                 \tag{1.1}
\]

For each `i in {1,2}`, the equality partition `pi_i` induced by `c` on
`T_i` has all of the following properties.

1. It is a proper boundary partition and is realised by the exterior
   graph `G-Y_i`.
2. It does not extend through `G[Y_i union T_i]`.
3. The two partitions are restrictions of one literal colouring, and
   hence agree on `T_1 intersection T_2`.
4. The same conclusions hold after replacing `Y_i` by any subset
   `A_i subseteq Y_i` which contains `y_i`.

Conversely, suppose `A_1,A_2` are disjoint sets and one colouring of
`G-e` is to induce an exterior-realised but interior-rejected trace after
deleting either `A_i`.  Then the two sets contain different ends of `e`.
Thus `e` runs between them.

#### Proof

The ends of `e` have the same colour under `c`, since otherwise `c` would
already six-colour `G`.  Removing `Y_i` removes one end of the only edge
which can be monochromatic under `c`.  Hence `c` is proper on `G-Y_i`
and induces a legal partition on `T_i`.

If the same partition extended through `G[Y_i union T_i]`, permute its
used colour names to agree with `c` on the literal boundary and glue it to
`c` on `G-Y_i`.  This would give a proper six-colouring of `G`, a
contradiction.  The same proof applies to every `A_i` containing `y_i`,
and both partitions visibly come from `c`.

For the converse, suppose `A_i` contained neither end of `e`.  If both
ends belonged to `N_G(A_i)`, their common colour would make the induced
boundary partition improper.  Otherwise the restriction of `c` itself is
proper on the closed `A_i`-side and extends the alleged rejected trace.
Both possibilities contradict the premise.  Each `A_i` therefore contains
an end.  Disjointness assigns the two different ends to the two sets.
`\square`

This converse is the first quantifier correction.  Two unrelated donors
cannot merely be “measured” under the same deleted-edge colouring.  A
genuine simultaneous response forces the deleted edge itself to join the
donors.

## 2. Individual and joint fixed-list cores

For `v in Y_i`, define

\[
             L_i(v)=[6]\setminus c(N_G(v)\cap T_i).     \tag{2.1}
\]

### Proposition 2.1 (operation-preserving core hull)

The graph `G[Y_i]` is not `L_i`-colourable.  A vertex-minimal
non-`L_i`-colourable induced subgraph `K_i` is connected, contains `y_i`,
and the only list violation of `c|Y_i` is at `y_i`.

Suppose in addition that `Y_i` is a proper subset of a connected model bag
`U_i`, that the nonempty set `U_i-Y_i` is connected, and that a named
nonempty far bag is anticomplete to `Y_i`.  Let `W_i` be the component of
`G[U_i-K_i]` containing
`U_i-Y_i`, and put

\[
                         H_i=U_i-W_i.                  \tag{2.2}
\]

Then `H_i` is connected, contains `y_i`, has connected complement in
`U_i`, retains the same far bag, and carries the same fixed trace.  Thus
either `H_i=Y_i`, or `H_i` is a proper operation-preserving geometric
donor.  Contacts prescribed on the donor itself need not survive; contacts
prescribed on its complement do survive because that complement only
grows.

#### Proof

An `L_i`-colouring of `Y_i` would glue to `c` on `G-Y_i` and six-colour
`G`.  Hence `K_i` exists.  The standard vertex-minimality argument makes
it connected.  The restriction of `c` to `Y_i-y_i` respects all lists,
whereas `c(y_i)=c(y_{3-i})` is excluded by the boundary neighbour
`y_{3-i}`.  Thus `y_i in K_i` and this is the sole violation.

Every component of `G[U_i-K_i]` other than `W_i` attaches to the connected
set `K_i`.  Their union with `K_i` is therefore the connected set `H_i`,
while `W_i` is its connected complement.  Since `H_i subseteq Y_i`, the
named far bag remains anticomplete.  Theorem 1.1 applies because `H_i`
contains `y_i`, proving fixed-trace retention.  The contact assertions are
immediate from

\[
                         U_i-H_i\supseteq U_i-Y_i.
\]

`\square`

There is also one genuinely joint core.  Put

\[
 Y=Y_1\cup Y_2,qquad B=N_G(Y),qquad
 L_Y(v)=[6]\setminus c(N_G(v)\cap B).                 \tag{2.3}
\]

### Proposition 2.2 (both endpoints lie in the fixed-boundary joint core)

The connected graph `G[Y]` is not `L_Y`-colourable.  Every
vertex-minimal non-`L_Y`-colourable induced subgraph contains both
`y_1,y_2`.

#### Proof

The edge `e` connects the two donors, so `Y` is connected.  An
`L_Y`-colouring would glue to `c` outside `Y` and six-colour `G`.

Let `K` be a minimal obstruction.  If, say, `y_1 notin K`, then `e` is
not an edge of `G[K]`.  The restriction `c|K` is proper, and every
neighbour of `K` in the **fixed** boundary `B` has a different `c`-colour
from its neighbour in `K`; the sole monochromatic edge of `c` is internal
to `Y`.  Hence `c|K` is an `L_Y`-colouring, a contradiction.  The same
argument treats `y_2`. `\square`

The word “fixed” is essential.  If the lists are relocalised from `B` to
`N_G(K)`, an omitted endpoint of `e` may enter the new boundary and
recreate a one-ended violation.  Proposition 2.2 cannot be iterated after
that silent change of interface.

## 3. The exact joint invariant

Write

\[
 O=T_1\cap T_2,\qquad
 X_{12}=T_1\cap Y_2,\qquad
 X_{21}=T_2\cap Y_1.                                  \tag{3.1}
\]

The set `O` is external boundary overlap.  The other two sets are
cross-incidence inside the donors; they are different resources.  The
cross-edge gives

\[
                 y_2 in X_{12},\qquad y_1 in X_{21},   \tag{3.2}
\]

but it need not give any vertex of `O`.  Direct set algebra gives

\[
\begin{aligned}
 |T_1\cup T_2|
   &=|T_1|+|T_2|-|O|,\\
 N_G(Y_1\cup Y_2)
   &=(T_1\cup T_2)\setminus(X_{12}\cup X_{21}),\\
 |N_G(Y_1\cup Y_2)|
   &=|T_1|+|T_2|-|O|-|X_{12}|-|X_{21}|.               \tag{3.3}
\end{aligned}

Thus a term `+lambda|O|` with positive weight penalises rather than
rewards useful overlap.  Fix a comparison class of pairs which retains the
model, operation, colouring, connected-donor conditions, and every labelled
duty; call its members **admissible**.  The natural pair order in that fixed
class is

\[
 \Theta(Y_1,Y_2)=
       \bigl(|T_1\cup T_2|,\ |Y_1|+|Y_2|\bigr).        \tag{3.4}

### Theorem 3.1 (private inflation under joint minimisation)

Suppose an admissible pair for this single-edge operation minimises (3.4).
If a proper core hull `H_i subsetneq Y_i` from Proposition 2.1 gives an
admissible replacement, then, for `j ne i`,

\[
       \bigl(N_G(H_i)\setminus N_G(Y_i)\bigr)
                       \setminus T_j\ne\varnothing.    \tag{3.5}

Every vertex in (3.5) lies in `Y_i-H_i` and is anticomplete to `Y_j`.
Consequently joint minimisation has the exact fork

\[
 \boxed{
 \begin{array}{l}
 H_i=Y_i;\\
 \text{the replacement leaves the fixed comparison class;}\\
 \text{or a private same-bag boundary vertex appears.}
 \end{array}}                                           \tag{3.6}
\]

It does not force boundary inflation into overlap with the other donor.

#### Proof

Put `T_i'=N_G(H_i)`.  If every new boundary vertex belonged to `T_j`,
then

\[
                         T_i'\cup T_j
                          subseteq T_i\cup T_j.         \tag{3.7}

A strict inclusion improves the first coordinate of (3.4); equality
improves the second because `H_i` is proper in `Y_i`.  Both contradict
minimality.  This proves (3.5).

Since `H_i subseteq Y_i`, every neighbour of `H_i` outside `Y_i` already
belongs to `N_G(Y_i)`.  Hence

\[
                N_G(H_i)\setminus N_G(Y_i)
                              subseteq Y_i-H_i.         \tag{3.8}

A witness outside `T_j=N_G(Y_j)` is anticomplete to `Y_j`, proving the
last assertion and the fork. `\square`

The explicit
[paired-donor overlap barrier](../barriers/hc7_k7minus_paired_donor_overlap_barrier.md)
shows that this is not merely a proof defect.  Even order-seven traces,
overlap of order five, the forced cross-edge, and five retained contacts
per smaller donor can exhibit simultaneous private inflation and joint
trace rejection in a `K_7^-`-minor-free graph.  That graph is deliberately
not a critical host, so it fixes the trust boundary rather than refuting a
host-level supply theorem.

## 4. What a supplied compatible pair would give

### Theorem 4.1 (conditional paired absorption)

Let `G` be seven-connected and let

\[
                         X,U_1,\ldots,U_6             \tag{4.1}
\]

be pairwise disjoint connected sets partitioning `V(G)`.  Suppose
`Y_1 subsetneq U_r` and `Y_2 subsetneq U_s`, for distinct `r,s`, satisfy
the hypotheses of Theorem 1.1 and have nonempty connected complements in
their bags.
Put

\[
 X'=X\cup Y_1\cup Y_2,qquad W_i=U_i-Y_i\quad(i=r,s). \tag{4.2}
\]

Assume `X'` is connected and that the six sets obtained from
`U_1,...,U_6` by replacing `U_r,U_s` with `W_r,W_s` have at most one
nonadjacent pair.  Then at least one of the following holds.

1. The seven sets consisting of `X'` and those six residual bags form an
   explicit `K_7^-` minor model.
2. The set

   \[
                         N_G(Y_1\cup Y_2)              \tag{4.3}
   \]

   is an actual separator of order at least seven.  The one fixed
   colouring `c` induces a boundary partition which is realised by the
   exterior and rejected by the connected donor union.  At order seven,
   every complementary component is full to the separator.

#### Proof

The seven displayed sets are a connected partition.  If their contact
graph has at most one missing edge, they are the branch sets in outcome 1.
Otherwise, since the six residual bags have at most one mutual nonedge,
`X'` is anticomplete to some residual bag `R`.  In particular, `R` is
anticomplete to `Y_1 union Y_2`, so it is a nonempty far side of (4.3).
The donor union is connected through `e`, proving that (4.3) is an actual
separator.

Seven-connectivity gives its lower bound.  At equality, a separator
vertex missing a complementary component would leave a six-cut.  Finally,
`c` is proper outside the donor union.  If its partition extended through
the union, the two colourings would glue and six-colour `G`. `\square`

This is the useful positive content of the paired idea.  A genuinely
compatible pair gives a forbidden minor or one literal response-bearing
separator.  The theorem does not bound that separator from above, identify
it with the original five-centre boundary, or normalize `c` to the
original equal/distinct pole response.

## 5. Why the five-centre reduction does not supply the pair

Proposition 3.6 of the audited
[unique-owner reduction](hc7_k7minus_five_centre_owner_nonedge_connector.md)
does not satisfy the premise of Theorem 4.1.

1. It guarantees one donor in one contacted bag.  The duplicate-neighbour
   count which starts its proof does not produce a second such bag.
2. Its unavoidable-core case has two disjoint canonical sets, but both
   lie in the same model bag.  No edge between them, connected complement
   after deleting both, or common far bag is guaranteed.
3. An arbitrary edge between two model bags need not have both ends in
   donor-eligible pieces retaining the prescribed contacts.
4. The original equal/distinct `pq` responses come from shore-specific
   contraction colourings.  Proper-minor minimality supplies a colouring
   of `G-e` for every selected edge `e`, but does not force that colouring
   to induce the original boundary partition.

There is also an anchoring obstruction.  If the two donors lie in distinct
ordinary `C`-only owner bags, bijective ownership gives

\[
        N_G(Y_1\cup Y_2)\cap Z\subseteq\{z_r,z_s\}.     \tag{5.1}

Their joint boundary therefore misses at least three of the five selected
centres and cannot itself be `Z union {p,q}`.  A minimum-side descent from
this joint separator requires a donor involving a pole or expanded
opposite-shore bag, or a separate label-transfer theorem.

The exact order-seven backup reaches the same obstruction.  The donor
theorem gives fullness at order seven, and Corollary 2 of the separately
audited
[three-component seven-cut exclusion](../results/hc7_k7minus_three_component_seven_cut_exclusion.md)
gives exactly two complementary components.  Neither places the five
centres in the new boundary or retains the original response orientation.
A new equality-response side is terminal by minimum-side descent only after
proving, literally, that its boundary is
`Z union {r,s}` and that it is a proper subcomponent of the distinguished
minimum equality side.

## 6. Decisive route nonclosure

The paired attack has therefore separated into a valid response theorem
and an unavailable supply theorem:

\[
 \boxed{
 \begin{array}{c}
 \text{one common single-edge deletion}\Longrightarrow
     \text{one cross-edge joining the two donors};\\
 \text{a supplied compatible cross-edge pair}\Longrightarrow
     K_7^-\text{ or a joint response-bearing separator};\\
 \text{the current unique-owner theorem does not supply that pair};\\
 \text{joint minimisation permits private same-bag inflation.}
 \end{array}}                                             \tag{6.1}
\]

Equivalently, the current recorded witnesses do not establish the
quantifier exchange

\[
 \begin{aligned}
 &\exists\text{ one donor}
   +\exists\text{ interbag edges}
   +\forall e\,\exists c_e\\
 &\hspace{18mm}\text{do not furnish }
   \exists(Y_1,Y_2,e,c_e)
   \text{ retaining the duties and original response}.  \tag{6.2}
 \end{aligned}

The smallest positive repair would be a **cross-edge paired-donor supply
theorem**: either an explicit `K_7^-` model, or two donor-eligible pieces
containing the ends of one edge, with connected residual bags, the named
owner/helper contacts, a common far side or terminal absorption pattern,
and one boundary-normalized colouring of the edge deletion.

This does not assert that the supply theorem is false under the full host
hypotheses.  The hostile bounded screen shows only that weakening those
host-level duties to
overlap and five anonymous contacts is false.  Repeating this single-edge
paired boundary minimisation without first proving the supply theorem would
reproduce the same label-loss obstruction as the one-donor gate.  The
single-edge variant is therefore frozen at (6.2); a genuinely joint
two-edge operation has not been analysed here.  The five-centre
three-connected campaign is not opened in this note.

## Claim status and dependencies

- Theorems 1.1, 3.1, and 4.1 and Propositions 2.1--2.2 are proved here.
- The one-donor and unique-owner statements invoked in Sections 3 and 5
  have separate hash-pinned GREEN internal audits.
- The finite local counterexample in Section 3 has a deterministic
  verifier and an adjacent hash-pinned audit in `barriers/`.
- No closure of `kappa(G-Z)=2`, no Five-Centre Exclusion Theorem, and no
  proof of the `K_7^-` six-colour conjecture is claimed.
