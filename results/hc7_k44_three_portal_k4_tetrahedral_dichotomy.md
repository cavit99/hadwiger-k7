# The tetrahedral obstruction for a three-portal `K_4` over `K_{4,4}`

**Status.** Computer-assisted local dichotomy with an independent orbit
enumeration, nine explicit positive certificates, and a human proof that
the remaining family is genuinely `K_7^-`-minor-free.  This is a sharp
side result and a separator normal form, not a proof of
Norin--Totschnig Conjecture 21 and not a major-theorem completion.

Write `K_7^-` for `K_7` with one edge deleted.

## Theorem 1 (three-portal `K_4` dichotomy)

Let `G` contain a specified literal `K_{4,4}` subgraph `H`, with shores

\[
 A=\{0,1,2,3\},\qquad B=\{4,5,6,7\},
\]

and a literal `K_4` on four vertices `P` disjoint from `H`.  Suppose that

\[
                         |N_H(p)|\ge3\qquad(p\in P).    \tag{1}
\]

Then at least one of the following conclusions holds.

1. `G` contains a `K_7^-` minor.
2. There are a four-set `S subseteq V(H)` and a bijection
   `p_s in P` for `s in S` such that

   \[
                          N_H(p_s)=S-\{s\}.             \tag{2}
   \]

The second outcome is genuine: for every four-set `S`, the graph
`F(S)` consisting of `H`, the clique `P`, and precisely the twelve edges
in (2) has no `K_7^-` minor.

Thus a target-free instance has exactly three core neighbours at each
clique vertex, and its core--clique incidence is `K_{4,4}` minus a perfect
matching on `S union P`.

## The exact finite census

First suppose every member of `P` has exactly three neighbours in `H`.
There are `binom(8,3)=56` possible neighbourhoods and therefore

\[
                         \binom{56+4-1}{4}=455{,}126    \tag{3}
\]

unordered four-neighbourhood profiles.

A sufficient certificate is a three-bag `K_3` minor model in `H` with at
most one missed contact among the twelve clique-vertex--bag pairs.  The
primary census enumerates `3,784` such core models.  It certifies
`453,956` profiles and leaves `1,170`.

The independent orbit verifier regenerates the calculation without using
the primary branch-set generator.  It assigns each of the eight core
vertices to one of three labelled bags or to an unused class, an explicit
universe of `4^8` assignments.  After testing connectivity and the three
bag contacts, it again obtains `3,784` models and the same `1,170`
restricted failures.  Quotienting by

\[
 \operatorname{Aut}(K_{4,4})\times S_4
 \cong ((S_4\times S_4)\rtimes C_2)\times S_4          \tag{4}
\]

leaves twelve orbits.  Nine orbits, containing `1,100` profiles, have the
explicit `K_7^-` models in Table 1.  The remaining three orbits, containing
`70` profiles, are precisely the family (2), one profile for each
four-set `S` in `H`.

### Table 1. The nine positive fallback orbits

The four triples in column three are the four `H`-neighbourhoods, in the
order assigned to clique vertices `8,9,10,11`.  Each row lists seven
disjoint connected branch sets.  All pairs of branch sets touch except
the single pair in the last column.

| row | orbit size | four neighbourhoods | seven branch sets | missing pair by bag index |
|---:|---:|---|---|---|
| 1 | 48 | `(012,013,014,234)` | `(2356),(07),(4,11),(1),(8),(9),(10)` | `0--6` |
| 2 | 144 | `(012,014,015,245)` | `(0367),(24),(5,11),(1),(8),(9),(10)` | `1--6` |
| 3 | 32 | `(012,034,134,234)` | `(0156),(278),(3),(4),(9),(10),(11)` | `0--6` |
| 4 | 48 | `(012,045,145,245)` | `(0167),(28),(34),(5),(9),(10),(11)` | `0--6` |
| 5 | 36 | `(014,015,234,235)` | `(048),(169),(27),(3),(5),(10),(11)` | `4--5` |
| 6 | 144 | `(014,015,245,267)` | `(236,11),(07),(4,10),(1),(5),(8),(9)` | `4--5` |
| 7 | 288 | `(014,024,035,125)` | `(1267),(05),(3,10),(4),(8),(9),(11)` | `3--6` |
| 8 | 288 | `(014,024,045,125)` | `(1367,11),(25),(0),(4),(8),(9),(10)` | `1--4` |
| 9 | 72 | `(014,025,135,234)` | `(068),(17,10),(35),(2),(4),(9),(11)` | `4--5` |

