# Rooted carriers at a dominated degree-eight centre

**Status:** active written reduction containing four computer-assisted finite
results; [cold internal audit GREEN](hc7_k7minus_dominated_degree_eight_rooted_seven_carrier_audit_cold.md).
The unbounded lifts are written proofs.  This closes two of the five
connected common-neighbour types, but does not close the dominated-centre
case, the eight-coordinate case, or `HC_7`.

Let `u` be a degree-eight vertex and let `v` be adjacent to every member of

\[
                         Q=N_G(u)-\{v\}.                 \tag{0.1}
\]

In the connected dominated-centre residue, `|Q|=7` and

\[
 \alpha(Q)=3,\qquad Q\text{ is triangle-free},\qquad
 K_5^-\npreccurlyeq Q.                                  \tag{0.2}
\]

Moreover `H=G-\{u,v\}` is five-connected.  The universal seven-terminal
theorem gives a `Q`-rooted `C_7` or `K_{3,4}` minor model in `H`.  The
`K_{3,4}` outcome is always terminal.  A second use of terminal-rooted
minors, after deleting the two unused roots, eliminates the theta graph and
the chorded seven-cycle.  Only three common-neighbour graphs remain.

The exact dominated-centre separation has order eight: its apparent
order-seven alternative has the edge `uv` as one component, and is excluded
by the audited theorem that a full order-seven cut has no forest component.

## 1. Rooted quotient composition

### Lemma 1.1 (rooted quotient lift)

Let `(B_q:q\in Q)` be pairwise disjoint connected branch sets in a graph
`J`, with `q\in B_q`.  Suppose their adjacency graph contains a graph `F`
on the labelled vertex set `Q`.  If `Q\cup F` contains a `K_5^-` minor,
then `J` has a `K_5^-` model every branch set of which meets `Q`.

#### Proof

Every edge of `F` is an actual adjacency between the corresponding branch
sets.  A literal edge `qr` of `Q` is also an adjacency between `B_q` and
`B_r`, through the vertices `q` and `r`.  Thus the adjacency graph of the
seven branch sets contains `Q\cup F`.

For every branch set of a `K_5^-` model in this quotient, take the union of
the `B_q` indexed by its vertices.  These five unions are connected,
disjoint, have all required adjacencies, and each contains a vertex of
`Q`. `\square`

If this conclusion holds in `H`, the singleton branch sets `\{u\},\{v\}`
extend it to a `K_7^-` model in `G`: they are adjacent to each other and to
every branch set meeting `Q`.

## 2. Exact finite carrier lemmas

The deterministic verifier
[`verify.py`](experiments/dominated_singleton_rooted_seven_carrier/verify.py)
uses the audited nine-graph classification and exact deletion/contraction
minor routine from the dominated-degree-eight experiment.

### Lemma 2.1 (seven-terminal carriers)

For each of the nine eligible graphs `Q`:

1. `Q\cup F` has a `K_5^-` minor for every labelled spanning
   `F\cong K_{3,4}`;
2. this is false for a spanning `C_7`.

Across all `9\binom73=315` bicliques there is no survivor.  Across all
`9(7!/14)=3240` cycles there are 456 survivors, forming 125 orbits under
the automorphism group of the fixed graph `Q`.

#### Computer-assisted proof

The verifier independently generates the 35 labelled bicliques and 360
undirected labelled seven-cycles.  It checks every union by exact minor
search and asserts the totals and orbit count. `\square`

### Lemma 2.2 (two robust five-root fans)

Write `F_5=K_1\vee P_4`.  If `Q` is either

1. the theta graph whose three internally disjoint paths have lengths
   `2,3,3`; or
2. a seven-cycle with one chord whose two resulting cycles have orders four
   and five,

then `Q` has a five-set `R` such that

\[
             Q\cup F\text{ contains a }K_5^-\text{ minor}       \tag{2.1}
\]

for every labelled copy `F\cong F_5` on `R`.

No such five-set exists when `Q` is `C_5\mathbin{\dot\cup}K_2`, a
five-cycle with a pendant path of length two at one cycle vertex, or
`C_7`.

#### Computer-assisted proof

For each of the 21 five-subsets of every eligible `Q`, the verifier
generates all 60 labelled copies of `F_5` and tests (2.1).  In its canonical
graph6 labelling the two positive five-sets are

