# Both-full component contractions: density and the exact three-separation obstruction

**Status:** active computation-free written proof;
[separate internal audit GREEN](hc7_k7minus_both_full_component_contraction_dichotomy_audit.md).
The results below do **not** eliminate the both-full case or prove the
`K_7^-` six-colour conjecture.  They reduce one whole-component contraction
to either a `K_7^\vee` minor in a proper minor or an explicitly described
three-separation.  Upgrading the near model, or eliminating the wide
three-separation, remains open.

Throughout, let `G` satisfy

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G.                         \tag{H}
\]

Let `u` be an exceptional vertex of degree eight, put `X=N_G(u)`, and
suppose that

\[
                     G-N_G[u]=A\mathbin{\dot\cup}B       \tag{1}
\]

has exactly two components, each adjacent to every vertex of `X`.  The
proved exceptional-neighbourhood theorem and two-component literal-clique
exclusion give

\[
 \alpha(G[X])=3,
 \qquad \delta(G)\ge8,
 \qquad |E(G)|\ge4|V(G)|.                              \tag{2}
\]

Neither `A` nor `B` is a singleton.  Indeed, if `A=\{f\}`, then fullness
and minimum degree eight give `N_G(f)=X=N_G(u)`.  In a six-colouring of
the proper minor `G-u`, the colour on `f` is absent from `X`; assigning
that colour also to the nonadjacent vertex `u` would six-colour `G`,
contrary to (H).

Write `H_A=G/A` and `H_B=G/B`, where the indicated whole connected
component is contracted to one vertex and parallel edges are suppressed.
Both are therefore simple proper minors of `G`.

## 1. At least one contraction lies above the `K_7^\vee` density threshold

Put

\[
 \begin{aligned}
  a&=|A|,& p_A&=|E(G[A])|+|E_G(A,X)|,&
  \Delta_A&=p_A-4a,\\
  b&=|B|,& p_B&=|E(G[B])|+|E_G(B,X)|,&
  \Delta_B&=p_B-4b,
 \end{aligned}                                        \tag{3}
\]

and let `e_X=|E(G[X])|`.  Since there are no edges from `u` to `A\cup B`
or between `A` and `B`,

\[
 |V(G)|=a+b+9,
 \qquad
 |E(G)|=8+e_X+p_A+p_B.                                \tag{4}
\]

Consequently (2) gives

\[
                         \Delta_A+\Delta_B+e_X\ge28.   \tag{5}
\]

The complement of `G[X]` is `K_4`-free because `\alpha(G[X])=3`.
Turan's theorem gives at most `21` complement edges on eight vertices, so

\[
                                  e_X\ge7.             \tag{6}
\]

### Lemma 1 (two-contraction density sum)

For

\[
 q_A=|E(H_A)|-(4|V(H_A)|-8),
 \qquad
 q_B=|E(H_B)|-(4|V(H_B)|-8),                           \tag{7}
\]

one has

\[
 q_A=e_X+\Delta_B-16,
 \qquad
 q_B=e_X+\Delta_A-16,
 \qquad
 q_A+q_B\ge e_X-4\ge3.                                \tag{8}
\]

In particular, for some `C\in\{A,B\}`,

\[
                    |E(H_C)|\ge4|V(H_C)|-6.
\]

#### Proof

Fullness of `A` to `X` means that its contraction has exactly eight
distinct neighbours.  Hence

\[
 |V(H_A)|=b+10,
 \qquad
 |E(H_A)|=|E(G)|-p_A+8=16+e_X+p_B.
\]

This gives `q_A=e_X+\Delta_B-16`; the other identity is symmetric.
Adding them and using (5)--(6) proves (8).  Since both quantities are
integers, their maximum is at least two. \(\square\)

## 2. Exact connectivity of a whole-shore contraction

For a component `C` of a graph and a set `W`, write `C-W` for the graph
obtained by deleting `W\cap V(C)`.

