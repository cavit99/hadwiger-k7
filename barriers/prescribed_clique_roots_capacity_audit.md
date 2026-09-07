# Internal audit: prescribed clique roots and vertex capacity

**Verdict: GREEN.** Separate internal mathematical audit, 7 September 2026;
not external peer review. The written counterexample family and its stated
scope are valid. No computational or external literature input is needed.

**Audited source:** [prescribed clique-root capacity](prescribed_clique_roots_capacity.md).
**Whole-file SHA-256:**
`b01ff427f2baafa35ebc87ed4ec27f36bfa87f427e26b95acc0df84aec57b18c`.

## Host and clique model

Deleting fewer than `4m-2` vertices leaves at least three vertices, hence
at least two parts. Such a complete multipartite graph is connected.
Deleting the complement of one part leaves two nonadjacent vertices,
proving the exact connectivity. One singleton per part gives a clique of
`2m` bags. The remaining vertices belong to distinct parts, so any pairing
gives `m` connected bags. A bag containing two parts meets every other
nonempty bag, verifying all contacts of the displayed `K_{3m}` model.

## Universal ownership obstruction

The strongest inference is the count for **every** `K_{3m}` model, without
assuming it is spanning. If `q` bags are nonsingleton, disjointness requires
at least `3m+q` vertices, hence `q<=m`. Pairwise adjacency permits at most
one singleton per part, giving `3m-q<=2m` and `q>=m`. Equality forces all
`4m` vertices to be used, every nonsingleton bag to have size two, and
exactly one singleton in each part. Larger bags or omitted vertices cannot
escape this conclusion.

The prescribed set fits in `ceil((3m-1)/2)` parts. At most that many of its
vertices occupy singleton bags. At least `floor((3m-1)/2)>m` therefore
occupy the `m` remaining bags, so two prescribed vertices share a bag.
The inequality holds for every `m>=3`; moreover `4m-2>=3m+1`. Thus the
family refutes the quantified assertion even at connectivity `t+1`.

## Exact limits

There is no unresolved gap in this counterexample proof. Its first
parameter is `m=3`, giving `t=9`; it does not refute five prescribed roots
in a `K_6` model. Nor does it refute choosing suitable neighbours instead
of prescribing them, or a construction using full critical-host data.
The Menger discussion correctly identifies a missing ownership inference,
not failure of Menger's theorem: distinct terminal selectors need not give
distinct first-entry bags or preserve their connections and contacts.
No clique-augmentation theorem follows from this negative finding or from
positive finite probes. Conjecture 21 and `HC_7` remain unproved here, and
this counterexample does not achieve the user's requested objective.