```text
FCR`o : {0,1,2,3,4}
FCpb_ : {0,2,3,4,5}.
```

The first code is the theta graph and the second is the chorded
seven-cycle.  Isomorphisms transport these certificates to any labelling.
The three negative graph types have zero robust five-sets. `\square`

## 3. The unbounded host reduction

### Theorem 3.1 (the biclique outcome is impossible)

In the setting above, the universal seven-terminal theorem applied to
`H` cannot return a `Q`-rooted `K_{3,4}` model.

#### Proof

Such a model, Lemmas 2.1 and 1.1, and the two singleton branch sets
`\{u\},\{v\}` would give a `K_7^-` model in `G`. `\square`

### Theorem 3.2 (five-root deletion eliminates two common-neighbour types)

In a `K_7^-`-minor-free host, `Q` is neither the theta graph of Lemma 2.2
nor the chorded seven-cycle of that lemma.

#### Proof

Let `R` be the robust five-set from Lemma 2.2 and put `D=Q-R`, so
`|D|=2`.  Since `H` is five-connected, `H-D` is three-connected: a cut of
order at most two in `H-D`, together with `D`, would be a cut of order at
most four in `H`.

Apply the audited universal five-terminal theorem to the five vertices of
`R` in `H-D`.  It returns an `R`-rooted `F_5` model; its labelling is not
prescribed.  Add the two singleton branch sets indexed by `D`.  The seven
branch sets are disjoint and their adjacency graph contains `Q\cup F`,
where `F` is the returned labelled copy of `F_5`.  Robustness of `R` and
Lemma 1.1 give a `Q`-meeting `K_5^-` model in `H`.  Adding `\{u\},\{v\}`
gives a `K_7^-` model in `G`, a contradiction. `\square`

The deletion of the two unused roots is essential.  Without it they could
lie inside the five rooted branch sets, and treating them as two further
singleton bags would be invalid.

### Corollary 3.3 (three connected dominated types remain)

In the target-free connected dominated degree-eight state,

\[
 Q\cong C_5\mathbin{\dot\cup}K_2,
 \quad C_5\text{ with an attached pendant path of length two},
 \quad\text{or}\quad C_7.                               \tag{3.1}
\]

Furthermore `H` has a `Q`-rooted seven-cycle model.  For these three
graphs, static union with a labelled carrier cycle has 326 target-free
placements, in 64 fixed-`Q` automorphism orbits.

#### Proof

The connected-exterior classification leaves five graph types.  Theorem
3.2 eliminates two, and Theorem 3.1 eliminates the biclique outcome of the
universal seven-terminal theorem.  The final counts are the corresponding
subtotals in the verifier. `\square`

This is an unbounded host conclusion: only the quotient calculation is
finite.  The seven rooted branch sets may have arbitrary order.

### Corollary 3.4 (the connected interface has order eight)

Let `C=G-N_G[u]` and `T=N_G(C)` be the exact separation supplied by the
connected-exterior theorem.  Then

\[
                            T=N_G(u)=\{v\}\cup Q,
                            \qquad |T|=8.                \tag{3.2}
\]

Thus `G-T` has precisely the singleton component `\{u\}` and the connected
component `C`.

#### Proof

If `|T|=7`, the exact-interface theorem gives the other component as the
edge `\{u,v\}`.  Its induced graph is a tree.  This is a forest component
behind a full order-seven cut, contrary to the audited forest-shore
exclusion theorem.  Hence `|T|=8`; the exact-interface description then
gives `T=N_G(u)` and singleton side `\{u\}`. `\square`

## 4. A terminal two-augmentation theorem

### Theorem 4.1 (two connected augmentations of a rooted cycle)

Let `(B_0,\ldots,B_6)` be a `Q`-rooted seven-cycle model in `H`, indexed
cyclically.  Suppose there are two disjoint connected sets `P_0,P_1`,
disjoint from all seven branch sets, such that each `P_j` has a neighbour
in every `B_i`.  Then `G` contains a `K_7^-` minor.

#### Proof

Enlarge `B_0` by `P_0` and `B_1` by `P_1`.  These enlarged branch sets are
connected and disjoint.  Each is adjacent to every other cycle branch set,
and they remain adjacent to one another through the original
`B_0B_1` cycle adjacency.  The five unchanged sets

\[
                         B_2,B_3,B_4,B_5,B_6
\]

contain a path in this order.  The seven branch sets therefore have
adjacency graph containing `K_2\vee P_5`.  The two universal vertices and
any three consecutive path vertices induce a `K_5^-`.  Each of those five
branch sets meets `Q`, so adjoining `\{u\},\{v\}` gives a `K_7^-` model in
`G`. `\square`

The two augmenting sets need not be adjacent.  One is not enough: it
creates only one universal quotient branch set.

## 5. Complete kernel catalogue and the four-bag repair

The coarse cycle-or-biclique theorem discards valid rooted adjacencies.
The audited exact seven-terminal irreducible-kernel theorem retains them.
Its catalogue has two branches:

1. every one of the 5,495 labelled edge-minimal three-connected graphs on
   the seven roots; and
2. every one of the 30,600 labelled order-eight irreducible templates,
   where, for each template, any neighbour of the extra vertex may absorb
   it and act as owner.

The deterministic verifier
[`verify.py`](experiments/dominated_singleton_complete_seven_terminal_kernel/verify.py)
checks this exact universal/existential catalogue against the three graphs
in (3.1).

### Proposition 5.1 (exact complete-kernel residue)

Static composition with the complete catalogue has precisely the following
residue.

1. In the order-seven branch there are 21 failed labelled compositions,
   forming four fixed-`Q` automorphism orbits.  In every one, the carrier is
   a six-wheel: its degree sequence is `6,3,3,3,3,3,3`.
2. In the order-eight branch there are 89 failed labelled templates,
   forming thirteen fixed-`Q` automorphism orbits.  Every survivor is a
   wheel or one-chord template.  No two-chord template survives.

#### Computer-assisted proof

The verifier independently regenerates the 5,495 order-seven carriers and
the three exact order-eight families.  It checks every order-seven union.
For each order-eight template it checks every legal owner and records a
failure only when no owner closes.  Assertions enforce the catalogue sizes,
counts, orbit counts and structural profiles. `\square`

### Proposition 5.2 (any four-bag connected augmentation closes)

For every quotient in Proposition 5.1 and every prescribed four-subset of
its seven rooted bags, adding a connected set which meets those four bags
closes the quotient after absorbing it into a suitable contacted owner.

In the order-eight branch, the original extra vertex and the new connected
set may be absorbed at two distinct owners.  For every template and every
four-subset, some such pair of owners gives a `K_5^-` minor in the
seven-bag quotient.

#### Computer-assisted proof

The order-seven check covers `21\binom74=735` combinations and the
order-eight check covers `89\binom74=3115`.  For each combination the
verifier adds the star from every legal contacted owner and tests the exact
minor conclusion.  In the order-eight branch it first ranges over every
legal owner of the kernel's extra vertex and requires the augmentation
owner to be distinct.  There is no failure. `\square`

The host lift in Proposition 5.2 is conditional but literal: if a connected
set `P`, disjoint from the seven carrier bags, meets four named bags, unite
`P` with the selected contacted owner bag.  The inserted quotient star is
then made of actual branch-set adjacencies.  What remains unproved is the
supply of such a movable set or an equivalent split inside one carrier bag.

### Corollary 5.3 (spanning residual normal form)

In the target-free host, `H` has a **spanning** `Q`-rooted seven-bag model
whose quotient belongs to the residue in Proposition 5.1.  More precisely:

1. an order-seven terminal kernel yields one of the 21 six-wheel
   compositions; or
2. an order-eight terminal kernel yields one of the 89 wheel or one-chord
   templates, with its extra bag absorbed at a legal owner.

Consequently every vertex of `H`, including each of the four other
degree-eight centres, lies in exactly one of these seven rooted bags.

#### Proof

Terminal-legal contraction partitions all vertices of `H` into the branch
sets of the lifted irreducible kernel, so the lifted model is spanning.  If
the kernel has order seven, delete carrier edges while retaining
three-connectivity.  The resulting minimal carrier is one of the 5,495
catalogued graphs.  Any composition outside the 21 failures gives the
forbidden minor by Proposition 5.1 and Lemma 1.1.

If the kernel has order eight, its extra branch set may be absorbed into
the bag of every legal owner.  Were the union of `Q` with some owner
quotient to contain `K_5^-`, the same lift would give the forbidden minor.
Hence the exact template is one of
the 89 failures recorded in Proposition 5.1.  Owner absorption preserves
the union of all branch sets, so the resulting seven bags still span `H`.
The final assertion follows because all four other centres belong to
`H`. `\square`

The spanning conclusion changes the interpretation of Proposition 5.2.
For this canonical kernel lift there is no component outside the model to
serve as the augmenting set.  The finite proposition instead identifies
the precise quotient improvement that a split of one existing branch set
must produce.

Call a connected set `P\subseteq B_s` **movable from `B_s` to `B_o`** if
`s\ne o`, the set `B_s-P` is connected and contains its root, every
carrier adjacency incident with `B_s` is still represented after deleting
`P`, and `P` has a neighbour in `B_o`.  Moving `P` means replacing

\[
             B_s,B_o\quad\hbox{by}\quad B_s-P,\ B_o\cup P.      \tag{5.1}
\]

If, after this split, `P` meets four distinct rooted bags including `B_o`,
then (5.1) realises exactly the four-contact star tested in Proposition
5.2.  In the order-eight case the owner of the kernel's extra bag must be
chosen compatibly with the distinct owner guaranteed by that proposition.
Thus such a movable split is terminal.

## 6. Hostile augmentation checks

The first verifier records the exact limits of the obvious one-object
repairs, restricted to the five graph types before Theorem 3.2.

1. Among the 402 target-free cycle placements, the minimum number of
   arbitrary missing quotient edges needed to force `K_5^-` is distributed
   as

   \[
                  1:334,\qquad2:54,\qquad3:13,\qquad4:1.        \tag{6.1}
   \]

   The unique four-edge placement is `Q=C_7` with an edge-disjoint carrier
   cycle, whose union is the complement of a seven-cycle.
2. Model one connected set meeting a chosen collection of at least five
   cycle bags by absorbing it into any contacted owner bag.  Of 11,658
   placements, 666 remain target-free.  Fourteen remain even when the set
   meets all seven bags.
3. Even the stronger aligned operation of making four existing cycle bags
   a clique has 701 failures among 14,070 placements.  There is one
   placement—the complement-of-`C_7` placement above—for which none of the
   35 four-subsets closes.
4. Every proper partition of `Q` into five nonempty independent blocks was
   also tested.  The three graphs in (3.1) have no robust five-set at all,
   so choosing a rainbow transversal of a saturated five-colouring cannot
   make the black-box rooted-`F_5` theorem terminal there.

These are barriers to the displayed quotient implications, not host
counterexamples.  In particular, an independently obtained rooted `K_4`
need not use unions of the seven fixed cycle bags, and the four-coordinate
response colourings do not identify their colour classes with those bags.

## 7. Exact remaining inference

The live state now has all of the following on one graph:

* one of the three common-neighbour graphs in (3.1);
* a spanning complete seven-terminal irreducible-kernel model in the
  five-connected graph `H`, reduced to the wheel/one-chord residue of
  Proposition 5.1;
* the canonical response on the exterior shore; and
* all fifteen nonempty signatures on the other four five-centre matching
  edges on the opposite shore of the same exact order-eight separation.

The response family cannot close by a common boundary partition: the two
shore languages have disjoint block counts.  Nor does five-connectivity
itself supply Proposition 5.2.  Corollary 5.3 makes the selected carrier
model spanning, so no component of `H-\bigcup_iB_i` exists.  Before the
model is made spanning, five-connectivity would give at least five
**vertices** in the boundary of such a component, but those vertices could
lie in fewer than four carrier bags.

The four other centres do not repair this automatically.  They are
vertices inside the seven spanning bags, possibly several in one bag.  The
fifteen opposite operation signatures supply proper colourings, but no
theorem currently turns one of those labelled vertices or its Kempe
subgraphs into a set movable in the sense of (5.1).  Deleting the four
centres before choosing the rooted carrier is also unavailable: it would
reduce the guaranteed connectivity of `H` from five to only one.

The first unsupported inference is therefore

\[
 \begin{gathered}
  \text{the spanning residual kernel model and the four-coordinate}\
  \text{opposite response family}
 \end{gathered}
 \Longrightarrow
 \begin{gathered}
  \text{one response-labelled movable branch-set piece meeting four bags, or a}\
  Q\text{-rooted }K_5^-\text{ model}.
 \end{gathered}                                         \tag{7.1}
\]

The smallest repair is therefore a **four-bag response-sensitive split
theorem**: one of the four labelled operations must either split a rooted
wheel/one-chord bag into a movable piece meeting four bags, while the source
remainder retains its root and carrier adjacencies, or directly give a
`Q`-rooted `K_5^-` model.  Proposition 5.2 then gives the forbidden minor.
An exterior four-bag augmentation is a sufficient diagnostic, but it is not
the canonical host object because the kernel lift is spanning.  The complete
catalogue shows that no stronger generic rooted-carrier theorem is needed;
the remaining issue is an unbounded, response-labelled branch-set split.

## Dependencies and scope

- [connected dominated exterior and four-coordinate response interface](hc7_k7minus_dominated_degree_eight_exterior_connectivity.md);
- [saturated five-root reduction](hc7_k7minus_dominated_singleton_rooted_five_reduction.md);
- [universal seven-terminal cycle-or-biclique theorem](../results/hc7_seven_terminal_rooted_cycle_or_biclique.md);
- [universal five-terminal rooted-fan theorem](../results/hc7_five_terminal_rooted_fan.md);
- [full order-seven forest-shore exclusion](../results/hc7_k7minus_forest_shore_four_colour_extension.md);
- [complete seven-terminal irreducible kernels](../results/hc7_seven_terminal_irreducible_kernel_classification.md); and
- the two retained finite verifiers adjacent to this note.

The five-centre matching coordinates in the response interface are not the
eight edges of the separate induced-forest construction.  No identification
between those two coordinate systems is made here.
