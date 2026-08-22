# Literal `K_{4,4}` exterior: exact quotient lemmas and three-connectivity

Status: rigorous computer-assisted side theorem and an explicitly labelled
capstone conjecture.  This note does **not** prove Conjecture 21 or the literal
`K_{4,4}` closure theorem.

## 1. Setting

Let `G` be a finite simple `7`-connected graph with no `K_7^-` minor.  Suppose
that `G` contains a literal `K_{4,4}` with shores

`A={a_0,a_1,a_2,a_3}` and `B={b_0,b_1,b_2,b_3}`,

and put `S=A union B` and `C=G-S`.  Edges inside a shore are allowed.  For a
subgraph `X` of `C`, write

`partial_S(X)=N_G(V(X)) intersect S`.

Whenever `X` is a nonempty proper fragment of `C`, seven-connectivity gives

`|N_C(X)|+|partial_S(X)| >= 7`.                                      (1)

Also `|partial_S(C)|>=7` whenever `C` is nonempty.

## 2. Exact finite quotient lemmas

All contractions below delete every vertex not named in the quotient.

### Lemma 2.1 (two anticomplete near-full vertices)

Start with `K_{4,4}` on `S` and add anticomplete vertices `c,d`, each adjacent
to at least seven vertices of `S`.  The resulting graph has a `K_7^-` minor.

#### Proof

The common `S`-neighbourhood of `c,d` has order at least six, and contains
at least two vertices in each shore.  Choose common neighbours `a in A` and
`b in B`.  Pair the other three vertices of `A` with the other three
vertices of `B`, avoiding the sole possible pair consisting of the vertex
missed by `c` and the vertex missed by `d`.  Such a perfect matching exists:
among the six possible perfect matchings, at most two use any prescribed
cross-pair.  Its three cross-edge bags, together with `{a}` and `{b}`, form
a `K_5` model in the literal `K_{4,4}`.  Every one of these five bags
contains a common neighbour of `c,d`.  Adding `{c}` and `{d}` gives seven
bags with every adjacency except possibly `cd`, and hence a `K_7^-` model.
QED

### Lemma 2.2 (an adjacent six-portal pair)

Start with `K_{4,4}` on `S` and add adjacent vertices `c,d`, each adjacent to
at least six vertices of `S`.  The resulting graph has a `K_7^-` minor.

### Lemma 2.3 (sharp adjacent five-portal classification)

Start with `K_{4,4}` on `S` and add adjacent vertices `c,d`, each adjacent to
at least five vertices of `S`.  If there is no `K_7^-` minor, then both have
exactly five neighbours in `S` and, after exchanging the shores and applying
shore automorphisms, their missed sets are

`S-N(c)={a_0,a_1,b_0}` and `S-N(d)={a_2,a_3,b_0}`.                  (2)

Conversely all `48` ordered profiles in (2) are target-free.  Adding any edge
between `{a_0,a_1}` and `{a_2,a_3}` makes every such profile target-positive.

Lemma 2.1 has the preceding human proof.  Lemmas 2.2--2.3 are independently
decided by exhaustive enumeration of every seven-bag minor model of the
ten-vertex *adjacent-pair* quotient.  There are exactly `11,880` canonical
partitions (unused vertices allowed).  The census output is

```
partitions=11880
total=26569 negative=5428
hist 4 4 4900
hist 4 5 240
hist 5 4 240
hist 5 5 48
special_five=48 crossing_edge_positive=192
```

The `48*4=192` last checks independently test every shore-crossing edge in
the sharp five-portal profiles.

## 3. Exterior three-connectivity theorem

### Theorem 3.1

In the setting of Section 1, `C` is connected and no set of at most two
vertices separates two nonempty vertex sets of `C`.  In particular, if
`|V(C)|>=4`, then `C` is three-connected.

### Proof

Suppose first that `C` has distinct components `X,Y`.  The neighbourhood of
each component is contained in `S`; hence seven-connectivity gives
`|partial_S(X)|,|partial_S(Y)|>=7`.  Contract `X` and `Y` separately and
delete every other exterior component.  This gives the quotient in Lemma 2.1,
a contradiction.  Thus `C` is connected.

Suppose next that `p` is a cutvertex of `C`, and let `X,Y` be two components
of `C-p`.  The set `partial_S(X) union {p}` separates `X`, so (1) gives
`|partial_S(X)|>=6`; similarly `|partial_S(Y)|>=6`.  Contract `X` to one bag
and `Y union {p}` to a second bag, deleting the other components.  The two
bags are adjacent because `p` has a neighbour in `X`.  Lemma 2.2 gives a
contradiction.  Hence `C` is two-connected.

Suppose finally that `{p,q}` is a two-cut, and choose distinct components
`X,Y` of `C-{p,q}`.  Since `C` is two-connected, every component of
`C-{p,q}` has a neighbour in each of `p,q`.  Equation (1) gives

`|partial_S(X)|,|partial_S(Y)|>=5`.                                (3)

Contract `X union {p}` and `Y union {q}` to adjacent bags.  Also make the
swapped contraction `X union {q}`, `Y union {p}`.  Because `G` is
target-free, Lemma 2.3 applies to both quotients.  From (3), equality holds,
and

