> **Archived working draft, 21 September 2026.** Superseded by the
> [standalone extremal theorem and C21 proof](../results/hc7_k7minus_bilight_extremal.md).
> This preserves the exploratory deductions and earlier dependency choices.
> The standalone proof includes a direct six-connected degree-six argument
> and the precise DNR Theorem 1.6 citation; use that result for current claims.
> Before archival annotations and relative-link repairs, this draft had SHA-256
> `26aff1304f1acb7e101fdd6284fc5dc19b4b1ea22363ca991f1c90def4da2df5`.

# Global composition of the proved rooted helper theorem

**Status, 21 September 2026:** complete written global proof awaiting
independent audit. Sections 7--10 supply the degree and end arguments
which resolve the earlier contraction obstruction recorded below. This
is the working draft for the [selected construction](../active/hc7_c21_rooted_density_construction.md),
not a second frontier. No audited completion of C21 or claim of HC7 is
made here.

## 1. Hypothesis and induction class

The separately audited [rooted helper theorem](../results/five_root_one_missing_contact.md),
abbreviated **H2**, states that every 4-light five-rooted graph of rooted 4-density at
least two contains five prescribed root bags and two root-free helper
bags with at most one absent contact among the eleven pairs incident
with a helper. Root–root contacts are not required.

For unrooted graphs put `rho(G)=e(G)-4v(G)`. A graph is 4-bilight if
there are no disjoint nonadjacent nonempty vertex sets `S,T`, each
with at most four external neighbours and with positive incident
4-density. Consider a graph `G` minimal lexicographically in
`(v(G),e(G))` among 4-bilight, `K7^-`-minor-free graphs satisfying
`v(G)>=3` and `rho(G)>=-2`.

The theorem proved below says no such `G` exists. It implies C21
by the seven-connectivity and density reduction. Proper minors are used
only within this explicitly stated density/bilight class; no colouring
criticality is inherited.

