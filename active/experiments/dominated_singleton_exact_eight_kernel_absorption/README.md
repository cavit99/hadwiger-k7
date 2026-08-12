# Exact eight-terminal kernel absorption and residue classification

This probe retains the complete exact eight-terminal terminal-kernel bundle
for the roots `Q` together with one further exceptional centre.  After the
kernel's nonterminal bags are assigned to legal owners, the centre-rooted
bag is absorbed into a neighbouring `Q`-rooted bag.  The seven resulting
bags all meet `Q`.

The default run screens the 196,976 labelled order-eight terminal quotients.
Pass `--all` to include the 2,408,280 order-nine owner families and the 5,040
order-ten owner-pair families.  `classify.py` then classifies the order-eight
and order-nine failures under the automorphism group of the fixed labelled
graph `Q`.

This remains a finite discovery diagnostic.  Promotion would require the
exact catalogue's stated audit boundary and an independent composition
verifier.

Observed output:

```text
order8_total_failures 425
FCQ`_ order8_extra_root_edge_forcing [(0, 30), (2, 80), (3, 40), (4, 60)]
FCQb_ order8_extra_root_edge_forcing [(0, 6), (2, 24), (3, 18), (4, 26)]
FCp`_ order8_extra_root_edge_forcing [(0, 15), (1, 28), (2, 35), (3, 14), (4, 49)]
order9_total_failures 803
order10_total_failures 0
```

Thus the exact two-nonterminal `C8/AABBAABB` branch always closes after the
additional centre root is absorbed.  The order-eight and order-nine kernel
branches still have small labelled residues.  The order-nine catalogue and
the present composition have not received an independent audit, so these
counts are a route diagnostic, not a promoted computer-assisted theorem.

## Fixed-`Q` orbit counts

The 425 order-eight failures form 66 fixed-`Q` automorphism orbits.  The 803
order-nine failures form 88 such orbits.

```text
Q                              order 8       orbits       order 9       orbits
C5 disjoint union K2              210            15           430            23
C5 with a pendant P2               74            37            86            43
C7                                141            14           287            22
total                             425            66           803            88
```

## The order-eight core after one idealised new centre contact

For each order-eight failure the classifier adds, in turn, every absent edge
from the protected centre root `w` to a `Q`-rooted bag.  This deliberately
grants the strongest uncoloured quotient effect of reselecting the matching
edge at `w`.  Fifty-one labelled quotients, in nine fixed-`Q` orbits, resist
every such addition.

Write `theta(a,b,c)` for the graph consisting of three internally disjoint
paths of lengths `a,b,c` with common ends.  Every resistant quotient has one
of the following four unlabelled forms:

1. `w` joined to every vertex of a seven-cycle;
2. `w` joined to the five degree-two vertices of `theta(1,2,5)`;
3. `w` joined to the five degree-two vertices of `theta(1,3,4)`; or
4. `w` joined to the five degree-two vertices of `theta(2,3,3)`.

Their labelled distribution is exact:

```text
Q                         theta125   theta134   theta233   wheel(C7)
C5 disjoint union K2              0         10         10          10
C5 with a pendant P2              0          2          2           2
C7                                7          7          0           1
```

The theta quotients have 13 edges and degree sequence

```text
(3,3,3,3,3,3,3,5),
```

with `d(w)=5`; the wheel has 14 edges and degree sequence

```text
(3,3,3,3,3,3,3,7).
```

Thus the exact protected-root noncontact count is two in every theta case
and zero in every wheel case.  After the literal edges of `Q` are added,
there are 13 missing pairs of `Q`-rooted bags in every theta case and in the
two non-`C7` wheel cases, and 14 in the `C7` wheel.

The missing-pair test is also sharp.  For the first two choices of `Q`, every
single new contact between `Q`-rooted bags closes the composition.  For
`Q=C7`, this remains true for `theta(1,3,4)` and for eleven of the thirteen
missing contacts of `theta(1,2,5)`.  The `C7` wheel survives every one new
contact, but every pair of new contacts closes it.  The two exceptional
contacts in `theta(1,2,5)` do not close even when both are added.

