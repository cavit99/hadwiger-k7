# Universal four-root two-helper factorization at a remote centre

**Status:** working theorem; the normalization proof below is independent of
the no-model part of Norin--Totschnig's rooted density argument.  It uses the
same maximum-helper/minimum-root normalization as the separately written
fifth-root augmentation lemma.  The diamond consequence is terminal for a
fixed factorization, but the variation over different four-root sets remains
open.

Write `K_7^-` for `K_7` with one edge deleted.  Let `G` be a graph satisfying

\[
 \kappa(G)\ge7,\qquad |E(G)|\ge4|V(G)|,
 \qquad K_7^-\npreccurlyeq G.
\]

Let `z` be a degree-eight vertex and let `e_1,e_2` be two independent edges
remote from `z` such that

\[
                         J=G-\{e_1,e_2\}
\]

is seven-connected.  Put

\[
                         H=J-z.
\]

A `Z`-rooted `K^*_{4,2}` model consists of four disjoint connected root
bags, one containing each vertex of the four-set `Z`, and two further
disjoint connected helper bags `U,V`.  Each helper is adjacent to every
root bag, and `U,V` are adjacent.  Adjacencies between different root bags
are not part of the definition.

## Theorem 1 (universal spanning two-helper factorization)

For every four-set `Z subseteq V(H)`, there is a partition

\[
                         V(H)=Z\mathbin{\dot\cup}U\mathbin{\dot\cup}V
                                                               \tag{1}
\]

such that `H[U]` and `H[V]` are connected, `U,V` are adjacent, and each of
`U,V` is adjacent to every vertex of `Z`.

Equivalently, every prescribed four-set is the set of four singleton root
bags in a spanning `Z`-rooted `K^*_{4,2}` model.

### Proof

Deleting one vertex from the seven-connected graph `J` gives

\[
                         \kappa(H)\ge6.                         \tag{2}
\]

If `h=|V(H)|`, then remoteness of the two selected edges from `z` gives

\[
 |E(H)|=|E(G)|-2-d_G(z)\ge4(h+1)-10=4h-6.             \tag{3}
\]

In particular, `(H,Z)` is internally four-connected.  The rooted
two-helper bound of Norin--Totschnig says that absence of a `Z`-rooted
`K^*_{4,2}` model would imply

\[
                         |E(H)|\le4h-10,
\]

contrary to (3).  Fix such a model.  Among all of them, choose one for
which the helper union `U union V` has maximum order and, subject to that,
the sum of the four root-bag orders is minimum.  Write the root bags as
`R_1,...,R_4`, with root `z_i in Z` in `R_i`, and put

\[
 P_i=\{r\in R_i:r\text{ has a neighbour in }U\cup V\}.
\]

We claim that `|P_i|=1`.  Both helpers meet `R_i`, so `P_i` is nonempty.
If it contains at least two vertices, there are distinct vertices `u,v`
such that `u` meets `U` and `v` meets `V`; otherwise the two nonempty
helper-contact sets have the same singleton union.  Take a minimal tree in
`H[R_i]` containing `z_i,u,v`.  The minimum choice of the root bags makes
this tree span `R_i`.  One of `u,v`, say `u`, is a leaf different from
`z_i`.  Move `u` from `R_i` into `U`.  The enlarged helper and reduced root
bag remain connected; the old tree edge at `u` preserves the root--`U`
contact, while `v` preserves the root--`V` contact.  This enlarges the
helper union, a contradiction.

No component outside the six model bags has a neighbour in `U union V`:
such a component could be absorbed into a helper that it meets.  Therefore

\[
 Q=N_H(U\cup V)-(U\cup V)
\]

contains at most the unique member of each `P_i`, and hence `|Q|<=4`.
The helper union is connected because `U,V` are adjacent.  If a vertex lay
outside `(U union V) union Q`, then `H-Q` would have the helper union as one
component and a nonempty second component, contradicting (2).  Thus

\[
                         V(H)=(U\cup V)\cup Q.                   \tag{4}
\]

Each root `z_i` lies outside the helpers.  Equation (4) forces it to equal
the unique portal in `P_i`; it also excludes every other vertex of `R_i`.
Consequently `R_i={z_i}` for all `i`, `Q=Z`, and there is no vertex outside
the six bags.  This is precisely (1).  \(\square\)

## Corollary 2 (diamond-complement concentration)

Suppose additionally that `z` is exceptional, so `G[N_G(z)]` has no
literal `K_4`.  Let `Z` be four vertices of `N_G(z)` spanning a diamond
`K_4^-`, and let `(Z,U,V)` be any factorization supplied by Theorem 1.
Then all four vertices of

\[
                         N_G(z)-Z                              \tag{5}
\]

belong to the same helper.

### Proof

If the four vertices in (5) meet both helpers, then the singleton `{z}` is
adjacent to `U`, to `V`, and to all four singleton root bags.  The seven
sets

\[
                         \{z\},\quad U,V,\quad (\{x\}:x\in Z)
\]

are pairwise adjacent except for the unique missing edge of the diamond.
They form a `K_7^-` model, contrary to the hypothesis.  Hence (5) is
contained in one helper.  \(\square\)

## Exact scope

Theorem 1 is an unbounded, computation-free factorization theorem.  The
normalization uses an existing rooted model; it does not import the portal
conclusion from an argument which assumes that no rooted model exists.

Corollary 2 applies separately to each diamond.  Different choices of `Z`
may produce different helper partitions, so overlapping diamonds are not
by themselves contradictory.  A terminal continuation must prove a
root-exchange statement between two factorizations, or combine the forced
co-helper side with disjoint missing-edge paths in the exceptional
neighbourhood.
