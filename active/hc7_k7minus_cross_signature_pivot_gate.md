# The cross-signature pivot gate at a co-bagged matching split

**Status:** active written lemmas and a recorded route nonclosure;
[separate internal audit GREEN](hc7_k7minus_cross_signature_pivot_gate_audit.md).
This note does not prove the matching row, the six-coordinate
terminalisation theorem, the `K_7^-` six-colour conjecture, or `HC_7`.

## 1. Setting

Use the opposite-coordinate setting of the audited
[matching common-state theorem](../results/hc7_k7minus_matching_square_common_state.md).
Thus

\[
                 e=ab,\qquad f=cd,\qquad H=G-\{e,f\},
\]

the six-colour signatures of `H` are exactly

\[
                         EP,\qquad PE,\qquad EE,       \tag{1.1}
\]

and `PP` is absent.  Here the first coordinate refers to `e`.  Fix the one
spanning `K_6`-minor model lifted from `G/e/f`.  It co-bags both endpoint
pairs.  For either selected pair, split its branch set across the restored
edge by deleting that edge from a spanning tree, as in the audited
[selected-edge response theorem](../results/hc7_k7minus_selected_edge_root_bag_response.md).

The all-lock case means that, after the bounded response outcomes have been
excluded, every `EP` colouring locks the equal ends of `e` in all five
alternate palettes, and every `PE` colouring does the same for `f`.

## 2. The ordinary deficiency profile is static

Fix the split

\[
                         R=R_a\mathbin{\dot\cup}R_b
\]

of the branch set containing `e`, and write the five foreign branch sets as
`B_1,...,B_5`.  Define

\[
 \delta_e(i)=
 \bigl({\bf1}_{E(B_i,R_a)=\varnothing},
       {\bf1}_{E(B_i,R_b)=\varnothing}\bigr).          \tag{2.1}
\]

### Lemma 2.1 (signature-invariance of split deficiency)

The five vectors in (2.1), and hence the set of foreign bags which meet
both split sides, are independent of the chosen colouring of `H`.
Consequently comparing their values in an `EP`, `PE`, and `EE` colouring
gives three copies of the same data and no pigeonhole gain.

#### Proof

Every term in (2.1) is an adjacency statement between fixed vertex sets in
the fixed graph `G`.  Neither the branch-set partition nor the split changes
when a different proper colouring of `H` is selected. `\square`

One may instead attach a profile to a bichromatic component, recording the
branch sets which it meets.  That profile is colouring-dependent, but then
the components selected in the three signatures are different existential
objects.  Nothing in (1.1) identifies them or puts the corresponding
colourings in one Kempe component.  This is the first quantifier issue in a
cross-signature deficiency argument.

## 3. What a genuine common `EE` pivot would force

There is nevertheless a useful conclusion if the missing common pivot is
supplied.  A **shared `EE` pivot** is a proper colouring `kappa` of `H` with
signature `EE`, together with two bichromatic components `C_e,C_f` such
that

* switching `C_e` changes the signature to `PE`; and
* switching `C_f` changes the signature to `EP`.

Thus the first switch separates precisely the ends of `e`, while the second
separates precisely the ends of `f`.

### Theorem 3.1 (forced interaction at a shared pivot)

Let the palettes of `C_e,C_f` be `P_e,P_f`, respectively.  Then

1. `P_e` and `P_f` are neither disjoint nor equal;
2. they therefore share exactly one colour, say

   \[
                         P_e=\{s,x\},\qquad P_f=\{s,y\},
                         \qquad x\ne y;                \tag{3.1}
   \]

3. either `C_e cap C_f` contains a vertex of colour `s`, or there is an
   edge between an `x`-coloured vertex of `C_e` and a `y`-coloured vertex
   of `C_f`.

#### Proof

If the palettes were disjoint, the two whole-component interchanges would
commute.  Each would leave the other selected pair equal, so their combined
effect would be a proper `PP` colouring, contrary to (1.1).

Suppose the palettes were equal.  Then `C_e,C_f` are components of the same
bichromatic induced subgraph.  They cannot be the same component, because
switching that component would then have both of the two different stated
signatures.  If they are distinct, switching both whole components is
proper and separates both selected pairs, again producing `PP`.  The
palettes are therefore distinct and intersect in exactly one colour, which
gives (3.1).

