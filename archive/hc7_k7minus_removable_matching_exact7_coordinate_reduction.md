# A matching coordinate gives a fan, and at order seven a labelled descent

**Status:** archived superseded written reduction; not separately audited.
Its six-coordinate fork is superseded by the stronger audited
[componentwise-induced forest theorem](../results/hc7_k7minus_six_coordinate_forest_reduction.md),
which also retains two seven-connected one-edge restorations.  This note does
not prove the `K_7^-` six-colour conjecture or `HC_7`.

This note isolates what the punctured matching-signature family contributes
when the exact `K_7^vee` model returns an actual separator.  At every
boundary order, a crossing coordinate gives a six-ended fan with the five
critical first edges prescribed.  At order seven, the stronger audited
fan/descent theorem also gives a well-founded labelled reduction.
If one selected matching edge crosses from the returned connected side to
its boundary, its singleton-signature colouring is already the critical
boundary-edge colouring required by the audited exact-seven fan/descent
theorem.  No recolouring, change of operation, or identification of colour
names is needed.

## 1. Setting

Let `G` be a seven-connected graph satisfying

\[
 \chi(G)=7,
 \qquad \chi(J)\leq6\quad\hbox{for every proper minor }J\hbox{ of }G.
                                                               \tag{1.1}
\]

Let `M` be a matching and put `H=G-M`.  Assume that, for every nonempty
`J subseteq M`, there is a proper six-colouring `c_J` of `H` with

\[
       \Sigma_M(c_J)=J.                                  \tag{1.2}
\]

Thus, after the edges of `M` are restored, `c_{\{e\}}` has exactly one
monochromatic edge, namely `e`.

Let `Y` be a nonempty connected set such that

\[
 T=N_G(Y),\qquad |T|\geq7,
 \qquad G-(Y\cup T)\ne\varnothing.                       \tag{1.3}
\]

The set `Y` is a component of `G-T`.  These are the properties of a
connected side returned by the spanning exact-`K_7^vee` dichotomy;
seven-connectivity supplies the boundary lower bound.

## 2. Crossing-coordinate reduction

### Theorem 2.1 (one matching coordinate)

Suppose that some edge `e=uv in M` satisfies

\[
                         u\in Y,\qquad v\in T.           \tag{2.1}
\]

Put `c=c_{\{e\}}` and `alpha=c(u)=c(v)`.  Then all of the following hold.

1. For each colour `beta ne alpha`, the graph `G-e` contains an
   `alpha`--`beta` path from `u` to `v`.  Stop such a path at its first
   vertex `t_beta` of `T` and put

   \[
       T_0=\{v\}\cup\{t_\beta:\beta\ne\alpha\}.        \tag{2.2}
   \]

   Then `|T_0|<=6`.

2. There are six paths from `u` to six distinct vertices of `T`, pairwise
   disjoint outside `u`.  One is the edge `uv`; the other five begin with
   the five colour-indexed first edges of the paths in item 1.

3. Suppose in addition that `|T|=7`.  If `|T_0|<=5`, choose any five-set
   `Q subseteq T` containing `T_0`.
   Then at least one of the following holds.

   a. There are five `u`--`Q` paths which preserve the five
      colour-indexed first edges and are pairwise vertex-disjoint outside
      `\{u\}\cup Q`.  Their ends in `Q` may coincide.

   b. There are a four-set `Z subseteq Y-\{u\}` and a nonempty connected
      proper set `A subsetneq Y` such that

      \[
       N_G(A)=(T-Q)\mathbin{\dot\cup}\{u\}
                    \mathbin{\dot\cup}Z,\qquad |N_G(A)|=7.       \tag{2.3}
      \]

      The restriction of the *same* colouring `c` to
      `G[A\cup N_G(A)]` is proper in `G`.  Its exact `alpha`-coloured
      boundary class contains `u` and at least one member of `Z`.
      Moreover, a proper six-colouring of the opposite closed shore has
      that same set as one exact boundary colour class.

