# Full-boundary fans at the final six-cut residue

**Status:** written proof for Theorems 2.1 and 3.1;
[separate internal cold audit GREEN](hc7_k7minus_six_cut_fan_model_alignment_audit.md).
Section 4 records a route nonclosure, not a counterexample.  This note does
not prove the `K_7^-` six-colour conjecture or `HC_7`.

**Revision:** the SHA-256 of this file is recorded in the adjacent audit;
any material change requires a new audit.

## 1. Setting

Let `G` be a seven-connected graph such that

\[
 \chi(G)=7,\qquad
 \chi(J)\leq6\text{ for every proper minor }J\text{ of }G,
 \qquad K_7^-\npreccurlyeq G.                         \tag{1.1}
\]

Suppose

\[
 V(G)=T\mathbin{\dot\cup}C_1\mathbin{\dot\cup}\cdots
             \mathbin{\dot\cup}C_r,\qquad
 |T|=t\in\{8,9\},\qquad r\in\{2,3\},                \tag{1.2}
\]

where the `C_i` are the components of `G-T` and every `C_i` is adjacent
to every literal vertex of `T`.  These are exactly the geometric
possibilities left by the audited
[six-cut coordinate-localisation theorem](../results/hc7_k7minus_six_cut_coordinate_localisation.md)
after all strict responses have been excluded.

For clarity, a **strict generic response** here means a nonempty connected
set `A subseteq C_i` such that

\[
             7\leq |N_G(A)|<t.                        \tag{1.3}
\]

It really does carry a colouring response.  If `ay` joins `A` to its
boundary, a proper six-colouring of `G-ay` has `a,y` equal-coloured;
deleting `A` removes that sole conflict.  Its partition on `N_G(A)` cannot
extend through the intact `A`-side, since such an extension would align
and glue to a six-colouring of `G`.

## 2. Excluding strict responses makes each shore torso highly connected

For a component `C=C_i`, put

\[
                 H_C=G[C\cup T]+\binom{T}{2}.          \tag{2.1}
\]

Thus `H_C` is obtained from the closed component-side by completing its
boundary to a clique.

### Theorem 2.1 (full-boundary linkage)

Assume that no strict generic response (1.3) exists.  Then:

1. `H_C` is `t`-connected for every component `C` of `G-T`;
2. for every nonempty connected subgraph `P` of `G[C]`, there are `t`
   paths from `P` to the `t` distinct vertices of `T`, pairwise
   vertex-disjoint outside `P` and meeting `T` only at their ends; and
3. any prescribed edges from `P` to distinct vertices of `T` may be used
   as the corresponding paths.

#### Proof

Suppose first that `Z` is a separator of `H_C` with `|Z|<t`.  Since `T`
is a clique in `H_C`, all vertices of `T-Z` lie in one component of
`H_C-Z`.  Any other component has a nonempty connected vertex set
`A subseteq C` and

\[
                       N_G(A)=N_{H_C}(A)\subseteq Z.   \tag{2.2}
\]

Another component of `G-T`, together with `T-Z`, lies on a genuine far
side of this neighbourhood.  Seven-connectivity gives
`|N_G(A)|>=7`, while (2.2) gives `|N_G(A)|<t`.  This is a strict generic
response, contrary to the hypothesis.  Hence `H_C` is `t`-connected.

For the path assertion, fix `x in V(P)`.  Since `H_C` is
`t`-connected, the Fan Lemma gives `t` paths from `x` to the `t`
distinct vertices of `T`, pairwise disjoint outside `x`.  Stop every
path at its first boundary vertex.  No added edge of the completed clique
is used before that first visit, so the truncated paths lie in the original
graph `G[C\cup T]`, with all internal vertices in `C`.

For each prescribed edge from `P` to a specified boundary end, replace
the fan path ending there by that edge.  The prescribed boundary ends are
distinct, the replacement has no internal vertex outside `P`, and
intersections inside `P` are permitted, so all the replacements are
compatible.  This proves all three assertions. `\square`

The conclusion is simultaneous on each fixed shore.  Fans chosen in
different components have disjoint open interiors automatically, although
they have the same terminal set `T`.

## 3. A coordinate response has a shore-confined prescribed six-fan

The preceding theorem does not remember the first edges of a Kempe
response.  Seven-connectivity nevertheless preserves those edges without
using the no-response assumption.

### Theorem 3.1 (prescribed response fan)

Retain (1.1)--(1.2), without assuming the absence of (1.3).  Let

\[
                         e=pv,\qquad p\in T,\quad v\in C,             \tag{3.1}
\]

and let `d` be a proper six-colouring of `G-e`.  Write
`d(p)=d(v)=\alpha`.  Then:

1. for each colour `\beta\ne\alpha`, there is an `\alpha`--`\beta` path
   from `v` to `T`, stopped at its first boundary vertex, whose internal
   vertices lie in `C`;
2. the five paths have five distinct first edges at `v`; and
3. there are six paths in `G[C\cup T]` from `v` to six distinct vertices
   of `T`, meeting `T` only at their ends and pairwise vertex-disjoint
   outside `v`, such that one path is `vp` and the other five retain those
   five prescribed first edges.

#### Proof

For `\beta\ne\alpha`, the `\alpha`--`\beta` component of `G-e` containing
`v` must contain `p`.  Otherwise interchanging the two colours on that
component would make the ends of `e` different and would six-colour `G`
after `e` was restored.  Take a `v`--`p` path in this component and stop
it at its first vertex of `T`.  Before that first visit the path lies in
`C`.  Its first neighbour of `v` has colour `\beta`, so the five alternate
colours give five distinct first edges.  This proves items 1--2.

