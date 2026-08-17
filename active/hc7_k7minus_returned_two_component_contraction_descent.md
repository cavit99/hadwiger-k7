# The returned two-component six-cut: safe completion, exact contraction obstruction, and cross-shore composition

**Status:** active computation-free written proof, awaiting cold audit.  The
results are unbounded and apply to arbitrary component orders.  They do not
eliminate the returned two-component row, prove the six-connected `4n`
statement, Conjecture 21, or `HC_7`.

Write `K_7^-` for `K_7` with one edge deleted and `K_7^\vee` for `K_7`
with two incident edges deleted.  Throughout Sections 1--6, let `G` be a
six-connected `K_7^-`-minor-free graph and let `S` be a set of six vertices
such that

\[
                 G-S=A\mathbin{\dot\cup}B,             \tag{1}
\]

where `A,B` are connected and both are adjacent to every vertex of `S`.
Put

\[
 e_S=|E(G[S])|,
 \qquad
 \eta(C)=|E(G[C])|+|E_G(C,S)|-4|C|.                  \tag{2}
\]

In the returned `4n` row one also has

\[
 |E(G)|=4|V(G)|+s,\quad s\ge0,\quad e_S\le11,
 \quad
 \eta(A)+\eta(B)=24+s-e_S.                           \tag{3}
\]

## 1. Completing a closed lobe is safe for connectivity

The natural whole-shore contraction need not preserve four-connectivity.
There is, however, an exact positive statement after boundary completion.

### Lemma 1 (six-connected clique completion)

For `C in {A,B}`, let

\[
             F_C=G[C\cup S]+E(\overline{G[S]}),       \tag{4}
\]

so that `S` is made into a clique.  Then `F_C` is six-connected.

#### Proof

Let `X subseteq V(F_C)` have order at most five.  Since `|S|=6`, the
clique `S-X` is nonempty.  It suffices to show that every component `K` of
`G[C]-X` has a neighbour in `S-X`.

The set `N_G(K)` is contained in `(X cap C) union S`: distinct components
of `G[C]-X` can meet only through `X cap C`, and there are no edges from
`C` to the other component of `G-S`.  Moreover `N_G(K)` separates `K`
from that other component.  Six-connectivity therefore gives

\[
                         |N_G(K)|\ge6.
\]

At most `|X cap C|` of these neighbours lie in `C`, and at most
`|X cap S|` of the resulting boundary neighbours have been deleted.
Consequently

\[
 |N_G(K)\cap(S-X)|
 \ge 6-|X\cap C|-|X\cap S|
 =6-|X|>0.                                            \tag{5}
\]

Thus every surviving part of `C` attaches to the nonempty clique `S-X`,
and `F_C-X` is connected.  \(\square\)

### Corollary 2 (what completion does, and does not, buy)

Contract the component other than `C` to a pole `d`, and then complete
`S` to a clique.  The resulting graph is six-connected.  It contains the
literal `K_7` on `S union {d}`.

This `K_7` is not a minor certificate in the original graph.  Splitting
`d` back replaces it by one connected full component, but the model still
uses every virtual nonedge of `G[S]`.  In the returned row there are at
least four such nonedges because `e_S<=11`.  Fullness of one connected
component does not supply six disjoint rooted bags which realise those
boundary edges.  Thus full boundary completion proves internal
connectivity but, by itself, destroys the lifting information.

#### Proof

The connectivity proof is the proof of Lemma 1 with the surviving pole
also joined to every vertex of `S-X`; if the pole is deleted, Lemma 1
applies verbatim.  The remaining assertions follow directly from the
construction.  \(\square\)

This is the first exact obstruction to the tempting route

```text
complete S -> apply an unrooted dense-minor theorem -> split the pole.
```

Any successful use of completion must control the virtual boundary edges
used by the returned model.  A star of virtual edges can be lifted by
absorbing a connected subgraph of the opposite component into its centre
bag.  Fullness alone does not lift an arbitrary set: if the full component
is a singleton, its only vertex can belong to at most one root bag and
cannot create a contact between two other root bags.