In outcome 3b the component has strictly decreased, while the literal
matching endpoint `u`, the singleton operation `G-e`, its colouring, and
one exact boundary block are all retained.

#### Proof

The colouring `c` is a proper six-colouring of `G-e`: every edge of
`M-\{e\}` is bichromatic by (1.2), and `e` is the only edge absent from
`G-e` on which its ends have equal colours.  If, for some
`beta ne alpha`, the ends of `e` lay in different `alpha`--`beta`
components of `G-e`, a Kempe interchange on the component containing `u`
would give the ends different colours.  Restoring `e` would then
six-colour `G`, contrary to (1.1).  This proves item 1; its cardinality
bound is immediate from the five colours distinct from `alpha`.

We prove item 2 directly, since the argument works for every
`|T|>=7`.  For each `beta ne alpha`, let `s_beta` be the neighbour of `u`
on the path chosen in item 1.  Its colour is `beta`, so the five vertices
`s_beta` are distinct.  Put

\[
 I=\{\beta:s_\beta=t_\beta\in T\},\qquad r=|I|,
\]

and retain the `r` direct edges `us_beta`, `beta in I`.  In

\[
 K=G[(Y-\{u\})\cup
       (T-(\{v\}\cup\{s_\beta:\beta\in I\}))]
\]

seek `5-r` disjoint paths from the remaining `s_beta` to distinct vertices
of the displayed part of `T`.  If they did not exist, the set form of
Menger's theorem would give a separator `Z` of order at most `4-r`.
Some source and some target survive, because there are `5-r` sources and
at least `|T|-1-r>=6-r` targets.  The component `A` containing a surviving
source has no surviving target and lies in `Y-(\{u\}\cup Z)`.  Since
`T=N_G(Y)`,

\[
 N_G(A)\subseteq Z\cup\{u,v\}
                 \cup\{s_\beta:\beta\in I\}.
\]

The right side has order at most `(4-r)+2+r=6`, and a surviving target
lies beyond it.  This contradicts seven-connectivity.  The required
linkage therefore exists.  Prepending the five prescribed first edges,
and adding the edge `uv`, gives item 2.

When `|T|=7` and `|T_0|<=5`, apply Theorem 3.1 and Corollary 3.2 of the
audited
[critical-edge fan/descent theorem](../results/hc7_exact7_critical_edge_fan_descent.md)
with the chosen five-set `Q`.  Its packing outcome is item 3a.  In its
descent outcome, equation (3.2) there is exactly (2.3), and the new
component is a proper subset of `Y`.  The only defect of `c` in `G` is
`uv`, while the vertex `v` belongs to `Q` and hence lies outside
`A\cup N_G(A)`.  The restriction is therefore proper.  The cited proof
also gives the repeated `alpha`-block containing `u` and a member of `Z`,
and its corollary realizes that exact block from the opposite shore.  This
proves item 3. `\square`

### Corollary 2.2 (the exact residue at a supported side)

Suppose `Y` meets `V(M)`.  Then one of the following holds.

1. A matching edge crosses from `Y` to `T`, and Theorem 2.1 supplies the
   prescribed six-ended fan at every boundary order.
2. Every matching edge incident with `Y` has both ends in `Y`.

Consequently a response-bearing side can avoid the coordinate-preserving
fan only by containing every matching pair which it meets.  At exact order
seven, the remaining non-descent configurations in the crossing case are
the five-path packing in Theorem 2.1(3a) and the six-hit case
`|T_0|=6`.

#### Proof

An edge incident with `Y` cannot have its other end beyond `T`, because
`T=N_G(Y)`.  Hence its other end lies in `Y` or `T`.  The first alternative
holds if one lies in `T`; otherwise every such edge is internal to `Y`.
The final assertion is exactly the list of alternatives in Theorem 2.1.
`\square`

### Corollary 2.3 (every returned side has a critical-edge fan)

