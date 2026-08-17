# Audit of returned three-component dense-boundary elimination

**Verdict:** GREEN.

This audit checks the locked mathematical revisions

```text
results/hc7_k7minus_returned_three_component_dense_boundary_elimination.md
SHA-256 c2920c9f4596a93350999471c004b345a9243d05bdf1b6f15c5f01b720426ab1

results/hc7_k7minus_returned_three_component_dense_boundary_elimination_verify.py
SHA-256 5d4cc91f168d5d0d8d89f2e4418478ffa713d7fd8d517a5567b27635ec194ac6
```

The proof, finite classifications, exact rational certificates and two
composition lemmas are correct at these hashes.  No source edit was made.
The theorem remains a partial elimination: it leaves type VII, all
boundaries with at most six edges, and the returned two-component case.

After promotion, only the theorem's status paragraph and one relative link
target were updated.  The promoted source has SHA-256
`78676354ff551da0fe3cd85e53f84495a07f60f723c93ff4d480868d21d09001`;
its mathematical statement and proof are the audited revision above.

## 1. Rooted inequality and strict equality case

For a component `C` and four roots `Z=S-{p,q}`, any separation of
`(G[C union Z],Z)` of order at most three lifts, after adding `p,q`, to a
cut of `G` of order at most five.  The far side lies in `C`, while either
of the other two components remains on the opposite side.  Thus the pair
is internally four-connected.

Both target constructions excluding a `Z`-rooted `K_4` model are valid.

- If `q` is cubic and `pq` is a nonedge, the bags
  `D union {p}`, `E`, and `{q}` supplement the four rooted bags.  Fullness
  supplies all component contacts, and `q` sees three distinct literal
  roots, so at most one adjacency is missing.
- If `pq` is an edge and `{p,q}` covers the neighbourhoods of all four
  roots, the bags `{p,q}`, `D`, and `E` supplement the rooted model.  Only
  `D E` may be missing.

Norin--Totschnig Lemma 9 gives the weak bound `3|V|-7`.  The claimed
one-edge strictness was checked directly against its proof.  In the
trisection outcome, the small branch has at most `3|V|-8` edges in the
present order range, and the recursive branch has at most `3|V|-9`.
Equality can therefore occur only in the planar outcome of their Theorem
8.  If the outer facial walk has length `lambda`, face counting gives

```text
|E| <= 3|V|-3-lambda.
```

All four distinct roots are incident with that face, so `lambda>=4`.
Equality at `3|V|-7` forces `lambda=4`; the facial walk is then the cycle
through the four literal roots, and all four of its edges lie in `B[Z]`.
The hypothesis that `B[Z]` has no four-cycle excludes equality.  Hence

```text
e_C + P - a_p - a_q + |E(B[Z])| <= 3c+4
```

is valid.  The endpoint `c=1` causes no exception: the rooted graph has
five vertices, so the four-vertex base case in Lemma 9 is not involved.

The elementary inequalities are also exact.  Connectedness gives
`e_C>=c-1`, the degree sum in `C` gives `2e_C+P>=6c`, and fullness plus
simplicity gives `1<=a_s<=c` for every boundary vertex.

## 2. Boundary classifications

The eight-edge degree sum is sixteen.  Under maximum degree three, the
only candidate degree sequences are `3,3,3,3,2,2` and
`3,3,3,3,3,1`.  The latter leaves five edges on a four-set after deleting
the degree-one vertex and its cubic neighbour, violating the four-set
bound.  In the former sequence, if `D` is the cubic four-set and `L` the
remaining pair, degree summation gives

```text
|E(B[D])|-|E(B[L])|=4.
```

The four-set bound forces `B[L]` empty and `B[D]` a four-edge graph.  The
cycle/paw alternatives and their admissible attachments give exactly the
three displayed classes.

With seven edges, four cubic vertices would give
`|E(B[D])|-|E(B[L])|=5`, again impossible.  At least three cubic vertices
therefore means degree sequence `3,3,3,2,2,1`; the high/low internal-edge
identity gives exactly the three displayed types I--III.  Every remaining
class has degree sequence `3,3,2,2,2,2`, and there are exactly four,
namely IV--VII.

As an independent classification cross-check, NetworkX's unlabelled graph
atlas gives three admissible eight-edge graphs and seven admissible
seven-edge graphs, split by degree sequence as

```text
8 edges: 3 x (3,3,3,3,2,2)
7 edges: 3 x (3,3,3,2,2,1), 4 x (3,3,2,2,2,2).
```

This agrees with the labelled enumeration and canonicalisation in the
locked verifier.

## 3. Weighted certificates

Every displayed omitted pair has a cubic end, and each corresponding
four-root graph is four-cycle-free.  The verifier checks these hypotheses
before using any inequality.

For the eight-edge types, the weighted rooted inequalities give

```text
(3/2)e_C + P <= (9/2)c+2.
```

Adding half of `c-e_C<=1` yields `eta(C)<=5/2`, hence the integral bound
`eta(C)<=2`.

