# Audit: contraction and colouring deductions in the exceptional case

Date: 22 September 2026.

**Verdict: GREEN for Section 8 and the strengthened end-block inequality
in Section 6 only.** The reviewed
[working source](hc7_degree7_exceptional_construction_working.md) has
whole-file SHA-256
`cb616c3f092e28db664a8416e652c3acbd5a22ff6f15129d39e6694c946e1b51`.
No mathematical gap was found in that scope. This is a separate internal
audit, not external peer review. Older Sections 1–7 are not audited here,
apart from the specified end-block argument. The reviewer contributed
the clique strengthening of the two-owner observation during independent
derivation; its proof is explicitly checked below.

The independently reviewed version had hash
`039a9c59b8f834d038e6c892b4f4e0a8fce84f90058f7cbd98a03aa516fc5b1f`.
The later edits remove the redundant deletion-colouring argument, note
the literal K5 witnessing that bound, and append Sections 9–11. The
remaining reviewed proofs are unchanged. **Sections 9–11 were developed
after this review and are not covered by its verdict.**

## Inputs and checks

The deductions use the exact statements of
[prism normalisation](../results/hc7_two_triangle_extremal_prism.md)
at SHA-256
`8d617e35d5bc6fac0f25b5f418c6f35e976d282d883401199084e15c6d258222`
and [bipartite contractibility](../results/bipartite_contractibility_via_matroid_reduction.md)
at SHA-256
`3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`.
Their hypotheses and applications were checked; this is not another
audit of those entire source proofs. All new deductions retain the
stated original critical graph and its actual extremal helper.

- **Two owners.** The root has degree seven. A missing edge among its
  first rail vertex and two helper neighbours gives an independent
  triple with u. After contracting the star, the proper-minor colouring
  expands with that triple monochromatic. Its remaining four neighbours
  leave a sixth colour available for the root. Thus all three claimed
  edges are forced, without a non-cut assumption.

- **Three-vertex contraction.** A small cut containing the contracted
  path lifts to at most five vertices. Every resulting component must
  contain a triangle root, by the root-free boundary condition. At most
  two deleted prism vertices hit at most two rails, so an intact third
  rail connects both surviving triangle cliques. This excludes the cut.
  The four-colouring expansion is proper because the path is induced,
  u has no helper neighbours, and all outside path-neighbours avoid the
  contracted colour. Rooted models lift with all five roots retained.

- **Maximum-helper comparison.** Expanding the contraction inside either
  part preserves its connectivity and P contacts. When it lies outside
  the helper, quotient inducedness confines every path vertex's other
  neighbours to M and the two adjacent rail vertices. Every discarded
  path vertex therefore has at least two actual M-neighbours. Absorption
  gives the stated inequality. A shortest joining subpath excludes extra
  endpoint attachments; equality at m consequently produces an induced
  prism. A root seeing the entire contracted path permits a one-vertex
  joining subpath and forces the quotient maximum to be m−2.

- **Colouring lift.** In the quotient, the fibre colour differs
  from u's colour. All outside X-neighbours avoid the fibre colour.
  Recoloured vertices formed an independent colour class, and none is
  adjacent to p: its external neighbours are exactly u,r,P−{p},v;
  r,P−{p} avoid u's colour and u,v are exempted. The only remaining
  outside vertices in u's colour are harmless: u has no X-neighbour,
  and v's X-neighbours receive the other bipartition colour.
  Connectedness of E−X is never used.

- **Mandatory Kempe moves.** Criticality forces exactly six colours on
  the seven neighbours of u. If both moves within P fail, their paths
  and the four forced cross-pair paths satisfy the complete K2,3 scheme
  definition. Its five roots have distinct colours; every path
  intersection has a common target endpoint of that colour. The omitted
  root a may be internal on paths incident with b, since a is not a
  prescribed root. No other prescribed root is internal to a nonincident
  path. The entire r-colour class is absent, so the scheme lies in J.
  Rooted contractibility and the literal shore edges give the forbidden
  T-meeting K5. The symmetric moves and their reversibility follow.

- **Conditional bypass bags.** The first helper connects through b to
  the assumed connected remainder and to p_i. The second connects the
  component containing P−{p_i} to I_i through a−p_j, Z and c's first-rail
  contact. Their vertex sets are disjoint, both are Q-full, and ab
  supplies their mutual edge. With singleton Q, all five bags meet T.
  Existence of Z with the stated complementary properties is assumed,
  not deduced.

- **Strict end-block inequality.** The swap is an admissible connected
  P-full partition, including when W owns p_i. Equality would make its
  new helper maximum. Each W vertex is non-cut in E and has E-degree at
  least three, with at most the attachment vertex outside W. Hence E[W]
  has minimum degree at least two and contains a cycle. But W is
  root-free and would lie inside the three path interiors of the new
  induced prism, a forest. Equality is impossible.

## Limits

The quotient comparisons are not an induction in the original critical
class. The colouring bounds do not allocate branch sets. The Kempe rule
does not force all nine repeated pairs into one orbit, and the bypass
does not establish the required path with its complementary contacts.
The surviving owner pattern is not an actual critical-graph counterexample
or an exhaustive classification. The two-triangle case, the full
degree-seven case and HC7 remain open.
