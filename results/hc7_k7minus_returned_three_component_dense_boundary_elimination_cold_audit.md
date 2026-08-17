# Independent cold audit: returned three-component dense-boundary elimination

**Verdict:** GREEN.  This is a second internal mathematical audit, not
external peer review.

The audit checks the frozen revisions

```text
results/hc7_k7minus_returned_three_component_dense_boundary_elimination.md
SHA-256 c2920c9f4596a93350999471c004b345a9243d05bdf1b6f15c5f01b720426ab1

results/hc7_k7minus_returned_three_component_dense_boundary_elimination_verify.py
SHA-256 5d4cc91f168d5d0d8d89f2e4418478ffa713d7fd8d517a5567b27635ec194ac6
```

No source edit is required.  The theorem is an unbounded elimination of the
stated boundary classes; it still leaves type VII, boundaries with at most
six edges, and the returned two-component case.

The promoted source differs only in its status paragraph and one relative
link target.  It has SHA-256
`78676354ff551da0fe3cd85e53f84495a07f60f723c93ff4d480868d21d09001`;
the mathematical statement and proof are unchanged.

## 1. Strict rooted inequality

For `Z=S-{p,q}`, a separation of `(G[C union Z],Z)` of order at most three
lifts, after adding `p,q`, to a cut of `G` of order at most five.  The other
two full components ensure that the opposite side is nonempty.  Thus the
four-root pair is internally four-connected.

Both exclusions of a `Z`-rooted `K_4` model are label-faithful.  In the
cubic-nonedge case, `{q}` sees three of the four literal roots and may miss
only the fourth.  In the adjacent-cover case, the connected bag `{p,q}`
sees every root bag.  Fullness supplies all remaining contacts, with at most
the one missing contact between the two bare components.

The one-edge sharpening of Norin--Totschnig Lemma 9 was checked directly
against its proof.  Its small trisection branch has at most `3|V|-8` edges
and its recursive branch at most `3|V|-9`.  Equality in the weak bound
`3|V|-7` therefore forces the planar outcome of their Theorem 8.  If the
outer facial walk has length `lambda`, Euler's formula gives

```text
|E| <= 3|V|-3-lambda.
```

All four distinct roots are incident with that face, so `lambda>=4`.
Equality forces `lambda=4`, and the facial walk is the literal four-cycle
on the roots.  The hypothesis that `B[Z]` has no four-cycle excludes this
case.  Hence the strict inequality used throughout the proof is valid,
including when `|C|=1`.

## 2. Finite classifications and inequalities

The eight-edge and seven-edge classifications agree with an independent
unlabelled-graph census.  There are three admissible eight-edge classes,
three seven-edge classes with degree sequence `3,3,3,2,2,1`, and four with
degree sequence `3,3,2,2,2,2`.

The weighted inequalities were recomputed exactly.  They give component
excess at most two in all eight-edge classes, at most three in types I--III,
at most four in types IV--V, and at most five in type VI.  For type VI, the
sum

```text
R_04 + R_13 + R_15 + degree + upper(a_1) + lower(a_2)
```

has coefficient vector exactly `e_C+P-4c` and constant five.  The displayed
type-VI family attains five in the linear system, whilst the type-VII vector
has excess `c+2`; both are correctly presented only as numerical
certificates.

The global identity

```text
|E(G)|-4|V(G)|=|E(B)|+sum_C eta(C)-24
```

is exact.  Substitution gives the four strict deficits recorded in the
theorem.

## 3. Composition lemmas

In the two-model composition, bags from different components overlap only
at their common literal root.  Merging corresponding bags is therefore
connected and preserves disjointness between different roots.  Their
contact graph contains exactly the union of the two completed boundaries;
fourteen boundary contacts give a `K_6^-` model, and the third full component
is adjacent to all six root bags.

In the helper composition, completing four roots gives exactly

```text
4|D|+eta(D)-a_p(D)-a_q(D)+6 >= 4(|D|+4)-9.
```

Norin--Totschnig Lemma 12 consequently supplies a rooted
`K^*_{4,2}` model.  The added root--root edges cannot be internal to a bag
or realise any required root--helper or helper--helper contact, so the model
already exists in the uncompleted graph.  The five-root enlargement is
internally five-connected, and the separately audited fifth-root lemma puts
`p` in one helper.  After merging corresponding rooted bags with the model
in the first component, the final full component may miss only the other
helper.  These are seven disjoint connected bags forming a `K_7^-` model.

## 4. Mechanical check and scope

The frozen verifier was rerun with assertions enabled and returned

```text
GREEN returned three-component dense-boundary certificates
eight_edge_labelled=630
eight_edge_isomorphism_classes=3
seven_edge_three_cubic_labelled=1260
seven_edge_three_cubic_isomorphism_classes=3
seven_edge_remaining_isomorphism_classes=4
seven_edge_unhandled_isomorphism_classes=1
type_VI_bound=5
cross_lobe_compatible_pair_pairs=7-VI:11;7-VII:10
```

It exhausts all labelled six-vertex boundaries, all `720` relabellings and
all relevant omitted pairs, using exact rational arithmetic.  No component
order is bounded in either the statement or its reduction.  There are no
unresolved assumptions within the theorem's stated scope.
