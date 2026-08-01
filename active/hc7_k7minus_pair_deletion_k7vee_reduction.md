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
sets whose contacts a transfer must retain.  Their first exits may all lie
in one unrelated branch set, and paths of different secondary colours may
share `alpha`-coloured vertices.  A small separator for these paths inside
`D` is not automatically a small separator of `G` and does not identify the
neighbourhood of an exceptional degree-eight vertex.  Thus (13) is the
first unsupported inference in the proposed dynamic closure; neither the
forced-interface theorem nor one fixed proper-minor colouring supplies it.

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
- seven-connectivity from contraction-criticality.

The note may be cited for the pair-deletion and single-deletion spanning
`K_7^\vee` models, their `K_6` normalizations, the displayed root-contact
restrictions, and the forced-interface inclusion (9).  It may not be cited
as an operation-coupled branch-set split, a same-host exceptional-component
descent, or an elimination of any remaining attachment regime.