## 2. Exact connectivity of an uncompleted whole-shore contraction

Fix `C in {A,B}`, let `D` be the other component, and let `H_C=G/D`, with
`D` contracted to a vertex `d`.  Put `J_C=G[C union S]`.

### Lemma 3 (exact cut test)

Every vertex cut of `H_C` of order at most three contains `d`.  Moreover,

\[
 H_C\text{ is four-connected}
 \quad\Longleftrightarrow\quad
 J_C-Z\text{ is connected for every }|Z|\le2.        \tag{6}
\]

More generally, `H_C` is five-connected if and only if `J_C-Z` is
connected for every `|Z|<=3`.

#### Proof

Let `X` be a cut of `H_C` with `|X|<=4`.  If `d notin X`, the component
of `H_C-X` containing `d` contains every surviving vertex of `S`, since
`d` is complete to `S`.  Splitting `d` back into the connected set `D`
cannot join any other component: there are no `C-D` edges.  Hence `X`
would also separate `G`, contrary to six-connectivity.  Thus every such
cut contains `d`.

For `X={d} union Z`, one has the literal identity

\[
                         H_C-X=J_C-Z.                 \tag{7}
\]

Taking `|X|<=3` and `|X|<=4`, respectively, proves both equivalences.
\(\square\)

The lemma corrects an unsafe inference: six-connectivity and fullness do
**not** make `H_C` automatically four- or five-connected.

### Lemma 4 (the complete obstruction to four-connectivity)

Suppose `H_C` is not four-connected.  Then there is a set
`Z subseteq C union S`, `|Z|<=2`, for which one of the following holds.

1. `C subseteq Z`; in particular `|C|<=2`.
2. There is a nonempty connected set

   \[
                        R\subseteq S-Z               \tag{8}
   \]

   with `|R|<=|Z cap C|<=2` such that

   \[
   N_C(R)\subseteq Z\cap C,
   \qquad
   N_{G[S]}(R)-R\subseteq Z\cap S,
   \qquad
   |N_D(R)|\ge6-|Z|.                                 \tag{9}
   \]

In the second outcome, if `|Z|=1`, then `Z={z} subseteq C`,
`R={r}`, `N_C(r)={z}`, `r` has no neighbour in `S-{r}`, and
`|N_D(r)|>=5`.  If `|Z|=2`, the atom `R` is a singleton or an edge and
has at least four distinct neighbours in `D`.

#### Proof

By Lemma 3, choose `Z` with `|Z|<=2` such that `J_C-Z` is disconnected.
If `C-Z` is empty, outcome 1 holds.  Assume otherwise.

Let `K` be a component of `G[C]-Z`.  As in (5), `N_G(K)` separates `K`
from `D` and is contained in `(Z cap C) union S`.  Hence `K` has at least

\[
                       6-|Z|                          \tag{10}
\]

neighbours in `S-Z`.  It follows that every component of `J_C-Z`
which contains a vertex of `C-Z` contains at least `6-|Z|` surviving
boundary vertices.  Two such components would require at least eight
boundary vertices, so there is exactly one; call it `Q`.

Every other component of `J_C-Z` is contained in `S-Z`.  The total number
of surviving boundary vertices outside `Q` is at most

\[
 |S-Z|- (6-|Z|)
 =|Z\cap C|.                                         \tag{11}
\]

Choose one such component and call its vertex set `R`.  It is connected,
nonempty, and satisfies the first two containments in (9).  Its open
neighbourhood separates `R` from `Q` and is contained in
`Z union N_D(R)`.  Six-connectivity gives

\[
 6\le |N_G(R)|\le |Z|+|N_D(R)|,
\]

which proves the last inequality in (9).

