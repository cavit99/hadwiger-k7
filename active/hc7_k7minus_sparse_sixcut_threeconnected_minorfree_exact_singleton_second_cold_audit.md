# Second cold audit: three-connected minor-free exact singleton

**Verdict:** **GREEN** at the pinned revisions below.  This audit was carried
out independently of the first assigned audit.  It certifies the finite mask
quantifiers, every exceptional-core decoder, the terminal composition, and
the exact-fragment bookkeeping; it is not external peer review.

## Pinned artefacts

```text
98bf46538abc095e7722db332eaf6d31fcbddca485ab669c98a700c231044760
  active/hc7_k7minus_sparse_sixcut_threeconnected_minorfree_exact_singleton.md
56b40afd3ab310fa3b7a71bc4a6bc5afeae2505b94c69d14b870df11e6f389a3
  active/experiments/sparse_sixcut_wood_woodall_rooting/verify.c
f6598778e66d5006264a1113e8d162d368793abf768e80e493a8477743163841
  active/experiments/sparse_sixcut_wood_woodall_rooting/README.md
```

The verifier was rebuilt with
`-std=c11 -O2 -Wall -Wextra -Werror -pedantic` and rerun from a fresh
temporary executable.  It reproduced exactly

```text
W3 tested=234256 decoder_failures=15 carrier_admissible_failures=0
W4 tested=9838752 decoder_failures=75 carrier_admissible_failures=0
long-wheel tested=5153632 decoder_failures=15 carrier_admissible_failures=0
prism tested=5153632 decoder_failures=15 carrier_admissible_failures=0
K33 tested=5153632 decoder_failures=15 carrier_admissible_failures=0
```

## 1. Finite mask lemma

The arrays contain exactly all `42` six-bit masks of order at least three
and all `22` masks of order at least four.  The loops therefore enumerate
the full ordered products `22^4`, `42*22^4`, and `22^5`; no symmetry
quotient or random sample is hidden in the counts.

`carrier_violation` checks all fifteen four-subsets and rejects precisely a
tuple in which one is contained in at least three masks.  This is exactly
the previously audited singleton four-root carrier guard.  For each retained
tuple, the decoder tries every injection of the relevant four or five bag
roots into the six-set.  A pair `ij` is counted precisely when the root in
one two-vertex bag is adjacent to the core vertex in the other.  The `W3`
routine additionally chooses the fifth singleton root, requires it to see
at least three core vertices, and then assigns four distinct roots avoiding
it.  Hence coverage in the program is actual bag contact, not merely union
coverage.

Every raw decoder failure is certified to violate the carrier guard.  The
five asserted finite statements consequently follow with the displayed
finite trust boundary.

## 2. Wood--Woodall cases and bag accounting

The published statement of Wood and Woodall, Lemma 4.2.1, was checked
directly: the three-connected `(K_5-e)`-minor-free graphs are the wheels,
the triangular prism, and `K_{3,3}`.

For `W_3=K_4`, the four rooted core bags are mutually adjacent and the
singleton fifth root meets at least three, leaving at most one noncontact.
For `W_4`, the core has eight edges and its only missing pairs are `13,24`;
the decoder supplies one.  In a long wheel, `B_0` contains the hub and is
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
finite decoders.  The long-wheel construction needs no boundary root at the
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
ordinary near-five minors and non-three-connected nested two-separations
remain outside this theorem.
