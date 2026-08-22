# Cold audit: dense seven-vertex double-cone boundary

**Verdict:** GREEN.  Every seven-vertex graph `S` with `delta(S)>=4` either
has a `K_5` minor or is the pentagonal bipyramid.  Consequently
`overline{K_2} join S` contains `K_7^-`, and every exact seven-cut `Z` in a
seven-connected target-free graph satisfies `delta(G[Z])<=3`.

This is a boundary theorem, not T44, Conjecture 21 or `HC_7`.

## 1. Hash-pinned files

```text
88b93cb80a4bd916fed0d10b68e74d0caba5c7c62492f8f667e59c0bef8a900e  hc7_k44_fourconnected_seven_boundary_double_cone.md
64371b10f7ea9cfe6fe2d01ffa166d0cd9e5d2b176a9b8cf1488972310171b4e  hc7_k44_fourconnected_seven_boundary_double_cone_census.py
7af251c769557f2ae2f38821525c5bb9dc44a6b446be5cedf73367c2b45c4672  hc7_k44_fourconnected_seven_boundary_double_cone_census.txt
32229e0699a892778cf3911b21332c2341eadb33eed1f99652634a79adffa168  hc7_k44_fourconnected_seven_boundary_double_cone_certificates.tsv
3ab82219ec67e75e9caf2d7533033bb972c32b1bfb05e8a5eeedc2b9f8c2725a  hc7_k44_fourconnected_seven_boundary_double_cone_certificates_verify.py
```

All paths are relative to `results/`.

## 2. Written proof audit

If a separator `X` of order at most two existed in a seven-vertex graph of
minimum degree four, every component `D` of `S-X` would satisfy
`|D|>=5-|X|`; two such components do not fit.  Thus `kappa(S)>=3`.

For a three-cut `T`, the remaining four vertices must be two components of
order two.  Degree four forces both component edges and all twelve contacts
from the two edges to `T`.  The five bags displayed in the source are then
pairwise adjacent, so `S` has a `K_5` minor.  Hence a `K_5`-minor-free `S`
is four-connected.

The standard Wagner consequence says that a four-connected nonplanar graph
has a `K_5` minor.  In the remaining planar case, minimum degree and Euler's
formula give `14<=m<=15`.

- At `m=15`, the graph is a triangulation.  Nonfacial triangles would be
  three-cuts.  The degree sequence is `(6,4^6)` or `(5,5,4^5)`.  A universal
  vertex forces three chords among its cyclic neighbours, hence a nonfacial
  triangle.  If the two degree-five vertices were adjacent, degree counting
  gives at least three common neighbours, while an edge of a four-connected
  plane triangulation has only its two facial common neighbours.  Thus they
  are nonadjacent and the other five vertices induce `C_5`.
- At `m=14`, all vertices have degree four and the embedding has one
  quadrilateral face.  At least one diagonal is absent.  Adding it in the
  face preserves planarity and four-connectivity and creates the already
  excluded adjacent degree-five pair.

The sole `K_5`-minor-free graph is therefore the pentagonal bipyramid.  The
seven explicit bags in the source have exactly one possible missing
contact.  In every other case, a `K_5` model together with the two universal
anticomplete apices gives the target directly.

For an exact seven-cut `Z` in a seven-connected graph, every complementary
component is full to `Z`; otherwise six cut vertices still separate it.
Contracting two components and deleting the rest gives the double cone over
`G[Z]`.  The contrapositive of the theorem yields `delta(G[Z])<=3`.

## 3. Independent finite audit

The atlas script enumerates all 1,044 unlabelled seven-vertex graphs.  For
each graph it builds the nine-vertex double cone and enumerates every
two-edge spanning forest, which is every spanning seven-bag model.  It finds
344 positive and 700 negative boundaries.  All 29 boundaries of minimum
degree at least four are positive.

Reproduce and independently validate the emitted witnesses with:

```bash
UV_CACHE_DIR=/tmp/t44-uv-cache uv run python \
  results/hc7_k44_fourconnected_seven_boundary_double_cone_census.py \
  /tmp/t44-double-cone.tsv /tmp/t44-double-cone.txt

UV_CACHE_DIR=/tmp/t44-uv-cache uv run python \
  results/hc7_k44_fourconnected_seven_boundary_double_cone_certificates_verify.py \
  /tmp/t44-double-cone.tsv
```

The reproduced certificate digest is

```text
d862876512b71717e4122aa9081b88b6731e21f59eb9eab0817f08f7215dd487
```

The validator does not import the model-search routine.  It checks each
graph, its minimum degree, all seven nonempty connected bags and at least
twenty quotient contacts.  The trust boundary is the Python interpreter,
NetworkX's complete order-seven atlas and exact integer enumeration.  The
written proof is independent of that finite search apart from the standard
Wagner consequence.
