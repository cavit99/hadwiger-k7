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
> \(S\) and not to \(p\); for some \(z\in S\), the vertex \(q\) is
> adjacent to \(p\) and every vertex of \(S-\{z\}\); and \(c\) is
> adjacent to \(p,z\) and at least five vertices of \(W\).  Then these
> contact conditions force an explicit `K_7^-`-minor model in the
> quotient.

This is the local abstraction arising when the selected component behind
the six-vertex boundary contains a neighbour of `p`.  The counterexample
below even makes `c` adjacent to every vertex of `W`.

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
`s_3s_4`.  Take `z=s_1`.  Add four pairwise nonadjacent vertices
`x,y,q,c`, and use exactly the following contacts:

\[
\begin{aligned}
 N_Q(p)\cap S&=\{s_0,s_2,s_3\},\\
 N_Q(x)&=N_Q(y)=S,\\
 N_Q(q)&=\{p,s_0,s_2,s_3,s_4\},\\
 N_Q(c)&=W.
\end{aligned}
\tag{2.2}
\]

Equations (2.1)--(2.2) specify all edges.  In particular, `c` sees both
`p` and `z`, as required for the selected component containing a
`p`-neighbour.  The graph has ten vertices and 27 edges.

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
partitions, 4,912 have all seven parts connected.  Among those, the
minimum number of nonadjacent branch-set pairs is two.  Hence none is a
`K_7^-`-minor model.

One partition attaining the minimum is

\[
 \{s_0,x\},\ \{s_2,y\},\ \{s_3\},\ \{s_4\},\
 \{p\},\ \{q\},\ \{c\}.
\tag{3.2}
\]

Its two nonadjacent pairs are `({s_4},{p})` and `({q},{c})`.  The
exhaustive record, including disconnected candidates, has SHA-256 digest

```text
e6f4284228d49e3143df81b07c311cb5a23a77014ac86124a3a2e3d8bb653ded
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

The graph `Q` is not an `E5` enemy and is not asserted to arise as the
quotient of one.  The example does not encode the internal structure of
the contracted components, the simultaneous family of exact cuts,
seven-connectivity, or the contraction-critical colouring hypotheses.
It therefore does not refute `E5`, `HC_7`, or a host-level argument using
any of those additional inputs.