### Lemma 2 (surviving boundary attachment)

If `W\subseteq B\cup X` and `|W|\le2`, every component of `B-W` has a
neighbour in `X-W`.

#### Proof

If a component `D` of `B-W` had no such neighbour, then, using that `B` is
a component of `G-N[u]`,

\[
                              N_G(D)\subseteq W.
\]

The rest of the graph is nonempty, so this would give a vertex cut of
order at most two, contrary to `\kappa(G)\ge7`. \(\square\)

Put

\[
                              J_B=G[X\cup B].           \tag{9}
\]

This graph is connected: `B` is connected and, by fullness, every vertex
of `X` has a neighbour in `B`.

### Theorem 3 (three-connectivity and the exact four-connectivity test)

The graph `H_A` is three-connected.  Moreover,

\[
                 H_A\text{ is four-connected}
                 \quad\Longleftrightarrow\quad
                 J_B\text{ has no cutvertex}.          \tag{10}
\]

If four-connectivity fails, every separating set of order at most three
which contains the contracted vertex and is minimal by inclusion has the
form

\[
                             \{a^*,u,b_0\},             \tag{11}
\]

where `a^*` is the vertex obtained by contracting `A` and
`b_0\in B` is a cutvertex of `J_B`.

#### Proof

Let `Z` be a vertex set of `H_A` of order at most three.  If
`a^*\notin Z`, then `H_A-Z` is obtained from the connected graph `G-Z` by
contracting `A`; hence it is connected.

Suppose `a^*\in Z` and put `W=Z-\{a^*\}`.  If `u\notin W`, then `u`
joins all vertices of `X-W`, and Lemma 2 says that every component of
`B-W` meets `X-W`.  Thus `H_A-Z` is connected.

It remains that `u\in W`.  If `W=\{u\}`, the remaining graph is `J_B`,
which is connected.  If `W=\{u,z\}`, the remaining graph is exactly
`J_B-z`.  Therefore no set of order at most two disconnects `H_A`, and a
set of order three disconnects it precisely when `z` is a cutvertex of
`J_B`.

No vertex `x\in X` is a cutvertex of `J_B`: after deleting `x`, the graph
`B` remains connected and every vertex of `X-\{x\}` still has a neighbour
in `B`.  Hence every such cutvertex lies in `B`, proving (10)--(11).
\(\square\)

The symmetric statement holds with `A` and `B` interchanged.

## 3. What a failed contraction says in the original graph

Assume that `b_0\in B` is a cutvertex of `J_B`.  For a component `K` of
`J_B-b_0`, put

\[
                         X_K=V(K)\cap X,
 \qquad
 N_A(X_K)=N_G(X_K)\cap A.                              \tag{12}
\]

### Theorem 4 (cutvertex blocks lift to seven-contact separations)

For every component `K` of `J_B-b_0`,

\[
 X_K\ne\varnothing,
 \qquad
 N_G(K)=\{u,b_0\}\mathbin{\dot\cup}N_A(X_K),
 \qquad
 |N_A(X_K)|\ge5.                                      \tag{13}
\]

The sets `X_K` form a nontrivial partition of `X`.  If equality holds in
the last inequality for some `K`, then

\[
                         S_K=N_G(K)                    \tag{14}
\]

is a literal order-seven cut of `G`, with `K` as one component of
`G-S_K`.  The critical seven-cut theorem therefore applies: the number
and total boundary-full connected-subgraph packing number of the
components of `G-S_K` lie between two and three.  In fact `G-S_K` has
exactly two components, and their packing vector is `(1,1)`, `(1,2)`, or
`(2,1)`.

#### Proof

If `K` did not meet `X`, then `K` would be contained in `B-b_0` and have
all its neighbours in `\{b_0\}`, contradicting seven-connectivity.  Thus
`X_K` is nonempty.  Distinct components of `J_B-b_0` partition `X`, and
there are at least two of them.

