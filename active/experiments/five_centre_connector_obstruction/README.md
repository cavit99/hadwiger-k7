# Five-centre connected-subgraph obstruction probe

**Status:** computer-assisted finite negative search.  This experiment
does not prove the unbounded connected-subgraph theorem and is not a
counterexample to it.

The graph `X=M(K_4)` has a known local obstruction to two vertex-disjoint
connected subgraphs, one containing five prescribed boundary roots and the
other containing two prescribed poles.  In the standard NetworkX labelling,
the initial portal pairs are

```text
z0: 58    z1: 35    z2: 02    z3: 27    z4: 05
p:  07    q:  25
```

The initial example is four-connected, five-chromatic, `K_5`-subgraph-free,
and every displayed portal pair is an edge.  It fails the relative
seven-connectivity condition: some nonempty subsets of `X` have fewer than
seven neighbours in `X` together with the boundary terminals.

The verifier exhausts two natural monotone repairs.

1. It checks all `2^14=16,384` edge-supergraphs of `M(K_4)` while retaining
   the initial portal pairs.  Of the 479 supergraphs for which adjoining the
   terminals does not create a `K_5` subgraph, none has relative boundary at
   least seven.
2. It adds the minimum terminal incidences required at the four vertices
   `4,6,7,8`, namely `3,3,1,2`.  There are 91,875 choices.  Of these, 18,780
   satisfy the hereditary local restrictions
   `|N_X(z)|<=6`, `alpha(X[N_X(z)])<=2`, and the absence of a `K_4` inside
   every terminal portal set.  Every one already has the two required
   disjoint connected subgraphs.

The second check rules out every valid portal-edge superfamily of the
initial obstruction.  Any family with relative boundary at least seven
contains one of the enumerated minimum repairs; the local restrictions are
hereditary under taking portal subsets, while existence of the desired
connected subgraphs is monotone under adding portal edges.

Run:

```text
uv run --with networkx==3.6.1 python \
  active/experiments/five_centre_connector_obstruction/mk4_relative7_search.py
```

Expected output ends with

```text
NO_EDGE_SUPERGRAPH {'tested': 16384, 'k5_free': 479, 'relative_seven': 0}
NONE {'tested': 91875, 'locally_valid': 18780, 'forest_free': 0}
```

The experiment shows both sides of the current trust boundary: chromaticity,
four-connectivity, and two adjacent portals per terminal do not suffice, but
the simplest obstruction disappears once its portals are forced to satisfy
the full relative order-seven condition.  An unbounded proof still needs the
global connectivity argument, such as the sharp density alternative of
Du--Li--Xie--Yu, rather than an inference from this finite census.