Here, for example, `(236,11)` means the branch set
`{2,3,6,11}`.  Direct inspection verifies connectivity and all twenty
displayed contacts; the independent verifier checks the exact listed gap
in every row.

The three negative orbit representatives and their sizes are

| shore split of `S` | orbit size | four neighbourhoods |
|---|---:|---|
| `4+0` | 2 | `(012,013,023,123)` |
| `3+1` | 32 | `(012,014,024,124)` |
| `2+2` | 36 | `(014,015,045,145)` |

They are uniformly

\[
                         \{S-\{s\}:s\in S\}.           \tag{5}
\]

The counts in the two tables give `1,100+70=1,170`.

## Lemma 2 (the tetrahedral graphs are target-free)

For every four-set `S subseteq V(H)`, the graph `F(S)` has no
`K_7^-` minor.

### Proof

Add all missing edges inside `S`, obtaining `F^+(S)`.  This is a clique-sum
of order four, along the clique `S`, of

\[
 Q_1=H+K[S]
 \quad\hbox{and}\quad
 Q_2=F(S)[S\cup P]+K[S].                              \tag{6}
\]

The second summand is `K_8-4K_2`: both `S` and `P` are cliques and the
only cross-nonedges are the four matched pairs `sp_s`.

Recall the standard localization fact: if a graph `J` is
`(k+1)`-connected and is a minor of a clique-sum of order at most `k`,
then `J` is a minor of one summand.  Indeed, a model using vertices
strictly on both sides induces in `J` a separation whose separator consists
of the at most `k` model bags meeting the sum clique.  If no model bag lies
strictly on one side, excursions into that side can be replaced through the
clique, leaving a model in the other summand.  The graph `K_7^-` is
five-connected, so the fact applies to (6) with `k=4`.

It remains to check the two eight-vertex summands.

For `Q_2=K_8-4K_2`, a seven-bag model either deletes one vertex or contracts
one connected pair.  Deleting one vertex leaves three matched nonedges.
A connected pair uses vertices from two different matched pairs, so the
other two matched nonedges remain between singleton bags.  In either case
at least two quotient edges are absent.  Thus `Q_2` has no `K_7^-` minor.

For `Q_1`, the only nonedges are same-shore pairs which are not both in
`S`.  By exchanging the shores, assume
`a=|S cap A| in {2,3,4}`.

* If `a=4`, the four vertices of `B` are independent.  After a deletion at
  least three of their six nonedges remain.  After a cross-shore
  contraction the three remaining `B` vertices retain three nonedges, and
  a same-shore connected contraction lies in `S subseteq A` and leaves all
  six `B` nonedges.
* If `a=3`, then `|S cap B|=1`, so all six pairs in `B` are nonedges.  A
  deletion or cross-shore contraction leaves at least three of them; a
  same-shore connected contraction again leaves all six.
* If `a=2`, each shore has only the one edge joining its two vertices in
  `S`.  A cross-shore contraction leaves at least two nonedges among each
  remaining shore triple, while a same-shore connected contraction leaves
  all five nonedges in the other shore.

Thus every seven-bag quotient of `Q_1` also misses at least two edges.
Neither summand contains `K_7^-`; localization shows that `F^+(S)`, and
hence its subgraph `F(S)`, does not contain it.  \(\square\)

## Proof of Theorem 1

For each `p in P`, choose a three-set `T_p subseteq N_H(p)`.  Apply the
finite census to the unordered profile `(T_p:p in P)`.  If it is one of
the `455,056` positive profiles, its displayed minor uses only selected
edges and lifts to `G`.

