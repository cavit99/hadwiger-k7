# Internal audit: exceptional-root deletion and `K_7^\vee`

**Verdict:** GREEN for the pair- and single-deletion model reductions, the
optimized forced-interface theorem, the exact labelled-absorption contact
formula, the two-hole persistence count and deficient-bag response, the
one-operation Kempe conclusion, the root-removal split proposition, the
two-owner portal collapse and terminal two-shore colouring, the fixed-response
nested-separator reduction, the connected two-loss atomic reduction, and the
exact order-seven/eight minimum-separator normal form with its order-eight
centred consequences, the persistent same-trace single-edge response, the
forced clean-fan and low-degree seven-column order-eight responses, their
connected-exterior root-aligned specialization, and the sufficient
same-host descent test.
Label-preserving donor optimization, operation-to-recipient allocation, and
the global terminal/descent target are correctly left open.  The recorded
separator-terminalization and joint-optimization failures identify exact
unsupported inferences and do not present them as counterexamples.

**Audited source:**
`active/hc7_k7minus_pair_deletion_k7vee_reduction.md`

**SHA-256:**

```text
7541a7f0f20ad1f407acd9158cfef5f76eb48d39ea528e57d943c1d1fec8b17e
```

This is a separate internal mathematical audit, not external peer review.
The new branch-set arguments were also cold-checked against the live and
archived transfer corpus before this audited update.

## 1. Density and external theorem matching

For degree-eight vertices `a,b`, deletion removes exactly

\[
                         16-\mathbf 1_{ab\in E(G)}
\]

edges.  The established disconnected-centre density bound `m>=4n` therefore
gives

\[
 |E(G-\{a,b\})|\ge4|V(G-\{a,b\})|-8
                    +\mathbf 1_{ab\in E(G)}.
\]

Deleting two vertices from a seven-connected graph leaves a
five-connected graph.  The hypotheses of Norin--Totschnig, Theorem 6,
therefore match: every four-connected graph with at least `4n-8` edges has
a `K_7^\vee` minor unless it is `K_{2,2,2,2}`.  The established
`n_8>=25+tau` gives `|V(G)|>=25`, so the deletion has at least 23 vertices
and cannot be the eight-vertex exception.

The checked density dependency is

```text
e1b54acdd971831786c0d8912d5e4189aaeedd84184540ed438e594aadb9b2e4  results/hc7_k7minus_one_nonfull_k5_and_nested_cut.md
```

## 2. Spanning enlargement and contact restrictions

Every component outside the initial model union has an edge to that union,
because the deletion graph is connected.  Assigning each whole component
to one adjacent branch set preserves connectedness, disjointness, and every
required model adjacency.  If this creates either nominally missing
adjacency at the deficient branch set, the seven enlarged bags already
contain a `K_7^-` model.  Thus in the target-free host the spanning model
retains both missing pairs.

The six nondeficient bags form a literal clique in the branch-set contact
graph.  A retained root meeting five of them completes a `K_7^-` model.
If a root meets the deficient bag and either missed twin, absorbing the
root into the deficient bag repairs that adjacency and leaves at most the
other one missing.  Finally, if both roots meet the deficient bag and all
four universal bags, those five bags and the two singleton roots have at
most the root--root adjacency missing.  These constructions verify all
three contact restrictions.

## 3. Localization and scope

At most nine degree-eight vertices lie in `N[u]`; hence

\[
                         n_8(E)+n_8(F)\ge16+\tau
\]

for the two exterior components.  This is only a sum.  Neither the degree
identity nor seven-connectivity gives a positive lower bound for either
summand separately.

The four-bag concentration in the source is explicitly an abstract contact
pattern not excluded by the proved restrictions, not a constructed graph
satisfying the critical hypotheses.  The theorem does not split a model
bag, return a boundary equal to `N(z)` for a named degree-eight vertex,
eliminate an attachment regime, construct a `K_7^-` minor, or produce a
six-colouring.  No finite computation is used.

## 4. Spanning `K_6` normalization

For every universal branch set `U_h`, the old `P-U_h` edge makes
`P union U_h` connected.  Its `U_h` part retains edges to `B,C` and the
other three universal branch sets.  Thus the six displayed sets are
connected, disjoint, spanning and pairwise adjacent.

