# Independent audit: contact-only `7,6,7` quotient barrier

**Status:** separate hash-pinned internal audit.

**Verdict:** **GREEN.**  The displayed fourteen-vertex graph satisfies the
refuted contact-only hypotheses and has no `K_7^-` minor.  The source states
the scope of the counterexample correctly.  This is an internal mathematical
audit, not external peer review.

## Audited revisions

- barrier note:
  `hc7_k7minus_three_piece_767_quotient_barrier.md`
- barrier note was cold-audited at SHA-256:

  ```text
  1667ff5cc651f14297b1d967a8409e8934429d5463b9201da94002e8e625e7ba
  ```

- first promoted barrier-note SHA-256:

  ```text
  8ae8ba0e3d1ec2bd76c051c4787a8236e83c7b36883b5a72771807d7d87ccc54
  ```

  This revision differs from the cold-audited mathematical revision only by
  the addition of the adjacent GREEN audit link.

- final barrier-note SHA-256:

  ```text
  487dafc7b94d282eb6a78d8ef377c7b1dc5c4de09970abbb1045d2c7750c5563
  ```

  The final revision changes only the reproduction command from the
  project-environment invocation to direct standard-library Python.  No
  statement, construction, or proof step changed.

- deterministic verifier:
  `../active/experiments/feedback_forest_boundary_gate/probe_three_piece_terminal.py`
- original cold-audited verifier SHA-256:

  ```text
  c176b807418fceba44076ff8fd012ccbe2fbf9b0c8111e16557c52606aa3fcec
  ```

- final standard-library verifier SHA-256:

  ```text
  21d043e3ef1693785bdd12f498ac5f06dc45b672b3c5502bbf9d72f8bdd51cfe
  ```

  The final verifier was separately cold-audited as described below.  It
  constructs the same labelled graph and decomposition and reproduces the
  same output and graph6 string as the original verifier.

## Construction and colouring

The boundary consists of `K_2\vee C_5` together with four leaves adjacent
only to one vertex of the `K_2`.  It therefore has order eleven, is
connected, and is exactly five-chromatic: the join has chromatic number
`2+3=5`, and adding the leaves does not increase it.

The three exterior vertices induce the path `a-b-c`.  Directly from the
listed neighbourhoods, their boundary-contact counts are `(7,6,7)` and
their degrees in the full graph are `(8,8,8)`.  Thus all numerical
hypotheses in the refuted assertion hold.

## Clique calculation

The largest clique of `K_2\vee C_5` has order four, and no pendant boundary
vertex enlarges one.  The neighbourhood of either outer path vertex has
clique number three: its possible triangles are exactly the types listed in
the source.  The middle vertex also has neighbourhood clique number at most
three because its two path neighbours are nonadjacent, `q` misses every
leaf, and the leaves are pairwise nonadjacent.  Hence the full graph has
clique number four and in particular has no `K_5` subgraph.

The final verifier independently enumerates vertex subsets in decreasing
order until it finds a clique and confirms this value.

## Tree-decomposition certificate

The five bags `K_3-K_2-K_1-E-D` form the displayed path, and the four bags
`L_i` are leaves at `D`.  Inspection gives:

- every graph vertex occurs in a bag;
- every boundary-core edge, path edge and boundary-contact edge occurs in
  a displayed bag; and
- for each graph vertex, the bags containing it induce a connected subtree.

All bags have order five, so the graph has treewidth at most four.  Since
`K_7^-` contains a `K_6` subgraph, its treewidth is at least five.  Treewidth
is minor-monotone, and therefore the constructed graph has no `K_7^-`
minor.  This is a complete structural certificate; it does not rely on the
absence of a model found by a search.

## Verifier reproduction

Running

```text
python3 -B \
  active/experiments/feedback_forest_boundary_gate/probe_three_piece_terminal.py
```

reproduced the output recorded in the source, including

```text
contacts=(7, 6, 7)
maximum_clique=4
treewidth_upper_bound=4
graph6=M~vNKA?_C?[No^w]_
COUNTEREXAMPLE_TO_CONTACT_ONLY_767_QUOTIENT
```

The final checker uses only the Python standard library.  Its adjacency-set
construction is symmetric and reproduces all 42 edges of the original
labelled graph.  Its colouring search exhausts every available colour for a
dynamically selected uncoloured vertex, backtracking after every failed
extension; it therefore decides the asserted four- and five-colourability
tests rather than applying a heuristic.  Its clique routine examines every
subset at each order, and its tree-decomposition validator checks treehood,
bag size, vertex and edge coverage, and running intersection.

The compact graph6 encoder uses the standard upper-triangle order
`(0,1),(0,2),(1,2),...`, pads the bit string to a multiple of six, and uses
the correct one-byte order prefix for fourteen vertices.  An independent
NetworkX round trip reproduced the exact graph6 string and all graph edges.
Runs under both the default hash seed and a fixed nondefault hash seed gave
the documented output.  An additional independent run gave vertex
connectivity three and degrees `(8,8,8)` at `a,b,c`.

## Scope and unresolved assumptions

The source correctly refutes only the contact-only finite quotient claim.
The constructed graph is not seven-connected and, having treewidth at most
four, cannot carry the co-bagged spanning `K_6` minor model from the critical
host.  It is not supplied with the six-coordinate response data or common
cycle used in the host-level problem.  Consequently it is not a
counterexample to the `K_7^-` six-colour conjecture or to a composition
theorem that spends any of those additional hypotheses.

There are no unresolved assumptions in the stated barrier claim.
