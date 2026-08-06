# Labelled separator-shore terminalisation at a reserve-blind vertex

**Baseline:** `b5e69a700bb1378c18df07a5ce1c12f37b54423e`  
**Parent experiment:** `c5c54917175522c9157fee314a8beca5a2d237d0`  
**Status:** computation-free working theorem; not independently audited.

This note supersedes the provisional stopping point in
[`canonical_seven_boundary_five_contact_attack.md`](canonical_seven_boundary_five_contact_attack.md).
It proves the narrow model-or-terminalisation lemma requested there.  No
finite boundary enumeration is used.

The output is local rather than the full `4n-2` theorem.  A blocked split
now gives one of:

1. a literal `K_7^-` model;
2. a legal rerouting of the contact-maximal `K_6` model;
3. an exact labelled seven-cut;
4. a strict smaller labelled separator shore; or
5. a proper seven-connected minor which still meets the `4n-2` threshold.

The fifth outcome contradicts minimum order.  The only output which still
needs a separate global rank to finish the whole positive-surplus layer is
the strict smaller shore in item 4: it retains literal model and far-side
labels, but may be root-free and need not itself be one of the original
seven canonical one-root shores.

Throughout, `K_7^-` is `K_7` with one edge deleted.

---

## 1. Canonical setting and lexicographic choice

Let `G` be a counterexample of minimum order and then minimum size to

\[
 \kappa(G)\ge7,\qquad |E(G)|\ge4|V(G)|-2
 \quad\Longrightarrow\quad K_7^-\preccurlyeq G,
\]

and suppose

\[
 q:=|E(G)|-(4|V(G)|-2)\ge1.
\]

Fix a reserve-blind degree-seven vertex `x`, and put

\[
 N=N_G(x),\qquad |N|=7,\qquad J=G-x.
\]

Thus `G[N]` has no literal `K_4`.  The audited canonical six-boundary
theorem gives, for every `y in N`,

\[
 T_y=N-\{y\},
 \qquad B_y=V(G)-(T_y\cup\{x\}),
\]

where `B_y` is connected,

\[
 (G-xy)-T_y=\{x\}\mathbin{\dot\cup}B_y,
\]

both displayed components are full to `T_y`, and

\[
 |E(G[T_y])|\le10,
 \qquad
 \delta_{B_y}=19+q-|E(G[T_y])|\ge9+q.                 \tag{1.1}
\]

Moreover `(J,T_y)` is internally six-connected,

\[
 |E(J)|=4|V(J)|-5+q,                                   \tag{1.2}
\]

and `J` has a `K_6` model.  No `K_6` model in `J` has five bags meeting one
fixed `T_y`.

Call a `K_6` model in `J` **root-covering** when all seven vertices of `N`
lie in its branch sets.  A spanning model is root-covering.  Choose a
root-covering `K_6` model lexicographically as follows.

1. Maximise the number of bags meeting `N`.
2. Subject to that, choose a multiply rooted bag `D` of minimum order.

The simultaneous contact lemma in the parent experiment applies to every
root-covering model: the seven roots occupy at most four bags.  Hence `D`
exists, and at least two of the five foreign bags are uncontacted.

The parent split decoder gives either `K_7^-` or a nonempty connected set
`C subsetneq D`, a root `y in N`, and an uncontacted foreign bag `U` such
that

\[
 C\cap N=\{y\},\qquad D-C\text{ is connected},\qquad
 E(C,U)=\varnothing.                                    \tag{1.3}
\]

Choose `(C,U)` with `|C|` minimum after the model and `D` have been fixed.
The strict containment `C subsetneq B_y` is literal, because the nonempty
bag `U` lies in `B_y-C`.

---

## 2. Five safe edges at every reserve-blind vertex

Put

\[
                         H=G[N].                        \tag{2.1}
\]

### Theorem 2.1

One has

\[
                         |E(H)|\le13.                   \tag{2.2}
\]

### Proof

For every `v in N`, the six-vertex graph `H-v` has neither a literal
`K_4` nor a `K_5^-` minor.  The audited six-vertex boundary lemma therefore
gives

\[
                         |E(H-v)|\le10.                 \tag{2.3}
\]

Summing over the seven choices of `v` counts every edge five times, and
hence gives `|E(H)|<=14`.

