# Pair deletion at degree-eight centres and a spanning `K_7^\vee` model

**Status:** written nonterminal reduction; separately internally audited in
[`hc7_k7minus_pair_deletion_k7vee_reduction_audit.md`](hc7_k7minus_pair_deletion_k7vee_reduction_audit.md).
This note records the two-root consequence of the disconnected
exceptional-centre branch, the corresponding one-root reduction available
at every exceptional centre, and the exact target interface forced by a
spanning-`K_6` model's optimality.  It does not construct a `K_7^-` minor,
produce a six-colouring, or prove exceptional anti-neighbourhood
connectivity.

## 1. Setting

Let `G` satisfy

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G.                         \tag{H}
\]

Under (H), the audited global bounds are `|E(G)|>=4|V(G)|-2` and
`b>=17+tau`, where `b` counts exceptional vertices.  Section 4 uses only
this global setting.

For Sections 2--3, assume additionally that some exceptional degree-eight
vertex has disconnected anti-neighbourhood.  The audited two-component
theorem then gives

\[
 \delta(G)\ge8,
 \qquad |E(G)|\ge4|V(G)|,
 \qquad n_8\ge25+\tau,                               \tag{1}
\]

where

\[
                  \tau=\sum_{i\ge10}(i-9)n_i.
\]

In this branch `G` contains no literal `K_5`, and every degree-eight vertex
is exceptional.

## 2. The pair-deletion reduction

### Theorem 1 (a spanning near-clique model after deleting two centres)

Let `a,b` be any two distinct degree-eight vertices of `G`, and put
`H=G-{a,b}`.  Then `H` is five-connected and contains a spanning
`K_7^\vee`-minor model.  Label its branch sets

\[
                         P,B,C,U_1,U_2,U_3,U_4,        \tag{2}
\]

so that the two missing adjacencies of `K_7^\vee` are `PB` and `PC`.
For each retained root `r\in\{a,b\}`:

1. `r` is adjacent to at most four of the six branch sets
   `B,C,U_1,U_2,U_3,U_4`;
2. if `r` is adjacent to `P`, then it is adjacent to neither `B` nor `C`;
3. `a` and `b` cannot both be adjacent to all five branch sets
   `P,U_1,U_2,U_3,U_4`.

Here a vertex is adjacent to a branch set when it has a neighbour in that
set.

#### Proof

Deleting two vertices from a seven-connected graph leaves a
five-connected graph.  Writing `n=|V(G)|` and `m=|E(G)|`, exact edge
accounting gives

\[
 \begin{aligned}
 |E(H)|
   &=m-d_G(a)-d_G(b)+\mathbf 1_{ab\in E(G)}\\
   &=m-16+\mathbf 1_{ab\in E(G)}\\
   &\ge4n-16+\mathbf 1_{ab\in E(G)}\\
   &=4|V(H)|-8+\mathbf 1_{ab\in E(G)}.                \tag{3}
 \end{aligned}
\]

Norin--Totschnig's extremal theorem therefore gives a `K_7^\vee` minor in
`H`, unless `H\cong K_{2,2,2,2}`.  Equation (1) gives `n\ge25`, whereas
`|V(H)|=n-2\ge23` and `K_{2,2,2,2}` has eight vertices, so the exception
is impossible.

Enlarge the seven branch sets to a partition of `V(H)` by assigning every
component outside their union to an adjacent branch set.  This preserves
connectedness and all required model adjacencies.  Since `G` has no
`K_7^-` minor, the pairs `PB` and `PC` remain nonadjacent: either additional
adjacency would make the seven branch sets contain a `K_7^-` model.

The six branch sets

\[
                         B,C,U_1,U_2,U_3,U_4           \tag{4}
\]

are pairwise adjacent.  If `r` met at least five of them, these six sets
together with the singleton branch set `\{r\}` would have at most one
missing adjacency, giving a `K_7^-` model.  This proves item 1.

Suppose next that `r` meets both `P` and `B`.  Absorb `r` into `P`.  The
enlarged branch set is connected and now adjacent to `B`; among the seven
sets in (2), only its adjacency to `C` may be absent.  This is again a
`K_7^-` model.  The same argument with `B,C` interchanged proves item 2.

Finally assume that both roots meet `P,U_1,U_2,U_3,U_4`.  Then

\[
             \{a\},\{b\},P,U_1,U_2,U_3,U_4            \tag{5}
\]

are seven pairwise adjacent branch sets except possibly for the single
pair `\{a\},\{b\}`.  They contain a `K_7^-` model, proving item 3.
\(\square\)

## 3. Spanning `K_6` normalization

### Proposition 2 (absorbing the deficient branch set)

