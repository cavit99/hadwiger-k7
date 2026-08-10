# Local coordinate data do not synchronize lifted-cut colourings

**Status:** barrier/counterexample to an intermediate synchronization
claim; separate internal audit GREEN in
[`hc7_k7minus_local_coordinate_synchronization_barrier_audit.md`](hc7_k7minus_local_coordinate_synchronization_barrier_audit.md).

This odd-wheel example shows that an exact lower-order cut, adjacent lifted
cuts, a critical-edge colouring, coherent normalization, two-sided Kempe
locks and a simultaneous path coordinate do not by themselves force a
common boundary partition on either lifted cut.  It is a low-order
mechanism barrier, not a counterexample to the \(K_7^-\) six-colour
conjecture or to the proposed fixed-trace transfer trichotomy.

## 1. Construction and exact cuts

Let

\[
                         G=K_1\vee C_5,
\]

with hub \(h\), cyclic rim \(v_0v_1v_2v_3v_4v_0\), and distinguished
edge \(e=v_0v_1\).  Put

\[
 x=v_0,\qquad u=v_1,\qquad
 Q=\{v_3,h\},\qquad L=\{v_0,v_4\},\qquad R=\{v_1,v_2\}.
                                                               \tag{1.1}
\]

The graph \(G\) is three-connected and four-chromatic.  The graph
\(H=G-e\) is three-colourable, and \(H-Q\) has exactly the two full
connected components \(L,R\).  Thus \(Q\) is an exact order-two cut in
\(H\).

In \(G\), the adjacent lifted boundaries

\[
                         S_x=Q\cup\{x\},\qquad
                         S_u=Q\cup\{u\}                         \tag{1.2}
\]

are exact order-three cuts, since

\[
 \begin{aligned}
  G-S_x&=\{v_4\}\mathbin{\dot\cup}G[\{v_1,v_2\}],\\
  G-S_u&=G[\{v_0,v_4\}]\mathbin{\dot\cup}\{v_2\}.
 \end{aligned}                                                    \tag{1.3}
\]

Every component displayed in (1.3) is adjacent to every vertex of its
boundary.

## 2. The colouring obstruction

Up to permuting three colours \(\alpha,\beta,\gamma\), every proper
three-colouring \(\kappa\) of \(H\) is

\[
 \kappa(h)=\gamma,qquad
 \kappa(v_0)=\kappa(v_1)=\kappa(v_3)=\alpha,qquad
 \kappa(v_2)=\kappa(v_4)=\beta.                       \tag{2.1}
\]

Indeed, the rim of \(H\) is a five-vertex path, which must alternate in
the two colours not used at its universal neighbour \(h\).  In particular,
every three-colouring of \(G-e\) makes \(x,u\) equal, and the common
partition on \(Q\) is discrete.

The complete table of boundary partitions supplied by the two closed
shores is

\[
\begin{array}{c|c|c}
\text{boundary}&\text{closed }L\text{-shore}&\text{closed }R\text{-shore}\\
\hline
S_x&\{\{h\},\{v_3,x\}\}&\{\{h\},\{v_3\},\{x\}\}\\
S_u&\{\{h\},\{v_3\},\{u\}\}&\{\{h\},\{v_3,u\}\}.
\end{array}                                                     \tag{2.2}
\]

These are the only possibilities: after fixing the hub colour, every
relevant rim path alternates in the other two colours.  Hence neither
lifted cut has a partition realized by both closed shores, even though all
four shore colourings induce the same partition on \(Q\).

The normalized two-sided lock also occurs.  Starting with \(\kappa\),
recolour only \(u\) from \(\alpha\) to \(\beta\) on
\(G[L\cup Q\cup\{u\}]\).  The resulting intact-shore colouring has the
\(\alpha\)--\(\beta\) path

\[
                         u-x-v_4-v_3,                            \tag{2.3}
\]

whose first edge is literally \(ux\).  Under \(\kappa\), the other shore
has the corresponding path

\[
                         u-v_2-v_3.                              \tag{2.4}
\]

Finally, the three paths

\[
 v_4-x-u-v_2,qquad v_4-v_3-v_2,qquad v_4-h-v_2                 \tag{2.5}
\]

are internally disjoint.  They meet each of \(S_x,S_u\) exactly once per
path, exhaust both boundaries, and put the changing coordinate on the
literal consecutive edge \(xu\).

## 3. Refuted inference and scope

The example refutes the following intermediate claim:

> An exact lower-order cut, two adjacent exact lifted cuts, a common
> lower-cut partition with critical-edge endpoint equality, coherent
> normalized shore colourings and two-sided Kempe locks, and a simultaneous
> linkage containing the literal replacement edge force a common boundary
> partition on one lifted cut.

It does not refute a transfer theorem which also uses the seven-connected
minor-critical host, a Boolean replacement square, a fixed
minimum-side trace, or rooted-minor and strict-descent alternatives.  The
wheel has the proper \(K_4\)-minor model

\[
             \{h\},\quad\{v_0\},\quad\{v_1,v_2\},\quad\{v_3,v_4\},
\]

so it is not contraction-critical at chromatic number four.  Moreover,
the linkage (2.5) lives in \(G\), while the endpoint-equality colouring and
lower-order cut live in \(G-e\).  The smallest repair is therefore a
fixed-trace theorem which either aligns the edge-deletion colouring with
the trace defining the minimum side or returns the prescribed rooted minor
or a strict trace-admissible descent.