The reusable external machinery is Dvořák–Norin–Rahman
[2609.17760v1, Sections 3–5](https://arxiv.org/html/2609.17760v1#S3):
their maximal reducible-fragment replacement preserves 4-bilightness and
does not decrease density (Lemma 3.3); their small-root extraction and
linkage arguments are Observation 4.1 and Corollary 4.2. Their
Theorem 2.6 supplies the labelled five-root density targets. The primary
proofs were inspected. Below, ``heavy'' means density at least two,
not their broader ``quite heavy'' condition.

## 2. A valid conditional orientation and edge-deletion reduction

**Conditional proposition.** Assuming H2, the minimal graph `G` above
has the following properties.

1. It has no reducible fragment in the sense of DNR Section 3.
2. For every five-separation with boundary `X`, exactly one side has
   rooted density at least two. If `m=10-e(G[X])`, that side has
   density at least `m+7`.
3. There are no nonadjacent disjoint positive-density fragments of
   boundary order at most five when every order-five member has
   density at least two.
4. `e(G)=4v(G)-2`.

**Proof.** A maximal reducible-fragment replacement is a proper minor,
retains at least three vertices, preserves 4-bilightness and does not
decrease `rho`. Its stored rooted branch sets lift every later minor.
It decreases vertex count, proving item 1 by minimality.

The proofs of DNR Corollary 5.3 and Lemma 5.4 apply with ``density at
least two'' in place of ``quite heavy'': H2 supplies a helper graph
which contains one of their allowed rooted graphs, so the same
small-root extraction applies. In particular, the side opposite a
heavy five-rooted side is 4-light. This invocation uses no density-one
case of H2.

Write the two side densities of a five-separation as `a>=b`. Exact
accounting gives

```text
a+b = rho(G)+20-e(G[X]) >= m+8.
```

Thus `a>=ceil((m+8)/2)>=4`. If `b>=2`, both sides are 4-light. The
larger side has a full rooted K5 by DNR's labelled density targets
(already `ceil((m+3)/2)` suffices), while H2 applies to the other
side. Glue corresponding root bags across their common prescribed
root. The five resulting bags are connected and pairwise adjacent;
the two helper bags stay entirely in their own open side. They give
`K7^-`. Consequently `b<=1` and `a>=m+7`, proving item 2.

The consistent-orientation argument of DNR Lemma 5.9 now applies to
two heavy five-fragments. If no five disjoint paths join their closed
sides, a separation of order at most four contradicts the preceding
small-root extraction argument. Otherwise trim the five paths to have
interiors outside both fragments, apply H2 on one side and the full
rooted K5 just obtained on the other, and join corresponding bags
along the paths. Each path has a different end at each five-element
boundary; the interiors are disjoint and belong to their own joined
root bag. This gives `K7^-`. A heavy five-fragment and a positive
fragment of boundary at most four contradict the opposite-side
lightness above. Two smaller positive fragments contradict
4-bilightness. This proves item 3, including the required consistency.

Suppose `rho(G)>=-1` and delete an edge `uv`, obtaining `J`. Minimality
forces `J` to have a dense bifragment `(S,T)` of boundary at most four.
Unless it already contradicts 4-bilightness in `G`, exchange `S,T`
so that `u in S` and `v` is outside `S` and its boundary in `J`.
Then `|N_G(S)|<=5` and `rho_G(S)=rho_J(S)+1>=2`.

Put `S'=S-{u}`. At most five edges join `u` to `N_G(S)`, and

```text
rho_G(S') = rho_G(S)+4-e_G({u},N_G(S)).
```

Also `|N_G(S')|<=|N_G(S)|`. If `S` has boundary at most four,
then `rho_G(S')>=rho_G(S)>0`; choose the labels so that `T` also has
boundary at most four when `v in T`. This contradicts 4-bilightness.
Otherwise `S` has boundary five, so item 2 gives `rho_G(S)>=7` and
`rho_G(S')>=6`. The pair `(S',T)` is nonadjacent in `G` because the
only restored edge was incident with `u`. The density of `T` stays
positive, and is at least two if its boundary becomes five.
Item 3 gives a contradiction. Hence `rho(G)=-2`. QED

The external reduction and each model composition above have genuine
minor lifts; their use does not repair the contraction case below.

## 3. The contraction obstruction requiring a further argument

Contract `uv`, where `uv` has at most three common neighbours. Then
`rho(G/uv)>=rho(G)`. Following DNR Lemma 6.2, a failure of
4-bilightness can be localized to positive fragments whose boundaries
contain the contracted vertex. When a boundary grows from four to five
on lifting, its density changes by the number of common neighbours of
`u,v` in the fragment.

The case not excluded by Section 2 alone is a lifted five-fragment `Z` with

```text
rho_G(Z)=1,
u,v in N_G(Z),
no vertex of Z adjacent to both u and v.
```

Item 3 does not exclude such a fragment. No induction on H2
H2 applies to it. The extra five units in the global density threshold
strengthen item 2, but do not alter this exact local density calculation.

Extending H2 to this class is false. Take roots `a,b,c,d,e`, add the
root edge `ab`, and add adjacent nonroots `p,q`. Let `p` meet exactly
`a,c,d,e` among the roots and `q` meet exactly `b,c,d,e`. This graph is
internally five-connected as a rooted graph: the two singleton nonroot
sets and their union all have boundary five. Its rooted density is one;
no nonroot meets both `a,b`. It has only nine helper contacts, and its
seven vertices force every bag of a seven-bag model to be a singleton.
It cannot satisfy the ten-contact conclusion. Contracting `ab` makes
`{p,q}` a positive fragment of boundary four and density one.

This refutes that local extension only. It is not a counterexample to
H2, the global density statement or C21. A replacement theorem must
either absorb such fragments while preserving 4-bilightness and the
global density budget, or exploit their interaction with the opposite
side of density at least `m+7` to construct the target. Sections 7--10
instead exclude all five-cuts of the minimum global graph; they do not
assert the false local density-one extension.

## 4. A compatible final-step repair

There is also a useful replacement for directly strengthening the
neighbourhood lemma in DNR Section 6.

**Conditional local lemma.** Suppose `v` is a vertex, `X` is a five-set
in `N(v)`, `G[N(v)]` has a K5-minus-edge model rooted at `X`, and a
component `C` of `G-N[v]` has boundary exactly `X`. If
`G[C union X]`, rooted at `X`, is 4-light and has density at least two,
then H2 gives a `K7^-` minor in `G`.

**Proof.** Add `v` to an endpoint bag of the missing edge of the rooted
neighbourhood model. Since `v` meets every vertex in that model, this
makes a full rooted K5. Apply H2 inside `C union X`, and glue the five
corresponding root bags. Their only shared vertices before gluing are
the prescribed roots; the helpers avoid `X` and lie in `C`. Thus all
seven final bags are connected and disjoint, with at most one absent
contact. QED

This uses the centre to repair the root clique while retaining two
helpers from the component. It does not justify lightness of that
component, handle boundaries of order six or seven, or resolve the
density-one contraction case.

## 5. The two-component six-cut: an actual terminal family

**Sixth-root augmentation lemma.** Let `(F,S)` be internally
six-connected, with `S=Z union {x}` and `|Z|=5`. If `F` has an H2-type
model rooted at `Z`, it has one with `x` in a helper bag.

**Proof.** Maximise the total number of vertices in the two helper bags;
subject to this, minimise the total order of the root bags. Each root
bag can be taken to have a single vertex adjacent to the helper union.
For a bag meeting both helpers, otherwise a minimal tree joining its
root and two distinct helper-contact vertices has a nonroot leaf which
can be transferred to the helper it meets, while the remaining bag
keeps both contacts. For a bag meeting only one helper, use a shortest
root-to-contact path; a second contact would allow shortening that path
and transferring its terminal part to the helper. Both operations
contradict maximality. An unused component meeting either helper could
also be absorbed into that helper. Consequently the external boundary
of the helper union has order at most five. If `x` is outside that
union, it is a nonempty root-free side of an order-at-most-five root
separation of `(F,S)`, a contradiction. QED

The argument allows the helpers to be nonadjacent, and preserves the
actual missing-contact budget. No root–root contacts are used in it.

**Conditional complete case.** Assume H2. Let `G` be six-connected with
`e(G)>=4v(G)`, and let a six-cut `S` have exactly two components `A,D`.
If `G[S]` contains a literal K4, then `G` has a `K7^-` minor.

**Proof.** Suppose the target is absent. The
[six-cut localisation theorem](../results/hc7_k7minus_exact_six_cut_localisation.md)
gives `b=e(G[S])<=11`. Put
`eta(C)=e(G[C])+e_G(C,S)-4|C|`. Since
`eta(A)+eta(D)>=24-b`, exchange the components so that `eta(A)>=7`.
Let `Q` be the four-clique and write `S-Q={x,y}`.

Root `F=G[A union S]` at `Z=S-{x}`. The
[retained-sixth-vertex calculation](../results/hc7_five_root_density_sixcut.md#2-retaining-the-sixth-vertex)
uses only six-connectivity and a nonempty opposite component, so applies
also here: `F` is 4-light and
`rho4(F)=eta(A)+d_{G[S]}(x)-4>=3`. H2 gives the seven-bag model, and
the augmentation lemma places `x` in one helper, say `P`; call the
other helper `U`. The five root bags are `R_y` and `R_q` for `q in Q`.

Replace `R_y` by `R_y union D`. This is connected because `D` meets
`y`. It meets every `R_q` through the prescribed root `q`, and it
meets `P` through `x`. The four `R_q` are mutually adjacent through
the literal K4. All contacts involving `U` and the other contacts
involving `P` are supplied by the H2 model, with at most one defect.
The resulting seven bags are connected, disjoint and give `K7^-`. QED

## 6. Why the six-root augmentation does not close every boundary

There is an exact obstruction to inferring the target from just the
augmented helper model and the opposite full component. On six roots
`0,...,5`, let the boundary nonedges be

```text
03, 13, 12, 45.
```

Thus the boundary has eleven edges and its complement is `P4 + K2`.
Take `x=1` as the root in a helper, supply the other helper `a`, and
let `d` represent the opposite full component. Give `a,d` every root
contact, leave `ad` absent, and let the rooted helper at `x` meet
every other root except `2`. This satisfies the at-most-one-defect H2
contact condition; the helper pair `x,a` is adjacent.

The resulting eight-bag graph is exactly `K_{2,2,2,2}`, whose four
nonedges are `03,12,45,ad`. It has no `K7^-` minor: it has 24 edges,
every vertex has degree six and every edge has four common neighbours.
Deleting a vertex leaves 18 edges, while contracting an edge leaves
19; either operation is necessary to obtain seven nonempty bags, and
the target needs 20 edges. This also rules out all smaller supporting
vertex sets.

This is a barrier to composition from the recorded bag contacts. It is
not a six-connected `4n` counterexample: the required original-shore
density is not asserted for this quotient. A successful proof must use
the component interiors or density to exclude this defect placement,
or reselect models with extra contacts. Obtaining two arbitrary H2
models does not fix it: they may both leave the root contact `12`
absent after their `x`-rooted helper bags are merged.

The immediate critical quotient has a further useful but limited fact.
For `H=G/vx`, every six-cut of `H` contains its contracted vertex, and
its seven-vertex preimage is a cut of `G` with the same components.
[Corollary 2 of the audited critical seven-cut theorem](../results/hc7_k7minus_three_component_seven_cut_exclusion.md#corollary-2-two-component-normal-form-in-the-critical-host)
therefore makes every such cut a two-component cut. This cannot be
applied after replacing `H` by an arbitrary smaller density
counterexample; no reduction forcing a six-cut while retaining this
provenance has been established here.

## 7. The global minimum graph is five-connected

**Proposition.** Subject to the unaudited global deductions in Section 2,
the minimum graph `G` has minimum degree at least five and is ordinarily
five-connected.

**Proof.** If `d_G(v)<=4`, then `J=G-v` has density at least `-2`.
The density bound on `G` forces `|V(G)|>=9`, so the order condition is
retained. If `J` has a positive bifragment `(A,B)` with both boundaries
of order at most four, the same sets are disjoint and nonadjacent in
`G`. A boundary that grows to order five acquires the neighbour `v`,
and its density increases by at least one, to at least two. A boundary
that stays of order at most four remains positive. Section 2(3) excludes
every such pair. Thus `J` is 4-bilight, contrary to minimum order.
This proves the degree bound.

Suppose next that `G` has connectivity `k<=4`. Choose a minimum cut
`S` of order `k`, including `S=emptyset` when `G` is disconnected.
Every component of `G-S` has neighbourhood exactly `S`. At least one
component `A` has nonpositive incident density, since two positive
components would violate 4-bilightness. The rooted graph
`R=G[A union S]`, rooted at `S`, is internally `k`-connected: a
nonempty subset of `A` with smaller boundary would give a cut of `G`
of order below `k`. Its nonroots retain their original degrees, at
least five, and all roots meet its connected interior `A`.

For `k<=2`, connectedness gives the boundary-rooted clique directly.
For `k=3`, the [audited rooted triangle lemma](../results/hc7_c21_rooted_density_low_degree_reduction.md#a-rooted-triangle-lemma)
gives it. For `k=4`, the [audited degree-five dart lemma](../results/rooted_dart_nonroot_degree_five.md)
gives a rooted dart; here `|A|>=2` because every original degree is at
least five. An opposite component together with `S` has at least six
vertices, again by the degree bound. Therefore `A` satisfies all the
conditions of a reducible fragment, contrary to Section 2(1). QED

This proposition by itself does not raise the minimum degree to six. A
degree-five vertex with a complete neighbourhood is terminal: any
component outside its closed neighbourhood is full to that five-clique
by five-connectivity; the component and the singleton vertex are the
two helpers. The noncomplete-neighbourhood split-off argument returns a
density-one five-fragment. The quasi-five-connectivity lemma handles
this fragment when it has at least three vertices, but the two-vertex
case is handled by the additional construction in Section 9.

## 8. A low-density five-fragment contains a low-triangle edge

**Proposition.** Suppose in addition that the minimum graph has minimum
degree at least six. If `A` is a five-fragment with `rho_G(A)<=1`,
some edge with an endpoint in `A` has at most three common neighbours
in `G`.

**Proof.** Write `S=N_G(A)` and `a=|A|`. Since

`rho_G(A)=sum_{v in A}d_G(v)-e(G[A])-4a`
`>=2a-binomial(a,2)`,

one has `a>=5`. Double counting gives

`sum_{v in A}(d_G(v)+d_S(v))=8a+2rho_G(A)<=8a+2`.

Choose `v in A` with `d_G(v)+d_S(v)<=8`. Suppose that every edge at
`v` has at least four common neighbours. In `G[N_G(v)]`, delete the
edges between vertices of `X0=N_G(v) intersect S`. Its vertices outside
`X0` still have degree at least four; vertices in `X0` have degree at
least `5-|X0|`. The audited rooted star lemma applies because
`|N_G(v)|+|X0|<=8`, with five prescribed vertices containing `X0`.

The rooted graph `G[A union S]` is internally five-connected. Hence
five disjoint paths from `S` to `N_G(v)` may be chosen with interiors
outside `N[v]`, and with trivial paths for `X0`. Apply the star lemma
at their five ends. Its central bag avoids `S`. Use that bag and
`{v}` as helpers, retain the four other paths as root bags, and remove
the final vertex from the central path. The trimmed path is nonempty
because its end is not a root. This gives an H2 contact model rooted
at `S`, wholly inside `A union S`, without using any artificial root
edge.

The opposite side is internally five-connected and has density at
least `m+7`, where `m=10-e(G[S])`, by Section 2. DNR Theorem 2.6
therefore gives a full clique rooted at `S` in that side. Gluing the
corresponding root bags gives `K7^-`, a contradiction. QED

This proves the required edge existence only for the low orientation
of a five-cut. Every five-fragment contained properly in such an `A`
is also low: a heavy one would be disjoint and nonadjacent to the
heavy opposite side of `A`, contrary to Section 2(3). However, an atom
chosen over all fragments whose boundaries contain a low-triangle
edge can have the high orientation. An atom chosen only over low
fragments does not satisfy Mader's ordinary minimum-atom hypothesis.
Padding a fixed high side also need not preserve the cuts blocking
new edges. Section 10 instead uses inclusion-minimal fragments and
proves the exact local end lemma it needs; no global atom theorem is
invoked.

## 9. Degree-five vertices are excluded

**Conditional proposition.** Assuming H2, the minimum graph `G` of
Section 1 has minimum degree at least six.

**Proof.** Use Sections 2 and 7: `G` is five-connected, has minimum
degree at least five and order at least nine, satisfies
`e(G)=4v(G)-2`, and admits no pair of disjoint nonadjacent positive
fragments of boundary at most five if each order-five member has
density at least two. Thus whenever two such positive fragments
occur, at least one has boundary five and density exactly one.

We use the separately audited
[localized quasi-five-connectivity lemma](../results/hc7_c21_helper_degree_six.md):
if a five-fragment `A` has at least three vertices, its opposite open
side has at least two vertices, and a boundary vertex `x` has a unique
neighbour `a` in `A`, then `G/xa` is quasi-five-connected. Here this
means four-connected with no four-cut whose two open sides both have
at least two vertices. The result includes the localized proof of
Kou--Qin--Yang--Zhang--Zhao, Lemma 1, rather than importing its stronger
global hypotheses.

Every quasi-five-connected graph is 4-bilight. Indeed, in a dense
bifragment both open sets have boundary four and at least two
vertices: a singleton with boundary four has density zero. The
boundary of either set would therefore be a forbidden nontrivial
four-cut. Contracting an edge with `t` common neighbours changes
`e-4v` by `3-t`. Consequently a quasi-five-connected contraction with
`t<=3` contradicts minimality. All contractions below retain at least
eight vertices, and a minor of `G` remains `K7^-`-minor-free.

We will also repeatedly use the following cut observation. For any
edge `xy` of a five-connected graph, `G/xy` is four-connected and every
four-cut contains the merged vertex. A four-cut avoiding that vertex
would lift to a four-cut of `G`. Hence, in any dense bifragment of
`G/xy`, the merged vertex lies on both boundaries, not in either open
set. Lifting either boundary gives a five-cut containing `x,y`; a
smaller boundary would contradict five-connectivity of `G`. The two
open sets remain disjoint and nonadjacent on lifting, their densities
do not decrease, and either opposite open side contains the other
positive fragment, which has at least two vertices.

Suppose `d_G(v)=5`. If `G[N(v)]` is complete, take a component `C`
outside `N[v]`, which exists since `|V(G)|>=9`. Its boundary is
contained in `N(v)` and five-connectivity forces equality. The five
singleton vertices of `N(v)`, together with `{v}` and `C`, give a
`K7^-` model: only the contact between the last two bags is absent.

Otherwise choose a missing pair `ab` in `N(v)` and set
`J=G-v+ab`. This is a minor: contract `va` and delete the additional
edges at `a` except `ab`. Its density is still `-2`, so minimum order
forces a dense bifragment `(Y,Z)` in `J`. Both sets remain nonadjacent
in `G`, their boundaries have order at most five, and their densities
remain positive. To check the last assertion, put
`k=e_G(v,Y)` and let `c` indicate whether `ab` has an endpoint in `Y`.
Then

```text
rho_G(Y)=rho_J(Y)+k-c,
```

and `c=1` implies `k>=1`; the same applies to `Z`. The exclusion from
Section 2 therefore lets us choose `Y` with boundary five and
`rho_G(Y)=1`. Its boundary grows on restoring `v`, so `k>=1`, and the
displayed identity forces `rho_J(Y)=k=c=1`. Exchange `a,b` if needed:
`a` is the unique neighbour of `v` in `Y`, and `b` belongs to both
boundaries of `Y`. In particular, `|Y|>=2`, since `ab` is absent in
`G`. The opposite open side of `Y` in `G` contains `Z` and hence has
at least two vertices.

If `|Y|>=3`, the localized lemma makes `va` quasi-five-contractible.
Since `v` has degree five and its neighbour `b` is not adjacent to
`a`, the edge `va` has at most three common neighbours, a contradiction.
Thus write `Y={a,c}`. The identity

```text
1=rho_G(Y)=d_G(a)+d_G(c)-e(G[Y])-8
```

and minimum degree five force `ac` to be an edge and both degrees to
equal five. As its boundary has order five, this pair has three common
neighbours, denoted by `R`, and its complete neighbourhoods are

```text
N(a)={c,v} union R,       N(c)={a,b} union R,       |R|=3.
```

The edge `vb` is present because `b` was chosen in `N(v)`.

Contract `ac`, which has exactly three common neighbours. Minimum
order again forces a dense bifragment. By the cut observation, its
lifted open sets are positive five-fragments. Choose a density-one
member `T`. Its density on lifting increases by the number of common
neighbours of `a,c` in it, so it avoids `R`. Since both `a,c` belong
to its lifted boundary, it contains `v,b`. Moreover, `a` has the
unique neighbour `v` in `T`, and its opposite open side has at least
two vertices. If `|T|>=3`, the localized lemma applies to `av`;
the missing edge `cv` again bounds the common-neighbour count by
three. Thus `T={v,b}`. The same degree calculation now gives

```text
N(v)={a,b} union D,       N(b)={c,v} union D,       |D|=3.
```

We have four degree-five vertices inducing the cycle `a,c,b,v,a`.
The triples `R,D` avoid these four vertices. If `|R intersect D|>=2`,
the cycle has at most four external neighbours; its outside is
nonempty since the graph has order at least nine, contradicting
five-connectivity.

If `|R intersect D|=1`, set `S=R union D` and
`U={a,c,b,v}`. Then `|S|=5` and `rho_G(U)=0`. The opposite open side
`W=V(G)-(U union S)` has density

```text
rho_G(W)=18-e(G[S])>=8.
```

This identity also shows `W` is nonempty. Its closed shore, rooted at
`S`, is internally five-connected and therefore 4-light. DNR
Theorem 2.6 supplies a full clique rooted at `S`. The disjoint
connected bags `{a,v}` and `{c,b}` are adjacent and both meet every
vertex of `S`. Together with the five rooted clique bags they give a
`K7` model, again a contradiction.

It remains that `R,D` are disjoint. We claim that every five-cut `L`
containing `a,v` also contains `c,b`. If `c` lies in one open side
of such a cut, all of `R` lie in that side or in `L`, because they
are neighbours of `c`. Then `a` has no neighbour in the opposite
open side: its neighbours are `c,v` and `R`. Removing `a` from `L`
still separates that opposite side, contradicting five-connectivity.
Thus `c in L`. The same argument applied to the pair `v,b` forces
`b in L`.

Now `av` has no common neighbour. If `G/av` were 4-bilight, its density
surplus of three would contradict minimum order. Take a dense
bifragment there. By the cut observation and the preceding claim,
both lifted five-boundaries contain all of `a,c,v,b`; both open sets
avoid those four vertices. Each open set meets both `R` and `D`,
because its boundary includes `a` and `v`. Since the sets are
disjoint and `|R|=3`, choose one of them, say `B`, containing exactly
one vertex `r` of `R`.

The set `B` is not a singleton, because its image is a positive
fragment of boundary four. It also cannot have order two. Otherwise
`B={r,d}` with `d in D`, while its boundary consists of the four
cycle vertices and one further vertex `z`. The vertex `r` is adjacent
to neither `v` nor `b`, by the displayed neighbourhoods and
`R intersect D=emptyset`. All its possible neighbours would therefore
lie in `{a,c,d,z}`, contrary to minimum degree five.

Thus `|B|>=3`. Its opposite open side contains the other positive
fragment and has at least two vertices. The boundary vertex `a` has
the unique neighbour `r` in `B`. The localized lemma makes `ar`
quasi-five-contractible; moreover, it has at most three common
neighbours because `d(a)=5` and `v` is a neighbour of `a` not adjacent
to `r`. This final contraction contradicts minimum order. Every
degree-five case has been excluded. QED

All minor lifts in this proof use the fixed contracted edge as the
preimage of its merged vertex. The two terminal constructions above
give explicit disjoint connected bags. This proposition closes the
degree-five obstruction in Section 7. The remaining contraction and
fragment-selection arguments are supplied next.

## 10. Ends exclude every five-cut, and finish the proof

**Local end lemma.** Let `J` be a five-connected graph in which every
ordinary five-fragment has at least four vertices. Let `F` be any family
of edges. Call a five-fragment an `F`-fragment when its boundary contains
both endpoints of an edge of `F`, and call it an `F`-end when it contains
no proper `F`-fragment. If `A` is an `F`-end, there is no edge `e in F`
which meets `A`, has both endpoints in `A union N_J(A)`, and has both
endpoints in a five-cut of `J`.

**Proof.** Put `S=N_J(A)` and `C=V(J)-(A union S)`. Suppose that a
five-cut `T` contains such an edge `e`. Partition `J-T` into two
nonempty unions of components, `B,D`. Write

```text
p=|A intersect T|,  s=|S intersect T|,  r=|C intersect T|,
u=|S intersect B|,  w=|S intersect D|.
p+s+r=u+s+w=5,       p+s>=2.
```

The last inequality holds because both distinct endpoints of `e` lie
in `(A intersect T) union (S intersect T)`. At least one lies in `A`.

If `A intersect B` is nonempty, its neighbourhood is contained in
`(A intersect T) union (S intersect T) union (S intersect B)`.
The displayed containing set cannot have order at most five. Order
below five contradicts five-connectivity; order five forces equality
with the actual neighbourhood and gives a proper `F`-fragment in `A`,
because it contains both endpoints of `e`. Properness holds because
`A intersect T` is nonempty. Thus

```text
p+s+u>=6, hence p>w and u>r.
```

The opposite corner `C intersect D` has neighbourhood contained in
`(C intersect T) union (S intersect T) union (S intersect D)`, of
order `r+s+w=5+r-u<5`; therefore it is empty. Symmetrically,
`A intersect D` nonempty implies `p>u`, `w>r`, and
`C intersect B` empty. The relevant complementary corner is always
separated from a nonempty opposite corner, so each use of
five-connectivity is a genuine separation.

If both `A`-corners are nonempty, both `C`-corners are empty. Then
`C subset T`, so `r=|C|>=4`, contrary to `p+s>=2` and `|T|=5`.

If only `A intersect B` is nonempty, then `D=S intersect D`, so
`w=|D|>=4`. The inequality `p>w` forces `p=5` and `r=s=0`.
Consequently `C=C intersect B` has neighbourhood contained in
`S intersect B`, whose size is `u=5-w<=1`, a contradiction.
The other one-corner case is symmetric.

Finally suppose that neither `A`-corner is nonempty. Then
`A subset T`, so `p=|A|>=4`. A nonempty `C`-corner, say
`C intersect B`, has neighbourhood of order at most `r+s+u`;
five-connectivity gives `u>=p>=4`. The other `C`-corner must be
empty, since otherwise also `w>=p>=4`, contrary to `u+w<=5`.
It follows that `D=S intersect D`, giving `w=|D|>=4` and the same
contradiction. At least one `C`-corner is nonempty because
`|C|>=4` whereas `r<=1`. These cases exhaust the possibilities. QED

**Proposition.** The minimum graph `G` has no five-cut.

**Proof.** By Section 9, every degree is at least six. A singleton
five-fragment is therefore impossible. For a five-fragment of order
`a=2` or `a=3`, counting degrees and possible incident edges gives

```text
2a-binomial(a,2) <= rho_G(A) <= binomial(a,2)+a.
```

For `a=2` its density is exactly three, and for `a=3` it lies
between three and six. Neither fits Section 2's alternatives:
every five-fragment has density at most one or at least seven.
Thus all ordinary five-fragments have at least four vertices.

Let `F` be the family of edges having at most three common neighbours.
Every `e in F` has its endpoints in a five-cut bounding a fragment
of density one. Indeed, its contraction retains density at least
`-2` and decreases order, so is not 4-bilight. As in Section 9's cut
observation, a dense bifragment lifts to two positive five-fragments
whose boundaries contain both endpoints of `e`. Section 2(3)
forces at least one lifted density to equal one.

Suppose a five-cut exists. It has a low side by Section 2, and
Section 8 supplies an edge of `F`. The preceding paragraph then
supplies a low `F`-fragment. Choose one, `A`, inclusion-minimal among
low `F`-fragments. It is an `F`-end in the ordinary, unrestricted
sense. For if an `F`-fragment `B` were properly contained in `A`,
a heavy `B` would be disjoint and nonadjacent to the heavy opposite
side of `A`, contrary to Section 2(3). Thus `B` would be low,
contrary to the choice of `A`.

Section 8 supplies an edge `e in F` with an endpoint in `A`; its
other endpoint necessarily lies in `A union N_G(A)`. Its certifying
five-cut was established above. The local end lemma now gives a
contradiction. Hence there is no five-cut. QED

**Theorem.** Every 4-bilight finite simple graph on `n>=3` vertices
with at least `4n-2` edges has a `K7^-` minor.

**Proof.** The assumed minimum counterexample is six-connected by
Sections 7 and 10, and has `e(G)=4v(G)-2`. Every edge has at least
four common neighbours: contracting an edge with at most three would
give a five-connected, hence 4-bilight, smaller minor retaining density
at least `-2`, contrary to minimality.

The graph has order at least nine. Since its average degree is
`8-4/v(G)<8` and its minimum degree is at least six, it has a vertex
of degree six or seven. In the first case the audited
[degree-six disk bound](../active/hc7_k7minus_degree6_common_neighbour_bound.md)
applies and gives `e(G)<=4v(G)-9`, a contradiction. In the second
case the audited
[saturated degree-seven exclusion](../active/hc7_k7minus_degree7_common_neighbour_exclusion.md)
applies and gives a `K7^-` minor, again a contradiction. Its finite
input concerns all 232 prescribed nine-vertex quotients, with exact
branch-set certificates, not bounded-order original hosts.
No minimum counterexample exists. QED

**C21 consequence.** If a `K7^-`-minor-free graph were not six-colourable,
take a minor-minimal such graph. The audited
[critical-host degree and density theorem](../results/hc7_k7minus_degree7_rooted_helper_closure.md)
makes it seven-connected with minimum degree at least eight, and hence
with at least `4v` edges. Seven-connectivity implies 4-bilightness,
so the theorem gives the forbidden minor. Therefore every
`K7^-`-minor-free graph is six-colourable, the assertion of C21.

The new global proof still requires independent audit, especially the
degree-five paired-square reduction, the unrestricted `F`-end selection,
and the exact corner counts. It proves no statement about arbitrary
`K7`-minor-free graphs beyond this near-clique assertion; HC7 itself is
not claimed.
