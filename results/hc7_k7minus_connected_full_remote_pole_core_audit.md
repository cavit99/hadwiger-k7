# Internal audit: centre-deletion graph and exhaustive six-cut lift

**Verdict:** **GREEN** for the promoted source revision recorded below.  This is a
separate internal mathematical audit, not external peer review.

## 1. Exact source and provenance

The promoted source is
[`hc7_k7minus_connected_full_remote_pole_core.md`](hc7_k7minus_connected_full_remote_pole_core.md),
with SHA-256

```text
a7bfb9746eb365e89d0ed3eec63aefa24a29d779744dcb3d929b3e945a567826
```

The complete mathematical text was cold-audited before promotion at
SHA-256 `7b7184454b4c2dced9c731e41834caf1561052f987df34a4a793bc0d2e7da2c2`.
Promotion changed only the status paragraph and one relative link to an
active frontier file.

The theorem was introduced in commit
`f9f3e721323bc6b433bc146e240f3ba968354579`.  A cold audit first checked
the mathematical text at that commit.  The source was then changed only to
replace metaphorical terminology, qualify the scope of a cited barrier,
remove wording that could suggest a biconditional, and correct the
dependency attribution for two clauses of (4.2).  This audit re-read the
complete pre-promotion source and checked that those edits did
not alter a hypothesis, quantifier, equation, case condition, or conclusion.

## 2. The common centre-deletion graph

Put `L=G-f` and `K=L-z`.  The named remote edge is seven-removable, so `L`
is seven-connected and deletion of one vertex leaves `K` six-connected.
Every remaining vertex loses at most one incident edge from `G`: a vertex
of `X=N_G(z)` can lose `z`, while an endpoint of `f` can lose `f`, and the
two classes are disjoint because `f` lies in `C=G-N_G[z]`.  Thus
`\delta(K)\ge7`.

Minor-criticality gives `\chi(K)\le6`.  A hypothetical five-colouring of
`K` extends to a six-colouring of `G` in both possible endpoint cases:

- if `u` and `v` have different colours, restore `f` and give `z` a fresh
  sixth colour;
- if they have the same colour, recolour `u` and `z` with the fresh colour
  and restore `f`.

The second recolouring is proper because `u` and `z` are nonadjacent and no
other vertex initially has the fresh colour.  Hence `\chi(K)=6`.  Target
exclusion descends to `K`.

Deleting the degree-eight vertex `z` and the disjoint edge `f` removes
exactly nine edges.  With `N=|V(K)|=|V(G)|-1`, this gives

```text
|E(K)| = |E(G)|-9 >= 4N-5.
```

The four-colour boundary conclusion is also valid.  If `K[X]=G[X]` had a
`K_5` model, its five bags, the connected `X`-full subgraph `C`, and the
singleton `{z}` would form a `K_7^-` model in `G`; the only possibly absent
contact is `Cz`.  Therefore `K[X]` is `K_5`-minor-free, and the established
case `HC_5` gives `\chi(K[X])\le4`.

## 3. Exact near-clique model

The graph `K` is four-connected, has order at least twenty-four, and has
more than the `4N-8` edge threshold in Norin--Totschnig Theorem 6.  Its
exception `K_{2,2,2,2}` has order eight and cannot occur.  Thus `K` has a
`K_7^\vee` model.

Making the model spanning is legitimate in the connected graph `K`.  A
contact between either nominally missing bag pair would turn the seven bags
into a `K_7^-` model, so target exclusion makes the spanning model exact.
The same argument after restoring `f` proves exactness in `G-z`: a new
missing-pair contact supplied by `f` would again give a forbidden
`K_7^-` model in `G`.  The source correctly does not identify this model
with the earlier fixed model in `H=G-T`.

## 4. Pointed signatures and palette constraint

The identity `H-z=G-z-f=K` is exact.  Hence every fixed signature colouring
`c_J` restricts to a proper six-colouring of the same graph `K`.  The kept
edges from `z` to `X-I` ensure that none of those five vertices has the
deleted-centre colour.  Exactness of the equality signature on the three
deleted star edges and on `f` therefore gives

```text
A_J = {x_i : zx_i in J},
epsilon_J = [f in J].
```

The fifteen nonempty subsets of the four-edge set `T` consequently give
exactly the fifteen pairs in (3.6), with no missing or duplicated labelled
pair.

For an arbitrary six-colouring of `K` with distinct colours on `u,v`, any
palette colour absent from `X` could be assigned to `z` after restoring
`f`, yielding a six-colouring of `G`.  Thus all six colours must occur on
`X`.  This proves (3.7) and its contrapositive.  A pure nonempty star
signature keeps `f` proper, while the `f`-only signature has the
deleted-centre colour absent from `X`; the two displayed witness patterns
are therefore correct and do not assert a converse to (3.7).

In each pure star signature, `X` has eight vertices and exactly six colour
blocks.  Its prescribed deleted-centre block is exactly `A`.  Distributing
the total excess `8-6=2` gives precisely

```text
|A|=3:  3+1+1+1+1+1;
|A|=2:  2+2+1+1+1+1;
|A|=1:  3+1+1+1+1+1 or 2+2+1+1+1+1.
```

The `f`-only boundary uses at most five colours.  Hence the asserted
six-block versus at-most-five-block separation of the two response families
is numerical and does not rely on identifying colour names across distinct
colourings.

## 5. Localisation at a six-cut

Let `S` be any six-vertex cut of `K`.  The audited six-cut localisation
theorem applies because `K` is six-connected and target-free.  It gives
`r\in\{2,3\}`, `N_K(D_i)=S`, and all the boundary sparsity conclusions in
(4.3).

The two remaining clauses of (4.2) are proved directly in the audited
source, not imported from localisation:

- a singleton component would have degree exactly six in `K`, contrary to
  `\delta(K)\ge7`;
- if a component missed `X-S`, it would remain separated from the other
  components after deleting `S` from the seven-connected graph `G-f`.

Distinct components meet disjoint vertices of `X-S`, so
`r\le|X-S|=8-|S\cap X|`.  If `|E(G)|\ge4|V(G)|+3`, then the exact
nine-edge deletion count gives `|E(K)|\ge4|V(K)|-2`, which is precisely the
extra density hypothesis for the sharpened `11`- and `8`-edge boundary
bounds.

## 6. Exhaustiveness of the lift

Deleting `Q=S\cup\{z\}` from `G` produces `K-S` with only the edge `f`
restored.  The proof considers every possible placement of the ends of
`f` relative to `S,D_1,D_2,D_3`.

### Three components

If `r=3`, restoring one edge can merge at most two components, so `Q`
remains a seven-vertex cut.  The audited three-component seven-cut
exclusion says that `G-Q` has exactly two components.  Consequently both
ends of `f` lie outside `S` in two distinct `D_i`, and `f` merges exactly
those two.  Seven-connectivity makes both resulting components full at
`Q`.  In the `f`-only colouring the sole restored conflict lies in the
merged open component, so the opposite closed-side restriction is proper.
An extension of its boundary partition through the merged side would glue
to a six-colouring of `G`.  This proves outcome 1 with its original
operation label.

### Two components, with `f` crossing

If the ends of `f` lie in different components, say `u\in D_1` and
`v\in D_2`, each component meets `X-S`.  Fullness in `K`, that contact
with `X`, and the single restored edge give the exact neighbourhoods

```text
N_G(D_1)=S ∪ {z,v},
N_G(D_2)=S ∪ {z,u}.
```

Both displayed sets are actual cuts because each opposite component has at
least two vertices.  Removing either selected component deletes one end of
the sole conflict in `c_{\{f\}}`; thus the one fixed colouring is proper in
both opposite orientations.  Matching either boundary partition through
the corresponding intact component would six-colour `G`.  The two
overlapping order-eight separations and their exact seven-vertex overlap
are therefore valid.

### Two components, without `f` crossing

If `f` does not join the two components, then `Q` is an order-seven cut
with the same two open components.  There are exactly three exhaustive
endpoint alternatives:

1. if `V(f)` is not contained in `S`, the edge `f` has an end in one open
   component and is absent from the opposite closed side;
2. if `V(f)` is contained in `S` but `I` is not, some star edge `zx_i`
   has an end in one open component and is absent from the opposite side;
3. otherwise `I\cup\{u,v\}` is contained in the six-set `S`.

In each of the first two alternatives, the singleton-signature colouring
for the selected edge has no restored conflict on the opposite closed side,
and the standard partition-gluing argument proves rejection through the
selected component.  In the last alternative, the five vertices in
`I\cup\{u,v\}` are distinct, so `S` consists of those five vertices and
one additional vertex.  All four operation edges lie in the common
boundary `Q`, and every nonempty fixed signature therefore retains a
monochromatic boundary edge on both closed sides.  Since
`V(K)=X\mathbin{\dot\cup}C`, the two possibilities for the final vertex give
exactly the two intersection vectors in (4.8A).

These alternatives are mutually exclusive.  They also cover the cases in
which one or both ends of `f` lie in `S`; no endpoint placement or operation
label is omitted.

## 7. Dependency and link check

The positive local dependencies match their adjacent GREEN audits at these
source hashes:

```text
2f7c69fd57319f898d84c9884907ac70e3e1f2064b3a5753d19da8531406ecf9  remote removable-edge operation cube
5bc54f3b7f4cbe68a7b3c35a35d16c693672cfbffa17686f65008938cdfc3865  remote-interface topological reduction
f2a4480d27556996620117a68a8a7924dd61cf37bf5ec9e8cce4c953dfcc88af  exact six-cut localisation
1041988a33b749bef5802dd21d3cd9419b5afc754735a20174bf5a13c0a56c96  three-component seven-cut exclusion
```

Norin--Totschnig Theorem 6 has exactly the form used: a four-connected
graph with at least `4|V|-8` edges has a `K_7^\vee` minor unless it is
`K_{2,2,2,2}`.  The use of `HC_5` is the established implication that a
`K_5`-minor-free graph is four-colourable.

Every local link and section anchor in the source resolves.  The files
cited in Section 2 are explanatory barriers or route limitations, not
positive dependencies of Theorems 3.1 and 4.1.  The common-portal sentence
now accurately limits that barrier to the specific surrogate construction
it refutes.

## 8. Terminology and unresolved scope

The audited source replaces the earlier metaphorical terms `lock`, `row`,
`state`, `ghost`, `pole`, `bow-tie`, and `trapped` with standard descriptions
of colouring constraints, cases, signatures, the deleted-centre colour,
and overlapping or boundary-contained separations.  The edits preserve the
mathematical content and bring the new theorem statement into the repository
terminology policy.

The result does **not** eliminate any of the following surviving cases:

- the seven-connected common graph `K`;
- the two overlapping order-eight separations;
- the boundary-contained five-endpoint order-seven cut; or
- the operation-labelled exact-seven return supplied by outcome 1.

It does not align a response partition with either exact minor model, assign
the missing model contacts to `f` or a deleted-centre trace, prove the bare
seven-connected extremal theorem, prove the `K_7^-` six-colour conjecture,
or prove `HC_7`.  It inherits the trust boundaries of its separately audited
inputs, including the earlier finite classifications used upstream in the
remote-interface reduction.  No new computation is used in this theorem.

No unresolved assumption or mathematical gap was found at the pinned source
revision.
