# Selected endpoint colour layers do not force a seven-clique minor

**Status:** explicit counterexample to a weakened construction claim;
not a counterexample to HC7 or the degree-seven critical-host target.
The [separate internal audit](hc7_degree7_selected_colour_layers_audit.md)
pins the reviewed version.

## Refuted inference

A vertex `u` has seven neighbours. A six-colouring after deleting an
exterior edge `xy` has two repeated pairs on that neighbourhood. The two
corresponding endpoint colour connections require `u`; the other three
connections avoid `u` and contain their singleton boundary roots.
These conditions alone do **not** force a `K7` minor, even when the
neighbourhood is `K3 dotunion K4` and hence has independence number two.

## Ten-vertex construction

Take vertices `u,x,y,b1,b2,c1,c2,r3,r4,r5`. Write
`S={b1,b2,c1,c2,r3,r4,r5}`. The edges are exactly:

- the triangle on `{b1,c1,r3}` and the clique on `{b2,c2,r4,r5}`;
- all edges from `u` to `S`;
- `xy`, `xb1`, `xc1`, `yb2`, `yc2`;
- all edges from each of `x,y` to `{r3,r4,r5}`.

Delete `xy` and colour `u,x,y` with zero, `b1,b2` with one, `c1,c2`
with two, and each `ri` with `i`. This is proper. The zero-one endpoint
component is the path `x-b1-u-b2-y`; the zero-two component is
`x-c1-u-c2-y`. Removing `u` separates the endpoints in each. For
`i=3,4,5`, the path `x-ri-y` avoids `u` and contains its prescribed
singleton root.

Nevertheless the graph has no `K7` minor. The following bags, in the
displayed order, form a path decomposition:

\[
\begin{split}
 &\{b_2,c_2,r_4,r_5,u,y\},\quad
 \{r_4,r_5,u,x,y\},\quad \{r_3,u,x,y\},\\
 &\{c_1,r_3,u,x\},\quad \{b_1,c_1,r_3,u,x\}.
\end{split}
\]

Every vertex occurs in an interval and every edge has both ends in a
bag. The width is five. Since treewidth is minor-monotone and `K7` has
treewidth six, the asserted minor is impossible. This is a written
certificate, not a conclusion from a failed search.

## Unaffected scope

The graph is six-colourable: in the displayed colouring change `y` to
one and `b2` to three, then restore `xy`. It is not seven-connected
(`b1` has degree four). It therefore does not refute any construction
using the full critical-host hypotheses or choosing a different response.
The first unsupported inference is replacing simultaneous branch-set
allocation by the existence of these five selected colour connections.
Further critical-host information must enter that allocation.

The optional [six-graph probe](../active/hc7_degree7_exceptional_layers_probe.py)
also checks two boundary orientations and up to two extra shared-colour
vertices, on at most twelve vertices. Run it with
`uv run python3 active/hc7_degree7_exceptional_layers_probe.py`.
Its expected final line starts `PASS six selected-response quotient probes`.
Neither those finite variants nor this example are a reduction of the
unbounded degree-seven problem.