For every `h\in\{1,2,3,4\}`, replacing `P,U_h` by

\[
                         \widehat U_h=P\cup U_h          \tag{6}
\]

turns (2) into a spanning `K_6`-minor model

\[
              B,C,U_1,\ldots,\widehat U_h,\ldots,U_4.   \tag{7}
\]

Every retained root `r in {a,b}` is adjacent to at most four branch sets
of every spanning `K_6` model in `H`.

#### Proof

The old `P-U_h` edge makes `\widehat U_h` connected.  The set `U_h`
retains edges from it to `B,C` and the other three universal branch sets,
so the six sets in (7) are connected, disjoint, spanning and pairwise
adjacent.

More generally, if a retained root met at least five branch sets of any
spanning `K_6` model in `H`, those six sets together with `{r}` would have
at most one missing adjacency.  They would be a `K_7^-`-minor model,
contrary to (H).  \(\square\)

The generic connected/co-connected branch-set move needed below is already
the audited one-admissible transfer: a connected part may move from a donor
to an uncontacted target when the donor complement is connected and retains
its four protected branch-set adjacencies.  The cut edge between the two
donor parts restores the donor--target adjacency.  Increasing contact with
one fixed root is its immediate one-root corollary.  The next theorem is the
new consequence of choosing this move globally optimally, rather than a new
transfer lemma.

Fix one retained root `r`.  For a spanning `K_6` model `Q`, let `nu_r(Q)`
be the number of its branch sets adjacent to `r`.  First maximize
`nu_r(Q)`.  Subject to that maximum, choose a pair `(Q,D)` for which `D`
contains at least two neighbours of `r` and `|D|` is minimum.  Such a donor
exists: `r` has \(8-\mathbf 1_{ab\in E(G)}\) neighbours in `H`, all
lying in at most four branch sets.

Let `T` be an uncontacted branch set of `Q`, and name the other four branch
sets besides `D,T` by `R_1,...,R_4`.  Put

\[
 A_D(T)=\{v\in D:E_G(\{v\},T)\ne\varnothing\}.          \tag{8}
\]

A **`T`-retaining core** is a connected set `Y subseteq D` which contains
a neighbour of `r` and has an edge to every `R_i`.

### Theorem 3 (forced target interface)

For every uncontacted target `T` and every `T`-retaining core `Y`,

\[
                         A_D(T)\subseteq Y.              \tag{9}
\]

Consequently every vertex of `A_D(T)` is either a cutvertex of `G[D]` or
is the unique `D`-endpoint of the edges from `D` to at least one protected
branch set `R_i`.  In particular, all but at most four vertices of
`A_D(T)` are cutvertices of `G[D]`.

#### Proof

Suppose `v in A_D(T)-Y`, and let `C` be the component of `G[D-Y]`
containing `v`.  The sets `C` and `D-C` are connected: every component of
`D-Y` has an edge to the connected set `Y`.  The set `C` meets `T`, while
`D-C` contains a neighbour of `r` and retains an edge to every protected
branch set through `Y`.

Move `C` from `D` to `T`.  The resulting two branch sets are connected,
and an edge from `C` to `Y` restores their mutual adjacency.  All other
`K_6` adjacencies are retained.  If `C` contains a neighbour of `r`, the
move increases `nu_r`, contradicting its maximality.  If `C` is root-free,
the contact count is unchanged and `D-C` retains all the root neighbours
of `D`, hence at least two; it is a smaller eligible donor, contradicting
the choice of `(Q,D)`.  This proves (9).

For a protected branch set `R_i`, write
`N_D(R_i)=N_G(R_i)\cap D`.  Now take `v\in A_D(T)`.  If `D-v` is connected,
it still contains a neighbour of `r`, because `D` contains at least two.
Unless some protected portal set `N_D(R_i)` equals `{v}`, the set `D-v` is
a `T`-retaining core which omits `v`, contradicting (9).  Distinct
non-cutvertices of `A_D(T)` require distinct protected singleton portal
sets, so there are at most four.  \(\square\)

This theorem identifies the remaining obstruction as a possibly long
cutvertex interface.  It does not bound `|A_D(T)|`, split that interface,
or attach its vertices to prescribed recipient labels.

## 4. Global one-centre extension

### Theorem 4 (a spanning near-clique and forced interface at every exceptional centre)

Let `r` be any exceptional vertex of `G`, and put `J=G-r`.  Then `J`
contains a spanning `K_7^\vee`-minor model and a spanning `K_6`-minor
model.  In every spanning `K_6` model of `J`, `r` is adjacent to at most
four branch sets.  After maximizing that contact number over all spanning
`K_6` models and globally minimizing an eligible branch set `D` containing
at least two neighbours of `r`, the forced-interface conclusion (9) and
its cutvertex consequence hold for every uncontacted target `T`.

