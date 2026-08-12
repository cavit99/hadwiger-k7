# Internal self-audit: rooted carriers at a dominated degree-eight centre

**Verdict:** **GREEN as an internal self-check** for the written host lifts,
the two-type elimination, and the exact recorded route nonclosure.  The
finite claims are computer-assisted.  This is neither a cold audit nor
external peer review.

## 1. Audited revision

The source and finite materials checked are listed by SHA-256 at the end of
this note.  The deterministic verifier was run from the repository root
without optimisation, so its assertions were active.

The audit checked claim scope separately:

* Lemmas 2.1 and 2.2 are computer-assisted finite results on the fixed
  seven-vertex set `Q`;
* Lemmas 1.1 and Theorems 3.1, 3.2 and 4.1 are unbounded written proofs;
* Propositions 5.1 and 5.2 are computer-assisted finite results with an
  explicit conditional branch-set lift;
* Corollary 5.3 is an unbounded written consequence of the terminal-legal
  contraction lift and the complete finite catalogue;
* the augmentation failures in Section 6 refute only quotient-level
  implications; and
* Section 7 records an unsupported inference, not a theorem or a
  counterexample to the host statement.

Corollary 3.4 is a direct use of the separately audited full forest-shore
theorem.  In the order-seven alternative, the exact-interface theorem
identifies the component outside the cut as the edge `uv`, which is a tree.
All critical-host hypotheses of the imported theorem are already in force.
Thus the surviving exact interface genuinely has order eight and singleton
component `\{u\}`.

## 2. Rooted quotient lift

The delicate distinction between terminal edges and model adjacencies is
respected.  A carrier edge is an actual adjacency between two rooted branch
sets.  A literal edge `qr` of `Q` is also an actual adjacency between those
sets because they contain `q` and `r`.  Consequently the branch-set
adjacency graph contains `Q\cup F`.

Taking unions of rooted bags along a quotient minor preserves connectivity,
disjointness and required adjacencies.  Every resulting branch set contains
at least one root.  Since both `u` and `v` are adjacent to every member of
`Q` and to each other, they extend a `Q`-meeting `K_5^-` model to exactly the
required `K_7^-` model.  No carrier edge is treated as an edge between the
terminal vertices themselves.

## 3. Finite coverage

The verifier imports the nine eligible graphs and exact recursive minor
routine from the adjacent audited classification.  It independently
generates:

* 360 undirected labelled seven-cycles;
* 35 labelled copies of `K_{3,4}`; and
* 60 labelled copies of `K_1\vee P_4` on each of 21 five-subsets.

The seven-terminal screen covers

```text
9 * (360 + 35) = 3555
```

labelled unions.  It asserts 456 total survivors, that all are cycle
carriers, and that their fixed-`Q` automorphism quotient has 125 orbits.
It also asserts 402 placements and 99 orbits for the five connected live
types, followed by 326 placements and 64 orbits for the three types left by
the rooted-fan elimination.

The rooted-fan screen covers

```text
9 * 21 * 60 = 11340
```

labelled unions.  The robust five-set counts on the five connected live
types are respectively

```text
0, 0, 1, 0, 1
```

in the order

```text
C5 disjoint-union K2,
C5 with a pendant path of length two,
theta(2,3,3),
C7,
chorded C7.
```

The two positive sets are printed explicitly.  Every fan labelling on each
of them closes, which is exactly the quantifier required because the
universal rooted-fan theorem does not prescribe its labelling.

The second verifier regenerates the complete seven-terminal kernel
catalogue with its audited quantifier order.  It checks all 5,495 labelled
minimal order-seven carriers universally.  It checks all 30,600 order-eight
templates universally, but accepts each fixed template when **some** legal
owner closes.

There are 21 failed order-seven placements in four fixed-`Q` orbits, all
with degree profile `6,3,3,3,3,3,3`; hence every carrier is a six-wheel.
There are 89 order-eight failures in thirteen orbits.  Their terminal
graphs have zero or one chord; no two-chord template survives.

For every four-subset of the seven rooted bags, the verifier then checks a
connected augmentation absorbed at a contacted owner.  Its exact totals are

```text
21 * binom(7,4) = 735,
89 * binom(7,4) = 3115.
```

In the order-eight test it ranges over every legal owner of the kernel's
extra vertex and requires a distinct augmentation owner.  Both screens have
zero failure.  This proves the finite quotient result, not the existence of
the connected augmentation in the host.

The verifier now asserts the full failure distributions, structural
profiles and owner histogram, rather than merely printing them.  In
particular, the 89 order-eight failures consist only of wheel and one-chord
templates with the four displayed extra-neighbour counts; a two-chord
failure would violate an assertion.

## 4. Five-root deletion lift

This is the most important new host step.  Let `R` be the robust five-set
and delete the other two vertices `D=Q-R` before applying the rooted-fan
theorem.  Five-connectivity of `H` implies three-connectivity of `H-D`: a
separator of order at most two there, together with `D`, would be a
separator of order at most four in `H`.

