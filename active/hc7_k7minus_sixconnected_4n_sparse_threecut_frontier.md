# Sparse three-component frontier for the six-connected `4n` theorem

**Status:** live conditional refinement, last consolidated on 17 August
2026.  The universal theorem, Conjecture 21 and `HC_7` remain open.  Every
statement called proved below has a separate hash-pinned internal audit; an
internal audit is not external peer review.

## 1. Entrance and exact accounting

The open extremal statement is

> Every six-connected graph `G` with `|E(G)|>=4|V(G)|` contains a
> `K_7^-` minor.

The audited
[critical contraction theorem](hc7_k7minus_critical_to_sixconnected_4n_reduction.md)
shows that this statement would imply Norin--Totschnig Conjecture 21.  The
[degree-eight low-codegree theorem](../results/hc7_k7minus_sixconnected_degree_eight_low_codegree.md)
reduces a minimum counterexample to an order-six separation.  The audited
dense-boundary and type-VII theorems eliminate every returned
three-component separation whose boundary spans at least seven edges.

The present frontier is the remaining three-component case.  Thus `S` is an
order-six cut, `G-S` has three components `C_1,C_2,C_3`, every component is
adjacent to every vertex of `S`, and

```text
|E(G[S])|<=6.
```

For a component `C`, put

```text
eta_S(C)=|E(G[C])|+|E_G(C,S)|-4|C|.
```

Writing `sigma=|E(G)|-4|V(G)|`, exact edge accounting gives

```text
|E(G[S])|+sum_i eta_S(C_i)=24+sigma,       sigma>=0.   (1)
```

No finite bound on the orders of the three components is assumed.

## 2. The local theorem which would close this case

For a six-set `U` and a connected `U`-full graph `X`, let `mu_U(X)` be the
maximum number of pairwise disjoint connected subgraphs of `X`, each
adjacent to every vertex of `U`.  A **punctured five-rooted near-clique
model** is a `K_5^-` model rooted at five vertices of `U` and contained in
the closed shore obtained by omitting the sixth root.

The exact remaining local assertion sufficient to close the entire sparse
row is the packet-weighted alternative

```text
X has a punctured five-rooted K_5^- model
  or eta_U(X)<=5 mu_U(X).                            (2)
```

Equivalently, `eta_U(X)>=5 mu_U(X)+1` forces the punctured rooted model.
The weaker sharp packet-one statement
`eta_U(X)>=6 =>` rooted model or `mu_U(X)>=2` is only the
`mu_U(X)=1` subcase; it does not bound the possible `mu_U(X)=2` lobe when
`G[S]` is a matching.  The audited
[connected-subgraph orientation theorem](hc7_k7minus_sparse_sixcut_rooted_packet_orientation.md)
shows that the weighted alternative (2) eliminates the whole case: total
packet number is at most four, and when `Delta(G[S])>=2` every lobe has
packet number one.  Combining `eta<=5 mu` with (1) gives a strict
contradiction.

This is an unbounded rooted extremal theorem, not a finite boundary
classification.  It has not been proved.

## 3. Proved structural reductions towards (2)

### 3.1 Rooted models already forced

The audited
[all-no-rooted-`K_4` closure](hc7_k7minus_sparse_sixcut_no_rooted_k4_closure.md)
proves that some component contains a rooted `K_4` for some four boundary
vertices.  It uses the fifteen Norin--Totschnig rooted inequalities and an
exact check only for the forced tree orders five and seven; it does not
extrapolate from that finite check.

The audited
[five-root construction and density inequality](hc7_k7minus_sparse_sixcut_five_root_packet_reduction.md)
proves that a punctured five-rooted near-clique model is terminal and gives
the coefficient-four inequality forced by its absence.  The audited
[four-root connected-subgraph bound](hc7_k7minus_sparse_sixcut_four_root_carrier_packing.md)
limits disjoint connected subgraphs adjacent to prescribed four-root sets.

### 3.2 Exact-six fragments are hereditary

The audited
[exact-six rerooting theorem](hc7_k7minus_six_boundary_fragment_rerooting.md)
proves a saturated linkage between the old and derived boundaries.  It
transfers punctured rooted models back to the original boundary and gives
exact additivity of `eta` across the separation.

The audited
[Hayashi--Kawarabayashi--Yoo alternative](hc7_k7minus_sparse_sixcut_tripod_or_exact_fragment.md)
therefore has a sharp output: either their rooted subdivision occurs, or a
two-separation of the four-root shore returns a genuine order-six fragment
to which the rooted exclusion and excess accounting both descend.

