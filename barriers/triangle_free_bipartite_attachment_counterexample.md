# An odd cycle with a bipartite attachment need not be contractible

**Status:** written proofs; separate internal audit recorded in the adjacent
audit file at the exact source hash. The construction was discovered by a
finite search, but no computation is a premise of either theorem below.
These are counterexamples to proposed classifications, not a solution of
Hadwiger's conjecture or completion of the user's significance objective.
Current status is governed by the [research ledger](../RESEARCH_LEDGER.md).

All graphs are finite and simple. An `H`-scheme has one path between the
prescribed roots of each target edge, no other root internally, and a
common target endpoint for every collection of paths meeting at a vertex.
Contractibility requires an `H` minor preserving every prescribed root.

## Statements

**Theorem 1.** For every odd integer `ell>=5`, let `H_ell` be obtained by
identifying a vertex `v` of `C_ell` with one vertex in the three-vertex
shore of `K_{3,4}`. Then `H_ell` is not contractible. It has an explicit
properly coloured scheme on `2ell+14` vertices, all paths of length three,
with no rooted `H_ell` minor.

Nevertheless `H_ell` is triangle-free, contains no skewed theta, and
becomes bipartite after deleting any edge of its unique odd cycle.
A skewed theta has three internally disjoint paths with the same two
ends, two of odd length and one even.

**Theorem 2.** Every subgraph `F` of every `H_ell` in Theorem 1 is
`M'`-contractible. Here `M'(F)` has a root `r_w` and a clone `x_w` for
each `w in V(F)`, with edges `r_u x_w`, `x_u r_w`, and `x_u x_w` for
each target edge `uw`. The roots are the vertices `r_w`.

Thus the following two proposed sufficiency statements are false:

1. A triangle-free graph with no skewed theta and at most one edge
   meeting all odd cycles in each component is contractible.
2. A graph is contractible whenever every subgraph is `M'`-contractible.

The examples also disprove unrestricted closure of contractibility under
attaching a bipartite graph at one vertex: cycles are contractible by
[1, Theorem 4.2], and the
[audited universal theorem](../results/bipartite_contractibility_via_matroid_reduction.md)
proves contractibility of the bipartite block.

## The explicit scheme

Write the cycle as `v,c_1,...,c_(ell-1),v`. Write the bipartite block's
shores as

`A={v,p,q}`, and `B=B_L union B_R`, where `|B_L|=|B_R|=2`.

Use all target vertices as their prescribed roots. The nonroots are:

- `y_i` of colour `c_i`, for `1<=i<=ell-1`;
- `v_L,v_R` of colour `v`, and `p_L,p_R` of colour `p`;
- `z` of colour `q`;
- `t_b` of colour `b`, for each `b in B`.

There are `ell+6` roots and `ell+8` nonroots. Take precisely the edges
of the following paths:

```text
P_(v,c_1)       = v,y_1,v_L,c_1
P_(c_i,c_(i+1)) = c_i,y_(i+1),y_i,c_(i+1)  (1<=i<=ell-2)
P_(c_(ell-1),v) = c_(ell-1),v_R,y_(ell-1),v

P_(v,b) = v,t_b,v_D,b
P_(p,b) = p,t_b,p_D,b
P_(q,b) = q,t_b,z,b                    (b in B_D, D in {L,R}).
```

Every path is simple and has length three, with no internal root. Its
colours alternate between its two target endpoints. Thus every set of
paths meeting at a vertex has its colour as a common target endpoint.
No edge occurs on two paths. In particular this is a properly coloured
scheme, and every nonroot belongs to at least two paths.

Let `J` be the graph induced by its nonroots, and set

`T_D={t_b:b in B_D}`, `U_D={v_D,p_D,z}` for `D in {L,R}`.

The graph `J` consists of two complete bipartite graphs on `(T_L,U_L)`
and `(T_R,U_R)`, sharing only `z`, together with the path

`v_L,y_1,...,y_(ell-1),v_R`.

This path has length `ell`. The bipartite portion has `v_L,v_R`
distance four. Every odd cycle in `J` therefore has length at least
`ell+4`; equality is attained. In particular `J` has no `C_ell`.

