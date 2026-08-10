# Linking Boolean replacement cuts to the minimum exact cut

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_boolean_minimum_separator_linkage_audit.md`](hc7_k7minus_boolean_minimum_separator_linkage_audit.md).

This note anchors the path geometry of every Boolean replacement separator
from the four-region equality case to the distinguished minimum
trace-admissible separator.  Truncating one common seven-path family gives
a linkage in which every replacement vertex is joined to its own centre by
the literal replacement edge, every unreplaced centre is fixed, and the
remaining three boundary vertices are linked bijectively.

The note also records the exact one-coordinate colouring language.
Rejection at the cut containing the replacement vertex already implies
rejection at the adjacent cut containing the centre; these are not two
independent constraints.  What remains is fixed-trace colour
synchronization, not path-coordinate identification.

The results are unbounded and computation-free.  They do not prove the
\(K_7^{-}\) six-colour conjecture.

## 1. Setting

Let \(G\) be a seven-connected graph such that

\[
 \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G,
 \qquad \delta(G)\ge8,
 \qquad |E(G)|\ge4|V(G)|.                            \tag{1.1}
\]

Let \(U\) be an independent set of four degree-eight vertices and put
\(H=G-U\).  Retain the rooted-web outcome, fixed colouring and named
vertices, the minimum trace-admissible cut of the audited
[trace-descent theorem](hc7_k7minus_four_centre_trace_descent.md), and the
four-region equality case of the audited
[common-colouring theorem](hc7_k7minus_common_colouring_centre_change.md).
Thus the distinguished cut is

\[
 H-T=C\mathbin{\dot\cup}D,\qquad
 N_G(C)=N_G(D)=S:=U\mathbin{\dot\cup}T.               \tag{1.2}
\]

Write \(x_j\in D\) for the fixed opposite anchor retained by the
trace-admissible data.

Let \(\mathcal B\) be the four inclusion-minimal exact-cut components
inside \(D\), and put

\[
                         \mathcal P=\{C\}\cup\mathcal B.             \tag{1.3}
\]

For \(P\in\mathcal P\), let \(T_P\) be its three-vertex auxiliary
boundary and \(O_P\) its opposite component.  Put

\[
 W_P=\{u\in U:|N_G(u)\cap P|=1\},                     \tag{1.4}
\]

and, for \(u\in W_P\), write \(x_{uP}\) for its unique neighbour in
\(P\).  These replacement vertices are distinct.  For
\(R\subseteq W_P\), set

\[
 X(P,R)=\{x_{uP}:u\in R\},\qquad
 S_R=(U-R)\cup T_P\cup X(P,R).                        \tag{1.5}
\]

The set \(S_R\) is an exact order-seven cut with open sides

\[
                         P-X(P,R),\qquad O_P\cup R.   \tag{1.6}
\]

For \(P\in\mathcal B\), the exact-cut comparison theorem gives

\[
                         P\subset D,\qquad C\subset O_P.             \tag{1.7}
\]

## 2. A centre-fixed linkage to the minimum separator

### Theorem 2.1 (minimum-separator linkage)

Fix \(P\in\mathcal B\), a nonempty \(R\subseteq W_P\), and vertices

\[
                  a\in P-X(P,R),\qquad b\in C.         \tag{2.1}
\]

Every family of seven internally vertex-disjoint \(a\)--\(b\) paths
contains, after truncation, seven pairwise vertex-disjoint paths from
\(S_R\) to \(S\) with the following endpoint correspondence.

1. For every \(u\in R\), the path from \(x_{uP}\) to \(u\) is the
   literal edge \(x_{uP}u\).
2. For every \(w\in U-R\), the path from \(w\) to \(w\) is trivial.
3. The three remaining paths link \(T_P\) bijectively to \(T\).

Every nontrivial interior in this truncated linkage lies in \(D\).
Moreover, in the original seven-path family, the coordinate path through
\(x_{uP}u\) continues from \(u\) to \(b\) with every vertex after \(u\)
in \(C\).  For distinct \(u\in R\), these \(u\)--\(b\) suffixes are
internally disjoint and meet only at \(b\).

#### Proof

The simultaneous-replacement theorem gives
\(|P-X(P,R)|\ge2\), so \(a\) exists.  Equation (1.7) puts
\(b\) in \(O_P\).  The coordinate-path theorem for the Boolean family
therefore applies to any seven internally vertex-disjoint \(a\)--\(b\)
paths.  Each path meets \(S_R\) exactly once.  For \(u\in R\), its
coordinate path \(Q_u\), traversed from \(a\) to \(b\), contains
\(x_{uP}\) immediately followed by \(u\).  Every member of
\((U-R)\cup T_P\) lies on its fixed path throughout the Boolean family.

The old set \(S=U\cup T\) is also an \(a\)--\(b\) separator of order
seven: \(a\in D\), \(b\in C\), and (1.2) lists the two components of
\(G-S\).  Every path meets \(S\).  Internal disjointness makes the seven
intersections distinct, so every path meets \(S\) exactly once and those
intersections exhaust \(S\).

The path \(Q_u\) already contains \(u\in S\), so this is its unique
\(S\)-intersection.  Its \(S_R\)-intersection is \(x_{uP}\), and the
two vertices are consecutive.  For \(w\in U-R\), the fixed path contains
\(w\), which belongs to both separators, and its truncated segment is
trivial.  All four vertices of \(U\) have now been used as the old
separator intersections.  The three paths labelled by \(T_P\) must
therefore end at the three distinct vertices of \(T\).

Truncate each original path between its \(S_R\)-intersection and its
\(S\)-intersection.  Since \(a,b\) lie outside both separators, the
segments are vertex-disjoint.  After leaving \(S_R\), a path cannot return
to \(P-X(P,R)\) without meeting \(S_R\) again.  Before its first and only
meeting with \(S\), it cannot enter \(C\).  Hence every nontrivial
interior vertex of a truncated segment lies in \(D\).

Finally, the part of \(Q_u\) after its unique \(S\)-vertex \(u\) ends at
\(b\in C\) and contains no further vertex of \(S\).  It cannot have an
internal vertex in \(D\), because reaching \(C\) from that vertex would
force a second meeting with \(S\).  Thus every vertex after \(u\) lies in
\(C\).  Distinct coordinate paths are internally disjoint and have only
the common endpoints \(a,b\), proving the last assertion. \(\square\)

### Corollary 2.2 (anchoring at a selected support)

Let \(Y\) be a nonempty connected subgraph of \(G[C]\), and choose
\(b\in Y\) in Theorem 2.1.  For every \(u\in R\), truncate the
\(u\)--\(b\) suffix at its first vertex \(y_u\) in \(Y\).  Prepending
the replacement edge gives an \(x_{uP}\)--\(Y\) path through \(u\) whose
part after \(u\) has interior in \(C-V(Y)\).  The paths are pairwise
internally disjoint; two first-hit vertices can coincide only at the
common endpoint \(b\).

In the paired-trace case, \(Y\) may be chosen as the nonempty interior of
the clean fan's \(p\)--\(p'\) path.  Every Boolean coordinate based at an
opposite-side region then reaches that literal fan through its own centre,
without permuting centre labels.

#### Proof

Apply Theorem 2.1 with the chosen \(b\) and stop each suffix at its first
meeting with \(Y\).  The first-hit property places its open interior in
\(C-V(Y)\).  Distinct original paths share no internal vertex; their only
permitted common vertex is \(b\). \(\square\)

This is path anchoring, not a Boolean replacement coordinate based at
\(C\).  It does not prove \(u\in W_C\), uniqueness of the first
\(C\)-neighbour, a new replacement cut, or preservation of a colouring
trace.

### Proposition 2.3 (an entering one-missing-centre separator is terminal)

For an oriented separation \(q\) of \(H\), write \(L_q,R_q,S_q\) for
its left open side, right open side and separator.  Let

\[
 C_U(q)=\{v\in U:N_H(v)\cap L_q\ne\varnothing\ne
                         N_H(v)\cap R_q\},
 \qquad \lambda_U(q)=|S_q|+|C_U(q)|.                 \tag{2.2}
\]

Let \(p_0=(C\cup T,D\cup T)\).  Suppose that \(q\) is a proper
separation of \(H\) such that, for some \(w\in U\),

\[
 |S_q|=4,\qquad C_U(q)=U-\{w\},\qquad
 x_j\in R_q,\qquad
 C\cap L_q\ne\varnothing\ne C\cap R_q,              \tag{2.3}
\]

where \(x_j\in D\) is the fixed opposite anchor in the trace-admissible
data.  Put \(m=p_0\wedge q\) and \(j=p_0\vee q\).  Then both corners are
proper and have lifted order seven.  Exactly one is an ordinary
three-separation crossed by all four centres; the other is an ordinary
four-separation crossed by exactly \(U-\{w\}\).

More precisely:

1. If \(w\) has no neighbour in \(R_q\), then \(m\) is the
   three-separation and its lift is a strict trace-admissible exact cut
   whose selected component is \(C\cap L_q\).
2. If \(w\) has no neighbour in \(L_q\), then \(m\) is the
   four-separation.  Its minimum lift is an exact order-seven cut with
   boundary

   \[
                         (U-\{w\})\mathbin{\dot\cup}S_m,              \tag{2.4}
   \]

   selected \(H\)-component \(C\cap L_q\), and \(w\) in the opposite
   open side.  This is an exact one-missing-centre cut strictly below
   \(p_0\), though it is not an exact-\(U\) trace-admissible cut.

#### Proof

Both \(p_0\) and \(q\) have lifted order seven.  Choose
\(c\in C\cap L_q\).  Then \(c\) and \(x_j\) are common opposite anchors
for the two separations.  Fixed-anchor exact uncrossing makes \(m,j\)
proper with

\[
                         \lambda_U(m)=\lambda_U(j)=7.                 \tag{2.5}
\]

Every centre in \(U-\{w\}\) crosses both inputs and hence both corners.
The rootwise equality case of lifted-order submodularity says that \(w\),
which crosses \(p_0\) but not \(q\), crosses exactly one corner.  Since

\[
                         |S_m|+|S_j|=|T|+|S_q|=7,                    \tag{2.6}
\]

(2.5) makes the corner crossed by \(w\) have a three-vertex separator and
the other a four-vertex separator.

The open sides of the meet are

\[
                         L_m=C\cap L_q,
 \qquad                  R_m=D\cup R_q.                              \tag{2.7}
\]

If \(w\) has no neighbour in \(R_q\), then it cannot cross the join,
whose right open side is \(D\cap R_q\).  Thus it crosses \(m\), so
\(|S_m|=3\) and every centre crosses \(m\).  The minimum lift has boundary
\(U\dot\cup S_m\).  The critical-host two-component theorem makes its
two open shores full connected components.  Equation (2.3) and (2.7) give

\[
                         \varnothing\ne C\cap L_q\subsetneq C.        \tag{2.8}
\]

The selected closed side lies inside the old closed \(C\)-side, while
\(x_j\) remains in the opposite open side.  The fixed colouring and named
data therefore restrict, giving the strict trace-admissible descent in
item 1.

If \(w\) has no neighbour in \(L_q\), it cannot cross \(m\).  Hence
\(|S_m|=4\), precisely the other three centres cross \(m\), and a minimum
lift has boundary (2.4).  The centre \(w\) lies on the right: it has no
left neighbour, while it has a neighbour in \(D\subseteq R_m\) because it
crosses \(p_0\).  The two-component theorem and (2.8) give the exact cut
and strict containment asserted in item 2. \(\square\)

The Boolean cuts currently based at \(P\subset D\) are nested with
\(p_0\); they do not split \(C\).  Proposition 2.3 is therefore a terminal
criterion for a future separator returned after the coordinate enters
\(C\), not a claim that the current Boolean cut has already moved there.

## 3. The exact one-coordinate response language

Fix \(P\in\mathcal P\), \(u\in W_P\), and
\(W_0\subseteq W_P-\{u\}\).  Put

\[
\begin{aligned}
 x&=x_{uP},\\
 Q&=(U-(W_0\cup\{u\}))\cup T_P\cup X(P,W_0),\\
 L&=P-X(P,W_0),\\
 R'&=O_P\cup W_0\cup\{u\}.
\end{aligned}                                          \tag{3.1}
\]

The graph \(G-ux\) has exact order-six separator \(Q\), with components
\(L,R'\).  The adjacent order-seven boundaries are

\[
                         S_u=Q\cup\{u\},\qquad
                         S_x=Q\cup\{x\}.               \tag{3.2}
\]

Let \(\theta\) be a proper six-colouring of
\(G[L\cup Q\cup\{u\}]\), obtained by restricting a coherent colouring of
the original closed \(P\)-side.  Let \(\Pi\) be its equality partition on
\(Q\), and let \(\alpha,\beta\) be the colour types of \(x,u\),
respectively.  A type is either a named block of \(\Pi\) or an unused
palette type.

A type \(\tau\) is compatible with \(\alpha\) when, after aligning the
named colours on \(Q\) and permuting unused palette colours, endpoints of
types \(\alpha,\tau\) can receive different colours.  The incompatible
types are exactly

\[
 \operatorname{Inc}_{\Pi}(\alpha)=
 \begin{cases}
  \{B\},&\alpha\text{ is the boundary type named by }B,\\
  \{*\},&\alpha\text{ is unused and }|\Pi|=5,\\
  \varnothing,&\alpha\text{ is unused and }|\Pi|\le4.
 \end{cases}                                           \tag{3.3}
\]

Let \(\mathcal T_{R'}(\Pi)\) be the types attained by \(u\) among proper
six-colourings of \(G[R'\cup Q]\) inducing exactly \(\Pi\) on \(Q\).

### Proposition 3.1 (one substantive rejection)

The coherent partition on \(S_u\) extends through \(G[R'\cup Q]\)
exactly when \(\beta\in\mathcal T_{R'}(\Pi)\).  The coherent partition on
\(S_x\) extends through \(G[R'\cup Q\cup\{x\}]\) exactly when
\(\mathcal T_{R'}(\Pi)\) contains a type compatible with \(\alpha\).
Since \(ux\) is proper under \(\theta\), the type \(\beta\) is compatible
with \(\alpha\).  Consequently rejection at \(S_x\) already implies
rejection at \(S_u\).

If the coherent \(S_x\)-partition is rejected, then

\[
               \mathcal T_{R'}(\Pi)
                  \subseteq\operatorname{Inc}_{\Pi}(\alpha).        \tag{3.4}
\]

Thus either \(\Pi\) is absent from the opposite response language, or:

- if \(\alpha\) is a boundary type, every response gives \(u\) that same
  boundary type;
- if \(\alpha\) is unused and \(|\Pi|\le4\), no response exists; or
- if \(\alpha\) is unused and a response exists, then \(|\Pi|=5\), both
  endpoints have the unique unused type, and \(\Pi\) has shape
  \(2+1+1+1+1\).

#### Proof

Equality of the partitions on \(S_u\) is exactly equality of \(\Pi\) on
\(Q\) together with the type of \(u\).  This proves the first assertion.

The vertex \(x\) has no neighbour in \(R'\) other than \(u\).  Indeed,
\(P\) and \(O_P\) are anticomplete, while for \(w\in W_0\) the unique
neighbour \(x_{wP}\) of \(w\) in \(P\) is distinct from \(x\).
The colouring \(\theta\) already makes type \(\alpha\) proper against
\(Q\).  A colouring of \(G[R'\cup Q]\) therefore extends over \(x\) with
the coherent boundary type exactly when the type at \(u\) can be made
different from \(\alpha\).  Permuting palette colours absent from \(Q\)
gives precisely (3.3).

The edge \(ux\) belongs to the graph coloured by \(\theta\), so
\(\theta(u)\ne\theta(x)\).  Hence \(\beta\) is compatible with
\(\alpha\), proving the implication between the two rejections.  Equation
(3.4) and the first two listed consequences are immediate from (3.3).
In the last case, Proposition 4.2 of the Boolean replacement theorem gives
the displayed five-block shape. \(\square\)

### Theorem 3.2 (normalized coordinate colouring and two-sided lock)

There is a coherent closed-\(P\)-side colouring for which the
empty-language alternative in Proposition 3.1 cannot occur.

More precisely, let \(\kappa\) be any proper six-colouring of \(G-ux\).
Then

\[
                         \kappa(u)=\kappa(x)=\alpha                 \tag{3.5}
\]

for some colour \(\alpha\).  On

\[
                         A_{\varnothing}=P\cup T_P\cup U,          \tag{3.6}
\]

recolour only \(u\) with a colour \(\beta\ne\alpha\) absent from its
neighbours there, and call the resulting colouring \(\theta\).  This is a
proper six-colouring of the intact graph \(G[A_{\varnothing}]\), it is
coherent across the whole Boolean family based at \(P\), and

\[
                         \theta|Q=\kappa|Q.                         \tag{3.7}
\]

Consequently the common partition \(\Pi\) on \(Q\) belongs to the response
language of both order-six shores.  Relative to the coherent endpoint type
\(\theta(x)=\alpha\), every opposite-shore response inducing \(\Pi\)
forces \(u\) into the unique incompatible type of Proposition 3.1.

There are also two \(\alpha\)--\(\beta\) paths, one in each open side of
the \(S_u\)-separation.  Both start at \(u\) and end in \(Q\), have
nonempty open-side interiors, and are internally disjoint.  The path on
the \(L\)-side is bichromatic under \(\theta\) and starts with the literal
coordinate edge \(ux\); the path on the \(R'\)-side is bichromatic under
\(\kappa\).

#### Proof

If a six-colouring of \(G-ux\) gave \(u,x\) different colours, restoring
the edge would six-colour \(G\), proving (3.5).

Inside \(A_{\varnothing}\), the vertex \(u\) has neighbours only at its
unique \(P\)-neighbour \(x\) and at at most three vertices of \(T_P\).
The other centres are independent from \(u\).  At most four palette
colours are therefore forbidden, and one may choose an available
\(\beta\ne\alpha\).  Recolouring \(u\) is proper.  Since \(u\notin Q\)
and no other vertex was changed, (3.7) follows.  Restriction of
\(\theta\) supplies the coherent colouring at every Boolean cut, while
\(\kappa|G[R'\cup Q]\) is a proper opposite-shore colouring with the
same partition on \(Q\).  Any compatible type at \(u\) would extend over
\(x\) and glue to the coherent \(S_x\)-side, six-colouring \(G\).
Proposition 3.1 now gives the endpoint-type assertion.

It remains to prove the two paths.  On the boundary
\(S_u=Q\cup\{u\}\), the restrictions of \(\theta\) and \(\kappa\) differ
by interchanging \(\alpha,\beta\) on the singleton \(\{u\}\).
This singleton is an entire boundary two-colour component.  Properness of
\(\kappa\) gives no \(\alpha\)-coloured neighbour of \(u\) in \(Q\), and
the choice of \(\beta\) gives no \(\beta\)-coloured neighbour there.

If the full \(\alpha\)--\(\beta\) component of
\(G[L\cup Q\cup\{u\}]\) containing \(u\), under \(\theta\), met no other
boundary component, interchanging its colours would produce the
\(\kappa\)-boundary trace.  It would then glue to
\(\kappa|G[R'\cup Q]\) and six-colour \(G\), a contradiction.  A shortest
connection to another boundary component gives a path from \(u\) to
\(Q\) with nonempty interior in \(L\).  The only neighbour of \(u\) in
\(L\subseteq P\) is \(x\), so its first edge is \(ux\).

Apply the same argument in reverse to the full two-colour component of
\(G[R'\cup Q]\) containing \(u\), under \(\kappa\).  This gives the
second path with nonempty interior in \(R'-\{u\}\).  The two interiors
are disjoint because they lie in opposite open sides. \(\square\)

For \(P=C\), the colour-labelled path beginning with \(ux\) already lies
in the minimum side.  For \(P\in\mathcal B\), it lies in the old opposite
component; neither the second two-colour path nor the common seven-linkage
forces the fixed minimum-side colouring trace.

### Corollary 3.3 (a colour-labelled prefix reaches the selected support)

Suppose \(P\in\mathcal B\), and choose the common endpoint \(b\) of
Theorem 2.1 in a connected support \(Y\subseteq C\).  Reverse the
\(L\)-side path from Theorem 3.2 and concatenate it at \(u\) with the
\(u\)--\(b\) suffix from Theorem 2.1.  After truncating at the first
meeting with \(Y\), this is a simple path from a vertex of \(Q\) to \(Y\)
which:

1. has an \(\alpha\)--\(\beta\)-coloured prefix ending with the literal
   edge \(xu\);
2. passes through the named old-boundary vertex \(u\), and, apart from its
   possible \(Q\)-endpoint, its prefix has no other vertex of \(U\cup T\);
3. has its remaining open interior in \(C-V(Y)\).

Thus the named colour pair and the named Boolean coordinate reach the
clean-fan support in one literal path.  No colour assertion is made about
the suffix inside \(C\).

#### Proof

The reversed two-colour path has all open-side vertices in
\(L\subseteq P\subset D\), ends with \(xu\), and meets \(Q\) at its other
end.  The coordinate suffix after \(u\) has all vertices in \(C\).
The two pieces therefore meet only at \(u\), and their concatenation is
simple.  Corollary 2.2 gives the first-hit assertion at \(Y\). \(\square\)

## 4. Exact gain and remaining theorem

Theorem 2.1 removes the geometric base-point ambiguity: every Boolean
separator based at \(P\subset D\) has a centre-fixed linkage to the
minimum separator, and every coordinate path enters \(C\) through its
named centre.  Corollary 2.2 couples this uncoloured geometry to a selected
support of the clean fan.

It does not transport a colouring.  The coherent colouring at \(P\) lies
on the side opposite \(C\), while the \(u\)--\(C\) suffix lies on the
other side.  The clean fan was obtained from a different fixed colouring
at the minimum cut.  The replacement edge itself is absent and
monochromatic in a six-colouring of \(G-ux\), so the coordinate path is
not one of that colouring's Kempe paths.

Proposition 3.1 shows that simultaneous rejection at the adjacent cuts
must be replaced by one endpoint-language obligation.  Theorem 3.2 aligns
one order-six partition and one named two-colour pair with the literal
coordinate edge, so the locally normalized language is nonempty.  The
next theorem must either make this normalization compatible with the
fixed trace used to minimize \(C\), or force

\[
 \mathcal T_{R'}(\Pi)\cap
 \{\text{types compatible with }\alpha\}\ne\varnothing,             \tag{4.1}
\]

or convert failure into the prescribed rooted \(K_6^{-}\) minor or a
strict trace-admissible exact cut inside \(C\).  To contradict the existing
minimum choice, the returned trace must be the fixed trace used to define
\(C\), not merely a trace from an arbitrary colouring of \(G-ux\).
Proposition 2.3 shows that any returned one-missing-centre separation which
actually splits \(C\) is already terminal: exact uncrossing gives either
that fixed-trace descent or an exact transported cut below \(p_0\).

The scoped
[odd-wheel mechanism barrier](../barriers/hc7_k7minus_local_coordinate_synchronization_barrier.md)
realizes the lower-order cut, both adjacent lifted cuts, endpoint locking,
the normalized two-sided Kempe paths and the literal linkage coordinate,
but still has no common partition on either lifted cut.  It does not satisfy
the critical-host or fixed-trace hypotheses.  Its role is to rule out any
proof which uses only the local package already captured by Theorem 3.2.

The order-six boundary bound, component-excess identity,
non-double-critical endpoint pair and spanning \(K_6\) model remain
available:

\[
 \sigma=|E(G)|-4|V(G)|,
 \qquad
 \delta_Z=|E((G-ux)[Z])|+|E_{G-ux}(Z,Q)|-4|Z|
 \quad(Z\in\{L,R'\}),                                 \tag{4.2}
\]

\[
 |E(G[Q])|\le11,\qquad
 \delta_L+\delta_{R'}\ge\sigma+12,\qquad
 \chi(G-\{u,x\})=6.                                    \tag{4.3}
\]

They are not needed for the uncoloured anchoring theorem.  The excess is
unoriented and the spanning \(K_6\) model is unrooted, so neither fact alone
localizes the required structure inside \(C\).

## Dependencies

- [A common colouring at several degree-eight vertices](hc7_k7minus_common_colouring_centre_change.md), especially Theorem 3.1 and Corollaries 4.2--4.3.
- [Linked Boolean replacement cuts and critical-edge colourings](hc7_k7minus_boolean_replacement_edge_coupling.md), especially Theorems 2.1 and 4.1 and Proposition 4.2.
- [Trace-preserving descent from a four-centre exact cut](hc7_k7minus_four_centre_trace_descent.md), for the distinguished minimum cut.
- [Four independent centres: rooted model or exact-cut lattice](hc7_k7minus_four_centre_web_cut_lattice.md), for lifted-order submodularity and fixed-anchor uncrossing in Proposition 2.3.
- [Two-component normal form for seven-vertex cuts](hc7_k7minus_three_component_seven_cut_exclusion.md), for exactness of the lifted cuts in Proposition 2.3.
- [A clean fan from a paired boundary trace](hc7_k7minus_four_centre_paired_trace_fan.md), for Corollary 2.2.
- [Local coordinate data do not synchronize lifted-cut colourings](../barriers/hc7_k7minus_local_coordinate_synchronization_barrier.md), for the sharp local-mechanism limit.