The four-contact bound is valid for every spanning `K_6` model in `H`, not
only these four normalizations.  If a retained root met five of the six
branch sets, the singleton root and the model would have at most one
missing adjacency and would be a `K_7^-` model.

Since a retained degree-eight root has seven or eight neighbours in `H`,
some contacted branch set contains at least two of them.  The optimization
in the source is correctly over all pairs `(Q,D)` consisting of a
contact-maximal spanning model and an eligible surplus donor.  Minimizing
only within one preselected model would not support the later contradiction.

## 5. Forced target interface

Let `Y` be a retaining core and `C` a component of `D-Y` containing a
target portal outside `Y`.  Connectedness of `D` makes every component of
`D-Y` adjacent to connected `Y`; hence both `C` and `D-C` are connected.
The latter retains a root neighbour and all four protected contacts through
`Y`, while `C` meets the target.

Moving `C` to the target is the already audited one-admissible transfer; the
contact increment is its immediate fixed-root corollary.  The cut edge from
`C` to `Y` repairs the donor--target adjacency.
If `C` contains a root neighbour, the target gains contact while the donor
retains contact through `Y`.  If `C` is root-free, all root neighbours stay
in the smaller donor.  These contradict respectively contact maximality and
the global donor minimum, proving

\[
                         A_D(T)\subseteq Y.
\]

For the cutvertex consequence, deleting a non-cutvertex target portal leaves
a connected donor with a root neighbour.  Unless that vertex is the unique
portal to a protected branch set, the remaining donor is itself a retaining
core.  Distinct such non-cutvertices require distinct singleton protected
portal sets, so there are at most four.

The proposed conditional augmentation lemma was not duplicated: it is
already proved by Lemma 1 of the audited surplus-root transfer note.  What is
new here is the optimized target-interface intersection for the pair-deletion
normalization.  The audit found no previous statement of that exact
consequence.

## 6. Global exceptional-root extension

For any exceptional degree-eight vertex `r`, the graph `J=G-r` is
six-connected and the audited global density bound gives

\[
 |E(J)|=|E(G)|-8\ge4|V(J)|-6.
\]

This exceeds the Norin--Totschnig threshold by two edges.  The global count
`b>=17` gives `|V(J)|>=16`, excluding `K_{2,2,2,2}`.  The same spanning
enlargement argument therefore gives an exact spanning `K_7^\vee` model in
`J`, and absorbing its deficient bag into a universal bag gives a spanning
`K_6` model.

The checked global density dependency is

```text
421544721b5084fe5dff280cd2299f0e4cb214ba39bc2b2fde5648fc393bcd83  results/hc7_k7minus_two_literal_k5_exclusion.md
```

Five contacts between `r` and any spanning `K_6` model would give a
`K_7^-` model.  Its eight neighbours therefore lie in at most four bags,
so a bag containing at least two exists.  The forced-interface proof uses
no second deleted root and hence applies after optimizing over all spanning
`K_6` models in `J`.

The archive already contains contact-maximal spanning `K_6` models and
surplus-root analysis in `G-r`; that part is not new.  The additional exact
near-clique model and the globalization of the forced-interface intersection
are the new deductions.  The audit also checks the stated limitation: a
globally optimized `K_6` model need not retain the `P,B,C` provenance of one
selected near-clique model.

## 6A. Exact labelled-absorption contact formula

If `p=0`, merging `P` with `U_h` preserves the old contact count `k`.  If
`p=1`, the merged bag is contacted regardless of `U_h`, so the new count is
`k` or `k+1` according as `U_h` was contacted or missed.  When `p=1`, target
exclusion makes `r` miss `B,C`; hence `k` counts only contacted universal
bags.  The cases attaining four contacts and the two unresolved regions in
(A2)--(A3) follow exactly.

Four is the unrestricted upper bound for every spanning `K_6` model, so an
absorption attaining four is globally contact-maximal.  This does not make
the four-absorption family exchange-closed.  A transfer only preserves a
contact with the fused bag and may lose its separate `P` or `U_h` portal.
For donors `B,C`, anticompleteness to `P` forces that contact to use `U_h`,
which verifies the stated safe class.  No analogous conclusion is claimed
for a universal donor.  A fused-donor transfer can also destroy the
connectivity or nonemptiness required to recover the original two branch
sets, and the source now records this separately.

