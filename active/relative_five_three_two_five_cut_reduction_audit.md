# Audit of the relative three--two five-cut reduction

Date: 12 September 2026.

**Current verdict: GREEN** for the reduction, three-component exclusion
and inner port coverage, with the full target still open.
**Current source SHA-256:**
`89217494d2bc1d72b420e56f65f0635e1683d34c2c615d23caa0aa8ee705826f`.

## Initial reduction audit

**Verdict: GREEN** for the stated minimum-counterexample reduction and
three-component exclusion, not for the conjectural linkage target.
The [source](relative_five_three_two_five_cut_reduction.md) has SHA-256
`468aab55fe3b21f5a6c491714eba19e36ceba5f620b3a847471527824373a5eb`.
The final reviewed revision was
`e0efb4c5437556a891a15ef8841880eb05e9ec5e04fabae1c094ca981cd2999c`;
only its status paragraph changed afterwards. Reversing the author's two
reference/scope corrections exactly recovers the earlier reviewed
`74804cc090498caaed384eaa435d7b76efe72f4bf6dc98177c38cef96dbfea0b`.

The strongest induction and lifting checks were:

- Maximal connected X gives every nonroot port two exterior neighbours;
  the exceptional enlargement to all D would create a forbidden thin root.
  Both the completed outer graph and the inner graph retain their exact
  degree/boundary hypotheses and have strictly fewer nonroots. A residual
  single nonroot is impossible by the retained degree bound.
- Inner minimality is used for complete three--two partitions of all five
  ports. The two outer carriers' port sets extend to such a partition, or
  one uses at least four ports and can absorb all X. The simultaneous lift
  preserves disjointness and every original root label; it does not assume
  that arbitrary virtual clique edges have compatible individual lifts.
- The further contractions preserve the original induction class. They
  yield two-connectivity after deleting V, disjoint V-neighbourhoods, and
  the stated root-neighbour normalisations. No colouring is retained or
  required by this induction.
- The unordered two-path argument uses a connected nonroot component of
  order at least two; the singleton star exception is excluded by the
  disjoint V-neighbourhoods. The auxiliary p,q identification needs no
  connected preimage: a positive linkage truncates at its actual final
  port, which is enough for the contrapositive application.
- The two cofacial inequalities give the displayed port-coverage and
  opposite-assignment bounds. Their thin-root cases use all side nonroots,
  so the asserted small boundaries are actual boundaries. The resulting
  paths assemble in separate sides, meeting only at their assigned ports.
  The two root-only case retains degree sum at least `6d-4` and at least
  seven root incidences, contradicting its planar upper bound of six.
  The final three-root-only case and all order-two endpoints also check.

The external planar alternative was checked against
[Norin--Totschnig, Theorem 13](https://arxiv.org/html/2507.03244v1),
quoting Robertson--Seymour--Thomas (2.4). It has no connectivity prerequisite;
relative boundary four excludes its root-free separation alternative.
Adding the outer four-cycle justifies Euler's bound without assuming a
simple original facial walk. [Xie's October 2019 Theorem 1.0.1](https://aco.gatech.edu/sites/default/files/images/xie_thesis.pdf)
requires precisely the smaller completion specified in the source;
it is a scope comparison, not a completed application here.

The reviewer helped check constructions during development and then reviewed
the complete frozen source. This is separate internal mathematical review,
not independent discovery or external peer review. No finite computation
is a proof premise. The two--one U distribution, including the stated
four-cut, and cuts containing U roots remain open. The normal form cannot
be transferred directly to a fixed colouring or critical host; neither
the whole linkage target nor C19, HC7 or the NT benchmark is established.

## Inner port coverage

**Scoped verdict: GREEN.** Removing only the new inner-port subsection
exactly recovers the previously audited source `468aab55fe3b21f5a6c491714eba19e36ceba5f620b3a847471527824373a5eb`.
Since the three ports lie in `D-X`, every X-subset is a proper old
D-subset and has boundary at least six. Identifying the V roots loses
at most one boundary vertex and no nonroot degree, by their disjoint
D-neighbourhoods. Fullness excludes singleton X, and `2<=|X|<|D|`
licenses minimality for each prescribed port in the auxiliary graph.
The triple carrier avoids the identified root and is unchanged. A simple
path from that root to the port lifts using the actual V endpoint of its
first edge; the direct-edge case works identically. No disconnected
preimage becomes a bag, and the two lifted carriers remain disjoint.
Coverage gives at least one V choice for every port; it supplies neither
a fixed V choice nor its compatibility with an outer construction.
The initial review and provenance above are preserved; no further
colouring, critical-host or global-conclusion claim is accepted.
