# Internal audit of five-root atom boundary incidence and crossed overlap

Audited file:
[`hc7_k7minus_five_centre_t5_atom_overlap_budget.md`](hc7_k7minus_five_centre_t5_atom_overlap_budget.md)

Audited SHA-256:

```text
16c08570bf039289f31134e1fb6f62010eff58fbb9774f2804cb093aec067260
```

**Verdict:** **GREEN.**  The atom boundary-incidence inequality, its
residual-set consequences, the whole witness-path inequality, the
crossed-overlap order-seven separation, and the unbounded numerical family
are correct under the stated minimally infeasible all-rainbow hypotheses.

This is a hash-pinned internal mathematical audit, not external peer review.
The numerical family establishes route nonclosure only; it is not a graph
construction.

## 1. Scope and pinned dependencies

| input | source SHA-256 | audit SHA-256 |
|---|---|---|
| order-fifteen atom theorem | `cef0f373ea433f72299cbc288a86274c0dae8414c8ee173c446320f01c310bab` | `9b2dd419cb244284162342e315b87904698a5ea97e51c2cb776b42a1a0becc45` |
| global five-root palette alternative | `b26f9f0d12822f93af55e3aa566fc75b985dcb5a17daa4ea2b329c8efea274c3` | `765df0db1168001a212c77e5f871abe4725d4c92cc4e11ae8d887ff808f92e6a` |
| exact boundary matching theorem | `e8c53c8255f7e6fe62b014e6909f4d12501e7994691d99e6b749ad9b2b9a3fd6` | `bb913b8a6af2aa830567c87d6350246885743195514fb6fcc1db4af49025d3ee` |
| five-centre two-cut reduction | `1917b5e3d183d44a2d905d2628272d10e4bc6f7ae0768b43cab0e9462b83332a` | `d01183c936d79ea2e07f956c2e89f7291df9cc28a5dab3dda6b093c8a69c4ea3` |

The audit independently checked:

1. the atom boundary-incidence inequality;
2. the deduction `w_z\ge4`, the `w_z=4` bounds, and the order-forty-four
   threshold;
3. the whole witness-path inequality;
4. the crossed-overlap separation; and
5. the unbounded numerical family establishing scalar-method nonclosure.

## 2. Atom boundary incidence

The planar-atom edge count gives exactly

\[
 e(R_z,U_z)=3r_z+k_z-\delta_{{\rm pl},z}
                         -q_z-\pi_z-t_z.
\]

Degree summation over `U_z`, using

\[
 e(U_z)\le k_z-1,qquad e(U_z,W_z)\le k_zw_z,
 \qquad e(U_z,\{p,q\})\le2,
\]

therefore gives

\[
e(U_z,Z)\ge
k_z(5-w_z)-3r_z+\delta_{{\rm pl},z}
+q_z+\pi_z+t_z+g(U_z).
\]

The centre `z` has a `C`-contact in `R_z`.  Each other centre has a
`C`-contact in the component of `H-P_z` containing the other four roots.
Thus every centre has a contact outside `U_z`, and

\[
                              e(U_z,Z)\le20-b.
\]

All inequality directions and constants in Theorem 2.1 follow.  The
`w_z\le2` rows are immediately too large.  At `w_z=3`, the only possible
nonsingleton parameters are `r_z=2,\rho_z=1,k_z=11`; the exact planar
identity then forces `q_z=3`, making the left side at least nineteen.
At `w_z=4`, the singleton and nonsingleton calculations give precisely the
stated bounds, including

\[
 c\le
 3\left\lfloor\frac{15+\rho_z-b}{2}\right\rfloor+24-b
 \le43.
\]

## 3. Whole-path and overlap checks

For `Q_z=V(P_z)\cap C`, the induced path has `|Q_z|-1` internal edges and
exactly two path edges to the poles.  Degree summation therefore gives

\[
                         (c-f_z)(6-f_z)+g(Q_z)\le20-b.
\]

This correctly implies `f_z\ge5`, and `f_z\ge6` for `c\ge24`.

For a component `X` of `G[R_z\cap R_w]`, the proof correctly establishes
that `X` has no centre or `D` neighbour and that its `C`-neighbourhood lies
in the three displayed crossed intersections.  The displayed boundary is
a superset of `N_G(X)`, so seven-connectivity gives it order at least
seven.  If its order is seven, it must equal `N_G(X)`, giving the claimed
exact separation.  Paths inside `L_z,L_w` give the two nonempty crossed
intersections.

## 4. Unbounded numerical family

Since vertex excess is nonnegative, `g=0` implies

\[
                         g(R_z)=g(U_z)=g(Q_z)=0.
\]

Direct substitution into the displayed family gives

\[
\begin{aligned}
 10r+5&=3r+(7r+5),\\
 2c-1+s+g&=20r+22=m,\\
 4c-23+b-g-h&=20r+10=2s,\\
 2r+8-\rho+\eta&=4r+4=k.
\end{aligned}
\]

The left side of the atom boundary-incidence inequality is

\[
                         -3r+q+t=-2r+3\le15=20-b.
\]

The corrected choice `f=r+5` gives

\[
                         |Q_z|=c-f=4r+4=k,
\]

so `Q_z=U_z` is consistent with
`U_z\subseteq Q_z\subseteq C-R_z`.  The whole-path inequality has left
side

\[
                         (4r+4)(1-r)\le0\le15
\]

for every `r\ge2`.  The scalar system is therefore genuinely unbounded.

## 5. Limitations

The numerical family is not a graph construction.  The overlap theorem
does not establish compatible boundary colourings, a prescribed minor
model, or anchored descent.

**Unresolved assumptions or gaps within the stated results:** none.