If `|Z|=1`, (11) forces `Z subseteq C` and `R` to be a singleton.  Fullness
of `C` to `r` makes its unique possible `C`-neighbour `z` an actual
neighbour.  The remaining assertions follow from (9).  For `|Z|=2`, a
connected graph on at most two vertices is a singleton or an edge, and
the final bound in (9) is four.  \(\square\)

For five-connectivity, the same proof with `|Z|<=3` gives the following
useful exact form.  If `J_C-Z` has two components containing vertices of
`C-Z` and no boundary-only component, then necessarily

\[
 |Z|=3,\qquad Z\subseteq C,                           \tag{12}
\]

and there are exactly two components, meeting complementary three-sets
of `S`.  In every other failure either `C subseteq Z` or a boundary-only
component occurs.  This is the precise unsafe-contraction dichotomy; no
automatic five-connectivity is claimed.

## 3. Density handoff: a boundary atom or a nested near-model separator

Exact accounting in the quotient gives

\[
 \begin{aligned}
 |V(H_C)|&=|C|+7,\\
 |E(H_C)|&=4|C|+\eta(C)+e_S+6,\\
 q_C:=|E(H_C)|-(4|V(H_C)|-8)&=\eta(C)+e_S-14.
 \end{aligned}                                      \tag{13}
\]

Together with (3),

\[
                         q_A+q_B=e_S+s-4.             \tag{14}
\]

If `e_S>=3`, at least one component `C` satisfies `q_C>=0`, since

\[
 \max\{\eta(A),\eta(B)\}
 \ge\left\lceil{24+s-e_S\over2}\right\rceil.        \tag{15}
\]

### Lemma 5 (six-connected exact near-model descent)

Let `L` be six-connected.  Suppose that

\[
                       X,P,Q,U_1,U_2,U_3,U_4          \tag{16}
\]

are pairwise disjoint connected sets which partition `V(L)` and satisfy:

1. `P,Q,U_1,U_2,U_3,U_4` form a `K_6` model;
2. `X` is anticomplete to `P,Q`; and
3. `X` is adjacent to every `U_i`.

Then `L` contains a `K_7^-` minor, or for some `i` there is a nonempty
proper connected set `Y subset U_i` such that `U_i-Y` is connected and
`N_L(Y)` is an actual vertex separator.  In the latter outcome

\[
                              |N_L(Y)|\ge6.            \tag{17}
\]

If equality holds, every component of `L-N_L(Y)` is adjacent to every
vertex of `N_L(Y)`.

#### Proof

Since the model spans and `X` misses `P,Q`,

\[
                    N_L(X)\subseteq U_1\cup\cdots\cup U_4.
\]

The bag `P` is a nonempty far side of `N_L(X)`.  Thus `N_L(X)` is an
actual separator, and six-connectivity gives `|N_L(X)|>=6`.  Some `U_i`,
say `U`, contains distinct vertices `p,q` adjacent to `X`.

For each of the five foreign bags

\[
                         P,Q,U_j\quad(j\ne i),         \tag{18}
\]

let its portal set in `U` be its nonempty set of neighbours in `U`.  A
retaining core based at `p` is a connected subset of `U` containing `p`
and meeting all five portal sets.

Suppose first that a retaining core `T` based at `p` avoids `q`, and let
`Y` be the component of `L[U-T]` containing `q`.  Then `Y` and `U-Y` are
connected and nonempty, and `U-Y` retains a neighbour in every bag in
(18).  If `Y` has an edge to `P` or `Q`, move `Y` into that bag.  The cut
edge from `Y` to `U-Y` restores the donor--recipient contact, while `T`
preserves all five old contacts of `U-Y`.  The bag `X` now meets both
altered bags through `p,q` and still meets the other three `U_j`.  The
seven resulting bags have at most one missing pair and form a `K_7^-`
model.

We may therefore assume that `Y` has no edge to either `P` or `Q`.  Either
connected twin is then a far side of `N_L(Y)`, so `N_L(Y)` is an actual
separator.  The same argument applies after interchanging `p,q`.

