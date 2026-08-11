# Three pole-incident centres cannot share one rainbow contact triangle

**Status:** written proof; separate hash-pinned internal audit **GREEN** in
[`hc7_k7minus_five_centre_common_rainbow_triangle_elimination_audit.md`](hc7_k7minus_five_centre_common_rainbow_triangle_elimination_audit.md).
This is a terminal subcase of the all-rainbow `t=5` row.  It does not
eliminate configurations in which no three pole-incident centres have the
same `D`-contact triangle.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Use the hypotheses and notation of the audited
[global five-root palette alternative](hc7_k7minus_five_centre_t5_global_palette.md).
Thus

\[
 S=Z\mathbin{\dot\cup}\{p,q\},\qquad |Z|=5,
\]

`G-S` has connected full components `C,D`, the permitted response on `C`
has `p=q`, and the permitted response on `D` has `p!=q`.  Both full rooted
instances are infeasible, and deleting any one root makes the corresponding
instance feasible.  Every centre has at least two contacts on each shore.

Fix the permitted colouring `phi_D` of the closed `D`-shore used in the
all-rainbow row, and name its boundary colours by

\[
 \phi_D(Z)=\alpha,\qquad
 \phi_D(p)=\beta,\qquad
 \phi_D(q)=\delta.
\tag{1.1}
\]

Put

\[
                     \Gamma=[6]-\{\alpha,\beta,\delta\}.
\tag{1.2}
\]

Every rainbow centre `z` has `N_D(z)` equal to a triangle whose three
vertices receive the three colours in `Gamma`.  A pole-incident rainbow
centre has the exact profile

\[
                         (c_z,d_z,\rho_z)=(4,3,1).
\tag{1.3}
\]

We also use Lemma 3.3 of the active
[synchronized-path theorem](hc7_k7minus_five_centre_distance_one_paths.md):
if a triangle lies in a component left in a rooted-infeasible shore by the
interior of a pole-to-pole path, then three vertex-disjoint paths join its
vertices to three distinct vertices of that pole path, with all open
interiors in the component.

## 2. The terminal common-triangle theorem

### Theorem 2.1

There do not exist three distinct pole-incident rainbow centres
`z_1,z_2,z_3 in Z` with

\[
                         N_D(z_1)=N_D(z_2)=N_D(z_3).
\tag{2.1}
\]

#### Proof

Suppose otherwise, and write the common contact triangle as

\[
                         T=\{t_1,t_2,t_3\}.
\tag{2.2}
\]

In the colouring `phi_D`, the usual response obstruction gives a
`beta`--`delta` path `R` from `p` to `q` whose open interior lies in `D`.
The vertices of `T` have the three colours in `Gamma`, so

\[
                         V(R)\cap T=\varnothing.
\tag{2.3}
\]

The triangle `T` therefore lies in one component `A` of
`G[D-V(R)^\circ]`.  Apply the prescribed-triple fan lemma quoted in
Section 1.  There are pairwise vertex-disjoint paths `L_1,L_2,L_3`, where
`L_i` joins `t_i` to a vertex `r_i in V(R)`, the three vertices `r_i` are
distinct, and every internal vertex of `L_i` lies in `A`.  Put

\[
                         B_i=V(L_i)-\{r_i\}.
\tag{2.4}
\]

Then `B_1,B_2,B_3,V(R)` are four pairwise disjoint connected sets.  The
triangle edges make the three `B_i` pairwise adjacent, and the last edge
of each `L_i` makes `B_i` adjacent to `V(R)`.

For each `i`, equation (1.3) gives

\[
                         |N_C(z_i)|=4.
\tag{2.5}
\]

The three four-sets `N_C(z_i)` have distinct representatives
`x_i in N_C(z_i)`: Hall's condition is immediate, because the union of
any nonempty subfamily has order at least four, while the family has only
three members.  Since `C` is connected, the
[terminal-respecting tree contraction lemma](../results/hc7_k7minus_distinct_miss_fan_tree_elimination.md#3-fan-trees-in-the-two-exterior-components)
gives pairwise disjoint connected subgraphs
`Q_1,Q_2,Q_3` of `C`, with `x_i in Q_i`, whose contact graph contains a
tree on the three labels.  Define

\[
                         A_i=Q_i\cup\{z_i\}.
\tag{2.6}
\]

Each `A_i` is connected, and the three sets are pairwise disjoint.  Their
contact graph has at most one missing edge, because it contains a tree on
three vertices.

We now verify all remaining adjacencies among the seven bags

\[
              A_1,A_2,A_3,\quad B_1,B_2,B_3,\quad V(R).
\tag{2.7}
\]

Every `z_i` is adjacent to every vertex of the common triangle `T`, so
`A_i` is adjacent to every `B_j`.  Each `z_i` has one pole neighbour, and
both poles belong to `V(R)`; hence every `A_i` is adjacent to `V(R)`.
The four bags on the right of (2.7) are pairwise adjacent by the preceding
fan construction.  Thus all pairs of bags in (2.7) are adjacent except
possibly one pair among `A_1,A_2,A_3`.  They form a `K_7^-` minor model in
`G`, a contradiction.  \(\square\)

## 3. Exact consequence and scope

Let the pole-incident rainbow centres be grouped by their literal
`D`-contact triangle.  Theorem 2.1 proves that every group has order at
most two.  In particular, the `b=5` row requires at least three distinct
contact triangles, and any three same-pole centres supplied by pigeonhole
cannot all use one triangle.

The proof does not require the three centres to use the same pole: the
single path bag `V(R)` contains both `p` and `q`.  It also does not assert
that two equal contact triangles are terminal.  With only two centres, the
connected `C`-side supplies one adjacency between their enlarged bags but
does not create the three-bag tree whose sole possible missing edge is
allowed in (2.7).

The theorem spends the exact features of the all-rainbow row: three free
colours keep the contact triangle disjoint from the pole-coloured path,
pole incidence makes every centre bag adjacent to that path bag, and four
`C`-contacts give the simultaneous distinct representatives.  A generic
triangle fan without those three facts does not yield the displayed
minor.

## Dependencies

- [global five-root palette alternative](hc7_k7minus_five_centre_t5_global_palette.md),
  especially the exact all-rainbow profiles;
- [five-centre two-cut reduction](../results/hc7_k7minus_five_centre_two_cut_reduction.md),
  for the distinct-response pole path and rooted infeasibility; and
- [synchronized Kempe paths](hc7_k7minus_five_centre_distance_one_paths.md),
  Lemma 3.3;
- [terminal-respecting tree contraction](../results/hc7_k7minus_distinct_miss_fan_tree_elimination.md#3-fan-trees-in-the-two-exterior-components),
  Lemma 4.
