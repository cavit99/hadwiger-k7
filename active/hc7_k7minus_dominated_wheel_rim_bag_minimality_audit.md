# Internal audit of rooted wheel rim-bag minimisation

**Status:** internal proof audit, GREEN for the theorem stated in
[`hc7_k7minus_dominated_wheel_rim_bag_minimality.md`](hc7_k7minus_dominated_wheel_rim_bag_minimality.md).
This is not external peer review.  The audited source is identified by its
SHA-256 hash below.

## 1. Pinned revision

Run from the repository root:

```text
shasum -a 256 active/hc7_k7minus_dominated_wheel_rim_bag_minimality.md
```

The expected digest is recorded after the final source edit in Section 6
of this audit.

## 2. Quantifier audit

The comparison class in Section 1 fixes:

1. the host graph;
2. all seven roots and their labels;
3. the labelled six-wheel whose edges must be represented; and
4. the source rim label.

It does **not** require the model to span.  This is necessary: when a
detachable piece has no owner, the proof removes it from the model.  The
live canonical kernel lift is spanning, but that property is intentionally
not claimed for the minimised model.

The minimisation concerns only the source-bag order.  In the unique-owner
case, the owner bag grows.  No lexicographic or total-size decrease is
asserted.

## 3. Transfer audit

For an admissible piece `P`, both `P` and the rooted remainder are
nonempty and connected.

- With no owner, every required source adjacency survives in the
  remainder, so omitting `P` gives a smaller rooted model.
- With unique owner `t`, an old source--`t` edge has its source end in
  `P`, so `P` meets `B_t` and the enlarged owner is connected.
- Connectedness of the old source bag supplies an edge between `P` and
  its complement.  After transfer this edge represents the required
  source--`t` adjacency.
- Every other required source adjacency survives by definition of the
  owner set.  Enlarging the owner destroys no adjacency.

Thus Theorem 2.1 is correct even when unrecorded interbag edges exist.
Those edges may create extra quotient adjacencies after transfer, but a
minor model only requires the prescribed wheel adjacencies.

For the spanning comparison in Theorem 2.2, the unique-owner move still
partitions every host vertex among the bags.  In the owner-free case, a
foreign contact allows the whole piece to be assigned to a contacted bag;
all required source contacts already survive.  If there is no foreign
contact, spanningness makes the internal attachment set the full host
neighbourhood of the piece.  The other six branch sets give a nonempty far
side, so connectivity applies and gives the asserted lower bound.

## 4. Path-shape audit

For a non-root vertex `x` whose deletion leaves the source connected,
Theorem 2.1 assigns at least two labels from a three-element set.  Distinct
such vertices have disjoint owner sets because every required source--bag
adjacency is nonempty.  Hence there is at most one such non-root vertex.

A nontrivial connected graph has at least two non-cutvertices.  Therefore
the root is one, and there is exactly one other.  The cited elementary
block-tree argument correctly implies that a connected graph with exactly
two non-cutvertices is a path.  The root and the unique other
non-cutvertex are its endpoints.

Every root-free terminal interval of that path has a connected rooted
complement, so Theorem 2.1 applies to it.  No statement that the path has
order two is made.

The block-chain corollary uses root-free leaf-block pieces with one
internal attachment vertex (or `B_s-root` in the two-connected case).
Different such pieces cannot own the same nonempty required adjacency.
Thus at most one leaf block is root-free; the elementary block-cut tree
count then gives exactly two leaf blocks and a path-shaped block tree.  The
source graph itself need not be a path because its blocks are unrestricted.

## 5. Finite refinement and host lift

The finite verifier has SHA-256 digest

```text
26f657f4563efef242abe126875d978f9f9b017d440c0f760360bcb3faf32534
```

and was rerun during this audit with the pinned output in Lemma 4.1.  It
imports the already retained complete-kernel generator and exact minor
routine.  Its assertions check all three finite claims, including the
per-residue vulnerable-rim count; the displayed aggregate count alone is
not used as a substitute.

The host lift of the missing-edge test is valid.  An actual unrecorded
interbag edge augments the labelled wheel quotient by that edge.  The
finite `K_5^-` model lifts through unions of the seven rooted branch sets,
each resulting branch set still meets `Q`, and the universal adjacent
vertices `u,v` then extend it to `K_7^-`.

For Corollary 4.2, literal `Q` edges are incident with the retained root
and therefore cannot be owned by a root-free piece.  A rim label has three
wheel neighbours.  Degree at least two in `Q` leaves at most one possible
owner, contradicting Theorem 2.2 for the one-attachment leaf piece.  At
degree one, the same piece must own exactly the two nonliteral contacts.
The corollary explicitly fixes one source label; it makes no simultaneous
six-bag minimisation claim.

## 6. Verdict and unresolved hypotheses

**Verdict: GREEN.**  The detachable-piece owner rule and rooted-path
conclusion are proved with the stated ordinary-model quantifiers.  The
weaker spanning-model dichotomy and rooted block-chain conclusion are also
proved with their separate quantifiers.

The proof does not establish any of the following:

- a spanning minimum with the rooted-path conclusion;
- an upper bound on a terminal interval's full host boundary;
- two distinct owner portal vertices;
- a four-bag movable split;
- preservation of a proper-minor boundary partition; or
- a `Q`-rooted `K_5^-` model.

When the full neighbourhood has a nonempty far side, five-connectivity
lower-bounds that boundary; it does not supply the missing upper bound.  If
there is no far side, the neighbourhood is not a proper separator and
connectivity supplies no conclusion.  The exact unresolved implication is
displayed as (5.1) in the source.

Pinned source digest:

```text
6aab6abe4f443f5c20c8b0dd3a94a5a7d3d96a29def82d25b2da3a765e9456ed
```