## Exact order-nine normal form of the failed compositions

Every one of the 803 order-nine owner families has the following common
structure in its exact nine-vertex kernel `K`, with unique nonterminal `x`:

```text
d_K(w)=3,
wx is an edge,
and w has exactly two neighbours in Q.
```

Moreover `d_K(x)` is 6, 7 or 8, so the owner-family sizes are exactly 6, 7
or 8.  Only four kernel degree sequences occur:

```text
degree sequence                    count
(3,3,3,3,3,3,3,3,6)                 185
(3,3,3,3,3,3,3,4,7)                 356
(3,3,3,3,3,3,3,3,8)                  91
(3,3,3,3,3,3,4,4,8)                 171
```

The corresponding edge counts are 15, 16 and 17, with multiplicities 185,
447 and 171.  Across every legal owner choice, the protected root can meet
five, six or seven `Q`-rooted bags.  The number of `Q` roots it can never
meet is therefore two, one or zero; these occur respectively 57, 370 and
376 times.  The classifier also emits the exact profile of universally
missing pairs between `Q`-rooted bags.

Most importantly, every order-nine failed family has a nonempty forcing set
of possible new `w`-to-`Q` contacts.  For the two `C5`-based graphs its order
is always five.  For `Q=C7` it has order three, four or five, occurring 49,
42 and 196 times.  Once the new contact is fixed in that set, a legal owner
of `x` can be chosen so that the rooted quotient contains a `K5` minus one
edge minor after the protected bag is absorbed.

## What the matching response does and does not supply

The selected matching edge at `w` is already represented by the exact
branch-set quotient whenever its ends lie in different bags.  The complete
endpoint-equality response square is additional colouring information; by
itself it does not create a new interbag contact.

Consequently the order-nine diagnostic closes that branch only under a
genuine placement statement: the matching representative must be selectable
in one of the forcing rooted bags.  The order-eight diagnostic is a stronger
negative test: 51 quotients survive even after an arbitrary single new
`w`-to-`Q` contact is granted.  Thirteen of them are wheels in which `w`
already meets all seven `Q` bags.

Thus full response-square information does not eliminate the residue at the
uncoloured quotient level.  A host theorem must use the response trace to
split or reroute a branch bag.  The finite classification reduces that host
problem to the four order-eight forms above, or, in order nine, to forcing
the selected matching representative into one of at least three explicitly
identified rooted bags.

## A second protected centre

`second_centre.py` tests the four resistant order-eight forms against a
second protected centre in two ways.

First, suppose two resistant quotients, one rooted at each protected centre,
are realised on the same seven `Q`-rooted bags.  Their union always contains
a `Q`-rooted `K5` minus one edge minor:

```text
Q                         ordered pairs tested   failures
C5 disjoint union K2                       900          0
C5 with a pendant P2                        36          0
C7                                         225          0
```

This is a genuine terminal finite composition, but the common-bag hypothesis
is not yet supplied by the host theory.  Two separately existential rooted
models cannot be identified without an alignment argument.

Second, keep one resistant quotient and add one further centre-bearing
connected set adjacent to a prescribed subset of the seven `Q`-rooted bags.
Four contacts always suffice.  Three suffice in every case except
`Q=C7` with the `theta(1,2,5)` or wheel quotient.  A single contact never
suffices.  The exact failed-subset counts for one representative of each
fixed-`Q` orbit are emitted by the verifier.

This places a precise demand on the full matching response.  Its one physical
matching edge supplies only one contact, so the endpoint-equality square must
be used to produce either:

* a centre-bearing response subgraph adjacent to four `Q`-rooted bags; or
* a second resistant rooted model whose seven `Q` bags align with the first.

Either output is terminal by the finite screen.  Merely retaining the second
edge and its three nonempty equality signatures is not.

## The exact two-contact relation in the all-terminal order-nine case

