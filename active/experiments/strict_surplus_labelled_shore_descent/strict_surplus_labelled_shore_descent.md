# Strict-surplus labelled-shore descent campaign

**Branch:** `research/labelled-shore-descent`  
**Baseline:** `93079280ceedd5754105446e27bb76985ad8ffc0`  
**Status:** active experimental proof campaign; not independently audited.

## Target

Prove the strict-surplus extremal theorem

\[
\kappa(G)\ge7,\qquad |E(G)|\ge4|V(G)|-1
\quad\Longrightarrow\quad K_7^-\preccurlyeq G.
\]

Equivalently, prove that a minimum counterexample to the seven-connected
`4n-2` target cannot have positive surplus

\[
q(G)=|E(G)|-(4|V(G)|-2)>0.
\]

## Accepted proof route

The primary route is an unbounded, label-preserving shore descent.  It must
close under every returned operation; a merely smaller connected set is not
a valid descent unless it remains in a precisely stated recursive class.
Further finite boundary enumeration does not count as closure.

The imported audited entrance consists of:

- `results/hc7_k7minus_strict_surplus_minimal_enemy.md`;
- `results/hc7_k7minus_strict_surplus_canonical_six_boundary.md`;
- `results/hc7_k7minus_strict_surplus_labelled_separator_shore.md`;
- `results/hc7_k7minus_degree7_safe_contraction.md`;
- the exact seven-cut component-capacity and contraction theorems.

The unpromoted local terminalisation at commit
`e014fe93ad9ddf64d0544f72550ce102963b47ab` is treated as a source of
candidate lemmas only.  Its six-cut exclusion and its root-free path-shore
handoff require a fresh hostile verification before use.

## Initial live obligations

1. **High-shore closure.**  A strict labelled separator shore may satisfy
   \(\eta(C)>q+|N(C)|-4\), so whole-shore contraction loses the global
   coefficient-four threshold.  The proof must localise its excess or
   return a different density-eligible operation.
2. **Root-free closure.**  A failed eligible contraction may return a
   smaller root-free path shore.  The recursive state must retain enough
   literal model duties, far-side labels and density data to repeat the
   argument.
3. **Singleton terminal.**  A singleton shore has no proper whole-shore
   contraction.  It must yield an exact seven-cut, a legal root transfer,
   or a compatible density-safe incident contraction.

## Parallel global rank

The audited generalised safe-atom theorem shows that every strict-surplus
minimum enemy is critically seven-connected with respect to the full
family of density-safe edges and therefore has a density-safe atom of order
at most three.  This atom rank will be used only when it can be coupled
literally to the labelled-shore state; an unrelated atom or certifying cut
does not close the shore recursion.

## Round 1: hostile audit of the prior terminalisation

The proposed six-cut exclusion in the unpromoted source is not valid as
written.  If `X` is a six-cut and `A_1,A_2` are full components of
`G-X`, fullness gives each boundary vertex **at least** one neighbour in
each component.  Together with six-connectivity this does not imply

\[
\delta(G[X])\ge4.
\]

A boundary vertex may have many neighbours in the open components, so its
internal boundary degree can be small.  The same reversed inference occurs
in the three-component row.  Therefore the deductions

\[
G[X]\cong K_6-3K_2
\]

and “`G[X]` is cubic” are unsupported, and the claimed contradiction from
rooted-`K_4` density cannot be used.

A second correction is required in the path handoff.  If two components of
`G-C-Z` are selected while other components remain unassigned, a path
between the selected pair can use another component as an excursion.  Its
interior need not lie in `C`.  The correct construction must partition
**all** components into the two terminal sides before applying Menger.

Consequences:

- a density-eligible labelled-shore contraction may still fail at a genuine
  six-cut;
- the old proof of shore-contained traversals is unavailable without the
  all-component partition;
- the global recursive class must retain a six-boundary state or replace
  the invalid exclusion by a correct linkage argument.

The safe statements surviving from that source are the neighbourhood
bounds `|E(G[N(x)])|<=13`, the existence of at least five density-safe
edges incident with a reserve-blind `x`, and the elementary transfer when a
root-free detachable path owns at most one foreign model duty.

## Round 2: corrected eligible-shore closure

The six-cut need not be eliminated.  The following theorem closes every
non-singleton **eligible** shore, including the six-cut row.

### Theorem 2.1 (eligible shore: exact seven-cut, reroute, or strict descent)

Let `G` be seven-connected and let

\[
\mathcal M=(D,Q_1,\ldots,Q_5)
\]

be a `K_6` model in a subgraph of `G`.  Let `U` be one of the foreign bags.
Suppose `C\subseteq D` is nonempty and connected, contains at most one
prescribed root, and

\[
E_G(C,U)=\varnothing.
\]

Put

\[
k(C)=|N_G(C)|,
\qquad
\eta(C)=|E(G[C])|+|E_G(C,N_G(C))|-4|C|.
\]

