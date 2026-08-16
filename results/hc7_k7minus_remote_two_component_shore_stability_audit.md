# Internal audit: remote two-component shore stability

**Verdict:** **GREEN** for the promoted source and verifier revisions recorded
below.  This is a separate internal mathematical and computational audit,
not external peer review.

## 1. Exact audited revisions

The promoted theorem is
[`hc7_k7minus_remote_two_component_shore_stability.md`](hc7_k7minus_remote_two_component_shore_stability.md):

```text
5e7d0d0a143fbe9439435cb71a8afb455861562b08259c0791efe1edb17e2640
```

The complete mathematical text was audited before promotion at SHA-256
`5ded9fe9bf29395c81570c1b2e428a14dbd14344fe182d77c824c35a9cd1d444`.
Promotion changed only the status paragraph and relative links to active
frontier files.

The audited standard-library verifier is
[`hc7_k7minus_remote_two_component_shore_stability_verify.py`](hc7_k7minus_remote_two_component_shore_stability_verify.py):

```text
8750ec3264b546f1278d018387c0ebc37d748caabaad651d8a1f325e82d01611
```

The source and verifier pass `git diff --check`.  All 24 Markdown links in
the source resolve to existing local files; the exact-section anchor for
the earlier seven-boundary reflection lemma also has the stated target.

## 2. Scope and response-language audit

The corrected title and status are exact.  The theorem treats the
order-seven case `N(C)=N(z)-{w}` and the order-eight both-full case.  It no
longer suggests coverage of the different order-eight outcome in which the
component carrying `f` is full and the other exterior component misses one
boundary vertex.

For the full eight-set `X=N(z)`, all four selected edges are absent from the
closed `E`-shore: the three spoke edges use the absent vertex `z`, while
`f` is internal to the different exterior component `C`.  Consequently all
15 operation colourings restrict properly there.  A star-only colouring is
also proper on the `C`-shore and is rejected by the `z`-shore; the
`f`-only colouring has the symmetric orientation; and a mixed colouring
cannot be accepted on both remaining shores.  Each assertion follows by
aligning colour names on the common equality partition and gluing the three
closed shores.

The visible `z`-colour block on `X` is exactly the selected nonempty subset
of `I`.  The four blocks

```text
I, I-{x1}, I-{x2}, I-{x3}
```

are pairwise intersecting and unequal, so they cannot be blocks of one
common partition.  This proves four distinct star partitions and four
distinct mixed partitions.  Since the `f`-only partition is accepted on
the `z`-shore while every star partition is rejected there, it is different
from all seven star partitions.  The five-partition lower bound is valid;
the theorem does not claim that all 15 partitions are distinct or identify
any partition with a minor-model bag.

## 3. Order-seven packing and bridge exclusion

Put `Q=N(C)=X-{w}`.  The critical seven-cut theorem gives two full
complementary components.  If `E` is `X`-full, the joined component contains
the disjoint connected `Q`-full subgraphs `E` and `{z}`.  If `E` misses
`r in Q`, the audited nonadjacent-miss elimination forces `wr`; together
with the required `wE` contact this makes `E union {w}` connected and
`Q`-full, again alongside `{z}`.  Thus the joined side has packing number
at least two and `C` at least one.  The critical capacity bound of three
forces the exact vector `(1,2)` with `mu_Q(C)=1`.

If `G[C]-f` were disconnected, it would have exactly two connected parts
`A,B`.  In the seven-connected graph `G-f`, each has external neighbourhood
contained in the seven-set `Q`; that neighbourhood is an actual separator,
so it equals `Q`.  The two parts would therefore be disjoint connected
`Q`-full subgraphs inside `C`, contradicting `mu_Q(C)=1`.  Deleting the
internal edge does not remove a boundary contact, so `C-f` remains full.
The internal-cycle conclusion is the standard nonbridge equivalence.

## 4. Finite order-eight lemma and unbounded lift

The verifier uses exactly the seven graph6 strings from the independently
audited both-full boundary classification.  It adds two vertices complete
to the literal eight-set and two adjacent vertices each missing exactly one
boundary vertex.  Swapping the last two vertices reduces the labelled miss
pairs to the 36 unordered pairs with repetition, giving exactly

```text
7 * 36 = 252
```

instances.  Its deletion/contraction recursion is exhaustive: deletion
accounts for unused quotient vertices, and successive mergers of touching
bags generate every connected branch set.  At seven bags it tests the exact
target condition of at least 20 of the 21 possible contacts.  Every returned
certificate is independently rechecked for nonemptiness, disjointness,
connectedness, and contact count.