Suppose equality holds.  Equation (2.3) gives `d_H(v)>=4` for every
vertex.  The degree sum is twenty-eight, so `H` is four-regular.  Its
complement is consequently a two-regular graph on seven vertices:

\[
                  \overline H\cong C_7
       \quad\text{or}\quad C_3\mathbin{\dot\cup}C_4.   \tag{2.4}
\]

In the first case label the complementary cycle cyclically by
`0,1,...,6`.  Delete `0` and contract the edge `25` of `H-0`.  Its ends
have no common neighbour in `H-0`, so the contraction leaves a five-vertex
nine-edge graph, namely `K_5^-`.

In the second case label the complementary triangle by `a,b,c` and the
complementary four-cycle cyclically by `d,e,f,g`.  Delete `d` and contract
`af`.  Again the contracted ends have no common neighbour and the quotient
is `K_5^-`.  Both alternatives contradict (2.3), proving (2.2).
\(\square\)

### Theorem 2.2

At most two vertices of `H` have degree at least five.

### Proof

Suppose `a,b,c` all have degree at least five and put
`W=V(H)-{a,b,c}`.  The three vertices cannot induce a triangle: each would
have at least three neighbours in the four-set `W`, so some member of `W`
would see all three and complete a `K_4`.  They cannot induce at most one
edge either, because one of them would then have degree at most four.
Thus they induce the path

\[
                         a-b-c.                         \tag{2.5}
\]

The endpoints `a,c` are complete to `W`, while `b` has at least three
neighbours there.  The graph `H[W]` is triangle-free, since a triangle with
`a` would be a `K_4`; and the neighbours of `b` in `W` are independent,
since an edge between two of them with `a,b` would again make a `K_4`.

The path, the eight endpoint-to-`W` edges, and the at least three
`b-W` edges already account for thirteen edges.  Theorem 2.1 forces
equality throughout: `H[W]` is edgeless and `b` has exactly three
neighbours in `W`.  The fourth member `w` of `W` has degree two, so
`H-w` has eleven edges, contrary to (2.3).  \(square\)

### Corollary 2.3

At least five vertices `s in N` satisfy

\[
 |N_G(x)\cap N_G(s)|=d_H(s)\le q+3.                   \tag{2.6}
\]

Thus at least five incident edges `xs` are density-safe, and every one of
their failed contractions supplies an exact order-seven cut containing the
literal labels `x,s`.

### Proof

For `q>=3`, every boundary degree is at most six.  For `q=2`, only degree
six is unsafe; for `q=1`, an unsafe vertex has degree at least five.
Theorem 2.2 leaves at most two unsafe vertices.  The contraction identity

\[
 q(G/xs)=q+3-|N(x)\cap N(s)|
\]

then preserves the threshold.  Minimum order makes the quotient
non-seven-connected, and the standard pullback of a minimum cut gives the
exact labelled seven-cut.  \(square\)

This closes the first singleton obligation at the correct level.  If
`C={y}` and `d_G(y)=7`, then `N_G(y)` itself is an exact seven-cut.  If
`D-y` is connected and `y` owns at most one foreign duty, deleting or
moving `y` is a valid root exchange.  In every remaining singleton case,
Corollary 2.3 still supplies at least five exact labelled safe-edge cuts in
the same seven-root family.  No finite boundary classification is needed.

---

## 3. High cells and density-eligible cells

For a connected set `P`, put

\[
 k(P)=|N_G(P)|,
 \qquad
 \eta(P)=|E(G[P])|+|E_G(P,N_G(P))|-4|P|.              \tag{3.1}
\]

The original canonical shore satisfies

\[
 k(B_y)=7,
 \qquad
 \eta(B_y)=20+q-|E(G[T_y])|\ge q+10.                  \tag{3.2}
\]

Call `P` **high** when

\[
                         \eta(P)>q+k(P)-4.              \tag{3.3}
\]

If the selected `C` is high, it is already the requested strict smaller
coefficient-four shore, with the original endpoint labels `x,y` and the
unique edge `xy` from `x` into the shore.

Assume henceforth that `C` is density-eligible:

\[
                         \eta(C)\le q+k(C)-4.           \tag{3.4}
\]

When `|C|>=2`, contract `C` onto its labelled root `y`, and denote the
proper minor by `G_C`.  Exact accounting gives