#### Proof

The global audited density and exceptional-count bounds give

\[
 |E(G)|\ge4|V(G)|-2,\qquad b\ge17.                    \tag{10}
\]

Hence `J` is six-connected and

\[
 |E(J)|=|E(G)|-8\ge4|V(J)|-6>4|V(J)|-8.              \tag{11}
\]

Norin--Totschnig's theorem supplies a `K_7^\vee` model.  Its exceptional
graph `K_{2,2,2,2}` is impossible because `|V(J)|\ge16`.  Enlarge the model
to span `J` as in Theorem 1; target exclusion ensures that both nominally
missing adjacencies remain absent.  Absorbing the deficient branch set into
any universal branch set gives a spanning `K_6` model.

If `r` met five branch sets of any spanning `K_6` model, those six sets and
`{r}` would form a `K_7^-` model.  Its eight neighbours therefore occupy at
most four bags, so an eligible donor exists.  The proof of Theorem 3 uses
only the spanning `K_6` model, the fixed root, and the stated global
optimization; it applies verbatim in `J`.  \(\square\)

The globally optimized `K_6` model need not be one of the four models
obtained from a selected `K_7^\vee` model.  Thus this theorem does not align
the optimized donor and target with the deficient labels `P,B,C`.

### Proposition 5 (exact contact counts after labelled absorption)

Fix one exact spanning model

\[
                         P,B,C,U_1,U_2,U_3,U_4
\]

in `G-r`.  Let `p` be one or zero according as `r` is adjacent to `P`, and
let `k` be the number of branch sets adjacent to `r` among

\[
                         B,C,U_1,U_2,U_3,U_4.
\]

For the spanning `K_6` model obtained by replacing `P,U_h` with
`P union U_h`, let `q_h` be its number of branch sets adjacent to `r`.
Then

\[
 q_h=
 \begin{cases}
 k,&p=0,\\
 k,&p=1\text{ and }r\text{ is adjacent to }U_h,\\
 k+1,&p=1\text{ and }r\text{ is not adjacent to }U_h.
 \end{cases}                                             \tag{A1}
\]

Consequently one of the four labelled absorptions attains the universal
four-contact upper bound precisely when

\[
                  (p=0\text{ and }k=4)
          \quad\text{or}\quad
                  (p=1\text{ and }k\ge3).               \tag{A2}
\]

The cases not forced to attain that bound are exactly

\[
                  p=0, k\le3,
          \qquad\text{or}\qquad
                  p=1, k\le2.                          \tag{A3}
\]

#### Proof

If `r` misses `P`, absorbing `P` into `U_h` neither gains nor loses a
contact: the fused branch set is contacted exactly when `U_h` was.  This
gives the first row of (A1).  If `r` meets `P`, the fused branch set is
always contacted, so the absorption gains one contact exactly when `U_h`
was missed.  This gives the other two rows.

Target exclusion bounds `k` by four.  Moreover, when `p=1`, the root misses
`B,C`, so the `k` contacted branch sets are among the four `U_i`.  Thus
`k=3` leaves a missed `U_h` whose absorption has contact four, while `k=4`
gives contact four for every choice.  The remaining assertions follow
from (A1).  \(\square\)

Attaining contact four resolves only the contact-number comparison: that
absorbed model is then contact-maximal among all spanning `K_6` models.
It does not justify donor minimization inside the four labelled
absorptions.  A valid `K_6` transfer may retain adjacency to the fused set
`P union U_h` while losing the separate portal to `P` or to `U_h` needed
to recover the seven labelled branch sets.

There is one immediate safe transfer class.  If the donor is `B` or `C`,
then it is anticomplete to `P`; hence every retained donor contact with
`P union U_h` uses `U_h`, and unabsorbing preserves the labelled
`K_7^\vee` refinement.  For a universal donor, the argument can fail when
the moved part contains every edge from the residual donor to `P` or to
`U_h`.  A transfer from the fused donor may additionally leave no connected
nonempty refinement of its original `P` or `U_h` part.  Neither criticality
nor target exclusion has yet eliminated these cases.

## 5. One named colouring operation and its exact limit

Choose \(x\in N(r)\cap D\) and fix one six-colouring `phi` of the proper
minor `G-rx`.  Necessarily

\[
                         \phi(r)=\phi(x)=\alpha.         \tag{12}
\]

