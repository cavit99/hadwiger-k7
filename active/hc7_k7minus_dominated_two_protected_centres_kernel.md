# Two protected exceptional centres eliminate the two-nonterminal kernel

**Status:** written host theorem with two computer-assisted finite
composition lemmas; internal hash-pinned audit adjacent.  The theorem
eliminates the order-eleven terminal-kernel branch of the connected
dominated degree-eight centre case.  The protected-centre fan-to-root
continuation is frozen.  This note does not eliminate the remaining
order-nine and order-ten kernels, prove Conjecture 21, or prove `HC_7`.

## 1. Host setting

Let `G` be a simple graph satisfying

\[
 \kappa(G)\geq7,
 \qquad K_7^-\npreccurlyeq G.                         \tag{1.1}
\]

Let `u` have degree eight and suppose that `v\in N_G(u)` is adjacent to
every vertex of

\[
                         Q=N_G(u)-\{v\}.              \tag{1.2}
\]

Assume that `u` belongs to a fixed independent set of five degree-eight
centres

\[
                         Z=\{u,w_1,w_2,w_3,w_4\}.     \tag{1.3}
\]

Retain the proved connected dominated-centre conclusions:

\[
 H=G-\{u,v\}\text{ is five-connected},               \tag{1.4}
\]

and

\[
 Q\cong C_5\mathbin{\dot\cup}K_2,
 \quad C_5\text{ with a pendant path of length two},
 \quad\text{or}\quad C_7.                             \tag{1.5}
\]

Choose two distinct centres `w,w'\in Z-\{u\}`.  They lie in `H-Q`, because
the five centres are independent and `N_G(u)=\{v\}\cup Q`.  Protect the
nine terminals