\[
 |E(G_C)|-(4|V(G_C)|-2)
     =q+k(C)-4-\eta(C)\ge0.                            \tag{3.5}
\]

If `G_C` is seven-connected, it contradicts the minimum order of `G`.
Suppose it is not.

Choose a minimum cut of `G_C`.  It contains the contracted vertex `c`,
so write it as

\[
                         \{c\}\cup Z,\qquad |Z|\le5.   \tag{3.6}
\]

Let `A,B` be two components of `G-C-Z`, put

\[
 X_A=N_C(A),\qquad X_B=N_C(B),\qquad p=7-|Z|,          \tag{3.7}
\]

and let `lambda(A,B)` be the minimum order of an `X_A-X_B` separator
contained in `C`, where separator vertices may belong to the terminal
sets.  Seven-connectivity gives

\[
                         \lambda(A,B)\ge p.             \tag{3.8}
\]

Indeed, a smaller separator `K subseteq C` would make `Z union K` a cut
of `G` of order at most six.  Equality in (3.8) gives immediately the
exact labelled seven-cut

\[
                         Z\cup K.                       \tag{3.9}
\]

The issue is therefore the portal-rich case `lambda>p`.

---

## 4. The six-cut quotient is impossible

The next theorem removes the only case in which `lambda>p` need not give
four disjoint traversals.

### Theorem 4.1

The graph `G_C` has no vertex cut of order six.

### Proof

Suppose `X` is a minimum six-cut, and let

\[
                         A_1,\ldots,A_r
\]

be the components of `G_C-X`.  Six-connectivity makes every component full
to `X`.

#### Component count

If `r>=5`, use five components: absorb four distinct boundary vertices
into four components, retain the fifth component as a bare bag, and keep
the other two boundary vertices as singleton bags.  These seven bags form
`K_7^-`.

If `r=4`, the analogous construction with four components shows that every
three boundary vertices span at most one edge; hence `Delta(G_C[X])<=1`.
But every boundary vertex has four neighbours in the four components and
minimum degree at least six, so it has at least two neighbours in `X`, a
contradiction.  Thus

\[
                         2\le r\le3.                    \tag{4.1}
\]

For a component `A_i`, define

\[
 \delta_i=|E(G_C[A_i])|+|E_{G_C}(A_i,X)|-4|A_i|.       \tag{4.2}
\]

If `q_C=|E(G_C)|-(4|V(G_C)|-2)`, exact accounting gives

\[
                         q_C=|E(G_C[X])|+
                              \sum_i\delta_i-22.        \tag{4.3}
\]

#### Two components

Suppose `r=2`.  Each boundary vertex has at least two outside neighbours,
so `delta(G_C[X])>=4`.  Leaving any prescribed five vertices of `X` as
singletons and using the two full components shows that every five-set
spans at most eight edges.  Summing over the six five-sets gives

\[
                         |E(G_C[X])|\le12.
\]

Thus equality holds and

\[
                         G_C[X]\cong K_6-3K_2.          \tag{4.4}
\]

Let `A` be either component.  For one of the three missing pairs
`{p,q}`, put `Q=X-{p,q}`; then `G_C[Q]=C_4`.  The rooted pair
`(G_C[A\cup Q],Q)` is internally four-connected.  It has no `Q`-rooted
`K_4` model: such a model together with the other full component and the
singletons `p,q` would be `K_7^-`, with only `pq` absent.

Norin--Totschnig Lemma 9 therefore gives

\[
 p_A(p)+p_A(q)\ge |A|+\delta_A-1,                     \tag{4.5}
\]

where `p_A(t)=|E(t,A)|`.  Summing (4.5) over the three missing pairs counts
all `A-X` edges once.  Connectedness of `A` also gives

\[
 |E(A,X)|=4|A|+\delta_A-|E(A)|
              \le3|A|+\delta_A+1.
\]

Consequently `delta_A<=2`.  The same holds for the other component, whereas
(4.3)--(4.4) require

\[
                         \delta_1+\delta_2=10+q_C,
\]

a contradiction.

#### Three components

Suppose `r=3`.  Every boundary vertex has at least three outside
neighbours, so `|E(G_C[X])|>=9`.  The standard three-component construction
shows that every four-set of `X` spans at most four edges, and hence
`|E(G_C[X])|<=10`.

