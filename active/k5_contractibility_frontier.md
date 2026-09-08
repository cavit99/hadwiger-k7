# Fully rooted K5 contractibility

**Status:** conjectural target. This is a conditional route under the
[research ledger](../RESEARCH_LEDGER.md), not a new completion criterion.

## Target and reason for the attack

**Target.** Every K5-scheme in every finite host contains five pairwise
disjoint connected branch sets, one containing each prescribed root,
with all ten contacts. A scheme has one root-to-root path per target
edge, no foreign root internally, and a common target endpoint for
every nonempty collection of paths meeting at a vertex.

This asks for a new conclusion beyond the completed bipartite theorem.
The unrooted conclusion is already Kündgen–Pelsmajer–Ramamurthi,
[Theorem 5.3](https://arxiv.org/html/1207.6141#S5); their Lemma 5.2 can
move roots when localising a scheme across a clique-sum. It does not
give the fixed preimages required here. Its statement and proof were
inspected for this attack. No priority or NT-level significance claim
is made for the present partial work.

The [matching-contraction construction](hc7_two_triangle_matching_colour_host.md)
gives actual five-root schemes in one branch of the remaining C19 host.
A rooted K5 theorem would extract their minors while retaining the
reserved independent transversal. The six-chromatic branch and the
extension to seven compatible bags would still remain. Neither this
target nor its local reductions may be reported as C19 or HC7.

## Written inputs and their limits

- The [independent-set reduction](../results/general_scheme_independent_set_reduction.md)
  applies to arbitrary targets only when its projection rank condition
  holds. Bipartite sufficiency does not remove that hypothesis for K5.
- The [local exchanges](k5_scheme_local_exchange.md), with an
  [adjacent audit](k5_scheme_local_exchange_audit.md), absorb two
  intersections into different root bags. One is a strict reduction;
  another gives a terminal model when a repaired path avoids the
  fifth-root path. Neither asserts that its configuration must occur.
- The [separator deductions](k5_scheme_separator_reduction.md), with an
  [adjacent audit](k5_scheme_separator_reduction_audit.md), make a
  minimum counterexample three-connected and restrict every three-cut
  to one rainbow pattern. Section 7 proves its terminal lifts.
- The [four-connectivity theorem](../results/k5_scheme_four_connectivity.md),
  with [two internal reviews](../results/k5_scheme_four_connectivity_audit.md),
  closes that pattern. A minimum rooted K5-scheme counterexample,
  if one exists, is four-connected.
- The [two-region theorem](../results/two_full_regions_paired_triangle.md),
  with an [adjacent audit](../results/two_full_regions_paired_triangle_audit.md),
  gives three pairwise adjacent bags joining two terminal triples whenever
  there are three disjoint paths between the triples and two disjoint
  connected regions full to all six terminals. The pairing is free.
- The [general paired-clique theorem](../results/paired_clique_full_regions.md),
  with [two internal reviews](../results/paired_clique_full_regions_audit.md),
  extends this construction to every k: k paths and k−1 full regions
  give k pairwise adjacent bags, each joining one terminal from each set.
  The region count is sharp and the construction is polynomial-time.
  Its stronger region hypothesis has not been obtained in the C19 host.
- The [allocation obstructions](../barriers/k5_scheme_full_colour_class_obstruction.md),
  with an [adjacent audit](../barriers/k5_scheme_full_colour_class_obstruction_audit.md),
  rule out requiring any whole colour class in its own bag, and rule
  out a proposed four-marker dichotomy. The first host and the second
  example's K5 extension have explicit rooted K5 models; neither refutes
  the target.

## The global construction still required

The three-cut construction is complete for arbitrary host order. Reverse
packing either produces two actual full regions, or its deficient rank
forces every component to occupy exactly one interval on each of two
strands. A second packing then lifts directly to contractions in the
original host, preserving every triangle-path vertex in its own colour.
The host order strictly decreases. No arbitrary model is lifted from
the auxiliary interval compression.

The remaining task is a rooted construction in the four-connected case,
or a reduction within the full class of properly coloured schemes.
Deleting one original root exposes a rooted K4 scheme and four spokes;
their compatible allocation is still missing. A separately chosen K4
model need not leave the required vertices available to the fifth bag.
The current local laboratory permits one colour to have at most one
nonroot, while all four other colours and the host order are unrestricted.
Strong normalisation preserves this class, although it can make a spoke
literal and can change which vertices are marked. The failed four-marker
dichotomy cannot therefore be substituted for a closed induction.
The positive obstruction models show why a root bag may take only part
of a colour class while another bag takes its remaining vertex.

**Three sufficient outcomes; existence unproved.** In a properly coloured
scheme, suppose a,u are the only a-coloured vertices and all four a-spokes
are nonliteral paths `a-s_i-u-r_i`. Put `J=G−{a,u}`, with markers `S={s_i}`.
A rooted K4 model in J suffices if it (i) avoids some s_i, or
(ii) puts S in four different old-root bags. In (i) add `{a,s_i,u}`;
in (ii) add `{a}`. Alternatively, (iii) suppose `J−r_i` has a K4 model
rooted at any marker s_j and the other three old roots. Adjoin a to its s_j bag,
use `{r_i,u}` for the omitted old root, and retain the other three bags.
All added bags are connected; u sees every r_j and s_j, while a sees
every s_j, giving all ten contacts with fixed disjoint preimages.
No general existence of these outcomes is proved; states with literal
a-spokes require separate handling.

A complete proof must now close the four-connected state.
Every reduction must retain all roots in fixed disjoint preimages,
preserve the full scheme intersection condition, decrease host order
within its stated class, and lift any returned model. Further local
lemmas do not discharge these obligations.
