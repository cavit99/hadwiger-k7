# Adversarial cold audit: three-connected minor-free exact singleton

**Verdict:** **GREEN** for the exact revisions below.  This audit was made
independently of the author and the other adjacent audit.  It specifically
pressure-tests the five exceptional-core decoders, the carrier hypothesis,
the terminal composition, and the derived exact-six lift.  It is not
external peer review.

## Pinned artefacts

```text
98bf46538abc095e7722db332eaf6d31fcbddca485ab669c98a700c231044760
  active/hc7_k7minus_sparse_sixcut_threeconnected_minorfree_exact_singleton.md
56b40afd3ab310fa3b7a71bc4a6bc5afeae2505b94c69d14b870df11e6f389a3
  active/experiments/sparse_sixcut_wood_woodall_rooting/verify.c
f6598778e66d5006264a1113e8d162d368793abf768e80e493a8477743163841
  active/experiments/sparse_sixcut_wood_woodall_rooting/README.md
```

The verifier was rebuilt with `-std=c11 -O2 -Wall -Wextra -Werror
-pedantic` and rerun.  A separate AddressSanitizer/UndefinedBehaviourSanitizer
build, with leak detection disabled because it is unavailable under the
runner's tracing layer, produced the same output and no diagnostic:

```text
W3 tested=234256 decoder_failures=15 carrier_admissible_failures=0
W4 tested=9838752 decoder_failures=75 carrier_admissible_failures=0
long-wheel tested=5153632 decoder_failures=15 carrier_admissible_failures=0
prism tested=5153632 decoder_failures=15 carrier_admissible_failures=0
K33 tested=5153632 decoder_failures=15 carrier_admissible_failures=0
```

## 1. Finite trust boundary

The mask arrays are exactly the `42` subsets of a six-set of order at least
three and the `22` subsets of order at least four.  The nested loops enumerate
ordered tuples, not a symmetry sample, so their sizes are precisely `22^4`,
`42*22^4`, and `22^5`.

For every tuple, `carrier_violation` checks all fifteen four-sets and returns
true exactly when one is contained in at least three masks.  Three vertices
with those masks are three disjoint singleton carriers, so this is exactly
the imported carrier obstruction, with no converse being assumed.

The five-bag routine tries every injection of five roots into the six-set,
requires the root assigned to bag `i` to lie in its mask, and counts `ij`
only when the assigned root of one bag is adjacent to the core vertex of the
other.  The `W_3` routine independently selects the fifth singleton root,
requires it to occur in three masks, and then finds four distinct assigned
roots avoiding it.  Thus the program checks literal branch-bag contacts,
not merely mask unions.  Every raw failure violates the carrier guard, and
the asserted mask lemma follows within this finite boundary.

## 2. Exceptional-core decoders

For `W_3=K_4`, the four two-vertex rooted bags inherit all six clique
contacts.  The fifth singleton root meets at least three of them, so at most
one of ten pairs is absent.

For `W_4`, the hub and rim supply eight contacts.  The only absent core pairs
are the opposite rim pairs `13` and `24`; the decoder supplies at least one.
The weaker order-three mask allowed at the hub is exactly what total degree
at least seven gives there.

For a wheel with rim order at least five, the source's five bags are
connected and disjoint even at the endpoint `m=5`: the displayed tail of
`B_4` is then empty after `v_4`.  For larger wheels it is a connected rim
segment.  The hub in `B_0` contacts all other bags.  Bags `B_1,...,B_4`
inherit `12,23,34`; their remaining pairs are exactly `13,14,24`, and the
decoder supplies two.  Hence there are at least four hub contacts and five
contacts amongst the other bags.

In the prism ordering

```text
b_0, a_1, b_2, a_0, b_1,
```

the inherited pairs are `02,03,04,13,14,24`, leaving exactly the path
`01,12,23,34`.  Covering three gives nine contacts.  In the `K_{3,3}`
ordering, the six cross-part pairs are inherited and the four nonedges are
exactly `01,02,12,34`; again three covered pairs give nine contacts.  The
omitted sixth core vertex is not used in either construction.

All bags in all five rows are connected, disjoint, and rooted at five
distinct boundary vertices.  They avoid the sixth root entirely.  The two
other full components then complete them without assuming an edge between
open components: put the unused root into one component bag, and its edge to
the other full component supplies the last outer contact.

## 3. Carrier and degree hypotheses

The pinned four-root theorem applies to a target-free six-connected host
with at least three components behind the six-cut, exactly the source setup.
A vertex whose attachment mask contains `Z` is a singleton `Z`-carrier, so
three masks sharing a four-set are forbidden.

If no total-degree-six vertex exists, six-connectivity makes every total
degree at least seven.  A wheel rim, prism vertex, or `K_{3,3}` vertex has
three internal neighbours and hence mask order at least four.  The `W_3`
hub has the same degree, the `W_4` hub has four internal neighbours and mask
order at least three, and the long-wheel construction never needs a hub
mask.  These are exactly, and not stronger than, the verifier hypotheses.

The published Wood--Woodall classification was checked against the primary
paper: a three-connected `(K_5-e)`-minor-free graph is a wheel, the triangular
prism, or `K_{3,3}`.  The cases above therefore exhaust the structural input.

## 4. Exact-six return

The contradictions in all Wood--Woodall cases force a vertex `v` of total
degree six.  Its neighbourhood is a genuine separator: deleting it isolates
`v`, whilst either of the other components of `G-S` remains as a far side.

Three-connectivity gives `d_C(v)>=3`, so at most three members of
`N_G(v)` lie in `S`; consequently `S-N_G(v)` is nonempty.  Completing `S`
to a clique adds no edge incident with `v`, and `{v}` is a component behind
the derived exact six-cut with the orientation required by the pinned
rerooting theorem.  That theorem explicitly permits boundary vertices in
`C`, so the internal neighbours of `v` in the new boundary cause no scope
problem.

The coefficient-four calculation and partition are exact:

```text
eta_{N(v)}({v})=0+6-4=2,
eta_S(C)=2+eta_S(C-{v}).
```

Punctured-rooted exclusion therefore descends to the singleton fragment.
No packet transfer or connectivity of the complementary bookkeeping side is
claimed.

## 5. Scope verdict

No counterexample, missing branch-set contact, carrier-quantifier error, or
exact-six orientation error was found.  The theorem removes the whole
three-connected ordinary-`K_5^-`-minor-free row.  It correctly leaves lobes
with an ordinary near-five minor and non-three-connected nested
two-separations outside its conclusion.
