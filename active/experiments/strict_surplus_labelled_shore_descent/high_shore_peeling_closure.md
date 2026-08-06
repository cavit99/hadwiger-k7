# Non-singleton high shores are not terminal

**Status:** experimental computation-free proof; independent audit pending.

This note supersedes treating the numerical high-shore alternative as a
separate infinite branch.  It uses the broader labelled-shore state from
the corrected eligible recursion, which does not require the complement of
the selected shore inside the donor bag to remain connected.

Let

\[
\mathcal M=(D,Q_1,\ldots,Q_5)
\]

be the selected `K_6` model, let `U` be a named foreign bag, and let
`C subseteq D` be nonempty and connected.  Assume

\[
E_G(C,U)=\varnothing,
\]

and that `C` contains at most one prescribed root.  Put

\[
k(C)=|N_G(C)|,
\qquad
\eta(C)=|E(G[C])|+|E_G(C,N_G(C))|-4|C|.
\]

## Theorem 1 (high-shore peeling)

If `|C|>=2`, then there is a strict connected subset

\[
C'\subsetneq C
\]

which is still anticomplete to `U` and contains at most the same one root.
Consequently repeated peeling reaches one of the following in finitely many
steps.

1. A non-singleton contraction-eligible shore, to which the corrected
   eligible-shore theorem applies.
2. A singleton shore.

In particular, a non-singleton high shore is never a terminal of the
labelled-shore recursion.

### Proof

Every connected graph of order at least two has a vertex `v` which is not
a cutvertex.  Put

\[
C'=C-\{v\}.
\]

Then `C'` is nonempty and connected.  Since `C' subseteq C`, it is
anticomplete to `U` and contains at most one prescribed root.  The named
bag `U` lies outside `C' union N(C')`, so `N(C')` is an actual separator.

The numerical alternatives

\[
\eta(C')\le q(G)+k(C')-4
\]

and

\[
\eta(C')>q(G)+k(C')-4
\]

are exhaustive.  In the first case `C'` is contraction-eligible; if it is
non-singleton, apply the corrected eligible-shore theorem, and if it is a
singleton, outcome 2 has been reached.  In the second case repeat the same
operation on the strictly smaller connected set `C'`.

Order decreases at every high step, so the process terminates.  `\square`

## Exact edge accounting for one peel

Although not needed for termination, the change in excess is explicit.
Let

\[
r=d_{G[C]}(v),
\]

and let `a` be the number of old boundary vertices whose only neighbour in
`C` is `v`.  Then

\[
k(C')=k(C)-a+1,
\]

and

\[
\eta(C')=\eta(C)+4-(d_G(v)-r).                       \tag{2.1}
\]

Thus, for the high slack

\[
h(C)=\eta(C)-(q(G)+k(C)-4),
\]

one has

\[
h(C')=h(C)+3-(d_G(v)-r)+a.                          \tag{2.2}
\]

The proof of Theorem 1 deliberately does not require this slack to be
monotone: either sign of `h(C')` is useful.

## Consequence for the campaign

The local labelled-shore machine now has only two genuine unresolved
handoffs:

- a singleton shore; and
- an exact order-seven cut returned by equality in the failed-contraction
  linkage.

The earlier `q=1,2` unsafe-edge and low-degree-spine results remain valid
structural descriptions, but they are no longer required to terminalise a
non-singleton high shore.  They may still be useful when analysing the
singleton and exact-cut endpoints.
