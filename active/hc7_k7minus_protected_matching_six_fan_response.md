# A protected matching edge gives a six-fan or an exact order-seven response

**Status:** written proof and recorded route nonclosure.  Theorem 2.1 and
Proposition 4.2 have a separate
[internal audit](hc7_k7minus_protected_matching_six_fan_response_audit.md).
Section 5 contains deterministic finite diagnostics, not unbounded
theorems.  This note does not prove the `K_7^-` six-colour conjecture or
`HC_7`.

The protected-centre reduction leaves a selected edge `wx` inside the
branch set rooted at `w`.  The edge-deletion colouring supplies the correct
operation, but a branch-set transfer must retain every adjacency owned by
the `x`-side.  This note records the exact conclusion obtainable from a fan
starting at `x`: failure of a sixth arm is a labelled order-seven response;
six arms alone do not preserve the owned branch-set adjacencies.

## 1. Setting

Let `G` be a finite simple graph satisfying

\[
 \chi(G)>6,\qquad \kappa(G)\geq7.                    \tag{1.1}
\]

Let `u,v` be adjacent, let

\[
 N_G(u)=Q\mathbin{\dot\cup}\{v\},\qquad |Q|=7,     \tag{1.2}
\]

and put `H=G-{u,v}`.  Let `w,x\in V(H)-Q` be distinct and
`wx\in E(G)`.  Fix a proper six-colouring `c` of `G-wx` with

\[
                              c(w)=c(x).              \tag{1.3}
\]

Thus `wx` is the only monochromatic edge after it is restored.

A boundary partition on `N_G(A)` is a **rejected exterior trace on `A`**
when it is induced by a proper six-colouring of `G-A` but is induced by no
proper six-colouring of `G[A\cup N_G(A)]`.

## 2. Exact fan or separation

### Theorem 2.1 (six arms or an operation-labelled order-seven separation)

Under (1.1)--(1.3), at least one of the following holds.

1. In `H-w` there are six paths from `x` to six distinct vertices of `Q`
   such that any two of the paths intersect only at `x`.
2. There is a nonempty connected set `A\subseteq V(H)-\{w\}` containing
   `x` such that

   \[
                    N_G(A)=S\mathbin{\dot\cup}\{v,w\},
                    \qquad |S|=5.                    \tag{2.1}
   \]

   In particular, `N_G(A)` is an actual separator of order seven, the
   selected edge `wx` crosses it, and `c|G-A` induces a rejected exterior
   trace on `A`.

#### Proof

Apply the fan form of Menger's theorem in `H-w`, from `x` to `Q`.  If the
six paths exist, outcome 1 holds.  Otherwise there is a set

\[
                 S\subseteq V(H-w)-\{x\},\qquad |S|\leq5,              \tag{2.2}
\]

which separates `x` from `Q-S`.  Let `A` be the component of
`(H-w)-S` containing `x`.  Since `|Q|=7>|S|`, the set `Q-S` is nonempty
and lies outside `A\cup N_G(A)`.  Moreover `A\cap Q=\varnothing`.
Equation (1.2) therefore gives

\[
                         N_G(A)\subseteq S\cup\{v,w\}.                 \tag{2.3}
\]

This is a genuine separation: `A` is nonempty, while `u` lies on the
opposite side because it has no neighbour in `A`.  Seven-connectivity and
(2.2)--(2.3) imply

\[
             7\leq |N_G(A)|\leq |S|+2\leq7.
\]

Equality throughout gives (2.1).  The edge `wx` crosses the separation
because `x\in A` and `w\in N_G(A)`.

Deleting `A` removes the sole monochromatic edge under `c`, so `c|G-A` is
proper.  If its boundary partition were realised by a proper colouring of
`G[A\cup N_G(A)]`, a permutation of the six colour names would align the
two boundary colourings and glue them to a proper six-colouring of `G`.
This contradicts (1.1), so the trace is rejected. `\square`

The theorem retains the original selected edge and its colouring.  It does
not assert that the rejected partition extends through the intact
`A`-side; it returns the standard operation-labelled exact-seven response
interface.

## 3. What six arms give inside the protected branch set

