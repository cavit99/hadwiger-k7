# Audit: five-vertex separators in the companion density problem

**Verdict: GREEN** for Lemmas 1–2, Theorem 3 and the stated reduction
limits. Separate internal audit by the route-assessment agent, 2026-09-07;
not external peer review or completion of the global density theorem,
Conjecture 19 or HC7.

**Source:** [density separators](hc7_companion_density_separators.md), SHA-256
`6bef580656a804b30ee415d535c24af604715c56821e7f8d84aed0216fab3bb9`.
The added eight-cycle navigation was checked; the positive proofs are unchanged.

**Input checked.** Norin–Totschnig Lemma 12 requires internal four-connectivity
at four roots and `e(F)>=4|F|-9`; it supplies adjacent helpers full to the
root bags, without root-root contacts. This audit uses the primary statement
recorded in the repository, without claiming fresh online inspection.
Both file hashes were verified:

- [Rooted-helper source](../results/hc7_k7minus_degree7_rooted_helper_closure.md):
  `6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67`.
- [Its audit](../results/hc7_k7minus_degree7_rooted_helper_closure_audit.md):
  `360a121c2ca33bc81b6300551203956f9bca6c00866d3c524bfe3602c9744407`.

**Strongest inference checks.**

1. A prohibited cut at `Z=S-{s}` has open side exactly `{s}`: otherwise
   adjoining `s` to the separator contradicts internal five-connectivity.
   Thus `d(s)<=3`; deletion leaves internal four-connectivity and at least
   `4|F-s|-8` edges. The exceptional fifth root is handled, not ignored.
2. Maximize helper union, then minimize root-bag order. Two actual ports
   yield a minimal root-and-ports tree with a nonroot port leaf. Transferring
   that leaf enlarges a connected helper while preserving both contacts
   and the prescribed root. Unused components cannot contact helpers.
   Hence at most four actual vertices bound the helper union. If `s` is
   outside, this is a prohibited `S`-rooted separation, even if a root is
   itself a boundary vertex. All four rooted bags stay disjoint and connected.
3. Actual cuts establish full components and internal connectivity of each
   closed side. The five-component merges, three-component diamond and
   four-component path constructions have seven disjoint connected bags;
   their only possible missing pairs are the displayed independent pairs.
4. Across a two-component cut, the opposite component contacts four literal
   roots and the fifth-root helper. The two possible missing pairs are
   independent. Otherwise the two side bounds, subtracting duplicated
   boundary edges, give `e(G)<=4|G|-e(G[S])<4|G|`. The diamond-free
   five-vertex bound `e<=6` is valid. The contraction identity and strict
   order decrease are exact; dense hosts have order at least nine, avoiding
   the small-order exception to the actual-five-cut assertion.

**Side-bound counterexample checked:** [barrier, Section 3](../barriers/hc7_companion_induction_shortcuts.md#3-a-full-boundary-apex-does-not-retain-a-sufficient-side-class), SHA-256
`99661d13e82d84c940e3a7861bb7cfd048502399c1484c62c487da5a1ca0fec3`.
Five independent roots complete to a triangle give internal five-connectivity
and side count `18>16`. Adding the boundary apex yields a subgraph of
`K_4 join I_5`, hence excludes `K_6` and the target, but has connectivity
four. Its adjacent audit records the arbitrary-bag exclusion check.

**Remaining gaps.** No suitable density-preserving contraction is proved
to exist, no five-connected induction class is closed, and no target is
constructed across every remaining diamond-free five-cut. Boundary clique
completion or the refuted side estimate cannot supply these steps. No
substantive gap was found in the scoped partial claims; the global theorem
and required colouring consequences remain unproved.
