# Second cold audit: three-connected minor-free exact singleton

**Verdict:** **GREEN** at the pinned revisions below.  This audit was carried
out independently of the first assigned audit.  It certifies the finite mask
quantifiers, every exceptional-core root assignment, the terminal
composition, and the exact-fragment bookkeeping; it is not external peer
review.

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

The verifier was rebuilt with
`-std=c11 -O2 -Wall -Wextra -Werror -pedantic` and rerun from a fresh
temporary executable.  It reproduced exactly

```text
W3 tested=234256 assignment_failures=15 four_set_admissible_failures=0
W4 tested=9838752 assignment_failures=75 four_set_admissible_failures=0
long-wheel tested=5153632 assignment_failures=15 four_set_admissible_failures=0
prism tested=5153632 assignment_failures=15 four_set_admissible_failures=0
K33 tested=5153632 assignment_failures=15 four_set_admissible_failures=0
```

## 1. Finite mask lemma

The arrays contain exactly all `42` six-bit masks of order at least three
and all `22` masks of order at least four.  The loops therefore enumerate
the full ordered products `22^4`, `42*22^4`, and `22^5`; no symmetry
quotient or random sample is hidden in the counts.

`violates_four_set_condition` checks all fifteen four-subsets and rejects
precisely a tuple in which one is contained in at least three masks.  This is
exactly the previously audited four-root packing bound for connected
singleton subgraphs.  For each retained tuple, the program tries every
injection of the relevant four or five bag roots into the six-set.  A pair
`ij` is counted precisely when the root in one two-vertex bag is adjacent to
the core vertex in the other.  The `W3`
routine additionally chooses the fifth singleton root, requires it to see
at least three core vertices, and then assigns four distinct roots avoiding
it.  Hence coverage in the program is actual bag contact, not merely union
coverage.

Every raw assignment failure is certified to violate the four-set condition.
The five asserted finite statements consequently follow with the displayed
finite trust boundary.

## 2. Wood--Woodall cases and bag accounting

The published statement of Wood and Woodall, Lemma 4.2.1, was checked
directly: the three-connected `(K_5-e)`-minor-free graphs are the wheels,
the triangular prism, and `K_{3,3}`.

For `W_3=K_4`, the four rooted core bags are mutually adjacent and the
singleton fifth root meets at least three, leaving at most one noncontact.
For `W_4`, the core has eight edges and its only missing pairs are `13,24`;
the root assignment supplies one.  In a long wheel, `B_0` contains the hub and is
universal to the other four bags.  Those four inherit `12,23,34`, and their
other pairs are exactly `13,14,24`; covering two gives five of their six
contacts.  The definition of `B_4` also works when the rim has order five.

With the prism ordering in the source, the six inherited edges leave
exactly `01,12,23,34`; with the `K_{3,3}` ordering, the six cross edges
leave exactly `01,02,12,34`.  Three covered pairs therefore give nine
contacts in either case.  All displayed bags are connected, disjoint, use
five distinct roots, and are confined after omitting the sixth root.

The two other full components complete any such five-bag model exactly as
claimed: one absorbs the unused root and thereby contacts the other
component, while both contact all five rooted bags through their roots.
Thus there is no assumed edge between distinct open components.

## 3. Exact singleton and excess

If no total-degree-six vertex exists, six-connectivity raises every total
degree to at least seven.  A wheel rim vertex then has at least four boundary
neighbours; the `W_4` hub has at least three; and every prism or `K_{3,3}`
vertex has at least four.  These are exactly the hypotheses sent to the
finite root assignments.  The long-wheel construction needs no boundary root at the
hub.  All Wood--Woodall cases therefore contradict target exclusion, so a
degree-six vertex exists.

Its full neighbourhood is a genuine exact six-cut: deletion isolates the
vertex and the other components of `G-S` provide a far side.  Three-
connectivity gives at least three neighbours in `C`, so at most three of the
six neighbours lie in `S`; hence `S-U` is nonempty and the exact-fragment
orientation is legal.  Completing `S` adds no edge incident with the
singleton.  Finally

```text
eta_U({v})=0+6-4=2,
eta_S(C)=eta_U({v})+eta_S(C-{v}),
```

by a direct partition of internal edges, boundary incidences, and vertex
terms.  The pinned exact-six rerooting theorem therefore applies with the
claimed orientation.

No quantifier, contact, exceptional-core label, terminal-composition, or
additivity defect was found.  The source also states its scope correctly:
the exact singleton is a nonterminal descent output, while ordinary
near-five minors and non-three-connected nested two-separations remain
outside this theorem.