Two roots adjacent in the target have host distance exactly three.
The displayed scheme gives distance at most three. Roots are independent,
and a common nonroot neighbour of adjacent roots would give a triangle
among their target colours, which is impossible.

## Counting the required nonroots

Suppose a rooted `H_ell` model exists, with branch sets `C_w`. Each
branch set avoids every other prescribed root. The counts below allow
arbitrary nonroots in every branch set; no confinement to a target block
or original colour is assumed.

### The cycle bags require at least `ell+1` nonroots

Let `S` be the cycle vertices whose bags are singleton roots. This is
an independent set of the target cycle. A bag indexed by a cycle
neighbour of `S` needs at least two nonroots: its contact to the
singleton bag and its connectivity give a path between adjacent roots,
whose distance is three. Every other nonsingleton cycle bag needs at
least one nonroot. The total is at least

`ell-|S|+|N_(C_ell)(S)|`.

For a nonempty independent set of an odd cycle,
`|N_(C_ell)(S)|>|S|`. Counting the edges from `S` gives the weak
inequality. Equality would make every vertex of `N(S)` have both
neighbours in `S`; hence `S union N(S)` would be a whole bipartite
component of the connected odd cycle, a contradiction.

If `S` is empty and the cycle bags use only `ell` nonroots, each bag
consists of its root and one distinct nonroot. For a required cycle
contact, an edge from one root to the other bag's nonroot would give a
length-two path between adjacent roots. Thus every required contact is
between the selected nonroots, yielding a `C_ell` in `J`. This was
excluded above. In all cases the cycle bags use at least `ell+1` nonroots.

### None of `C_v,C_p,C_q` is a singleton

If `C_p={p}`, its four host neighbours `T_L union T_R` must belong to
the four different `B` bags. Root `q` has precisely the same neighbours,
so its connected bag cannot expand and is also a singleton. Each `B`
bag needs at least two nonroots to contact `C_p`, using at least eight
in total. The cycle bags use at least `ell+1` more. These are disjoint
sets of bags, requiring `ell+9` nonroots where only `ell+8` exist.
The same argument starts from `C_q={q}`.

If `C_v={v}`, its `6` host neighbours must belong to its six different
target-neighbour bags. None of those bags is `C_p` or `C_q`. Thus neither
of these two bags can contain any vertex of `T_L union T_R`, its root's
entire neighbourhood. Both must be singletons, giving the same
contradiction.

### The seven bipartite-block bags require at least ten nonroots

Singleton `B` bags occur in whole pairs. Indeed, the two roots of `B_D`
have identical host neighbourhood `U_D`. If either is a singleton,
the three vertices of `U_D` must belong to the three different `A` bags.
The other root of `B_D` can then have no nonroot in its connected bag.

**Both pairs singleton.** The bag containing `z` needs at least two
nonroots, since no `A` root is adjacent to `z`. Each other `A` bag
contains one member of `{v_L,p_L}` and one of `{v_R,p_R}`. These two
vertices are nonadjacent, neither is adjacent to an `A` root, and they
have no common nonroot neighbour. A connected bag containing its root
and these vertices consequently needs at least four nonroots. The total
is at least `2+4+4=10`.

**Exactly one pair singleton**, say `B_L`. Each `A` bag contains its
own member of `U_L` and needs at least two nonroots. If both `B_R` bags
have at least two, the total is at least ten. Otherwise a `B_R` bag is
`{b,s}`, where `s` is `v_R` or `p_R`; it cannot be `z`, already in an
`A` bag.

Consider either `A` bag containing `v_L` or `p_L`. If it had exactly
two nonroots, its additional vertex would have to be a common neighbour
of its root and its left nonroot. It is therefore in `T_L`, or it is
`y_1` when the root is `v` and the left nonroot is `v_L`. None of these
vertices, the left nonroot, or the `A` root has an edge to `{b,s}`.
This contradicts a required contact. Hence these two `A` bags each
need at least three nonroots. The total is at least `3+3+2+1+1=10`.
This argument includes contacts that might otherwise use a right nonroot
or a cycle vertex; it does not assume which contact edge is selected.

