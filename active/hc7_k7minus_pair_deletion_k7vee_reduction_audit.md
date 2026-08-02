# Internal audit: exceptional-root deletion and `K_7^\vee`

**Verdict:** GREEN for the pair- and single-deletion model reductions, the
optimized forced-interface theorem, the exact labelled-absorption contact
formula, the two-hole persistence count and deficient-bag response, the
one-operation Kempe conclusion, and the sufficient same-host descent test.
Label-preserving donor optimization, operation-to-recipient allocation, and
the terminal/descent target are correctly left open.  The recorded failed
joint-optimization route correctly identifies its two ordered quantifier
gaps and does not present them as a counterexample.

**Audited source:**
`active/hc7_k7minus_pair_deletion_k7vee_reduction.md`

**SHA-256:**

```text
aca10eb92f3901207db70abc397c7aa317924220705c014632054e303169eb88
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

## 7B. Joint-optimization negative finding

For the deficient-bag application of Proposition 6 one has `p=1`.  The
contact formula in (A1) then makes a labelled absorption globally
contact-maximal only when `k>=3`; no proved statement excludes `k<=2` in
the absolute minimum rooted `P`-bag family.  Thus the failed attack cannot
legitimately start the optimized forced-interface argument on the same
model and response.

Even conditional on `k>=3`, Theorem 4 minimizes the donor over all
contact-maximal spanning `K_6` models.  Its transfer proof preserves the
six fused branch sets, not necessarily the separate `P,U_h` refinement or
the support of the fixed jointly persistent pair.  The source therefore
correctly rejects a lexicographic potential combining these choices: the
relevant family has not been proved exchange-closed.

The two stated repair lemmas address these gaps in their logical order.
The note claims neither that they hold nor that their failure is realized
by a graph satisfying the critical-host hypotheses.  This is a scoped
negative finding about an unsupported proof mechanism, not a barrier or a
mathematical disproof of the one-operation target.

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