`N_S(p),N_S(q) subseteq partial_S(X) intersect partial_S(Y)`.       (4)

Lemma 2.3 now gives, after symmetry, a vertex `b_0 in B` and a two-set
`U subset A` such that

`partial_S(X)=(B-{b_0}) union U`,

`partial_S(Y)=(B-{b_0}) union (A-U)`,                              (5)

and (4) is contained in `B-{b_0}`.

There cannot be a third component `Z`.  For a fixed five-set in (5), the
classification in Lemma 2.3 has a unique target-free partner, namely the
other five-set in (5).  Thus `partial_S(Z)=partial_S(Y)`, but the pair `Y,Z`
has equal profiles and is not one of the `48` exceptional ordered profiles.
Its adjacent contraction is target-positive, a contradiction.

Delete the six vertices `{p,q} union B`.  By (4)-(5), and because `X,Y` are
the only components of `C-{p,q}`, the remaining graph is disconnected
between `X union U` and `Y union (A-U)` unless `G[A]` has an edge joining
`U` to `A-U`.  Seven-connectivity therefore forces such an edge.  The last
assertion of Lemma 2.3 says that this edge makes the contracted quotient
target-positive, again a contradiction.  No two-cut exists.  QED.

## 4. Two further exact completion lemmas

### Lemma 4.1 (portal triangle)

`K_{4,4}` plus an exterior triangle whose three vertices each have at least
four core neighbours always contains `K_7^-`.

A restricted core-`K_4` packing handles `733,990` of the `735,130` unordered
minimal profiles.  An unrestricted exact fallback handles the remaining
`1,140`; it checks `8,601,313` branch models and finds no negative profile.

Consequently, a target-free exterior `C` has no three pairwise adjacent
connected branch sets that each see at least four vertices of `S`.  In
particular, `C` has at most two individual vertices with at least four core
neighbours: in a three-connected graph any three prescribed vertices admit
a rooted triangle model.

### Lemma 4.2 (portal `K_4`, sharp form)

`K_{4,4}` plus an exterior `K_4` whose four vertices each have at least three
core neighbours contains `K_7^-`, with exactly one family of exceptions:
the four neighbourhoods are the four distinct three-subsets of one common
four-set `Q subseteq S`.

For the `455,126` unordered minimal profiles, a restricted core-`K_3`
packing handles `453,956`.  An independent SMT encoding of connected branch
sets decides the other `1,170` and returns exactly `binom(8,4)=70` negatives,
one for each `Q`.  Monotonicity makes the displayed family the complete
classification for neighbourhoods of size at least three: fixing any three
of the four exceptional triples uniquely determines the fourth, so no
neighbourhood can be enlarged.

If the exterior `K_4` model is spanning, the exceptional family is impossible,
because it would give `|partial_S(C)|=4`, whereas seven-connectivity gives at
least seven.

## 5. The remaining capstone and falsified naive versions

The following is sufficient to prove the literal `K_{4,4}` closure theorem.

### Core-sensitive capstone (open)

Under (1), for a three-connected exterior `C`, at least one holds:

1. `C` has three pairwise adjacent disjoint connected bags, each with at
   least four distinct neighbours in `S`;
2. `C` has a spanning `K_4` model whose four bags each have at least three
   distinct neighbours in `S`;
3. the literal `K_{4,4}` together with `C` already has a `K_7^-` minor.

Items 1 and 2 close by Lemmas 4.1 and 4.2.  Item 3 is the conclusion.

The target alternative is essential.  Let `C=K_6` and give its vertices
portal sets `{0,i}` for `i=1,...,6`.  Then every nonempty `X subseteq C`
satisfies equality in (1), but three weight-four bags need at least nine
vertices, while every four-part partition of six vertices has two singleton
weight-two bags.  Nevertheless core vertex `0` together with `C` is a
literal `K_7`.

The naive weighted-`K_4` assertion is also false in a fully seven-connected
host.  One exact obstruction has `C=W_5`, with hub portal set `{5,6}` and the
five rim portal sets

`{2,3,5,7}`, `{0,3,4,7}`, `{1,2,3,4}`, `{0,1,3,6}`, `{1,3,5,7}`

in cyclic order.  Every `K_4` model of `W_5` leaves the hub as a weight-two
singleton.  This host is nevertheless target-positive through a portal-rich
triangle.  A concrete `K_7^-` model is recorded by the verifier.

Thus a proof must use a lexicographically maximal model together with the
target alternative; connectivity alone does not force the weighted model.

## 6. Reproducibility

The self-contained adjacent-pair verifier is
`hc7_literal_k44_adjacent_portal_census_verify.c`; it certifies only Lemmas
2.2--2.3, while Lemma 2.1 is proved directly above.  The two independent
orbit verifiers supporting Lemmas 4.1--4.2 are linked from their dedicated
result notes.  Exact source hashes and commands are pinned in
`hc7_k44_closure_local_normal_forms_audit.md`.

Random falsification (not proof) found no failure of the literal closure or
the rooted `K_4` plus disjoint rooted three-vertex-path packing in fully
seven-connected samples on 11--15 vertices.  No bounded experiment is used
to infer an unbounded statement.
