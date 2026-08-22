# Pure `C_7` twin seam: arc-local portals and a three-connected exterior

**Status.**  Written reduction with an exact finite boundary verifier.  It
does not eliminate the pure-cycle branch.  In particular, exterior bags are
not silently treated as adjacent to the twins.

## 1. Setting

Let `G` be seven-connected with minimum degree at least eight.  Let `a,b`
be adjacent degree-eight true twins and put

\[
 T=N_G(a)-\{b\}=N_G(b)-\{a\},\qquad
 D=G-(T\cup\{a,b\}).
\]

Assume that `G[T]` is the chordless cycle
`t_0t_1...t_6t_0` and that `G` has no `K_7^-` minor.  Every `t_i` has at
least four neighbours in `D`, since its two twins and two cycle neighbours
account for exactly four of its neighbours outside `D`.

For `X subseteq D`, write

\[
                P(X)=N_G(X)\cap T,
\]

and put `P(x)=P({x})`.

## 2. A finite anchored-cycle lemma

### Lemma 2.1

Let `X,Y` be disjoint connected adjacent vertex sets, anticomplete to two
adjacent twins which are complete to a disjoint chordless seven-cycle `T`.
If

\[
                         |P(X)|\ge5,\qquad |P(Y)|\ge5,
\]

then the graph contains a `K_7^-` minor.

### Exact verification

The verifier `verify_c7_two_support_anchored_k5minus.c` checks every one of
the

\[
             \left(\binom75+\binom76+\binom77\right)^2=29^2=841
\]

ordered support pairs.  For each pair it exhausts all assignments of the
seven cycle vertices to five bag labels `X,Y,A,B,C` or to the unused label.
It requires:

1. every bag receives a cycle vertex, so all five bags meet `T`;
2. every cycle vertex assigned to the `X`-bag (respectively `Y`-bag) lies
   in the corresponding support, so adjoining it preserves connectivity;
3. each of the three cycle-only bags induces a connected subpath of `C_7`;
4. the literal `X--Y` exterior edge, all support edges and all cycle edges
   give at least nine of the ten five-bag contacts.

The output is

```text
GREEN support_pairs=841 failures=0 minimum=5
```

Adding the singleton twin bags gives the required seven-bag model.  This
is an exact exhaustive proof of the finite lemma once the 94-line verifier
is audited; it is not an inference from bounded host enumeration.

The anchors in item 1 are essential.  Merely taking `X,Y` and three cycle
arcs would leave both exterior bags anticomplete to both twins, losing four
contacts.

## 3. Exterior connectivity

### Theorem 3.1

Under the setting of Section 1, `D` is three-connected.

### Proof

The already proved disconnected-exterior argument says that every component
of a disconnected `D` is `T`-full; two components and three cycle intervals
then give a `T`-hitting `K_5^-` model, contrary to the hypothesis.  Thus `D`
is connected.

Suppose first that `z` is a cut vertex of `D`, and let `C` be a component
of `D-z`.  Since

\[
                         N_G(C)\subseteq T\cup\{z\},
\]

seven-connectivity gives `|P(C)|>=6`.  The set `D-C` is connected: it
contains `z`, and every other component of `D-z` attaches to `z`.  It also
contains another component `C'` of `D-z`, and the same argument gives
`|P(C')|>=6`.  Hence `|P(D-C)|>=6`.  The two shores are adjacent, so
Lemma 2.1 is a contradiction.  Thus `D` is two-connected.

Now suppose that `Z={z_1,z_2}` is a two-vertex cut of `D`, and let `C` be a
component of `D-Z`.  Two-connectivity makes every component of `D-Z`
adjacent to both vertices of `Z`; otherwise one member of `Z` would be a
cut vertex.  Therefore `D-C` is connected.  Seven-connectivity and

\[
                         N_G(C)\subseteq T\cup Z
\]

give `|P(C)|>=5`.  A second component `C'` exists and is contained in
`D-C`, so the same inequality gives `|P(D-C)|>=5`.  Again the two shores
are adjacent and Lemma 2.1 is a contradiction.  No cut of order at most two
exists.  \(\square\)

## 4. Edge-profile restriction

### Corollary 4.1

For every edge `xy` of `D`,

\[
                            |P(x)\cup P(y)|\le4.       \tag{4.1}
\]

### Proof

The set `X={x,y}` is connected.  By Theorem 3.1,
`Y=D-{x,y}` is connected.  It is adjacent to `X`, since deleting the two
vertices cannot leave `X` isolated from the rest of the connected graph
`D` (and `D` has more than two vertices; indeed every cycle portal has four
neighbours in `D`).
Every cycle vertex has at least four neighbours in `D`, so deleting `x,y`
leaves a neighbour in `Y`; hence `P(Y)=T`.  If the left side of (4.1) were
at least five, Lemma 2.1 applied to `X,Y` would give the forbidden minor.
\(\square\)

Thus any completion by a connected support-five bipartition must use a
shore of order at least three.  If such a shore has connected complement,
it is already terminal by Lemma 2.1.

## 5. Arc-locality from the rooted-K4 concentration identities

Assume additionally the campaign's critical-host hypotheses, so the
Rolek--Song/Kriesell--Mohr rooted packet is available for every independent
triple of `T`.  For an independent triple `S`, absorb the unused vertices
of `G-(\{a,b\}\cup S)` into the four rooted `K_4` bags indexed by `T-S`.
Target-freeness gives, for every `s in S`,

\[
 N_D(s)\subseteq B_{s^-}\cup B_{s^+}.                 \tag{5.1}
\]

### Lemma 5.1

No vertex of `D` is adjacent to two cycle vertices at cyclic distance
three.  Consequently every `P(x)` is contained in some three-consecutive
vertex arc of `T`.

### Proof

Let `t_i,t_j` be at cyclic distance three.  They extend to an independent
triple `S` of the seven-cycle.  Their two pairs of cycle neighbours are
disjoint.  In the spanning four-bag partition, (5.1) would place a common
exterior neighbour in one of the two bags indexed by the first neighbour
pair and simultaneously in one of the two disjoint bags indexed by the
second pair.  This is impossible.

The previously proved portal lemma says that `|P(x)|<=2`, or `P(x)` is a
consecutive triple.  A set of order at most two with no distance-three pair
also lies in a three-consecutive arc.  \(\square\)

Combining Lemma 5.1 with (4.1), adjacent exterior vertices have two
arc-local portal profiles whose union has order at most four.

## 6. Exact stopping point

The remaining assertion is unbounded:

> In the three-connected exterior `D`, with each portal occurring at least
> four times, relative inequality
> `|N_D(X)|+|P(X)|>=7`, minimum degrees
> `d_D(x)+|P(x)|>=8`, arc-local vertex profiles, and the edge restriction
> (4.1), find two disjoint connected sets of support at least five.

Two disjoint connected sets can be extended to a connected bipartition, and
Lemma 2.1 would then close the seam.  No proof of this packing statement is
given here.  In particular, a support-three `st` sweep does not suffice:
without two separately consumed cycle anchors, the twin--shore contacts are
absent.

The exact MILP `search_c7_twin_support5_arc_local.py` has found no weighted
counterexample on any unlabelled three-connected exterior through order
eight (`136` graphs at order seven and `2388` at order eight).  The retained
generator now accepts the target order as an optional argument; the exact
order-eight input has `11117` connected isomorphism classes and SHA-256
`8ad4ca0903a76a39e28ae4d19b1f6137b8bb23798f3896b7aa37399ad639e500`.
This is bounded falsification only, not a proof of the displayed assertion.
