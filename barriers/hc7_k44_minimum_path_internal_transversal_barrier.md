# A minimum support-full path does not force the internal-support transversal

**Status.** Explicit counterexample to the local rooted-transversal claim
stated below, with a deterministic exhaustive verifier.  This graph has many
closing bonds.  It is not a counterexample to the minimum-blocker bisection
target, the literal `K_{4,4}` case of T44, T44, Conjecture 21, or `HC_7`.

## 1. Claim refuted

Let `X` be a three-connected graph with supports

\[
 R_a,R_b,E_L,E_R,F_1,F_2,F_3\subseteq V(X).
\]

Suppose the complete local hypotheses of the nonsingleton minimum-blocker
theorem hold: the seven-resource boundary inequalities and their strict
version hold, the five `K`-supports have order at least two, an eligible
vertex `p in R_a` exists, and the exact three-cut profiles hold.  Suppose in
addition that a minimum support-full bond opposite `p` has first shore

\[
 U=u_1u_2\cdots u_m,
\]

where `U` meets `R_b`, `E_L cap U={u_1}`, `E_R cap U={u_m}`,
and `F_1,F_2,F_3` are contained wholly in `U` with pairwise edge-disjoint
path hulls.

These hypotheses alone do **not** imply either

1. a bond separating `p` from a specified vertex of `R_b cap U` and
   splitting `F_1,F_2,F_3`; or
2. a three-cut of `X`.

Thus the proposed step from the sequential path intervals to a rooted
nonseparating transversal cannot be proved from the path data, connectivity,
and boundary inequalities alone.  A completion proof must additionally use
the global consequence of target-freeness that every three-support bond
confines all of `R_a union R_b` to one shore, or it must split a different
triple of supports.

## 2. Construction

Let `X` be the graph with graph6 code

```text
GEnbvw
```

on vertices `0,...,7`.  Its edges are

```text
03 04 05 07 13 15 16 17 24 25 26 27 34 36 37 46 47 57.
```

Put

\[
\begin{aligned}
R_a&=\{0,1,2,3,6\},&R_b&=\{5\},\\
E_L&=\{0,2,3,4,7\},&E_R&=\{2,4,6\},\\
F_1&=\{0,5\},&F_2&=\{1,5\},&F_3&=\{1,6\}.
\end{aligned}                                                   \tag{1}
\]

Take `p=2` and

\[
 U=\{0,5,1,6\},\qquad X[U]=0\mathord-5\mathord-1\mathord-6,
 \qquad V=\{2,3,4,7\}.                                      \tag{2}
\]

The graph is four-connected and has minimum degree four.  Direct exhaustion
over all vertex sets verifies

\[
 |N_X(W)|+|\{d:R_d\cap W\ne\varnothing\}|\ge7               \tag{3}
\]

for every nonempty `W`, with the value at least eight for every proper
connected `W` meeting both `R_a` and `R_b`.  It also verifies

\[
 |N_X(W)|+|\{R\in\{E_L,E_R,F_1,F_2,F_3\}:R\cap W\ne
 \varnothing\}|\ge6                                        \tag{4}
\]

for every nonempty proper connected `W`.  Hence all three-cut conditions
are vacuous.  The vertex `p` belongs to `R_a`, meets only `E_L,E_R` among
the five supports, and deleting it leaves every other boundary support
represented.

Both shores in (2) are connected, `U` meets all five supports and `R_b`,
and no support-full first shore opposite `p` has fewer than four vertices.
The only supports split by (2) are `E_L,E_R`, uniquely represented in `U`
at `0,6`, respectively.  The internal supports have the three single-edge
hulls

\[
 05,\qquad 51,\qquad 16.                                    \tag{5}
\]

## 3. Failure of the rooted internal transversal

Suppose a bond `(T,X-T)` placed `p=2` in `T`, placed `5` in `X-T`, and
split all three supports in (5).  Splitting `F_1={0,5}` and
`F_2={1,5}` forces `0,1 in T`; splitting `F_3={1,6}` then forces
`6 notin T`.

If `7 in T`, vertex `5` has no neighbour in `(X-T)-{5}`, so the second
shore is disconnected.  If `7 notin T`, connectivity of `T` forces both
`3` and `4` into `T`, after which vertex `6` has no neighbour in
`(X-T)-{6}`.  No such bond exists.

This failure is not a failure of the actual closing-bond theorem.  For
example, the bond

\[
             \{0,4\},\qquad V(X)-\{0,4\}                    \tag{6}
\]

has its first shore meet `R_a`, its second shore meet `R_b`, and splits
`E_L,E_R,F_1`.  The exhaustive verifier finds many further closing bonds.
The construction therefore isolates the first unsupported inference in the
proposed local path route: one cannot prescribe the three wholly-path
supports and the distinguished anchor simultaneously.

## 4. Verification

Run

```text
python3 barriers/hc7_k44_minimum_path_internal_transversal_barrier_verify.py
```

The verifier uses no third-party package.  It checks four-connectivity,
minimum degree, every boundary inequality, eligibility of `p`, minimum
support-fullness and all stated path incidences, absence of the rooted
internal-support bond, and the explicit closing bond (6).
