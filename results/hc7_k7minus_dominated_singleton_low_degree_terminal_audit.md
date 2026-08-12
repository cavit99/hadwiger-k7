# Separate internal audit: low-degree dominated-singleton completion

**Verdict:** **GREEN.**  The finite marked-neighbourhood classification,
its exterior-component completion, and the lift to model-persistent edges
at vertices of degrees eight and nine are correct at the pinned revision.
Together with the audited high-degree result, the stated all-degree
component-alignment corollary follows.  This is a conditional reduction; it
does not eliminate the resulting response side or prove the `K_7^-`
six-colour conjecture or `HC_7`.

This is a separate internal mathematical and computational audit, not
external peer review.

## Exact revisions

| Item | SHA-256 |
|---|---|
| [`hc7_k7minus_dominated_singleton_low_degree_terminal.md`](hc7_k7minus_dominated_singleton_low_degree_terminal.md) | `d5c3fa4bcfb43af83d617d4022fa151bdb445240c2a152df74fb5bf178f7f779` |
| [`README.md`](../active/experiments/dominated_singleton_low_degree_completion/README.md) | `e0069c0d4a851e1d5343d31831da020d6b9a98e842d5354c2b7906a33bea7fe1` |
| [`verify.py`](../active/experiments/dominated_singleton_low_degree_completion/verify.py) | `81980e29daba936ace8e599a1147ffad233a227718247cce8872cadbbe9d4495` |

The final source change before pinning added only repository-relative links
to this audit and its verifier materials.

## 1. Finite enumeration and exact minor test

The verifier uses nauty's `geng -t` to enumerate all unlabelled
triangle-free graphs of orders seven and eight.  Its graph6 decoder was
cross-checked against nauty's `showg` on both surviving encodings.  It then
computes the independence number exactly and rejects a graph precisely when
an edge-deletion/contraction recursion finds a five-vertex minor with at
least nine edges.  A five-vertex graph with at least nine edges contains
`K_5^-` as a subgraph, so this is an exact `K_5^-`-minor test.

For each eligible graph the script enumerates every vertex set of order at
most two whose deletion leaves at least two components.  It tests all
singleton markings at order seven and all two-vertex markings at order
eight.  Thus its survivor condition is exactly

\[
              M\subseteq S\quad\hbox{for every cut }S
              \hbox{ of order at most two},
\]

including the empty cut when the graph is disconnected.  The independently
rerun computation returned

```text
GREEN dominated-singleton low-degree completion
order7 eligible=9 marked=63 survivors=2 graph6=FCxv? exterior_profiles=9
order8 eligible=158 marked=4424 survivors=1 graph6=G?rF`w exterior_profiles=46
```

For `FCxv?`, the only cut of order at most two is `{0,5}`; the graph is
`K_{3,3}` with one edge subdivided, and the two surviving singleton
markings are its automorphic cut vertices.  For ``G?rF`w``, the only such
cut is `{6,7}`, which is also the unique surviving marked pair.  These facts
were recomputed directly from the decoded graphs.

The minor recursion is exact for the exterior completion as well.  Once
the graph has seven vertices, having at least twenty edges is equivalent to
containing `K_7^-` as a subgraph; the deletion/contraction recursion
therefore tests precisely for a `K_7^-` minor.  The positive and negative
controls pass.  The verifier now refuses optimised Python execution, so its
assertion-based proof checks cannot be disabled with `python -O`.

## 2. Independence bounds and persistent endpoints

At degree eight, literal `K_5` exclusion makes `u` exceptional.  The
audited exceptional-neighbourhood theorem gives
`alpha(G[N(u)])=3`.  Since `v` is complete to `Q`, adjoining `v` cannot
increase a nontrivial independent set, and hence `alpha(Q)=3`.

At degree nine, Dirac's contraction-critical neighbourhood bound gives

\[
          \alpha(Q)\le \alpha(G[N(u)])\le d_G(u)-5=4.
\]

For the fixed spanning labelled exact `K_7^vee` model, at most one edge
`ux` can be the unique attachment of `u` to `R-u`.  For each required
foreign label, at most one can be the unique branch-set adjacency.  If the
label of `R` has degree at most five, these account for at most six edges.
If it has degree six, the named foreign branch set anticomplete to `u`
removes one of the six foreign possibilities, again leaving at most five
foreign essential edges and one internal edge.  Consequently at least one
endpoint is persistent when `|Q|=7`, and at least two are persistent when
`|Q|=8`.

Unless such a marking is one of the finite exceptions, some cut of order at
most two omits a marked endpoint.  The component containing that endpoint
therefore supplies exactly the model-persistent side asserted in Theorem
2.1.  Deleting its incident edge preserves the displayed branch sets, and
the present triangle through `u,v,x` makes the two equality signatures
exclusive.  The colouring in which `ux` is the unique monochromatic edge
restricts properly outside the component and gives the claimed rejected
boundary partition.

## 3. Exterior-component lift

The exceptional cases have a genuine exterior component.  For the cut
supplied by the dominated-singleton theorem, every component of `Q-S` has
at least `5-|S|`, and hence at least three, neighbours in
`O=G-N[u]`.  Thus `O` is nonempty without an additional order hypothesis.

For a component `C` of `G[O]`, no edge joins `C` to another component of
`O`, and no vertex of `C` is adjacent to `u`.  Hence

\[
                N_G(C)\subseteq \{v\}\cup V(Q).
\]

This neighbourhood separates `C` from `u`; seven-connectivity gives at
least seven distinct neighbours.  Contracting `C`, deleting other exterior
vertices, and retaining `Q,u,v` therefore gives exactly one of the finite
augmented profiles tested by the verifier.  There are nine possible miss
sets at order seven and forty-six at order eight, and all contain a
`K_7^-` minor.  The finite computation is consequently lifted only after
the host has already reduced the neighbourhood to orders seven or eight;
no unbounded search limit is being assumed.

## 4. Scope

The proof establishes one model-persistent endpoint outside one
common-neighbour cut at every degree.  It does not bound the returned
boundary above, choose persistent endpoints in two different components,
or align one boundary partition across both sides.  No further hidden
assumption or unsupported inference was found in the stated result.
