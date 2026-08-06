# Canonical seven-boundary five-contact attack

**Baseline:** `b5e69a700bb1378c18df07a5ce1c12f37b54423e`  
**Branch:** `agent/canonical-seven-boundary-five-contact`  
**Status:** experimental source note.  The computation-free core in Sections
2--6 is incorporated, with corrected scope, in the
[promoted labelled-separator-shore theorem](../../../results/hc7_k7minus_strict_surplus_labelled_separator_shore.md).
Section 7 is an unpromoted fallback.  The final conversion of every returned
separator side into a seven-connected proper minor or a terminal minor model
is not proved here.  Thus this note does not prove the `4n-2` extremal target.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

---

## 1. Imported canonical setting

Let `G` be a counterexample of minimum order and then minimum size to

\[
 \kappa(G)\ge7,\qquad |E(G)|\ge4|V(G)|-2
 \quad\Longrightarrow\quad K_7^-\preccurlyeq G,
\]

and suppose

\[
 q:=|E(G)|-(4|V(G)|-2)\ge1.
\]

Fix a reserve-blind degree-seven vertex `x`, put

\[
 N=N_G(x),\qquad |N|=7,\qquad J=G-x,
\]

and assume `G[N]` contains no literal `K_4`.  For `y in N`, put

\[
 T_y=N-\{y\},\qquad B_y=V(G)-(T_y\cup\{x\}).
\]

The audited canonical six-boundary theorem gives all of the following.

1. `B_y` is connected and
   \[
   (G-xy)-T_y=\{x\}\mathbin{\dot\cup}B_y.
   \]
2. Every member of `T_y` has a neighbour in both displayed components.
3. `G[T_y]` is literal-`K_4`-free and `K_5^-`-minor-free, and
   \[
   |E(G[T_y])|\le10.
   \]
4. With
   \[
   \delta_y=|E(G[B_y])|+|E_G(B_y,T_y)|-4|B_y|,
   \]
   one has
   \[
   \delta_y=19+q-|E(G[T_y])|\ge9+q.
   \]
5. `(J,T_y)` is internally six-connected and
   \[
   |E(J)|=4|V(J)|-5+q.
   \]
6. `J` has a spanning `K_6`-minor model, but every `K_6` model in `J`
   has at most four branch sets meeting any fixed six-set `T_y`.

The source is
[`results/hc7_k7minus_strict_surplus_canonical_six_boundary.md`](../../../results/hc7_k7minus_strict_surplus_canonical_six_boundary.md).

The seven cuts are not independent instances: they all live in the same
graph `J`, and

\[
                         B_y=(V(G)-N[x])\cup\{y\}.
\]

The proof below uses that common realization.

---

## 2. All seven roots occupy at most four bags simultaneously

### Lemma 2.1 (simultaneous contact cap)

Let

\[
                         \mathcal M=(D_1,\ldots,D_6)
\]

be any spanning `K_6` model in `J`.  Then the seven vertices of `N` lie in
at most four bags of `\mathcal M`.

### Proof

Suppose `N` met at least five bags.  Since seven roots occupy at most six
bags, some bag contains at least two roots.  Choose one of them, say `y`.
After deleting `y`, that bag is still met by `T_y=N-{y}`.  Hence `T_y`
meets every bag of `\mathcal M` which was met by `N`, at least five bags.
This contradicts the imported four-contact bound for `T_y`. \(\square\)

Thus every spanning model has a multiply rooted bag.  No bipartite
reconstruction of an unrooted `K_6` is needed.

For the remainder of Sections 3--5, choose any spanning `K_6` model.  A branch
set is called **contacted** when it contains a member of `N`, and
**uncontacted** otherwise.  Lemma 2.1 says that at most four branch sets are
contacted.

---

## 3. Near-clique completion after a connected split

The following elementary use of the one-missing-edge allowance is the key
new observation.

### Lemma 3.1 (two rooted halves and the uncontacted-bag test)

Let `D` be one bag of a spanning `K_6` model, and let the other five bags be

\[
                         Q_1,\ldots,Q_5.
\]

Suppose

\[
                         D=A\mathbin{\dot\cup}B
\]

