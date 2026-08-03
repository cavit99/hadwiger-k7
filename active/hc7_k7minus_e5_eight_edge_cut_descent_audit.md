# Internal audit: descent from an eight-edge five-cut

**Verdict:** GREEN.

**Audited source:**
[`hc7_k7minus_e5_eight_edge_cut_descent.md`](hc7_k7minus_e5_eight_edge_cut_descent.md)

**Source SHA-256:**
`e3558243639d3da82d8bebc3c0aadbe829f2c494a04148d1e3d05cb2a6024ba7`

This is a separate internal mathematical audit, not external peer review.
The theorem is computation-free.  It proves a strict descent from the
eight-edge row; it does not eliminate every eight-edge cut.

## 1. The two partial completions are actual minors

The opposite component `D` is connected and adjacent to all five boundary
vertices.  An `x`--`y` path through `D` can therefore be contracted to
realise the single virtual edge `xy`, with unused material deleted.  Thus

```text
G[C union S]+xy
```

is an actual proper minor.  Its edge count is exactly

```text
4|C|+delta_S(C)+9,
```

so the high-excess hypothesis places it at the `E5` threshold.  Since it
is target-free and smaller than `G`, failure of five-connectivity follows
from the definition of a minimum `E5` enemy.  The same verification
applies after adding only `zw`.

## 2. The separators have exactly one interior vertex

In the first partial completion, every component remaining after deletion
of a separator of order at most four contains a surviving boundary
vertex.  Otherwise a nonempty subset of the old component `C` would have
at most four neighbours in `G`.

The boundary induces `K_5-zw`.  It can be split between two components
only when precisely `z,w` survive, so the separator contains `{x,y,t}`.
The set `{x,y,t}` alone cannot separate `z,w`, because `C` is connected
and full to both.  Hence the separator is exactly `{x,y,t,p}` for some
`p in C`, and `p` meets every `z`--`w` path through `C`.  The symmetric
completion gives `{z,w,t,q}`, where `q` meets every `x`--`y` path.

The linked paths in `C` are vertex-disjoint, so `p!=q`.  For a component
`L` of `C-p`, its possible neighbourhood is contained in
`S union {p}` and omits at least one of `z,w`.  Five-connectivity forces
the exact five-set

```text
{p,x,y,t,z}       or       {p,x,y,t,w}.
```

Any component not containing `q` would consequently supply an
`x`--`y` path avoiding `q`; therefore `C-p` is connected.  The symmetric
argument proves that `C-q` is connected.  Relabelling the two missing
pairs then gives the exact one-neighbour assertions
`N_C(w)={p}` and `N_C(y)={q}`.

## 3. The new set is an actual component behind an order-five cut

For

```text
R=C-{p,q},             Q={p,q,x,z,t},
```

the set `R` is nonempty: a two-vertex `C` has at most eleven
internal-or-boundary edges and hence excess at most three.

Every component `L` of `G[R]` has no neighbour at `y` or `w` and no
neighbour outside the old closed side.  Thus `N_G(L) subseteq Q`, and
five-connectivity gives equality.  Each such `L` is consequently an
actual component of `G-Q`, not merely a component of an induced auxiliary
graph.

All remaining vertices lie in one other component: the old component `D`
is full and connected, and joins `y` to `w`.  Hence the number of
components of `G-Q` is one more than the number of components of `G[R]`.

The exclusions used to prove that `R` is connected were checked at their
exact scopes:

- two components of `G[R]` give three components behind `Q`, while
  `G[Q]` contains the literal triangle `xzt`, contradicting the
  three-component triangle-free theorem;
- three components give the separately eliminated four-component case;
- four components give the eliminated five-component case;
- at least five components give six full components behind a five-cut.

In the last case the displayed seven branch sets are connected and
disjoint.  Fullness supplies every required adjacency except possibly the
one between the last two whole components, so this is an explicit
`K_7^-` model.

## 4. Boundary size and exact excess transfer

The new cut has at most eight boundary edges.  Ten edges, together with
the two full components, give five boundary singleton bags and two whole
component bags.  Nine edges is the already eliminated `K_5^-` boundary.

The edge calculation was independently recomputed.  In the old closed
side,

```text
d(y)=4 with neighbours z,w,t,q,
d(w)=4 with neighbours x,y,t,p.
```

Deleting `y,w` removes seven edges.  Therefore

```text
|E(G[R union Q])|=4|R|+delta_S(C)+9
                  =4|R|+delta_Q(R)+|E(G[Q])|,
```

and hence

```text
delta_Q(R)=delta_S(C)+9-|E(G[Q])|.                    (1)
```

If the new boundary again has eight edges, (1) makes `R` the high-excess
component in the exact independent-miss configuration of the existing
eight-edge theorem.  Its other component has excess at most one, so `R`
is the component supplying the two disjoint paths.  The descent can
therefore be repeated.  Each repetition lowers the component order by
two and preserves nonemptiness, so it terminates.  At termination the
boundary has at most seven edges, and (1) shows that the excess has risen
by at least one from the original value.

## 5. Quantifier and scope check

The minimum-component corollary minimises over **all** order-five cuts and
all components satisfying `delta>=q+4`.  If such a minimiser had an
eight-edge boundary, the strict descent would contradict its choice.

It would be invalid to minimise only among eight-edge boundaries, because
the descended boundary may have at most seven edges.  It would also be
invalid to conclude that no eight-edge cut exists.  The source states
neither claim: it concludes only that a globally minimum high-excess
component has boundary size at most seven.  This is the exact proved
frontier.

## 6. Dependencies

The audit uses the written results in:

- `hc7_k7minus_e5_k5minus_cut_elimination.md`: elimination of a
  `K_5^-` boundary, the exact eight-edge two-component reduction, the
  five-component exclusion, and the three-component triangle-free
  theorem;
- `hc7_k7minus_e5_independent_four_component_elimination.md`: elimination
  of the four-component case.

No finite enumeration, solver, or unretained certificate is a dependency.