The audited
[spanning rooted-`K_4` support theorem](hc7_k7minus_sparse_sixcut_spanning_rooted_k4_support.md)
normalises a four-bag model and proves that each omitted root can meet at
most two branch sets.  Four actual model portals do not yield a cut of order
at most five; six-connectivity instead forces another exact order-six
fragment.  The audited
[portal-orientation descent](hc7_k7minus_sparse_sixcut_rooted_k4_portal_descent.md)
shows that at least two roots are exchanged and that every proper fragment
inherits the local alternative by minimality.  The unresolved point is
transferring two disjoint boundary-full connected subgraphs across one
saturated linkage.

In the two-exchanged-root case, the audited
[clean-path construction](hc7_k7minus_sparse_sixcut_clean_portal_path_completion.md)
and its
[connected-subgraph repair](hc7_k7minus_sparse_sixcut_packet_repaired_portal_completion.md)
give explicit seven-branch-set `K_7^-` models unless the internal portals
control separate essential arms of the rooted branch sets.  These theorems
are deliberately restricted to the two-exchange case; the proof uses a
retained original root which is absent in the four-exchange case.

### 3.3 Ordinary `K_5^-` minors

The audited
[ordinary-minor contraction theorem](hc7_k7minus_ordinary_k5minus_rooting_contraction_gate.md)
roots every ordinary `K_5^-` minor when the component has order at most six,
and roots a literal five-vertex `K_5^-` subgraph at arbitrary component
order.  In a minimum larger counterexample, contraction of every edge
internal to a branch set is blocked by a connected exact order-six fragment
containing both edge ends in its boundary.  The first possible nonliteral
order, seven, has an exact Hall-deficiency profile.

Two independently audited boundary-composition results constrain any
spanning ordinary model:

- the [two-pole property-B theorem](hc7_k7minus_sparse_sixcut_two_pole_property_b_gate.md)
  forces a branch set adjacent to at most two boundary vertices;
- the sharper
  [boundary-visibility theorem](hc7_k7minus_sparse_sixcut_nearfive_boundary_visibility.md)
  forces either one branch set adjacent to at most one boundary vertex, or
  three branch sets each adjacent to at most two boundary vertices.

The latter six-vertex set-system lemma was also checked exhaustively over
all `5,194,959` eligible multisets, including repetitions.  The proof is
unbounded; the finite check is an adversarial verification, not its basis.
The remaining task is to turn the simultaneous internal boundary vertices
of those low-visibility branch sets into a valid split or another exact-six
fragment.

The audited
[Wood--Woodall descent](hc7_k7minus_sparse_sixcut_ordinary_minor_wood_woodall_descent.md)
also controls the branch in which no ordinary near-five minor exists.  A
cutvertex yields an exact-six fragment or two disjoint boundary-full
connected subgraphs.  A three-connected minor-free component is a wheel,
the triangular prism or `K_{3,3}`; absent an exact singleton fragment, its
order is at most `31`.  Disjoint strict two-separation shores are likewise
bounded in number and size.  A nested chain of two-separations and the
finite wheel/prism/`K_{3,3}` incidence cores remain, and the current excess
bounds are not the sharp value five required by (2).

## 4. Falsified shortcuts retained as barriers

The following stronger-looking statements are false and must not be used:

- relative five-connectivity plus every three--two root partition does not
  force a rooted `K_5^-` model
  ([explicit barrier](../barriers/hc7_relative_five_three_two_carrier_rooted_k5minus_barrier.md));
- a rooted `K_4` on four stable roots need not augment to a five-rooted
  near-clique even under the relative neighbourhood condition
  ([explicit barrier](../barriers/hc7_relative_five_rooted_k4_augmentation_barrier.md));
- every density-six instance need not admit a model with only three
  one-vertex branch-set augmentations
  ([explicit barrier](../barriers/hc7_three_augmented_incidence_certificate_barrier.md)); and
- boundary-incidence data alone do not bound the excess: an unbounded
  clique-and-private-neighbour family has `mu=1` and arbitrarily large
  excess, although it does contain the required rooted model through larger
  branch sets
  ([explicit barrier](../barriers/hc7_incidence_only_rooted_k5minus_gate_clique_barrier.md)).

These examples do not refute (2).  They show that a proof must retain
multi-vertex branch sets and exact-separation structure, rather than only
incidence counts or abstract two-part connectedness.

## 5. Immediate research obligation

The live proof obligation is to eliminate a minimum counterexample to (2)
after the exact-six descent.  The proved reductions leave two concrete
forms:

1. a rooted four-bag model whose two support branch sets contain essential
   exchanged-root portals on separate arms; or
2. a spanning ordinary near-five model with one very low-visibility branch
   set or three simultaneously low-visibility branch sets, every internal
   edge contraction returning an exact-six fragment.

A valid completion must either construct the punctured rooted model, produce
two disjoint connected subgraphs adjacent to all six roots, or descend to a
strictly smaller instance while preserving both alternatives.  Merely
identifying another boundary profile does not close the programme.