For seven-edge types I and II, the three omitted pairs partition `S` and
the total root deficit is five.  The same connectedness completion gives
`eta(C)<=3`.  In type III, and then IV and V, the two exceptional
attachment coefficients are completed with `a_s<=c`, after which half of
the degree inequality makes every final coefficient one.  The resulting
bounds are respectively three, four and four.

For type VI, summing the rooted inequalities for `04,13,15`, then adding

```text
-2e_C-P+6c <= 0,   a_1-c <= 0,   -a_2 <= -1
```

has coefficient vector exactly `e_C+P-4c` and constant five.  The family

```text
e_C=2c-5,  (a_0,...,a_5)=(c,c,1,3,3,3),  c>=4
```

satisfies all four available rooted inequalities and all elementary
constraints with equality value five, so the linear certificate is sharp.
The type VII vector likewise satisfies every available inequality and has
`eta=c+2`; it is correctly labelled only as a numerical recession
certificate, not as a graph construction.

The global identity

```text
|E(G)|-4|V(G)|=|E(B)|+sum_C eta(C)-24
```

was recomputed directly.  Substitution gives the four negative upper
bounds `-10,-8,-5,-2`, so every claimed boundary class is excluded at
the `4n` density.

## 4. Two-model composition

In Lemma 2, models in two distinct components overlap only at a common
literal root.  Merging bags with the same root is therefore connected and
does not create overlap between different bags.  The six resulting root
bags have every contact in `B^P union B^Q`; fourteen of the fifteen pairs
give a `K_6^-` model.  The third full component is adjacent to all six
through their literal roots and supplies the seventh bag.

The verifier considers all unordered pairs with repetition from the
fifteen omitted boundary pairs.  It recomputes both clique completions and
accepts precisely those whose union has at least fourteen edges.  The
reported lists are complete: eleven pair-pairs for VI and ten for VII.

## 5. Rooted-model/helper composition

For Lemma 3, completing `Z` to a clique gives exactly

```text
4|D|+eta(D)-a_p(D)-a_q(D)+6 >= 4(|D|+4)-9.
```

The separator lift makes the four-root pair internally four-connected, so
the contrapositive of Norin--Totschnig Lemma 12 supplies a rooted
`K^*_{4,2}` model.  Added root--root edges cannot be internal to a model
bag or realise a required root--helper/helper--helper edge, so the same
model exists before the clique completion.

The pair on `D union Z union {p}`, rooted at `Z union {p}`, is internally
five-connected: adjoining the sole omitted boundary vertex `q` to a
separation of order at most four would give a cut of `G` of order at most
five.  The audited fifth-root augmentation lemma therefore places `p` in
one helper bag.  After corresponding root bags are merged with the rooted
`K_4` model in the first component, the four root bags form a clique, both
helpers meet every root bag and each other, and the final component meets
the four root bags and the helper containing `p`.  Only its contact with
the other helper may be missing.  The seven bags are disjoint and
connected.

The fifth-root dependency was checked at its currently audited hashes:

```text
active/hc7_k7minus_e5_k5minus_cut_elimination.md
SHA-256 81306114489449f1bd2d8521c4aefc216411f81bf6721c7763412d4a7a87c6c0

active/hc7_k7minus_e5_k5minus_cut_elimination_audit.md
SHA-256 924d89d2a7c7645b9834a125d5851a342640a5c8aeb68f0c6acc667d435af1b2
```

## 6. Primary source and verifier

The following statements were checked against Norin--Totschnig,
[*Every graph with no `K_7^\vee`-minor is 6-colorable*](https://arxiv.org/html/2507.03244v1):

- Theorem 8 gives the rooted `K_4` model, trisection, separation and planar
  alternatives used in the strict equality analysis.
- Lemma 9 gives `|E(H)|<=3|V(H)|-7` for an internally four-connected
  four-root pair with no rooted `K_4` model; its proof has the strict branch
  bounds used above.
- Lemma 12 gives `|E(H)|<=4|V(H)|-10` when such a pair has no rooted
  `K^*_{4,2}` model.

Running

```text
python3 -B results/hc7_k7minus_returned_three_component_dense_boundary_elimination_verify.py
```

returned GREEN.  It enumerated 630 admissible labelled eight-edge
boundaries and 1,260 admissible labelled seven-edge boundaries with at
least three cubic vertices; these reduce to three isomorphism classes in
each case.  It found four further seven-edge classes, eliminated three and
left one.  Exact `Fraction` arithmetic verified every weighted coefficient,
the type-VI dual value five, the type-VII recession vector, the
adjacent-cover triggers and both compatibility lists.

The verifier's search space is complete: all `15 choose m` labelled edge
sets are considered, all fifteen four-subsets are checked, and canonical forms
are minimised over all `6!=720` relabellings.  No random choice, numerical
tolerance or bounded component order enters the theorem.

## Final assessment

The theorem is GREEN at the pinned hashes.  The strict Lemma 9 equality
case, both composition lemmas, the finite classifications, all displayed
dual certificates and the global quantifiers are complete.  The result is
unbounded in component order but remains below the campaign's terminal
benchmark because its explicitly stated residual cases are still open.
