# Elimination of the final seven-edge returned boundary

**Status:** proved and independently audited.  The computer-assisted finite
result is reproduced by a deterministic standard-library verifier and an
independent graph-state verifier.

Write `K_7^-` for the graph obtained from `K_7` by deleting one edge.  A
component of `G-S` is **full** at `S` if it has a neighbour at every vertex of
`S`.

## Theorem 1 (type-VII elimination)

Let `G` be a six-connected graph with no `K_7^-` minor.  There is no vertex
cut

\[
 S=\{0,1,2,3,4,5\}
\]

such that `G-S` has exactly three components, all full at `S`, and

\[
 E(G[S])=\{01,02,03,14,24,35,45\}.                 \tag{1}
\]

Thus the last seven-edge boundary left by the dense-boundary theorem is
eliminated, with no restriction on the orders of the three components.

The proof uses the following sharpening of the rooted estimate.

## Lemma 2 (two-edge four-root bound)

Let `H` be a graph, let `Z` be a set of four vertices, and suppose that

- `(H,Z)` is internally four-connected;
- `H` has no `Z`-rooted `K_4` model;
- `|V(H)|\ge7`; and
- `|E(H[Z])|\le2`.

Then

\[
                         |E(H)|\le3|V(H)|-9.         \tag{2}
\]

### Proof

Apply Norin--Totschnig Theorem 8, and inspect their proof of Lemma 9.  The
rooted-model outcome is excluded by hypothesis, and internal
four-connectivity excludes the separation outcome.

In the trisection outcome, the proof of Lemma 9 first shows that each of the
two parts outside the central part consists of one root.  If the central part
has at most four vertices, then `|V(H)|\le6`, contrary to the hypothesis.
The remaining, inductive, trisection branch gives
`|E(H)|\le3|V(H)|-9` exactly as in that proof.

It remains to consider the planar outcome.  The graph `H` is connected:
otherwise a component containing a non-root, or a root-free component,
gives a separation of `(H,Z)` of order at most three.  Let `\lambda` be the
length of the boundary walk of the outer face in the drawing supplied by
Theorem 8.  All four roots occur on this walk.  If `\lambda\le5`, four
distinct marked positions on a cyclic walk of length at most five contain
at least three consecutive marked pairs.  These give three distinct edges
of `H[Z]`, a contradiction.  Hence `\lambda\ge6`.  Euler's formula and the
fact that every bounded face has length at least three give

\[
 |E(H)|\le3|V(H)|-3-\lambda\le3|V(H)|-9.
\]

This proves the lemma. `\square`

## Lemma 3 (the finite `K_2` quotients)

Let `B` be the graph in (1).  The following two classes of graphs contain a
`K_7^-` minor.

1. Add an edge `xy`, two further vertices adjacent to all six vertices of
   `B`, and no other vertices.  Suppose each of `x,y` has at least five
   neighbours in `B`, every vertex of `B` has a neighbour in `\{x,y\}`, and
   both `1` and `2` are adjacent to both `x` and `y`.
2. Add two disjoint edges `x_1y_1,x_2y_2`, one further vertex adjacent to
   all six vertices of `B`, and no other vertices.  For `i=1,2`, suppose
   each end of `x_i y_i` has at least five neighbours in `B` and every
   vertex of `B` has a neighbour in that edge.  Suppose `1` is adjacent to
   both ends of the first edge but `2` is not, while `2` is adjacent to both
   ends of the second edge but `1` is not.

### Finite verification

For a fixed edge, fullness leaves three choices at each boundary vertex:
only its first end is adjacent, only its second end is adjacent, or both
are adjacent.  The endpoint degree conditions leave 21 patterns in the
first class.  They leave 10 patterns for each designated edge in the second
class, hence 100 ordered pairs.  Exact deletion and contraction find and
validate a seven-branch-set model with at least 20 of the 21 possible
contacts in every one of the 121 graphs.

The verifier cited below enumerates all these patterns.  Its target oracle
starts with singleton branch sets and recursively performs every possible
edge contraction and vertex deletion.  Conversely, every minor model is
obtained by contracting a spanning tree in each connected branch set and
deleting the unused vertices.  The search is therefore exact.  Each returned
model is checked independently for disjointness, connectedness and at least
20 pairwise contacts.  Positive and negative seven-vertex controls test the
target encoding.  The serialised branch-set certificates have SHA-256 digest

