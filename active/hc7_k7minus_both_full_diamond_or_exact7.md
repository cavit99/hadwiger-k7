# A rooted-diamond completion or a strict order-seven shore

**Status:** active written unbounded theorem;
[separate internal audit GREEN](hc7_k7minus_both_full_diamond_or_exact7_audit.md).
This note does not eliminate the both-full case.  It gives a computation-free terminal
alternative for two operation-generated fan supports and identifies the
exact remaining intersection obstruction.

Let `G` satisfy

\[
 \kappa(G)\ge 7,
 \qquad \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G.                         \tag{H}
\]

Let `u` be an exceptional degree-eight vertex, put `X=N_G(u)`, and suppose
that `G-N_G[u]` has exactly two components `E,F`, each adjacent to every
vertex of `X`.

## 1. Four roots in an order-eight shore

### Lemma 1.1 (rooted diamond or strict order-seven shore)

Let `Q\subseteq X` have order four.  At least one of the following holds.

1. `G[F\cup Q]` contains a `Q`-rooted `K_4^-` model.
2. There is a nonempty proper set `W\subsetneq F` and a three-set
   `C\subseteq F\cup Q` such that

   \[
             N_G(W)=C\mathbin{\dot\cup}(X-Q).         \tag{1.1}
   \]

   In particular, (1.1) is the boundary of an actual order-seven
   separation, and its open side `W` is strictly smaller than `F`.

#### Proof

First, `|F|\ge2`.  Indeed, if `F=\{f\}`, fullness gives `N_G(f)=X`.
In a six-colouring of the proper minor `G-u`, the colour of `f` is absent
from `X`; assigning that colour also to the nonadjacent vertex `u` would
six-colour `G`.

Put `J=G[F\cup Q]`.  If `(J,Q)` is internally four-connected, then
`|V(J)|\ge6`, so Jorgensen's rooted-diamond theorem gives outcome 1.

Otherwise there is a separation `(A,B)` of `J` with

\[
 Q\subseteq A,\qquad B-A\ne\varnothing,
 \qquad |A\cap B|\le3.                               \tag{1.2}
\]

Put `C=A\cap B`, `S=C\cup(X-Q)`, and let `W` be the vertex set of one
component of `G[B-A]`.  The set `W` lies in `F`.  There is no edge from
`W` to `A-B` in `J`, no edge from `F` to
`E\cup\{u\}`, and every boundary vertex outside `Q` lies in `S`.
Consequently `N_G(W)\subseteq S`.  The vertex `u` lies outside
`W\cup S`, so `S` is a vertex cut of order at most seven.
Seven-connectivity forces

\[
 |C|=3,\qquad |S|=7.                                  \tag{1.3}
\]

If `N_G(W)` were a proper subset of `S`, it would be a cut of order at
most six, again impossible.  Hence (1.1) holds.  Finally, `W\ne F`:
otherwise at least one of the four vertices of `Q` lies in `A-B`, and
fullness of `F` supplies a forbidden edge from `W` to `A-B`.  Thus
outcome 2 holds. \(\square\)

## 2. Two almost-full connected subgraphs

### Theorem 2.1 (two supports, rooted diamond, or exact separation)

Suppose `A_0,A_1\subseteq E` are disjoint connected vertex sets and are
adjacent.  Put

\[
                    m_i=|X-N_X(A_i)|.
\]

Assume

\[
                   m_0,m_1\le3,
                   \qquad m_0+m_1\le4.               \tag{2.1}
\]

Then `G` contains a `K_7^-` minor, or Lemma 1.1 returns a strict
order-seven separation whose open side is a proper subset of `F`.

#### Proof

The common boundary neighbourhood

\[
               Z=N_X(A_0)\cap N_X(A_1)
\]

has order at least four.  Choose four distinct vertices

\[
                         q_1,q_2,q_3,q_4\in Z
\]

and put `Q=\{q_1,q_2,q_3,q_4\}`.  Since

\[
               |N_X(A_i)-Q|\ge4-m_i\ge1
               \qquad(i=0,1),
\]

