# Internal audit: shore-allocation barriers

Audited file:
`barriers/hc7_k7minus_shore_allocation_barrier.md`

Audited source SHA-256:

```text
e6d3bf5c480ad3775de530014aa70f2bb1e32c880e64af45a3087e30d93acee9
```

Retained verifier SHA-256:

```text
a41e5125738eab3cf2180d883f349f73f34c564b8568c8d62763d70173686643
```

The retained verifier refuses optimized Python execution, so its
assertion-based checks cannot be silently disabled with `python -O`.

**Verdict:** **GREEN** for the exact revision.

This is a separate internal mathematical and computational audit, not
independent human review or external peer review.

## Balanced-label barrier

For every one of the 15 diamond-deletion boundary types, the verifier
checks one fixed two-shore labelling of all boundary nonedges.  For every
independent triple, each label occurs on at least two nonedges of the
five-vertex reserve.  All stored masks are confined to actual nonedges, and
their sorted certificate digest is

```text
325a008189de182c099d60990d72c94f02fe78709e4858bc5aa48ec8eba59367
```

A separate constraint search, initialized without the stored masks, found
a qualifying labelling for all 15 types and independently validated the
saved witnesses.  Thus the refuted inference really fails for every
independent-triple rotation.  The labels remain abstract; the note does not
claim that they arise simultaneously from critical Kempe responses.

## Mechanism witness

Independent decoding confirms that the boundary is
`K_3` disjoint-union `K_3` disjoint-union `K_2`.  The three added vertices
are independent and complete to the boundary.  Direct checks give
connectivity three and chromatic number four, and every independent triple
leaves reserve `2K_2` disjoint-union `K_1`.

The rooted-model argument is sound: with only one universal nonroot, at
least four of five rooted bags are singleton roots, and those four have far
too few mutual contacts for a rooted `K_5^-`.  Independent exhaustive
connected-bag enumeration found no rooted near-model for any of the 18
independent triples.

For the full graph, the clique-sum explanation is valid because
`K_7^-` is five-connected.  The retained verifier independently enumerates
all spanning seven-bag connected partitions and finds no model with at
least 20 contacts.  A second exact deletion/contraction search reached 987
cached states and also returned negative; literal and subdivided
`K_7^-` positive controls returned positive.

The verifier reproduced

```text
balanced global shore labels=15/15 every rotation keeps 2 demands per shore
balanced-witness sha256=325a008189de182c099d60990d72c94f02fe78709e4858bc5aa48ec8eba59367
mechanism graph vertices=11 connectivity=3 chromatic_number=4
mechanism independent triples=18 shore-rooted K5-minus=0
mechanism K7-minus minor=no
PASS K7-minus shore-allocation barriers
```

## Scope

No mathematical or finite-encoding defect was found.  The mechanism is
only three-connected and four-chromatic and is not proper-minor
six-colour-critical.  It therefore does not refute the critical-host
shore-allocation target.  Together the two results refute only static
boundary-counting and fullness-plus-minor-exclusion shortcuts; they show
that compatible critical colourings or additional packet-one topology must
do essential work.
