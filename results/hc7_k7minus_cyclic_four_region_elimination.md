# Elimination of the cyclic four-region interaction

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_cyclic_four_region_elimination_audit.md`](hc7_k7minus_cyclic_four_region_elimination_audit.md).

This note eliminates one of the three interaction graphs left by the
four-region equality case.  The graph `C_4` cannot occur.  If the
interaction graph is `P_4`, every Boolean replacement square is based at
one of the two internal regions; in particular, the two internal regions
carry at least five unique-centre incidences between them.

The proof is unbounded and computation-free.  Its conclusion is terminal
for the eliminated cases: each forbidden configuration gives an explicit
`K_7^-`-minor model.

## 1. Setting

Let `G` be a seven-connected graph such that

\[
 \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G,
 \qquad \delta(G)\ge8.                              \tag{1.1}
\]

Let `U` be an independent set of four degree-eight vertices.  Retain the
four-region equality case of the audited
[common-colouring theorem](hc7_k7minus_common_colouring_centre_change.md).
Thus

\[
                         \mathcal P=\{C\}\cup\mathcal B,            \tag{1.2}
\]

where `|mathcal B|=4`, the five members of `mathcal P` are pairwise
disjoint connected subgraphs, `C` is anticomplete to every member of
`mathcal B`, and every member is adjacent to every vertex of `U`.  The
interaction graph `Gamma` on `mathcal B` joins two regions exactly when
they are adjacent in `G`, and

\[
                         \Gamma\in\{2K_2,P_4,C_4\}.                 \tag{1.3}
\]

For `P in mathcal P`, let `T_P` be its three-vertex auxiliary boundary and
put

\[
 W_P=\{u\in U:|N_G(u)\cap P|=1\}.                    \tag{1.4}
\]

For `u in W_P`, write `x_{uP}` for the unique neighbour of `u` in `P`.
The simultaneous-replacement theorem gives

\[
                         \sum_{P\in\mathcal P}|W_P|\ge8.            \tag{1.5}
\]

If `u,v in W_P` are distinct and `x=x_{uP}`, `y=x_{vP}`, then

\[
 R=P-\{x,y\}                                             \tag{1.6}
\]

is connected, has at least two vertices, and is a full component behind
the exact order-seven boundary

\[
 S_{uv}=(U-\{u,v\})\mathbin{\dot\cup}T_P
                  \mathbin{\dot\cup}\{x,y\}.          \tag{1.7}
\]

## 2. Three rooted bags inside a doubly replaced component

### Lemma 2.1

Let `u,v in W_P` be distinct, retain (1.6)--(1.7), and let
`r in U-\{u,v\}`.  The graph

\[
                         G[R\cup\{x,y,r\}]             \tag{2.1}
\]

contains a `{x,y,r}`-rooted `K_3`-minor model.

#### Proof

Apply the audited
[closed-shore rooted-connectivity lemma](hc7_closed_shore_rooted_connectivity.md)
to the exact separation with component `R` and boundary `S_{uv}`.  The
rooted pair in (2.1) is internally three-connected.

Suppose it has no `{x,y,r}`-rooted triangle.  The audited rooted-triangle
obstruction says that there is a vertex `z` such that every component
after deleting `z` contains at most one member of
`{x,y,r}-{z}`.  The vertex `z` cannot be a root.  Indeed, `R` is connected
and is adjacent to all three roots, so after deleting any one root the
other two lie with `R` in one component.

Hence `z in R`.  Since `|R|>=2`, some component `A` after deleting `z`
contains a vertex of `R-{z}`.  It contains at most one root.  Put

\[
                         Z=\{z\}\cup(A\cap\{x,y,r\}).                 \tag{2.2}
\]

Then `|Z|<=2`, and separating `A-Z` from the rest while retaining all
three roots on the other closed side gives a rooted separation explicitly:
if `J` denotes (2.1) and `W=A cap \{x,y,r\}`, take

\[
 X=(V(J)-A)\cup\{z\}\cup W,
 \qquad Y=A\cup\{z\}.                                \tag{2.3}
\]

Then `X cap Y=\{z\} union W=Z`, all three roots belong to `X`, and
`Y-X=A-W` is nonempty because it contains the chosen vertex of `R-{z}`.
There is no edge between the two open sides because `A` is a component of
`J-z`.  This contradicts internal three-connectivity.  Therefore the
rooted triangle exists. \(\square\)

## 3. Terminal interaction-graph reduction

### Theorem 3.1

The interaction graph `Gamma` is not `C_4`.

If `Gamma=P_4`, then

\[
 |W_C|\le1,
 \qquad |W_P|\le1
 \quad\text{for each endpoint region }P\text{ of }\Gamma.          \tag{3.1}
\]

Consequently, if `P_1,P_2` are the two internal regions of this path,
then

\[
                         |W_{P_1}|+|W_{P_2}|\ge5,                    \tag{3.2}
\]

so both sets are nonempty and at least one has order at least three.

#### Proof

We first prove a common terminal assertion.  Fix `P in mathcal P` with
distinct `u,v in W_P`, put `x=x_{uP}`, `y=x_{vP}`, and write

\[
                         U=\{u,v,r,s\}.                              \tag{3.3}
\]

By Lemma 2.1 there are three disjoint connected, pairwise adjacent branch
sets rooted respectively at `x,y,r`, all contained in
`R union \{x,y,r\}`.  Add `u` to the `x`-rooted bag and `v` to the
`y`-rooted bag.  The enlarged bags remain disjoint, connected and pairwise
adjacent.  Each is adjacent to every member of
`mathcal P-\{P\}`: the three bags contain respectively the centres
`u,v,r`, and every centre has a neighbour in every one of the five
pieces.

It remains only to choose four branch sets from `mathcal P-\{P\}` which
form a `K_4^-` model after the unused centre `s` is absorbed into one of
them.

Suppose first that `Gamma=C_4`.  If `P=C`, add `s` to any region
`B in mathcal B`.  This makes that bag adjacent to the other three, while
`Gamma-B` is a three-vertex path.  If `P in mathcal B`, add `s` to `C`;
this makes the `C`-bag adjacent to all three remaining regions, and
`Gamma-P` is again a three-vertex path.  In either case the four outer
bags are pairwise adjacent except possibly for the two ends of that path.
Together with the three pairwise adjacent inner bags, which are adjacent
to every outer bag, they form an explicit `K_7^-`-minor model.  This
contradicts (1.1).  Equation (1.5) guarantees some `P` with
`|W_P|>=2`, so `Gamma=C_4` is impossible.

Now let `Gamma=P_4`.  If `P=C`, add `s` to an endpoint region of
`Gamma`; deleting that endpoint leaves a three-vertex path.  If `P` is
itself an endpoint region, add `s` to `C`; the other three regions induce
the path obtained by deleting `P` from `Gamma`.  The same seven bags give
a `K_7^-` model in either case.  Hence no such `P` can have two members of
`W_P`, proving (3.1).

There are three pieces covered by (3.1): `C` and the two endpoint regions.
Their total contribution to (1.5) is at most three.  The two internal
regions therefore contribute at least five, proving (3.2).  Since each
`W_P` is a subset of the four-set `U`, (3.2) also gives the last assertion.
\(\square\)

## 4. Exact effect on the live residue

The four-region interaction graph is now restricted to

\[
                         \Gamma\in\{2K_2,P_4\}.                      \tag{4.1}
\]

In the `P_4` case, the Boolean square supplied by the incidence count is
not arbitrary: a square based at `C` or at an endpoint region is already
terminal, and at least five unique-centre incidences lie on the two
internal regions.  The theorem does not eliminate those internal-region
squares or the `2K_2` interaction graph, and it does not synchronize their
proper-minor colourings.

## Dependencies

- [A common colouring at several degree-eight vertices](hc7_k7minus_common_colouring_centre_change.md), Corollaries 4.1--4.3.
- [Closed-shore rooted connectivity](hc7_closed_shore_rooted_connectivity.md).
- [Rooted-triangle obstruction](hc7_exact7_rooted_triangle_portal_rank.md), Lemma 2.1.