The separate all-terminal order-nine catalogue protects `Q` and two centres.
For every static failed composition, `two_coordinate_contacts.py` records the
relation

```text
F subset Q times Q,
```

where `(q,r)` belongs to `F` precisely when adding a contact from the first
centre to the `q` bag and from the second centre to the `r` bag closes the
rooted composition.  Its complement is the exact nonforcing relation.  For
a set of `a` rows, the largest possible common set of nonforcing columns,
maximised over the whole catalogue, is:

```text
Q                              a=1  2  3  4  5  6  7
C5 disjoint union K2             7  7  6  5  5  3  0
C5 with a pendant P2             7  7  6  5  5  3  0
C7                               7  7  7  7  4  3  0
```

It follows, conditionally on two sets of candidates occupying five distinct
named `Q` bags each, that the `C7` case closes.  This conclusion is not a bag
spread theorem: the five matching candidates may occupy fewer than five
bags, and may remain in a centre-rooted bag.

The two `C5`-based cases have exact `5 by 5` exceptions.  There are four
labelled records in three fixed-`Q` orbits for `C5` disjoint union `K2`, and
eight labelled records in five fixed-`Q` orbits for the pendant case.  Every
bad rectangle has the same structural form, up to exchanging the centres:

* one five-set omits an edge of the distinguished `C5`; and
* the other omits the two vertices outside that `C5`--the isolated `K2`, or
  the pendant `P2`.

Thus the two induced five-vertex graphs are respectively `P3` disjoint union
`K2` and `C5` in the first case, and `P5` and `C5` in the second.  In all
twelve labelled records the two protected centres are nonadjacent in the
carrier, have carrier degree three or four, and every existing `Q` contact
of a centre lies in its corresponding bad five-set.

The forcing-relation digests are:

```text
C5 disjoint union K2
f93d64db04c268ecef99a59f55bf8a7ccb32a9440451a9213ccd01b90b748e2d

C5 with a pendant P2
ec1eca861ac3481fd7939030ceecaa9f252dafceb3ed4e919dad863e78d5ed55

C7
24846426af0f01174b836dec4630b779f4b61a2d1a671e972deacda596b9bd86
```

## Matching-candidate feasibility of the exceptional five-sets

The bad rectangles are not removed by the local degree-eight neighbourhood
conditions.  Fix an independent triple `I` in an eight-vertex neighbourhood
and put `R=N(w)-I`.  After fixing `C5`, `P3` disjoint union `K2`, or `P5` on
`R`, `candidate_set_gate.py` enumerates all `2^15` choices of edges between
`I` and `R`.  It retains independence number three, no `K4` subgraph and no
`K6` minus one edge minor.  The exact surviving counts are:

```text
G[R]             R selectable as N(w)-I     R exactly N(w)-K_w
C5                                  12363                    315
P3 disjoint K2                        8904                      0
P5                                   10296                      0
```

Here `K_w` is the intersection of all independent triples in `N(w)`.  The
zeroes in the final column are elementary: if `|N(w)-K_w|=5`, then `K_w` is
the unique independent triple, so the remaining five vertices cannot
contain an independent triple.  The `C5` case really can occur; the verifier
retains connected witnesses of minimum degree four with no `K6^-` minor.

This test gives a sharp limitation.  If the five candidates were the five
literal vertices of `Q` and equalled `N(w)-K_w`, one side of every bad
rectangle would be impossible.  In a rooted minor model, however, arbitrary
candidate vertices in five branch bags need not inherit the edges of `Q`,
and several candidates may occupy one bag.  Consequently this observation
does not eliminate the host residue.  The missing statement remains a
response-preserving bag-spread or common-model theorem.

## A swallowed matching mate: exact rooted-suffix transfer

`swallowed_mate_split.py` tests a more faithful branch-bag operation.  Let a
protected-root bag contain its selected matching mate.  Split off a rooted
suffix which owns a set `O` of at least two adjacencies of the source bag,
and absorb the suffix into an owned `Q` bag `q`.  The exact quotient operation
is:

