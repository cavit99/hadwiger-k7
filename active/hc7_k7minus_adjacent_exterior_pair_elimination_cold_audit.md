# Independent cold audit: adjacent exterior-pair elimination

**Verdict:** **GREEN** at the frozen theorem and verifier revisions

```text
8f83354b67632d21e558f7ab86ee16958cfe25f6a478b8f81a83555fbe7cce31
  active/hc7_k7minus_adjacent_exterior_pair_elimination.md
2fa83c339c36504d8fae1fed1aab99fdcfa6397bae36b1c5e1e99246ba2bf55c
  active/experiments/sixconnected_codegree2_two_vertex_verify.py
```

This is an independent internal mathematical and computational audit, not
external peer review.  The frozen sources were not edited during the audit.

The current theorem SHA-256 is
`1650513ef9aee4136bb9feeab0da3d5f2fe49e1b0799b4da7edaf3fa34fea196`.
The only later change records this GREEN audit in its status paragraph; no
statement, proof, computation, dependency, or scope claim changed.

## 1. Complete local and attachment universes

NetworkX `3.6.1` supplies all `1,044` unlabelled order-seven atlas graphs.
Deleting any chosen vertex of an eight-vertex graph and transporting its
neighbourhood shows that adjoining a new vertex with each of the `2^7`
possible neighbourhoods is complete.  The degree sequence and
Weisfeiler--Lehman hash used for bucketing are isomorphism invariants, and
graphs within a bucket are compared by exact isomorphism.  Thus the
`2,590` minimum-degree-at-least-three representatives are complete and
duplicate-free.  The imported exact minor oracle leaves precisely `1,562`
representatives with no `K_6^-` minor.

For either exterior vertex, six-connectivity forces at least five
neighbours in `J`, so its missed set has order at most three.  A cubic
vertex of `J` must be seen by both exterior vertices, and a degree-four
vertex may be missed by at most one.  The verifier enumerates exactly
these conditions.  Conversely, it applies the exact connectivity test to
every such pair, so no sufficiency is assumed.  Restricting the second
missed set to the suffix beginning at the first is complete because
interchanging the adjacent vertices `x,y` is an automorphism of the
construction outside their labelled attachments.

If `m` vertices of `J` have degree at least four, the number of individual
missed-set profiles is

```text
sum_{i=0}^3 binom(m,i),
```

giving the nine displayed values

```text
1, 2, 4, 8, 15, 26, 42, 64, 93.
```

Their asserted class distribution sums to `1,562`.  The resulting exact
pair loop contains `668,408` degree-feasible unordered attachment pairs.

## 2. Exact six-connectivity test

If the centre `v` survives a cut of order at most five, every surviving
vertex of `J` lies in one component through `v`.  Minimum degree six means
that one surviving member of `{x,y}` cannot be isolated: deleting the
other member and all at least five of its boundary neighbours would need
six deletions.  If both survive outside the centre component, all of
`N_J(x) union N_J(y)` must have been deleted.  This union has order at
most five exactly when the two boundary neighbourhoods are the same
five-set, which is the special rejection in the verifier.

If `v` is deleted, only four further vertices may be deleted.  The program
tests every subset of orders zero through four in the ten-vertex graph
`Q-v`, using a literal bitset reachability computation.  These two cases
exhaust all cuts of order at most five.  As an adversarial implementation
check, `500` fixed-seed random quotients were compared with a direct test
of every order-at-most-five deletion in the full eleven-vertex graph; all
`500` classifications agreed, including `42` six-connected examples.

## 3. Exact minor search and cache reuse

The imported oracle has frozen SHA-256

```text
d721c181a8388feb7901e8ab04f704c19679cfb56551752756a45733f28d6fdc
  results/hc7_k7minus_sixconnected_degree_eight_low_codegree_verify.py
```

and already has two adjacent GREEN audits.  Its recursion from singleton
bags is exact: deletion removes unused vertices, while touching mergers
along a spanning tree construct every connected branch set.  At seven
bags, at most one missing interbag pair is exactly a `K_7^-` model, with a
`K_7` correctly accepted.

Cached models are safe across quotients.  Every cache entry originated as
a tuple of seven disjoint nonempty branch sets, properties independent of
the host edges.  Before reuse, the verifier retests connectedness and all
twenty-one pairwise contacts in the current labelled quotient.  It then
calls the imported `verify_model`, which again asserts nonemptiness,
disjointness, connectedness and at most one missed contact.  The documented
run used Python `3.12.13` with assertions enabled; running with `-O` is not
part of the frozen verification protocol.

## 4. Reproduced census

A clean run under the pinned lockfile SHA-256
`ff6a929a94dd162d2e3b08e25bf3b7aa7845b70b2511a15772f84776a122092c`
and NetworkX `3.6.1` reproduced

```text
GREEN six-connected codegree-two adjacent-pair quotient
local_isomorphism_classes=2590
K6minus_free_local_classes=1562
profile_distribution={1: 6, 2: 9, 4: 58, 8: 127, 15: 291,
                      26: 421, 42: 403, 64: 192, 93: 55}
degree_feasible_attachment_pairs=668408
six_connected_quotients=611678
exact_minor_searches=407
cached_model_templates=407
certificate_digest=c54b07a9dfa35f6d5d4c41b89f982379d074f0aea0231503d30c17fd9e002858
```

The class counts, profile distribution, attachment counts and digest are
explicit runtime invariants.  The `407` search/template count is a
deterministic statistic of this frozen run rather than a theorem-critical
assertion; every one of the `611,678` accepted quotients nevertheless has
a model revalidated in its own adjacency relation.

## 5. Unbounded corollary and scope

For Corollary 2, contracting the two connected exterior parts produces
exactly the finite quotient: their cross-edge gives `xy`, neither part
meets `v`, and `v` remains complete to `J`.  A `K_6^-` model in `J`,
together with singleton `{v}`, would already be a forbidden `K_7^-`
model, so the local exclusion hypothesis is automatic.  A target model in
the quotient lifts through both contractions.

No profile-completeness, connectivity, cache-reuse, minor-search,
certificate, or lifting defect was found.  The theorem does not assert
that an arbitrary connected full exterior admits the required
six-connectivity-preserving two-block contraction, and the source states
that remaining structural gate accurately.