Suppose `G` is target-free.  Then every selection must have the form (5).
Fix the selected triples at three clique vertices.  In a tetrahedral
profile those three distinct triples determine the four-set `S` and the
fourth triple uniquely.  If the fourth clique vertex had four or more core
neighbours, it would have a different selectable three-subset, producing a
non-tetrahedral and hence positive profile.  Thus its core degree is three.
Repeating this argument at each clique vertex proves that every
`N_H(p)` has order exactly three, and their unique profile is (5).  Relabel
the vertices of `P` to obtain (2).  Lemma 2 proves the asserted sharpness.
\(\square\)

## Lemma 3 (one component seeing the whole clique is terminal)

Assume the tetrahedral outcome (2).  Let `D` be a connected subgraph
disjoint from `H union P`.  If `D` is adjacent to every vertex of `P` and
has at least one neighbour in `H`, then `G` contains a `K_7^-` minor.

### Proof

Contract `D` to a vertex `d`.  Partition `S` into two pairs.  Make each
pair into a connected core bag as follows.  A pair meeting both shores is
already connected.  For a same-shore pair, add a distinct unused vertex
from the opposite shore.  Such distinct connectors can always be chosen:
for the three shore splits `4+0`, `3+1`, and `2+2`, respectively, two,
one, and zero connectors are needed.  Call the resulting bags `B_1,B_2`.

The bags are disjoint, each meets both shores, and hence they are adjacent.
Each contains two vertices of `S`.  Since `p_s` misses only `s` in `S`,
every vertex of `P` is adjacent to both bags.  If neither bag contains a
neighbour of `d`, absorb any `H`-neighbour of `d` into one bag; because
that bag meets both shores, connectivity is preserved.

Now use the four singleton bags in `P`, the singleton `{d}`, and
`B_1,B_2`.  All pairs touch except possibly `{d}` and the core bag into
which no `d`-neighbour was absorbed.  These are seven branch sets for
`K_7^-`.  \(\square\)

## Corollary 4 (seven-connected component profile)

Let `G` be seven-connected and target-free, and suppose `H` and `P`
satisfy (1).  Put `R=G-(V(H) union P)`.  Then:

1. the tetrahedral outcome (2) holds;
2. every vertex of `P` has a neighbour in `R`; and
3. no component `D` of `R` is adjacent to all four vertices of `P`.

Consequently, the proper subsets `N_P(D)` over components `D` of `R`
cover `P`, and seven-connectivity gives the exact lower bound

\[
                       |N_H(D)|\ge 7-|N_P(D)|.          \tag{7}
\]

### Proof

Theorem 1 gives assertion 1.  In the tetrahedral configuration each clique
vertex has exactly six neighbours in `H union P`, so minimum degree seven
gives assertion 2.  If a component of `R` saw all of `P`, then its boundary, contained in
`H union P`, would have order at least seven.  It would therefore see at
least three vertices of `H`, contradicting Lemma 3.  This proves assertion 3, and
the boundary inequality is immediate.  \(\square\)

## Reproduction and finite trust boundary

Run

```text
python3 results/hc7_k44_three_portal_k4_tetrahedral_dichotomy_verify.py
```

The independent audit terminates with

```text
core_models 3784
restricted_failures 1170
orbits 12 positive 9 negative 3
negative_profiles 70
orbit_sizes [2, 32, 32, 36, 36, 48, 48, 72, 144, 144, 288, 288]
sha256 95b9d40e6e9ff1778b364b0a883fe0d72e7f41f9f5d9258c31af215ea38272bf
tetrahedral_near_miss_orbits 3 quotient_edges 19
classification_and_certificates_valid
```

The finite trust boundary is the Python interpreter, exact integer bit
operations, and the explicit exhaustive loops.  The independent verifier
does not import either primary census.  It also checks the exact one-edge
gap in every positive representative and exhaustively checks the two
eight-vertex clique-sum summands in the negative proof.  This is an
internal cold audit, not external peer review.

## Scope

The theorem gives a sharp normal form for a literal exterior `K_4` and
turns seven-connectivity into the proper-component cover in Corollary 4.
It does not eliminate that cover: several exterior components may divide
the four clique vertices among proper attachment sets.  No claim is made
that an arbitrary three-connected exterior contains such a literal
`K_4`, or that an arbitrary `K_{4,4}` minor can be made literal while
preserving seven-connectivity.
