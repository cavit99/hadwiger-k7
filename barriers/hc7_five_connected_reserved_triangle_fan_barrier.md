# Five-connectivity does not reserve a connected set from a triangle fan

**Status:** written barrier/counterexample to an intermediate claim; not
separately audited.  This is not a counterexample to the five-centre
theorem, the `K_7^-` six-colour conjecture, or `HC_7`.

## Refuted statement

The following connectivity-only assertion is false:

> If `H` is five-connected and nonplanar, `w` is a vertex, `T` is a
> triangle disjoint from `w`, and `C` is a nominated connected subgraph
> disjoint from `T union {w}`, then `H-C` contains a `w`--`T` fan of order
> three.

## Construction

Take two copies of `K_8` with vertex sets

\[
                         C\mathbin{\dot\cup}L,
              \qquad    C\mathbin{\dot\cup}R,
\]

where `|C|=5` and `|L|=|R|=3`, and identify their common five-clique
`C`.  There are no `L-R` edges.  Call the resulting graph `H`.

Deleting `C` separates `L` from `R`, so `kappa(H)<=5`.  Deleting at most
four vertices leaves a vertex of `C`; that vertex is adjacent to every
remaining vertex in `L union R union C`.  Hence

\[
                              \kappa(H)=5.
\]

The graph is nonplanar.  Choose `w in L` and let `T=R`, which is a
triangle.  Every `w`--`T` path meets `C`, because `C` separates `L` from
`R`.  Consequently every `w`--`T` fan uses `C`, and no such fan exists in
`H-C`.

## Scope

The example proves only that five-connectivity and nonplanarity cannot
reserve an arbitrary connected set from a triangle fan.  It does not
satisfy the five-centre degree, colouring-response, or shore-contact
hypotheses.  Those additional hypotheses may still force a reserved fan.
In the active saturated-pair argument, any such conclusion must therefore
use those hypotheses rather than the connectivity of `G-{z,w}` alone.
