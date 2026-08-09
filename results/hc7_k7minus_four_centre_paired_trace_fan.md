# A clean fan from a paired boundary trace

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_four_centre_paired_trace_fan_audit.md`](hc7_k7minus_four_centre_paired_trace_fan_audit.md).

In the paired alternative of the minimum four-centre cut, three Kempe
connections force a much cleaner configuration: one path joins the paired
boundary vertices, while two further paths join an endpoint of the pair to
the remaining boundary vertex.  Their interiors are disjoint.  The proof
uses seven-connectivity and the minimal selected side; it does not assume
that three chosen Kempe paths have bounded intersections.

## Setting

Use the minimum trace-admissible cut and the paired alternative of the
[exact-boundary bridge reduction](hc7_k7minus_four_centre_exact_u_bridge_reduction.md):

\[
 H-T=C\mathbin{\dot\cup}D,
 \qquad N_G(C)=N_G(D)=U\mathbin{\dot\cup}T,
 \qquad T=\{p,p',q\}.                                \tag{1.1}
\]

Here `U` is an independent set of four vertices, `pp'` is a nonedge, and
`q` is adjacent to at least one of `p,p'`.  Relabel the pair so that
`pq in E(G)`.  The closed `C`-shore has an exact-`U` six-colouring in
which `p,p'` have a common colour `alpha`, and it has no exact-`U`
colouring in which `p,p',q` have distinct colours.  For three distinct
colours `lambda_1,lambda_2,lambda_3` absent from the boundary, there are
`alpha`--`lambda_i` paths from `p` to `p'` whose interiors lie in `C`.

## The clean fan

### Theorem 2.1

The graph

\[
                         G[C\cup T]-pq               \tag{2.1}
\]

contains a `p`--`p'` path and two `p`--`q` paths such that

- every internal vertex of all three paths lies in `C`;
- the two `p`--`q` paths meet only at `p,q`; and
- the `p`--`p'` path meets either `p`--`q` path only at `p`.

#### Proof

For each `i`, let `v_i` be the first internal vertex of the corresponding
`alpha`--`lambda_i` path after `p`.  Then `v_i in C`, `pv_i in E(G)`,
and the three vertices are distinct because they have the three distinct
colours `lambda_i`.

Start with `G[C union {p,p'}]` and add two new vertices `q_1,q_2`, each
adjacent precisely to `N_G(q) cap C`.  Call the resulting graph `J` and
put

\[
                         I=\{p',q_1,q_2\}.            \tag{2.2}
\]

A three-fan in `J` from `p` to `I` translates, after identifying the two
copies of `q`, into the three paths asserted in the theorem.  Thus suppose
that no such fan exists.  The fan form of Menger's theorem gives a set

\[
 W\subseteq V(J)-\{p\},\qquad |W|\le2,               \tag{2.3}
\]

such that in `J-W` the vertex `p` cannot reach any member of `I-W`.  Put

\[
 Z=W\cap C,
 \qquad
 \epsilon=\begin{cases}1,&p'\in W,\\0,&p'\notin W,\end{cases}
 \qquad
 \rho=|W\cap\{q_1,q_2\}|.                            \tag{2.4}
\]

At least one of `v_1,v_2,v_3` avoids `Z`; fix such a vertex `v`.  Let `A`
be the component of `G[C-Z]` containing `v`.  The edge `pv` makes every
vertex of `A` reachable from `p` in `J-W`.  Consequently, a neighbour of
`A` in `C` belongs to `Z`; a neighbour at `p'` is possible only when
`epsilon=1`; and a neighbour at `q` is possible only when both copies of
`q` belong to `W`.  There are no edges from `C` to `D`.  Hence

\[
 N_G(A)\subseteq
 U\cup\{p\}\cup Z
 \cup\bigl(\{p'\}\text{ if }\epsilon=1\bigr)
 \cup\bigl(\{q\}\text{ if }\rho=2\bigr).             \tag{2.5}
\]

The nonempty component `D` lies outside `A union N_G(A)`.  Since `G` is
seven-connected, (2.3)--(2.5) imply

\[
 7\le |N_G(A)|\le
 5+|Z|+\epsilon+\boldsymbol 1_{\{\rho=2\}},
 \qquad |Z|+\epsilon+\rho\le2.                       \tag{2.6}
\]

If `rho=1`, the right side of (2.6) is at most six.  It is also at most
six if `rho=2`.  Therefore

\[
                  \rho=0,\qquad |Z|+\epsilon=2,       \tag{2.7}
\]

and equality holds throughout (2.6).  In particular,

\[
 N_G(A)=
 \begin{cases}
 U\mathbin{\dot\cup}\{p\}\mathbin{\dot\cup}Z,
      &\epsilon=0,\ |Z|=2,\\
 U\mathbin{\dot\cup}\{p,p'\}\mathbin{\dot\cup}Z,
      &\epsilon=1,\ |Z|=1.
 \end{cases}                                         \tag{2.8}
\]

Thus (2.8) is an exact order-seven cut with a three-vertex part outside
`U`.  The audited two-component theorem makes `A` one of its two connected
components and places `D` in the other.  Its selected closed side is
contained in `C union U union T`; the fixed six-colouring therefore
restricts to it, all four nominated roots still avoid `A`, and the fixed
opposite root remains in `D`.  Since `Z` is a nonempty subset of `C`, one
has

\[
                         \varnothing\ne A\subsetneq C. \tag{2.9}
\]

The cut is consequently trace-admissible and contradicts the minimum
choice of `C`.  This contradiction proves the theorem.  \(\square\)

## Scope

The theorem replaces arbitrary intersections among three selected Kempe
paths by a clean fan.  It does not supply an `S`-full connected subgraph
disjoint from the fan, nor does it by itself produce the required rooted
`K_6^-` model.  Those are the remaining global uses of the configuration.

## Dependencies

- [Exact boundary traces and a bounded shore reduction](hc7_k7minus_four_centre_exact_u_bridge_reduction.md), Theorem 2.1.
- [Trace-preserving descent from a four-centre exact cut](hc7_k7minus_four_centre_trace_descent.md), especially Corollary 2.2.
- [Two-component normal form for seven-vertex cuts](hc7_k7minus_three_component_seven_cut_exclusion.md), Corollary 2.
