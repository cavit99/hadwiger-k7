# Independent audit: literal-clique exclusion and nested cuts

Audited file:
`results/hc7_k7minus_one_nonfull_k5_and_nested_cut.md`

Audited SHA-256:

```text
e1b54acdd971831786c0d8912d5e4189aaeedd84184540ed438e594aadb9b2e4
```

**Verdict:** **GREEN** for the exact revision above.

The promoted source differs from the revision originally audited at
`28fb2ccad0dbb0b9a2cac4d5a97055aedf368ec6bf5f819dbea538289ee12d17`
only in its status line.  No theorem statement, hypothesis, proof, or scope
text changed.

This is a separate internal mathematical audit, not independent human review
or external peer review.  The generalized two-component clique exclusion was
reconstructed from scratch, independently of the earlier one-nonfull proof.
No finite calculation is used in the new argument.

## Checked dependencies

| Dependency | SHA-256 |
|---|---|
| One-nonfull attachment reduction | `2b269e7ecea09f695991689e2a6db64d928aedb141ea8cfbf85d14f84fc70617` |
| Degree-seven neighbourhood classification | `04e085032a096ef3fd508ca4ee287ef82417a718ae3d95646ae4cbd0b911ed2e` |
| Seven exceptional vertices and degree defect | `5cf181ca631ba0e4f6f5235ca4357faac5bdcce3acde5ba8e83dde0e05e1a388` |
| Critical seven-cut capacity | `d4d650fee168fc2ff0e00a3b7b0faed6ff674ba8cd3c06c263f63c4170656f34` |
| Uniform defect-two connected-subgraph reflection | `7957de3aeb635a9f48e1e1668e34f43abbba15cac270c0f716821b2925af3fd8` |

The adjacent audits mark each of these revisions GREEN.  In particular, the
first dependency supplies the exact `(1,2)` packing orientation, membership
of `G[S]` in the frozen 129-boundary residual, and
`|N_G(x)\cap S|\le4`.  The third dependency records the audited degree-defect
inequality used in Corollary 2.1.

## 1. Common-attachment five-linkage

Let `D` be one exterior component and `D'` the other.  Because `D` is a
component of `G-N_G[u]`, its entire open neighbourhood is `N_X(D)`: it has
no edge to `D'` or `u`.  If `|N_X(D)|\le6`, that neighbourhood would
separate `D` from `D'\cup\{u\}`, contrary to seven-connectivity.  Hence
both exterior components meet at least seven of the eight vertices of `X`,
and their common attachment set

\[
                         T=N_X(E)\cap N_X(F)
\]

has order at least six.

Suppose a literal clique `L` of order five lies in
`J_D=G[D\cup N_X(D)]`.  If five disjoint set paths from `L` to `T` did not
exist in `J_D`, set Menger gives an `L`--`T` blocker `W` of order at most
four.  Length-zero paths correctly cover `L\cap T`.  The clique `L-W` is
nonempty and lies in one component `Q` of `J_D-W`.  The component `Q` is
disjoint from `T-W`; otherwise it contains an `L`--`T` path avoiding `W`.

Put

\[
                     R=W\cup\{u\}\cup(X-N_X(D)).
\]

The three displayed parts are pairwise disjoint, and `X-N_X(D)` has order
at most one, so `|R|\le6`.  The proof
must exclude every route from `Q` in `G-R`; the list is exhaustive:

1. there is no route to another vertex of `J_D-W` because `Q` is a
   component there;
2. a vertex of `D` has no neighbour in `D'`, while a vertex of `N_X(D)`
   adjacent to `D'` belongs to `N_X(D')` and hence to `T`; no such surviving
   vertex lies in `Q`;
3. every vertex of `X-N_X(D)` has been deleted, as has `u`; and
4. there is no third exterior component.

Thus `Q` remains a component of `G-R`.  Meanwhile `T-W` is nonempty
(indeed it has order at least two), is not deleted by `X-N_X(D)`, and lies
outside `Q`.  Hence `R` is a genuine vertex cut of order at most six,
contradicting seven-connectivity.  The five `L`--`T` paths therefore exist.

After trimming, each enlarged clique bag contains a distinct literal
endpoint in `T`.  The original clique supplies all pairwise adjacencies
among the five bags.  Since an endpoint in `T` is adjacent to the connected
component `D'` and to `u`, every bag is adjacent to both additional branch
sets.  Here component adjacency is sufficient: different endpoints may use
different neighbours in the single branch set `D'`.  The centre `u` is
anticomplete to `D'`, and this is the sole absent adjacency.  The seven
branch sets form an explicit `K_7^-`-minor model.  Lemma 1 is sound for
either choice of `D`.

## 2. Global clique exclusion and the density jump

A literal `K_5` containing `u` would give a literal `K_4` in the exceptional
neighbourhood `G[X]`.  A clique avoiding `u` cannot meet both anticomplete
exterior components.  If it meets one component `D`, each of its boundary
vertices has an edge to its chosen vertex in `D`, so every such boundary
vertex belongs to `N_X(D)`; the clique lies in `J_D` and Lemma 1 excludes
it.  The only remaining possibility is a clique wholly in `X`, which also
contradicts `K_4`-freeness.  These cases exhaust `V(G)=\{u\}\cup X\cup
E\cup F`, proving the generalized Theorem 2.