A clean execution under Python 3 returned exit status zero and exactly:

```text
boundary_types=7 digest=bf063de64c772c1c9c1c83cba7dc39d11bb9c214f3e101595889fe63f25861a0
bridge_split_cases=252 terminal=252 survivors=0
certificate_digest=311f08b508413fdc416b5af98e20abe0c45b86dafe890c8c88402b73e1565c8c
PASS remote two-component shore stability finite lemma
```

For the unbounded lift, if `C-f` has components `A,B`, seven-connectivity
of `G-f` gives each at least seven neighbours in `X`.  Contracting `A,B,E`
and retaining `z` and the literal boundary produces precisely the verified
quotient: `z` and the `E` image are full, `A,B` are adjacent only through
`f`, distinct exterior components are anticomplete, and `z` has no exterior
neighbour.  A full `A` or `B` image has exactly one boundary edge more than
the checked one-miss version.  The corrected source deletes one such edge
from every full image, so it covers the case in which both images are full.
This proves `C-f` connected and full, and hence puts `f` on an internal
cycle.

## 5. Order-free reflection and demand bounds

Lemma 5.0 is valid for a boundary of arbitrary order.  Let `U` be a maximum
clique among the singleton-block vertices of `Pi`.  Exactly

```text
|Pi|-|U| = d_{G[S]}(Pi)
```

blocks remain.  Assign them injectively to disjoint connected full
subgraphs in `L`.  Each union of a packet with its assigned independent
boundary block is connected, the unions are pairwise disjoint, and positive
demand guarantees that at least one edge is contracted.  The contraction
images are pairwise adjacent by fullness, are adjacent to every vertex of
`U`, and `U` is a clique.  They therefore form a clique with one vertex for
each block of `Pi`, of order at most six.  A six-colouring of the proper
minor gives those block representatives distinct colours.  Pulling the
colours back over their assigned blocks is proper because every crossing
edge was represented in the minor, and it induces exactly `Pi` on `S`.

All uses satisfy the lemma's positive-demand hypothesis.  The relevant
partitions come from six-colourings and therefore have at most six blocks,
whereas their boundaries have order seven or eight.  At least one block is
nonsingleton, so the singleton-block clique has order strictly below
`|Pi|` and the demand is at least one.

The reflection orientations are also correct.

- At order seven, the two full subgraphs in the rich component reflect the
  `f`-only partition onto `C`, giving demand at least three; the single full
  subgraph `C` reflects a star partition in the reverse direction, giving
  demand at least two.  The `z`-colour is absent from `Q` in the `f`-only
  response, so that partition has at most five blocks.
- In the both-full case, `C,E` reflect a star partition onto `{z}`, while
  `{z},E` reflect the `f`-only partition onto `C`.  Both demands are at
  least three.  For a mixed response, `E` is anticomplete to the combined
  opposite open shore `C union {z}` and one packet would reflect the
  partition there, so its demand is at least two.

In every forbidden low-demand case, the reflected colouring and the
original proper opposite-shore restriction have the same exact boundary
partition and glue to a six-colouring of `G`.  Thus Lemma 5.0 fully closes
the former order-eight trust-boundary gap.

The one-nonfull and distinct-adjacent-miss reductions give
`alpha(G[Q])=3`, so the independent triple may be chosen inside `Q`.
The four visible star blocks remain distinct after restriction to `Q`, and
the remote partition differs from them by opposite-shore gluing.  Corollary
5.2 is therefore valid.

## 6. Cycle placements and exact limitation

For each pair of leaves, the selected edges form the componentwise-induced
linear forest `K_2 dotunion P_3` of length three.  The audited
linear-forest theorem applies above its four-connectivity threshold and
puts all three edges on one cycle.  A simple cycle uses exactly two edges
at `z`, so the three leaf pairs produce three different cycles.  The
internal `f`-cycle lies in `C` and avoids `z`, making four distinct literal
cycles in total.

The dependency list now includes the one-nonfull attachment reduction and
the linear-forest cycle theorem as well as every input used in the packet,
boundary, response, and finite-lift arguments.  The note does not claim to
align an operation partition with the fixed exact model, split the connected
full shore, cover the omitted order-eight one-nonfull orientation, prove the
`K_7^-` six-colour conjecture, or prove `HC_7`.
