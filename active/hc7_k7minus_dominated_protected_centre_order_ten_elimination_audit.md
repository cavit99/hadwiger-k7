# Internal audit: protected-centre order-ten kernel elimination

**Verdict:** **GREEN as an internal self-audit** for the exact finite
composition and its unbounded host lift.  The theorem eliminates only the
order-ten irreducible-kernel branch.  This is not a cold audit or external
peer review, and it does not promote the unaudited order-eight/order-nine
catalogues.

## 1. Audited revision and claim scope

The exact source, verifier and reproduction note checked are pinned by
SHA-256 at the end of this audit.  The verifier was run with Python
assertions enabled.

The claim statuses are:

* Lemma 2.1 is a computer-assisted finite composition result;
* Theorem 3.1 is an unbounded written host theorem;
* the exact order-ten terminal-kernel classification and the legality of
  all sixteen nonterminal-owner pairs are imported proved results with a
  separate independent `GREEN` audit; and
* the order-eight/order-nine counts in Section 4 are explicitly labelled
  discovery diagnostics and are not premises of Theorem 3.1.

## 2. Structural entrance

The seven vertices of `Q=N(u)-{v}` are distinct from every other centre:
the five centres are independent, whereas every member of `Q` is adjacent
to `u`.  Thus each chosen `w in Z-{u}` is a legitimate eighth terminal in
`H=G-{u,v}`.

Deleting two vertices from a seven-connected graph leaves a
five-connected graph, so the three-connectivity required by the
terminal-kernel theorem holds.  Terminal-legal contractions preserve all
eight terminal labels and yield a spanning rooted minor of order at most

```text
8 + floor(8/4) = 10.
```

No protected terminal is absorbed during that reduction.  The three
possible graphs `Q` are exactly the already obtained target-free connected
dominated-centre residue.

## 3. Exact order-ten quantifiers

The imported classification gives, for every actual order-ten kernel:

* a labelled terminal cycle of order eight;
* two nonadjacent nonterminals with complementary four-neighbour sets
  `A,B` in cyclic order `AABBAABB`; and
* every pair `(a,b) in A cross B` as a legal pair of owners.

The finite lemma respects the necessary quantifier order:

```text
for every labelled exact normal form,
  there exist a in A, b in B,
  and then an actual Q-neighbour r of the protected w-bag,
  such that the seven-bag quotient closes.
```

The choices may depend on the exact normal form and on the fixed labelled
graph `Q`.  No universal owner is asserted.  If `w` itself is selected as
one nonterminal owner, the subsequent absorption moves the entire enlarged
`w`-rooted bag; this is still a connected legal branch-set union and is
correctly represented by the quotient calculation.

## 4. Finite coverage and exact minor test

The verifier is self-contained and uses only the Python standard library.
It fixes one orientation for each of the

```text
8!/16 = 2520
```

undirected labelled cycles and generates the four ordered `AABBAABB`
shifts.  Deduplication gives exactly 10,080 templates.  Their sorted
eight-byte encoding has SHA-256

```text
78217d8621685a5839aa55172a51e3470297e6f989516c0455a4884471923418,
```

agreeing with the independently recorded normal-form generator.  An
assertion pins both the count and digest.

For every template the code ranges over all four choices of the first
owner and all four choices of the second owner.  It constructs the exact
two-owner quotient, lists the actual neighbours in `Q` of terminal `7`, and
tests every possible absorption until a certificate is found.  This is
performed for fixed canonical labellings of all three `Q` types.  Because
every terminal labelling of the normal form is generated, fixing the `Q`
labelling loses no case.

The recursive minor test is exact.  At more than five vertices it branches
over every vertex deletion and every edge contraction.  Any five-branch-set
minor either omits a current vertex or, when all current vertices are used,
has a branch set of order at least two containing an edge.  At order five,
nine edges are exactly a spanning `K_5^-` subgraph (and ten edges contain
one after an edge deletion).  Thus the recursion has neither false positive
nor false negative for the requested target.

The reproduced output is

```text
FCQ`_ templates=10080 failures=0
FCQb_ templates=10080 failures=0
FCp`_ templates=10080 failures=0
protected-centre order-ten composition templates=10080 q_types=3 failures=0
witness_digest bacd9ed98b08a1a0a60829250f852e54763e6fc812404e807f2cebf2cdc62202
```

The witness digest is a reproducibility fingerprint of the
lexicographically first owner triple for every `(Q,template)`; the theorem
depends on the asserted absence of failures, not on cryptographic trust in
that digest.

## 5. Branch-set lift

Inverse images of the terminal-legal contractions give ten disjoint
connected branch sets spanning `H`.  Absorb the two nonterminal sets into
the two distinct terminal owners supplied by the finite lemma.  All eight
terminal-rooted bags remain disjoint and connected.  Then absorb the
`w`-rooted bag into the selected adjacent `Q`-rooted bag.  The seven
remaining bags are connected, disjoint, and contain the seven distinct
members of `Q`.

Every quotient edge checked by the verifier is an actual adjacency between
these bags.  Every edge of the fixed graph `Q` is also an actual adjacency,
through its literal roots.  A `K_5^-` minor of the seven-vertex union
therefore lifts by taking unions of rooted bags.  Each of its five branch
sets meets `Q`.

The vertices `u,v` are adjacent, and each is adjacent to every member of
`Q`.  Their singleton bags are consequently adjacent to all five lifted
branch sets and to one another.  This produces the required `K_7^-` minor,
contradicting the host hypothesis.  The order-ten branch is therefore
excluded without using any order-eight/order-nine census.

## 6. Remaining trust boundary

The theorem leaves kernels of orders eight and nine.  The displayed
diagnostic counts `425` and `803` were reproduced by the current exact
bundle generator, but that generator's order-eight and order-nine
catalogues have not received the independent audit required for theorem
promotion.  The source correctly states their scale and count meaning and
does not use them as proved classifications.

Protecting the four exterior centres one at a time gives four valid but
potentially different rooted reductions.  The theorem neither co-bags
those centres nor aligns their four operation colourings with the resulting
kernel bags.  Those are the remaining compatibility issues.

The two- and three-protected-centre carrier screens mentioned in the source
use valid deletion budgets (`H-q` is four-connected and `H-{q,r}` is
three-connected), and their absorption enumeration is a sufficient quotient
test.  Their surviving coarse carriers establish only failure of that
particular composition rule.  They are not used in the positive theorem and
need no catalogue claim beyond the separately audited 5,936-carrier
trichotomy.

## 7. Hashes

```text
2027f5597de323eabd6ea30a8e58f9c5ee638b5abd6a34fe68b5a17e55313009  active/hc7_k7minus_dominated_protected_centre_order_ten_elimination.md
c673842f22fa40ac537a99b3a7482944bfe592e2d44c697f1ee485dcc0e8c32d  active/experiments/dominated_singleton_protected_centre_order_ten/verify.py
37e365abe0b874444db405d0cf0fb2de820f38b29b3d4c268f0ce7dac6736353  active/experiments/dominated_singleton_protected_centre_order_ten/README.md
```
