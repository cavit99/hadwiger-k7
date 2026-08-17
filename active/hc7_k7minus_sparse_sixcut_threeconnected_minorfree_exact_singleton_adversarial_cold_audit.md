# Adversarial cold audit: three-connected minor-free exact singleton

**Verdict:** **GREEN** for the exact revisions below.  This audit was made
independently of the author and the other adjacent audit.  It specifically
pressure-tests the five exceptional-core root assignments, the four-root
packing hypothesis, the terminal composition, and the derived exact-six
lift.  It is not
external peer review.

## Pinned artefacts

```text
8c8084bf0291098c2a323d43200562f5d0aaad5b61503bb3c78390f27c9e5176
  active/hc7_k7minus_sparse_sixcut_threeconnected_minorfree_exact_singleton.md
37584ca0a390c9d556fdfe7cdfc83d24afd7f5fe39987209693f0512c83d60ca
  active/experiments/sparse_sixcut_wood_woodall_rooting/verify.c
e63be6b2758356e8f141b14cb688e66cc84cd433181c7518d796a17d7b76f40f
  active/experiments/sparse_sixcut_wood_woodall_rooting/README.md
```

Relative to the mathematical revision originally audited, the theorem,
proof, dependencies and exhaustive search are unchanged.  The current text
uses descriptive four-root-packing and root-assignment terminology and makes
explicit that the exact singleton is a descent output, not a terminal
elimination of the whole weighted local problem.  The verifier changes only
corresponding identifier and output labels.

The verifier was rebuilt with `-std=c11 -O2 -Wall -Wextra -Werror
-pedantic` and rerun.  A separate AddressSanitizer/UndefinedBehaviourSanitizer
build, with leak detection disabled because it is unavailable under the
runner's tracing layer, produced the same output and no diagnostic:

```text
W3 tested=234256 assignment_failures=15 four_set_admissible_failures=0
W4 tested=9838752 assignment_failures=75 four_set_admissible_failures=0
long-wheel tested=5153632 assignment_failures=15 four_set_admissible_failures=0
prism tested=5153632 assignment_failures=15 four_set_admissible_failures=0
K33 tested=5153632 assignment_failures=15 four_set_admissible_failures=0
```

## 1. Finite trust boundary

The mask arrays are exactly the `42` subsets of a six-set of order at least
three and the `22` subsets of order at least four.  The nested loops enumerate
ordered tuples, not a symmetry sample, so their sizes are precisely `22^4`,
`42*22^4`, and `22^5`.

For every tuple, `violates_four_set_condition` checks all fifteen four-sets
and returns true exactly when one is contained in at least three masks.
Three vertices with those masks are three disjoint connected singleton
subgraphs, each adjacent to all four roots, so this is exactly the imported
packing obstruction, with no converse being assumed.

The five-bag routine tries every injection of five roots into the six-set,
requires the root assigned to bag `i` to lie in its mask, and counts `ij`
only when the assigned root of one bag is adjacent to the core vertex of the
other.  The `W_3` routine independently selects the fifth singleton root,
requires it to occur in three masks, and then finds four distinct assigned
roots avoiding it.  Thus the program checks literal branch-bag contacts,
not merely mask unions.  Every raw failure violates the four-set condition,
and
the asserted mask lemma follows within this finite boundary.

## 2. Exceptional-core root assignments

For `W_3=K_4`, the four two-vertex rooted bags inherit all six clique
contacts.  The fifth singleton root meets at least three of them, so at most
one of ten pairs is absent.

For `W_4`, the hub and rim supply eight contacts.  The only absent core pairs
are the opposite rim pairs `13` and `24`; the root assignment supplies at
least one.
The weaker order-three mask allowed at the hub is exactly what total degree
at least seven gives there.

For a wheel with rim order at least five, the source's five bags are
connected and disjoint even at the endpoint `m=5`: the displayed tail of
`B_4` is then empty after `v_4`.  For larger wheels it is a connected rim
segment.  The hub in `B_0` contacts all other bags.  Bags `B_1,...,B_4`
inherit `12,23,34`; their remaining pairs are exactly `13,14,24`, and the
root assignment supplies two.  Hence there are at least four hub contacts
and five
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

All bags in all five cases are connected, disjoint, and rooted at five
distinct boundary vertices.  They avoid the sixth root entirely.  The two
other full components then complete them without assuming an edge between
open components: put the unused root into one component bag, and its edge to
the other full component supplies the last outer contact.

## 3. Four-root packing and degree hypotheses

The pinned four-root theorem applies to a target-free six-connected host
with at least three components behind the six-cut, exactly the source setup.
A vertex whose attachment mask contains `Z` is a connected singleton
subgraph adjacent to every vertex of `Z`, so three masks sharing a four-set
are forbidden.

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
No transfer of two boundary-full connected subgraphs or connectivity of the
complementary bookkeeping side is claimed.

## 5. Scope verdict

No counterexample, missing branch-set contact, four-root-packing quantifier
error, or exact-six orientation error was found.  The theorem eliminates the
no-exact-fragment subcase of the three-connected
ordinary-`K_5^-`-minor-free case.  The returned exact fragment is a descent
output, not a terminal contradiction; transfer across it, lobes with an
ordinary near-five minor, and non-three-connected nested two-separations
remain.
