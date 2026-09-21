# A density bound and six-colour theorem for graphs excluding K7 minus an edge

**Status:** written proof. The [adjacent independent audit](hc7_k7minus_bilight_extremal_audit.md)
records its verdict against the exact source hash. Internal audits are not
external peer review. The degree-seven step uses an elementary nine-vertex
lemma; the original graphs have no order bound.

**Theorem.** Every finite simple 4-bilight graph on `n>=3` vertices with
at least `4n-2` edges contains `K7^-` as a minor.

**Corollary.** Every `K7^-`-minor-free graph is six-colourable.

Here `K7^-` is the complete graph on seven vertices with one edge deleted.
The corollary is Norin--Totschnig Conjecture 21. It does not assert the
six-colourability of all `K7`-minor-free graphs and therefore is not HC7.

## 1. Definitions and inputs

All graphs are finite and simple. Write `v(G)=|V(G)|`, `e(G)=|E(G)|`,
and `rho(G)=e(G)-4v(G)`. For a nonempty vertex set `A`, let `N_G(A)`
be its external neighbourhood and put

```text
rho_G(A)=e(G[A])+e_G(A,N_G(A))-4|A|.
```

Following Dvořák--Norin--Rahman, a **fragment** means a nonempty vertex
set; a `k`-fragment has exactly `k` external neighbours. Its **opposite
open side** is `V(G)-(A union N_G(A))`. A fragment is **proper** when
this opposite side is nonempty. In a `k`-connected graph, a proper
`k`-fragment is equivalently a nonempty union of components of the
graph after deleting a minimum cut, other than their entire union.

A **bifragment** is a pair of disjoint nonempty fragments with no edge
between them. It is **dense** if both fragment densities are positive.
The graph is **4-bilight** if it has no dense bifragment whose two
boundaries each have order at most four. In particular, every
five-connected graph is 4-bilight.

For a graph `H` with five prescribed roots `X`, define

```text
rho4(H,X)=e(H)-e(H[X])-4|V(H)-X|.
```

It is **4-light** if every nonempty root-free set with at most four
external neighbours has nonpositive fragment density. It is **internally
five-connected** if every nonempty root-free set has at least five
external neighbours; the analogous definition applies to `k` roots
and internal `k`-connectivity. A rooted minor model has disjoint nonempty
connected bags, each prescribed root in its own bag, with no other
prescribed root in that bag. Every further bag avoids the roots.

A separation `(A,B)` satisfies `A union B=V(G)` and has no edge between
`A-B` and `B-A`; its boundary is `A intersect B`. Its right side is
`G[B]` rooted at that boundary. Root bags from opposite sides may be
joined at their common prescribed root. Their interiors are disjoint,
so this operation preserves connectivity, disjointness and every
specified contact.

The following are the inputs used below.

1. The [proved rooted helper theorem](five_root_one_missing_contact.md),
   abbreviated **H2**, gives five root bags and two root-free helpers in
   every 4-light five-rooted graph of density at least two, with at least
   ten of the eleven helper--root and helper--helper contacts.