## 7. One fixed edge-deletion response

In every six-colouring of `G-rx`, the endpoints `r,x` have one common
colour `alpha`; otherwise the deleted edge can simply be restored.  Each
other colour occurs at a neighbour of `r`, since a missing colour could be
assigned to `r`.  If the `alpha,beta` component of `x` omitted `r`, swapping
that component would again make `rx` proper and six-colour `G`.  A shortest
component path to `r` therefore gives the five claimed paths in `G-r`, all
from the same named operation.

This conclusion carries colour labels, not branch-set labels.  The source
correctly does not infer pairwise disjoint target and owner pieces.  Existing
prescribed-spoke machinery does extend the five distinct first edges in the
six-connected graph `G-r` to any chosen five-set, including one vertex in
each named target or protected bag.  It does not prescribe the pairing and
does not stop a path from first entering a differently labelled bag.  The
rerouting retains operation-generated first edges, not bichromatic paths.
Thus it supplies named ends, not clean named first hits.  Existing first-hit
and Rado--Menger results likewise do not turn an internal separator into a
bounded host separator or identify it with `N(z)`.  The first unsupported
operation-level inference is therefore stated at the right point.

## 7A. Two-hole persistence and the deficient-bag response

Proposition 6 is a genuine two-missing-edge adaptation of the cited rooted
persistence theorem, rather than an application of that theorem verbatim.
Target exclusion makes every reselected labelled `K_7^\vee` model exact:
filling either `PB` or `PC` gives `K_7^-`.  For every component of `R-r`,
the same reassignment argument therefore forces at least two exclusive
required labels.  The private-label count and exact degree identity give

\[
 \rho=8-m+k_0+2k_1+q+\sigma\ge9-m.
\]

Support classes have independent deletion effects.  A non-joint pair can
only be an entire class of order two, so the non-joint pairs form a
matching.  If all joint pairs have adjacent outer endpoints, `K_4`-freeness
of `G[N(r)]` gives exactly `K_5-2K_2` at `rho=5`, exactly `K_6-3K_2` at
`rho=6`, and excludes `rho>=7`.

For `D=P`, the lower bound is five.  Equality `rho=5` forces
`k_0=k_1=sigma=0` and `q=1`; all five persistent edges then form one
external support class.  Their outer endpoints would be a `K_5` under the
no-good-pair assumption, contradicting `K_4`-freeness.  At `rho=6`, a
six-fan in `G-r` from a remaining neighbour to all six endpoints gives a
connected set `T` disjoint from and adjacent to those endpoints.  If the
three possible missing pairs are `a_i b_i`, then

\[
 \{a_1,a_2\},\{b_1\},\{b_2\},\{a_3\},\{b_3\},\{r\},T
\]

are seven disjoint connected branch sets with only `a_3b_3` possibly
nonadjacent.  This verifies the explicit `K_7^-` contradiction and hence
the nonadjacent jointly persistent pair for every minimum `P`-bag.

Contracting its two-edge star is a proper minor.  Pullback gives the exact
three-vertex common colour class on the deleted incident edges; a missing
alternate colour at the other six neighbours would extend to a
six-colouring of `G`.  Joint persistence keeps the same labelled model.
The audit separately confirms the stated limit: no palette colour has yet
been assigned to a required branch-set role.

## 7B. Root-removal compatibility and the split residue

For `D=P`, the protected label set has order four.  Proposition 6 proves
that the monopoly sets of the components of `R-r` are disjoint and each
has order at least two.  A universal label directly contacted by `r` is
counted either by its unique nonpersistent edge in `ell`, or once in `q`
when a persistent edge exists.  Any second `R-U_i` edge would preserve the
required adjacency after deletion, so a nonpersistent contact is unique;
conversely every `ell` edge and `q` label is a direct universal contact.
Thus `k_R=ell+q`, and (B4) gives the sharper

\[
                             2h+k_R\le4.
\]

This yields at most two components and at most two direct universal
contacts whenever the rooted bag is nonsingleton.  If the bag is the
singleton `{r}`, all four required universal adjacencies are direct.

