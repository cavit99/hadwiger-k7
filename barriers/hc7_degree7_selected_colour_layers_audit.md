# Internal audit: selected degree-seven endpoint colour layers

**Verdict: GREEN.** This is a separate internal audit, not external peer
review. The construction refutes the stated selected-layer inference;
it does not refute HC7 or close the degree-seven critical-host case.

## Audited revision

Source: [selected endpoint colour layers](hc7_degree7_selected_colour_layers.md).

SHA-256:

```text
3dd4336ff544c134cd94fbc533f27890deaf8e8f4123161fef6aa3717c6b6843
```

The source hash was checked before verification. After the audit link
was added, deleting only that two-line addition reproduced the original
audited hash `e8b94f7894034479dd894819cba78365f52bc738ec4cfbd50942cb91b41127c2`.
The mathematics is byte-identical. The optional finite probe is not a
premise of this audit or of the minor-exclusion proof.

## Independent checks

The edge specification gives exactly ten vertices and 27 edges:
nine boundary-clique edges, seven edges incident with `u`, five edges
in the third displayed family, and six edges in the fourth. These
families are disjoint. In particular, `N(u)=S`, `G[S]=K3 dotunion K4`,
and `G-N[u]` is the connected edge `xy`.

The displayed colouring is proper on `G-xy`. Its zero-one induced
subgraph is exactly `x-b1-u-b2-y`, and its zero-two induced subgraph is
exactly `x-c1-u-c2-y`. Consequently deleting `u` destroys both endpoint
connections. For each of colours three, four and five, the induced
layer contains the literal path `x-ri-y`; each path avoids `u` and
contains the prescribed singleton boundary root. Both repeated boundary
blocks are independent pairs.

The five displayed decomposition bags cover every edge. Their occurrence
intervals, numbering the bags from one, are:

| Vertices | Bags containing the vertex |
| --- | --- |
| `u` | 1–5 |
| `x` | 2–5 |
| `y` | 1–3 |
| `b2,c2` | 1 |
| `r4,r5` | 1–2 |
| `r3` | 3–5 |
| `c1` | 4–5 |
| `b1` | 5 |

Every occurrence set is an interval. The largest bag has six vertices,
so this is a valid path decomposition of width five. Minor-monotonicity
of treewidth and `tw(K7)=6` therefore exclude a `K7` minor without any
search assumption.

Changing `y` to colour one and `b2` to colour three gives a proper
six-colouring of the original graph. The restored edge `xy` then has
colours zero and one. No new conflict occurs at `y`, whose other
neighbours have colours two, three, four or five; none occurs at `b2`,
whose neighbours have colours zero, one, two, four or five. Also
`d(b1)=4`, excluding seven-connectivity.

These claims were independently checked from a fresh edge-set construction
using a standard-library script run with
`UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache uv run python3`. It checked the
source hash, edge count, both exact layer edge sets, the three prescribed
paths, every decomposition edge and interval condition, and both
colourings. It did not import or call the optional minor-search probe.
The output was:

```text
PASS: hash, 10 vertices, 27 edges, exact selected layers, path decomposition width 5, six-colouring, degree bound
```

## Trust boundary

No unresolved assumption or gap was found in the stated barrier. The
example fails seven-chromaticity and seven-connectivity. Its width-five
certificate in fact implies that every minor is six-colourable, so the
missing critical-host condition should be understood as the entire
minor-minimal *non-six-colourable* setup, not as a demonstrated failure
of the proper-minor colouring assertion alone. The source correctly
does not claim a counterexample to a construction using all host
hypotheses or allowing a different response.