It remains that every retaining core based at either marked vertex
contains the other.  Let `C_q` be the component of `L[U-q]` containing
`p`, and put `Z_q=U-C_q`; define `Z_p` symmetrically.  The two opposite
gates `Z_p,Z_q` are nonempty, disjoint and connected, and have connected
complements.  Their nonempty monopoly sets among the five labels in (18)
are disjoint.  Indeed, an empty monopoly set would make the corresponding
complement a retaining core avoiding the opposite marked vertex.  A
vertex in both gates would force every path from it to `p` to use `q` and
every path from it to `q` to use `p`, contrary to a suffix of a simple
path.  Finally, a nonempty portal set cannot be contained in two disjoint
gates.

If either gate has no edge to `P` or `Q`, its open neighbourhood is an
actual separator with that missed twin as a far side.  Otherwise each gate
has an edge to both twins.  Neither twin label is then monopolised by
either gate.  The two nonempty disjoint monopoly sets lie among only the
three labels `U_j`, `j\ne i`; one of them has order one.  Move that gate
`Z` from `U` into `X`.  The enlarged `X union Z` is connected, meets
`P,Q` through `Z`, and retains its contacts with the other three neutral
bags.  The connected set `U-Z` loses at most the unique monopolised
contact.  These altered sets and the five unchanged bags form a
`K_7^-` model.

This proves the dichotomy.  Inequality (17) is six-connectivity.  If
equality holds and a separator vertex misses one component, the other five
separator vertices separate that component, again contradicting
six-connectivity.  \(\square\)

The proof is the existing audited seven-connected near-model argument with
the only numerical step lowered from seven to six: six neighbours among
four neutral bags still force a repeated portal.

### Theorem 6 (dense returned-row descent)

Assume (3) and `e_S>=3`.  Then at least one of the following holds.

1. A component `C` selected by (15) is an edge of order two, and

   \[
       9\le e_S\le11,
       \qquad |E_G(C,S)|\ge21-e_S.                    \tag{19}
   \]

2. There is a boundary atom `R` satisfying (8)--(9) for that selected
   component.
3. `G` contains a spanning exact `K_7^\vee` model.  Relative to that
   model, Lemma 5 returns a nonempty proper connected part of a neutral
   branch bag whose open neighbourhood is an actual separator of order at
   least six.  At order six the returned separator is full on every
   component.

#### Proof

Choose `C` with `q_C>=0`.  If `H_C` is not four-connected, apply Lemma 4.
In its first outcome, density excludes `|C|=1`: a singleton full component
has `eta(C)=2`, whereas `eta(C)+e_S>=14` and `e_S<=11`.  Thus `C` is an
edge.  Writing `p=|E_G(C,S)|`,

\[
                         \eta(C)=1+p-8=p-7.
\]

Since `p<=12` and `eta(C)+e_S>=14`, (19) follows.  The other outcome of
Lemma 4 is conclusion 2.

Suppose instead that `H_C` is four-connected.  Equation (13) and
`q_C>=0` give

\[
                         |E(H_C)|\ge4|V(H_C)|-8.
\]

Norin--Totschnig, Theorem 6, supplies a `K_7^\vee` minor unless
`H_C` is `K_{2,2,2,2}`.  In that exception `|C|=1`; the pole and the
retained singleton are the unique nonadjacent pair, and their six common
neighbours induce `K_{2,2,2}`, which has twelve edges.  This contradicts
`e_S<=11`.

The quotient is a minor of `G`, so it is target-free.  Make the model
spanning by absorbing each unused component into an adjacent bag.  Target
exclusion ensures that neither absorption creates a missing centre
contact.  Split the pole back into the connected full component `D`
inside the bag which contains it.  Every old contact and the connectedness
of that bag survive.  If either missing centre contact is created in the
lift, the seven bags form a `K_7^-` model in `G`.  Hence the lifted
spanning model is exact.

