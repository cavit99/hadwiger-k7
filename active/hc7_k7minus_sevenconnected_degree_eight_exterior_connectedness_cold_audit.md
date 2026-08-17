# Independent cold audit: exterior connectedness at a degree-eight centre

**Verdict:** **GREEN** at the frozen revisions below.  This audit was
conducted independently of the theorem and verifier authors.  It is an
internal mathematical audit, not external peer review.

## Frozen artefacts

```text
3654719b95d3a6b3446d5c15630ee474b07725568cf38a4ad426d0a3635a1fcf
  active/hc7_k7minus_sevenconnected_degree_eight_exterior_connectedness.md
a7b7e62b334b79c5364eb67da1b876ce10ce922974a72f558ef05d7e6c98d139
  active/experiments/sevenconnected_codegree2_profiles/verify.py
ba6e4469de5a456af717e51e59bd7ddff2764d40b739169d9ddf0d48d2bac99e
  active/experiments/sevenconnected_codegree2_profiles/cold_verify.py
```

The imported exact minor engine has SHA-256
`d721c181a8388feb7901e8ab04f704c19679cfb56551752756a45733f28d6fdc`.
The closed-shore lemma and its audit have respective SHA-256 hashes
`ba6dbfe1ca9e89041b1a77174844c24598984cbe76349a55c41f15b2e997cc03`
and
`03738f53f8892c786dadd236c529c59b7045b3dc8371de22f0836f3721e5e43a`.

## 1. Quotient and pair-classification quantifiers

For every component `L` of `G-N[v]`, all neighbours of `L` lie in
`J=G[N(v)]`.  The vertex `v` lies outside `L union N(L)`, so
seven-connectivity gives `|N(L)|>=7`; hence the contracted image of `L` is
full to `J` or misses exactly one vertex.  Two different components give
nonadjacent images, both nonadjacent to `v`.  Contracting the components
and deleting all unused vertices therefore gives exactly a profile tested
by the verifier, irrespective of the components' orders.

A `K_6^-` model in `J`, together with the universal singleton `v`, would
be a `K_7^-` model.  Thus all four filters used in the finite census follow
from the theorem's hypotheses.  The order-eight generation is exhaustive:
deleting a vertex leaves one of the `1,044` order-seven atlas graphs, and
all `2^7` neighbourhoods of the restored vertex are generated.  The
bucketing invariants are isomorphism-invariant and exact isomorphism tests
make the final decision.  The minor recursion is also exhaustive: unused
vertices are deleted, whilst successive mergers along a spanning tree
produce every connected branch set.

The negative pair list is a statement in one fixed labelled copy of
``GMs`KK``, not merely a list of four unrelated isomorphism types.  Once
`C,D` are labelled as missing `3,5`, any third component `E` would, from
the fixed pair `(C,E)`, have to miss `5` or `6`; from `(D,E)` it would have
to miss `3` or `4`.  The full-image case is absent from the negative list.
These requirements are incompatible, so the exclusion of a third
component does not relabel `J` between pairs.

## 2. Closed-shore and rooted-diamond steps

After the third-component exclusion, vertex `3` has its three neighbours
in `J`, the neighbour `v`, no neighbour in `C`, and no possible exterior
neighbour outside `D`.  Since a seven-connected graph has minimum degree at
least seven, vertex `3` has at least three distinct neighbours in `D`.
Thus `|D|>=3`.

Set `S_0=V(J)-{5}`, `A=D`, and
`R=V(G)-(D union S_0)`.  Then `|S_0|=7`, both `A` and `R` are nonempty,
and `A` is anticomplete to `R` because `N(D)=S_0`.  Consequently the
closed-shore lemma applies with `Q={2,3,4,6}` and gives internal
four-connectivity of

```text
(G[D union Q],Q).
```

This rooted graph has at least seven vertices, so it exceeds the required
order-six threshold.  Norin--Totschnig, arXiv:2507.03244v1, Lemma 10,
states exactly that an internally four-connected four-root pair of order at
least six has a rooted `K_4^-` model; it identifies this as the
reformulation of Jorgensen, *Contractions to K8*, Lemma 16(2).  The rooted
model definition in the same primary arXiv source supplies four disjoint,
connected bags containing the four distinct roots, exactly as used here.

The literal edges `26` and `34` guarantee those two rooted-bag
adjacencies.  Hence the rooted diamond's possible absent pair is confined
to `23,24,36,46`.  A rooted clique causes no additional case: any of the
four rows remains valid when the nominally omitted adjacency is present.

## 3. Seven-bag completions

The independent checker compresses each rooted bag `R_i` to its root `i`
and retains only literal local edges and the five required rooted-diamond
adjacencies.  This is conservative: replacing the compressed vertices by
the actual rooted bags preserves every checked edge and can only add
adjacencies.  It checks disjointness, connectivity of every displayed
union, and all twenty-one interbag pairs.  For missing rooted pairs
`23,24,36,46`, respectively, the only absent ordinal bag pairs are

```text
(6,7), (2,3), (2,3), (2,3).
```

In the first row this is the allowed `v--C` nonedge.  In the other rows it
is the allowed nonedge between the second and third displayed bags.  The
unions are connected for explicit reasons: `1R_3` uses `13`, `5R_2` uses
`25`, `R_2R_3` uses the required rooted adjacency `23`, `07R_3` uses
`07,03`, `07R_4` uses `07,04`, and `1C` uses fullness of `C` at `1`.
All bags are disjoint because the rooted bags lie in `D union Q`, the
remaining boundary vertices are outside `Q`, and `C,D,{v}` are mutually
disjoint.  Every row is therefore a valid `K_7^-` model in the host.

## 4. Independent computation

The pinned main verifier was read in full and rerun under the repository's
pinned NetworkX version.  It reproduced the stated `542` local classes,
all `24,390` two-image profiles, the four negative profiles, and all three
certificate digests.

The retained cold checker does not import the main verifier or its minor
engine.  For each of the four exceptional eleven-vertex quotients it
enumerates every partition into seven connected bags on every support of
order seven through eleven.  It checked `159,027` partitions per quotient
and found no `K_7^-` model.  It then rebuilt the completion rows from the
displayed local edge set and returned

```text
rows={(2, 3): [(5, 6)], (2, 4): [(1, 2)],
      (3, 6): [(1, 2)], (4, 6): [(1, 2)]}
GREEN independent partition and completion check
```

Thus the exceptional quotient classification has both positive
certificates from the main verifier and an independent exhaustive check of
every negative profile.

## 5. Scope

The theorem proves only that the exterior has at most one component under
the three stated local hypotheses.  It does not eliminate an empty or
connected exterior and does not establish an incident edge of codegree at
most two.  No unresolved mathematical assumption, labelling ambiguity, or
branch-set gap remains at the frozen revisions.
