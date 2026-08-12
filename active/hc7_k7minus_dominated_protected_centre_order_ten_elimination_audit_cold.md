# Cold internal audit: protected-centre order-ten kernel elimination

**Verdict:** **GREEN.**  The exact finite composition, its quantifier order
and the unbounded rooted branch-set lift are correct at the revisions pinned
below.  This audit covers only the order-ten kernel elimination.  It does
not certify the order-eight or order-nine discovery catalogues and is not
external peer review.

## Exact revisions

```text
2027f5597de323eabd6ea30a8e58f9c5ee638b5abd6a34fe68b5a17e55313009  active/hc7_k7minus_dominated_protected_centre_order_ten_elimination.md
c673842f22fa40ac537a99b3a7482944bfe592e2d44c697f1ee485dcc0e8c32d  active/experiments/dominated_singleton_protected_centre_order_ten/verify.py
37e365abe0b874444db405d0cf0fb2de820f38b29b3d4c268f0ce7dac6736353  active/experiments/dominated_singleton_protected_centre_order_ten/README.md
3c4efc5ca2480abee3892b88fac231136ef57077beca5ebadd5cf414ad0c2c0f  active/hc7_eight_terminal_exact_bundle.md
10d8af0bb4336e82162557e7a5f63c77fef6f1ac14c92f096341588f60551086  active/hc7_eight_terminal_exact_bundle_audit.md
```

The requested theorem hash `270bd29a...` had already been superseded by a
claim-neutral status/dependency edit when this cold audit began.  The
mathematical theorem and verifier were unchanged; this audit pins the
current theorem revision above.

## 1. Structural entrance and kernel bound

Every other exceptional centre `w` is distinct from `u,v` and from every
member of `Q`: the centres are independent, while `v` and all members of
`Q` are adjacent to `u`.  Hence `T=Q union {w}` is an eight-set in
`H=G-{u,v}`.

Seven-connectivity of `G` makes `H` five-connected and therefore
three-connected.  Terminal-legal contractions preserve all eight labels
and produce a spanning irreducible rooted kernel with at most

```text
8 + floor(8/4) = 10
```

vertices.  This is exactly the range used in the theorem.

## 2. Imported order-ten normal form

The independently audited analytic classification gives every actual
order-ten kernel as:

* a terminal eight-cycle;
* two nonadjacent nonterminals with complementary four-neighbour sets
  `A,B`; and
* cyclic word `AABBAABB`.

Every pair in `A cross B` is a legal owner pair.  Absorbing the two
nonterminal bags at such a pair retains eight disjoint connected
terminal-rooted bags.  If either owner is `w`, the later absorption simply
moves the enlarged `w`-bag; no overlap is introduced.

The downstream quantifier is therefore

```text
for every labelled exact template and every fixed labelled Q type,
  there exist a in A, b in B, and an actual Q-neighbour r of the w-bag
  for which the final quotient closes.
```

The verifier implements this order.  It does not choose one owner triple
uniformly over all templates.

## 3. Finite coverage

The code fixes one orientation of each of the `8!/16=2520` undirected
labelled cycles and takes the four distinct shifts of `AABBAABB`.  The
10,080 resulting encodings are deduplicated and their digest is asserted as

```text
78217d8621685a5839aa55172a51e3470297e6f989516c0455a4884471923418.
```

For each of the three fixed labelled graphs `Q`, every template is tested
against all sixteen legal owner pairs and every actual `Q`-neighbour of the
resulting `w`-bag.  Fixing the labelled `Q` loses no case because the
template enumeration ranges over every terminal labelling.  Rerunning the
verifier with assertions enabled reproduced

```text
FCQ`_ templates=10080 failures=0
FCQb_ templates=10080 failures=0
FCp`_ templates=10080 failures=0
protected-centre order-ten composition templates=10080 q_types=3 failures=0
witness_digest bacd9ed98b08a1a0a60829250f852e54763e6fc812404e807f2cebf2cdc62202
```

The recursive minor predicate is exact.  At order above five, a
five-branch-set model either omits a vertex or has a non-singleton connected
bag containing an edge, corresponding to deletion or contraction.  At
order five, nine edges are exactly the required `K_5^-` subgraph threshold.
As an implementation-independent check, I reconstructed the minor search
by enumerating connected five-bag partitions and confirmed the selected
witness quotient for ten spread-out templates of each of the three `Q`
types.

## 4. Host lift

Inverse images of the terminal-legal contractions form ten disjoint
connected branch sets partitioning `V(H)`.  The two legal owner
absorptions reduce them to eight terminal-rooted bags.  The finite witness
then supplies an actual adjacency from the `w`-bag to a bag rooted at
`r in Q`, so their union is connected and leaves seven disjoint bags, each
containing one distinct vertex of `Q`.

Every checked quotient edge is an actual inter-bag adjacency.  Each edge of
the fixed graph `G[Q]` is also actual through its literal roots.  Thus a
`K_5^-` minor of the seven-vertex quotient union lifts by taking unions of
rooted bags, and all five lifted branch sets meet `Q`.  The singleton bags
`{u},{v}` are adjacent to each other and to all five sets, producing the
forbidden `K_7^-` minor.  No terminal is duplicated or discarded.

## 5. Scope

The theorem validly excludes `|V(K)|=10` for each separately protected
exterior centre, leaving orders eight and nine.  It does not align the four
separately chosen kernels, place the four centres in distinct bags, or use
their degree-eight response colourings.  The order-eight/order-nine counts
and coarse multi-protected diagnostics are explicitly nondependencies and
remain outside this verdict.