Apply Lemma 5 in `G`.  Its target outcome is excluded, so it returns the
separator in conclusion 3.  The final fullness statement is the equality
case of Lemma 5.  \(\square\)

The theorem pushes the dense contraction beyond an unrooted near model:
it returns a strict branch-set separator.  It does not yet prove that the
new separator has order six or that one of its closed sides retains
coefficient-four density.

The subsequent independently audited
[`order-two dense-lobe elimination`](hc7_k7minus_returned_order_two_dense_lobe_elimination.md)
rules out outcome 1 by contracting the arbitrary opposite component and
exhausting the resulting `122,941` labelled nine-vertex quotients.  Thus the
current `e_S\geq3` residue consists only of the boundary atom and nested
near-model separator outcomes.

### Proposition 6.1 (the sparse-boundary Lo handoff)

Assume (3) and `e_S<=2`, and choose `C` with maximum excess.  Then

\[
 |E(H_C)|\ge
 \begin{cases}
 4|V(H_C)|-10,&e_S=0,\\
 4|V(H_C)|-9,&e_S\in\{1,2\}.
 \end{cases}                                         \tag{19a}
\]

Either `H_C` is not five-connected and the `|Z|<=3` obstruction following
Lemma 4 occurs, or `H_C` contains both a `K_6^-` minor and a `K_{3,4}`
minor.

#### Proof

Equation (15), substituted in (13), gives `q_C>=-2` when `e_S=0` and
`q_C>=-1` when `e_S` is one or two.  This is (19a).  If `H_C` is not
five-connected, Lemma 3 and the paragraph following Lemma 4 give the
stated obstruction.

Otherwise `H_C` is five-connected and hence has minimum degree at least
five.  It has order at least eight, and (19a) gives

\[
 |E(H_C)|\ge4|V(H_C)|-10>3|V(H_C)|-6,
\]

so it is non-planar.  Lo's Theorem 1.3 supplies both minors; the sole
`K_{3,4}` exception `K_6` has the wrong order.  \(\square\)

This covers the numerical rows missed by the `4n-8` near-model entrance,
but the conclusion is deliberately unrooted.  Neither Lo minor controls
which bags see the pole, and the repository's audited one-apex and
five-visible-bag barriers show that visibility alone cannot be silently
upgraded to `K_7^-`.

## 4. Exact position of the contracted pole in the near model

Label a spanning exact model from Theorem 6 as in (16), with deficient bag
`X`, missed twins `P,Q`, and neutral bags `U_1,...,U_4`.  In the quotient,
let `R_H` be the bag containing the pole `d`; its lifted counterpart is
`R=(R_H-{d}) union D`.

### Lemma 7 (pole-bag visibility)

The following statements hold.

1. If `R=X`, then neither `P` nor `Q` contains a vertex of `S`.
2. If `R=P` or `R=Q`, then `X` contains no vertex of `S`.
3. If `R` is neutral, fullness alone imposes no missing-pair repair.

#### Proof

Every vertex of `S` has a neighbour in `D`.  If `D subseteq X` and, say,
`P` contained a boundary vertex, the edge from that vertex to `D` would
create the missing `X-P` contact and leave at most `X-Q` absent.  This
would be a `K_7^-` model.  The same argument treats `Q`.

If `D subseteq P` and `X` contained a boundary vertex, fullness would
repair `X-P`; the other twin is symmetric.  A neutral bag is already
adjacent to every other model bag, so contacts created from it repair
neither of the two missing pairs.  \(\square\)

This is the normalization which follows formally from the contraction.
The unrooted density theorem does not force the pole bag to be the
deficient bag or a twin.

### Lemma 8 (exact pole-split certificate)

Let `d` denote the contracted pole before it is split.  Choose five model
bags other than `R_H` which form a `K_5` model.  Such a choice is always
possible; if `R_H` is a twin or neutral, omit `X`.  Suppose that

