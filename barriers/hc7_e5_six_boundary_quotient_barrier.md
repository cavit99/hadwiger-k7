# Six-boundary quotient contacts do not force a `K_7^-` minor

**Status:** barrier/counterexample to an intermediate claim;
computer-assisted finite result; see the
[adjacent audit](hc7_e5_six_boundary_quotient_barrier_audit.md) for
independent verification and the exact computational trust boundary.

The dependency-free verifier is
[`hc7_e5_six_boundary_quotient_barrier_verify.py`](hc7_e5_six_boundary_quotient_barrier_verify.py).

## 1. Intermediate claim refuted

The following quotient-level claim is false.

> Let \(S\) induce \(P_3\mathbin{\dot\cup}K_2\), put
> \(W=S\cup\{p\}\), and let \(x,y,q,c\) be pairwise nonadjacent vertices
> outside \(W\).  Suppose that \(x,y\) are adjacent to every vertex of
> \(S\) and not to \(p\).  Let \(t,z\in S\) be distinct, with \(t\) of
> degree one in the graph induced by \(S\).  Suppose that \(pt\) is an
> edge, \(q\) is adjacent precisely to \(p\) and the vertices of
> \(S-\{z\}\), and \(c\) is adjacent precisely to the vertices of
> \(W-\{t\}\).  Then these contact conditions force an explicit
> `K_7^-`-minor model in the quotient.

This is the local abstraction arising when the selected component behind
the six-vertex boundary contains a neighbour of `p`.  The missing contact
`ct` is forced in the host by the equality \(N_A(t)=\{p,q\}\).

## 2. Counterexample

Let

\[
 S=\{s_0,s_1,s_2,s_3,s_4\},\qquad W=S\cup\{p\},
\]

and put

\[
 E(Q[S])=\{s_0s_1,s_1s_2,s_3s_4\}.
\tag{2.1}
\]

Thus `Q[S]` is the disjoint union of the path `s_0s_1s_2` and the edge
`s_3s_4`.  Take `t=s_3` and `z=s_1`.  Add four pairwise nonadjacent vertices
`x,y,q,c`, and use exactly the following contacts:

\[
\begin{aligned}
 N_Q(p)\cap S&=\{s_0,s_2,s_3,s_4\},\\
 N_Q(x)&=N_Q(y)=S,\\
 N_Q(q)&=\{p,s_0,s_2,s_3,s_4\},\\
 N_Q(c)&=W-\{s_3\}.
\end{aligned}
\tag{2.2}
\]

Equations (2.1)--(2.2) specify all edges.  The vertex `t=s_3` has degree
one in `Q[S]`, `p` is adjacent to `t`, and `c` sees both `p` and `z` while
missing `t` exactly.  Thus the example has the contact pattern forced by
the host relation \(N_A(t)=\{p,q\}\).  The graph has ten vertices and 27
edges.

## 3. Exclusion of a `K_7^-` minor

A `K_7^-`-minor model in a ten-vertex graph consists of seven pairwise
disjoint nonempty connected branch sets, with edges between all but at
most one pair of branch sets.  Unused vertices are allowed.

The verifier exhausts every possible model.  For each used vertex set of
order `k` from seven through ten, it enumerates every partition into seven
nonempty unlabelled parts.  The number examined is

\[
 \binom{10}{7}S(7,7)+\binom{10}{8}S(8,7)
 +\binom{10}{9}S(9,7)+S(10,7)
 =120+1260+4620+5880=11880,
\tag{3.1}
\]

where `S(k,7)` is a Stirling number of the second kind.  Of these
partitions, 4,873 have all seven parts connected: respectively 120, 756,
1,988, and 2,009 for used vertex sets of orders seven, eight, nine, and
ten.  Among those, the minimum number of nonadjacent branch-set pairs is
two.  Hence none is a `K_7^-`-minor model.

One partition attaining the minimum is

\[
 \{s_0,x\},\ \{s_2,y\},\ \{s_3\},\ \{s_4\},\
 \{p\},\ \{q\},\ \{c\}.
\tag{3.2}
\]

Its two nonadjacent pairs are `({s_3},{c})` and `({q},{c})`.  The
exhaustive record, including disconnected candidates, has SHA-256 digest

```text
3f94261a42cdadf57a2b55576d9cd2ce9bd3a173eceebe5fef0d553cf294ff67
```

under the canonical encoding documented by the verifier.

Run

```text
python3 barriers/hc7_e5_six_boundary_quotient_barrier_verify.py
```

to reconstruct the graph, repeat the exhaustive search, and check the
digest.

## 4. Exact scope

This example refutes only the proposed inference from the six-boundary
quotient contacts to a `K_7^-` minor.  It shows that contracting the four
relevant components to `x,y,q,c` loses too much information to close the
`s=4` case by this contact pattern alone.

The host-level theorem nevertheless closes the `s=4` case: it uses the
high-excess information retained inside the component represented by `c`,
not merely that component's contacts with `W`.  That information is absent
from this quotient, so the theorem and this barrier are compatible.

The graph `Q` is not an `E5` enemy and is not asserted to arise as the
quotient of one.  The example does not encode the internal structure of
the contracted components or their excess, the simultaneous family of
exact cuts, seven-connectivity, or the contraction-critical colouring
hypotheses.  It therefore does not refute `E5`, `HC_7`, or the host-level
`s=4` theorem.
