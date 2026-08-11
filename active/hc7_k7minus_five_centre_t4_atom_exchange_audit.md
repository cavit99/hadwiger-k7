# Internal audit of the four-root atom and exchange reduction

Audited file:
`active/hc7_k7minus_five_centre_t4_atom_exchange.md`

Audited SHA-256:

```text
42a8fab66b2396880f479fe600a03c57a568ef121925b45d0989ae5f47494f0d
```

**Verdict:** **GREEN.**  The scalar exchange, the literal planar-atom
construction, the exact deficit identity, the singleton contact table, and
the stated trichotomy are correct under the standing cited inputs.  No
unresolved gap remains in the audited derivation.  None of the three outcomes
is terminal for the `K_7^-` target under the results presently invoked.

This is a hash-pinned internal mathematical audit, not external peer review.
Relative to the theorem revision originally checked, the source changes
only its audit-status metadata; no theorem or proof text changed, so the
GREEN verdict is retained.

The constructive source checked was the gzip-compressed TeX supplied at
`/private/tmp/dly.tar`.  Its compressed SHA-256 is

```text
27ae988f5bfcb98293fd319d95c8ac15a2153303677dbc7a8c2ced026e5bea46
```

and the decompressed `main.tex` SHA-256 is

```text
4121fc964080272ae5d7df2641ad2118ded38973561e2a2737392284a8f88ddd
```

## 1. Audit scope and dependencies

The audit checks the deductions in the pinned revision, including their use
of the constructive proof of Du--Li--Xie--Yu, Theorem 1.2.  It takes as inputs
the cited five-centre two-cut reduction, the pair and three-root feasibility
results, the four-root palette transfer, seven-connectivity, and the audited
exceptional-neighbourhood conclusion
`\alpha(G[N(z)])=3` together with literal `K_5` exclusion.  Those upstream
results are not re-audited here.

In the decompressed source, the relevant construction is at lines 469--603:
the maximal component and induced pole path at 469--473, the Seymour quotient
and its lift at 480--555, critical feasibility at 560--574, and the critical
density/decomposition calculation at 579--603.  The repaired proof now
re-establishes, in the present host, the property used at source line 493;
it no longer imports a conclusion available only inside the source's
minimal-counterexample induction.

## 2. Scalar exchange

If `T=Z-\{j\}` is infeasible, every proper subset of `T` is feasible by the
standing hypothesis, so `T` is inclusion-minimal.  Direct subtraction gives

\[
 \begin{aligned}
 \sigma_j-s
 &=\left(5c+1-m-h-\sum_{z\ne j}c_z\right)
   -\left(6c+1-m-h-\sum_zc_z\right)\\
 &=c_j-c.
 \end{aligned}
\]

Thus `\sigma_j=s-c+c_j=c_j-a`, as asserted.  The proof of (2.4) also checks:
after the root and pole colours are aligned, the colour of `j` is either the
safe root colour or one of four freely permutable colours.  At most three
contacts cannot occupy all four free colours, so a permutation glues the two
shore colourings.

## 3. Literal atom construction

Fix `z\in T`.  Minimality supplies a feasible three-root instance after
deleting `z`.  Maximizing the component `L_z` containing the restored `z`
over induced `p`--`q` witness paths is exactly the specialization of the
source construction.  Its attachment set satisfies

\[
 N_H(L_z)\subseteq U_z\cup\{p,q\},
 \qquad U_z\subseteq V(P_z)\cap C.
\]

Let `K_z` be the component off `z\cup P_z` containing the other three roots
and contract it to `a^*`.  A linkage pair for
`(H^*,\{a^*,z\},p,q)` expands through the connected `K_z` to a forbidden
four-root linkage pair in `H`; hence the contracted instance is infeasible.
Seymour's theorem gives a collection whose quotient has boundary order
`z,p,a^*,q`.

The repaired lifting argument is sufficient and was checked in both cases.

1. Every collection member `Y` sees `a^*`.  Otherwise `Y` is a nonempty
   terminal-avoiding subset of `C` with `|N_H(Y)|\le3`.  In `G` it can gain
   only the omitted centre `r`, so its neighbourhood has order at most four
   and separates it from the nonempty opposite shore, contradicting
   seven-connectivity.

2. If a connected member meets `P_z`, the first and last edges by which it
   meets the induced path give two distinct path-direction neighbours.
   Together with `a^*`, these exhaust its at most three neighbours.  It
   cannot also meet `L_z`: since `z\notin Y` and `L_z` is connected, a
   component of `Y\cap L_z` has a neighbour in `L_z-Y`, which would be a
   fourth neighbour.  Nor can it meet `U_z` without meeting `L_z`, because
   each vertex of `U_z` has a neighbour in `L_z`, again producing a fourth
   neighbour.  Thus a member meeting the path avoids `L_z\cup U_z`.

