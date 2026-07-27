# Audit: static height-six topological-transversal barrier

**Verdict:** GREEN.

## Audited revisions

- barrier SHA-256:
  `522748a4af07fa32816a5e00d63ad8daef252541e202dfd7653143d2f658b265`;
- verifier SHA-256:
  `fec6a3f3b58c5ec572289c049becab0514271d0cb5060da830eb8188f12e390c`.

The pure-standard-library verifier ran successfully and returned `GREEN`.

## 1. Complete family and transversal number

The graph6 decoder reconstructs the stated 15-vertex, 50-edge graph and
checks it against an explicit edge list.  Exhaustive enumeration considers
every five-set for a literal `K_5` and, on every six-set, every possible
internal vertex and subdivided branch edge.  It gives exactly three literal
`K_5` supports and 48 six-vertex `TK_5` supports.

No set of order at most two meets all 51 supports, while `{0,4,12}` does.
Thus the asserted transversal number is exactly three.  Every two-set
avoids a support of order at most six.  Each displayed private pair meets
all literal `K_5` supports and avoids its displayed six-support, proving

\[
                        \theta_J(P_i)=6=\Theta_5(J).
\]

## 2. Relative kernel and support types

For each `A_i`, the displayed `P_i` is disjoint from `A_i` and meets every
member of `F_5(J) union (C-{A_i})`.  The fixed relative family has no
two-vertex transversal, so `C` is inclusion-minimal relative to the complete
literal-clique family.

The six selected subdivision witnesses have exactly three deficiency types
`(1,3,0)` and three types `(1,2,1)`.  Their subdivided branch edge is absent,
none uses `(2,2,0)`, and each displayed segment is the unique spanning
subdivision witness on its six-set, up to reversal.  The chosen private-pair
family contains disjoint pairs.

## 3. Minor exclusion and colouring

The displayed tree-decomposition bags cover every graph edge and satisfy
the running-intersection property on the displayed tree.  Their maximum
order is six, so `tw(J)<=5`, excluding a `K_7` minor.

The five displayed colour classes partition the vertex set and are
independent.  Together with a literal `K_5`, this proves `chi(J)=5`.
Deleting `{4,9,10,13}` isolates vertex `3`, so the graph is not
seven-connected.

## 4. Scope

The example validly blocks an exchange inferred only from the complete
small-topological-support family, global height six, relative criticality,
private-pair maximality, the topological split forms, and `K_7`-minor
exclusion.  It does not refute the proposed theorem for a hypothetical
minimal counterexample: the graph is five-chromatic, not seven-connected,
and lacks the contraction-critical hypotheses.  Whole-family composition
of the operation responses remains open and is correctly excluded.