The three components cannot all be singletons: then `|V(G_C)|=9` and
`|E(G_C)|<=28<4\cdot9-2`.  Thus one is nontrivial.  If a boundary vertex
had four boundary neighbours, a rooted `K_4^-` in a nontrivial component,
the other two full components, and that boundary singleton would form
`K_7^-`.  Hence `Delta(G_C[X])<=3`.  It follows that `G_C[X]` is cubic and
has nine edges.

Fix a component `A`, an ordered boundary nonedge `(q,p)`, and put
`Q=X-{q,p}`.  As above, `(G_C[A\cup Q],Q)` is internally four-connected.
It has no `Q`-rooted `K_4`: combine such a model with

\[
       A_j\cup\{p\},\qquad A_k,\qquad\{q\},
\]

where `A_j,A_k` are the other components.  The cubic boundary makes `q`
adjacent to three of the four roots, so at most one adjacency is missing.

Summing the resulting Lemma 9 inequalities over the twelve ordered
nonedges gives

\[
              3|E(A)|+2|E(A,X)|\le9|A|+6.             \tag{4.6}
\]

Connectedness then yields `delta_A<=3`.  The same holds for all three
components, whereas (4.3) requires

\[
                         \sum_i\delta_i=13+q_C.
\]

This is again impossible.  The six-cut is eliminated.  \(square\)

The theorem is density-sensitive.  Contact geometry alone admits static
six-boundary obstructions; the contradiction uses the exact coefficient
four on every component.

---

## 5. Portal-rich smaller cuts: reroute or strict shore

By Theorem 4.1 the minimum cut in (3.6) has order at most five.  Hence

\[
                         p=7-|Z|\ge3.                   \tag{5.1}
\]

Suppose `lambda>p`.  Menger's theorem gives at least four pairwise
disjoint connected `X_A-X_B` paths

\[
                         P_1,\ldots,P_\lambda\subseteq C. \tag{5.2}
\]

At most one contains the unique root `y`, so at least three are root-free.
For a connected set `P subseteq D`, let

\[
 \Omega(P)=\{R:R\text{ is a foreign bag and every }D-R
                         \text{ edge has its }D\text{-end in }P\}. \tag{5.3}
\]

The ownership sets of disjoint paths are disjoint.  The uncontacted bag
`U` belongs to none of them, because `C` is anticomplete to `U`.  Thus
three root-free paths have disjoint ownership sets inside a four-label
set.  One of them, call it `P`, satisfies

\[
                         |\Omega(P)|\le1.               \tag{5.4}
\]

The set `P` is a proper subset of `C`, since it is root-free while
`C\cap N={y}`.

### Lemma 5.1

If `D-P` is connected, the contact-maximal model has a legal rerouting to
a model with the same contact count and a strictly smaller multiply rooted
bag.

### Proof

If `Omega(P)` is empty, replace `D` by `D-P`.  Every foreign duty survives,
all seven roots remain covered, and the residual bag remains multiply
rooted.

If `Omega(P)={R}`, replace

\[
                         D\mapsto D-P,
             \qquad     R\mapsto R\cup P.             \tag{5.5}
\]

The target is connected through an actual `P-R` edge; the cut edge from
`P` to `D-P` restores the donor-target adjacency; and every other donor
duty survives.  No root moves, so the contact count is unchanged.

Both operations contradict the lexicographic choice of `D`.  \(square\)

### Lemma 5.2

If `D-P` is disconnected, then `P` is a strict smaller labelled separator
shore.

### Proof

The set `P` is connected and anticomplete to the nonempty foreign bag `U`.
Thus `N_G(P)` is an actual separator, with `P` on one side and `U` on a far
side.  The path has literal neighbours in both named quotient components
`A,B`, and (5.4) retains at most one owned foreign duty.  Finally
`P subsetneq C`, proving strict descent in order.  \(square\)

Combining the two lemmas, the portal-rich case gives a forbidden model
rerouting or the requested strict smaller labelled shore.  If no strict
shore output is allowed, `lambda>p` is impossible and equality in (3.8)
produces the exact seven-cut (3.9).

---

## 6. Main local terminalisation theorem

### Theorem 6.1

In the canonical reserve-blind setting, one of the following holds.

1. `G` contains a `K_7^-` minor.
2. The selected blocker `C` is a strict endpoint-labelled high shore:
   \[
      C subsetneq B_y,\qquad
      \eta(C)>q+k(C)-4.
   \]