1. `d` is adjacent to at least four of the chosen five bags; and
2. some component `W` of `H_C[R_H-{d}]` has a neighbour at `d` and has an
   edge to every chosen bag.

Then `G` contains a `K_7^-` minor.

#### Proof

In `H_C`, the seven sets consisting of `{d}`, `W`, and the five chosen
bags are connected and disjoint.  The chosen bags form a `K_5`, `W` is
adjacent to all of them and to `{d}`, and `{d}` misses at most one of
them.  They form a `K_7^-` model in `H_C`, which lifts to `G`.  \(\square\)

Consequently, in a target-free quotient, for every eligible external
`K_5` on which the pole has at least four contacts, no component of
`R_H-{d}` carries all five required contacts (some contacts may be carried
only by `d`).  If there is no such `K_5`, the pole has at most three
contacts on each eligible external `K_5`.  This is the first obstruction
to splitting the pole out of an unrooted `K_7^\vee` model.

If both inequalities

\[
                    \eta(A)+e_S\ge14,
        \qquad       \eta(B)+e_S\ge14                 \tag{20}
\]

hold and both quotients pass the cut test in Lemma 3, the argument gives
two spanning exact models, one in each contraction orientation.  Each
model separately satisfies Lemmas 7 and 8 and returns a nested separator
through Lemma 5.  Pole-visibility and pole-articulation are therefore the
remaining alternatives in both orientations; the present argument proves
no incompatibility between their portal partitions.  Coupling those two
partitions is the exact missing two-orientation theorem.

## 5. Complementary rooted helpers do compose across the two shores

For `C in {A,B}` and `t in S`, write

\[
                         a_C(t)=|E_G(C,\{t\})|.        \tag{21}
\]

### Theorem 9 (two-shore rooted-helper composition)

Choose distinct `a,x,y in S` and put `T=S-{a,x,y}`.  Suppose `G[T]` is a
triangle.  If

\[
 \eta(A)>a_A(a)+a_A(x),
 \qquad
 \eta(B)>a_B(a)+a_B(y),                              \tag{22}
\]

then `G` contains a `K_7^-` minor.

#### Proof

Put `Z_A=S-{a,x}`.  Complete `Z_A` to a clique in `G[A union Z_A]`.  The
resulting four-rooted graph has

\[
 \begin{aligned}
 |E|
 &=4|A|+\eta(A)-a_A(a)-a_A(x)+6\\
 &\ge4(|A|+4)-9.                                     \tag{23}
 \end{aligned}
\]

The rooted pair is internally four-connected: a rooted separation of
order at most three, together with `a,x`, would give a cut of `G` of order
at most five with `B` on the other side.  Norin--Totschnig, Lemma 12,
therefore supplies a `Z_A`-rooted `K^*_{4,2}` model.  The added edges join
distinct nominated roots.  Root bags are distinct and root--root
adjacencies are not required in `K^*_{4,2}`, so deleting those added edges
does not damage the model.

The pair rooted at `S-{a}` in `G[A union(S-{a})]` is internally
five-connected: a forbidden rooted separation of order at most four,
together with the omitted vertex `a`, would again give a cut of `G` of
order at most five.  The audited fifth-root augmentation lemma therefore
puts `x` in one helper bag.  Call the other helper `V_A`.

The symmetric argument in `B`, with roots `Z_B=S-{a,y}`, puts `y` in one
helper and gives a residual helper `V_B`.

For each `t in S-{a}`, merge the two model bags containing `t`.  The five
resulting label bags are disjoint and connected.  The bag labelled `x` is
adjacent to the other four through the `A`-model, and the bag labelled `y`
is adjacent to the other four through the `B`-model.  The remaining three
are pairwise adjacent through the literal triangle `G[T]`.  Thus the five
label bags form a `K_5` model.

Each of `V_A,V_B` is adjacent to all five label bags.  The two residual
helpers lie in opposite components and may be nonadjacent; this is the
only possible missing pair.  The seven bags form `K_7^-`.  \(\square\)

