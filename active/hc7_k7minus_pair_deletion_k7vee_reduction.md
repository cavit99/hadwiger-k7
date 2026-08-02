# Pair deletion at degree-eight centres and a spanning `K_7^\vee` model

**Status:** written nonterminal reduction; separately internally audited in
[`hc7_k7minus_pair_deletion_k7vee_reduction_audit.md`](hc7_k7minus_pair_deletion_k7vee_reduction_audit.md).
This note records the two-root consequence of the disconnected
exceptional-centre branch, the corresponding one-root reduction available
at every exceptional centre, and the exact target interface forced by a
spanning-`K_6` model's optimality.  It eliminates the exact two-component
root-removal residue and the nonconcentrated connected two-loss residue by
two-boundary colouring arguments.  More generally, the minimum deficient
bag and its fixed two-edge response now yield an explicit `K_7^-` model or
an operation-preserving actual nested separator.  The latter is not yet a
six-colouring or exceptional anti-neighbourhood descent.  Global boundary
minimization gives an exact two-shore seven-cut or a full two-/three-component
higher-order interface, but loses the nested labels and operation-to-shore
alignment.  The singleton, atomic two-loss, and one-loss branches therefore
remain nonterminal at that normalized interface.

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

### Proposition 8 (the two-component root-removal residue is impossible)

Under (H), let `r` be exceptional and fix an exact spanning labelled
`K_7^vee` model in `G-r` whose deficient `P`-bag is adjacent to `r`.  Use
Proposition 6 with `D=P` and its minimum rooted `P`-bag `R`.  Then
`G[R]-r` has at most one component.  In particular, the exact `2+2` split
in Proposition 7 cannot occur.

More precisely, assume that split and let `Z_2` be the component with
root-neighbour set `W_2` in (B9).  After relabelling its two owners as
`U_a,U_b`, the minimum-bag transfer first gives vertices

\[
                         t\in Z_2-W_2,\qquad p\in R-t
\]

such that

\[
 N_{G[R]}(t)=\{p\},\qquad
 N_G(t)\subseteq\{p\}\cup U_a\cup U_b,                 \tag{B11}
\]

and every edge from the `P`-bag `R` to either `U_a` or `U_b` has
`P`-endpoint `t`.  In particular both owner-neighbour sets of `t` are
nonempty.  These conclusions yield two proper minors whose six-colourings
glue to a six-colouring of `G`, a contradiction.

#### Proof

Start with the connected set `C` supplied by outcome 2 of Proposition 7
inside `Z_2-s_0`.  It is disjoint from `W_2`, has only `s_0` as a neighbour
inside `R-C`, and has foreign neighbours only in `U_a,U_b`.

Suppose `C` meets `U_a` and some `R-U_b` edge has its `R`-endpoint outside
`C`.  Move `C` from `R` into `U_a`.  The residual `P`-bag is connected;
the enlarged `U_a`-bag is connected; an edge across
`C | (R-C)` restores their mutual adjacency; and the outside portal retains
the `P-U_b` adjacency.  Every other labelled adjacency survives.  This is
a spanning model with a smaller rooted `P`-bag, contrary to the choice of
`R`.  Interchanging the owners gives the same conclusion.  Since `C`
contains at least one owner portal and both model adjacencies are nonempty,
`C` consequently contains every `P`-endpoint of both owner adjacencies.

Among all nonempty connected sets `L\subseteq C` such that `R-L` is
connected, `L` has exactly one neighbour in `R-L`, and `L` contains all
`P`-endpoints of both owner adjacencies, choose one of minimum order.  Let
`q` be its unique neighbour in `R-L`, and put

\[
 B=N_L(q),\qquad A_i=N_L(U_i)\quad(i\in\{a,b\}).
\]

If `G[L]` had vertex-disjoint paths from `A_a,A_b` to two distinct vertices
of `B`, enlarge those paths to a connected partition
`L=L_a\mathbin{\dot\cup}L_b` and move `L_a,L_b` into their respective
owners.  The two distinct `q-L` edges restore both owner adjacencies, again
shrinking the rooted `P`-bag.  The two-owner Rado--Menger criterion
therefore gives a vertex `w\in L` meeting every path in `G[L]` from `B` to
`A_a\cup A_b`.