\[
                         T=Q\cup\{w,w'\}.             \tag{1.6}
\]

Apply terminal-legal contractions in `H` until a `T`-irreducible simple
three-connected rooted minor `K` is reached.  The audited terminal-kernel
theorem gives

\[
                         9\leq |V(K)|\leq11.          \tag{1.7}
\]

The purpose of protecting both exterior centres is to retain two literal
vertices through the same contraction process.

## 2. Exact Wu-charge structure at order eleven

Suppose that `|V(K)|=11`, and write

\[
                         V(K)-T=\{x,y\}.              \tag{2.1}
\]

For a nonterminal `s\in\{x,y\}`, let `A_s` be the set of all neighbours
of `s` which have degree three and are incident with exactly two
contractible edges.  Wu's theorem and terminal irreducibility imply that

\[
 A_x,A_y\subseteq T,
 \qquad |A_x|,|A_y|\geq4,
 \qquad A_x\cap A_y=\varnothing.                     \tag{2.2}
\]

Every `a\in A_s` has one edge to `s` and precisely two edges with both
ends in `T`.  In particular,

\[
                         d_{K[T]}(a)=2.               \tag{2.3}
\]

There are only two charge cases.

### Lemma 2.1 (charge-complete normal form)

If `A_x\cup A_y=T`, then, after interchanging `x,y` if necessary,

1. `|A_x|=4` and `|A_y|=5`;
2. `K[T]` is a nine-cycle;
3. `xy\notin E(K)`, `N_K(x)=A_x`, and `N_K(y)=A_y`; and
4. around the terminal cycle the membership runs have lengths

```text
A,A ; B,B,B ; A,A ; B,B,
```

up to cyclic reversal and rotation.

#### Proof

The disjoint charge sets have orders at least four and together contain all
nine terminals, so their orders are four and five.  Equation (2.3) makes
`K[T]` two-regular.  Deleting `x,y` from the three-connected graph `K`
leaves a connected graph, so `K[T]=C_9`.

A charged terminal has degree three and therefore cannot see the other
nonterminal.  Thus the displayed charge sets are the complete terminal
neighbourhoods of `x,y`.  If `xy` were present, `K-\{x,y\}=C_9` would be
two-connected.  The standard contraction criterion would make `xy`
contractible, contrary to terminal irreducibility.

Fix `a\in A_x`.  The graph `K-\{x,a\}` is the path `C_9-a` together with
`y`, adjacent exactly to the members of `A_y`.  A path plus an apex is
two-connected exactly when the apex sees both path ends.  Since `xa` is
not contractible, at least one cyclic neighbour of `a` lies in `A_x`.
The same argument applies to every vertex of both charge classes.  Hence
every monochromatic cyclic run has length at least two.

With four `A` vertices and five `B` vertices, either there is one run of
each class or the runs have lengths `2,2` and `2,3`.  In the first case,
deleting the two endvertices of the four-vertex `A` run separates `x` and
the two internal `A` vertices from the rest of `K`, contradicting
three-connectivity.  The second pattern is the one displayed. `\square`

### Lemma 2.2 (one-uncharged-terminal form)

If `A_x\cup A_y\ne T`, there is a unique terminal

\[
                         z\in T-(A_x\cup A_y),        \tag{2.4}
\]

and `|A_x|=|A_y|=4`.  The graph `K[T]` is a union of `r` cycles meeting
pairwise exactly in `z`, where `1\leq r\leq4`; equivalently, `K[T]-z` is a
union of `r` paths, each of order at least two, and every path end is
adjacent to `z`.  Moreover

\[
 \begin{aligned}
 N_K(x)&=A_x\cup E_x,\\
 N_K(y)&=A_y\cup E_y,
 \end{aligned}                                       \tag{2.5}
\]

where `E_x\subseteq\{z,y\}` and `E_y\subseteq\{z,x\}`.  Thus the only
undetermined edges outside the terminal bouquet are `xz,yz,xy`.

#### Proof

The two disjoint charge sets each have order at least four, and they do not
cover the nine terminals, so each has order four and (2.4) is the sole
uncharged terminal.  Every other terminal has degree two in `K[T]` by
(2.3).  The graph `K[T]=K-\{x,y\}` is connected.  The degree of `z` in
`K[T]` is positive and even by the handshaking lemma.  Removing `z` leaves
components of maximum degree two.  Connectivity rules out a cycle
component, and simplicity rules out a one-vertex path with both ends at
`z`.  Hence the components are paths of order at least two whose two ends
see `z`.  There are at most four because only eight charged terminals are
available.

A member of `A_x` already has its three incident edges, so it cannot be
adjacent to `y`; symmetrically no member of `A_y` sees `x`.  The only
additional possible terminal neighbour of either nonterminal is `z`, and
the only possible nonterminal--nonterminal edge is `xy`.  This proves
(2.5). `\square`

The second lemma is already a finite structural parameterisation.  The
exact filters of three-connectivity and noncontractibility of every edge
incident with `x` or `y`, together with the requirement that `z` is not
itself Wu-special, reduce it further to 34 canonical parameter
instances: two have `K[T]=C_9`, and thirty-two have two five-cycles
meeting only at `z`.

## 3. Finite rooted composition

### Lemma 3.1 (charge-complete composition)

For every labelled kernel satisfying Lemma 2.1, every placement of the
seven vertices of one of the three graphs in (1.5) and the two protected
centres on `T`, there are seven pairwise disjoint connected unions of
kernel vertices, one containing each vertex of `Q`, whose adjacency
quotient contains a `K_5^-` minor after the literal edges of `Q` are added.

#### Computer-assisted proof

The deterministic verifier
[`probe.py`](experiments/dominated_singleton_nine_terminal_kernel/probe.py)
generates all `20,160` labelled terminal cycles and the nine cyclic
`AABBBAABB` placements on each.  For each of the three fixed labelled
graphs `Q`, it ranges over every legal owner of `x`, every legal owner of
`y`, and every connected assignment of the two protected-centre bags to
the seven `Q`-rooted bags.  It checks the final quotient for a `K_5^-`
minor by exact deletion-and-contraction recursion.  The complete totals are

```text
patterns 9 tests 544320
failures {'FCQ`_': 0, 'FCQb_': 0, 'FCp`_': 0}
```

Assertions enforce the pattern and test counts and the absence of a failed
composition. `\square`

### Lemma 3.2 (one-uncharged-terminal composition)

The conclusion of Lemma 3.1 holds for every kernel satisfying Lemma 2.2.

#### Computer-assisted proof

The deterministic verifier
[`verify_order_eleven.py`](experiments/dominated_singleton_nine_terminal_kernel/verify_order_eleven.py)
generates all ordered partitions of the eight charged terminals into
bouquet paths, all `\binom84=70` charge assignments, and all eight choices
of the optional edges `xz,yz,xy`.  This gives `13\cdot70\cdot8=7,280`
canonical parameters before filtering.  Exact vertex-cut tests and the
contraction criterion and the exact uncharged condition retain 34
instances, with the structural profile

```text
K[T]=C9                               2
K[T]=two C5s meeting at z            32.
```

For each instance the verifier checks all `\binom92=36` placements of the
two protected centres.  On the seven remaining roots it generates every
labelled copy of each graph in (1.5): respectively 252, 2,520, and 360
copies.  It then enumerates every connected assignment of the two centre
bags and the two nonterminal bags to the seven rooted bags.  The exact
minor test reports

```text
protected_centre_placements 1224
tests {'FCQ`_': 308448, 'FCQb_': 3084480, 'FCp`_': 440640}
failures {}
```

The parameterisation is exhaustive by Lemma 2.2: ordering and orienting
the bouquet paths identifies any exact kernel with one generated instance,
and the later centre placements and labelled `Q` copies cover every
terminal labelling. `\square`

## 4. Host consequence

### Theorem 4.1 (two protected centres exclude order eleven)

Under (1.1)--(1.6), a `T`-irreducible kernel obtained from `H` cannot have
order eleven.  Consequently

\[
                         |V(K)|\in\{9,10\}.           \tag{4.1}
\]

Equivalently, one common terminal-legal contraction process can retain
`Q,w,w'` while leaving at most one nonterminal branch set.

#### Proof

Suppose `|V(K)|=11`.  Terminal-legal contractions lift the eleven vertices
of `K` to eleven pairwise disjoint connected branch sets which partition
`V(H)`, with the nine prescribed terminals in distinct bags.  Lemmas 2.1
and 2.2 exhaust the Wu-charge alternatives.  Apply Lemma 3.1 or 3.2 as
appropriate and lift its seven connected quotient bags through the
contractions.  The rooted quotient lemma gives a `K_5^-` model in `H`,
every branch set of which meets `Q`.

The singleton sets `\{u\},\{v\}` are adjacent to one another and to every
branch set meeting `Q`.  They extend the rooted `K_5^-` model to a
`K_7^-` model in `G`, contrary to (1.1).  Thus order eleven is impossible,
and (1.7) leaves (4.1). `\square`

## 5. Exact residue and scope

This theorem removes the complete two-nonterminal branch, not merely one
owner choice.  The two protected centres remain simultaneous literal roots
through the contraction process.

The all-terminal order-nine branch is not eliminated by the same static
composition.  The retained diagnostic
[`verify_order_nine.py`](experiments/dominated_singleton_nine_terminal_kernel/verify_order_nine.py)
finds target-free placements among the 57 edge-minimal three-connected
nine-vertex carriers.  The exact counts for the three graphs in (1.5) are

\[
                         427,\qquad1446,\qquad379.     \tag{5.1}
\]

There is, however, no survivor after the following deliberately generous
two-coordinate augmentation.  Give each protected centre one new edge to
an arbitrary `Q`-rooted bag, choose both contacted bags after the exact
carrier and labelled `Q` placement are known, and then repeat every
connected centre absorption.  All placements in (5.1) close; the number of
surviving fixed-`Q` orbits is zero for each graph type.

This is not yet a host theorem.  The common matching supplies each
protected centre with a literal incident representative edge, but after the
terminal-legal contractions its other endpoint may lie inside the same
centre-rooted bag.  It therefore need not give a new quotient contact with
a distinct `Q`-rooted bag.  The exact missing supply lemma in the
all-terminal branch is:

```text
the two protected centres simultaneously have usable matching-coordinate
contacts with (not necessarily prescribed) Q-rooted bags.
```

If that lemma is proved, the order-nine branch closes by the verified
calculation.

The corrected computer-assisted one-contact diagnostic has a different,
but still useful, form.  Among all 2,252 static survivors, a suitably chosen
adaptive contact
at at least one of the two named centres closes every placement.  In 1,901
placements, each named centre admits some closing contact.  In the remaining
351 exactly one centre does; these
split as

\[
                         102,\qquad204,\qquad45        \tag{5.2}
\]

over the three `Q` types.  Thus contacts at both centres always close, and
one contact closes if it is supplied at a centre selected after the rooted
quotient is known.

An earlier version of the diagnostic incorrectly reported 2,177 and 75.
Its purported one-contact helper passed `(contact,0)` or `(0,contact)` to a
two-contact routine, thereby adding a hidden contact from the other centre
to the fixed `Q` root indexed by zero.  The adjacent audit did not detect
that implementation error.  The order-eleven proof and the independently
checked order-ten result use different routines and are unaffected.

The kernel degrees of the two centre vertices do not remove this residue.
Static survivors occur with sorted degree pairs from `(3,3)` through
`(4,5)`, and with the two centre vertices both adjacent and nonadjacent.
Nor may the lifted root bags be assumed adjacent: the literal centres are
independent in `G`, and a quotient adjacency can only be created after a
bag absorbs other material.  A standard owner choice supplies neither such
an adjacency nor a `Q` contact without a literal edge leaving the
centre-rooted bag.

The order-ten branch has also been classified exactly.  If `x` is its
unique nonterminal and `J=K-x`, then `J` is two-connected.  Wu's theorem
forces at least four degree-two vertices of `J`, every one adjacent to `x`.
Every other neighbour of `x` may have higher degree in `J`.  Conversely,
enumerating every two-connected graph `J` of order nine, joining `x` to
every degree-two vertex and any subset of the others, and retaining exactly
the three-connected graphs in which no edge at `x` is contractible gives

\[
                       1153                              \tag{5.3}
\]

unlabelled rooted occurrences.  The exact degree profile of `x` is

```text
d_K(x)       4    5    6    7    8    9
occurrences 62  241  376  306  138   30.
```

The verifier
[`screen_order_ten.py`](experiments/dominated_singleton_nine_terminal_kernel/screen_order_ten.py)
checks all `1153\binom92=41,508` placements of the two centres and every
labelled `Q` copy.  Static composition leaves respectively

\[
                         840,\qquad1811,\qquad598       \tag{5.4}
\]

placements.  Allowing **one** new quotient contact from either protected
centre to an adaptively chosen `Q`-rooted bag eliminates every placement in
(5.4).  Thus order ten needs only one usable protected-centre contact.  At
order nine, two contacts always suffice; one suffices when it is supplied
at a quotient-good centre.

The independent checker
[`audit_order_ten.py`](experiments/dominated_singleton_nine_terminal_kernel/audit_order_ten.py)
does not import the discovery catalogue, composition screen or minor
routine.  It regenerates the 1,153 rooted occurrences directly from the
`geng` stream, obtains the pinned digest

```text
b4b188d11db1d2c7047e8d92e479e0f8c0e937a48e7c47caf1b88a2ed4975702
```

and checks the one-contact conclusion by connected five-bag partitions.
It reports no failure for any of the three graphs on `Q`.

These contact statements remain conditional finite composition theorems.
They do not by themselves prove that a selected matching representative
edge leaves its centre-rooted kernel bag.  Hence no unconditional conclusion
beyond (4.1) is presently claimed.

The finite terminal-kernel composition calculations are now complete.  The
exact remaining
host problem is to supply contacts at both centres, or to identify from the
host which one centre is closing after the quotient is known, or to turn
swallowing directly into a response-labelled bag split.  A single usable
contact closes every order-ten kernel.  At order nine, contacts at both
centres close every placement, while one contact closes every placement
only when the quotient-good centre may be selected adaptively.  A bare
static carrier theorem is known to be insufficient in the order-nine
branch.

Two different swallowed-coordinate diagnostics must not be conflated.  A
generous screen which retains every old source-bag adjacency and merely adds
the star of a suffix with at least two contacts eliminates every order-nine
survivor.  The exact rooted-suffix transfer instead deletes every adjacency
owned only by the suffix before absorbing it.  That faithful operation
leaves respectively

\[
                         256,\qquad1022,\qquad256
\]

placements for the three graphs on `Q`.  Thus ordinary root-bag minimisation
and two-owner transfer do not close order nine.  What is still absent from
the quotient is the singleton-signature colouring of the swallowed matching
edge.  The exact host obligation is an **operation-labelled contact-or-split
theorem**: either a selected centre edge leaves its rooted bag in a usable
`Q`-rooted bag, or its bichromatic response supplies a movable split or an
actual labelled separation.  Static ownership alone is exhausted.

## Dependencies

- [connected dominated exterior](hc7_k7minus_dominated_degree_eight_exterior_connectivity.md);
- [three remaining common-neighbour graphs](hc7_k7minus_dominated_degree_eight_rooted_seven_carrier.md);
- [audited terminal-kernel theorem](../results/hc7_five_terminal_rooted_fan.md);
- [exact contraction criterion](hc7_eight_terminal_exact_bundle.md); and
- the two deterministic finite verifiers retained beside this theorem.