For every other colour `beta`, the `alpha,beta` component containing `x`
also contains `r`.  Otherwise swapping those two colours in the component
of `x` would make the deleted edge proper and six-colour `G`.  Hence a
shortest path in that component from `x` to `r`, with its final vertex
deleted, gives an `alpha,beta` path in `G-r` from `x` to a
`beta`-coloured neighbour of `r`.  The five endpoints are distinct, and
all five paths arise from this one named edge-deletion colouring.

Their five first edges at `x` are distinct.  Since `G-r` is
six-connected, the audited prescribed-spoke theorem can extend those
five edges to a fan ending at any prescribed five-set.  In particular,
after choosing one literal vertex from an uncontacted target `T` and from
each protected branch set `R_1,...,R_4`, there is a fan sharing only `x`
and ending once in every named branch set.  This retains the five first
edges generated by one operation and five named **ends**, but not five named
**first hits**: a path assigned to one end may traverse another branch set
first.

### Proposition 6 (two-hole persistence and a deficient-bag response)

Under (H), let `r` be exceptional and fix an exact spanning labelled
`K_7^\vee` model

\[
                         P,B,C,U_1,U_2,U_3,U_4
\]

in `G-r`, with missing pairs `PB,PC`.  Let `D` be a branch set adjacent to
`r`.  Add `r` to `D`, and among all spanning models with the same labels
and `r` in the `D`-bag choose one whose `D`-bag `R` has minimum order.

Target exclusion makes every such model exact: an edge across either
nominal missing pair would already give a `K_7^-` model.  In particular,
`r` has no neighbour in a foreign bag whose label is not adjacent to `D`.
Put

\[
 m=d_{K_7^\vee}(D)=
 \begin{cases}
 4,&D=P,\\
 5,&D\in\{B,C\},\\
 6,&D\in\{U_1,U_2,U_3,U_4\}.
 \end{cases}                                             \tag{B1}
\]

At least `9-m` edges incident with `r` are individually
deletion-persistent for this same labelled model.  Two such edges in
different support classes are jointly persistent, and the pairs which are
not jointly persistent form a matching.

Let `rho` be the number of persistent incident edges and let `S` be their
other endpoints.  If every jointly persistent pair has adjacent endpoints,
then the `K_4`-free condition on `G[N(r)]` gives

\[
 \begin{array}{c|c}
 \rho& G[S]\\ \hline
 5&K_5-2K_2,\\
 6&K_6-3K_2,
 \end{array}                                             \tag{B2}
\]

and `rho>=7` is impossible.

If `D=P`, there are jointly persistent edges `rx,ry` with `xy` absent.
One six-colouring `c` obtained by contracting both edges satisfies, when
pulled back to `G-{rx,ry}`,

\[
 c(r)=c(x)=c(y),\qquad
 N(r)\cap c^{-1}(c(r))=\{x,y\},                         \tag{B3}
\]

and all five other colours occur on `N(r)-{x,y}`.  The same spanning
labelled `K_7^\vee` model survives in this one response.

#### Proof

Write `Gamma(D)` for the `m` labels required to be adjacent to `D`.  Let
`Z_1,...,Z_h` be the components of `G[R]-r`, and let `k_0,k_1` count those
with respectively one and at least two edges to `r`.  For such a component
put

\[
 \Lambda(Z_i)=\{X\in\Gamma(D):
        \varnothing\ne N_G(B_X)\cap R\subseteq Z_i\}.
\]

The sets `Lambda(Z_i)` are pairwise disjoint and each has order at least
two.  Indeed, if one has order zero, seven-connectivity gives an edge from
`Z_i` to a foreign branch set.  Moving `Z_i` to that branch set either
gives a smaller rooted model or fills one of `PB,PC`, producing a
`K_7^-` model.  If `Lambda(Z_i)={X}`, moving `Z_i` to `B_X` and using an
`r-Z_i` edge to restore the `D-B_X` adjacency has the same two outcomes.
Both contradict the choice of `R` or (H).

Let `ell` count nonpersistent edges from `r` to foreign branch sets, let
`q` count required labels receiving a persistent external edge, and let
`rho` count all persistent incident edges.  The sets `Lambda(Z_i)`, the
`ell` private labels and these `q` labels are disjoint.  Spanning and the
degree of `r` give

\[
 2(k_0+k_1)+\ell+q\le m,
 \qquad 8=k_0+\ell+\rho.                                \tag{B4}
\]

If `sigma=m-(2(k_0+k_1)+ell+q)`, then

\[
 \rho=8-m+k_0+2k_1+q+\sigma\ge9-m.                     \tag{B5}
\]