The five returned rooted bags therefore avoid both omitted roots.  Adding
the latter as singleton bags is legitimate.  All seven branch sets are
disjoint, and literal `Q` edges give precisely the extra quotient
adjacencies used by the finite certificate.  This validates the theta and
chorded-cycle elimination.

Applying the rooted-fan theorem directly in `H` would not validate this
step: an omitted root could lie inside a fan bag.  The source explicitly
records why deleting the two vertices is necessary.

## 5. Two-augmentation theorem

If two disjoint connected sets each meet all seven cycle bags, they may be
absorbed into two adjacent cycle bags.  The original cycle edge keeps the
two enlarged bags adjacent; each absorbed set makes its owner adjacent to
all other bags.  Deleting those two adjacent positions from the seven-cycle
leaves a five-vertex path.  Thus the quotient contains `K_2\vee P_5`.

The two hubs and three consecutive path vertices have nine of the ten
possible edges, hence form `K_5^-`.  All five bags retain a root, so the
two-apex lift is valid.  No adjacency between the two augmenting sets is
assumed or used.

## 6. Negative diagnostics and trust boundary

The minimum-added-edge search exhausts subsets of missing quotient edges in
increasing order and asserts the histograms

```text
all 456:  {1:381, 2:61, 3:13, 4:1}
live 402: {1:334, 2:54, 3:13, 4:1}.
```

The unique four-edge placement is printed.  The connected-owner test adds
exactly the star adjacencies obtained by absorbing one connected set into
one of the bags it meets.  The aligned-`K_4` test is deliberately stronger
than an unrelated rooted `K_4`: it inserts all six clique adjacencies among
four existing cycle bags.  Their failures therefore justify the stated
quotient barriers.

The proper five-block partitions are enumerated as partitions into
nonempty independent sets.  They show that colour saturation cannot select
a robust five-set in any of the three final graph types.  This does not
refute a proof using the internal geometry of Kempe components or a
different rooted-fan model.

Finally, five-connectivity bounds the number of **vertices** in the
boundary of a component outside a fixed carrier model.  It does not force
four distinct carrier-bag neighbours, and a spanning carrier has no outside
component.  The source therefore does not infer either Theorem 4.1 or the
four-bag augmentation in Proposition 5.2 from connectivity alone.  Nor does
it identify the four five-centre operation labels with either palette
colours or carrier bags.

## 7. Complete-kernel trust boundary

For the elementary host lift of Proposition 5.2, the augmenting set must be
disjoint from the seven current rooted bags.  Absorbing it at a contacted
bag then creates the exact star checked in the quotient.  Four attachment
**vertices** are not enough if they occupy fewer than four bags.

The exact terminal-kernel lift is stronger than a vertex-maximal choice: its
branch sets are the inverse images of terminal-legal contractions and hence
partition all vertices of `H`.  In the order-eight branch, absorbing the
extra bag at a legal owner preserves that union.  Corollary 5.3 is therefore
correctly stated with a spanning seven-bag model.  If its quotient were not
among the 21 or 89 finite failures, Proposition 5.1 and the rooted quotient
lift would already give the target.

At this spanning endpoint there is no outside component, and
five-connectivity supplies no attachment set at all.  Proposition 5.2 can
be used only after splitting a connected piece from an existing branch set
while retaining the source root and every carrier adjacency.  Moving that
piece to a contacted owner creates exactly the quotient star checked by the
verifier.  The source correctly records this additional condition rather
than inferring a split from the finite calculation.

Likewise, a component meeting at most three bags need not create a cut of
order at most four: its open neighbourhood may contain arbitrarily many
vertices inside those three branch sets.  Replacing those vertices by the
three bag labels is a contraction in the quotient, not a separator in the
host.  Any positive argument must split one of the branch sets or use an
operation-labelled connected subgraph before all vertices are absorbed.

All four other exceptional centres lie in the exterior and therefore in
the spanning carrier bags.  Their fifteen operation signatures do not by
themselves say that four centres occupy four distinct bags, nor do their
colourings furnish a movable connected subgraph.  Deleting all four before
applying the rooted-kernel theorem would leave only a one-connectivity
guarantee.  The exact remaining statement is consequently the
response-sensitive branch-set split recorded in Section 7, not an exterior
component capture.

## 8. Hashes

```text
679c340cafd0b27bf16ddfcf7829dde2ab73d0403df3c41603ec9a2a5e4e1dd5  active/hc7_k7minus_dominated_degree_eight_rooted_seven_carrier.md
79fb33eacad3591c6f89c0bf1758475287feb462999927241daf8a83a3961927  active/experiments/dominated_singleton_rooted_seven_carrier/verify.py
7f062d12451b751d71789144b85bf09ff5a2ee29306702385eb4e0416c4e6cc2  active/experiments/dominated_singleton_rooted_seven_carrier/README.md
ab9df3d879e53784f8afcc77dfc7f37137a5e1a370caee95df01fc905b00cfb7  active/experiments/dominated_singleton_complete_seven_terminal_kernel/verify.py
53eebed6d60ddef759c0fca021c4c9b2955752b7e4510aae930474edd4b36fab  active/experiments/dominated_singleton_complete_seven_terminal_kernel/README.md
```