where `A,B` are nonempty connected sets, each contains a vertex of `N`, and
there is an `A-B` edge.  If every uncontacted foreign bag has an edge to
both `A` and `B`, then `G` contains a `K_7^-` minor.

### Proof

Classify each foreign bag as:

- `A`-only, when it meets `A` but not `B`;
- `B`-only, when it meets `B` but not `A`; or
- crossing, when it meets both.

By hypothesis every uncontacted bag is crossing.  Therefore every
`A`-only or `B`-only bag is contacted.  The whole model has at most four
contacted bags, one of which is `D`, so there are at most three exclusive
foreign bags in total.  Hence one of the two exclusive classes has order at
most one.

Suppose first that at most one foreign bag is `A`-only.  Use the seven
branch sets

\[
                         A\cup\{x\},\quad B,\quad
                         Q_1,\ldots,Q_5.                 \tag{3.1}
\]

The first set is connected because `A` contains a neighbour of `x`; it is
adjacent to `B` because `B` also contains a neighbour of `x`.  It is
adjacent to every foreign bag: an `A`-meeting bag supplies a literal edge,
while a `B`-only bag is contacted and hence has an edge to `x`.  The bag
`B` is adjacent to every foreign bag except possibly the unique `A`-only
bag.  The five foreign bags remain pairwise adjacent.  Thus (3.1) has at
most one missing adjacency and is a `K_7^-` model.

If instead the `B`-only class has order at most one, interchange `A,B` and
use `B\cup\{x\}`. \(\square\)

The statement is label-faithful: the two contacts with `x` are the literal
vertices of `N` contained in the two halves.

---

## 4. Two one-root connected sides in a multiply rooted branch set

### Lemma 4.1 (two disjoint one-root leaves)

Let `D` be connected and contain at least two vertices of `N`.  There are
disjoint connected sets `C_1,C_2 subseteq D` such that, for `i=1,2`,

\[
 |C_i\cap N|=1,
 \qquad D-C_i\text{ is connected}.                    \tag{4.1}
\]

### Proof

Take a spanning tree of `G[D]` and let `R` be its minimal subtree
containing all vertices of `D\cap N`.  Every leaf of `R` belongs to `N`.
Choose two distinct leaves.  For each chosen leaf, delete the first tree
edge on its route into `R`, and let `C_i` be the leaf-side tree component.
No other root lies in that component, the complementary tree component is
connected, and the two chosen leaf components are disjoint. \(\square\)

### Theorem 4.2 (five-contact model or strict labelled separator)

Under the canonical setting, at least one of the following holds.

1. `G` contains a `K_7^-` minor.
2. There are
   
   - a root `y in N`,
   - a connected set `C subsetneq B_y`, and
   - an uncontacted branch bag `U` of the fixed spanning `K_6` model,
   
   such that
   \[
   C\cap N=\{y\},\qquad D-C\text{ is connected},
   \qquad E_G(C,U)=\varnothing,                        \tag{4.2}
   \]
   where `D` is the multiply rooted model bag containing `C`.
   Consequently
   \[
   x\in N_G(C),\qquad N_G(x)\cap C=\{y\},             \tag{4.3}
   \]
   and `N_G(C)` is an actual vertex separator of order at least seven.

### Proof

By Lemma 2.1, some model bag `D` contains at least two roots.  Apply Lemma
4.1 and obtain `C_1,C_2`.

Suppose both `C_1` and `C_2` met every uncontacted foreign bag.  Consider
the connected bipartition

\[
                         D=C_1\mathbin{\dot\cup}(D-C_1).
\]

The second side contains `C_2`, so every uncontacted foreign bag meets both
sides.  Lemma 3.1 would give `K_7^-`, outcome 1.

Therefore one of `C_1,C_2`, call it `C`, misses an uncontacted foreign bag
`U`.  Let `y` be its unique root.  The bag `U` is connected, disjoint from
`C`, and anticomplete to it.  Hence deleting `N_G(C)` leaves `C` and `U`
on different sides, so `N_G(C)` is an actual separator.  Seven-connectivity
gives its order at least seven.