The last inequality follows because `rho=0` would give `8<=m`, while any
persistent edge makes `k_1>0` or `q>0`.  Grouping persistent edges by their
component of `R-r` or their foreign label proves the support-class claim:
edges in different classes are jointly persistent, a class of order at
least three retains one edge after any two deletions, and a non-joint pair
can only be an entire class of order two.  If all joint pairs have adjacent
endpoints, every nonedge of `G[S]` therefore belongs to a matching.  Since `G[N(r)]` is
`K_4`-free, that matching has order two when `rho=5`, order three when
`rho=6`, and cannot cover enough pairs when `rho>=7`.  This proves (B2).

Suppose finally that `D=P` and that no jointly persistent pair has
nonadjacent endpoints.  Here `m=4`, so `rho>=5`.  If `rho=5`, equality in
(B5) forces

\[
 k_0=k_1=\sigma=0.
\]

Since `rho>0` and `k_1=0`, some persistent edge is external, so `q=1`.
Thus `R={r}` and all five persistent edges lie in one external support
class.  Every pair is jointly persistent, so their endpoints form a
`K_5`, contrary to the `K_4`-free neighbourhood of `r`.  The case
`rho>=7` is already excluded by (B2).

It remains that `rho=6` and `G[S]=K_6-3K_2`.  Write its possible missing
pairs as `a_i b_i`, `1<=i<=3`, and choose `y in N(r)-S`.  The Fan Lemma in
the six-connected graph `G-r` gives six paths from `y` to the six vertices
of `S` which meet only at `y`.  Thus they meet `S` only at their six ends.
Their union with the vertices of `S` deleted is a connected set `T`,
disjoint from `S`, adjacent to `r` and to every vertex of `S`.  The five sets

\[
             \{a_1,a_2\},\{b_1\},\{b_2\},\{a_3\},\{b_3\}
\]

form a `K_5^-` model in `G[S]`; only `a_3b_3` may be absent.  Together
with `{r}` and `T` they form a `K_7^-` model.  This final contradiction
proves the existence of `rx,ry` for every minimum `P`-bag.

Contract the two-edge star on `r,x,y` and six-colour the resulting proper
minor.  Pulling the colouring back gives (B3).  If one of the other five
colours were absent from the remaining six neighbours of `r`, recolouring
`r` with it and restoring `rx,ry` would six-colour `G`.  Joint persistence
keeps the same labelled model after the two deletions.  \(\square\)

### Proposition 7 (root-removal compatibility and the exact split residue)

Use Proposition 6 with `D=P`, and retain its minimum rooted `P`-bag `R`.
Let `h` be the number of components of `G[R]-r`, and let `k_R` be the
number of universal bags met directly by `r` in this reselected model.
Then

\[
                             2h+k_R\le4.                \tag{B6}
\]

In particular, `h<=2`.  If `h=0`, then `R={r}` and `k_R=4`; if `h>=1`,
then `k_R<=2`.

If it has exactly two components `Z_1,Z_2`, then, after relabelling the
universal bags,

\[
 \Lambda(Z_1)=\{U_1,U_2\},\qquad
 \Lambda(Z_2)=\{U_3,U_4\}.                              \tag{B7}
\]

Moreover,

\[
 N_G(Z_1)\subseteq \{r\}\cup U_1\cup U_2,
 \qquad
 N_G(Z_2)\subseteq \{r\}\cup U_3\cup U_4,              \tag{B8}
\]

and `r` has no neighbour in any foreign branch set.  Thus all eight
neighbours of `r` lie in `Z_1\cup Z_2`.  Writing

\[
                         W_i=N(r)\cap Z_i,
\]

both sets are nonempty and, after possibly interchanging their names,

\[
                 \alpha(G[W_1])=1,\quad |W_1|\le3,
                 \qquad
                 \alpha(G[W_2])=2,\quad |W_2|\ge5.       \tag{B9}
\]

The jointly persistent nonadjacent pair in Proposition 6 may then be
chosen with both outer endpoints in `W_2`.

For either `i`, let `U_a,U_b` be the two universal bags owned by `Z_i`,
and put

\[
 T_i=N(r)\cap Z_i,qquad
 A_a=N_G(U_a)\cap Z_i,qquad A_b=N_G(U_b)\cap Z_i.
\]

Then one of the following holds:

1. `A_a=A_b={s}` for one vertex `s\in Z_i`; or
2. there are `s\in Z_i` and a nonempty connected component `C` of
   `G[Z_i-s]` such that

   \[
    C\cap T_i=\varnothing,qquad
    N_G(C)\subseteq\{s\}\cup U_a\cup U_b,qquad
    |N_G(C)|\ge7.                                      \tag{B10}
   \]

   In this outcome one of `U_a,U_b` contains at least three literal
   neighbours of `C`.