If there are two, both monopoly sets have order two and partition the four
universal labels.  Exactness gives no edge from `R` to either missed twin.
For an owned universal label, every endpoint in `R` lies in its owning
component; hence the opposite component has no edge to that bag.  If `r`
met a universal bag, that label's endpoint set in `R` would not be contained
in either component and the label could not occur in the asserted
partition.  Thus `r` has no foreign-bag neighbour.  Spanningness then puts
all eight neighbours of `r` in the two components and proves the two
neighbourhood inclusions in (B8).

Both root-neighbour sets are nonempty and anticomplete.  The audited
exceptional-neighbourhood theorem, at SHA-256

```text
fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd
```

gives both `alpha(G[N(r)])=3` and `K_4`-freeness.  Additivity across the
anticomplete partition makes the two independence numbers one and two.
The independence-one side is a clique of order at most three, leaving at
least five root neighbours on the other side.  This verifies (B9).

The larger side has at least five incident root edges.  Each is persistent,
and any two are jointly persistent because other edges still attach that
component to `r`.  Its endpoints cannot form a clique in the `K_4`-free
neighbourhood, so the nonadjacent persistent pair may be selected wholly
inside this component.  This verifies the strengthened response statement
and (B9).

For one two-owner component, disjoint paths from the two owner portal sets
to distinct root portals would partition the component into two connected
pieces.  Moving those pieces into their corresponding owners leaves
`{r}` plus the other component as a connected deficient bag; the root
edges to the distinct terminal vertices restore the two lost universal
adjacencies.  This is a smaller spanning rooted model, contradicting the
minimum.  Hence the audited two-owner Rado--Menger theorem, at SHA-256

```text
4cd27295dc89c172d4246c67a529b87318d9e4343e5185dc5233f37d04f7109b
```

gives one vertex meeting every path from the root portals to the union of
the two owner portal sets.  If the owners are not both concentrated at that
vertex, a component behind it contains an owner portal but no root portal.
The exact `2+2` ownership makes its whole host neighbourhood lie in the
separator vertex and the two owner bags.  This is an actual separator from
the surviving root, so seven-connectivity gives order at least seven; the
two bags then contribute at least six literal neighbours in total and one
contributes at least three.  This checks (B10).

On the large root-neighbour side, deleting any prospective common owner
portal `s` leaves vertices of the component.  Their only possible external
neighbours are `r` and `s`: exact ownership excludes all other branch bags.
This would make `{r,s}` a separator, contradicting seven-connectivity.
Hence the large side necessarily gives the thick host separator outcome,
as claimed.

The source correctly does not infer compatibility merely from having at
most one component.  To become the deficient bag of a model in `G-r`, the
remainder must be nonempty and connected and every one of the four required
universal adjacencies must have a surviving endpoint outside `r`.
Proposition 6 does not exclude failure of any of these requirements.

## 7C. Two-owner portal collapse and terminal colouring

The connected set in (B10) is detachable from the minimum rooted `P`-bag:
its complement remains connected, it has one attachment inside that bag,
and it has foreign neighbours only in its two owner bags.  If it contacts
one owner while a portal to the other owner remains outside, moving the set
into the contacted owner preserves every labelled adjacency and strictly
shrinks the rooted bag.  Applying this in both directions proves that the
set monopolizes both owner adjacencies.

Choose an inclusion-minimal connected lobe with that property.  A full
two-owner linkage to two distinct residual attachment vertices would split
the lobe between the owners and shrink the rooted bag.  Its Rado--Menger
failure therefore gives one vertex meeting every attachment-to-owner path.
If either owner portal is not concentrated there, a component behind that
vertex avoids the residual attachment set.  The same one-owner transfer
argument makes this smaller component monopolize both owners, contradicting
the lobe minimum.  Both owner portal sets are consequently the same
singleton.  Any remaining component of the lobe minus that singleton has
all host neighbours in the singleton and the unique parent vertex, contrary
to seven-connectivity.  This verifies (B11), including the exact single
`P`-neighbour and both portal monopolies.

Let `Q=Z_2-\{t\}`.  It is nonempty because it contains `W_2`.  The unique
`R`-neighbour of `t` makes `t` a leaf of the connected graph `G[Z_2]`, so
`Q` is connected.  Spanningness identifies the complementary open side
`H` as `Z_1` together with the six foreign branch sets.  Those branch sets
form a connected `K_6` contact graph and `Z_1` meets its two owner bags, so
`H` is connected.

