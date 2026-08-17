# Elimination of the returned order-two dense lobe

**Status:** computer-assisted finite theorem with two independent exact
verifiers; adjacent independent cold audit GREEN.  The theorem applies to
components of arbitrary opposite order because that component is contracted
to one vertex.  It eliminates outcome 1 of the active returned two-component
descent, but does not eliminate its boundary-atom or nested-separator
outcomes and does not prove the universal six-connected `4n` theorem,
Conjecture 21, or `HC_7`.

Write `K_7^-` for the graph obtained from `K_7` by deleting one edge.

## Theorem 1 (order-two dense-lobe elimination)

Let `G` be a finite simple graph, let `S` be a set of six vertices, and
suppose that

\[
                       G-S=A\mathbin{\dot\cup}B,
\]

where `A,B` are the two components of `G-S`.  Suppose that both components
are adjacent to every vertex of `S`, and that

\[
                         A=\{x,y\},\qquad xy\in E(G).
\]

Put

\[
 e_S=|E(G[S])|,
 \qquad p=|E_G(A,S)|.
\]

If

\[
                    9\le e_S\le11,
             \qquad p\ge21-e_S,                       \tag{1}
\]

then `G` contains a `K_7^-` minor.

### Proof

Contract the connected component `B` to a vertex `b`, and retain
`S\cup\{x,y,b\}`.  The resulting nine-vertex minor `Q` has the following
edges:

1. the arbitrary `e_S` edges of `G[S]`;
2. the edge `xy`;
3. all six edges from `b` to `S`; and
4. the `p` edges from `\{x,y\}` to `S`.

There are no edges from `b` to `x` or `y`.  Fullness of `A` says that every
vertex of `S` is adjacent to at least one of `x,y`.

We first justify reducing (1) to equality.  If `d` vertices of `S` are
adjacent to both `x` and `y`, then

\[
                              p=6+d.                  \tag{2}
\]

The lower bound in (1) is therefore `d\ge15-e_S`.  Choose exactly
`15-e_S` of the doubly adjacent vertices.  At every other doubly adjacent
vertex, delete one of its two edges to `\{x,y\}`.  Every boundary vertex
still has a neighbour in `A`, and the resulting spanning subgraph `Q_0` of
`Q` satisfies

\[
                 |E_{Q_0}(\{x,y\},S)|=21-e_S.        \tag{3}
\]

It is enough to find the target in `Q_0`, since adding back edges cannot
destroy a minor.  Thus the inequality case is covered rigorously by
monotonicity; it is not omitted from the finite verification.

It remains to check the labelled equality profiles.  For fixed `e_S`, the
boundary graph has `\binom{15}{e_S}` choices.  Equation (3) says that
exactly `e_S-9` vertices of `S` are adjacent to only one of `x,y`; choose
those vertices and, independently, which endpoint sees each one.  Hence the
number of profiles is

\[
 \binom{15}{e_S}\binom6{e_S-9}2^{e_S-9}.             \tag{4}
\]

The three rows are

| `e_S` | boundary graphs | attachment strings | profiles |
|---:|---:|---:|---:|
| 9 | `5,005` | `1` | `5,005` |
| 10 | `3,003` | `12` | `36,036` |
| 11 | `1,365` | `60` | `81,900` |
| **total** |  |  | **`122,941`** |

For each profile, both exact verifiers find seven pairwise disjoint,
nonempty, connected branch sets with at most one nonadjacent pair.

The first verifier starts from the nine singleton bags and recursively
performs every possible deletion of a bag and merger of two touching bags.
Every state therefore consists of disjoint connected bags.  Conversely,
every minor model is reached by contracting a spanning tree in each branch
set and deleting unused vertices.  At seven bags the verifier accepts
exactly when at most one of the twenty-one bag pairs is nonadjacent.

The independent verifier does not recurse through minor operations.  It
directly generates every partition of every subset of order seven, eight,
or nine into seven nonempty bags.  There are

\[
 \binom97 S(7,7)+\binom98 S(8,7)+\binom99 S(9,7)
 =36+252+462=750                                      \tag{5}
\]

such partitions.  It tests connectedness of every bag and all twenty-one
interbag adjacencies.  Both searches return a `K_7^-` certificate in all
`122,941` profiles.  This proves the theorem within the displayed finite
trust boundary.  \(\square\)

## Corollary 2 (removal of outcome 1 in the returned descent)

In the setting of
[`Theorem 6`](hc7_k7minus_returned_two_component_contraction_descent.md#theorem-6-dense-returned-row-descent)
of the returned two-component six-cut descent, outcome 1 cannot occur.
Consequently, when `e_S\ge3`, that theorem may be sharpened to the following
two outcomes:

1. there is a one- or two-vertex boundary atom satisfying its displayed
   conditions (8)--(9); or
2. `G` has a spanning exact `K_7^\vee` model from which the near-model
   descent returns a proper connected part of a neutral branch set whose
   open neighbourhood is an actual separator of order at least six.

### Proof

Outcome 1 of the cited theorem supplies a selected component `C` which is
an edge of order two, together with

\[
               9\le e_S\le11,
       \qquad |E_G(C,S)|\ge21-e_S.

The standing hypotheses of that note say that the opposite component and
`C` are both connected and adjacent to every member of the six-set `S`.
These are exactly the hypotheses of Theorem 1, which gives the forbidden
`K_7^-` minor.  Hence only outcomes 2 and 3 of the cited theorem remain.
\(\square\)

## Reproducibility

The two verifiers and their roles are documented in
[`active/experiments/returned_order_two_dense_lobe_elimination/`](experiments/returned_order_two_dense_lobe_elimination/README.md).
Run:

```text
python3 active/experiments/returned_order_two_dense_lobe_elimination/recursive_verify.py

g++ -O3 -std=c++20 \
  active/experiments/returned_order_two_dense_lobe_elimination/partition_verify.cpp \
  -o /tmp/returned_order_two_dense_lobe_partition_verify
/tmp/returned_order_two_dense_lobe_partition_verify
```

The expected census is

```text
eS=9 checked=5005 positive=5005
eS=10 checked=36036 positive=36036
eS=11 checked=81900 positive=81900
total=122941
```

Both programs include positive and negative controls.  Source hashes and
the recursive certificate digest from a clean rerun are

```text
recursive_verify.py
  SHA-256 929ca03af1c5404b659b0391b9fe089acd414dfebe8f93117fe3ac02d1c682df
partition_verify.cpp
  SHA-256 1c44627c6ec673efefd38d9b31584b68f8e36defb3b77530c58761ab4337407c
recursive certificate digest
  SHA-256 c90f0ffb52a2ee94b30d0d249e048b5501f97d4f34fdf291874780fab968370c
```

## Exact scope

The unbounded content is the contraction of an arbitrary connected
opposite component to the universal boundary pole `b`.  The finite trust
boundary is only the resulting nine-vertex quotient.  No bound is placed on
the order or internal structure of `B`.

The theorem removes the dense order-two lobe.  It does not eliminate the
one- or two-vertex **boundary** atom in the other outcome of the returned
descent, control the order or coefficient-four excess of the nested
separator, or treat the sparse `e_S\le2` row.