Let `R` be a connected branch set containing `w,x` and disjoint from `Q`,
as it is when `R` is the `w`-rooted bag of a model whose seven `Q` roots
lie in distinct bags.  Let `A` now denote the component of `G[R-w]`
containing `x`.  Then `A` and `R-A` are connected: every component of
`G[R-w]` has an edge to `w`.  In outcome 1 of Theorem 2.1, truncate each
path at its first vertex outside this `A`.  The result is six paths with
interiors in `A` and six distinct ends in

\[
                             N_H(A)-\{w\}.            \tag{3.1}
\]

This is a genuine contact-multiplicity statement.  It is not an
ownership-preserving branch-set split.

To see the distinction, put

\[
 B=N_G(R-A)\cap A,
 \qquad A_L=N_G(L)\cap A                             \tag{3.2}
\]

for every foreign model bag `L` whose required adjacency to `R` is owned
entirely by `A`.  The audited multi-owner transfer theorem requires
pairwise vertex-disjoint paths inside `A`, one from every `A_L` to a
**distinct** member of `B`.  The six fan arms all start at `x\in B`.
Reversing them gives six paths with the same retained-side end `x`, so their
rank towards `B` may still be one.  If `A` owns two required labels, moving
all of `A` into either owner restores at most one of those two adjacencies.

Consequently the first unsupported inference is

\[
 \begin{gathered}
  \text{six }x\text{--}Q\text{ paths meeting only at }x
  \text{ and with distinct first exits}
 \end{gathered}
 \Longrightarrow
 \begin{gathered}
  \text{an ownership-preserving split of the }x\text{-side of }R.
 \end{gathered}                                      \tag{3.3}
\]

The failure is the common retained-side attachment `x`, not a shortage of
outside contacts.

## 4. Two related positive observations

### Proposition 4.1 (prescribing the first edge of a five-fan)

Assume additionally the critical-host hypotheses of the common
five-centre matching theorem, let `Z` be its fixed set of five independent
degree-eight centres, let `w\in Z`, and suppose that `H` is five-connected.
Let

\[
 K_w=\bigcap\{I\subseteq N_G(w): |I|=3\text{ and }I
                         \text{ is independent}\}.
\]

There is a five-fan from `w` to `Q`.  Its five first neighbours after `w`
are distinct, and at least two of them lie in `N_G(w)-K_w`.  Either may be
prescribed as the mate of `w` in the common five-centre matching while
retaining the complete punctured equality-signature cube.

#### Proof

The Fan Lemma in the five-connected graph `H` gives the five-fan.  Internal
disjointness makes its first neighbours distinct.  The exceptional
neighbourhood theorem gives `|K_w|\leq3`, so at least two first neighbours
avoid `K_w`.  The prescribed-representative theorem applies to either of
them. `\square`

This does not make the selected edge a `Q`-bag contact in a fixed lifted
kernel.  Its other end may lie in the `w`-rooted bag, and the first later
edge leaving that bag is not the selected operation.

### Proposition 4.2 (a mate-protected kernel has a quotient contact)

Let `J` be simple and three-connected.  Let `Q` be a seven-set and let
`w,x\notin Q` be distinct with `wx\in E(J)`.  Protect all nine vertices

\[
                              T=Q\cup\{w,x\}
\]

and contract `T`-legal contractible edges to a `T`-irreducible graph `L`.
Then `x` is adjacent in `L` to a member of `Q`.

#### Proof

The terminal-kernel theorem gives `|V(L)-T|\leq2`.  Suppose that `x` has no
neighbour in `Q`.  If there are at most one nonterminal vertices, then `x`
has at most two neighbours, namely `w` and that possible nonterminal,
contrary to three-connectivity.

Thus `V(L)-T=\{a,b\}` and minimum degree forces `x` to be adjacent to
`w,a,b`.  Every edge incident with `a` or `b` is `T`-legal and hence
noncontractible.  Wu's theorem gives sets `A_a,A_b` of at least four
degree-three neighbours, each incident with two contractible edges.  Those
two edges have both ends in `T`, so `A_a,A_b\subseteq T`.  The sets are
disjoint: a common member would have its two terminal edges and an edge to
each of `a,b`.  The vertex `x` belongs to neither set for the same reason.
Hence `A_a,A_b` partition the eight-set `Q\cup\{w\}` and both have order
four.  Every member of `Q\cup\{w\}` consequently has degree two in `L[T]`,
while `x` has degree one there.  The degree sum of `L[T]` is