If the two owner portal sets are not both contained in `\{w\}`, choose a
component `L'` of `G[L-w]` containing an owner portal outside `w`.  It
contains no vertex of `B`, so it has only `w` as a neighbour in `R-L'`.
The preceding one-owner transfer argument, applied to `L'`, forces `L'` to
contain all `P`-endpoints of both owner adjacencies.  This contradicts the
minimum choice of `L`.  Hence

\[
    A_a=A_b=\{w\}.                                 \tag{B12}
\]

If `L-w` were nonempty, a component of `G[L-w]` would have all its host
neighbours in `\{q,w\}`: (B12) excludes the owners, and the exact ownership
relations exclude every other branch set.  This would contradict
seven-connectivity.  Thus `L=\{w\}`.  Set `t=w` and `p=q`.  This proves
(B11) and the portal assertion.

Put `Q=Z_2-\{t\}` and let

\[
                    H=V(G)-(Q\cup\{r,t\}).             \tag{B13}
\]

The set `Q` is nonempty because `W_2\subseteq Q` and `|W_2|\ge5`.
Since `t\notin W_2`, the edge `rt` is absent; hence `p\ne r`.  Componenthood
of `Z_2` in `G[R]-r` then puts `p` in `Z_2`.  Thus `t` is a leaf of the
connected graph `G[Z_2]`, and `G[Q]` is connected.  The six foreign branch
sets induce a connected subgraph, and `Z_1` attaches to its two owner bags;
hence `G[H]` is connected.

The exact ownership inclusion (B8), componenthood of `Z_2` in `G[R]-r`,
and the portal assertion give no edge between `Q` and `H`.  Both open sides
meet both boundary vertices: `Q` meets `r` through `W_2` and meets `t`
through `p`; `H` meets `r` through `W_1` and meets `t` through either owner
bag.  Finally `rt` is absent because `t\notin W_2`.

Contract the connected set `H\cup\{r\}` to `r`.  Because `Q` is
anticomplete to `H`, and because `H` meets `t`, the resulting proper minor
is exactly

\[
                       G[Q\cup\{r,t\}]+rt.             \tag{B14}
\]

Similarly, contracting the connected set `Q\cup\{r\}` to `r` gives the
proper minor

\[
                       G[H\cup\{r,t\}]+rt.             \tag{B15}
\]

Both minors have six-colourings by (H).  In each colouring `r` and `t`
have different colours because the edge `rt` is present.  Permute the
palette of one colouring so that the ordered colours on `r,t` agree in the
two colourings.  Their restrictions then glue across `\{r,t\}`; there is
no edge between `Q` and `H`.  This gives a six-colouring of `G`, contrary
to (H).  Thus the two-component outcome is impossible.  \(\square\)

### Proposition 9 (the fixed response yields a nested actual separator)

Retain Proposition 6 with `D=P`, its minimum rooted bag `R`, the jointly
persistent nonadjacent edges `rx,ry`, and the fixed six-colouring `c` of

\[
                            H=G-\{rx,ry\}.              \tag{B16}
\]

Then either `H` contains a `K_7^-` minor or there are an \(i\) and a
nonempty proper connected set \(Y\subset U_i\) such that \(U_i-Y\) is
connected and \(N_G(Y)\) is an actual separator of order at least seven.
Under (H), only the separator outcome can occur, and the same fixed
colouring `c` remains attached to it.

#### Proof

The exact model is spanning, and `R` is anticomplete to the connected bags
`B,C`.  Hence

\[
                         N_G(R)\subseteq U_1\cup\cdots\cup U_4
\]

is an actual separator and has order at least seven.  Deleting `rx,ry`
removes at most two vertices from this boundary.  Joint persistence says
that the same model survives in `H`, so each `U_i` still contains an
`H`-neighbour of `R`.  At least five surviving boundary vertices are
therefore distributed among four universal bags, and one bag contains two.

