# A `K_4`-reserve inequality at an essential-edge six-separation

**Status:** written proof; separate internal audit GREEN for the revision
identified in the adjacent audit.  This is a computation-free restriction
on a six-separation.  It does not prove the seven-connected `4n-2` target,
the auxiliary statement `(E5)`, Conjecture 21, or `HC_7`.

Throughout, `K_7^-` denotes the graph obtained from `K_7` by deleting one
edge.  In a `Z`-rooted `K^*_{4,2}` model, the four root bags are each
adjacent to two adjacent helper bags; adjacency between different root bags
is not part of the definition.

We use two existing inputs.  Norin and Totschnig, Lemma 12, proves that an
internally four-connected pair `(F,Z)` with `|Z|=4` and no `Z`-rooted
`K^*_{4,2}` model satisfies

\[
                         |E(F)|\le 4|V(F)|-10.       \tag{1}
\]

The audited
[fifth-root augmentation lemma](../active/hc7_k7minus_e5_k5minus_cut_elimination.md#lemma-1-fifth-root-augmentation)
states that, if `(F,Z\cup\{r\})` is internally five-connected, any
`Z`-rooted `K^*_{4,2}` model can be chosen with `r` in a helper bag.

## Theorem 1 (six-connected `K_4`-reserve inequality)

Let `H` be a six-connected graph with no `K_7^-` minor.  Let `S` be a
six-cut such that

\[
              H-S=A\mathbin{\dot\cup}B,
\]

where `A` and `B` are connected and every vertex of `S` has a neighbour in
each of `A,B`.  Suppose

\[
 S=Z\mathbin{\dot\cup}\{r,s\},\qquad |Z|=4,
 \qquad H[Z]=K_4.
\]

For `X\in\{A,B\}`, define

\[
 \delta_X=|E(H[X])|+|E_H(X,S)|-4|X|.
\]

Then

\[
                 \boxed{\delta_X\le |E_H(X,\{r,s\})|}.       \tag{2}
\]

### Proof

Fix `X\in\{A,B\}` and let `Y` denote the other component.

The pair `(H[X\cup Z],Z)` is internally four-connected.  Indeed, a rooted
separation of order at most three with a nonempty open side in `X`, after
adding `r,s` to its separator, would give a cut of `H` of order at most
five separating that side from `Y`.

Similarly,

\[
              (H[X\cup Z\cup\{r\}],Z\cup\{r\})
\]

is internally five-connected: a forbidden rooted separation of order at
most four, together with the omitted vertex `s`, would again give a cut of
`H` of order at most five.

Suppose that `H[X\cup Z]` has a `Z`-rooted `K^*_{4,2}` model.  Fifth-root
augmentation in the larger closed shore puts `r` in one helper bag.  The
four root bags are pairwise adjacent through the literal clique `H[Z]`,
and the two helper bags are adjacent by definition.  Hence these six bags
form a `K_6` model.  The connected opposite component `Y` is adjacent to
all four root bags and to the helper containing `r`; it may miss only the
other helper.  The seven bags therefore form a `K_7^-` model, a
contradiction.

Thus `H[X\cup Z]` has no such rooted model.  Applying (1) gives

\[
 |E(H[X\cup Z])|
 \le 4(|X|+4)-10
 =4|X|+6.
\]

Since `H[Z]=K_4`, subtracting its six edges yields

\[
                 |E(H[X])|+|E_H(X,Z)|\le4|X|.
\]

Adding the edges from `X` to `\{r,s\}` and subtracting `4|X|` proves
(2). \(\square\)

## Corollary 2 (degree sum in the primary `4n-2` programme)

Let `G` be an edge-minimal seven-connected graph with no `K_7^-` minor and
with `|E(G)|\ge4|V(G)|-2`.  Put

\[
                        q(G)=|E(G)|-(4|V(G)|-2),
\]

and let `xy\in E(G)`.  Apply the audited
[essential-edge six-separation theorem](hc7_k7minus_essential_edge_six_separation.md)
to `H=G-xy`, obtaining a six-cut `S` and its two boundary-full components
`A,B`.  Suppose `G[S]` contains a clique `Z` of order four, and write

\[
 S=Z\mathbin{\dot\cup}\{r,s\},\qquad
 t=|E_G(\{r,s\},Z)|,\qquad
 \varepsilon=\mathbf 1_{rs\in E(G)}.
\]

Then each shore satisfies (2), and

\[
 \boxed{d_G(r)+d_G(s)\ge15+q(G)+\varepsilon}.         \tag{3}
\]

so `r,s` cannot both have degree seven.  If they are adjacent, their degree
sum is at least `16+q(G)`.

### Proof

The graph `H` and its two shores satisfy Theorem 1.  The essential-edge
identity is

\[
                    \delta_A+\delta_B
                    =21+q(G)-|E(G[S])|.               \tag{5}
\]

Summing (2) over the two shores and using

\[
 |E(G[S])|=6+t+\varepsilon
\]

gives

\[
 15+q(G)-t-\varepsilon
 \le |E_G(A\cup B,\{r,s\})|.                         \tag{6}
\]

Every edge incident with `r` or `s` has its other end in
`A\cup B\cup S`, and hence

\[
 |E_G(A\cup B,\{r,s\})|
 =d_G(r)+d_G(s)-t-2\varepsilon.
\]

Substitution in (6) proves (3).  Since the density hypothesis gives
`q(G)\ge0`, the degree-seven consequence follows. \(\square\)

## Scope

The theorem turns a literal boundary `K_4` into a quantitative reserve on
the other two boundary vertices.  It does not prove that an arbitrary
essential-edge boundary contains a `K_4`, combine the restrictions from
different essential edges, or produce a density-preserving
seven-connected shore contraction.  Those are global obligations in the
primary target.

## External source

Sergey Norin and Agnès Totschnig,
[*Every graph with no `K_7^\vee`-minor is 6-colourable*, Lemma 12](https://arxiv.org/abs/2507.03244).
