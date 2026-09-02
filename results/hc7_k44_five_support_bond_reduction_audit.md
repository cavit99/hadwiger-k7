# Independent internal audit: five-support bond reductions

**Verdict: GREEN.**  At the exact revision below, the six-boundary
inequality, the six-connected rooted augmentation, the minimum-side block
reduction, the parity-bond deductions, and the facial-cycle Euler deduction
are correct under their stated hypotheses.  In particular, the strengthened
choice of a minimum support-full side opposite a specified
`p in R_a` is valid, and if that side meets `R_b`, it is necessarily a
triangle-free path with exactly two movable vertices and exactly two split
supports.

This is a separate internal mathematical audit, not external peer review.

**Audited source:**
[`hc7_k44_five_support_bond_reduction.md`](hc7_k44_five_support_bond_reduction.md)

**Source SHA-256:**
`687034d01f4b1a9784585aa9596def4439939f17efc6ecd0d0530c2c95aa7773`

After the initial mathematical audit, the source status line was changed from
“audit pending” to “audit GREEN,” and Theorem 3.1 was clarified to say
explicitly that its rooted-model equivalence is asserted under its preceding
equivalent connectivity conditions.  Corollaries 5.4--5.5 were then added and
separately checked below.  The displayed hash covers all of those changes.

## Checks performed

### Six-boundary reduction and augmentation

Lemma 2.1 uses both hypotheses exactly.  A value `q(W)<=4` contradicts the
ordinary seven-boundary inequality, while `q(W)=5` forces both distinguished
supports and then contradicts the strict inequality.

Theorem 3.1 is correct in both directions.  In the forward direction,
deleting the five new clique vertices leaves `X`, minimum degree gives two
neighbours in each support, and the displayed neighbourhood is a separator
whenever it has order at most five.  Conversely, every deletion of at most
five vertices either deletes the whole new clique or leaves its surviving
vertices in one component; any other component would be a proper connected
set `W` with `q(W)<=5`.  The rooted-minor equivalence has the exact contact
count `16+s(U,V)`.  Extending the two non-root branch sets along a shortest
path and then assigning each unused component to a side it meets preserves
connectivity and all existing root contacts.

### Strengthened minimum-side block reduction

The admissible family used in Section 4 is nonempty.  Three-connectivity
makes `X-p` connected, and `|R_i|>=2` ensures that `X-p` still meets every
one of the five supports.  Thus `(X-p,{p})` is an admissible bond and a
minimum first side exists.

Every single-vertex move used in the proof preserves the additional
constraint `p in V`: for `x in M`, the smaller candidate is
`(U-x,V union {x})`, whose second side still contains `p`.  Minimality
therefore supplies a support whose unique vertex in `U` is `x`.  Support
multiplicity places another vertex of that support in `V`, and distinct
members of `M` yield distinct split supports.  Hence `|M|<=s(U,V)`.

The closing thresholds are applied with the correct orientation.  Since
`p in V cap R_a`, the bond may be oriented with `V` first.  Four split
supports always close it.  If the original side `U` also meets `R_b`, three
split supports close it, so the no-closing hypothesis gives `s(U,V)<=2` in
that case.

The no-cutvertex case is complete.  There `M=B`.  If `U-B` is nonempty,
three-connectivity and `|B|=|M|<=s<=3` force `|B|=s=3`; a component of
`X[U-B]` then has at most three graph-boundary vertices and meets at most the
two supports not assigned to `M`, contradicting `q>=6`.  Thus `U=B` and
`|U|<=3`.  The order-two incidence count produces a singleton bond splitting
at least four supports.  At order three, `X[U]` is a triangle; the two
non-split supports intersect, and moving an intersection vertex produces a
bond splitting four supports.  Both outcomes are closing because the side
containing `p` meets `R_a`.

In the cutvertex case, every leaf block has a lobe vertex adjacent to `V`,
or its attachment cutvertex would separate that lobe in `X`.  Such a vertex
belongs to `M`, so there are at most three leaf blocks.  For each block `Q`,
the proof correctly counts one distinct member of `M` in every incident
component of the block-cut tree, giving

\[
 |C_Q|+|M\cap(V(Q)-C_Q)|\le |M|.
\]