For the large component `Z_2` in (B9), only outcome 2 is possible.

If `G[R]-r` is connected and every `P-U_i` adjacency has an edge with its
`P`-endpoint outside `r`, then replacing `R` by `R-r` gives the exact
spanning labelled `K_7^\vee` model in `G-r` needed for Proposition 5.
Neither connectedness nor survival of all four adjacencies is presently
forced by the preceding results.  If they do hold, the parameters of that
model in Proposition 5 satisfy `p=1` and `k=k_R<=2`.

#### Proof

For `D=P`, the required-label set `Gamma(P)` consists of the four universal
labels.  Proposition 6 proves that the sets `Lambda(Z)` over the components
of `G[R]-r` are pairwise disjoint and each has order at least two.  Every
universal label met directly by `r` contributes either its unique
nonpersistent external edge to `ell` or its label to `q`.  If another
`R-U_i` edge existed, deleting the selected root edge would retain both
bag connectivity and the required adjacency; in particular, two root edges
to one universal bag would each be individually persistent.  Conversely
every `ell` edge and every label counted by `q` is a direct universal
contact here.  Hence `k_R=ell+q`, and (B4) gives

\[
                         2h+k_R\le2h+\ell+q\le4.
\]

If `h=0`, spanningness gives `R={r}`, and all four required universal
adjacencies must be direct contacts.  If there are two components, equality
throughout forces (B7).

Exactness makes `R` anticomplete to `B` and `C`.  By the definition of
`Lambda`, every `R-U_j` edge has its `R`-endpoint in the component which
owns `U_j`; this proves (B8) and excludes all cross-ownership contacts.
If `r` met some `U_j`, then `N_G(U_j)\cap R` would not be contained in
either `Z_i`, contradicting that the four labels occur in the disjoint
union in (B7).  Since the model is spanning, every neighbour of `r` is
therefore in `Z_1\cup Z_2`.

Connectedness of `R` makes both `W_i` nonempty.  The sets are anticomplete,
so the audited identity `\alpha(G[N(r)])=3` gives

\[
                 \alpha(G[W_1])+\alpha(G[W_2])=3.
\]

Each summand is positive.  One is therefore one and the other two.  The
first set is a clique of order at most three because `G[N(r)]` is
`K_4`-free; the other contains the remaining at least five neighbours.
This proves (B9).  Every edge from `r` to `W_2` is individually persistent,
and any two are jointly persistent because at least three other such edges
keep `Z_2` attached to `r`.  Since `W_2` is not a clique, two have
nonadjacent outer endpoints.  The final assertions are immediate from the
definition of a labelled model after deleting `r` and the count above.

It remains to prove the last dichotomy.  If `G[Z_i]` contained disjoint
paths from `A_a,A_b` to two distinct vertices of `T_i`, enlarge their
vertex sets to a connected partition `Z_i=L_a\dot\cup L_b`.  Replace

\[
 R\longmapsto R-Z_i,qquad
 U_a\longmapsto U_a\cup L_a,qquad
 U_b\longmapsto U_b\cup L_b.
\]

The other component of `R-r` keeps the new `P`-bag connected and retains
the other two universal adjacencies.  The two distinct `r-T_i` edges
restore the adjacencies to the enlarged owner bags.  Every other labelled
adjacency persists.  This is a spanning labelled model with a smaller
rooted `P`-bag, a contradiction.