Assume now that the two components are disjoint.  Interchange `s,x` on
`C_e` and `s,y` on `C_f` simultaneously.  Each selected pair becomes
proper: a component whose individual switch leaves that pair equal cannot
contain exactly one of its ends, and disjointness prevents it from
containing both ends of the pair separated by the other component.

The individual switches already preserve every edge except that a new
conflict might be created between the two switched sets.  For an edge
between them, the only possible original colour pairs are

\[
                         (s,y),\qquad(x,s),\qquad(x,y).
\]

The first two remain proper after both switches.  The last becomes
`s-s`.  Hence, if no displayed `x-y` edge existed, the simultaneous
assignment would be a proper `PP` colouring, again impossible.  This proves
item 3.  If the components are not disjoint, every vertex in their
intersection has their sole common palette colour `s`. `\square`

Theorem 3.1 spends the missing fourth signature literally.  Its conclusion
is an overlap or an edge in the graph, not merely an equality between
palette names.

## 4. Why this still does not allocate the fixed model

The hypotheses currently proved do not supply a shared `EE` pivot.  They
give

\[
 \operatorname{Col}_{EP}(H)\ne\varnothing,\qquad
 \operatorname{Col}_{PE}(H)\ne\varnothing,\qquad
 \operatorname{Col}_{EE}(H)\ne\varnothing,             \tag{4.1}
\]

and universal locking inside each singleton-response family.  They do not
give

\[
 \exists\kappa\in\operatorname{Col}_{EE}(H)
 \quad\text{adjacent by Kempe interchanges to both singleton families}.
                                                               \tag{4.2}
\]

Even putting an `EP` and a `PE` colouring in one Kempe component would not
imply (4.2).  Since the all-lock hypothesis excludes a direct `EP`--`PE`
move, a shortest route passes through the `EE` family, but it may enter at
one `EE` colouring, make several moves within that family, and leave from
another.  The switches at the two ends then have no common base colouring
and cannot be composed.

There is a second, independent gap after (4.2).  The overlap or edge in
Theorem 3.1 belongs to the spanning branch-set partition, but it may lie
inside one foreign bag, inside a root bag, or between two foreign bags
which were already adjacent.  None of these placements makes a one-sided
foreign bag meet the missing side of the selected split.  Thus a shared
pivot gives one literal interaction, but does not by itself repair any of
the static deficiency vectors (2.1).

The exact failed inference is therefore

\[
 \begin{gathered}
 EP,PE,EE\text{ realised},\quad PP\text{ absent},\\
 \text{all singleton palettes locked},\quad
 \text{one fixed co-bagged model}
 \end{gathered}
 \quad\Longrightarrow\quad
 \begin{gathered}
 \text{a Kempe interaction meeting a deficient model label,}\
 \text{or a common shore partition.}
 \end{gathered}                                      \tag{4.3}
\]

The left side supplies neither the common-pivot quantifier nor the
label-incidence conclusion on the right.  This is a route nonclosure, not a
counterexample to a terminal cross-signature theorem.

## 5. Smallest valid repair

The next positive statement must couple the colouring transition to the
fixed branch-set partition.  A minimal sufficient form is the following.

> **Deficiency-aware shared-pivot theorem (open).**  At a target-free
> blocked split in the seven-connected matching common host, either there
> is an original-coordinate response boundary of order seven or eight, or
> one boundary partition extends through both original shores, or there is
> a shared `EE` pivot for which the interaction in Theorem 3.1 supports a
> branch-set reassignment that strictly increases the number of foreign
> bags meeting both split sides while retaining both co-bagged coordinate
> pairs.

Iteration of the last outcome terminates after at most four increases; the
four-foreign-contact criterion then gives an explicit `K_7^-` minor.  This
form uses only whole Kempe components, so it avoids the invalid partial-lock
switch identified by the audited
[all-lock transfer gate](hc7_k7minus_all_lock_branch_transfer_gate.md).

A theorem proving only Kempe equivalence of the two singleton families is
too weak: it does not give one common pivot or a model-label incidence.  A
theorem proving only Theorem 3.1's overlap is also too weak: the overlap may
be absorbed by an already adjacent branch bag.  The required new content is
precisely a **Kempe-valid, model-monotone exchange**, with the two bounded
response outcomes retained when that exchange is blocked.

## Dependencies and scope

The note uses the audited matching common state, selected-edge response,
matching-lock boundary reduction, and all-lock transfer gate.  Lemmas 2.1
and Theorem 3.1 are unbounded and computation-free.  No comparison of
colourings from unrelated Kempe classes is made.