All vertices of `C-{y}` lie outside `N`, so `C subseteq B_y`.  The
uncontacted bag `U` contains no vertex of `N` and therefore lies in
`V(G)-N[x] subseteq B_y`; as `U` is disjoint from `C`, the containment is
strict.  Finally, `x` is adjacent to `y` and to no other vertex of `C`,
which proves (4.3). \(\square\)

This is the promised simultaneous use of all seven canonical boundaries.
The result is not a finite boundary list.  It converts every failure of the
five-contact model into one strict, literal, endpoint-labelled separator side
inside one of the original shores.

---

## 5. Exact coefficient-four accounting on the separator shore

For a connected set `C`, put

\[
 k(C)=|N_G(C)|,
 \qquad
 \eta(C)=|E(G[C])|+|E_G(C,N_G(C))|-4|C|.              \tag{5.1}
\]

When `C` is supplied by Theorem 4.2, call it a **labelled separator shore**.
It retains the original endpoint edge `xy`, has `C\cap N(x)={y}`, and is a
strict subset of `B_y`.

### Lemma 5.1 (the seven original shores are strongly high)

For every `y in N`,

\[
 k(B_y)=7,
 \qquad
 \eta(B_y)=\delta_y+1
            =20+q-|E(G[T_y])|\ge q+10.                \tag{5.2}
\]

### Proof

The boundary of `B_y` in `G` is `T_y\cup\{x\}`.  The only edge from `x`
to `B_y` is `xy`.  Thus (5.2) is the imported excess identity with that
one edge restored. \(\square\)

Such a separator shore is called **high** when

\[
                         \eta(C)>q+k(C)-4.              \tag{5.3}
\]

This is exactly the condition that contracting the whole cell cannot retain
the global `4n-2` density.

### Theorem 5.2 (high descent or density-preserving contraction)

Let `C` be the strict labelled separator shore from Theorem 4.2.  Then
exactly one of the following numerical alternatives holds.

1. `C` is high.  It is a strictly smaller coefficient-four high shore which
   retains the literal labels `x,y` and the unique edge from `x` into the
   shore.
2. `C` is density-eligible:
   \[
                         \eta(C)\le q+k(C)-4.           \tag{5.4}
   \]
   If `|C|>=2`, contract `C` onto the labelled vertex `y`, and call the
   resulting proper minor `G_C`.  Then
   \[
   |E(G_C)|-(4|V(G_C)|-2)
        =q+k(C)-4-\eta(C)\ge0.                         \tag{5.5}
   \]

### Proof

Only (5.5) needs verification.  Contracting `C` removes `|C|-1` vertices.
It replaces the

\[
 |E(G[C])|+|E_G(C,N_G(C))|
     =4|C|+\eta(C)
\]

edges internal to or leaving `C` by exactly `k(C)` edges from the new
labelled vertex `y` to `N_G(C)`.  Substituting
`|E(G)|=4|V(G)|-2+q` gives (5.5). \(\square\)

Thus the split never loses the coefficient-four bookkeeping.  It returns
either a strict labelled high-shore localisation or a proper
threshold-preserving contraction candidate.  The high shore is not known to
be another canonical six-boundary instance.

The only degenerate density-eligible separator shore is a singleton.  If
`C={y}`,
then

\[
                         \eta(C)=d_G(y)-4=k(C)-4,
\]

so (5.4) is always strict by the positive amount `q`, but contracting the
shore performs no operation.  Its boundary has order `d_G(y)>=7`; equality
is not known.  This is one of the residues recorded in Section 8.

---

## 6. What a failed eligible contraction returns

### Theorem 6.1 (label-preserving contraction-failure certificate)

Assume `|C|>=2` and (5.4).  If `G_C` is seven-connected, it is a smaller
counterexample and contradicts the choice of `G`.  Otherwise there are

\[
 Z\subseteq V(G)-C,\qquad |Z|\le5,                     \tag{6.1}
\]

and at least two components of

\[
                         G-C-Z                         \tag{6.2}
\]

such that every component `A` of (6.2) satisfies

\[
                         |N_G(A)\cap C|
                         \ge7-|Z|.                     \tag{6.3}
\]

Moreover, if two sides of (6.2) admit an `A-B` separator
`K subseteq C` of order exactly `7-|Z|` in `G-Z`, then

\[
                         Z\cup K                       \tag{6.4}
\]

