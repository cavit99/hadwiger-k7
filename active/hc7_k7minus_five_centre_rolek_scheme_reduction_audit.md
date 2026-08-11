# Internal audit: generalized-chain rooted-model reduction

Audited file:
`active/hc7_k7minus_five_centre_rolek_scheme_reduction.md`

Audited SHA-256:

```text
bf77dc74dadb8e010f3b444b838d53d120720e0cfad38c7401fac550ade588d9
```

**Verdict:** **GREEN** for Lemma 1.1, Theorem 2.1, Corollary 3.1,
Theorem 4.1, Corollary 4.2, and their stated scope.

This is a hash-pinned internal mathematical audit, not external peer
review.  The results are unbounded local rooted-minor and separator
reductions.  They do not close the all-rainbow five-centre row.

## 1. External inputs

The audit checked the two cited primary statements in the exact forms
used:

- Rolek--Song--Thomas, Lemma 1.7, permits an arbitrary set of missing
  edges among the five remaining neighbours and makes paths for
  nonincident demands vertex-disjoint; and
- Kuendgen--Pelsmajer--Ramamurthi, Theorem 6.2, states that
  `K_{1,1,3}` is contractible.

The all-rainbow profile and critical-host hypotheses come from the
separately audited global five-root palette alternative, source hash
`b26f9f0d12822f93af55e3aa566fc75b985dcb5a17daa4ea2b329c8efea274c3`
and audit hash
`765df0db1168001a212c77e5f871abe4725d4c92cc4e11ae8d887ff808f92e6a`.

## 2. Rooted-scheme conversion

For the six `X`--`Y` demands, present edges are used literally and missing
edges use the generalized paths.  A nontrivial path has no other root,
and two nonincident nontrivial demands are disjoint.  A nonincident
literal edge is also disjoint from every nontrivial path because the
latter has open interior outside `N[z]`.

If a family of selected paths has a common vertex, its demand edges have
a common endpoint.  A family not using the `Y`-edge is a pairwise incident
family in `K_{3,2}` and hence a star.  A family using the literal `Y`-edge
can meet at only one of its ends, which is then the common endpoint.  The
seven paths therefore form a genuine `K_{1,1,3}`-scheme.  Contractibility
gives the rooted model.  Two edges inside the three-set `X` leave at most
one of the ten `K_5` adjacencies missing; three leave none.

## 3. Five-vertex residue classification

For a pole-free centre, the contact graph `G[A]` has independence number
two and no `K_4`.  Its complement `L` is triangle-free with
`alpha(L)<=3`.  Under failure of the positive rooted `K_5^-` outcome,
deleting the ends of every edge of `L` leaves at least two edges.

The source correctly derives `delta(L)>=2`, hence `5<=e(L)<=6`.
The five-edge case is `C_5`; the six-edge Mantel equality case is
`K_{2,3}`.  Taking complements gives exactly `C_5` and
`K_3 dotunion K_2`, and direct deletion leaves exactly one edge in each
three-vertex `X`.  No finite-order assumption on a shore is used.

## 4. Model-separator and exterior checks

Let `W` be the union of the five rooted bags and `H=G-z`.  Since `H` is
six-connected, an inclusion-minimal separator contained in `W` between
two components of `H-W` has order at least six.  Minimality makes both
distinguished components full to the separator.  Each contains a member
of `I`, so restoring `z` changes its exact neighbourhood from `Q` to
`Q union {z}`.  This proves Theorem 4.1.

If a component of `H-W` instead contains all of `I`, maximality of `I`
makes that component adjacent to every one of the five rooted bags.
Together with `{z}`, it supplies the two universal completing bags and
forms a `K_7^-` model.

For a component `F` of `G-N[z]`, seven-connectivity gives at least seven
neighbours, all among the eight vertices of `N(z)`.  Thus `F` misses at
most one neighbour of `z`.  The case split in Corollary 4.2 chooses a
vertex `i in I` so that `F union {i}` is connected and sees every rooted
bag, including the possibly missed root.  The resulting seven bags again
form a `K_7^-` model.  Hence a nonterminal model must meet every such
exterior component.

## 5. Scope

The generalized-chain colouring need not be the fixed all-rainbow shore
colouring, and the paths are not shore-confined or pole-reserving.  The
separator in Theorem 4.1 may have order greater than six.  These are
explicit limitations, not conclusions of the audited claims.  No
unresolved assumption or proof gap remains inside the pinned results.
