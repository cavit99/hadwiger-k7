# Rooting an ordinary `K_5^-` minor: the exact contraction gate

**Status:** proved small-order theorem and unbounded minimal-counterexample
reduction.  Any counterexample to rooting an ordinary `K_5^-` minor has at
least seven shore vertices, and every edge inside a chosen branch bag is
blocked by a coefficient-neutral exact six-fragment.  The note does not yet
eliminate those fragments.

## 1. Setup

Let `S` be a stable six-set and let `C` be a connected `S`-full shore.  Write
`H=G[C union S]` and assume the relative six-connectivity condition

```text
|N_C(X)|+|N_S(X)|>=6                 (1)
```

for every nonempty `X subseteq C`.  This is automatic when `C` is a component
of `G-S` in a six-connected host.

The desired **ordinary-minor implication** is

```text
C has a K_5^- minor
  => H has a punctured S-rooted K_5^- model
     or mu_S(C)>=2.                                  (2)
```

## 2. Exact theorem through shore order six

### Theorem 2.1

If `|C|<=6` and `C` has an ordinary `K_5^-` minor, then `H` has a punctured
`S`-rooted `K_5^-` model.  The packet alternative is not needed.

### Proof

For every nonempty `X subseteq C`,

```text
|N_C(X)|<=|C|-|X|<=6-|X|.
```

Together with (1), this gives

```text
|N_S(X)|>=|X|.                                      (3)
```

Apply Hall's theorem to the bipartite incidence graph between `C` and `S`.
Condition (3) gives a matching which saturates `C`.

Let `B_1,...,B_5` be the disjoint connected branch bags of any ordinary
`K_5^-` model in `C`.  Choose one vertex `v_i in B_i` from each bag.  Their
five matching partners `s_i in S` are distinct.  Enlarge `B_i` to

```text
B_i union {s_i}.
```

Each enlarged bag is connected, the five bags remain disjoint, and all old
quotient adjacencies remain.  They are rooted at five distinct vertices of
`S`; the unused sixth root is absent.  Thus they form the required punctured
rooted model.  □

This proof covers both a literal near-clique and a six-vertex model with one
two-vertex branch bag.  It also corrects a tempting but invalid larger-order
shortcut: when `|C|>6`, vertices outside a literal five-vertex core contribute
to `N_C(X)`, so (1) alone need not give Hall directly on that core.

### Theorem 2.2 (a literal near-clique at arbitrary order)

At any shore order, if five vertices `W subseteq C` span a `K_5^-`, then `H`
has a punctured `S`-rooted `K_5^-` model.

### Proof

There are five vertex-disjoint `S`--`W` paths in `H`.  Indeed, a separator
`T` of order at most four leaves a vertex of both `S` and `W`.  If no
`(S-T)`--`(W-T)` path remained, a component `X` containing a surviving vertex
of `W` and no vertex of `S` would satisfy `N_H(X) subseteq T`, contrary to
(1).  The set version of Menger's theorem now gives the five paths.

Orient them from `S` to `W`.  First truncate each path at its first vertex of
`W`, and then replace it by the subpath beginning at its last vertex of `S`
before that end.  They remain disjoint, meet `S` and `W` only in their
distinct ends, and their five `W` ends exhaust `W`.  Use the five paths as
branch bags.  Their ends in `W` inherit all nine edges of the literal
`K_5^-`, whilst their ends in `S` are five distinct roots and the sixth root
is absent.  □

Thus a counterexample to the ordinary-minor implication must use a genuinely
nonliteral minor model; the obstruction is in its nonsingleton branch bags,
not in routing to a five-vertex near-clique already present.

## 3. Exact behaviour under one branch-bag contraction

Fix an edge `uv` of `C`, contract it to a vertex `w`, and give `w` the union
of the boundary neighbourhoods of `u,v`.  Denote the contracted shore by
`C/uv`.

### Lemma 3.1 (the only connectivity failure)

The contracted shore fails (1) if and only if there is a nonempty connected
set

```text
X subseteq C-{u,v}
```

such that

```text
|N_H(X)|=6,                 u,v in N_C(X).           (4)
```

For such an `X`, contraction identifies the two boundary vertices `u,v` and
reduces the boundary order from six to five.  In particular, (4) is an exact
six-fragment with both ends of the contracted edge on its boundary.

### Proof

Consider a nonempty set `Y subseteq C/uv`.  If `w in Y`, lift it to

