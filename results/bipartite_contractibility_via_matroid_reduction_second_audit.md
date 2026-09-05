# Second independent audit: universal bipartite contractibility

**Status:** separate internal mathematical audit, 5 September 2026.
This is an internal agent audit, not external peer review.

**Verdict: GREEN** for Lemmas 0--2, the universal rooted theorem, and
the stated bipartite-flow corollary. No unresolved mathematical gap was
found under their explicit finite-graph hypotheses.

## Exact revisions

- [Theorem source](bipartite_contractibility_via_matroid_reduction.md),
  whole-file SHA256:
  `3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`.
- [Independent diagnostic implementation](../active/experiments/bipartite_contractibility/matroid_reduction.py),
  whole-file SHA256:
  `4a3cc58d41b57aa4b1de4b1e5b4b2bc1309b151d7d5a43491d91d7f3185ec1a8`.

The auditor independently examined the proposed reduction before reading
the completed source, then checked the exact promoted text. The main
adversarial question was whether deleting a shared label silently borrows
a vertex already assigned to another projection. It does not.

## Strongest inference: allocated component contraction

For a maximizing disjoint family `I_a` and a minimizing set `X`, equality
in the matroid union expression forces every `I_a cap X` to have rank
`r_a(X)`. This assertion holds simultaneously for the chosen family and
set; it does not combine independent existential choices. A forest of
that rank spans every component of `M_a(X)`, including its isolated
vertices. Labels outside a projection are correctly treated as matroid
loops.

The connected set assigned to a component consists of its own `A`
vertices and only its allocated `B` labels. All these sets are disjoint:
the colour classes and their component partitions are disjoint, and
the forests allocate each label at most once. No prescribed `B` root
is included, and each set contains at most one prescribed `A` root.

If a discarded label `x` was allocated elsewhere, a path traversal
`u x v` is still removed legitimately: the projected edge labelled `x`
puts `u,v` in the same component. The forest allocated to that component
connects them without borrowing `x`. After contraction both endpoints
are the same vertex. This is a genuine contraction of disjoint connected
sets, followed by edge and vertex deletions. It is not a virtual edge
whose eventual lift has unspecified ownership.

Some contraction edges join component vertices on the same shore;
the proof explicitly deletes these. Every retained path step instead
comes from an original `A`-vertex-to-surviving-`B`-vertex edge. Removing
the discarded traversals yields a walk using only the two correct target
colours. Repeated visits to a component, including the component containing
the initial root, are resolved by loop erasure. The resulting simple path
has its required endpoints and no other root internally. Its two-colour
property verifies the intersection condition simultaneously for all paths.
The pre-contraction replacement walks need not form a scheme, and the
proof does not require that stronger statement.

## Remaining theorem checks

The direct normalization contracts disjoint monochromatic components,
each containing at most one prescribed root. Its path images can be
shortened to simple paths while retaining their two labels and endpoints.
Unused vertices and edges are deleted. No minimum nonroot degree is used
by the subsequent argument.

Each projection is connected because it is the union of projected paths
containing its root. A label occurs at most once in a projection, and
its endpoints there are distinct. Every ground-set label appears in a
projection. Thus the total projection rank is exactly `N_A`, and the
ground-set size is `N_B`.

Reversing the bipartition ensures `N_A<=N_B` without moving any root.
If packing reaches rank `N_A`, every individual forest is spanning;
its lift connects its complete `A` colour class. The original final
scheme edges give all contacts with the singleton current `B` roots.

If packing has rank `R<N_A`, then `R<|E|`, so a minimizing set `X`
cannot be empty. Every nonempty `X` contains a nonloop projected label,
giving positive total rank on `X`. At least one allocated tree edge
therefore contracts its two distinct `A` endpoints and its intervening
label. The host order strictly decreases. The recursive target is the
same finite graph with the same named roots represented injectively.
Composing the two root-preserving minor maps preserves disjointness,
connectivity, root containment and all required contacts. Isolated and
empty targets are handled separately as stated.

The flow corollary is also valid. Pairwise intersecting edges of a
bipartite graph have a common endpoint. A terminal on a nonincident
demand path would meet an independent demand path incident with that
terminal: bipartiteness and minimum degree two supply a neighbour outside
the nonincident edge's endpoints. Hence the asserted flow is a scheme.

The external matroid union input was checked in
[Edmonds' primary author text](https://www.researchgate.net/profile/Jack-Edmonds-2/publication/226200830_Matroid_Partition/links/0deec51d1e5ee4de7b000000/Matroid-Partition.pdf),
Theorem 1 and the matroid-partition identification on pp. 202--203.
Taking the polymatroid function to be the sum of the finitely many
graphic-matroid ranks gives exactly the formula used in Lemma 1.

## Independent computational diagnostics

The linked implementation uses shortest augmenting paths for graphic
matroid union and derives `X` from the final reachable set. It checks
the exact dual rank equality with NetworkX, checks the rank of every
allocated forest, and verifies each contracted set in the actual host.
It separately checks the reduced scheme and every retained quotient
edge, every root preimage, strict descent, and the final fully lifted
rooted model.

The augmentation engine was compared with exhaustive assignment of six
labels to three independently specified graphic matroids, or to no
matroid, on 21 systems. Independence in this comparison uses a separate
union-find check. The explicit deficient system has three connected
three-vertex projections and maximum union size four, so the comparison
tests a nontrivial minimizing set as well as successful packing.

The singleton-shore barriers at orders `n=3,4,5` passed, with respective
host-order sequences `36,21`, `56,32`, and `80,45`. Each run reverses the
chosen shore after contraction. One hundred variable-support `K_{3,3}`
schemes and one hundred `K_{4,4}` schemes with mixed pair/triple supports
also passed. Empty targets, isolated roots, literal edges and schemes
with one-path nonroots were checked. The final certificate checker
rejected overlapping branch sets and a branch containing a nonexistent
vertex.

```sh
uv run python3 active/experiments/bipartite_contractibility/matroid_reduction.py --order 5 --samples 100
uv run python3 active/experiments/bipartite_contractibility/matroid_reduction.py --order 3 --json
```

The second invocation emits the input paths, allocation forests,
minimizing sets, contracted sets, reduced paths and a final rooted model.
These are finite implementation diagnostics. They are not premises of
the universal written proof, and their sample bounds do not bound its
target or host classes.

## Limits of this verdict

No unresolved assumption or gap was found beyond the explicitly cited
matroid union theorem. The universal bipartite contractibility claim is
proved by an unbounded written induction; Hadwiger's conjecture, T44 and
Conjecture 21 are not proved. The audited prefix-construction failures
remain failures of those intermediate claims. Publication priority,
external validation and significance comparable to Norin--Totschnig are
not established by this internal audit.