The matching hypothesis is unnecessary if fixed common-host provenance is
not required.  For every `Y,T` satisfying (1.3), there is an edge
`uv` with `u in Y`, `v in T` such that a proper six-colouring of `G-uv`
and the edge `uv` satisfy the path, packing and descent conclusions of
Theorem 2.1, with `uv` as the selected critical edge rather than as a
matching coordinate.  In particular, every model-bag separator, of
arbitrary order, carries a prescribed six-ended critical-edge fan; at
order seven it also has the packing/descent alternative in item 3.

#### Proof

Choose any edge from the connected side `Y` to its nonempty open
neighbourhood `T`.  The proper minor `G-uv` has a six-colouring.  Its two
ends have one common colour, since otherwise restoring `uv` would
six-colour `G`.  The proof of Theorem 2.1 uses only these facts, not the
other edges of `M`, so it applies verbatim. `\square`

## 3. A maximum deficient bag eliminates the avoidable-core case

Now assume that `G` has no `K_7^-` minor and has a spanning exact
`K_7^vee` model

\[
                     P,B,C,U_1,U_2,U_3,U_4,             \tag{3.1}
\]

where `P` is anticomplete to `B,C` and the other six bags form a clique
model.  Among all such labelled spanning models, choose one for which
`|P|` is maximum.

Fix a universal bag `U=U_i` and two distinct vertices

\[
                         p,q\in N_G(P)\cap U.            \tag{3.2}
\]

For each of the five foreign clique bags

\[
                  B,C,U_j\quad(j\ne i),                 \tag{3.3}
\]

its **portal set in `U`** is its nonempty neighbourhood in `U`.  A
`p`-retaining core is a connected subset of `U` containing `p` and meeting
all five portal sets.

### Theorem 3.1 (maximum-`P` opposite-gate normal form)

Under the preceding hypotheses:

1. every `p`-retaining core contains `q`, and every `q`-retaining core
   contains `p`;
2. if `C_q` is the component of `G[U-q]` containing `p` and

   \[
                         Z_q=U-C_q,                      \tag{3.4}
   \]

   and `Z_p` is defined symmetrically, then `Z_p,Z_q` are nonempty,
   connected and disjoint, their complements in `U` are connected, and
   each monopolises the whole portal set of at least one foreign bag;
3. at least one of `Z_p,Z_q` is anticomplete to `B` or to `C`.  That gate
   is a connected side of an actual separator of order at least seven,
   contains one of the prescribed literal `P`-portals, and has a nonempty
   set of monopolised model labels.

Thus maximising `|P|` removes the avoidable-core outcome entirely.  Every
pair of `P`-portals in one universal bag returns a canonical
model-labelled separator unless the target minor already exists.

#### Proof

Suppose that a `p`-retaining core `R` avoids `q`, and let `Y` be the
component of `G[U-R]` containing `q`.  The set `U-Y` is connected and,
because it contains `R`, retains an edge to every foreign bag in (3.3).

If `Y` meets `B` or `C`, say `B`, move `Y` from `U` into `B`.  The enlarged
bag `B\cup Y` is connected and meets `P` through the prescribed edge from
`q` to `P`.  The residual bag `U-Y` remains connected, meets `P` through
`p`, and retains all five foreign contacts.  The seven resulting bags
have only `PC` possibly absent, and hence form a `K_7^-` model.  This is
excluded.

Hence `Y` is anticomplete to both `B,C`.  Move it instead into `P`.  The
bag `P\cup Y` is connected through the edge from `q` to `P`, remains
anticomplete to `B,C`, and meets `U-Y` across the cut inside the connected
bag `U`.  All its other universal-bag contacts are inherited from `P`,
while `U-Y` retains the five contacts certified by `R`.  This is another
spanning exact `K_7^vee` model, now with deficient bag `P\cup Y`, contrary
to the maximum choice of `|P|`.  Therefore every `p`-retaining core
contains `q`.  Interchanging `p,q` proves item 1.

