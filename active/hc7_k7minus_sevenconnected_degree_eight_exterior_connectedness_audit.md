# Adversarial audit: exterior connectedness at a degree-eight centre

**Verdict:** GREEN for the frozen revisions below.  This was an
author-side adversarial recheck, not a substitute for a later independent
audit.

## Frozen artefacts

```text
3654719b95d3a6b3446d5c15630ee474b07725568cf38a4ad426d0a3635a1fcf
  active/hc7_k7minus_sevenconnected_degree_eight_exterior_connectedness.md
a7b7e62b334b79c5364eb67da1b876ce10ce922974a72f558ef05d7e6c98d139
  active/experiments/sevenconnected_codegree2_profiles/verify.py
3d02ef9a9aff141b63fd12100ae3bf34038c927a09a335caed36a7940d0f7083
  active/experiments/sevenconnected_codegree2_profiles/README.md
```

The imported exact minor engine has SHA
`d721c181a8388feb7901e8ab04f704c19679cfb56551752756a45733f28d6fdc`.
The closed-shore lemma and its audit have respective SHAs
`ba6dbfe1ca9e89041b1a77174844c24598984cbe76349a55c41f15b2e997cc03`
and
`03738f53f8892c786dadd236c529c59b7045b3dc8371de22f0836f3721e5e43a`.

## 1. Quotient reduction

For a component `L` of `G-N[v]`, every external neighbour lies in
`J=G[N(v)]`.  Since `v` remains outside `L\cup N(L)`, seven-connectivity
does imply `|N(L)|>=7`.  Contracting two components and deleting the rest
therefore gives exactly the quotient tested by the verifier: the two new
vertices are mutually nonadjacent, nonadjacent to `v`, and each is full to
`J` or misses one vertex.

The local graph cannot contain a `K_6^-` minor: the singleton `v` is
adjacent to every branch set of such a model.  Hence all verifier filters
follow from the stated hypotheses.  The order-eight generation is
complete because deleting any vertex leaves one of the `1,044` atlas
graphs of order seven, and all `2^7` neighbourhoods of the restored vertex
are generated.  Exact isomorphism tests, rather than the preliminary
invariants, decide duplication.

For the minor test, every minor model is obtainable from the singleton
partition by repeatedly merging two touching bags and deleting unused
bags.  The memoised recursion performs both operations exhaustively and
checks the returned connected, disjoint bags.  Thus a negative result is
not a bounded branch-set or subgraph test.

The exceptional pair list is fixed in one labelled copy of ``GMs`KK``.
After the first pair is labelled with misses `3,5`, every further component
would have to miss a vertex in `\{5,6\}` when paired with the first and a
vertex in `\{3,4\}` when paired with the second.  This checks that the
argument excluding a third component does not silently relabel `J` from
pair to pair.

## 2. Rooted-shore step

In the exceptional graph, vertex `3` has its three local neighbours, the
centre `v`, no neighbour in `C`, and no exterior neighbour outside `D`.
Minimum degree seven therefore gives at least three distinct neighbours in
`D`, so `|D|>=3`.

For the seven-set `S=V(J)-\{5\}`, take `A=D` in the closed-shore lemma.
The opposite set contains `v,5,C`, is nonempty, and is anticomplete to
`D`: the first two facts use the definition of the exterior and the last
uses `N(D)=S`.  The lemma therefore applies literally and makes
`(G[D\cup\{2,3,4,6\}],\{2,3,4,6\})` internally four-connected.  Its order
is at least seven, exceeding the six-vertex threshold in Jorgensen's
rooted-diamond theorem.

The rooted bags containing `2,6` are adjacent through the literal edge
`26`, and those containing `3,4` through `34`.  Hence an actual missing
rooted adjacency can only be `23,24,36`, or `46`.  If the rooted model is
a clique, one may simply ignore an extra adjacency and use any row.

## 3. Independent check of the four rows

I rebuilt the labelled graph directly from graph6 code, added the centre
and the contracted `C`-image, completed the four root vertices except for
the nominated pair, and checked connectivity, disjointness, and all 21
bag pairs without importing the experiment verifier.  Numbering the bags
from zero, the only absent pairs were

```text
23  1.3/4/2.5/6/0.7/8/9       absent=[(5,6)]
24  2.3/4/5/6/0.7/1.8/9       absent=[(1,2)]
36  2/4/5/6/0.3.7/1.8/9       absent=[(1,2)]
46  2/3/5/6/0.4.7/8/1.9       absent=[(1,2)]
```

Replacing each completed root vertex by its rooted branch set preserves
every used edge.  A union such as `R_2\cup R_3` is connected precisely in
the row where `23` is required; the other unions use the displayed literal
edges.  Unused vertices of `D` may be deleted.  Thus the quotient rows lift
to the host and each has at most one absent bag adjacency.

## 4. Reproduction and scope

With NetworkX `3.6.1` pinned by `uv.lock`, the frozen command returned

```text
GREEN seven-connected degree-eight quotient classification
minimum_degree_three_extensions=27529 isomorphism_classes=2590 critical_local=542
one_component_profiles=4878 positive=4215 negative=663 negative_graphs=155
one_component_certificate_digest=bb82cf5a05ad28d4cb5bcb323cf3f094c0a189c2a15ca1763a9fe67d2abaf024
two_component_profiles=24390 positive=24386 negative=[('GMs`KK', 3, 5), ('GMs`KK', 3, 6), ('GMs`KK', 4, 5), ('GMs`KK', 4, 6)]
two_component_certificate_digest=664897369992e2eac75bca74d64911889203787ce9d9eb8d3b720438b7d863c9
exceptional_rooted_completion_digest=f36610df787fe55c2aa64c339e1c18f2cb485c723747d05259a728eb01218414
all_one_component_survivors_have_kappa_J_in_{2,3}
```

The theorem proves only that the exterior has at most one component under
the three stated local hypotheses.  It neither eliminates an empty or
connected exterior nor proves the desired incident-codegree-two statement.
