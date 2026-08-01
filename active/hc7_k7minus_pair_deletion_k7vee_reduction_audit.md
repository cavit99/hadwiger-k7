# Internal audit: exceptional-root deletion and `K_7^\vee`

**Verdict:** GREEN for the pair- and single-deletion model reductions, the
optimized forced-interface theorem, the one-operation Kempe conclusion, and
the sufficient same-host descent test.  The operation-to-recipient
allocation and terminal/descent target are correctly left open.

**Audited source:**
`active/hc7_k7minus_pair_deletion_k7vee_reduction.md`

**SHA-256:**

```text
fdfaf7e540cb36e23bac8f4327ec5632bc6555c7d1e375722ccaea2c182b1b07
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
first-hit and Rado--Menger results likewise do not turn an internal
separator into a bounded host separator or identify it with `N(z)`.  The
first unsupported inference is therefore stated at the right point.

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
