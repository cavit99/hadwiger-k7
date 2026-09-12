# Audit of the relative three--two five-cut reduction

Date: 12 September 2026.

**Current verdict: GREEN** for the reductions, completed cut configurations,
inner port coverage and the induced-path endpoint, with the full target open.
**Current source SHA-256:**
`2e3ae751857d2d8c17b659072c0c73b9c17da893612dd0a2fe09342a1ade171a`.

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

## Cut closures and a small U root

**Scoped verdict: GREEN**, 12 September 2026, for the current source above.
The diff against Git `268bcaa` retains the earlier mathematics through inner
port coverage; it adds the cut constructions and assertion 5, and revises
the title and remaining scope. The historical reviews above remain intact.
The reusable [linkage source](../results/four_root_linkage_with_ports.md) is
pinned at `f41f60cb657d39c9de1e19457c86d65b228607a9115e711b8c48a4d0dc92a8c1`,
with [audit](../results/four_root_linkage_with_ports_audit.md)
`f10c0a01f4e0329945bf830b647a740d2920a3e7f30ab1892fcbab195425ad51`.

- The U-containing cut uses a connected opposite-side preimage. Its only
  possible neighbour at any retained interior vertex was u0, so degrees
  and boundaries survive. Root incidence at least nine licenses the
  two-port criterion; expanding that preimage retains all three U roots.
- Maximality ranges over cuts both containing and avoiding U. Absorbing a
  port with at most one exterior neighbour leaves another U root outside
  the new cut, so it gives a legitimate larger single-U component. The
  relaxed V path can use unused ports while the U arm attaches to the
  connected opposite component. The two-vertex endpoint uses the original
  no-isolated-neighbour normalisation to obtain its actual V-to-port edge.
- The fully completed graph's six-connectivity and Xie's exact smaller
  completion classify the remaining cuts. A root-only component yields
  a U root of D-degree two or three. No root-only carrier construction is
  inferred merely from this classification.
- The proper-six boundary bound and retained V-neighbours prove that F-U
  is two-connected. Thus a nonroot p meeting all three U roots is terminal.
  Otherwise contract the connected set `{u,p,U1}` for a small U root u
  and a neighbour p meeting U1 but not U2. Relative boundary four survives.
  Degree loss plus the new root incidence is +1, zero or -1 for one, two
  or three neighbours in this set. At most two surviving nonroots have
  three such neighbours. The other root incidences contribute at least
  five, giving `2e>=6d+3`, contrary to the cofacial bound. The positive
  linkage lifts through the fixed connected preimage with all U roots.
- For a two-neighbour U root, contracting either incident edge preserves
  the original induction class if the opposite port has degree at least
  seven. Both port degrees therefore equal six. The stated connected
  remainder and its attachment counts check; no terminal allocation for
  that remaining configuration is inferred.

This is separate internal review with the earlier development provenance,
not external peer review. The two- and three-neighbour U-root residues and
the full linkage target remain open. Neither these normalisations nor the
new contractions preserve a fixed original colouring; no C19, HC7 or
NT-comparable conclusion is accepted.

## Induced-path endpoint and thin-port contraction

**Scoped verdict: GREEN**, 12 September 2026, for source SHA-256
`2e3ae751857d2d8c17b659072c0c73b9c17da893612dd0a2fe09342a1ade171a`.
The predecessor is Git `c95c0a03934110adf5966d206ee94a681248a565`, with source
`d499b9b4e6b6e5f5289d7b5477c4160bec42c8c4fa406cfb196daa4152665354`
and audit `68ae19309e4509d56cd50b1ceb37b9153c361aa4e9ee53d0d6e1d91209fd2686`.
Removing only the final root--root-edge clarification exactly recovers the
reviewed revision `6ab1810282bfcaafa9a074176fe42ed4629507d9250de7f0539dd1c3ca429774`.
Earlier audit records remain historical; this review covers the added endpoint.

- Lexicographic minimality in `(|D|,|E|)` permits deleting root--root edges
  and deleting `up` when `d(p)>=7`: degrees, all five roots and the required
  subset boundaries survive. Any resulting linkage already lies in F.
- A spanning connected partition exists. Maximising its U side excludes
  off-spine branches and non-edge spine blocks on the V side by their small
  actual boundaries. Thus the complement is an induced V path. The root's
  two or three D-neighbours are consecutive and all have degree six.
- The thin-port identity `2e(J)=sum d_F(z)+K-6` cancels epsilon exactly.
  Equality in the four-root disc bound forces the stated root incidences.
  Drawing contractions preserve distinct cofacial roots; both resulting
  four-vertex contact sets contradict the proper-six boundary condition.
- In the new maximal partition of J, all five H-neighbours of p lie on its
  V path. If q is bracketed, the replacement through p frees a root-free
  interval containing q; q's two U-side contacts connect that interval and
  u to the U carrier. The two original root groups remain disjoint.
- Extremality of q leaves at most one common H-neighbour. Contracting pq
  would otherwise preserve the induction class, so minimality forces its
  unique degree-six common nonroot x. Contracting `{u,p,q}` has a connected
  root preimage, leaves exactly x at degree five, preserves boundary five,
  and gives the new root degree seven; the explicit absence of root--root
  edges justifies that exact last count.

The reviewer participated in earlier thin-root development and separately
checked its scratch equality proof; this is an exact-source internal review,
not independent discovery or external peer review. No absorption of x, fixed
colouring preservation, full linkage theorem, C19 closure or HC7 conclusion
is accepted. The degree-five quotient remains outside the induction class.
