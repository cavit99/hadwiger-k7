# Cold internal audit: rooted carriers at a dominated degree-eight centre

**Verdict:** **GREEN.**  The four finite composition results, their
rooted-model lifts, the elimination of the biclique, theta and chorded-cycle
outcomes, the complete irreducible-kernel residue, the four-bag refinement
and the two-augmentation theorem are correct at the pinned revisions below.
Three connected common-neighbour types remain; this does not close the
dominated-centre case or `HC_7`.

This audit was performed independently of the theorem and verifier author.
It is an internal cold audit, not external peer review.

## Exact revisions and reproduction

```text
679c340cafd0b27bf16ddfcf7829dde2ab73d0403df3c41603ec9a2a5e4e1dd5  active/hc7_k7minus_dominated_degree_eight_rooted_seven_carrier.md
79fb33eacad3591c6f89c0bf1758475287feb462999927241daf8a83a3961927  active/experiments/dominated_singleton_rooted_seven_carrier/verify.py
7f062d12451b751d71789144b85bf09ff5a2ee29306702385eb4e0416c4e6cc2  active/experiments/dominated_singleton_rooted_seven_carrier/README.md
ab9df3d879e53784f8afcc77dfc7f37137a5e1a370caee95df01fc905b00cfb7  active/experiments/dominated_singleton_complete_seven_terminal_kernel/verify.py
a2ccef4f3fc2718c2f79dd461c540f2b3483b805c034596dfc3838ec4d7ec228  active/experiments/dominated_singleton_complete_seven_terminal_kernel/README.md
81980e29daba936ace8e599a1147ffad233a227718247cce8872cadbbe9d4495  active/experiments/dominated_singleton_low_degree_completion/verify.py
91097a5185909dd69684783b3175f4e57e9ec84b9b973c26442069f55e6e9a25  results/hc7_seven_terminal_irreducible_kernel_classification.md
925b390b35a22f54db30f6b0608ff55bea6f5b971578fb3aa4394bfd308f1744  results/hc7_seven_terminal_irreducible_kernel_classification_audit.md
```

The verifier was rerun at these revisions with assertions enabled.  It
reproduced, in particular,

```text
K3,4 survivors=0
C7 survivors=456, fixed-Q orbits=125
live C7 placements=402, fixed-Q orbits=99
post-F5 C7 placements=326, fixed-Q orbits=64
robust F5 five-set counts on the five live Q types: 0,0,1,0,1
independent five-block partitions=438
rainbow-robust failures=322
complete order-seven carriers=5495, failures=21, fixed-Q orbits=4
complete order-eight templates=30600, failures=89, fixed-Q orbits=13
four-contact refinement: order-seven 0/735 failures
four-contact refinement: order-eight 0/3115 failures
```

As an independent check, I enumerated every partition of every subset of
the seven quotient vertices into five nonempty connected branch sets and
tested the ten inter-branch-set adjacencies directly.  This did not use the
verifier's deletion-and-contraction recursion.  It confirmed all 315
`K_{3,4}` closures, exactly 456 cycle survivors, and the complete robust
five-set count vector

