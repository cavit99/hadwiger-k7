# Independent audit of the incident-bypass conflict-compression barrier

## Verdict

**GREEN** for the exact source revision

```text
7f19e5c78a1a004f7624e24eb1e4bcdb86dece590c72560be7216a51f9f77691  barriers/hc7_incident_bypass_conflict_compression_barrier.md
```

This is a separate internal mathematical audit, not external peer review.
The construction realizes every prescribed nonempty bipartite conflict
graph and has the claimed colouring, Kempe-normalization, connectivity and
minor properties.  It is a barrier only to simplifying a coupled bypass by
central-colouring normalization; it is not a counterexample to the active
order-eight theorem or to `HC_7`.

## 1. Chromatic and response checks

The triangles `sar` and `arx` force `s` and every vertex of `X` to have one
colour in any hypothetical three-colouring of the base.  Symmetrically,
`sbp` and `bpy` force `s` and every vertex of `Y` to have one colour.  Since
`R` has an edge, this is impossible.  The displayed four-colouring proves
that the base is exactly four-chromatic, and joining the clique raises the
chromatic number to `q+1`.

After contracting the two marked incident edges, the displayed colouring
descends.  The contraction image, `r`, and any vertex of `X` form a triangle,
so the contracted base is exactly three-chromatic and the joined graph is
exactly `q`-chromatic.

The central colouring and the two named component switches realize the
three stated equality signatures.  A fourth, all-proper signature would
restore both marked edges and colour the original graph, so it is
impossible.  The central trace is exactly `{a,b}`.

## 2. Exact conflict graph and Kempe rigidity

The named components are exactly `A={a} union X` and `B={b} union Y`.
Their simultaneous switch makes all vertices of `X union Y` monochromatic,
and the resulting conflict edges are precisely the edges of `R`.  This
remains true when `R` is disconnected or has isolated vertices.

In any central colouring, the displayed triangles force the colours of
`X,Y,r,p` up to a swap of the two noncentral base colours.  The corresponding
two-colour subgraph is connected because `R` is nonempty.  Every
central-preserving Kempe interchange is therefore a global palette
permutation; interchanges on either central/noncentral pair leave the class
of central colourings.  Thus central-colouring minimization cannot simplify
the chosen bipartite graph.

## 3. Seven-connected terminal instance

The base for `R=K_{3,3}` remains connected after deleting at most three
vertices and has a vertex of degree four, so its connectivity is exactly
four.  Joining `K_3` makes the full graph seven-connected.  The four base
bags

```text
{s}, {a}, {r}, {b,x,y}
```

form a `K_4`-minor model for any edge `xy` of `K_{3,3}`.  The three joined
singleton vertices complete an explicit `K_7`-minor model.

## 4. Scope

The seven-connected example is already terminal through that `K_7` minor.
For conflict graphs with more than one edge the construction is not
minor-critical, and it does not realize the exact order-eight two-full-shore
column setting.  It therefore refutes only the proposed compression by
shortestness or Kempe normalization.  A positive theorem may still use
`K_7`-minor exclusion, the unit responses supplied by full minor-criticality,
or the latent-column labels.  No unresolved assumption remains within the
barrier's stated scope.