* delete the source-root edges to `O`;
* retain every nonowned source edge;
* add the edges from `q` to `O-{q}`; and
* restore the source-root edge to `q` through the matching edge joining the
  root part to the suffix.

The screen tests every ownership set contained in the actual carrier
neighbourhood of the selected protected root.  It also separately restricts
ownership to `Q` neighbours.  Even with an existential choice of centre,
ownership set and absorption bag, exact failures remain:

```text
Q                              failures / static       fixed-Q orbits
C5 disjoint union K2                  256 / 427                     66
C5 with a pendant P2                 1022 / 1446                   230
C7                                    256 / 379                     66
```

Allowing the owned set also to contain the other protected centre does not
change this failure set.  More strongly, none of the 2,252 static failures
is ownership-robust: for each protected centre there is some legal ownership
set for which no owned absorption bag closes.

Every existential failure has one of the following protected-root profiles,
up to exchanging the centres:

```text
carrier degrees       Q-contact counts       centres adjacent
(3,3)                  (2,2)                  yes
(3,3)                  (3,3)                  no
(4,3)                  (3,2)                  yes
```

Only four complete carrier degree sequences occur:

```text
3^8 4,    3^8 6,    3^7 4 5,    3^8 8.
```

The result digests, first with ownership confined to `Q` and then with every
actual carrier neighbour allowed, are:

```text
Q                       Q-owned                                  all-owned
FCQ`_   bfea496351c9892147e44418decce6a3ffaa235e85f227d95fe5b0c2b7f6fb7c
        57938234e380c6a561ab45812c5831c5498129c1a20c9643e969f948ef504680
FCQb_   3c65473e3b7fec53779d35499ee50632441de5b741a983b372b68c570a56d1dc
        1d397e81648fe458cbfe6e284fac3a3c4285aa141083afd62e416b2e1356f272
FCp`_   40df88955f5cb4bdf6f08ca76c97a739b1e32b01a6bf49c495518268beddeb06
        8402f52d0ac50acde72bff01ea0a81e896c2c9b8f3abd9c68403c087f1305040
```

This is a recorded route nonclosure, not a host counterexample.  It proves
that ordinary rooted-bag minimisation plus ownership transfer is not enough.
The quotient does not encode the singleton-signature colouring of the
swallowed matching edge.  A further proof must use a bichromatic component
forced by that colouring, and must prove where a movable part of that
component lies; it cannot treat the component as a free static contact.

## Earlier one-contact summary

The original one-contact profile, retained for reproducibility, is

```text
degree sequence            protected-root degree       count
(3,3,3,3,3,3,3,5)                   5                    38
(3,3,3,3,3,3,3,7)                   7                    13
```

The degree-seven cases have no absent protected-root edge; in the degree-five
cases neither of the two absent edges closes.  These are not critical-host
counterexamples.  They do not encode the selected edge's branch-set
ownership, its bichromatic component, or its rejected boundary partition.

## Trust boundary and hashes

The order-eight and order-nine terminal catalogues are deterministic and
digest-pinned, but they have not received the independent audit required for
promotion.  Their input digests are:

```text
order-eight labelled masks
2191c87cc229cbf109b19bf66badb40c115838c5b1350709c64fd9a2ec2f020d

order-nine exact templates
7fadafedb382d766267504eee62f441f60aef0cc756aea0c453f62a4ce516dd4

order-nine owner families
5251ac96f42ec8d18d8d4db24f291f91183d031a34c31089a0d52657238c892c
```

The present classification produces these exact result digests:

```text
Q       order-eight failure / orbit / one-contact-resistant
FCQ`_   c55752fbffcd95fd56f78ed38e2d73dd6bcbe0e5afa7e35fcd9fe70fc914b075
        0b2fb43e68bba75ae35a4619384ee8bb6353d539a39da8943a61a07bdf278c74
        963d684f9ac1dd9b94ea75c098f89263ad82a7a97c432d302b141edd0b270b3f
