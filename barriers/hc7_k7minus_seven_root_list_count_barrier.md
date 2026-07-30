# Barrier: static list states at seven exceptional vertices

**Status:** written counterexample to an intermediate list-colouring claim.
It is not a `K_7^-`-minor-free critical host and does not refute the
seven-exceptional-vertices finishing theorem.

## Refuted inference

The following collection of static information does not force a colouring:

> Seven marked degree-eight vertices have `K_4`-free neighbourhoods of
> independence number three, their induced graph is `K_5`-free, the ambient
> graph is highly connected, and their lists arise from one proper
> six-colouring of the unmarked vertices.

## Counterexample

Let

\[
                             J=C_7\vee C_6
\]

be the join of disjoint cycles, and take `B` to be the seven vertices on
the `C_7` side.  Every `b\in B` has degree eight and

\[
                         J[N(b)]=2K_1\vee C_6.           \tag{1}
\]

This neighbourhood has clique number three and independence number three,
so all seven marked vertices are exceptional.  The induced graph `J[B]` is
`C_7`, hence `K_5`-free.  The join-connectivity formula gives
`kappa(J)=8`.

Two proper six-colourings of the `C_6` side exhibit the two exact static
obstructions.

1. Give its six vertices six distinct colours.  Every marked vertex then
   has an empty list, so a minimal uncolourable core can be a singleton and
   the other six marked vertices disappear from the obstruction.
2. Colour the cycle cyclically `3,4,3,4,5,6`.  Every marked vertex has list
   `\{1,2\}`.  The full induced `C_7` is then vertex- and edge-minimal
   uncolourable from these common two-element lists.

## Scope

The graph `J` is five-chromatic and is not contraction-critical; no
forbidden-minor assertion is made.  Thus it is not a counterexample to the
finishing theorem.  It proves that even degree eight, exceptionality,
neighbourhood independence three, `K_5`-freeness of the seven-root graph,
eight-connectivity, and one genuine exterior colouring state do not finish
the argument.  The missing ingredient must couple the seven different
proper-minor responses, or use Kempe and rooted-minor structure.
