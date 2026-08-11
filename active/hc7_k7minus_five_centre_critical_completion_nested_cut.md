# Every centre in the minimal five-root row is rainbow

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_five_centre_critical_completion_nested_cut_audit.md`](hc7_k7minus_five_centre_critical_completion_nested_cut_audit.md).
This note eliminates both critical-completion outcomes of the five-root
palette theorem.  For a pole-incident centre, a four-root witness and a
two-sided transfer contradiction localize the omitted centre's contacts
before the first retained-root contact; the resulting prefix component
contradicts seven-connectivity.  For a pole-free centre, the retained roots
meet both poles, so every split of the witness path is admissible, while
seven-connectivity supplies two disjoint centre-contact paths to distinct
vertices of that path.  Contracting the two resulting sides gives the same
transfer contradiction directly.  Hence all five centres are rainbow on the
distinct-response shore in one fixed colouring.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Use the hypotheses and notation of the audited
[global five-root palette alternative](hc7_k7minus_five_centre_t5_global_palette.md).
Thus

\[
 S=Z\mathbin{\dot\cup}\{p,q\},\qquad |Z|=5,
\]

`G-S` has connected full components `C,D`, the permitted response on `C`
has equal pole colours, and the permitted response on `D` has distinct pole
colours.  Both five-root instances are infeasible, while deleting any one
root makes the corresponding instance feasible.

Fix a permitted colouring `phi_D` of the closed `D`-shore and name its
boundary colours by

\[
 \phi_D(Z)=\alpha,\qquad
 \phi_D(p)=\beta,\qquad
 \phi_D(q)=\delta,
 \qquad
 \Gamma=[6]-\{\alpha,\beta,\delta\}.
\tag{1.1}
\]

Let `z in Z` be adjacent to `p` and not to `q`, and suppose that `z` is
not rainbow on `D` in `phi_D`.  In particular,

\[
             \Gamma\nsubseteq\phi_D(N_D(z)).
\tag{1.2}
\]

Put `A=Z-{z}`.  Choose a `p`--`q` path `P` witnessing feasibility of the
`D`-rooted instance with root set `A`, and let `K` be the component after
deleting `P` which contains `A`.  Full five-root infeasibility gives

\[
                         E_G(z,K)=\varnothing .
\tag{1.3}
\]

Indeed, one edge from `z` to `K` would put all five roots in one component
after deleting the same path.

The set `K` has at least two distinct neighbours on `P`.  To see this,
choose a component `R_0` of `G[K\cap D]`.  Such a component exists because
four independent roots are connected in `K`.  Its neighbourhood is
contained in `Z\cup V(P)`, and that set separates `R_0` from the nonempty
component `C`.  Seven-connectivity therefore gives at least two neighbours
of `R_0`, and hence of `K`, on `P`.

Orient `P` from `p` to `q`.  An edge of `P` is **admissible** when `K` has
a neighbour on both components of the path left by deleting that edge.

## 2. A two-sided centre contact is impossible

### Lemma 2.1 (two-sided transfer contradiction)

Let an admissible edge split `P` into connected subpaths `P_p,P_q`
containing `p,q`, respectively.  Neither of the following can occur:

1. `z` has a neighbour on `P_q`; or
2. a component `B` of the rooted graph minus `P`, different from `K`, is
   adjacent to `z` and has a neighbour on `P_q`.

#### Proof

In the second case `B` contains no root of `A`, and hence `B subseteq D`.
Contract `K`, `P_p`, and `P_q union B` to vertices `k,a,b`, respectively;
in the first case use `P_q` in place of `P_q union B`.  Delete the unused
vertices of `D` and retain `C` and `z`.  This is a proper minor `N` of `G`.
The vertices `k,a,b` form a triangle.  Moreover `z` is adjacent to `a`
through the literal edge `zp` and to `b` through the assumed contact.

Suppose `N` had a proper six-colouring.  Rename the colours of `k,a,b` as
`alpha,beta,delta`.  The colour of `z` is neither `beta` nor `delta`.
Expand the literal vertices of `A` from `k` and the poles from `a,b`, and
compare the resulting colouring of `C union S` with `phi_D`.

If `z` has colour `alpha`, the two colourings glue: every member of
`N_D(z)` avoids `alpha` in `phi_D`.  Otherwise `z` has a colour in
`Gamma`.  By (1.2), some colour of `Gamma` is absent from
`phi_D(N_D(z))`; permute the three names in `Gamma` on the minor side so
that `z` receives that absent colour.  The colourings again glue across
`A union {p,q}`, and all edges from `z` to `D` are proper.  This would
six-colour `G`, a contradiction.

Thus `N` is not six-colourable, contrary to proper-minor criticality of
`G`. \(\square\)

This lemma is stronger than saying that one selected transfer minor has an
artificial critical edge.  It applies to every feasible witness, every
admissible split, and every off-path component which could be absorbed into
the opposite pole bag.

## 3. Prefix minimization

Among all feasible witnesses `(P,K)`, choose one minimizing the distance
along `P` from `p` to the first vertex `w` of `P` having a neighbour in
`K`.  There is another `K`-contact strictly after `w`, so the edge of `P`
immediately after `w` is admissible.  Lemma 2.1 gives

\[
 \begin{split}
 N_P(z)&\subseteq V(P[p,w]),\\
 N_P(B)&\subseteq V(P[p,w])
 \quad\text{for every component `B!=K` adjacent to `z`.}
 \end{split}
\tag{3.1}
\]

### Lemma 3.1 (the first core contact is internal)

One has `w!=p`.

#### Proof

Suppose `w=p`.  By Lemma 2.1 applied immediately after `p`, no neighbour
of `z` in `D` lies on `P`.  Hence every such neighbour lies in a component
`B!=K` after deleting `P`; recall that `z` is anticomplete to `K` by
(1.3).  Equation (3.1) says that every neighbour of `B` on `P` is `p`.
Therefore

\[
                         N_G(B)\subseteq Z\cup\{p\}.
\]

The right side has order six and separates `B` from `C`, contrary to
seven-connectivity.  Thus no such component exists.  But the one-edge row
has `|N_D(z)|>=2`, a contradiction. \(\square\)

### Lemma 3.2 (no bridge crosses the first core contact)

No component of the rooted graph minus `P`, different from `K`, has both a
neighbour strictly before `w` and a neighbour strictly after `w` on `P`.
There is also no chord of `P` with one end strictly before `w` and the
other strictly after `w`.

#### Proof

Suppose first that a component `B` has such attachments `x,y`, ordered

\[
                         p\ldots x\ldots w\ldots y\ldots q.
\]

Replace the `x`--`y` segment of `P` by an `x`--`y` path whose interior
lies in `B`.  The old open segment contains `w`; after the replacement it
joins `K` and therefore belongs to the component containing `A`.  That
component meets the new path at `x` (and possibly earlier), so its first
contact occurs strictly before `w`.  The new path still witnesses
four-root feasibility.  This contradicts the choice of `(P,K)`.

A chord with ends `x,y` gives the same replacement using the one-edge
`x`--`y` path. \(\square\)

## 4. The nested two-cut

### Theorem 4.1 (strict nesting inside the distinct-response shore)

There is a nonempty component `L` of

\[
                              F-\{p,w\},
                 \qquad F=G-Z,
\]

such that

\[
                         L\subsetneq D,
       \qquad N_F(L)=\{p,w\},
       \qquad N_G(L)=Z\mathbin{\dot\cup}\{p,w\}.
\tag{4.1}
\]

In particular, `{p,w}` is another actual two-cut of `F`, and `L` is a
strictly smaller component nested inside the old distinct-response side.

#### Proof

If the open `p`--`w` segment of `P` contains a vertex, take the component
of `F-{p,w}` containing that segment.  It cannot reach the suffix of `P`
without using `w`: on a shortest such route, the subpath between the last
prefix vertex of `P` and the first suffix vertex of `P` is either a chord
or has its interior in one component of the rooted graph minus `P`,
contrary to Lemma 3.2.  It cannot reach `K`: distinct components of the
rooted graph minus `P` do not meet, while no vertex of `P` strictly before
`w` has a neighbour in `K` by the definition of `w`.  There are no `C-D`
edges.  Hence it has no neighbour in `F` outside `{p,w}`.

It remains to check nonemptiness when `pw` is an edge of `P`.  At most one
neighbour of `z` in `D` then lies on `P[p,w]`, namely `w`.  Since
`|N_D(z)|>=2`, another neighbour lies in a component `B!=K` after deleting
`P`.  By (3.1), every attachment of `B` to `P` belongs to `{p,w}`.  A
component of `F-{p,w}` containing `B` therefore supplies the required
nonempty `L`.

The component `R_0 subseteq K cap D` used in Section 1 has two distinct
contacts on `P`.  Neither precedes the first `K`-contact `w`, so one lies
strictly after `w`.  Consequently `R_0` joins the suffix after deleting
`p,w` and lies outside `L`.  Hence `L` is a proper subset of `D`.
There are no `C-D` edges.  Lemma 3.2 forbids an off-path route from the
prefix side to the suffix side, while the definition of `w` forbids a
prefix edge into `K`.  Consequently `N_F(L) subseteq {p,w}`.

The nonempty graph `C` lies outside `L union Z union {p,w}`.  Thus
`N_G(L)` is a genuine separator and

\[
                         N_G(L)\subseteq Z\cup\{p,w\}.
\]

Seven-connectivity forces equality.  Removing `Z` gives the first equality
in (4.1), and the theorem follows. \(\square\)

### Lemma 4.2 (the retained roots miss the nested component)

The set `A=Z-{z}` is anticomplete to `L`.

#### Proof

First suppose that `P(p,w)` is nonempty, so `L` is the component of
`F-{p,w}` containing this open path segment.  Suppose that `a in A` has a
neighbour `x in L`.  If `x` lies on `P`, then the proof of Theorem 4.1 puts
it strictly before `w`; since `a in K`, this is a `K`-contact preceding
`w`, a contradiction.

Thus `x` is off `P`.  The edge `ax` puts `x` in the component `K` of the
rooted graph minus `P`.  Take an `x`--`P(p,w)` path in `L`, and let `y` be
its first vertex on `P` when traversed from `x`.  Its open interior avoids
`P` and joins `x`, so it also lies in `K`.  Hence `y` is again a
`K`-contact strictly before `w`, a contradiction.

It remains that `pw` is an edge of `P`.  In this case `L` contains the
component `B!=K` selected in the proof of Theorem 4.1.  In fact `L=B`:
the only neighbours of `B` in the rooted graph outside `B` lie on `P`, all
of its path attachments belong to `{p,w}`, the old component `C` is
anticomplete to `D`, and every vertex of `Z` is absent from `F`.  Distinct
components `B,K` of the rooted graph minus `P` are anticomplete.  Since
`A subseteq K`, no member of `A` is adjacent to `L=B`.  \(\square\)

### Corollary 4.3 (terminal elimination of the one-edge row)

The setting of Section 1 cannot occur.

#### Proof

Theorem 4.1 gives

\[
                         N_G(L)=Z\mathbin{\dot\cup}\{p,w\}.
\]

In particular, every member of the nonempty four-set `A` has a neighbour
in `L`.  This contradicts Lemma 4.2. \(\square\)

## 5. Why generic critical-edge lifting was not enough

The terminal proof above does not use a minor model in the exactly
seven-chromatic critical completion.  The following diagnostic records why
trying to lift such a model directly would have required an additional
label-preserving hypothesis.

Let `M` be one of the transfer minors and let `e=zb` be its missing
centre--opposite-pole incidence.  If the exactly seven-chromatic graph
`M+e` is smaller than a globally smallest counterexample, it contains a
`K_7^-` minor.  This does not make `e` automatically replaceable.

### Lemma 5.1 (clean replacement is sufficient)

Fix a `K_7^-` model in `M+e`.  If there is a `z`--`b` path in the original
host whose internal vertices avoid the lifted union of all seven branch
sets, then the model lifts to a `K_7^-` model in `G`.

#### Proof

If `e` joins two model bags, adjoin the internal vertices of the clean path
to one bag up to the last edge into the other.  If `e` lies inside one
model bag, replace its use in a connected spanning subgraph of that bag by
the clean path.  Disjointness and every old model adjacency are preserved
in either case. \(\square\)

When `e` joins two different bags and is essential, deleting it leaves an
exact seven-bag model with two missing pairs: the `e`-pair and the genuine
missing pair of the old `K_7^-` model.  If the old missing pair were already
adjacent, or if `e` represented that pair, the same bags would already be
a `K_7^-` model in `M`.  When `e` lies inside one bag, deleting it leaves
the corresponding split-bag obstruction.

The smallest quotient showing why the three colour-distinguished paths do
not settle this is

\[
                         K_7-\{zv,rs\}.
\tag{5.1}
\]

Adding `zv` gives a literal `K_7^-`.  Before adding it, any three of the
other vertices give three internally disjoint two-edge `z`--`v` paths,
but the seven-vertex graph has no `K_7^-` minor: a seven-bag model would
have seven singleton bags, while (5.1) has two missing edges.  The same
warning holds when the two missing pairs share an endpoint.

Thus a clean replacement path would be sufficient, but several
colour-distinguished paths are not sufficient merely by their number.  The
prefix argument in Sections 2--4 avoids this label-preserving lifting issue
and gives the stronger terminal contradiction in Corollary 4.3.

## 6. Consequence for the five-root palette alternative

In the minimally infeasible five-root, no-singleton-contact setting, every
pole-incident centre is rainbow on the distinct-response shore in the fixed
permitted colouring.  Equivalently, conclusions 2 of the global palette
alternative never occur.  For each centre, the surviving alternatives are
therefore: it is rainbow, or it is pole-free and has the two-incidence
critical completion.  This is a terminal elimination of the one-edge branch,
not a proof of the full five-centre two-cut theorem.

## 7. The pole-free nonrainbow row is also impossible

Retain the setting of the global palette theorem and suppose now that a
pole-free centre `z` is not rainbow on `D`.  Thus

\[
 zp,zq\notin E(G),\qquad |N_D(z)|\in\{2,3\},
 \qquad \Gamma\nsubseteq\phi_D(N_D(z)).             \tag{7.1}
\]

Put `A=Z-{z}` and choose a feasible `D`-side four-root witness `(P,K)` as
in Section 1.  Write

\[
                         H=G[D\cup A\cup\{p,q\}].    \tag{7.2}
\]

Thus `P` is a `p`--`q` path in `H`, `K` is the component of `H-P`
containing `A`, and full five-root infeasibility again gives

\[
                              E_G(z,K)=\varnothing.   \tag{7.3}
\]

Because both pole labels occur in the exact centre--pole matching and `z`
is pole-free, there are roots `a_p,a_q in A` adjacent to `p,q`,
respectively.  Both roots lie in `K`.  Hence `K` meets `P` at both end
vertices: every edge of `P` is admissible.

Put

\[
                              T=N_D(z).              \tag{7.4}
\]

By (7.1) and the clique conclusion of the global palette theorem, `T` is
a clique of order two or three.  Equation (7.3) gives `T cap K=emptyset`.

### Lemma 7.1 (two disjoint contacts with the witness path)

There are vertex-disjoint `T`--`P` paths `Q_1,Q_2` with distinct initial
vertices `t_1,t_2 in T` and distinct terminal vertices `r_1,r_2 in P`.
They may be chosen so that

\[
                         V(Q_i)\cap V(P)=\{r_i\}
                         \qquad(i=1,2).              \tag{7.5}
\]

#### Proof

If at least two members of `T` lie on `P`, take two trivial paths.  Suppose
exactly one member `r_1` of `T` lies on `P`.  Since `T` is a clique, all
members of `T-\{r_1\}` lie in one component `B` of `H-P`, and `r_1` is
an attachment of `B`.  If it were the only attachment, then distinct
components of `H-P` are anticomplete, `A subseteq K`, and there are no
`C`--`D` edges, so

\[
                              N_G(B)\subseteq\{z,r_1\}.
\]

This would separate the nonempty set `B` from `C`, contrary to
seven-connectivity.  Thus `B` has another attachment `r_2 in P`.  A path
through `B` from a member of `T-\{r_1\}` to `r_2`, together with the
trivial path at `r_1`, has the required form after truncation at its first
vertex of `P`.

It remains that `T cap P=emptyset`.  Since `T` is a clique, it lies in one
component `B` of `H-P`.  Apply the set form of Menger's theorem in
`G[B union P]`.  If two vertex-disjoint `T`--`P` paths with distinct ends
did not exist, a set `X` of order at most one would meet every such path.
The set `T-X` is nonempty and connected.  Let `W` be its component in
`B-X`.  The defining property of `X` gives no edge from `W` to `P-X`.
As above, every neighbour of `B` outside `B union P` belongs to `{z}`.
Consequently

\[
                              N_G(W)\subseteq\{z\}\cup X.
\]

This set has order at most two and separates `W` from `C`, again contrary
to seven-connectivity.  The two paths therefore exist, and truncating each
at its first vertex of `P` gives (7.5). \(\square\)

### Theorem 7.2 (terminal elimination of the pole-free row)

The pole-free nonrainbow setting (7.1) cannot occur.

#### Proof

Orient `P` so that `r_1` precedes `r_2`, and split `P` at an edge between
them into connected subpaths `P_p,P_q` containing `p,q`, respectively.
Every edge of `P` is admissible, so `K` has a neighbour in both path
halves.  By Lemma 7.1 the three connected sets

\[
                 K,\qquad P_p\cup Q_1,\qquad P_q\cup Q_2
\]

are pairwise disjoint.  Contract them to `k,a,b`, delete the unused
vertices of `D`, and retain `C` and `z`.  The result is a proper minor `N`
of `G`: the vertices `k,a,b` form a triangle, and `z` is adjacent to both
`a,b` through the two distinct starts `t_1,t_2 in T`.

Six-colour `N` and rename the colours on `k,a,b` as
`alpha,beta,delta`.  The colour on `z` avoids `beta,delta`.  Expand the
literal vertices of `A,p,q`, use the minor colouring on the closed
`C`-side and on `z`, and use `phi_D` on `D`.

If `z` has colour `alpha`, every edge from `z` to `D` is proper because
those neighbours avoid `alpha` in `phi_D`.  Otherwise `z` has a colour in
`Gamma`.  Since `z` is nonrainbow, permute the three names in `Gamma` on
the minor side so that `z` receives a colour absent from
`phi_D(N_D(z))`.  The two partial colourings then glue to a proper
six-colouring of `G`, a contradiction. \(\square\)

## 8. Global consequence

Corollary 4.3 eliminates every pole-incident nonrainbow centre, and
Theorem 7.2 eliminates every pole-free nonrainbow centre.  Therefore the
critical-completion outcome of the global five-root palette alternative is
empty:

\[
             \boxed{\ N_D(z)\text{ is a rainbow triangle for every }
                     z\in Z.\ }                     \tag{8.1}
\]

All five triangles and all thirty pole--triangle Kempe connections occur in
the one fixed permitted colouring `phi_D`.  This closes the entire
critical-completion branch.  The remaining five-root task is precisely the
all-rainbow branch.