and (2.1) ensures that at least one of the two displayed sets has order at
least two.  Hence there are distinct vertices
`z_i\in N_X(A_i)-Q` for `i=0,1`.  Apply Lemma 1.1.  Its second outcome is
the asserted separation.  In its first outcome, let
`B_1,B_2,B_3,B_4` be the rooted diamond bags, with `q_i\in B_i`.

The seven sets

\[
 B_1,B_2,B_3,B_4,
 \qquad A_0\cup\{z_0\},\qquad A_1\cup\{z_1\},
 \qquad \{u\}                                         \tag{2.2}
\]

are pairwise disjoint and connected.  The first four have at most one
missing mutual adjacency.  Each `A_i\cup\{z_i\}` is adjacent to every
`B_j` through a literal `A_i-q_j` edge; the two such sets are adjacent by
hypothesis.  Finally, `u` is adjacent to every other bag through the six
distinct boundary roots in (2.2).  Thus the sole possible missing contact
is the one allowed inside the rooted diamond, and (2.2) is a `K_7^-`
minor model. \(\square\)

## 3. Application to operation-generated seven-fans

A clean seven-fan in `E\cup X`, with centre in `E`, determines a connected
support in `E`: take its centre and all open path interiors.  This support
is adjacent to the seven distinct boundary ends.

### Corollary 3.1 (disjoint fan supports)

Suppose two clean seven-fans in `E` have disjoint supports.  Then `G`
contains a `K_7^-` minor, or there is a strict order-seven separation inside
the opposite component `F`.  The separation leaves both literal fan
supports and all of their first edges unchanged on its far side.

#### Proof

Because `E` is connected, take a shortest path joining the two supports.
Its open interior avoids both.  Absorb that interior into one support;
the resulting supports remain disjoint and connected, become adjacent,
and retain all seven boundary contacts.  Theorem 2.1 applies.

The open side `W` returned by Lemma 1.1 is contained in `F`.  The opposite
closed side contains `E\cup X`, so the literal fan supports, first edges,
and paths are preserved.  This does not assert preservation of an entire
proper-minor colouring response.
\(\square\)

### Corollary 3.2 (two-arm intersection)

Let `A` be the support of a clean seven-fan in `E`, with centre `v`, and
let `B\subseteq E` be a connected set adjacent to at least seven vertices
of `X`.  Suppose `v\notin B`, `A\cap B\ne\varnothing`, and `B` meets the
open interiors of at most two fan paths.  Then `G` contains a `K_7^-` minor,
or there is a strict order-seven separation inside `F` preserving `B` and
the portions of the named fan on its `E`-side.

#### Proof

Let `A'` be the component of `G[A-B]` containing `v`.  Every fan arm not
met by `B` remains in `A'`, so `A'` is adjacent to at least five distinct
vertices of `X` and has boundary defect at most three.  On a met arm, the
predecessor of its first vertex in `B` belongs to `A'`; hence `A'` and `B`
are adjacent.  They are disjoint and connected.  The boundary defect of
`B` is at most one, so Theorem 2.1 applies. \(\square\)

## 4. Exact gain and limitation

This replaces a seven-graph boundary allocation in the disjoint-support
branch by one uniform rooted-minor argument.  It also shows why two
independently selected shore-rooted diamonds do not by themselves close
the both-full case: their possible missing pairs are independent, and no
operation identifies them.

For the two same-shore fan families produced by the current dynamic
colouring argument, the no-minor, no-order-seven-separation branch now has
the following exact residue:

1. every support from the first operation family meets every support from
   the second family; and
2. unless one fan centre lies in the other support, each such meeting uses
   at least three arms of the relevant fan.

Eliminating the second alternative requires an operation-coupled
intersection or uncrossing theorem.  Neither an additional boundary code
check nor two arbitrary rooted diamonds resolves it.

## Inputs

- Jorgensen's rooted `K_4^-` theorem, as stated in Lemma 10 of Norin and
  Totschnig
- [minimal root-star responses and clean fans](../results/hc7_degree8_minimal_root_star_response_reduction.md)