2. Dvořák--Norin--Rahman (DNR), [2609.17760v1](https://arxiv.org/html/2609.17760v1),
   Theorem 2.6 and Lemma 5.6: a 4-light five-rooted graph with `m` missing
   root edges and density at least `ceil((m+3)/2)` has a full clique
   rooted at the five roots. We use their Lemma 3.3 on reducible fragments
   and the small-root extraction in Observation 4.1 and Corollary 4.2.
   The density and orientation arguments in their Section 5 are adapted
   explicitly in Section 2 below.
3. The [rooted star and triangle lemmas](hc7_c21_rooted_density_low_degree_reduction.md)
   and [degree-five dart lemma](rooted_dart_nonroot_degree_five.md).
   The star lemma gives a connected central bag at one prescribed vertex
   and singleton bags at the other four: if `X0` is an independent
   subset of the five prescribed vertices in a graph `H`,
   `|V(H)|+|X0|<=9`, degrees outside `X0` are at least four and degrees
   inside `X0` are at least `5-|X0|`, the centre can be chosen outside
   `X0`. A dart consists of four roots, a universal nonroot, and a
   three-vertex path among the roots.
4. The [local quasi-five-connectivity lemma](hc7_c21_helper_degree_six.md):
   in a five-connected graph, if a proper five-fragment has at least
   three vertices, its opposite side has at least two, and a boundary
   vertex `x` has exactly one neighbour `a` in the fragment, then
   contracting `xa` leaves a four-connected graph with no four-cut
   whose two open sides both have at least two vertices.
5. The [elementary nine-vertex lemma](hc7_k7minus_degree7_quotient_hand_proof.md):
   if a seven-vertex graph has minimum degree at least four, adjoining
   one vertex full to it and another meeting at least six of its vertices
   forces `K7^-`. Its proof reduces the complement to five maximal forms
   and gives explicit models for all nine marked cases.
6. Robertson--Seymour--Thomas, *Hadwiger's conjecture for K6-free graphs*,
   [Theorem (2.4)](https://thomas.math.gatech.edu/PAP/hadwiger.pdf), also
   quoted as Theorem 13 in [Norin--Totschnig, 2507.03244v1](https://arxiv.org/html/2507.03244v1).
   For four vertices in a prescribed cyclic order, it gives disjoint
   crossing paths, a separation of order at most three with the four
   vertices on one side and at least two vertices on the other open
   side, or a drawing in a disc with the four vertices on its boundary
   in that order. The six-connected degree-six argument using this
   result is proved directly in Section 7.

## 2. The minimum counterexample and consistent orientations

Suppose the theorem is false. Choose a counterexample `G` minimizing
`(v(G),e(G))` lexicographically. Thus `G` is 4-bilight, has `v(G)>=3`
and `rho(G)>=-2`, and excludes `K7^-`. The density inequality and
simplicity imply `v(G)>=9`. All inductive reductions below strictly
decrease this finite lexicographic parameter and are used only when
4-bilightness, density at least `-2` and order at least three are retained.
Their fixed connected minor preimages lift every resulting model.

A fragment with boundary at most four is **reducible** when its density
is nonpositive, at least three vertices remain outside it, and its closed
side has either a boundary-rooted clique or, for a four-element boundary
and at least two interior vertices, a rooted dart. DNR Lemma 3.3 says
that replacing an inclusion-maximal such fragment by its clique or dart
preserves 4-bilightness and does not decrease the global density.

Call a five-fragment or five-rooted side **heavy** if its density is
at least two, and **low** if its density is at most one.

**Lemma 2.1.** The minimum graph `G` has the following properties.

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

## 3. Ordinary five-connectivity

**Lemma 3.1.** The minimum graph `G` has minimum degree at least five
and is five-connected.

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
For `k=3`, the [audited rooted triangle lemma](hc7_c21_rooted_density_low_degree_reduction.md#a-rooted-triangle-lemma)
gives it. For `k=4`, the [audited degree-five dart lemma](rooted_dart_nonroot_degree_five.md)
gives a rooted dart; here `|A|>=2` because every original degree is at
least five. An opposite component together with `S` has at least six
vertices, again by the degree bound. Therefore `A` satisfies all the
conditions of a reducible fragment, contrary to Section 2(1). QED

## 4. Minimum degree six

**Lemma 4.1.** The minimum graph `G` has minimum degree at least six.

**Proof.** Use Sections 2 and 3: `G` is five-connected, has minimum
degree at least five and order at least nine, satisfies
`e(G)=4v(G)-2`, and admits no pair of disjoint nonadjacent positive
fragments of boundary at most five if each order-five member has
density at least two. Thus whenever two such positive fragments
occur, at least one has boundary five and density exactly one.

We use the separately audited
[localized quasi-five-connectivity lemma](hc7_c21_helper_degree_six.md):
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

## 5. Low-density sides contain low-triangle edges

**Lemma 5.1.** If `A` is a proper five-fragment of the minimum graph `G`
with `rho_G(A)<=1`, some edge with an endpoint in `A` has at most three common neighbours
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

## 6. The end argument excludes every five-cut

**Lemma 6.1 (ends).** Let `J` be a five-connected graph in which every
proper five-fragment has at least four vertices. Let `F` be any family
of edges. Call a proper five-fragment an `F`-fragment when its boundary contains
both endpoints of an edge of `F`, and call it an `F`-end when it contains
no `F`-fragment as a proper subset. If `A` is an `F`-end, there is no edge `e in F`
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
with the actual neighbourhood and gives an `F`-fragment properly
contained in `A`, because it contains both endpoints of `e`. Its
opposite side contains `C`, and strict containment holds because
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

**Lemma 6.2.** The minimum graph `G` has no five-cut.

**Proof.** By Section 4, every degree is at least six. A singleton
five-fragment is therefore impossible. For a five-fragment of order
`a=2` or `a=3`, counting degrees and possible incident edges gives

```text
2a-binomial(a,2) <= rho_G(A) <= binomial(a,2)+a.
```

For `a=2` its density is exactly three, and for `a=3` it lies
between three and six. Neither fits Section 2's alternatives:
every five-fragment has density at most one or at least seven.
Thus all proper five-fragments have at least four vertices. Also, every
low five-fragment is proper: an empty opposite side would give
`rho_G(A)=18-e(G[N_G(A)])>=8`.

Let `F` be the family of edges having at most three common neighbours.
Every `e in F` has its endpoints in a five-cut bounding a fragment
of density one. Indeed, its contraction retains density at least
`-2` and decreases order, so is not 4-bilight. As in Section 4's cut
observation, a dense bifragment lifts to two positive five-fragments
whose boundaries contain both endpoints of `e`. Section 2(3)
forces at least one lifted density to equal one.

Suppose a five-cut exists. It has a low side by Section 2, and
Section 5 supplies an edge of `F`. The preceding paragraph then
supplies a low `F`-fragment. Choose one, `A`, inclusion-minimal among
low `F`-fragments. It is an `F`-end in the ordinary, unrestricted
sense. For if an `F`-fragment `B` were properly contained in `A`,
a heavy `B` would be disjoint and nonadjacent to the heavy opposite
side of `A`, contrary to Section 2(3). Thus `B` would be low,
contrary to the choice of `A`.

Section 5 supplies an edge `e in F` with an endpoint in `A`; its
other endpoint necessarily lies in `A union N_G(A)`. Its certifying
five-cut was established above. The local end lemma now gives a
contradiction. Hence there is no five-cut. QED

## 7. The six-connected degree-six calculation

**Lemma 7.1.** Let `H` be six-connected, have at least nine vertices,
exclude `K7^-`, and have at least four common neighbours on every
edge. If `H` has a vertex of degree six, then `e(H)<=4v(H)-9`.

**Proof.** Let `d_H(v)=6`. Every vertex of `T=N_H(v)` has at least
four neighbours within `T`, so the complement of `H[T]` is a matching.
Label `T={u1,w1,u2,w2,u3,w3}` so the only possible nonedges are `uiwi`.

There cannot be two vertex-disjoint paths joining two distinct pairs
`ui,wi` and `uj,wj`, with interiors outside `N[v]`. Contracting each
path to an edge fills two of the three possible missing edges in
`H[T]`. Together with `{v}`, this gives seven disjoint bags missing
at most one contact, a `K7^-` model.

All three pairs are nonedges. Otherwise take the existing pair edge
as one path. A component outside `N[v]` exists and has neighbourhood
all of `T` by six-connectivity. It supplies a path for another pair,
contradicting the preceding observation.

Some pair, say `u1,w1`, has no common neighbour outside `N[v]`.
Otherwise choose an exterior common neighbour `xi` for each pair.
Two distinct choices give the forbidden disjoint length-two paths.
Thus all three choices coincide at one vertex `x`. Since `v(H)>=9`,
there is a component `C` outside `N[v] union {x}`. Its neighbourhood
is contained in `T union {x}` and has order at least six, so at least
five vertices of `T` meet `C`. In particular `C` supplies a path
joining one pair; a length-two path for another pair through `x`
is disjoint from it, again a contradiction.

Apply the Robertson--Seymour--Thomas theorem to
`H'=H-{v,u1,w1}`, with ordered terminals `u2,u3,w2,w3`.
Crossing paths give the excluded two-pair model. If its separation
outcome `(A,B)` occurs, all four terminals belong to `A`,
`|A intersect B|<=3`, and `|B-A|>=2`. Then

```text
(A union {v,u1,w1}, B union {u1,w1})
```

is a separation of `H` of order at most five. It is proper because
`v` is on the first open side and `B-A` is on the second; no edge
from `v` reaches `B-A`. This contradicts six-connectivity.

Therefore `H'` has a disc drawing with the four distinct terminals
on its boundary. The plane edge bound gives `e(H')<=3v(H')-7`.
Every vertex outside `N[v]` meets the deleted triple `{v,u1,w1}`
at most once, by the chosen pair's property. The four other vertices
of `T` each meet that triple three times, and the triple induces two
edges. Writing `n'=v(H')=v(H)-3`, we obtain

```text
e(H) <= (3n'-7)+(n'-4)+4*3+2 = 4v(H)-9.
```

This proves the lemma. In particular, this argument uses
six-connectivity directly and requires no auxiliary five-separation
or prescribed five-linkage claim. QED

## 8. The extremal theorem and six-colour corollary

**Theorem 8.1.** Every finite simple 4-bilight graph on `n>=3` vertices
with at least `4n-2` edges contains `K7^-` as a minor.

**Proof.** The assumed minimum counterexample is six-connected by
Lemmas 3.1 and 6.2, and has `e(G)=4v(G)-2`. Every edge has at least
four common neighbours: contracting an edge with at most three would
give a five-connected, hence 4-bilight, smaller minor with density
at least `-2`, contrary to minimality.

The graph has order at least nine. Its average degree is
`8-4/v(G)<8`, while Lemma 4.1 gives minimum degree at least six.
Thus it has a vertex of degree six or seven. In the first case,
Lemma 7.1 gives `e(G)<=4v(G)-9`, a contradiction.

In the second case, let `v` have degree seven and put `J=G[N(v)]`.
The common-neighbour bound gives `delta(J)>=4`. There is a component
`C` outside `N[v]`, and six-connectivity gives `|N_G(C)|>=6`.
Contract all of `C` to one vertex and delete the other exterior
components. The resulting nine-vertex minor consists of `J`, the
vertex `v` full to `J`, and a nonadjacent exterior vertex full to
at least six vertices of `J`. The elementary nine-vertex lemma gives a
`K7^-` model. Replacing the contracted vertex by `C` lifts the model to
`G`, a contradiction.

No minimum counterexample exists. QED

No upper bound is imposed on `G`, `C`, or any preceding fragment.

**Corollary 8.2 (C21).** Every `K7^-`-minor-free graph is six-colourable.

**Proof.** Otherwise choose a minor-minimal graph `G` that excludes
`K7^-` and is not six-colourable. It has chromatic number at least
seven, and every proper minor is six-colourable. DNR
[Theorem 1.6](https://arxiv.org/html/2609.17760v1#S1)
therefore gives seven-connectivity and `e(G)>=4v(G)-2`.
Seven-connectivity implies 4-bilightness, and Theorem 8.1 gives the
forbidden `K7^-` minor. QED

In particular, Theorem 8.1 proves the five-connected density assertion
in DNR Conjecture 1.5 as well. The colouring conclusion excludes a
minor obtained by deleting one edge from `K7`; it does not prove HC7.