**Neither pair singleton.** Suppose the seven bags use at most nine
nonroots. Let `a` be the total excess over one nonroot in each `A` bag,
and `b` the corresponding excess in the four `B` bags. Thus `a+b<=2`.
Call a bag *small* in this paragraph if it has exactly one nonroot.
A small `B` bag uses a member of `U_L union U_R`. A small `A` bag uses
a member of `T_L union T_R`, except that `C_v` might use `y_1` or
`y_(ell-1)`. Between two small bags for adjacent target vertices every
contact must be nonroot-to-nonroot, by the distance-three observation.

- If `b=0`, the four `B` bags use four different members of `U_L union U_R`.
  Some `A` bag is small because `a<=2`. Its nonroot has at most three
  neighbours in that set, so cannot contact all four bags.
- If `b=2`, all three `A` bags are small, and at least two `B` bags are
  small. Neither end cycle vertex can serve `C_v`, since it has only
  one neighbour in `U_L union U_R`. The three distinct `A` nonroots
  are therefore in `T_L union T_R`, meeting both two-element sets.
  Their only common neighbour in `U_L union U_R` is `z`. Two different
  small `B` bags cannot both use it.
- If `b=1`, three `B` bags are small and at least two `A` bags are
  small. To contact the three distinct nonroots of those `B` bags, the
  two `A` nonroots must be exactly the two vertices of `T_D`, for one
  `D in {L,R}`, and those three `B` nonroots must be exactly `U_D`.
  Consider the small `B` bag containing `p_D`. Its root's neighbours
  are the three vertices of `U_D`, all in `B` bags. The other neighbours
  of `p_D` are the two roots of `B_D` and the two vertices of `T_D`.
  These belong to `B` bags or the two small `A` bags. There is no edge
  to the third `A` bag, a contradiction.

These exhaust the possible values of `b`. The bound of ten follows.

### Conclusion of Theorem 1

The remaining `ell-1` cycle roots have the disjoint target edges
`c_1c_2,c_3c_4,...,c_(ell-2)c_(ell-1)`. Each pair of corresponding bags
requires at least two nonroots, again by distance three. These bags
therefore require at least `ell-1` nonroots in addition to the ten in
the seven bipartite-block bags. The total is `ell+9`, exceeding `ell+8`.
No rooted model exists.

Finally, every cycle and every theta lies within a block. The blocks
of `H_ell` are its odd cycle and its bipartite `K_{3,4}`. Thus its only
odd cycle is `C_ell`, neither block contains a skewed theta, and deleting
any cycle edge makes the graph bipartite. This verifies all hypotheses
of the refuted sufficiency statement. The construction and contradiction
hold for every odd `ell>=5`, without an induction or a finite bound. QED

## Why all canonical subgraph tests pass

We give the matching argument explicitly. The sufficient two-copy test
is [1, Proposition 7.5]: if `S` is independent, a matching from `S` covers
`N(S)`, and the graph left after deleting `S union N(S)` has an
automorphism `pi` with `w pi(w)` an edge for every vertex, then the
target is `M'`-contractible. The empty graph is allowed.

To check this input directly, leave roots in `S` singleton. For each
`w in N(S)`, take the bag `{r_w,x_w,x_s}`, where `sw` is its matching
edge. On the remaining graph use `{r_w,x_(pi(w))}`. The bags are
connected and disjoint. An edge incident with `N(S)` is supplied by
its own-colour clone and the other root; every remaining target edge
is supplied by the shift automorphism's clone edge. This proves the
sufficient test with all original roots preserved.

We also recall a direct form of the bipartite matching-cover equality.
Given a maximum matching in a bipartite graph, let `Z` be the vertices
reachable by alternating paths from unmatched vertices of its first
shore. Then `(first shore minus Z) union (second shore intersect Z)`
is a vertex cover with one endpoint of every matching edge, of size the
matching. An uncovered edge or a reachable unmatched second-shore vertex
would respectively contradict reachability or give an augmenting path.
Any minimum cover `C` has that same size. Consequently every maximum
matching pairs all vertices of `C` to distinct vertices outside `C`.
This is the usual constructive proof of König's matching-cover theorem.