is an actual order-seven cut of `G`.

### Proof

Let `c` be the vertex of `G_C` representing `C`, retaining the label `y`,
and choose a cut `X` of `G_C` of order at most six.  The vertex `c` belongs
to `X`: otherwise expanding it back to the connected set `C` cannot join
two components of `G_C-X`, and `X` would also be a cut of `G`.

Put `Z=X-{c}`.  Then `|Z|<=5`, and deleting `X` from the quotient leaves
exactly the graph in (6.2), so it is disconnected.

For a component `A` of (6.2), every neighbour outside `A` lies in
`C\cup Z`.  Seven-connectivity gives `|N_G(A)|>=7`, proving (6.3).

Finally, in `G-Z` the set `C` separates two different components `A,B` of
(6.2).  If `K subseteq C` is an `A-B` separator of order `7-|Z|`, then
`Z\cup K` separates the same sides in `G` and has order seven.
\(\square\)

Distinct order-seven cuts obtained in this way need not cross; they may be
nested.  If no separator `K` of the displayed order exists, an additional
capacitated linkage statement inside `C` would be needed.  Neither outcome
is terminal here.

---

## 7. A five-contact Hall theorem for a nonspanning core

The spanning split above is the primary argument.  The following secondary
lemma records the exact Hall deficit if one first shrinks to a nonspanning
`K_6` core in which every contacted bag contains exactly one root.

### Theorem 7.1 (five-contact augmentation or deficiency two)

Let `M=(M_1,\ldots,M_6)` be a `K_6` model in `J`, not necessarily spanning,
and suppose exactly `c<=4` bags are contacted, each by exactly one vertex
of `N`.  Put

\[
 u=6-c,
 \qquad R=N-\bigcup_iM_i,
 \qquad |R|=u+1.
\]

Run vertex-disjoint **root-clean model-avoiding paths** from distinct roots
in `R` to distinct uncontacted branch sets: apart from its initial root and
terminal vertex, each path avoids the model and every unused root.

Then either:

1. at least `u-1` uncontacted bags can be augmented, producing a `K_6`
   model with at least five contacted bags and hence a `K_7^-` model with
   `{x}`; or
2. after a maximum augmentation there remain `u'>=2` uncontacted bags and
   `u'+1` unused roots.  If `W` is the union of the components outside the
   augmented model which contain those unused roots, then
   \[
   S=\{x\}\cup P,
   \qquad P=N_J(W)\cap\bigcup_iM_i,                   \tag{7.1}
   \]
   is an actual separator, every member of `P` lies in a contacted bag,
   and
   \[
                         |P|\ge6.                      \tag{7.2}
   \]
   If the augmented model has `c'=6-u'` contacted bags and
   `P_i=P\cap M_i`, then
   \[
      \sum_{i:P_i\ne\varnothing}(|P_i|-1)
          \ge |P|-c'\ge u'\ge2.                       \tag{7.3}
   \]
   Thus a five-contact failure has at least two literal surplus portals,
   not merely the one-portal surplus of a full-contact Hall failure.

### Proof

If `u-1` paths exist, absorb each path into its terminal bag.  The old
`K_6` adjacencies remain, and the augmented bags contain distinct roots.
There are at least

\[
                         c+(u-1)=5
\]

contacted bags.  Adding `{x}` gives seven branch sets with at most the one
missing adjacency to the sole uncontacted bag.

Otherwise choose a maximum linkage of order `rho<=u-2` and absorb it.  The
new model has

\[
 u'=u-\rho\ge2,
 \qquad c'=c+\rho=6-u',
\]

and exactly `u'+1` roots remain outside it.  By maximality, in the graph
outside the augmented model no path runs from a remaining root to an
external portal of an uncontacted bag.

Let `W` be the union of the outside components containing those roots.
It is anticomplete to every uncontacted bag, and all its model neighbours
belong to contacted bags.  The set `{x}\cup W` is connected because every
component of `W` contains a neighbour of `x`.  Hence (7.1) separates it
from every uncontacted bag.  Seven-connectivity gives
`1+|P|>=7`, proving (7.2).  Since the portals occupy at most `c'` bags,
(7.3) follows. \(\square\)