This theorem is the desired compatible-pair implication: two complementary
rooted `K^*_{4,2}` models really do cross-merge.  What the global excess
identity does not force is the compatible choice of omitted roots.

## 6. Exact recession obstruction to forcing compatible pairs by excess

For any `c>=2`, let a component `C` be an induced path on `c` vertices.
Make four vertices of `S` adjacent to every path vertex and make the
remaining two vertices adjacent only to opposite ends of the path.  Then

\[
 |E(C)|=c-1,
 \qquad
 (a_C(t):t\in S)=(c,c,c,c,1,1),
 \qquad
 \eta(C)=c+1.                                        \tag{24}
\]

Hence

\[
                 \eta(C)>a_C(p)+a_C(q)               \tag{25}
\]

holds for exactly one pair: the two low-attachment roots.  Two such lobes
aligned on the same low pair therefore supply the same single edge in
their helper-supply graphs.  Theorem 9 needs two distinct supply edges
with a common endpoint, so the excess inequalities alone do not force a
compatible pair.

This obstruction meets the returned arithmetic at arbitrary lobe scale.
For example, take path orders five and six and `e_S=11`.  Their excesses
are six and seven, so (3) holds with `s=0`.  One can also meet literal
six-connectivity: label the low roots `0,1`, the common roots `2,3,4,5`,
and take the eleven boundary edges

```text
02 03 04 05  12 13 14 15  23 25 34.
```

If a common root survives deletion of at most five vertices, it joins all
surviving path pieces and both low roots.  If all four common roots are
deleted, only one further deletion is possible; the two low roots and the
two parallel paths remain connected.  Thus this equality host is
six-connected.

The family is a recession profile for the **inequality system**, not a
target-free counterexample and not a failure of the actual rooted models.
It proves that the next positive input must use equality structure or
model placement inside the lobes, rather than only `eta(A)+eta(B)` and the
six attachment totals.

The deterministic standard-library checker
[`experiments/returned_two_component_equality_witness_verify.py`](experiments/returned_two_component_equality_witness_verify.py)
exhausts all `9,402` deletions of at most five vertices and verifies the
edge count, the two full components, excesses `(6,7)`, six-connectivity,
six literal boundary triangles, and absence of a compatible supply triple.
Its SHA-256 is

```text
e7960a8c3738ac3cb3c1f621a221db21cf94c5e7f1fa0a1fe2cc7df9896a2c56.
```

It deliberately makes no target-minor claim.

## External inputs

- Sergey Norin and Agnès Totschnig,
  *Every graph with no `K_7^\vee` minor is 6-colourable*, Theorem 6 and
  Lemma 12, arXiv:2507.03244.
- O.-H. S. Lo, *A characterization of graphs with no `K_{3,4}` minor*,
  Theorem 1.3, arXiv:2603.27973v1.
- The audited
  [fifth-root augmentation lemma](hc7_k7minus_e5_k5minus_cut_elimination.md#lemma-1-fifth-root-augmentation).
- The audited seven-connected
  [`K_7^\vee` model-or-separator theorem](../results/hc7_k7minus_exact_k7vee_separator_dichotomy.md),
  whose proof is reproduced at connectivity six in Lemma 5.

## Exact scope

Theorem 6 is an unbounded target-sensitive reduction of every returned
two-component boundary with at least three edges.  Its order-two dense-lobe
output has now been eliminated by the linked independently audited theorem.
Its unresolved outputs are a one- or two-vertex pinned boundary atom or a
new near-model separator whose density has not been controlled.
Proposition 6.1 reduces the remaining boundary sizes to the exact
three-separation obstruction or to two unrooted Lo minors.

Theorem 9 is an unconditional cross-shore composition theorem.  Section 6
shows exactly why the known excess bounds do not force its hypotheses.
Neither result eliminates the whole two-component row.  In particular,
the significance benchmark of the Norin--Totschnig paper has not been met
by this note.