3. If a connected member misses `P_z` but meets `L_z`, its adjacency to
   `a^*` gives an `a^*`--`L_z` path through that member.  The two endpoints
   lie in different components off `P_z`, so the path must meet `P_z`, a
   contradiction.

Therefore no collection member meets the literal atom.  Compressing only
the members that meet the pole path preserves the order of `U_z`; the disc
region bounded by that path and the boundary arc through `z` contains
`L_z` and every edge incident with it.  The uncontracted `A_z^+` is therefore
disc-planar with boundary order `p,U_z,q,z`.  Adding the `2k_z+1`
noncrossing edges from the source and applying Euler's formula yields

\[
 e(A_z^+)\le3v(A_z)-7-2k_z.
\]

This closes the only blocking gap in the preceding audited revision.

## 4. Critical complement and exact identity

For `H_1=H-L_z`, maximality of `L_z` gives critical feasibility with
respect to `U_z`, exactly as at source lines 560--574.  A member of the
critical theorem's collection lies in `C`, has `H_1`-neighbourhood of order
at most five, and is disjoint from `U_z\cup\{p,q\}`.  Since
`N_H(L_z)\subseteq U_z\cup\{p,q\}`, it gains no neighbour in `L_z`; in the
whole graph it can gain only the omitted centre `r`.  Its neighbourhood
would have order at most six and separate it from the opposite shore.
Seven-connectivity therefore makes the collection empty, giving

\[
 e(\mathcal G_1)\le5v(H_1)-15-k_z.
\]

Define the two nonnegative integer deficits by

\[
 \begin{aligned}
 \delta_{\rm pl,z}&=3v(A_z)-7-2k_z-e(A_z^+),\\
 \delta_{\rm crit,z}&=5v(H_1)-15-k_z-e(\mathcal G_1).
 \end{aligned}
\]

The completed terminal graph has fourteen edges, so the restricted slack is
`\sigma_r=R_4-e(\mathcal G)`.  The exact decompositions are

\[
 \begin{aligned}
 e(\mathcal G)&=e(\mathcal G_1)+e(A_z^+)+3,\\
 v(H)&=v(H_1)+v(A_z)-k_z-2.
 \end{aligned}
\]

The three extra edges join `z` to the other three roots.  Also
`v(A_z)=r_z+k_z+3`.  Substitution, with no inequality discarded, gives

\[
 \begin{aligned}
 R_4-e(\mathcal G)
 &=2\bigl(v(A_z)-k_z-3\bigr)
   +\delta_{\rm pl,z}+\delta_{\rm crit,z}\\
 &=2r_z+\delta_{\rm pl,z}+\delta_{\rm crit,z}.
 \end{aligned}
\]

Thus the coefficient `2`, both deficits, and the absence of an additional
boundary term are all verified.

## 5. Singleton table and trichotomy

If `r_z=0`, then `L_z=\{z\}` and every `C`-contact of `z` lies on the
induced path `P_z`.  Hence

\[
 \alpha(G[N_C(z)])\ge\left\lceil c_z/2\right\rceil.
\]

The `C`- and `D`-contact sets are anticomplete, while
`\alpha(G[N(z)])=3`.  This gives `c_z\le4`.  If two `C`-contacts were
nonadjacent, or if there were three or four path contacts, their independent
pair would force `N_D(z)` to be a clique.  Literal `K_5` exclusion bounds
that clique by three; the degree-eight identity then gives every row of
Lemma 3.2.  No case is missing.

For a bad omission `j` with `c_j\le3`, the exchange identity gives
`a\le c_j\le3`.  If `a\le1`, substitution in (1.5) gives
`e(C)=3c-a-1+g\ge3c-2+g`.  If `a\in\{2,3\}`, then
`0\le\sigma_j=c_j-a\le1`; the atom identity forces `r_z=0` for every
selected root, and the singleton table gives outcome 3.  Outcome 1 is the
complementary case.  This verifies Theorem 4.1 exhaustively.

## 6. Terminal scope

The note correctly labels all three outcomes as nonclosures.  The density
outcome supplies only an unrooted `K_5` minor in `C`; it does not align five
branch sets with the boundary.  A rooted `K^*_{4,2}` model does not repair
this by itself, because its four root bags need not be pairwise adjacent.
The singleton atoms constrain four separately chosen induced paths without
synchronizing them.  Therefore this `t=4` consequence is not terminal for
the `K_7^-` target.