3. A legal branch-set transfer preserves the maximum contact number and
   strictly decreases the selected multiply rooted bag.
4. There is an actual exact order-seven cut carrying the named labels of
   the failed contraction.
5. There is a connected labelled separator shore `P` with
   \[
      |P|<|C|,\qquad E(P,U)=\varnothing,\qquad
      P\sim A,B,\qquad |\Omega(P)|\le1.
   \]
6. Contracting `C` gives a proper seven-connected minor satisfying
   \[
      |E(G_C)|\ge4|V(G_C)|-2.
   \]

Outcome 6 contradicts the choice of `G`, and outcome 3 contradicts the
lexicographic model choice.

### Proof

The parent split decoder gives outcome 1 or the blocker (1.3).  Apply the
high/eligible dichotomy of Section 3.  A high blocker gives outcome 2.  An
eligible nonsingleton blocker gives the threshold-preserving contraction.
If the quotient is seven-connected, outcome 6 holds.  Otherwise Theorem
4.1 excludes a six-cut.  For a smaller quotient cut, equality in (3.8)
gives outcome 4, while strict inequality invokes Lemmas 5.1--5.2 and gives
outcome 3 or 5.  The singleton case is covered by Corollary 2.3 and the
root exchanges following it.  \(square\)

This is the narrow terminalisation requested after the parent experiment.
It does not reconstruct an unrooted `K_6`; that model was present from the
start.  Pair deletion and two-root transfer machinery are not used.

---

## 7. Optional high-surplus root-swap strengthening

When `q>=3`, every edge incident with `x` is density-safe.  In that layer,
Yuan's locally-critical fragment theorem gives a second computation-free
output.

There are a root `t in N`, a six-set `Q`, and a component `F` of `J-Q`
such that

\[
                         F\cap N=\{t\},\qquad N_J(F)=Q. \tag{7.1}
\]

Thus `Q union {x}` is an exact seven-cut.  If `F={t}`, then `d_G(t)=7`.
Otherwise every component `K` of `F-t` has

\[
                         N_G(K)=Q\cup\{t\},            \tag{7.2}
\]

and there are at most two such components.  Hence `Q union {t}` is a
second exact seven-cut and each `K` is strictly smaller than `F`.

The proof is the standard six-connected, locally one-critical argument:
failed safe contractions give `kappa(J-s)=5` for every `s in N`; every
fragment of `J` and of `J-s` meets the surviving root set; Yuan supplies
four fragments with disjoint root traces; and one trace is a singleton
because `|N|=7`.

---

## 8. Exact scope

The local model-contraction programme is now terminal in the sense requested:
there is no residual six-cut, no uncontrolled portal-rich contraction
failure, and no need for another finite boundary list.

The theorem does **not** by itself prove that `q(G)>0` is impossible.  To
turn outcome 5 into a contradiction one must choose a global well-founded
rank over the enlarged family of labelled separator shores.  The returned
shore retains:

- its two named contraction sides `A,B`;
- the missed uncontacted model bag `U`;
- at most one owned foreign duty; and
- a strict order decrease.

It need not contain the original root `y`, so a rank restricted only to the
seven original canonical one-root shores is too narrow.  The correct final
global statement is therefore:

> minimise order over the closure of the canonical one-root shores under
> the labelled path-shore handoff in outcome 5; prove that a root-free
> minimum either has coefficient-four high excess, admits a proper
> density-preserving contraction, or can be absorbed by the same one-owner
> transfer.

That is a single unbounded rank theorem, not a boundary enumeration.  Until
it is proved and independently audited, the headline `4n-2` theorem remains
open.

## Dependencies

The direct repository inputs are:

- `results/hc7_k7minus_strict_surplus_canonical_six_boundary.md`;
- `results/hc7_k7minus_strict_surplus_minimal_enemy.md`;
- `results/hc7_k7minus_degree7_safe_contraction.md`;
- `results/hc7_k7minus_seven_cut_three_component_bound.md`;
- `active/hc7_k7minus_degree6_cut_capacity_excess.md`;
- Norin--Totschnig Lemma 9 for the rooted `K_4` density bound.

Section 7 additionally uses Yuan's fragment theorem in the same form
already audited in the repository's degree-seven atom work.