Let `D` be the set of first neighbours which already lie in `T`, put
`h=|D|`, and retain the corresponding `h` one-edge paths.  The other
`ell=5-h` first neighbours form a set `S subseteq C-{v}`.  In

\[
               G[(C-\{v\})\cup(T-(D\cup\{p\}))]       \tag{3.2}
\]

seek `ell` pairwise vertex-disjoint paths from `S` to distinct members of
`T-(D union {p})`.  If they do not exist, Menger's theorem gives a set
`Z` of order at most `ell-1` meeting every such path.  Some source survives.
Its component `A` after deleting `Z` is contained in `C` and satisfies

\[
             N_G(A)\subseteq \{v,p\}\cup D\cup Z,
             \qquad |N_G(A)|\leq2+h+(\ell-1)=6.        \tag{3.3}
\]

A different component of `G-T` lies on a far side, so (3.3) contradicts
seven-connectivity.  The linkage therefore exists.  Prepend the five
prescribed first edges, retain the direct paths, and add `vp`.  Truncation
at the first boundary visit gives item 3. `\square`

For a singleton forest signature, the colouring in Theorem 3.1 is exactly
the proper colouring of `G-e` obtained from the common six-coordinate
host.  Hence the theorem applies to every selected coordinate whose open
end lies in one of the full components.

## 4. Model-alignment attempt and exact route nonclosure

Theorems 2.1 and 3.1 remove path existence from the final `t=8,9`
residue.  They do **not** assign the paths to the branch sets of the exact
spanning `K_7^vee` model in the forest-deletion graph.

The first unsupported inference is literal.  Distinct boundary vertices
need not belong to distinct model branch sets.  Even if six desired model
labels have representatives on `T`, forcing the response paths to those
six selected representatives is not a consequence of the proof above.
The unused boundary vertices then enter the potential separator.  With
five non-direct sources, the same Menger count becomes

\[
       |N_G(A)|\leq
       1\;\text{(the source vertex)}+
       1\;\text{(the coordinate boundary end)}+
       (t-6)\;\text{(unused boundary vertices)}+4
       =t,                                             \tag{4.1}
\]

rather than the order-six bound in (3.3).  Seven-connectivity excludes
neither an order-eight separator nor an order-nine separator.  Direct
first edges ending at an unselected boundary vertex make the prescribed-
label version fail even before this count.

There is a second, independent mismatch.  The exact spanning
`K_7^vee` model is supplied in `G-F`; a selected coordinate edge is absent
there and its ends need not lie in one branch set.  Contracting that one
edge instead gives a six-chromatic graph and hence a `K_6` model whose root
bag can be chosen to contain the contraction image, but this is a different
model.  No proved theorem identifies its five foreign labels with the six
foreign labels of the exact near-clique model while retaining the same
component and the boundary `T`.

For the one-edge model, the exact obstruction can be stated without
colour terminology.  Lift an edge-rooted `K_6` model from `G/e`, choose a
spanning tree of its root bag containing `e`, and delete `e` from that
tree.  If four of the five foreign bags meet both resulting connected
sides, the two sides and the five foreign bags form an explicit
`K_7^-`-minor model: only the fifth bag can miss one side.  Therefore every
target-free split has at most three foreign bags with contacts on both
sides.  The response fan must repair this blocked split without consuming
or disconnecting the foreign bags.  Vertex-disjointness of the fan alone
does not do that, because its paths run through a spanning model and may
take internal vertices from the very bags they are meant to preserve.

This is a **recorded route nonclosure**, not a counterexample to the
critical-host conclusion.  Existing local barriers show that first-hit
colour-to-label allocation and selected fans cannot be assumed before
minor exclusion and the universal response law are spent; they do not
realise all hypotheses of (1.1)--(1.2).  In particular, this note does not
refute a terminal fan-to-model exchange theorem.

## 5. Smallest repair theorem

The remaining statement should be made on one literal shore and one
edge-rooted model, rather than by comparing abstract palettes.

> **Boundary-respecting fan-to-model exchange target.**  In the setting
> of Theorem 3.1, choose a spanning `K_6` model in `G/e` whose root bag
> contains the contraction image, and lift and split that bag across `e`.
> Then either:
>
> 1. a label-preserving reassignment of prefixes of the shore-confined fan
>    makes at least four foreign bags adjacent to both split sides, giving
>    an explicit `K_7^-` minor;
> 2. the selected response partition extends through the intact `C`-side
>    and the two colourings glue; or
> 3. a connected proper subset of `C` has an actual neighbourhood of order
>    between seven and `t-1`, carrying a proper-minor colouring response.

Every outcome is terminal for the present `|T| in {8,9}` residue.  The
new mathematical content is the label-preserving reassignment: path
existence, exact boundary coverage, and the blocked-split count are already
proved above.

## Dependencies and scope

The only inputs are seven-connectivity, proper-minor six-colourability,
the exact residual geometry from the audited coordinate-localisation
theorem, Menger's theorem, and the established `HC_6` when the co-bagged
`K_6` model is mentioned in Sections 4--5.  No finite enumeration is used.

The route nonclosure is scoped to the proposed direct allocation of one
operation-specific fan into a pre-existing exact model.  It does not rule
out using two coordinate responses simultaneously, reselecting the model,
or exploiting the full punctured six-coordinate signature family.
