# Bipartite schemes can require expansion of both root shores

**Status:** barrier/counterexample to an intermediate claim, with a written
proof. This is not a counterexample to bipartite contractibility.

## Refuted statement and scope

The following proposed normal form is false:

> In every coloured scheme of a bipartite graph, there is a rooted model
> in which every root in at least one of the two bipartition classes is a
> singleton branch set.

The counterexamples below permit arbitrary colour mixing and omitted
vertices in the other branch sets. Consequently, they also refute the
stronger versions which connect complete colour classes, or connect only
their roots and required terminal neighbours by disjoint projected trees.
Choosing the more favourable shore does not repair the statement.

They do not refute a model construction which expands roots on both shores,
or a root-preserving reduction followed by a singleton-shore construction:
lifting such a reduction may expand the original roots.

## Theorem

For every integer `n>=3`, there is a graph `G_n` on `2n^2+6n` vertices
and `9n^2` edges containing a coloured `K_{n,n}`-scheme and an explicit
rooted `K_{n,n}` minor, but no rooted `K_{n,n}` model in `G_n` leaves
either whole root shore singleton.

Here a coloured scheme has the meaning in
[the even-subdivision theorem](../results/even_subdivision_contractibility.md):
each target edge has a path between its roots using just their two colours;
the colouring is proper, fixes every root, and every nonroot has degree at
least four. The paths satisfy the scheme intersection condition.

### Construction

All indices are in `Z/nZ`. The target roots are `a_i,b_j`. Distinct symbols
below denote distinct vertices. The colour classes are

\[
 A_i=\{a_i,Y_i,Z_i\}\cup\{x_{ik}:k\in\mathbb Z/n\mathbb Z\},
 \qquad
 B_j=\{b_j,y_j,z_j\}\cup\{X_{jk}:k\in\mathbb Z/n\mathbb Z\}.
\]

Let `G_n` be the union of the paths

\[
 P_{ij}=
 a_i\,X_{j,i+1}\,Z_i\,X_{ji}\,Y_i\,y_j\,
 x_{ij}\,z_j\,x_{i,j+1}\,b_j.
 \tag{1}
\]

Every path is simple and alternates its two endpoint colours. Each edge is
in precisely one path. A vertex of colour `a_i` occurs only on paths with
first index `i`, and a vertex of colour `b_j` only on paths with second
index `j`. Thus any collection of paths with a common vertex has target
edges with a common endpoint. The vertices `x_{ik},X_{jk}` occur on exactly
two paths and have degree four. The vertices `Y_i,Z_i,y_j,z_j` occur on
`n` paths and have degree `2n`. This verifies the coloured scheme and the
claimed vertex and edge counts.

### No model keeps all `a_i` singleton

Suppose such a model exists, with branch sets `C_{b_j}` for the other roots.
The root neighbourhoods

\[
 N(a_i)=\{X_{j,i+1}:j\in\mathbb Z/n\mathbb Z\}
 \tag{2}
\]

are `n` disjoint sets, each of order `n`. Every one of the `n` branch sets
`C_{b_j}` must meet every set in (2). Disjointness therefore forces each
branch set to contain precisely one `X` vertex of every second index,
and exhausts all `n^2` vertices of the form `X_{jk}`.

Put `S={Y_i,Z_i:i in Z/nZ}`, so `|S|=2n`, and fix one branch set `C`.
Its `n` selected `X` vertices have no neighbours in `C` outside `S`:
their only other neighbours are the roots `a_i`, which are unavailable.
A vertex `Z_i` sees only `X` vertices of second indices `i,i+1`, and so
sees at most two selected `X` vertices. A vertex `Y_i` sees only `X`
vertices of second index `i`, together with vertices outside `S` and the
set of all `X` vertices. There are no edges within `S`.

Identify all vertices of `C` outside `S` and the selected `X` vertices
with one auxiliary vertex `r`. This set is nonempty because it contains
the root of `C`. Its identification preserves connectivity; no assertion
that the identified set is connected, or that this identification is a
minor operation, is needed. Delete resulting loops and parallel edges.
If `s=|C cap S|`, the resulting connected graph has `n+s+1` vertices.
Every edge has one endpoint in `C cap S`, and each such vertex has degree
at most two. Its number of edges is therefore at most `2s`. Connectivity
requires at least `n+s` edges, giving `s>=n`.

The `n` disjoint branch sets would consequently use at least `n^2` distinct
vertices of `S`. This contradicts `|S|=2n` for `n>=3`.

### No model keeps all `b_j` singleton

The same argument uses
`N(b_j)={x_{i,j+1}:i in Z/nZ}` and the separator
`{y_j,z_j:j in Z/nZ}`. Each opposite branch set contains one `x` vertex
of every second index and requires at least `n` separator vertices.
Again `n^2>2n` gives a contradiction.

### An explicit rooted model

For each `i`, take the prefix of `P_{ii}` from `a_i` through `Y_i` as
`C_{a_i}`. For each `j`, take the suffix of `P_{jj}` from `y_j` through
`b_j` as `C_{b_j}`. These `2n` paths are pairwise disjoint: within either
half they come from matching target edges, and the two halves use disjoint
symbols. They contain their prescribed roots. Every `Y_i y_j` is an edge
by (1), providing all required adjacencies. This proves the theorem. QED

## Verification

The [deterministic certificate checker](../active/experiments/bipartite_contractibility/singleton_shore_obstruction.py)
constructs the graph, checks all coloured-scheme conditions, verifies the
neighbourhood partition and the degree bound in the identification argument,
and checks the explicit rooted model. Its `--json` output lists all colours,
scheme paths, branch sets and obstruction data.

```text
uv run python3 active/experiments/bipartite_contractibility/singleton_shore_obstruction.py --order 3
uv run python3 active/experiments/bipartite_contractibility/singleton_shore_obstruction.py --order 4
uv run python3 active/experiments/bipartite_contractibility/singleton_shore_obstruction.py --order 5
```

Expected graph orders are `36,56,80`, with `81,144,225` edges respectively.
These are finite checks of the construction; the theorem for all `n>=3`
is established by the written argument above.