Apply the audited
[exact-`K_7^\vee` separator dichotomy](../results/hc7_k7minus_exact_k7vee_separator_dichotomy.md#corollary-2-preserving-a-fixed-two-edge-response)
to those two surviving portals.  It gives a `K_7^-` model using no deleted
edge, or the stated actual separator in `G`.  No recolouring is performed,
so `c` is retained in the second outcome.  \(\square\)

The proposition is operation-preserving but nonterminal.  The separator
may have order greater than seven, and its boundary need not be the
neighbourhood of an exceptional degree-eight vertex.

### Proposition 10 (two lost adjacencies reduce to one atomic bag)

Assume `Z=R-r` is nonempty and connected, and precisely the `P-U_3` and
`P-U_4` adjacencies disappear after deleting `r`.  Then either `G` is
six-colourable or

\[
                              R=\{r,s\}                 \tag{B17}
\]

for one vertex `s`, where `rs` is an edge, `s` is the unique `P`-endpoint
of the `P-U_1` and `P-U_2` adjacencies, and `r` is the only possible
`P`-endpoint of the `P-U_3` and `P-U_4` adjacencies.

#### Proof

The two lost adjacencies force `r` to meet `U_3,U_4`.  Proposition 7 gives
`k_R<=2`, so `r` misses `U_1,U_2`.  Put

\[
 T=N(r)\cap Z,
 \qquad A_i=N_G(U_i)\cap Z\quad(i=1,2).                \tag{B18}
\]

All three sets are nonempty.  If `G[Z]` contained disjoint paths from
`A_1,A_2` to distinct vertices of `T`, enlarge them to a connected
partition \(Z=L_1\mathbin{\dot\cup}L_2\) and move \(L_i\) into \(U_i\).  The
two paths are vertex-disjoint, including their distinct endpoints.  The
distinct `r-L_i` edges restore the corresponding `P-U_i` adjacencies, while the
two direct contacts at `r` retain the other two.  This would leave the
smaller rooted `P`-bag `{r}`, contrary to the choice of `R`.

The two-owner Rado--Menger criterion therefore gives a vertex \(s\in Z\)
meeting every \(T\)--\((A_1\cup A_2)\) path in `G[Z]`.  If

\[
                              A_1=A_2=\{s\},            \tag{B19}
\]

then any component of `G[Z-s]` has all its host neighbours in `{r,s}`:
exactness excludes `B,C`, the two lost adjacencies exclude `U_3,U_4`,
and (B19) excludes `U_1,U_2`.  Seven-connectivity forces `Z={s}`.  This is
exactly (B17), including `rs in E(G)` because `R` is connected.

Otherwise choose a component `D` of `G[Z-s]` containing an owner portal
outside `s`.  It contains no member of `T`.  If it met one owner while a
portal to the other owner remained outside, moving `D` into the first
owner would preserve the other adjacency and shrink `R`.  Applying this
in both orientations gives

\[
                              A_1\cup A_2\subseteq D.   \tag{B20}
\]

Inside `D`, choose a smallest nonempty connected set `L` which contains
\(A_1\cup A_2\), has exactly one neighbour \(q\) in \(R-L\), and leaves \(R-L\)
connected.  Apply the same two-owner Rado--Menger argument between the two
owner portal sets and `N_L(q)`.  A successful linkage again splits `L`
between the two owners and shrinks `R`.  On failure, its one-vertex
separator `t` must contain every owner portal: otherwise a portal-side
component is a smaller choice of `L` by the preceding one-owner transfer.
If `L-t` were nonempty, one of its components would have all host
neighbours in `{q,t}`, contradicting seven-connectivity.  Hence

\[
 L=\{t\},\qquad N_{G[R]}(L)=\{q\},\qquad q\in R-L,
 \qquad A_1=A_2=\{t\},
 \qquad rt\notin E(G).                                 \tag{B21}
\]

Put `Q=Z-t` and let `J` be the union of the six foreign branch sets.  The
vertex `t` is a leaf of connected `G[Z]`, so `Q` is connected and
nonempty.  The foreign `K_6` model makes `J` connected.  Equations
(B20)--(B21), exactness, and the two lost adjacencies give

\[
 E_G(Q,J)=\varnothing.                                 \tag{B22}
\]

Both `Q` and `J` meet both nonadjacent boundary vertices `r,t`: the set
`Q` meets `r` through `T` and `t` through `q`; the exact model gives the
edges from `r` to `U_3,U_4`, while `t` meets `U_1,U_2`, so `J` meets both
boundary vertices.

Contracting \(J\cup\{r\}\) to `r` gives the proper minor

\[
                         G[Q\cup\{r,t\}]+rt,            \tag{B23}
\]

and contracting \(Q\cup\{r\}\) to `r` gives

\[
                         G[J\cup\{r,t\}]+rt.            \tag{B24}
\]

Six-colour both minors.  The edge `rt` makes its endpoint colours
distinct; permute one palette so that the ordered colours on `r,t` agree.
The two colourings glue across `{r,t}` by (B22), six-colouring `G`.  In
fact, (B22) already makes `{r,t}` a two-vertex cut; the colouring splice is
retained to exhibit the terminal conclusion directly.  Thus
the nonconcentrated branch is impossible and only (B17) remains.
\(\square\)

### Proposition 11 (global minimum-separator normal form)

The existence of the separator returned by Proposition 9 guarantees a
separator \(S=N_G(A)\), where \(A\) is nonempty and connected,

\[
             G-(A\cup S)\ne\varnothing,                \tag{B25}
\]

and \(|S|\) is minimum over all sets satisfying these conditions.  Exactly
one of the following holds.

1. \(|S|=7\), and \(G-S\) has exactly two components.  If their maximum
   numbers of pairwise disjoint connected subgraphs full to \(S\) are
   \(\mu_1,\mu_2\), then, up to exchanging the components,

   \[
                       (\mu_1,\mu_2)\in\{(1,1),(1,2)\}, \tag{B26}
   \]

   while

   \[
       K_5\npreccurlyeq G[S],\qquad 2\le\chi(G[S])\le4.
   \]
2. \(|S|\ge8\), every component of \(G-S\) is adjacent to every vertex of
   \(S\), and \(G-S\) has exactly two or three components.  If their number
   is \(m\), then for every integer \(a\) and every \(a\)-set \(F\subseteq S\),

   \[
     0\le a\le m-1
     \quad\Longrightarrow\quad
     \chi(G[S-F])\le5-a,
     \qquad K_{6-a}^-\npreccurlyeq G[S-F],             \tag{B27}
   \]

   and

   \[
     0\le a\le m-2
     \quad\Longrightarrow\quad
     K_{5-a}\npreccurlyeq G[S-F].                    \tag{B28}
   \]

   In particular,

   \[
    K_5\npreccurlyeq G[S],\qquad \chi(G[S])\le4,
    \qquad
    \begin{cases}
      2\le\chi(G[S])\le4,&m=2,\\
      3\le\chi(G[S])\le4,&m=3.
    \end{cases}                                       \tag{B29}
   \]

The fixed colouring \(c\) from Proposition 9 remains globally available in
both outcomes.  The globally minimized set \(A\) need not lie inside the
separator side returned there or preserve its branch-set labels; in
particular, this proposition does not assert that either deleted edge avoids
\(S\) or joins prescribed sides.

#### Proof

Proposition 9 supplies at least one set satisfying (B25), and
seven-connectivity gives \(|N_G(A)|\ge7\) for every such set.  Choose one
with minimum boundary order and put \(S=N_G(A)\).

If \(|S|=7\), the audited critical seven-cut theorem and the audited
three-component exclusion say that \(G-S\) has exactly two components and
give (B26), together with an edge of \(G[S]\).  The audited general
seven-cut capacity theorem excludes a \(K_5\) minor from the boundary; the
known case \(t=5\) of Hadwiger's conjecture supplies the upper chromatic
bound.

Suppose \(|S|\ge8\).  Then \(A\) is a minimum eligible set in the sense of
the audited minimum-positive-separator normal form.  If some component
\(D\) of \(G-S\) had \(|N_G(D)|=7\), then \(D\) itself would satisfy
(B25) with a smaller boundary: another component of \(G-S\) lies outside
\(D\cup N_G(D)\).  This contradicts the choice of \(A\).  The other
outcome of that normal-form theorem therefore applies: every component is
full to \(S\), and their number is two or three.

For (B27), choose \(a+1\) full components and enumerate
\(F=\{s_1,\ldots,s_a\}\).  Contract each
\(D_i\cup\{s_i\}\) for \(i\le a\), contract \(D_{a+1}\) alone, delete
all unused components, and retain \(S-F\).  The \(a+1\) contracted vertices
form a clique complete to \(G[S-F]\).  A six-colouring of this proper minor
gives \(\chi(G[S-F])\le5-a\).  A \(K_{6-a}^-\)-minor in the retained
boundary, together with that clique, would give a \(K_7^-\)-minor in \(G\).
The minor is proper: when \(a=0\) another nonempty component is deleted,
and when \(a>0\) an edge between an augmented component and its assigned
boundary vertex is contracted.

For (B28), choose \(a+2\) full components, augment the first \(a\) as
above, and contract the last two without a boundary vertex.  The resulting
\(a+2\) branch sets are complete to \(G[S-F]\) and have exactly one
possibly absent adjacency, between the two unaugmented components.  A
\(K_{5-a}\)-minor in the retained boundary would therefore complete an
explicit \(K_7^-\)-minor model.

Taking \(a=0\) in (B28) excludes a \(K_5\) minor from \(G[S]\).  The known
case \(t=5\) of Hadwiger's conjecture gives \(\chi(G[S])\le4\).  If \(m=2\)
and \(S\) were independent, contract the opposite full component together
with all of \(S\) when colouring each closed shore; the two colourings make
\(S\) monochromatic, align, and glue.  If \(m=3\) and \(G[S]\) were
bipartite, partition \(S\) into at most two nonempty independent classes
and assign them injectively to the other two full components when colouring
each closed shore.  Contract each assigned component together with its
class.  Again the exact boundary partitions align and glue.  Either
construction would six-colour \(G\), which proves the lower bounds in
(B29).

No operation is changed in choosing \(A\), so the fixed colouring remains
globally defined.  The final limitations are immediate: global boundary
minimization does not retain the original nesting or control the locations of
\(r,x,y\).  \(\square\)

### Continuation gate

Proposition 8 satisfies the colouring terminal for the disconnected
remainder.  Proposition 10 does the same for every nonconcentrated
connected remainder with two lost universal adjacencies.  Its only
two-loss survivor is the atomic bag (B17); one-loss remainders remain.

Proposition 9 bypasses all of those root-removal forms at the model level.
In the target-free host it always returns an actual nested separator while
retaining the fixed response (B3).  This is stronger than another local
case split, but it is not one of the three required terminal outcomes.
Using only the existence of that separator, Proposition 11 separately
sharpens the host to an exact two-shore seven-cut, or to a globally minimum
boundary of order at least eight with exactly two or three full complementary
components and the contraction profile (B27)--(B29).  This second normalization
does not retain the original nested side or branch-set labels.

The immediate target is therefore no longer an unlabelled
root-removal-compatibility statement.  It is an **operation-labelled
separator terminalization**: use the fixed response to produce a common
boundary equality partition, an explicit `K_7^-` model, or a component of
`G-N[z]` smaller than the chosen minimum for a named exceptional `z`.

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
neighbourhood of an exceptional degree-eight vertex.  Proposition 9 now
supplies a real host separator before that first-hit inference, but it does
not align the deleted endpoints `x,y` with opposite open shores.  Even when
such alignment is imposed, the coupled Kempe switches can stop at
five-colour saturation on one side of the boundary.  No proved theorem
converts that saturation into a named branch-set transfer or exceptional
anti-neighbourhood descent.

### Recorded negative finding: the nested separator is not yet terminal

**Status:** recorded negative finding / route nonclosure; not a
counterexample to the open target.

Proposition 9 repairs the model-level root-removal obstruction: without
choosing among the singleton, connected one-loss, or atomic two-loss forms,
the fixed two-edge-star response now returns an actual separator in the
host.  Proposition 11 makes the residual separator boundary-minimal and
forces either the exact two-shore order-seven form or the two-/three-shore
full-interface form (B27)--(B29).  Neither form is a terminal outcome.  The deleted
endpoints need not lie in opposite open shores, and the boundary need not be
\(N_G(z)\) for any named exceptional degree-eight vertex \(z\).

There is one exact endpoint normalization when the operation-preserving
separator of Proposition 9 itself has order seven.  Put

\[
 A=Y,\qquad S=N_G(Y),\qquad
 B=V(G)-(A\cup S).
\]

Then `A,B` are the two open components and \(r\notin A\).  The fixed
double-deletion colouring is proper on \(G[A\cup S]\) whenever \(r\in B\);
if \(r\in S\), it is proper on that closed shore exactly when
\(x,y\in B\), and symmetrically on the other shore exactly when
\(x,y\in A\).  These are simply the placements for which neither deleted
edge lies wholly in the displayed closed shore.

More generally, if some \(z\in\{x,y\}\) lies outside \(S\), take a named
six-colouring of the proper minor \(G-rz\).  Its ends have one colour,
the labelled near-clique model still survives, and the restriction to the
closed shore opposite the edge `rz` is a legal boundary colouring.  Thus a
named legal one-sided response is always available unless
\(x,y\in S\).  In that last placement no six-colouring of
\(G-\{rx,ry\}\) can be proper on \(G[S]\), since it would then also be a
six-colouring of `G`.  This isolates two residues: double-boundary placement,
where even endpoint legality fails, and every other placement, where a legal
partition exists but lacks the required connected subgraphs on its shore.

Even if the endpoints are assumed to lie in opposite shores, simultaneously
switching two boundary-avoiding Kempe components repairs both deleted edges
and six-colours \(G\).  Hence failure forces one endpoint to be saturated:
all five relevant bichromatic components meet the boundary.  They may all
meet it through the same vertex \(r\).  The first unsupported inference is
therefore

\[
 \begin{split}
 &\text{five-colour saturation at an operation-labelled separator}\\
 &\qquad\Longrightarrow
 \text{ a label-preserving transfer, a common boundary partition,}\\
 &\hspace{45mm}\text{or a named exceptional anti-neighbourhood descent.}
 \end{split}                                             \tag{13a}
\]

No proved result in the repository supplies this implication.  This does
not refute operation-labelled terminalization; it identifies the extra
localization theorem that it needs.

Two audited separator results describe the nearest existing route.  The
[nested full-neighbourhood descent](../results/hc7_nested_full_neighbourhood_descent.md)
strictly decreases separator excess unless every complementary component is
full to the current boundary, but it need not preserve the fixed operation
or identify a degree-eight centre.  At exact order seven, the
[selected-response preservation theorem](../results/hc7_exact7_selected_response_preservation.md)
would six-colour `G` if one shore contained the required partition-specific
carrier system.  The exact near-clique frame does not yet force that carrier.

### Secondary route nonclosure: the two optimizations remain incompatible

The minimum deficient-bag response of Proposition 6 and the labelled
absorption formula of Proposition 5 still do not apply to the same optimized
model.  Proposition 6 minimizes a rooted `P`-bag in `G`; Proposition 5 begins
with a labelled model in `G-r`.  Consequently it is not legitimate to assign
the parameters `p,k` of Proposition 5 to the minimized rooted model carrying
the fixed two-edge-star response.

Even after root-removal compatibility is supplied, applying Proposition 6
with `D=P` gives `p=1` in Proposition 5.  By (A1), one of the four labelled
absorptions has the globally maximal four root contacts only when `k>=3`.
But (B6) forces every compatible nonsingleton minimum rooted model into
the low-contact case

\[
                              p=1,\qquad k\le2.          \tag{13b}
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

The repair statements are now:

1. terminalize the operation-labelled separator of Proposition 9 by proving
   the implication in (13a);
2. if the separate absorption route is used, eliminate (13b) by proving
   that the resulting rooted `P`-bag with at most two contacted universal
   bags already gives a `K_7^-` model, a six-colouring, or a smaller
   exceptional anti-neighbourhood component; and
3. in its remaining contact-four case, prove that every donor-reducing
   transfer either lifts to another absolute minimum rooted `P`-bag model
   preserving the same operation response, or gives one of those terminal
   outcomes directly.

Ordinary first-hit linkage, a gammoid rank, or a block--cutvertex
decomposition does not supply these repairs by itself: those tools do not
preserve simultaneously the fixed colouring operation, the separate near-clique
labels, and a residual branch set.  This is the first exact unsupported
inference in the attempted joint model--colouring optimization and should
be checked before any future use of that route.

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
- [two-owner Rado--Menger transfer](../results/hc7_multi_owner_portal_linkage_transfer.md);
- [nested full-neighbourhood separator descent](../results/hc7_nested_full_neighbourhood_descent.md);
- [exact-seven selected-response preservation](../results/hc7_exact7_selected_response_preservation.md);
- seven-connectivity from contraction-criticality.

The note may be cited for the pair-deletion and single-deletion spanning
`K_7^\vee` models, their `K_6` normalizations, the displayed root-contact
restrictions, the forced-interface inclusion (9), the two-hole persistence
count, the deficient-bag response (B3), the two-owner singleton reduction,
the six-colouring exclusion of the two-component root-removal residue, the
fixed-response nested-separator reduction, and the connected two-loss atomic
reduction.
It may not be cited as an operation-to-branch-set allocation, a same-host
exceptional-component descent, complete root-removal compatibility, or host
closure.