```text
FCQ`_:0  FCQb_:0  FCR`o:1  FCp`_:0  FCpb_:1
FCpV?:3  FCpv?:6  FCZb_:6  FCxv?:21.
```

I also replayed all 21 and 89 complete-kernel survivors with a second minor
implementation based on connected set partitions, rather than the imported
deletion-and-contraction recursion.  It independently confirmed every
survivor and every one of the 3,850 four-contact closures.  The replay used
888 distinct seven-vertex quotients.

## 1. Rooted quotient lift

Let `B_q`, for `q in Q`, be the seven disjoint connected rooted bags.  A
carrier edge is an actual edge between the corresponding bags.  A literal
edge `qr` of `G[Q]` is also an actual edge between those bags, through the
vertices `q in B_q` and `r in B_r`.  Hence their adjacency graph contains
the simple labelled union `Q union F`.

For each branch set of a `K_5^-` model in that union, take the union of all
rooted bags indexed by its vertices.  Quotient-model edges make this union
connected; the five unions remain disjoint and retain every required
adjacency.  Each contains at least one literal member of `Q`.  Both `u`
and `v` are complete to `Q` and `uv` is an edge, so the singleton bags
`{u},{v}` extend these five rooted bags to a `K_7^-` model.  This argument
does not treat a carrier adjacency as an edge between terminal vertices.

## 2. Complete finite carrier coverage

The imported classification consists of exactly the nine unlabelled
order-seven graphs which are triangle-free, have independence number at
most three, contain no `K_5^-` minor, and possess a cut of order at most
two.  At this order triangle-freeness makes the stated independence number
equal to three.

There are `binom(7,3)=35` labelled `3+4` bipartitions and `7!/14=360`
undirected labelled seven-cycles.  Testing each on every eligible graph
covers every labelling allowed by the universal seven-terminal theorem.
All 315 biclique unions contain `K_5^-`; the cycle screen has the asserted
456 survivors and 125 orbits under the automorphism group of the fixed
literal graph `Q`.

For the five-root screen, every five-subset and all 60 labelled copies of
`F_5=K_1 vee P_4` are tested.  Thus a set is declared robust only when
**every** possible hub and path labelling closes, exactly matching the
unprescribed labelling in the universal rooted-fan theorem.  The theta
graph and the chorded seven-cycle each have one such set; the other three
live types have none.

## 3. Five-root deletion lift

For either positive graph, let `R` be its robust five-set and
`D=Q-R`.  Since `H=G-{u,v}` is five-connected, `H-D` is
three-connected: a cut of order at most two in `H-D`, together with the
two deleted vertices, would be a cut of order at most four in `H`.

The universal five-terminal theorem therefore gives an `R`-rooted
`F_5` model in `H-D`.  Its five bags avoid both vertices of `D`; adding
those vertices as singleton bags is consequently legitimate.  Literal
edges of `Q` and the rooted carrier edges give an adjacency graph
containing `Q union F`.  Robustness and the quotient-lift lemma then give
a `Q`-meeting `K_5^-` model, and adjoining `{u},{v}` gives the forbidden
minor.  Deleting `D` before choosing the rooted model is essential and
correctly resolves the possible absorption of an unused root.

This eliminates exactly the theta graph with path lengths `2,3,3` and the
seven-cycle with a chord bounding cycles of orders four and five.  The
connected-exterior classification had five types, so the remaining three
are

```text
C5 disjoint-union K2,
C5 with a pendant path of length two,
C7.
```

Their cycle-carrier subtotals are `150+84+92=326` placements and
`11+42+11=64` fixed-`Q` orbits.

## 4. Two connected augmentations

Let the rooted-cycle bags be `B_0,...,B_6`.  Absorb the two disjoint
connected augmenting sets into the adjacent bags `B_0,B_1`.  Each
augmentation meets its owner, so the enlarged bag is connected, and it
meets every other cycle bag, so each enlarged bag is universal in the
seven-bag quotient.  They remain disjoint.  The old cycle edge also keeps
the two enlarged bags adjacent.

The unchanged bags `B_2,...,B_6` contain a path in that order.  The
quotient therefore contains `K_2 vee P_5`.  Its two universal vertices
together with three consecutive path vertices induce `K_5^-`.  Those five
bags still meet `Q`, so adjoining `{u},{v}` gives `K_7^-`.  No edge
between the two augmenting sets is assumed or used.

## 5. Complete irreducible kernels and four-bag augmentation

The imported kernel classification has the quantifiers used by the new
screen.  On seven roots, every three-connected carrier contains one of the
5,495 labelled edge-minimal spanning three-connected graphs.  In the
order-eight branch, every irreducible kernel is one of 30,600 labelled
wheel, one-chord or two-chord templates, and **every** neighbour of the
extra bag is a legal owner.  Thus completeness requires every order-seven
carrier, and for each order-eight template it may choose a closing owner.
The verifier implements precisely these universal/existential quantifiers.

The order-seven composition leaves 21 labelled failures.  Their degree
sequence is `6,3,3,3,3,3,3`.  The degree-six vertex is universal; deleting
it leaves a simple two-regular graph on six vertices.  Three-connectivity
rules out two disjoint triangles, so the carrier is a six-wheel, as claimed.
The four fixed-`Q` orbit count follows by applying the automorphism group of
each fixed common-neighbour graph to the carrier mask.

The order-eight composition leaves 89 templates.  Their terminal-edge and
extra-neighbour profiles are

```text
(0 chords, 7 contacts): 13
(1 chord, 5 contacts): 19
(1 chord, 6 contacts): 38
(1 chord, 7 contacts): 19.
```

Hence every survivor is a wheel or one-chord template, and no two-chord
template survives.  Relabelling the terminal-edge and neighbour masks
together gives thirteen fixed-`Q` orbits.  The asserted failure counts and
profiles are now executable assertions, not unverified printed totals.

For a connected set meeting four named rooted bags, absorption into one
contacted owner adds exactly the star from that owner to the other three
contacted bags.  This is the finite operation tested in the order-seven
case.  In the order-eight case the catalogue permits the extra kernel bag
to be absorbed into any of its neighbours.  The verifier chooses that
owner and a distinct contacted owner for the new connected set, then adds
the two actual stars.  It proves

```text
21 * binom(7,4) = 735
89 * binom(7,4) = 3115
```

closures with no failure.  The host lift is valid provided the new
connected set is disjoint from the seven bags after the kernel owner has
been chosen and meets the four specified bags.  The result does not supply
such a set.

Corollary 5.3's spanning assertion is also correct.  The terminal-kernel
reduction uses contractions but no vertex deletions, so the lifted kernel
bags partition all of `V(H)`.  Deleting carrier edges in the order-seven
quotient changes no bag.  Absorbing the order-eight extra bag into a legal
owner also preserves the union of the bags.  Target exclusion forces the
chosen order-seven carrier or order-eight template into the corresponding
21/89 failure list; otherwise Lemma 1.1 lifts the quotient `K_5^-` model.

For this canonical spanning model, an exterior augmenting component does
not exist.  Proposition 5.2 instead specifies the quotient effect required
from an internal split.  The definition of a movable set preserves the
source root, source connectivity and every old carrier adjacency; adjoining
the connected piece to its contacted owner is therefore a valid branch-set
move.  If it contacts four bags, it realises exactly the tested four-contact
star.  In the order-eight branch the kernel owner and movement owner must be
chosen as the distinct pair certified by the finite screen.

## 6. Negative diagnostics

The minimum-added-edge loop tests subsets of missing quotient edges in
increasing order and asserts the histograms

```text
all 456:  1:381, 2:61, 3:13, 4:1
live 402: 1:334, 2:54, 3:13, 4:1.
```

The unique four-edge case is the union of two edge-disjoint seven-cycles,
namely the complement of a seven-cycle.  Thus an unspecified additional
carrier adjacency is not a sufficient repair.

The connected-owner check models absorption of one connected set by adding
its star of contacts from every possible owner; 666 of 11,658 cases remain,
including fourteen full seven-bag contact sets.  The aligned-`K_4` check
adds every clique edge among four existing cycle bags and still has 701
failures.  These are valid quotient barriers, but not host
counterexamples: they forget five-connectivity away from the roots,
critical colourings and response provenance.

Finally, all proper partitions of `Q` into five nonempty independent
blocks are enumerated.  There are 438 such set partitions (the five blocks
themselves are unordered).
For each one, the verifier enumerates every rainbow transversal and asks
whether at least one is a robust five-set.  There are 322 failures.  In
particular, none of the final three graph types has any robust five-set, so
a black-box choice of a rainbow transversal followed by an arbitrarily
labelled universal rooted fan is not terminal.  This is a quotient
diagnostic, not an unbounded impossibility theorem; it does not exclude a
model chosen in coordination with Kempe components.

## 7. Scope

The selected irreducible-kernel lift is spanning, so five-connectivity
cannot supply an exterior augmenting component.  Before making a carrier
spanning, connectivity would guarantee boundary **vertices**, not four
distinct contacted bags.  The fifteen opposite operation signatures
likewise do not identify palette colours with kernel-bag labels or make a
piece of one bag movable.

The exact remaining step is correctly recorded as a response-sensitive
four-bag split theorem: an operation-labelled connected subgraph inside one
spanning bag must be made movable into another while meeting four named
bags, or directly give the rooted target.  No gap was found in the proved
conclusions, and the source does not claim closure of the dominated-centre
case, the eight-coordinate branch, Conjecture 21, or `HC_7`.