```text
(Y-{w}) union {u,v}.
```

Its internal and root boundary is unchanged by contraction.  If `w` is not
in `Y`, regard `Y` as the same subset of `C-{u,v}`.  Its boundary changes only
by identifying `u` and `v`, and hence drops by one exactly when both vertices
belong to the old boundary.  Since the old boundary has order at least six,
the new condition fails exactly when a (not necessarily connected) witness
satisfies (4).  For any component `X_0` of that witness,
`N_H(X_0) subseteq N_H(X)`.  Condition (1) forces the first set to have at
least six vertices, so equality holds and `N_H(X_0)=N_H(X)`; in particular
both `u,v` remain on its boundary.  Replacing the witness by `X_0` gives the
connected formulation.  The converse is immediate.  □

### Lemma 3.2 (all three conclusions lift)

Suppose `uv` lies inside a branch bag of an ordinary `K_5^-` model.

1. The contracted shore still has an ordinary `K_5^-` model.
2. A punctured rooted `K_5^-` model in the contracted shore lifts to one in
   the original shore.
3. Two disjoint connected `S`-full packets in the contracted shore lift to
   two such packets in the original shore.

### Proof

For the first assertion contract `uv` inside its branch bag.  For the second,
if a rooted branch bag uses `w`, replace `w` by the adjacent pair `{u,v}`;
every incident edge represented after contraction has an original end at
`u` or `v`, so connectedness and all bag contacts lift.  If `w` is unused,
nothing changes.  For the third assertion, at most one of two disjoint packets
uses `w`; replace it there by `{u,v}`.  Connectivity and the union of boundary
neighbourhoods are preserved, and disjointness from the other packet remains.
□

## 4. Minimal-counterexample consequence

### Corollary 4.1

Let `(C,S)` be a minimum-order counterexample to (2), and choose any ordinary
`K_5^-` branch model in `C`.  Then `|C|>=7`, and for every edge `uv` lying
inside one of its branch bags there is a nonempty exact fragment `X` satisfying
(4).

### Proof

The order bound is Theorem 2.1.  If contraction of a branch-bag edge preserved
(1), Lemma 3.2 would give a smaller shore with an ordinary minor.  Minimality
would return a rooted model or two packets, and either conclusion would lift,
contrary to the choice of `(C,S)`.  Lemma 3.1 therefore supplies (4).  □

For each returned fragment, the coefficient-four excess has the exact
additivity used elsewhere in the sparse-six-cut programme, and punctured-model
exclusion reroots hereditarily to its derived six-boundary shore.  What is not
automatic is transfer of two packets across that exchanged boundary.  Thus
Corollary 4.1 identifies the same exact two-copy obstruction as the portal
descent, now forced along every nonsingleton branch bag of the ordinary minor.

## 5. Order-seven Hall profile

The first possible order is already highly rigid.  Suppose `|C|=7` and
normalise an ordinary model to a partition `B_1,...,B_5` of `C`: every
component outside the five bags meets a bag because `C` is connected, and can
be absorbed into one it meets without losing connectivity or a quotient edge.
If the
root--bag incidence graph has no matching saturating the five bags, choose an
inclusion-minimal Hall-deficient family `I`, put `i=|I|` and
`U=union_{j in I}B_j`.  Then

```text
|U|=i,
|N_S(U)|=i-1,
N_C(U)=C-U.                                          (5)
```

Indeed, (1) and Hall deficiency give

```text
6 <= |N_C(U)|+|N_S(U)|
  <= (7-|U|)+(i-1),
```

while `|U|>=i`; equality is forced throughout.  Hence every bag in `I` is a
singleton and every one of those singleton vertices is adjacent to every
vertex outside `U`.  Minimality of `I` gives a matching of `i-1` of these
singletons to the `i-1` roots in `N_S(U)`.

There is also a perfect matching between `C-U` and `S-N_S(U)`.  For every
nonempty `Y subseteq C-U`, apply (1) to `U union Y` and use
`|N_C(U union Y)|<=7-i-|Y|`; it follows that

```text
|N_S(Y)-N_S(U)|>=|Y|.
```

Both sides have order `7-i`, so Hall applies.  Any order-seven counterexample
must therefore have precisely one unrooted universal singleton branch bag and
two surplus, distinctly root-matched vertices in the complementary branch
bags.  The remaining issue is not root visibility but preserving the
`K_5^-` quotient when one of those surplus vertices is transferred across
the branch partition.