Exact ownership and portal monopoly give no edge between `Q` and `H`.
Both sides see both `r,t`: `W_2` and the parent `p` do so on the `Q` side,
while `W_1` and the two owner bags do so on the `H` side.  Also `rt` is
absent.  Contracting `H union \{r\}` therefore gives exactly
`G[Q union \{r,t\}]+rt`, and the
symmetric contraction of `Q union \{r\}` gives exactly
`G[H union \{r,t\}]+rt`.  Both are proper minors.  Their six-colourings
make `r,t` distinct, so one palette permutation aligns the ordered pair and
the colourings glue across `\{r,t\}`.  This verifies the terminal
six-colouring contradiction and the conclusion `h<=1`.

## 7D. Fixed-response nested separator

The minimum rooted deficient bag `R` is anticomplete to the two missed twin
bags, so its open neighbourhood lies in the four universal bags and is an
actual separator of order at least seven.  Removing the two persistent
incident edges deletes at most two boundary vertices.  Joint persistence
retains at least one `H`-edge from `R` to each universal bag, hence at least
five surviving boundary vertices distributed over four bags.

The separately audited exact-`K_7^\vee` separator dichotomy applies to two
surviving portals in one bag.  It produces either a `K_7^-` model using no
deleted edge or a proper connected donor piece with connected complement
and an actual separator in `G`.  Under (H) the first outcome is impossible.
The construction does not recolour `H`, so the named two-edge-star response
remains fixed.  This verifies Proposition 9.

The separator conclusion is deliberately nonterminal.  Its order need not
be seven, the deleted endpoints need not occupy opposite open shores, and
the separator need not be the neighbourhood of an exceptional vertex.

## 7E. Connected two-loss atomic reduction

Suppose `Z=R-r` is connected and exactly two universal adjacencies are lost.
The other two owner portal sets and the root-neighbour set in `Z` are
nonempty.  A two-owner Rado--Menger linkage would split `Z` into two
connected pieces and reduce the rooted bag.  Failure therefore gives one
vertex separating the root-neighbour set from both owner portal sets.

If both owner portal sets are that singleton, seven-connectivity forces
`Z` itself to be the singleton.  Otherwise the portal-side component is
root-free and the two one-owner transfer orientations force it to contain
both complete owner portal sets.  A second, inclusion-minimal two-owner
application collapses its retaining lobe to a singleton `t` with one open
neighbour `q` in the rooted bag.  Any nontrivial remainder would have all
host neighbours in `{q,t}`, contradicting seven-connectivity.

Thus `t` is a leaf of `G[Z]`.  The connected set `Q=Z-t` and the union `J`
of the six foreign branch sets are nonempty, connected and anticomplete.
Both meet the nonadjacent vertices `r,t`: `Q` through the root-neighbour set
and `q`, and `J` through the two lost-owner contacts at `r` and the two
retained owner contacts at `t`.  Contracting either open side together with
`r` gives the corresponding exact proper minor with `rt` added.  Their
six-colourings align on the ordered boundary `(r,t)` and glue.  This checks
Proposition 10.  In fact `{r,t}` is already a two-vertex cut; the colouring
splice explicitly realizes the requested terminal.

The only survivor is the atomic bag `R={r,s}` with the exact `2+2` owner
split.  This is an adaptation of Proposition 8, not a new general gluing
method, and it does not use the fixed two-edge-star colouring.

## 7F. Minimum-separator normal form

Proposition 9 makes the family of all connected sets with a nonempty far side
nonempty.  Its minimum boundary order `s` equals `kappa(G)`: every member
has a separating boundary, while a component behind a minimum vertex cut
belongs to the family and has that cut as its full neighbourhood.  The
audited Jakobsen bound `2|E(G)|<=9|V(G)|-25` and
`delta(G)>=kappa(G)=s` exclude `s>=9`.  Thus the minimum order is exactly
seven or eight.  At boundary order seven,
the audited
critical capacity theorem and three-component exclusion give exactly two
components, packing vector `(1,1)`, `(1,2)`, or `(2,1)`, and a boundary
edge.  The general seven-cut capacity theorem also excludes a boundary
`K_5` minor, and the established `t=5` case gives four-colourability.