\[
                              8\cdot2+1=17,
\]

contradicting the handshaking lemma. `\square`

On lifting, the `x`-rooted bag is adjacent to a `Q`-rooted bag.  Absorbing
the former into the latter turns the literal edge `wx` into a protected
root-to-`Q`-bag contact.  This is only a one-centre kernel.  Protecting a
second centre changes the terminal set and permits the extra neighbour
which breaks the parity proof; five-connectivity does not make separately
chosen contraction sequences or their branch bags common.

## 5. Exact finite limitations

### 5.1 A target-free quotient with six direct arms

There is a ten-vertex graph with roots

\[
                    Q=(0,2,3,4,5,6,7),\qquad w=8,quad x=9,
\]

whose adjacency bitmasks are

```text
(592, 352, 928, 704, 641, 326, 555, 540, 550, 477).
```

It has the following properties.

1. `G[Q]` contains a fixed labelled spanning
   `C_5\mathbin{\dot\cup}K_2` (and two further edges).
2. The graph is three-connected, `wx` is an edge, and `x` is adjacent to
   six distinct roots.  Thus it has six direct `x-Q` arms and the split
   `{x}|{w}` is connected on both sides.
3. It has no `K_7^-` minor.
4. It has no `Q`-rooted `K_5^-` model, even when unused non-root vertices
   may be deleted.

The deterministic
[`verify.py`](experiments/protected_matching_six_fan_response/verify.py)
checks these statements using the repository's exact deletion--contraction
minor routines.  This is an exact finite diagnostic showing that the
uncoloured data encoded in (3.3) are insufficient.  It is not classified
as a barrier to a host theorem: the graph is only three-connected and
carries no critical colouring response.

### 5.2 Correction to the historical one-contact diagnostic

The function `one_contact_quotient_family` in the historical order-nine
verifier calls a two-contact helper with `(contact,0)` or `(0,contact)`.
It therefore adds a hidden contact at the unselected protected centre.  The
reported statement that one contact closes `2,177` of the `2,252` static
survivors, leaving `75`, is not supported by that code.

A literal one-edge replay of the same rooted-composition criterion gives

\[
\begin{array}{c|cc}
Q&\text{each centre individually admits a contact}
 &\text{only one named centre admits a contact}\\ \hline
C_5\dot\cup K_2&325&102\\
C_5\text{ with a pendant }P_2&1242&204\\
C_7&334&45
\end{array}                                           \tag{5.1}
\]

Thus, in `1,901` placements, each centre individually admits some closing
contact; in `351` only one does.  There is no placement in which neither
centre works.  The adaptive existence of a good one-centre contact and the
separate two-contact zero-survivor conclusion remain intact.  The
`2,177/75` split and its derived degree-profile statements must not be
used.  The correction is a computer-assisted active diagnostic and
requires a separate audit before promotion.

## 6. Frozen residual requirement

Theorem 2.1 closes the failure of a sixth arm.  In the six-arm outcome, any
future repair would have to go beyond another contact count.  It would need
an operation-sensitive owner-circuit theorem using the colouring of `G-wx`
to prove one of:

1. distinct retained-side attachment vertices for the required owners;
2. an ownership-preserving branch-set transfer;
3. a `K_7^-` minor; or
4. an actual separation retaining `wx` and its rejected boundary trace.

The common-hub quotient in Section 5 shows that target exclusion at the
static quotient level is insufficient.  No such owner-circuit theorem is
proved here, and the fan-to-root route is frozen rather than designated as
the next proof attack.

## Dependencies

- [the terminal-kernel theorem](../results/hc7_five_terminal_rooted_fan.md);
- [the prescribed matching representative theorem](hc7_k7minus_prescribed_matching_representative_kernel_barrier.md);
- [the multi-owner portal linkage transfer](../results/hc7_multi_owner_portal_linkage_transfer.md); and
- [the exact protected-centre residue](hc7_k7minus_protected_centre_exact_kernel_residue.md).