FCQb_   81ef936d202c6e7ea94eb36a84ac70efa44e026879e0ee56e64b2e56aa07abde
        3e76341fdfa48a0a112133e4871ece9422898cab45ef135c50f23137839a5148
        b643da90e161f09f0ed2dad106db0f10a15ae0dabd5ab340124be685fbfaee33
FCp`_   e035517d80755c975ce14d9f8e2975418d4116ba5013c59e3a51d5eecfaaf151
        519c0d539ceff75de4faf5b3be8c503de2512fca9d010694319b616faf0d0b9e
        267e5503b72098fae72b53f0e67a7543bb5aa2d5a768c12deebbc2c7187d88f3

Q       order-nine failure / orbit / template / forcing-record
FCQ`_   b49748191bea4777569dbeb118b7a8ae1d026695e7b05bef672c6bf1abe94762
        95ff0d29854557f23177e7f585d602b00e64d9f1ded8355c6cdc7fa3e14ce8ef
        64d86fc63d87133f67129512faf4eda282b574fc794f9d8c560ea9f479996779
        82a12875888fe55d99b213aa8b47b960e68a081c59e63e8ba1239846ff31f068
FCQb_   1e165f2907cf6a8be7a5b23f58c3e3386e7748186b6deac1c49c7f6ee81e7cba
        264644933c634e2689d214dd05b9700834dae93681df428316b265b2751c3a24
        4dbbd1a51ad4175efee02a0325103bc6bb1d4500081aa4c942d42f0719b5c003
        31e6f31d15c4410fec6895e49647ca0ef58f17493f76e2c94296423b45a8d98c
FCp`_   765a9a7810705acc1bc08750edcaa66bbe51db48f9a5cdc17ea224cc40c44530
        0ac35dbffd26b5f80c92a12ab24ebabb067084f71827f2e7d858b12fa6bc15cd
        6cfbea37b94786830e1e9c0aad70dec68e3f8773cf664c34689172d8a11cebe9
        f1967db18fe4fb4df53be182f09a904ab3c000d55d82e23cdd02e41d0567a568
```

The checked script revisions are:

```text
probe.py          05ef17908c9d1c81aefa68ca4a2d530d8b9c9a05a5e661d21058db415a32917f
classify.py       4b5396991de5279e752091456c06f665296294d2a39bc7c5969a71299438c20f
second_centre.py  19cd57e1d9bb40d6a49645d64d3d1711a88652250614a80a2e74c61e8205c86f
two_coordinate_contacts.py
                  7c655792d1d502b61ee04c5e68660c6c9c361311a5bd9f06103aa32c4de7f1fa
candidate_set_gate.py
                  f7e2dbc661e14bc9208d65c6c0e7ad21c1bb655dbce66d853067ffcf69caa565
swallowed_mate_split.py
                  7d60de6786b9642718d83f6ba54181fe6fa8247c8bee997d95c4cecbb5a0e6bb
```

These hashes record a discovery computation; they do not turn it into an
audited computer-assisted theorem.  In particular, the common-bag and
four-contact conclusions are conditional finite compositions, not supply
theorems in the critical host.

## Reproduction

```text
python3 active/experiments/dominated_singleton_exact_eight_kernel_absorption/probe.py --all
python3 active/experiments/dominated_singleton_exact_eight_kernel_absorption/classify.py --all
python3 active/experiments/dominated_singleton_exact_eight_kernel_absorption/second_centre.py
python3 active/experiments/dominated_singleton_exact_eight_kernel_absorption/two_coordinate_contacts.py
python3 active/experiments/dominated_singleton_exact_eight_kernel_absorption/candidate_set_gate.py
python3 active/experiments/dominated_singleton_exact_eight_kernel_absorption/swallowed_mate_split.py
```

Pass `--orbits` to `classify.py` to print every fixed-`Q` orbit
representative, its multiplicity, owner-family size, protected-root contact
sets, forcing set, universal missing pairs, edge counts and exact bit masks.