At minimum boundary order eight, the selected set is eligible for
the audited minimum-positive-separator theorem.  Its exact-seven alternative
would itself be a member of the minimizing family with smaller boundary, so
the full-component alternative is forced.  That theorem gives exactly two
or three components.

For an `a`-set `F` of boundary vertices, augment `a` full components with
the distinct members of `F` and contract one additional component without a
boundary vertex.  The `a+1` images form a clique complete to the retained
boundary.  Proper-minor six-colourability gives
`chi(G[S-F])<=5-a`; a `K_{6-a}^-` model there would complete a literal
`K_7^-` model.  The constructed minor is proper by deletion of another
component when `a=0`, and by an augmented component--boundary contraction
when `a>0`.

Using two unaugmented components instead makes their mutual adjacency the
only missing pair.  A `K_{5-a}` model in the retained boundary would again
complete a `K_7^-` model.  At `a=0` this excludes a `K_5` minor from the
whole boundary, and the established `t=5` case of Hadwiger's conjecture
gives four-colourability.

The lower chromatic bounds use direct contractions, not the order-seven-only
reflection lemma.  With two components, an independent boundary can be
contracted into the opposite full component on each shore.  With three
components, at most two independent boundary classes can be assigned to
the other two full components on each shore.  In both cases the exact
boundary partitions align and the closed-shore colourings glue, contradicting
`chi(G)=7`.  No finite enumeration enters these arguments.

In the order-eight outcome, `kappa(G)=8` and the defect identity gives

\[
 25\le9|V(G)|-2|E(G)|=n_8-\tau.
\]

Hence `delta(G)=8`, `n_7=0`, `|E(G)|>=4|V(G)|`, and
`n_8>=25+tau`.  At most one literal `K_5` exists and it contains every
nonexceptional degree-eight vertex, so `b>=20+tau`.

Every degree-eight singleton `{z}` is another member of the minimizing
family: `n_8>=25` leaves a nonempty far side and `|N(z)|=8`.  Repeating the
same arbitrary-minimizer argument shows that `G-N[z]` is connected or has
two components, all full to `N(z)`.  Two singleton components behind a
full eight-cut would be nonadjacent false twins; a six-colouring after
deleting one extends by the colour of the other.  Thus there is at most one
singleton component, and both exterior components in the disconnected
centred case are nonsingleton.

The fixed colouring is not changed by selecting another separator, but the
global minimizer need not be nested in the Proposition 9 side or retain any
near-clique label.  The colouring need not be proper on either closed side
after the deleted edges are restored, and its endpoints need not avoid the
new boundary.  Proposition 11 therefore does not claim a terminal outcome or
operation-to-shore alignment.  These additional consequences likewise do
not supply a terminal outcome.

## 7G. Persistent same-trace single-edge response

The pulled-back two-edge-star colouring gives `r,x,y` one colour and uses
all five other colours on the remaining six neighbours of `r`.  Exactly
four of those six vertices therefore have a unique residual colour.
Proposition 6 supplies at least five persistent incident edges, including
`rx,ry`; the four unique-colour vertices and five persistent endpoints in
the eight-set `N(r)` must intersect.

For a vertex `z` in the intersection, recolour only `r` with `c(z)`.
The edges `rx,ry` become proper and `rz` is the sole new monochromatic
edge, so deleting it gives a six-colouring of `G-rz` agreeing with the
fixed response away from `r`.  Individual persistence of `rz` retains the
same labelled model.  This improves trace compatibility but does not assign
the five colours to the required branch-set roles.

## 7H. Forced order-eight operation responses

In the order-eight branch, the order-seven outcome of the audited
operation-coupled response theorem contradicts `kappa(G)=8`; its clean
five-path fan is therefore forced for every crossing-edge response.

For the two-component case, minimize the selected open side after boundary
order.  The arbitrary-edge response-star theorem then has neither an
order-seven outcome nor a strict order-eight response-side descent, so its
paired-root seven-column outcome is forced.  A `K_5^-` minor in the column
contact graph, joined to the two adjacent roots which are complete to all
columns, would lift to a `K_7^-` minor.  The contact graph is therefore
`K_5^-`-minor-free.  The seven-column theorem leaves low degree or the
pentagonal bipyramid; contracting two disjoint rim edges of the latter
gives a triangle complete to two nonadjacent poles, an explicit `K_5^-`
model.  Hence the contact graph has minimum degree at most three.