**Lemma 3.** Let an odd cycle `C_(2k+1)`, `k>=2`, meet an arbitrary
bipartite graph `F` in exactly one vertex `v`, with no other edges
between them. Their union is `M'`-contractible.

**Proof.** There are two exhaustive cases.

If some maximum matching `M` of `F` leaves `v` unmatched, take a minimum
vertex cover `C` of `F`. It avoids `v`, since every vertex of `C` is
matched by `M`. Put `S=V(F) minus (C union {v})`. The set `S` is
independent, `N_F(S)=C`, and `M` covers `C` from `S`. The remaining
graph of the union is precisely its odd cycle, which has the cyclic
shift automorphism. The sufficient test applies.

Otherwise every maximum matching of `F` saturates `v`. Writing `nu`
for its maximum matching size, `F-v` has maximum matching size `nu-1`.
A minimum cover `C'` of `F-v` has size `nu-1`, so `C=C' union {v}`
is a minimum cover of `F`. Put `S_F=V(F)-C`; a maximum matching pairs
all of `C=N_F(S_F)` into `S_F`.

Write the cycle as `v,c_1,...,c_(2k),v`, and set

`S=S_F union {c_1,c_3,...,c_(2k-3)}`.

This is independent. Its neighbourhood is
`C union {c_2,c_4,...,c_(2k-2)}`. Extend the matching by the edges
`c_1c_2,c_3c_4,...,c_(2k-3)c_(2k-2)`. It covers that neighbourhood;
`v` was already covered by the matching in `F`. The remaining graph
is the edge `c_(2k-1)c_(2k)`, whose endpoint swap is a shift
automorphism. Again the sufficient test applies. QED

For a bipartite target alone, taking the complement of a minimum vertex
cover as `S` gives the same sufficient test with empty remainder; this
is [1, Corollary 7.6]. Now let any subgraph of `H_ell` be given. If it
omits an edge or vertex of the odd cycle, it is bipartite. Otherwise it
is the full odd cycle together with a bipartite subgraph meeting that
cycle only at `v`, so Lemma 3 applies. Disconnected bipartite components
and isolated vertices are included in the matching-cover argument.
This proves Theorem 2 for every subgraph, not merely induced subgraphs
or schemes below a finite size. QED

## Consequences and precise limits

The universal bipartite theorem and the necessary odd-cycle-edge theorem
remain intact. The new targets have a nonbipartite block. The first false
inference in the classification proposal was sufficiency of the necessary
target conditions; the first false inference in the broader proposal was
that all canonical subgraph schemes test arbitrary schemes. Theorems 1--2
refute those inferences directly, including their existential versions.

Splitting the clones of `v` and `p` across incident paths is essential
data absent from the canonical two-copy test. A repair must account for
such actual membership choices and exclude these targets, or impose and
prove additional compatible attachment conditions. There can be no global
construction with the former classification's exact hypotheses.

No unrooted noncontractibility is asserted for `H_ell`; the obstruction
preserves every prescribed root. No failure of a spectral theorem, T44,
or Hadwiger's conjecture follows. Nor does this counterexample establish
an independent theorem comparable in significance to Norin--Totschnig.

The [retained verifier](triangle_free_bipartite_attachment_verify.py)
constructs the paths, checks their semantics and independently enumerates
all possible rooted branch sets for `ell=5`. It can emit the explicit
paths as a certificate. This is a diagnostic check of the smallest
example, not the premise of the unbounded proofs.

## Reference

[1] A. Kündgen, M. J. Pelsmajer and R. Ramamurthi, *Finding minors in
graphs with a given path structure*, Journal of Graph Theory 79 (2015),
30--47, [primary paper](https://arxiv.org/html/1207.6141),
Theorem 4.2, Proposition 7.5 and Corollary 7.6. The sufficient two-copy
test is existing input, reproduced above; the refuted sufficiency
conjectures were proposals in this repository, not claims of that paper.