```text
88bef0aaee0914ff2b71cc4e00d7b55e8d4a42c274294d8418d37da646805fe6
```

This proves the finite lemma. `\square`

## Proof of Theorem 1

Fix a component `C` of `G-S`, and put

\[
 c=|C|,\qquad e=|E(G[C])|,\qquad
 a_i=|E_G(C,\{i\})|,\qquad P=\sum_{i=0}^5a_i.       \tag{3}
\]

Suppose first that `c\ge3`.  Put `Z=S-\{0,5\}`.  The pair
`(G[C\cup Z],Z)` is internally four-connected: a rooted separation of
order at most three, together with `0,5`, would give a cut of `G` of order
at most five, with either of the other two components on the opposite side.

There is no `Z`-rooted `K_4` model.  If there were one, let `D,E` be the
other two components.  Its four rooted branch sets, together with

\[
                         D\cup\{5\},\qquad E,\qquad\{0\},       \tag{4}
\]

would form a `K_7^-` model.  Indeed, fullness supplies all contacts involving
`D` or `E`; vertex `0` has its three boundary neighbours in `Z` and hence
misses at most one rooted branch set.  This contradicts the hypothesis on
`G`.

The graph induced by `Z=\{1,2,3,4\}` has precisely the two edges `14,24`.
Lemma 2, applied to the graph on `C\cup Z`, therefore gives

\[
                         e+P-a_0-a_5\le3c+1.         \tag{5}
\]

Repeat the argument with `Z=S-\{3,4\}`.  Now vertex `4` is the cubic root,
`34` is absent, and the root graph has precisely the two edges `01,02`.
Thus

\[
                         e+P-a_3-a_4\le3c+1.         \tag{6}
\]

Adding (5) and (6) yields

\[
 2e+(a_0+a_3+a_4+a_5)+2(a_1+a_2)\le6c+2.           \tag{7}
\]

Six-connectivity gives minimum degree at least six.  Summing the degrees
inside `C` gives

\[
 2e+(a_0+a_3+a_4+a_5)+(a_1+a_2)\ge6c.              \tag{8}
\]

Subtracting (8) from (7) gives `a_1+a_2\le2`.  Fullness gives the reverse
individual bounds, so

\[
                              a_1=a_2=1.             \tag{9}
\]

Equation (9) also holds when `c=1`, by simplicity and fullness.  Consequently
only a component of order two can have both its vertices adjacent to `1` or
both adjacent to `2`.  Such a component is an edge.

Both `1` and `2` have degree two in `B`.  Their degree in `G` is at least six,
so each receives at least four incident edges from the three components.
Fullness contributes a baseline of three.  Hence some order-two component
has both vertices adjacent to `1`, and some order-two component has both
vertices adjacent to `2`.

If one component has both properties, retain that edge and contract each of
the other two full components to one vertex.  Each end of the retained edge
has its mate and therefore, by minimum degree, at least five boundary
neighbours.  The resulting minor belongs to the first class of Lemma 3.

Otherwise the two components are distinct.  Retain their two edges and
contract the third full component.  The first retained edge is doubled at
`1` but not at `2`, and the second is doubled at `2` but not at `1`; again
each endpoint has at least five boundary neighbours.  This is the second
class of Lemma 3.

In either case Lemma 3 gives a `K_7^-` minor of `G`, a contradiction.  This
proves the theorem. `\square`

## Verification and scope

Run

```text
python3 -B results/hc7_k7minus_returned_type_vii_elimination_verify.py
```

Expected output:

```text
GREEN returned type-VII quotient elimination
same_component_feasible_profiles=21
split_component_first_profiles=10
split_component_second_profiles=10
split_component_profile_pairs=100
target_certificates=121
certificate_digest=88bef0aaee0914ff2b71cc4e00d7b55e8d4a42c274294d8418d37da646805fe6
```

Together with the preceding dense-boundary theorem, Theorem 1 eliminates
every seven- or eight-edge boundary in the returned three-component case.
It does not address boundaries with at most six edges or the returned
two-component case.

## External source

Sergey Norin and Agnès Totschnig,
*Every graph with no `K_7^\vee`-minor is 6-colorable*, Theorem 8 and the
proof of Lemma 9,
[arXiv:2507.03244](https://arxiv.org/abs/2507.03244).