The standard opposite-gate argument now applies.  The set `Z_q` in (3.4)
and its complement are nonempty and connected.  If its complement met
every portal set, a connected subgraph of that complement containing `p`
and one vertex of every portal set would be a `p`-retaining core avoiding
`q`.  Thus `Z_q` contains a whole portal set.  The same holds for `Z_p`.
The two gates are disjoint: a vertex in both would make every path from it
to `p` use `q` and every path from it to `q` use `p`, while the suffix of a
simple path contradicts the second assertion.  A nonempty portal set
cannot be contained in both disjoint gates, so their monopoly-label sets
are disjoint.  This proves item 2.

Suppose finally that both gates meet both `B,C`.  Since they are disjoint,
neither can monopolise the `B`-portal set or the `C`-portal set: the other
gate contains a portal of each twin.  Their two nonempty disjoint monopoly
sets therefore lie among only the three labels `U_j`, `j ne i`.  One gate,
say `Z`, monopolises exactly one of those labels.  Put `W=U-Z` and
`P'=P\cup Z`.  The bag `P'` is connected, meets `B,C` through `Z`, and
meets every other universal bag through the old `P`; hence the six bags
other than `W` form a clique model.  The residual `W` is connected, meets
`P'` across the cut, and retains every foreign adjacency except possibly
the unique monopolised label.  These seven bags form a `K_7^-` model, a
contradiction.

At least one gate consequently misses `B` or `C`.  The missed connected bag
is a nonempty far side of its open neighbourhood, so that neighbourhood is
an actual separator.  Seven-connectivity gives its order, and items 2--3
give the claimed root and model label. `\square`

### Theorem 3.2 (a deletion-persistent model edge on the gate)

Retain Theorem 3.1 and let `Z` be one of its separator gates.  Write
`r` for its selected `P`-portal and `s` for the other selected portal, so

\[
             r\in Z,\qquad s\in U-Z.                   \tag{3.5}
\]

Choose edges `xr,ys` with `x,y in P`, and put `e=xr`.  Then:

1. deleting `e` leaves the same spanning exact `K_7^vee` model (3.1),
   because the distinct edge `ys` retains the `P-U` adjacency;
2. contracting `e` and merging the old bags `P,U` gives a spanning
   `K_6`-minor model in `G/e`;
3. `chi(G-e)=chi(G/e)=6`, and every six-colouring of `G-e` gives `x,r`
   one common colour;
4. in one such colouring, five colour-indexed bichromatic `r`--`x` paths
   coexist with the fixed exact model in `G-e`;
5. inside the separator side `Z`, those five prescribed first edges and
   `rx` extend to six paths from `r` to six distinct vertices of
   `N_G(Z)`, pairwise disjoint outside `r`.

If `|N_G(Z)|=7`, Theorem 2.1(3) additionally gives the five-path packing or
the strict labelled descent whenever its first-hit set has order at most
five.  Thus the model separator, the deleted edge, the singleton equality
response, the exact near-clique model and the critical fan can all be
chosen in one literal graph.

#### Proof

The edges `xr,ys` are distinct because `r ne s`.  They join the same two
old branch sets.  Deleting the first therefore preserves every branch-set
adjacency, proving item 1.

After contracting `xr`, combine the images of `P` and `U` into one
connected branch set.  It is adjacent to `B,C` through the old universal
bag `U` and to each of the other three universal bags.  The five remaining
bags `B,C,U_j`, `j ne i`, are pairwise adjacent.  These six bags partition
the contracted graph and form the model in item 2.

Both edge deletion and edge contraction are proper minors and hence are
at most six-chromatic.  If either were five-colourable, expand the
contraction or use the deletion colouring and assign one end of `e` a
fresh sixth colour; this would six-colour `G`.  Hence both chromatic
numbers equal six.  In a six-colouring of `G-e`, the two ends have one
common colour, since otherwise `e` could be restored.  A Kempe interchange
shows that they lie in one bichromatic component for each of the other
five colours, exactly as in Theorem 2.1(1).  This proves items 3--4.