For the connected-exterior specialization, `S=N(r)` is a minimum
order-eight cut and `G-S` has the two full components `{r}` and `G-N[r]`.
The arbitrary-edge theorem applies with operated side `{r}` and edge `rz`.
Eight-connectivity excludes its order-seven outcome, and its strict
response-side descent cannot be a nonempty proper subset of a singleton.
Thus the paired-column outcome is forced without replacing the root, edge,
or colouring from Proposition 12.  The target contains `z`, and the same
five Kempe components generate the source paths.  The preceding
contact-graph argument again gives minimum degree at most three.

On `N(r)`, the vertices `x,y` retain their common old root colour.  The
other six vertices use all five remaining colours, so their multiplicities
are `2,1,1,1,1`; Proposition 12 chooses `z` in a singleton class.  The
full boundary partition is therefore `2,2,1,1,1,1`, with `z` singleton.
The surviving labelled near-clique model and paired columns are tied to the
same deleted edge and colouring, but no inference identifies their two
label systems.  The source correctly leaves that allocation open.

This is still nonterminal.  The low-degree column need not be the operated
target, and an operation-generated path may meet a root or another column
before its intended target.  The result neither performs a label-preserving
dirty-path exchange nor identifies a smaller exceptional anti-neighbourhood.

## 7I. Recorded route nonclosures

For an exact-seven separator returned by Proposition 9, its connected side
is a component and the three-component exclusion leaves one opposite
component.  The root lies outside the returned side.  Since `rx,ry` are the
only edges absent from the fixed response graph, the stated closed-shore
legality conditions follow exactly from endpoint placement.  If an endpoint
`z` is outside the boundary, the edge `rz` lies wholly in one closed shore;
a colouring of `G-rz` is therefore proper on the opposite one.  Its ends
must be equal, and joint persistence keeps the same labelled model.  If both
endpoints lie in the boundary, a colouring of the double deletion proper on
the literal boundary would colour both restored edges and hence all of `G`.
This verifies the endpoint normalization and its exceptional placement.

The legal one-sided trace obtained from a single-edge response need not be
the trace of the original double-deletion colouring.  More importantly, the
packing vector supplies too few partition-specific connected subgraphs to
invoke selected-response preservation automatically.  The normalization is
therefore a proved reduction inside the recorded nonclosure, not a terminal
claim.

For the nested-separator route, even endpoint alignment only proves that
two boundary-avoiding Kempe components would six-colour `G`; failure may
leave one endpoint five-colour saturated through the boundary vertex `r`.
No audited theorem turns that saturation into a labelled transfer, common
boundary partition, or named exceptional anti-neighbourhood descent.
The cited nested full-neighbourhood theorem can reduce separator excess but
does not preserve the operation or a named centre.  The exact-seven selected
response theorem closes only after a partition-specific carrier system is
supplied; the present frame does not provide one.

The separate absorption route retains its older quantifier mismatch.
Proposition 6 minimizes a rooted labelled model, whereas Theorem 4 globally
optimizes a spanning `K_6` model.  A donor transfer in the latter can lose
the separate `P,U_h` refinement or the support of the fixed persistent pair.
The source therefore correctly rejects exchange closure.  Both statements
are scoped negative findings, not counterexamples to the open target.

## 8. Same-host descent test

Choose a minimum-order component `C_0` among all `G-N[v]`, with `v`
exceptional.  For `J=G-r`, let `W` be a component of `J[Z]` under (14).
There is no edge in `G-N[r]` from `W` to:

- another component of `J[Z]`, by componenthood; or
- `J-Z`, because every such neighbour lies in `N(r)`.

Thus `W` is a component of `G-N[r]`, and `|W|<|C_0|` is a strict
same-host descent.  In a pair-deletion host one must additionally exclude
edges from the other omitted root.  This is why the source requires the
extra condition there.

The operation-level target is logically sufficient: its minor and colouring
outcomes contradict the critical-host hypotheses, while its descent outcome
contradicts the global choice of `C_0`.  It is important that `C_0` and `W`
are components.  Whole exceptional anti-neighbourhoods all have order
`|V(G)|-9`, so no strict order descent is possible between whole exteriors.
The source correctly labels this finishing target open.