There are no edges from `B` to `A\cup\{u\}`.  There are no edges from
`K` to another component of `J_B-b_0`, while every component has a
neighbour at `b_0`.  Finally `u` is adjacent to every member of `X_K`.
These observations give the equality for `N_G(K)` in (13).
Seven-connectivity now gives

\[
             7\le |N_G(K)|=2+|N_A(X_K)|,
\]

and hence the asserted lower bound.  Equality makes (14) an order-seven
cut, so the packing conclusions follow from the proved critical seven-cut
capacity theorem.  To exclude three components, observe that `u` and
`b_0` are isolated in `G[S_K]`: `u` has neighbours only in `X`, while
`b_0\in B` has no neighbour in `A\cup\{u\}`.  If `G-S_K` had three
components, that theorem would give `\chi(G[S_K])=3` and require every
proper three-colouring to have class sizes `3,2,2`.  Restrict one such
colouring to the other five boundary vertices.  Some colour occurs at
least twice there; assigning that colour also to both isolated vertices
gives a proper three-colouring with a class of order at least four, a
contradiction.  Thus `G-S_K` has exactly two components. \(\square\)

After contraction, every component of `H_A-\{a^*,u,b_0\}` is adjacent to
all three separator vertices.  Thus failure of four-connectivity is not
an arbitrary three-separation: it is the image of the partition (13),
where each part has at least five distinct neighbours in the original
component `A` that was contracted.

### Corollary 4.1 (connected boundary gives four-connectivity)

If `G[X]` is connected, then both `H_A` and `H_B` are four-connected.

#### Proof

Every edge of `G[X]` has both ends in the same set `X_K`, because the
sets arise from distinct components of `J_B-b_0`.  Thus a cutvertex of
`J_B` would partition `X` into at least two nonempty unions of components
of `G[X]`, contrary to connectedness.  Theorem 3 gives four-connectivity
of `H_A`; symmetry gives it for `H_B`. \(\square\)

There is also a useful density consequence when all those inequalities are
strict.  Put

\[
                         h_A=\sum_{v\in A}(d_G(v)-8).   \tag{15}
\]

Since vertices of `A` have no neighbours in `B\cup\{u\}`,

\[
 2|E(G[A])|+|E_G(A,X)|=8|A|+h_A,
 \qquad
 \Delta_A=\frac{|E_G(A,X)|+h_A}{2}.                   \tag{16}
\]

### Corollary 4.2 (wide blocks transfer density to the other contraction)

Suppose `J_B-b_0` has `r` components and every one of them satisfies
`|N_A(X_K)|\ge6`.  Then

\[
                 \Delta_A\ge3r,
 \qquad
                 q_B\ge e_X+3r-16\ge3r-9.            \tag{17}
\]

In particular, if `r\ge3`, the other contraction `H_B` also has at least
`4|V(H_B)|-8` edges.

#### Proof

The sets `X_K` partition `X`.  For each block, its six distinct neighbours
in `A` account for at least six distinct edges from that block to `A`.
Therefore `|E_G(A,X)|\ge6r`.  Equations (6), (8), and (16) now give
(17). \(\square\)

## 4. The exact near-model augmentation requirement

The contracted vertex `a^*` and `u` are nonadjacent twins in `H_A`:

\[
                         N_{H_A}(a^*)=X=N_{H_A}(u).    \tag{18}
\]

This gives a sharp contact test, but not automatic augmentation.

### Lemma 5 (reserved-twin five-contact completion)

Let `Q_1,\ldots,Q_6` be pairwise disjoint connected pairwise adjacent
subgraphs of a `K_7^-`-minor-free graph, and let `s,t` be two further
nonadjacent vertices, disjoint from every `Q_i`, with `N(s)=N(t)`.  Then
`s` and `t` are adjacent to at most four of the six subgraphs.

#### Proof