Finally `r in Z`, `x in P subseteq N_G(Z)`, and `rx` crosses the actual
separator side returned by Theorem 3.1.  Apply the arbitrary-order fan
proof in Theorem 2.1(2), with component `Z` and edge `rx`.  It preserves
the five first edges just obtained and proves item 5.  The exact-seven
addendum is Theorem 2.1(3). `\square`

### Corollary 3.3 (a completed matching cube and a six-coordinate fork)

Assume in addition that `M` is the five-edge matching from the
seven-removable common-host theorem and put `H=G-M`.  The pair `p,q` in
Theorem 3.1, and hence the edge `e` in Theorem 3.2, can be chosen so that,
in the notation (3.5),

\[
                         xr,ys\in E(H),\qquad e=xr.      \tag{3.6}
\]

Put

\[
                         F=M\cup\{e\},\qquad K=G-F=H-e. \tag{3.7}
\]

Unconditionally, `K` has a colouring with equality set exactly `\{e\}` on
`F`, and for every nonempty `J subseteq M` it has a colouring with equality
set exactly `J`.  Consequently

\[
       \{\Sigma_M(c):c\text{ is a proper six-colouring of }K\}=2^M.
                                                               \tag{3.8}
\]

The edge set `F` is a forest of size six.  Exactly one of the following
holds.

1. Every component of the forest `F` is induced on its own vertex set in
   `G`.  Then the exact signature language on all six coordinates is

   \[
    \{\Sigma_F(c):c\text{ is a proper six-colouring of }K\}
                         =2^F-\{\varnothing\}.          \tag{3.9}
   \]

2. The unique component of `F` containing `e` has a chord in `G`.  It is
   a path on at most four vertices, so the chord is a literal triangle or
   a chord joining the ends of that four-vertex path.

Thus the model-labelled gate edge either becomes a genuine sixth Boolean
coordinate, or it has an explicit interaction of radius at most two with
one or two of the original matching edges.  In both cases its deletion
retains the exact near-clique model and the critical fan from Theorem 3.2.

#### Proof

The connected set `B` lies outside `P\cup N_H(P)`, because `P,B` are
anticomplete already in `G`.  Hence `N_H(P)` is a vertex separator in the
seven-connected graph `H`, and

\[
                         |N_H(P)|\ge7.                  \tag{3.10}
\]

All its vertices lie in the four universal bags of the fixed partition.
Some `U_i` therefore contains distinct `p,q in N_H(P)`.  Use this pair in
Theorem 3.1.  Whichever opposite gate is returned, its selected portal
edge and the other portal edge both belong to `H`, proving (3.6) and
allowing the choice of `e` in Theorem 3.2.

Every nonempty `J subseteq M` has a signature-`J` colouring of `H`.  It
remains a colouring of `K`, and its equality set on `F` is exactly `J`
because `e` is a literal edge of `H`.  A six-colouring of `G-e`, restricted
to `K`, has equality set exactly `\{e\}` because every edge of `M` remains
present and proper in `G-e`.  This proves (3.8).

The set `F` is a forest: adding one distinct edge to a matching can only
join at most two matching components.  If each component is induced on its
own vertex set, Lemma 4.1 applies and gives (3.9).  Otherwise only the
component containing `e` can have more than two vertices.  It is a path on
three or four vertices, and any extra edge within its vertex set has the
form stated in outcome 2. `\square`

## 4. What is special about a matching-labelled trace

Every nonempty proper vertex set already carries some rejected exterior
trace.  Indeed, choose a crossing edge as in Corollary 2.3 and restrict a
six-colouring of its deletion to the exterior.  If its boundary partition
extended through the set, the two colourings could be palette-permuted to
agree and then glued to six-colour `G`.

Thus meeting `V(M)` is not needed merely to obtain a trace.  Its value is
that the trace comes from one fixed colouring of the common graph `G-M`
and retains a literal matching-coordinate label.  The following elementary
observation shows why even that label has no automatic branch-set location.