Assume `|C|>=2` and

\[
\eta(C)\le q(G)+k(C)-4.                              \tag{2.1}
\]

Then at least one of the following holds.

1. Contracting `C` gives a proper seven-connected minor still satisfying
   the `4n-2` density threshold.
2. There is an actual order-seven cut whose vertices consist of the
   external part of a failed quotient cut and vertices of `C`.
3. There is a legal branch-set rerouting which preserves all prescribed
   roots and contacts and removes a nonempty proper connected subset of
   `C` from `D`.
4. There is a connected set `P\subsetneq C`, containing at most the same
   one prescribed root, such that
   \[
   E_G(P,U)=\varnothing
   \]
   and `N_G(P)` is an actual separator.

The fourth outcome is a strict shore-order descent in the same host.

### Proof

Contract `C` to one vertex `c`, producing `G_C`.  Exact accounting gives

\[
q(G_C)=q(G)+k(C)-4-\eta(C)\ge0.                       \tag{2.2}
\]

If `G_C` is seven-connected, outcome 1 holds.  Otherwise choose a cut

\[
X=\{c\}\cup Z,
\qquad |X|\le6,
\qquad |Z|\le5.                                      \tag{2.3}
\]

The contracted vertex belongs to every such cut, since a cut avoiding it
would also disconnect `G`.  Let

\[
\mathcal K=\mathcal C(G-C-Z).
\]

Partition the nonempty component family into two nonempty subfamilies

\[
\mathcal K=\mathcal A\mathbin{\dot\cup}\mathcal B.
\]

Treat the unions of the components in `\mathcal A` and `\mathcal B` as
the two terminal sets.  A terminal-to-terminal path may be truncated after
its last vertex in the first union and before its first vertex in the
second.  Since every component of `G-C-Z` belongs to one of the two terminal
sets, every internal vertex of the truncated path lies in `C`.

Let `lambda` be the minimum order of a separator in `C` between those two
terminal sets in `G-Z`.  Seven-connectivity gives

\[
\lambda\ge7-|Z|=:p\ge2.                               \tag{2.4}
\]

Indeed, a smaller separator `K\subseteq C` would make `Z\cup K` a cut of
`G` of order at most six.  If equality holds, `Z\cup K` is an actual
order-seven cut, giving outcome 2.

Suppose `lambda>p`.  Menger's theorem gives at least

\[
p+1\ge3                                                   \tag{2.5}
\]

pairwise vertex-disjoint terminal-to-terminal paths whose nonempty internal
parts

\[
P_1,\ldots,P_m\subseteq C
\]
are pairwise disjoint connected sets, each adjacent to both terminal sides.
For `P\subseteq D`, define its owned foreign duties by

\[
\Omega(P)=\{Q_i:\text{every }D-Q_i\text{ edge has its }D
             \text{-end in }P\}.                       \tag{2.6}
\]

The ownership sets of disjoint `P_i` are disjoint.  The bag `U` belongs to
none of them because `C` is anticomplete to `U`.  Hence the `m>=3`
ownership sets lie disjointly in the four-label set
`\{Q_1,\ldots,Q_5\}-\{U\}`.  Some `P=P_i` therefore satisfies

\[
|\Omega(P)|\le1.                                      \tag{2.7}
\]

Since there are at least three disjoint nonempty path interiors,
`P\subsetneq C`.

If `D-P` is disconnected, then `P` is connected and anticomplete to the
nonempty connected bag `U`; consequently `N_G(P)` is an actual separator.
This is outcome 4.

Assume `D-P` is connected.  If `P` contains the possible prescribed root,
then `P` itself is a smaller one-root blocker with connected complement in
`D`, again outcome 4.  Thus it remains that `P` is root-free.

If `\Omega(P)=\varnothing`, replace `D` by `D-P`.  Every model duty and
prescribed root survives.  If `\Omega(P)=\{Q_i\}`, replace

\[
D\mapsto D-P,
\qquad
Q_i\mapsto Q_i\cup P.
\]

The target bag is connected through an actual `P-Q_i` edge, an edge across
`P|(D-P)` restores the donor-target adjacency, and every other donor duty
survives.  This is outcome 3.  \(\square\)

### Corollary 2.2 (closed eligible recursion)

Theorem 2.1 applies equally to a one-root shore and to every root-free shore
returned by outcome 4.  No internal six-cut exclusion is needed.  Thus the
eligible part of the labelled-shore state is closed under strict order
descent.

The remaining global problem is exactly the high-shore/singleton entrance:
one must show that a rank-minimal shore either contains a density-safe edge
(two vertices then form an eligible shore), is a terminal singleton, or
already yields the target or a valid exact-cut descent.

## Trust boundary

No claim in this file is promoted until it is separately audited.  Every
use of an exact cut must distinguish nested from genuinely crossing cuts,
and every model transfer must retain the actual branch-set adjacencies and
root labels it claims to preserve.