The exact degree-seven theorem then gives `n_7=0`, while the standard
critical-host lower bound `\delta(G)\ge7` improves to `\delta(G)\ge8`.
Consequently `2|E(G)|\ge8|V(G)|`.  Because a degree-eight vertex is
nonexceptional exactly when it belongs to a literal `K_5`, every
degree-eight vertex is exceptional.  Substitution into

\[
 25\le 9|V(G)|-2|E(G)|=2n_7+n_8-
       \sum_{i\ge10}(i-9)n_i
\]

gives `n_8\ge25+\tau` and hence `|V(G)|\ge25`.

The neighbour partition

\[
 N_G(x)=\{u\}\mathbin{\dot\cup}(N_G(x)\cap S)
             \mathbin{\dot\cup}(N_G(x)\cap F)
\]

gives at least three neighbours in `F`.  If `E` had one vertex, that vertex
would have degree at most seven.  If `E` had two vertices, connectedness and
minimum degree eight would force each one to be adjacent to the other and to
all seven vertices of `S`; their singleton subgraphs would contradict the
packing-one conclusion.  This one-nonfull specialization proves Corollary
2.2; unlike Theorem 2 and Corollary 2.1, it uses the one-nonfull dependency.

## 3. Six-fan obstruction

The fan version of Menger's theorem is used with a separator `W` avoiding
`x`.  If the six-fan failed, `|W|\le5`, and `S-W` is nonempty.  In
`G-(W\cup\{u\})`, no path from `x` can enter `E` before reaching `S-W`:
`E` is anticomplete to `x\cup F` and its only boundary contacts lie in `S`.
This would be a cut of order at most six, contradicting
seven-connectivity.

Truncation at the first visit to `S` leaves six arms sharing only `x`.
Their open union `T` is connected, lies in `F\cup\{x\}`, and contacts six
distinct boundary vertices.  If `T` avoided an `S`-full connected subgraph
`P\subseteq F`, then `\{u\}`, `P`, and `T` would be pairwise disjoint on
the same open shore: the first two are `S`-full and `T` has boundary defect
one.  The opposite component `E` is `S`-full, and `G[S]` lies in the frozen
residual, so every hypothesis of the uniform defect-two reflection theorem
is met.  Its six-colouring contradiction proves Lemma 3.

## 4. Tight nested-cut reduction

For the component `K` of `(F\cup\{x\})-V(P)` containing `x`, exterior
anticompleteness and the component definition leave exactly three types of
outside neighbours: `u`, vertices of `A\subseteq S`, and vertices of
`B\subseteq V(P)`.  Hence

\[
                         N_G(K)=\{u\}\mathbin{\dot\cup}A
                                      \mathbin{\dot\cup}B.
\]

Seven-connectivity gives `|A|+|B|\ge6`.  If `|A|\ge5`, the subgraphs
`\{u\}`, `P`, and `K` are pairwise disjoint on the joined shore; the first
two are full at `S` and `K` has boundary defect at most two.  Together with
the full component `E`, the uniform reflection theorem would six-colour
`G`.  Thus the surviving bound `|A|\le4` is valid.

At equality, `C=\{u\}\cup A\cup B=N_G(K)` has order seven.  Every component
of `G-C` has neighbourhood all of `C`, by seven-connectivity.  Any component
other than `K` must therefore contain a neighbour of `u`; all available
ones are in `S-A`, and every vertex of `S-A` lies with the connected
component `E`.  Thus there is exactly one component besides `K`.

Within `K`, the vertex `x` is the unique neighbour of the boundary vertex
`u`.  Every `C`-full connected subgraph in `K` must contain `x`, while `K`
itself is full, so its packing number is exactly one.  Critical seven-cut
capacity makes the other packing number one or two.  In the packing-two
case, the connected-rich diamond-deletion lemma from the one-nonfull
reduction applies verbatim and yields
`K_4^-\npreccurlyeq G[C]-c` for every `c\in C`; otherwise the vector is
exactly `(1,1)`.

If `K=\{x\}`, equality would give `d_G(x)=7`, contradicting the established
minimum degree eight.  For each component `Q` of `K-x`, all outside
neighbours lie in the seven-set `Z=\{x\}\cup A\cup B`.  Seven-connectivity
forces equality `N_G(Q)=Z`, so these are components of `G-Z`.  Every other
component `D` of `G-Z` likewise has `N_G(D)=Z` and is therefore adjacent to
`x`.  Outside `Z` and the components of `K-x`, the only available neighbour
of `x` is `u`; hence all remaining vertices form one component containing
`u`.

Critical seven-cut capacity allows at most three components after deleting
`Z`.  It follows that `K-x` has one or two components.  In the latter case,
the exact three-component conclusion of that theorem gives
`\chi(G[Z])=3` and colour-class sizes `3,2,2` in every proper
three-colouring.  Every conclusion of Theorem 4 follows.

## Scope and unresolved assumptions

No unresolved internal gap was found.  The result is conditional on the
five separately audited dependencies listed above, including the
computer-assisted frozen-boundary and defect-two reflection inputs.  The
new linkage and nested-cut arguments themselves are computation-free.

The result excludes literal `K_5`s whenever an exceptional degree-eight
centre has exactly two exterior components, and sharply structures the
tight failed allocation case in the one-nonfull specialization.  It does
not settle the non-tight case
`|A|+|B|\ge7`, the remaining tight `(1,1)` or connected-rich cases, the
general connected-subgraph allocation theorem, the `K_7^-` six-colour
conjecture, or Hadwiger's conjecture for `t=7`.