The two vertices have the same contact set among the `Q_i`.  If they met
five of them, those five connected subgraphs together with `\{s\}` and
`\{t\}` would be seven pairwise adjacent branch sets except for the one
pair `st`, an explicit `K_7^-` model. \(\square\)

Thus, when the six mutually adjacent branch sets of a `K_7^\vee` model are
disjoint from both `a^*` and `u`, the model is terminal as soon as either
twin contacts a fifth such branch set.  On the other hand, in a model which reserves `u` and
uses `a^*` as the singleton deficient branch set, the near model itself
requires four contacts, and `K_7^-`-minor exclusion forbids a fifth.  Its
two missed branch sets need not meet `X`.  Equation (18) then gives `u`
the same four contacts and no fifth one.  This is the sharp
**four-contact twin residue**.

For a general unrooted near model, a twin may instead be absorbed in a
larger branch set or both twins may be used.  Lemma 5 cannot then split a
branch set while retaining all six mutual adjacencies.  The exact missing
rooted input is therefore a model-or-separator theorem which either

1. reserves both twins and gives five contacts to the six mutually
   adjacent branch sets;
2. splits the branch set containing a twin while preserving those six
   branch sets; or
3. returns an actual order-seven separation carrying the same rooted
   model and proper-minor colouring data.

Existence of two unrooted `K_7^\vee` models from the two contractions does
not supply this input: their branch sets and their deficient labels need
not agree.

## 5. Conditional Norin--Totschnig conclusion and exact residue

Let `C\in\{A,B\}` be chosen so that `q_C\ge2`, as supplied by Lemma 1.
If `H_C` is four-connected, Norin--Totschnig, Theorem 6, applies: every
four-connected `n`-vertex graph with at least `4n-8` edges contains a
`K_7^\vee` minor, apart from `K_{2,2,2,2}`.  Here
`|E(H_C)|\ge4|V(H_C)|-6`, so the exception is impossible.  Consequently

\[
                              K_7^\vee\preccurlyeq H_C. \tag{19}
\]

Here `K_7^\vee` denotes `K_7` with two incident edges deleted.  Statement
(19) is not yet a contradiction: a `K_7^\vee` model may avoid the
contracted vertex or use it in a branch set without providing either
missing adjacency after expansion.

If `H_C` is not four-connected, Theorems 3--4 give a cutvertex in the
opposite closed shore and the partition (13).  A block with exactly five
neighbours in `C` returns to an actual order-seven cut.  The remaining
case is the following **wide-articulation residue**:

\[
             |N_C(X_K)|\ge6
             \quad\text{for every cutvertex block }K. \tag{20}
\]

If this partition has at least three blocks, Corollary 4.2 makes the other
component contraction density-eligible as well.  Thus either that other
contraction is four-connected and also gives (19), or both closed shores
have cutvertex partitions of the form (13).  The one-sided residue not
automatically transferred by density has exactly two cutvertex blocks.

Current fullness and boundary-full packing-number-one information does
not force equality in (13), and it does not by itself augment the near
model in (19).  Closing the both-full case by this route therefore needs
one of two genuinely host-level statements:

1. a rooted augmentation theorem which uses the expanded contracted shore
   to restore one of the two missing incidences of (19); or
2. a colouring-response or uncrossing theorem which eliminates (20), or
   turns one of its blocks into a strict smaller actual separation carrying
   the same proper-minor response.

Neither statement is proved here.

## References

- [exceptional-neighbourhood and exterior-completion theorem](../results/hc7_k7minus_exceptional_neighbourhood_completion.md)
- [two-component literal-clique exclusion](../results/hc7_k7minus_one_nonfull_k5_and_nested_cut.md)
- [critical seven-cut capacity theorem](../results/hc7_k7minus_critical_seven_cut_capacity.md)
- Sergey Norin and Agnes Totschnig,
  [*Every graph with no `K_7^\vee`-minor is 6-colorable*, Theorem 6](https://arxiv.org/abs/2507.03244)