### Lemma 4.1 (automaticity of chordless-forest signatures)

Let `G` be minor-minimal subject to `chi(G)>k`, and let `M` be any
forest in `G` such that every component of `M` is induced on its own
vertex set.  For a colouring `c` of `G-M`, define `Sigma_M(c)` as the set
of forest edges whose ends have equal colours.  Then

\[
 \{\Sigma_M(c):c\text{ is a proper }k\text{-colouring of }G-M\}
                         =2^M-\{\varnothing\}.          \tag{4.1}
\]

#### Proof

For nonempty `J subseteq M`, take a `k`-colouring of the proper minor
`G/J` and expand the contracted forest edges into `G-M`.  The edges of
`J` have equal-coloured ends.  No edge of `G-M` becomes a loop: its ends
cannot lie in one component of `J`, since they would then lie in one
component of `M` and the componentwise-induced hypothesis would put that
edge in `M`.  Every edge of `M-J` remains literal as well, because its ends
cannot be joined by a path in `J` without creating a cycle in `M`.  The
minor colouring therefore expands to a proper colouring of `G-M`, and its
signature is exactly `J`.  An empty signature would remain proper after
all edges of `M` were restored and would `k`-colour `G`.
`\square`

Thus the punctured cube does not, by itself, relate the matching to the
branch sets of an exact near-clique model.  The removable-matching theorem
adds the decisive fact that `G-M` is seven-connected; it does not add a
portal-incidence condition.  In particular, maximising the number of
matching endpoints among the deficient bag's portal vertices cannot be
completed by a counting argument from (4.1).

## 5. Recorded route nonclosure and smallest repair

The maximum-`P` normalization and its new gate edge remove the need to
force one of the original matching edges across the separator.  What
remains is now the following exact response/model composition problem.

1. At boundary order greater than seven, the gate edge gives the prescribed
   six-ended fan but there is no current labelled discharge.
2. At order seven, the fan may give the five-path packing in
   Theorem 2.1(3a), or its five bichromatic paths may first hit five
   distinct boundary vertices so that `|T_0|=6`.
3. The common response on `H-e` is either the punctured six-cube or the
   explicit short-chord alternative of Corollary 3.3.  Neither has yet
   been composed with the gate's monopoly labels.

Neither (4.1) nor endpoint incidence identifies the five palette labels
of these paths with the five foreign branch-set labels.  Existing
palette/branch-set barriers in the repository show that this
identification cannot be assumed.

The smallest useful repair is therefore a **cube-completed model-labelled
fan discharge**.  It starts with the canonical gate and edge in
Theorems 3.1--3.2.  On `H-e`, that edge supplies the missing empty matching
signature, so the five original coordinates form the full cube.  In the
componentwise-induced case the gate edge extends this to the punctured
six-cube; otherwise Corollary 3.3 returns the explicit short chord as an
additional local interaction.  The theorem must convert this response,
the gate's nonempty monopoly-label set and the prescribed fan into an
explicit `K_7^-` model or an exact order-seven separation with a strictly
smaller connected side and retained literal branch-set labels.  A weaker
theorem producing another unlabelled separator would not advance the
terminalization target.

## 6. Dependencies and scope

The exact-seven part uses the separately audited
[exact-seven critical-edge fan/descent theorem](../results/hc7_exact7_critical_edge_fan_descent.md).
The maximum-`P` theorem is a strengthened normalization of the retaining
core and opposite-gate proof in the separately audited
[exact near-clique dichotomy](../results/hc7_k7minus_exact_k7vee_separator_dichotomy.md).
Lemma 4.1 separates what comes from minor-criticality from what comes from
the removable-matching theorem.

This reduction deliberately avoids needing one of the original five
matching edges to cross the separator.  It does not yet discharge the
model-labelled fan, at any boundary order, or turn a common exact boundary
block into a complete common boundary partition.