The audited
[strict-gammoid Rado--Menger criterion](../results/hc7_multi_owner_portal_linkage_transfer.md#3-exact-local-failure-certificate)
for the two nonempty owner sets
therefore gives a vertex `s` meeting every
`T_i-(A_a\cup A_b)` path in `G[Z_i]`.  If both owner portal sets lie in
`{s}`, they both equal `{s}`.  Otherwise choose a component `C` of
`G[Z_i-s]` containing an owner portal outside `s`.  It contains no vertex
of `T_i`, while all its neighbours within `Z_i` lie at `s`.  The exact
ownership relation (B8) gives the displayed host-neighbourhood inclusion.
That neighbourhood separates `C` from `r`, so seven-connectivity gives
its lower bound.  Apart from `s`, all its vertices lie in the two owner
bags; hence one owner supplies at least three of them.  This proves (B10)
and the dichotomy.  Finally, `Z_2-s` is nonempty for every `s`, because
`Z_2` contains at least five root neighbours.  In outcome 1, every
component of `G[Z_2-s]` would have all its external neighbours in
`{r,s}`: the two owner portal sets equal `{s}`, and (B8) excludes every
other foreign bag.  Deleting `{r,s}` would disconnect `G`, contrary to
seven-connectivity.  Thus `Z_2` has outcome 2, completing the proof.
\(\square\)

Proposition 6 is a two-missing-edge adaptation of the existing rooted
persistence argument; the one-missing-edge theorem does not apply
verbatim.  Reselecting `R` can change the original contact pattern.  Even
the exact deficient-bag response (B3) does not identify its five alternate
colours with the five required branch-set roles.

What is not proved is the operation-to-recipient allocation

\[
 \begin{array}{c}
 \text{five colour-indexed paths}\cr
 \Downarrow\cr
 \text{pairwise disjoint target and owner pieces carrying the}\cr
 \text{specified `K_6` branch-set labels.}
 \end{array}                                             \tag{13}
\]

The path colours need not cover the labels `T` and the protected branch
sets whose contacts a transfer must retain.  Before prescribed-spoke
rerouting, paths of different secondary colours may share
`alpha`-coloured vertices; after rerouting, their first exits may have
repeated branch-set labels.  A small separator for these paths inside `D`
is not automatically a small separator of `G` and does not identify the
neighbourhood of an exceptional degree-eight vertex.  Within an already
aligned donor model, the passage from named ends to clean named first hits
is the first unsupported operation-level inference; neither the forced-
interface theorem nor one fixed proper-minor colouring supplies it.  The
root-removal compatibility gap below occurs earlier when trying to align
that donor model with the minimum deficient-bag response.

### Recorded negative finding: root removal and the two optimizations cannot yet be coupled

**Status:** recorded negative finding / route nonclosure; not a
counterexample to the open target.

The minimum deficient-bag response of Proposition 6 and the labelled
absorption formula of Proposition 5 do not yet apply to the same model.
Proposition 6 minimizes a rooted `P`-bag in `G`; Proposition 5 begins with a
labelled model in `G-r`.  Proposition 7 leaves three possibilities: `R` may
equal `{r}`, `R-r` may be connected while some required `P-U_i` adjacency
is supported only at `r`, or `R-r` may have the exact two-component residue
(B7)--(B9).  Thus it is not yet legitimate to assign the parameters `p,k`
of Proposition 5 to the minimized rooted model carrying the fixed
two-edge-star response.

Even after root-removal compatibility is supplied, applying Proposition 6
with `D=P` gives `p=1` in Proposition 5.  By (A1), one of the four labelled
absorptions has the globally maximal four root contacts only when `k>=3`.
But (B6) forces every compatible nonsingleton minimum rooted model into
the low-contact case

\[
                              p=1,\qquad k\le2.          \tag{13a}
\]

Thus the absorbed model carrying the fixed two-edge-star response need not
even be contact-maximal among spanning `K_6` models.

Reaching a contact-four absorption therefore requires leaving that minimum
rooted family.  In any such alternative model, the donor minimum in
Theorem 4 is taken over all contact-maximal spanning `K_6` models.  A
contact-preserving branch-set transfer can retain adjacency to the fused
bag `P union U_h` while losing the separate `P` or `U_h` contact or
connectivity needed to recover the labelled `K_7^\vee` model.  It can also
move an endpoint or support class needed by the jointly persistent edge
pair.  Hence the family consisting of a minimum rooted `P`-bag, its fixed
pair and colouring, and a contact-four labelled absorption is not known to
be exchange-closed.  A lexicographic potential over those objects therefore
cannot be invoked.

The three repair statements, in their logical order, are now explicit:

1. prove root-removal compatibility: `R-r` is a nonempty connected
   deficient bag retaining all four universal adjacencies, or obtain a
   `K_7^-` model, a six-colouring, or a smaller exceptional
   anti-neighbourhood component;
2. eliminate (13a) by proving that the resulting rooted `P`-bag with at
   most two contacted universal bags already gives a `K_7^-` model, a
   six-colouring, or a smaller exceptional anti-neighbourhood component;
   and
3. in the remaining contact-four case, prove that every donor-reducing
   transfer either lifts to another absolute minimum rooted `P`-bag model
   preserving the same operation response, or gives one of those terminal
   outcomes directly.

Ordinary first-hit linkage, a gammoid rank, or a block--cutvertex
decomposition does not supply these repairs: those tools do not preserve
simultaneously the fixed colouring operation, the separate near-clique
labels, and a residual branch set.  This is the first exact unsupported
inference in the attempted joint model--colouring optimization and should
be checked before any future use of that route.

The newly proved three-component `3,2,2` seven-cut exclusion does not close
the split residue (B7).  Seven-connectivity gives only
`|N_G(Z_i)|>=7`; it gives no upper bound, and (B8) naturally separates two
shores rather than three.  Even equality would require an operation-labelled
two-shore colouring or descent theorem.

Choose `(r,C_0)` so that `r` is exceptional and `C_0` has minimum order
among all components of `G-N[v]` over all exceptional vertices `v`.  Put
`J=G-r`.  A sufficient certificate for a genuine same-graph descent is a
nonempty set `Z\subseteq V(J)-N(r)` satisfying

\[
                         N_J(Z)\subseteq N(r).            \tag{14}
\]

Every component `W` of `J[Z]` is then a component of `G-N[r]`.  If
`|W|<|C_0|`, this contradicts the choice of `C_0`.  In the two-root
pair-deletion host `G-{r,s}`, the same test additionally requires
`N(s)\cap Z=\varnothing`.

The exact operation-level finishing target is therefore the following.

> **One-operation terminal/descent target (open).**  At a root `r` owning
> the globally minimum component `C_0`, choose the optimized model, donor
> `D`, and target `T` of Theorem 4.  For some `x\in N(r)\cap D`, one fixed
> six-colouring of `G-rx`, used throughout, yields an explicit `K_7^-`
> minor model, a six-colouring of `G`, or an exceptional vertex `z` and a
> component `W` of `G-N[z]` with `|W|<|C_0|`.

Any of the three outcomes contradicts (H) or the choice of `C_0`, so this
single statement would eliminate the whole critical host and prove the
`K_7^-` six-colour conjecture.  It is not proved here: the one-operation
analysis above does not supply (13) or a set satisfying (14).

## 6. Exact limit of the reduction

The theorem does not control how the eight neighbours of a retained root
are distributed *inside* a contacted branch set.  In particular, its
conclusions do not exclude the following contact pattern:

\[
 N_G(a)\cap V(H),N_G(b)\cap V(H)
     \subseteq U_1\cup U_2\cup U_3\cup U_4,
 \qquad
 \{a,b\}\text{ anticomplete to }P\cup B\cup C.        \tag{15}
\]

This is a surviving abstract contact pattern, not a claimed example
satisfying (H).  Seven-connectivity supplies paths from the roots but does
not by itself split one of the four contacted branch sets while preserving
its five other model adjacencies.

The global count has the same localization limit.  For `D\subseteq V(G)`,
write `n_8(D)=|\{v\in D:d_G(v)=8\}|`.  For a disconnected exceptional
centre `u` with exterior components `E,F`, the nine vertices of `N[u]` and
(1) give only

\[
                         n_8(E)+n_8(F)\ge16+\tau.       \tag{16}
\]

There is no positive lower bound on either summand separately.  Thus the
count does not place a degree-eight centre in a selected minimum exterior
component or in an operation-returned side.

The reusable open step exposed by (13) is a label-preserving branch-set
transfer: move a root-neighbour piece into an uncontacted member of (4)
while retaining the other required branch-set adjacencies, or return an
actual separation whose boundary is literally the neighbourhood of a
named exceptional degree-eight vertex.  An arbitrary smaller separation
does not certify exceptional anti-neighbourhood descent.  Theorem 3 reduces
the model-only part of this problem to a forced cutvertex interface; (13)
is the remaining operation-specific gap.

## Inputs and scope

- [two-component literal-clique exclusion and density jump](../results/hc7_k7minus_one_nonfull_k5_and_nested_cut.md);
- [global critical density and exceptional count](../results/hc7_k7minus_two_literal_k5_exclusion.md);
- [Norin--Totschnig](https://arxiv.org/abs/2507.03244), *Every graph with
  no `K_7^\vee`-minor is 6-colorable*, Theorem 6;
- [audited one-admissible transfer](../results/hc7_near_k7_surplus_root_transfer.md#1-one-admissible-transfer);
- [rooted incident-edge persistence](../results/hc7_rooted_persistent_model_edge.md) and
  [support-class refinement](../results/hc7_persistent_support_class_refinement.md),
  adapted in Proposition 6 from one missing model edge to the two incident
  missing edges of `K_7^\vee`;
- [deficient-singleton joint persistence](../results/hc7_deficient_singleton_joint_persistence.md),
  for the deletion-capacity and fan-model templates;
- [prescribed first edges and an arbitrary target set](../results/hc7_order8_prescribed_spoke_reduction.md#1-a-prescribed-spoke-fan-lemma);
- seven-connectivity from contraction-criticality.

The note may be cited for the pair-deletion and single-deletion spanning
`K_7^\vee` models, their `K_6` normalizations, the displayed root-contact
restrictions, the forced-interface inclusion (9), the two-hole persistence
count, and the deficient-bag response (B3).  It may not be cited as an
operation-to-branch-set allocation, a same-host exceptional-component
descent, or an elimination of any remaining attachment regime.
