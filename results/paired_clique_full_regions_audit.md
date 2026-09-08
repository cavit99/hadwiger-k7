# Audit of the paired-clique theorem with full regions

**Verdict: GREEN** for the theorem, sharpness example and constructive
consequence in [the source](paired_clique_full_regions.md), SHA-256
`78121803cfc368cf0ff2e367d87dfc6747fbe888b0f3f5e994abdfe83ac5b8da`.
This records two separate whole-source internal reviews. It is not
external peer review or a finding about novelty or comparative significance.

## Scope and provenance

The conclusion holds for every finite host and every `k>=1`, with an
unspecified pairing of the two k-element terminal sets. The supplied
`k-1` regions must be nonempty, connected, disjoint from one another and
from all terminals, and each must contact every terminal. The k-linkage
is an additional hypothesis. No whole-host connectivity is assumed.

Both reviewers independently read the complete draft at SHA-256
`07442caff41a03e0e780f6c3d0eb938c83d39be1a25f65774ae236a1d6046567`
and returned GREEN. The present reviewer had previously audited the
three-pair special case and identified why the general interval argument
must use an actual edge, rather than merely a cut containing its endpoints.
That contribution precedes this whole-source review and is disclosed here.
The second reviewer separately checked all sections beyond the proof outline.

Both reviewers also read the final promoted source and returned GREEN.
Reversing its
status paragraph, relative link, British spelling and the added elementary
converse recovers the reviewed draft hash exactly. The converse is valid:
choose a terminal-to-terminal path in each connected bag; the paths are
disjoint and use distinct endpoints. No other mathematical text changed.

## Strongest checks

1. **Induction and ownership.** The `k=1` endpoint is explicit. Before
   recursion at `k-1`, both unused terminals are deleted together with
   the reserved region. The returned bags cannot absorb either terminal.
   Component absorption preserves all regions; a component with no region
   contact and neighbours on only one terminal shore is avoided by every
   full linkage. Contraction uses a fixed connected preimage containing
   no terminal. Each recursive operation strictly lowers host order.

2. **Internal cuts and spanning paths.** A failed region-edge contraction
   yields a lifted separator of exactly k vertices. It must meet every
   other region: even terminal deletions cannot remove all terminals on
   either shore within the remaining budget. Thus it has no terminal and
   exactly one vertex in each other region. Each region vertex has an
   internal neighbour, so the fixed linkage covers all nonterminals and
   every region edge has endpoints on different linkage paths.

3. **The interval step.** Spanning makes separation equivalent to absence
   of a strict prefix-to-suffix edge, which proves coordinatewise minimum
   and maximum closure. Projection between consecutive chain cuts prevents
   skipping a vertex position. For an actual region edge, separated
   occurrence intervals would either expose a forbidden crossing edge or
   give a strict intermediate median cut. A common cut alone would not
   suffice; the source explicitly retains the required edge condition.

4. **All clique contacts.** Every chain cut meets all `k-1` regions, so
   their occurrence intervals have depth at most two within each region.
   The interval intersection graph is a forest containing the connected
   actual region as a spanning subgraph; they must be the same tree.
   The first-vertex cut therefore joins its two vertices in the unique
   duplicated region. For different regions, one is represented uniquely,
   and fullness of the other path's R terminal supplies the contact.
   The linkage paths are disjoint bags retaining exactly one terminal
   from each shore, so no additional allocation or pairing assumption is used.

5. **Sharpness and algorithm.** With only `k-2` universal added vertices,
   two proposed bags contain none and are forced to be distinct,
   nonadjacent matching edges. This includes `k=2`. The algorithm needs
   only polynomially many vertex-flow tests per recursive call. If every
   region-edge test fails, the proof applies to any returned full linkage;
   constructing or enumerating the separator lattice is unnecessary.

The only external proof input is vertex Menger's theorem, used also in
its standard vertex-capacitated flow form. The linked three-pair result
is contextual rather than a dependency of this self-contained proof.
No finite computation is a premise of the theorem.

## Remaining limits

The regions must be supplied; the theorem does not construct them from
colourings or unrelated minor models. It does not preserve the regions
as additional bags or prescribe the terminal pairing. Applying it to
the fully rooted K5 or C19 constructions still requires their own exact
region hypotheses and a valid lift with all remaining bags disjoint.
Neither those targets nor HC7 is proved by this audit.