If a non-cutvertex of `Q` were outside `M`, a connected component `W` of all
such vertices would have graph neighbourhood contained in the cutvertices
of `Q` together with the members of `M` in `Q`.  The `|M|` supports assigned
to movable vertices avoid `W`; consequently `q(W)<=5`, a contradiction.
Thus every non-cutvertex of `X[U]` belongs to `M`.

There are therefore at most three non-cutvertices in the whole block graph.
The standard block-cut tree enumeration is exhaustive:

1. two singleton leaf lobes give a path, with at most one internal edge
   replaced by a triangle;
2. leaf-lobe sizes two and one give a triangle with a pendant path; and
3. three singleton leaf lobes give a subdivided claw, possibly with its
   central vertex replaced by a triangle.

All three graphs have maximum degree three, so `delta(X)>=4` gives the stated
attachments to `V`.  Finally, if `U` meets `R_b`, the orientation argument
gives `s<=2`, while the two leaf blocks give `2<=|M|<=s`.  Hence
`|M|=s=2`; the enumeration then permits only the triangle-free path.

No property of `p` beyond `p in R_a` is used in this theorem.  Stronger
minimum-blocker facts about the admissible choice of `p` remain available for
the unresolved completion step but are not hidden hypotheses here.

### Parity and planar deductions

Theorem 5.1 and Corollary 5.2 use Theorems 1.2 and 1.1 of
Chen--Ding--Yu--Zang, *Bonds with Parity Constraints*, with the required
hypotheses.  The three two-element sets are nontrivial and have nonempty
symmetric difference, hence are acyclic.  A feasible bond alternates the
four displayed vertices and gives exactly the claimed split supports.  In a
four-connected nonplanar graph the cited facial-cycle obstruction is
impossible.

Corollary 5.4 is a valid mixed-support specialization of the same theorem.
Its three two-element sets make the quadruple nontrivial, and (18) is exactly
the acyclicity condition.  A feasible bond separates the ends of all three
pairs, hence splits three distinct indexed supports.  The first pair has one
end in `R_a` and the other in `R_b`, so its separation supplies the required
orientation for a closing bond.  Four-connectivity and nonplanarity exclude
the remaining facial obstruction by Theorem 1.1 of the cited paper.

The pair-selection argument in Corollary 5.5 is complete.  From any three of
the four support indices other than `i`, choose two-element sets
`B_1,B_2,B_3`.  If
`A_i triangle B_r triangle B_s` were empty for all three pairs, the first two
equalities would give `B_2=B_3`, while the third would give
`B_2 triangle B_3=A_i`, contradicting the fact that `A_i` has two elements.
Thus Corollary 5.4 applies to some two distinct other support indices.  The
argument does not require the chosen two-element sets to be disjoint or
distinct as vertex sets.

Lemma 5.3 is also correct.  With the specified facial cycle as outer face,
face counting gives `e<=3n-h-3` and therefore

\[
 \sum_{v\notin C}(6-d(v))+\sum_{v\in C}(4-d(v))\ge6.
\]

Minimum degree four makes every cycle summand nonpositive, so some vertex
off the cycle has degree at most five.  If all five supports lay on the
cycle, its singleton would contradict `q>=6`.

## Exact scope and unresolved point

This audit proves no existence theorem for a closing bond.  The unresolved
unbounded statement is exactly the leaf-block completion lemma in Section 6:
the three block forms must still be eliminated using the complementary side,
the full support incidences, and the exact three-cut profiles of the audited
minimum-blocker theorem.  The parity theorem supplies a possible route, not
an automatic exclusion of its weakly-linkable outcome.

Corollary 5.5 excludes a support containing distinct representatives of both
distinguished supports only in the four-connected nonplanar case.  It does
not make that exclusion for a merely three-connected graph or for the planar
facial-obstruction case.

Accordingly, the audited result does not prove the weighted splitter theorem,
the literal `K_{4,4}` case of T44, T44, Conjecture 21, or `HC_7`.  The finite
experiments and the adjacent rooted-extension counterexample retain their
separately stated computational and counterexample scopes; no unbounded
claim is inferred from them here.
