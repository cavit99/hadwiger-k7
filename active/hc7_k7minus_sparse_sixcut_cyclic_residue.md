# The cyclic residue of a sparse returned six-cut

**Status:** written proof; adjacent independent cold audit GREEN.  This is
a corollary of the audited four-root carrier-packing theorem.  It bounds every tree lobe
by an absolute constant and shows that an unbounded lobe must have
linearly growing cycle rank.  It does not bound the excess of a cyclic
lobe or eliminate the sparse three-component case.

Let `G` be a six-connected graph with no `K_7^-` minor, let `S` be a
six-vertex cut, and suppose that `G-S` has at least three components.  Fix
a component `C` of `G-S`.  Put

```text
c=|C|,
beta(C)=|E(G[C])|-c+1,
a(v)=|N_G(v) cap S|  for v in C.
```

Thus `beta(C)` is the cyclomatic number of the connected graph `G[C]`.

## Theorem 1 (order versus cycle rank)

Every component `C` satisfies

```text
c <= 28+2 beta(C).                                  (1)
```

If `Delta(G[S])>=2`, then the stronger bound

```text
c <= 25+2 beta(C)                                   (2)
```

holds.  In particular, a nontrivial tree component has at most `22`
vertices in general and at most `19` vertices when
`Delta(G[S])>=2`.

### Proof

The audited four-root carrier-packing theorem gives

```text
sum_{v in C} binom(a(v),4) <= 30.                    (3)
```

If `Delta(G[S])>=2`, a boundary vertex and two of its neighbours span a
three-set with at least two edges.  The sharpened form of the same theorem
then gives

```text
sum_{v in C} binom(a(v),4) <= 27.                    (4)
```

Six-connectivity implies minimum degree at least six.  Since `C` is a
component of `G-S`, every `v in C` therefore satisfies

```text
d_C(v)+a(v)=d_G(v)>=6.                               (5)
```

Assume first that `c>=2`.  Let `n_1,n_2`, and `h` denote respectively
the numbers of vertices of internal degree one, internal degree two, and
internal degree at least three.  Every vertex counted by `n_1` has
`a(v)>=5`, and every vertex counted by `n_2` has `a(v)>=4`.

From (3), a vertex with `a(v)>=5` contributes at least five and a vertex
with `a(v)>=4` contributes at least one.  Since the two classes are
disjoint, the joint inequality is

```text
5n_1+n_2<=30.                                        (6)
```

Under (4), this improves to

```text
5n_1+n_2<=27.                                        (7)
```

The degree identity for a connected graph gives

```text
sum_{v in C}(d_C(v)-2)=2 beta(C)-2.
```

The vertices of degree one contribute `-n_1`, the degree-two vertices
contribute zero, and each of the `h` remaining vertices contributes at
least one.  Consequently

```text
h<=2 beta(C)-2+n_1.                                  (8)
```

Combining (6) and (8),

```text
c=n_1+n_2+h
 <=2n_1+n_2+2 beta(C)-2
 <=28+2 beta(C),
```

which proves (1).  Combining (7) and (8) instead gives

```text
c<=25+2 beta(C),
```

which proves (2).  The case `c=1` satisfies both inequalities directly.
If `C` is a nontrivial tree, then `beta(C)=0` and `n_1>=2`.  Retaining
the `-3n_1` discarded above gives

```text
c<=30-3n_1-2<=22,
```

and under (7) it gives `c<=27-3n_1-2<=19`.  This proves the stated tree
bounds.  \(\square\)

## Consequence

In the remaining sparse three-component row, unbounded lobe order cannot
come from trees or from graphs of bounded cyclomatic number.  More
precisely, when `Delta(G[S])>=2`,

```text
beta(C) >= ceil((c-25)/2),
```

and without that boundary hypothesis the analogous lower bound is
`ceil((c-28)/2)`.  Thus every unbounded residue has linearly many
independent cycles; this is the part still requiring a genuinely cyclic
packing or excess argument.

## Dependency

The only non-elementary input is the
[four-root carrier-packing theorem](hc7_k7minus_sparse_sixcut_four_root_carrier_packing.md),
source SHA-256
`adfcc70aca8543e15bcf7e94e1fb310492535f8155f02cb5a5430adba4ce8372`,
with adjacent GREEN cold-audit SHA-256
`4a185697d20ed73c358703eb7d433c3555bca6474497a011630d3805dc493e97`.
