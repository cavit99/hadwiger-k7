# Seven paths between two bad degree-eight vertices do not force `K_7^-`

**Status:** explicit barrier/counterexample to an intermediate claim;
deterministic verifier retained.  This is not a counterexample to the full
seven-connected contraction-critical target or to `HC_7`.

## Refuted statement

The following implication is false:

> Two nonadjacent degree-eight vertices with `K_4`-free neighbourhoods of
> independence number three, together with seven internally disjoint paths
> between them, force a `K_7^-` minor.

## Construction

Use the vertices

\[
 \{u,v,p,q,x_1,x_2,y_1,y_2,y_3,z_1,z_2\}.
\]

Join `u` to

\[
 p,x_1,x_2,y_1,y_2,y_3,z_1,z_2,
\]

and join `v` to the same seven vertices other than `p`, with `q` in place
of `p`.  Add the edges of the triangles

\[
 \{p,x_1,x_2\},\qquad \{q,x_1,x_2\},\qquad
 \{y_1,y_2,y_3\},
\]

and the edge `z_1z_2`; add no others.

Then `u,v` are nonadjacent and both have degree eight.  Their neighbourhoods
induce

\[
                              K_3\mathbin{\dot\cup}K_3
                              \mathbin{\dot\cup}K_2,
\]

so each has independence number three and contains no `K_4`.  The paths
`u-s-v`, for

\[
                    s\in\{x_1,x_2,y_1,y_2,y_3,z_1,z_2\},
\]

are seven internally vertex-disjoint `u`--`v` paths.

Nevertheless the graph has treewidth at most four.  A width-four tree
decomposition has central bag

\[
 B_0=\{u,v,x_1,x_2\}
\]

and four leaf bags

\[
 \begin{aligned}
 B_p&=\{u,p,x_1,x_2\}, & B_q&=\{v,q,x_1,x_2\},\\
 B_y&=\{u,v,y_1,y_2,y_3\}, & B_z&=\{u,v,z_1,z_2\}.
 \end{aligned}
\]

Every leaf is adjacent to `B_0` in the decomposition tree.  Since `K_7^-`
contains a `K_6` subgraph, it has treewidth at least five.  Treewidth is
minor-monotone, so this graph has no `K_7^-` minor.

## Exact scope

The graph is not seven-connected and is not contraction-critical.  It has
none of the proper-minor colouring responses or simultaneous externally
routed missing-edge paths available in the live host.  Thus it shows that
the nonadjacent bad-pair theorem must use those global inputs; it does not
refute that theorem.

Run:

```text
python3 barriers/hc7_k7minus_bad_pair_seven_paths_barrier_verify.py
```
