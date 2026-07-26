# Edge-maximal source contacts give a labelled one-defect `K_7` model

**Status:** computer-assisted finite result;
[separately audited GREEN](hc7_order8_edge_maximal_source_contact_audit.md).
The dependency-free verifier is
[`hc7_order8_edge_maximal_source_contact_verify.py`](hc7_order8_edge_maximal_source_contact_verify.py).

This is a conditional endpoint for the source-saturated response-column
branch.  Its hypothesis is **abstract** edge-maximality of the seven-vertex
contact graph.  Maximizing contacts among host-realizable labelled column
systems does not establish that hypothesis.

## 1. Finite theorem

### Theorem 1.1

Let `J` be a simple graph on the labelled vertex set

\[
                         \{t,c_0,c_1,c_2,c_3,c_4,q\}. \tag{1.1}
\]

Assume:

1. `t` is adjacent to all five vertices `c_0,...,c_4`;
2. `d_J(c_0)<=3`;
3. `J` has no `K_5` minor; and
4. adding any missing edge to `J` creates a `K_5` minor.

Then `d_J(c_0)=3`, `|E(J)|=15`, and `J-c_0` has a spanning `K_4`-minor
model

\[
                              B_1,B_2,B_3,B_4             \tag{1.2}
\]

such that `c_0` is adjacent to exactly three of the four branch sets.

### Proof by exhaustive verification

The five target--source edges are fixed and the other sixteen possible
edges vary, giving `2^16=65,536` labelled graphs.  The verifier:

1. checks `K_5`-minor containment by exhausting all `266` possible five-bag
   systems on subsets of the seven vertices;
2. retains exactly the `K_5`-minor-free graphs satisfying the degree and
   one-edge maximality hypotheses;
3. checks all `65` spanning four-partitions of `J-c_0` for (1.2) and the
   exact three-bag contact condition; and
4. canonicalizes the retained graphs under all permutations of the seven
   vertices as a reproducibility check.

The exact output is

```text
labelled_graphs 65536
edge_maximal_survivors 562
unlabelled_types 6
type_counts 007fff:10 00efff:192 01d7ff:120 01deff:84 05cdff:144 05defb:12
spanning_k4_failures 0
PASS order8_edge_maximal_source_contact
```

Every one of the `562` retained labelled graphs has fifteen edges and
`d_J(c_0)=3`; every one passes the required direct branch-set check.  The
six hexadecimal codes are canonical ordinary unlabelled graph encodings,
and their multiplicities sum to `562`. \(\square\)

## 2. Response-column consequence

### Corollary 2.1

Suppose `J` is the contact graph of seven connected columns dominated by
two disjoint adjacent connected roots, both roots being adjacent to every
column.  Under the hypotheses of Theorem 1.1, the host contains seven
pairwise disjoint connected branch sets which are pairwise adjacent except
for exactly one possible pair, and that missing pair is incident with the
column `c_0`.

#### Proof

Lift the four bags in (1.2) through unions of their literal columns.  The
column `c_0` is adjacent to exactly three of those four bags, so these five
sets form a five-branch-set system with exactly one missing adjacency,
incident with `c_0`.  Both roots are adjacent to all five sets and to one
another.  They complete the displayed seven-set one-defect model.
\(\square\)

The audited
[one-defect two-root completion/separation theorem](hc7_one_defect_two_root_k5_separator.md)
applies as follows.  Use the four bags in (1.2) together with one original
root as its `K_5` model.  Use `c_0` and the other original root as its two
adjacent roots.  The latter meets all five model bags, while `c_0` meets the
first original root and exactly three of the four bags, hence four model
bags in total.  The theorem therefore returns an explicit `K_7`-minor model
or a genuine full-neighbourhood separation.  The latter can have unbounded
order and carries no selected boundary response.

## 3. Trust boundary

The theorem does not prove that a response-column system can realize every
missing abstract contact, or that a host-maximal decorated system has an
abstractly edge-maximal contact graph.  It therefore does not close a dirty
bypass, bound the separation returned by the one-defect theorem, synchronize
a boundary partition, close the order-eight interface, or prove `HC_7`.

Its exact value is to identify the finite terminal shape after a future
dirty-path exchange reaches abstract edge-maximality: the missing adjacency
is attached to the same low-degree response source selected by the
operation.
