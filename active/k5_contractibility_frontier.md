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
  to the state below. Section 7 proves the terminal lifts below;
  it does not make the host four-connected.
- The [two-region theorem](../results/two_full_regions_paired_triangle.md),
  with an [adjacent audit](../results/two_full_regions_paired_triangle_audit.md),
  gives three pairwise adjacent bags joining two terminal triples whenever
  there are three disjoint paths between the triples and two disjoint
  connected regions full to all six terminals. The pairing is free.
- The [allocation obstructions](../barriers/k5_scheme_full_colour_class_obstruction.md),
  with an [adjacent audit](../barriers/k5_scheme_full_colour_class_obstruction_audit.md),
  rule out requiring any whole colour class in its own bag, and rule
  out a proposed four-marker dichotomy. The first host and the second
  example's K5 extension have explicit rooted K5 models; neither refutes
  the target.

## The global construction still required

For a surviving three-cut, its vertices have colours c,d,e; those
three original roots lie on one side, and roots a,b on the other.
The construction must carry the three roots to distinct boundary bags
with all three mutual contacts, or give another smaller rooted scheme.
The available paths include two simultaneous systems joining each
i-root to its i-port, one using colours i,a and one using i,b.
The c,d,e demand paths may have excursions on the opposite side.
An arbitrary three-path linkage does not retain the triangle contacts.

The two-region theorem closes their joint allocation for arbitrary host
order. Its proof contracts internal region edges when three-path
connectivity survives. Otherwise exact three-cuts make every linkage
spanning; taking coordinatewise minima of these cuts forces a separator
avoided by one intact region. The original three-connected host supplies
the required root-to-port linkage, truncated at its first boundary visits.

Producing the two regions remains open. The reverse packing uses c,d,e
vertices as labels; these can be adjacent on the triangle paths. A deficient
packing therefore does not license the existing independent-set reduction.

An alternative now has a verified lift: three disjoint connected bags,
each joining i to its i-port using only colours i,a,b. The inside triangle
paths then supply a rooted model for the contacts absent outside the cut.
The outside pieces form a smaller K5-scheme, and every returned model lifts
through the fixed bags. If all three triangle paths have outside excursions,
any three-path root-to-port linkage already suffices. Thus a minimum
counterexample has zero, one or two such excursions. The next task is to
force one of these allocations or a strict reduction in all remaining cases.

For hosts without a three-cut, a global exchange is also missing.
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
rooted at s_i and the other three old roots. Adjoin a to its s_i bag,
use `{r_i,u}` for the omitted old root, and retain the other three bags.
All added bags are connected; u sees every r_j and s_j, while a sees
every s_j, giving all ten contacts with fixed disjoint preimages.
No general existence of these outcomes is proved; states with literal
a-spokes require separate handling.

A complete proof must cover both the separator and inseparable states.
Every reduction must retain all roots in fixed disjoint preimages,
preserve the full scheme intersection condition, decrease host order
within its stated class, and lift any returned model. Further local
lemmas do not discharge these obligations.