Every component of `W` contains at least one root.  If one contains several,
a leaf-root tree split gives a strict one-root connected subset; if it
contains one, use the whole component.  This gives a labelled one-root
separator side anticomplete to every uncontacted branch set.  It need not
satisfy the donor-branch-set and connected-complement clauses of Theorem 4.2.

### Corollary 7.2 (the four-contact exact `K_7^vee` refinement)

In outcome 2 of Theorem 7.1, if `c'=4` and `u'=2`, then either `G` contains
`K_7^-`, or the seven sets

\[
             \{x\}\cup W,\quad
             M_1,M_2,M_3,M_4,\quad U_1,U_2             \tag{7.4}
\]

can be enlarged to a spanning exact `K_7^vee` model whose deficient centre
is `\{x\}\cup W`.  The audited exact-`K_7^vee` separator dichotomy then
returns an actual nested separator inside one of the four universal bags.

### Proof

The centre in (7.4) is connected, meets each contacted bag through its
literal root, and is anticomplete to the two uncontacted bags.  The six
foreign bags form a `K_6` model.

A component outside the seven displayed sets contains no remaining root
and is anticomplete to `W`; it is therefore anticomplete to the centre.
Assign it to any adjacent foreign bag.  Repeating gives a spanning model
without repairing either deficient centre adjacency.  If either adjacency
were repaired during this enlargement, only the other could remain absent,
and `K_7^-` would already be present.  Apply
[`results/hc7_k7minus_exact_k7vee_separator_dichotomy.md`](../../../results/hc7_k7minus_exact_k7vee_separator_dichotomy.md).
\(\square\)

This is a fallback normalization only.  The primary split theorem did not
need pair deletion, a bipartite reconstruction, or a finite portal census.

---

## 8. Exact endpoint and remaining obligation

The campaign proves the following unbounded theorem.

> **Five-contact model-or-labelled-shore theorem.**  For one reserve-blind
> degree-seven vertex `x`, every spanning `K_6` model in the common graph
> `G-x` either yields an explicit `K_7^-` model, or yields a root
> `y in N(x)` and a strict connected separator shore
> \[
> C\subsetneq B_y,
> \qquad C\cap N(x)=\{y\},
> \]
> whose literal neighbourhood is an actual separator, with `x` in that
> neighbourhood and `xy` the unique edge from `x` into the shore.
> The shore is either coefficient-four high, or its contraction onto `y`
> preserves the `4n-2` density.

This closes the model-splitting part requested in the attack.  It is
strictly stronger than saying that a multiply rooted bag is merely
"blocked": the obstruction is a literal same-host separator inside one of
the seven original canonical shores, and all density and endpoint labels
are retained exactly.

The full positive-surplus elimination would additionally require the
following final statement.

> **Remaining terminalisation theorem.**  Let `C` be a strict labelled
> separator shore supplied above.  If `C` is non-singleton and
> density-eligible, then the
> density-preserving contraction `G/C` is seven-connected, or the
> contraction-failure certificate in Theorem 6.1 produces `K_7^-`, a proper
> density-preserving seven-connected minor, or a strictly improved labelled
> separator shore.  A separate re-entry theorem is required for the high
> shore, and a singleton shore must first be shown to have degree seven or
> be replaced by an exact labelled order-seven cut.

Three residues prevent claiming this theorem here.

1. **High separator shore.**  A strict high `C` need not inherit the
   canonical six-boundary or spanning-model hypotheses, so strict containment
   alone does not permit iteration.
2. **Singleton separator shore.**  The strict shore may be `{y}`.  It is
   always density-eligible but has no proper whole-shore contraction, and
   `d_G(y)=7` is not known.
3. **Failed eligible contraction.**  An exact local separator supplies one
   order-seven cut, but it may be nested with the existing cuts.  If the
   exact local separator does not exist, the required label-preserving
   capacitated linkage statement is also open.

Pair deletion and two-root transfer were checked only as fallbacks.  They
reproduce the same portal-placement issue and do not remove these three
residues without an additional label-preserving co-connected split theorem.

Accordingly this note is substantial progress, but it is not a proof of the
strict-surplus layer or of the headline `4n-2` theorem.  The next accepted
step must close the three displayed residues; another finite boundary list
would not do so.
