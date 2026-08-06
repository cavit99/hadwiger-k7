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

## Trust boundary

No claim in this file is promoted until it is separately audited.  Every
use of an exact cut must distinguish nested from genuinely crossing cuts,
and every model transfer must retain the actual branch-set adjacencies and
root labels it claims to preserve.
