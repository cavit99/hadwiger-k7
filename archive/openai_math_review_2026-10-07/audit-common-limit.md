# Targeted audit: product tests and common limit

Date: 7 October 2026. Source: `openai/math`, commit
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`, manuscript
`preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026`.

## Scope and verdict

**Verdict: conditional local pass; no explicit counterexample or first unsupported inference found in the two assigned sections. This is not a validity verdict for the whole manuscript.**

Primary scope: every substantive statement and proof in
`10-product-tests.tex` and `11-common-limit.tex`. I reconstructed the
energy increment, four-copy estimate, projection calculation, construction
of the probability space, truncation argument, density identification and
zero-overlap consequence. I checked the definitions and hypotheses imported
from the introduction, raw supersaturation, frame-image/Walsh laws, key
reference, histograms and the end of the parameter section. The deeper
proofs of preparation, generic mixers, histogram control, unary positivity,
binary mixing, status-span, rare overlap, collision lifting and graph
sampling are not certified by this report. Relevant portions of the
histogram and frame proofs were inspected to identify their exact interfaces.
No finite computation or Lean verification was run or used as evidence.

SHA-256 of the exact primary sources:

- `10-product-tests.tex`: `9d7f78c87bb88b128979ffaec3baf1cfb07d9cc0e99e4b94521a01fe1109d216`
- `11-common-limit.tex`: `a61e277284bd1e67ef62d4bfca99b187ea578cc0834f68c189ab74a9fe98343c`
- Inspected dependency `09-histograms.tex`: `675d50021e381ed42d94b135c334067ea4ed2f9bda1aa097b4f2b37143974ee3`

Line locators below refer to these downloaded files. This audit is saved
outside the HC7 repository and does not change its mathematical standing.

## Exact hypotheses that must remain attached

The construction constants, including `M_0`, are fixed as `n` tends to
infinity, and `N=M_0 n`. A query has a fixed bounded number of positions.
Original query labels are distinct at each endpoint. Fresh copies used in
moments may repeat these labels but have independently sampled parameters.
The parameter law is a product over positions; only separately feasible
flavor, diagonal and permitted tester conditioning is normalized. Every
flavor retains a fresh uniform `Z` block.

For mixed-law assertions, Section 9 requires a fixed joint-density exponent
`C` and endpoint marginal inflation subexponential in `n`:

    rho_n <= 2^(C N) mu^2,
    (rho_n)_i <= M 2^(a_n N) mu,   a_n -> 0.

For leaf histogram compactness, the distinct input is a uniform leaf joint
cap `pi <= 2^(C_L N) mu^2`. A normalized individual leaf is not assumed to
have small endpoint marginal caps. Two units and their leaves are sampled
independently before usability/flag indicators are multiplied into the
integrand. No pair-dependent conditioning is silently substituted for this
independent product experiment.

The permitted successful-query filter is an orientation-only flag times
unary numerical-status predicates times the specified Gram and nominal
`L,R` predicates. An arbitrary joint parameter predicate is not covered.
A flag depending on the opposite leaf remains orientation-only once the
leaf pair is fixed; it must not depend on the opposite sampled orientation
or query parameters unless a separate argument supplies that format.

## Section 10: reconstruction and challenges

### Finite twisted regularity (lines 89–134)

The energy increment is valid under the actual product reference, even
though Gram bits are correlated with the two groups. At each step the
conditioning algebra includes both current group partitions and all
crossing Gram bits. Quantized witnesses have bounded complexity and retain
correlation greater than `delta/2`. Orthogonality to the old algebra gives
an increment at least `delta^2/4` in the squared norm of the conditional
expectation. Its norm is bounded by `B`, so only a bounded number of steps
are possible.

On each pair of final cells, extending the bounded conditional expectation
by zero at impossible Gram configurations permits an ordinary finite
Fourier expansion. Each Fourier coefficient is bounded by `B`; its
characters are exactly the allowed twists. This preserves the pointwise
remainder bound `2B`. No false independence of Gram bits is needed.

### Four-copy terminal remainder (lines 140–249)

For fixed orientation the two Cauchy–Schwarz applications give the usual
four-corner expression. Its nonnegativity follows by writing it as the
mean square of an inner expectation. Crucially, the separate weights have
then disappeared. Thus one exceptional orientation set can control every
choice of orientation-dependent group weights; no union over an uncountable
family of weights is required.

The four-copy test is a deterministic function of nominal inputs and their
global keys. It has a fixed sup bound and two copies of each original
position. The imported typicality lemma explicitly permits repeated labels.
It is therefore the applicable interface, provided that lemma is valid.
The asserted typicality conclusion is used only for each fixed test and
fixed positive tolerance, not simultaneously for all tests.

For its raw mean, fix the nominal inputs. Fresh uniform `Z` coordinates make
the bounded collection of nominal columns independent, separately by
endpoint/component/mode, except with exponentially small probability. The
primal frame-image law then has only its same-endpoint Gram constraints and
individual injectivity. With boundedly many columns, removing injectivity
has exponentially small error and all Gram normalization ratios have fixed
bounds. The nominal `L,R` signs are constants at this point; their values
need not be independent.

I reconstructed the exhaustive character classification:

1. Terms internal to one of `I_0,I_1,J_0,J_1` are separate group weights.
2. If an `I_0`–`I_1` coefficient rectangle is nonzero, fix both `J` groups.
   The remaining integrand has two bounded weights and a nonzero bilinear
   form in distinguished global slots. Its rank is at least `N`. Individual
   diagonal densities can be absorbed in the weights with fixed constants.
   Walsh gives exponentially small correlation. The same applies to a
   nonzero `J_0`–`J_1` rectangle, including when both kinds occur.
3. If both copy-to-copy rectangles vanish, fix `I_1,J_1`. The `I_0,J_0`
   integral contains one copy of the cut-small remainder, an allowed
   quadrant twist, and bounded separate weights. The other three copies
   contribute at most `B_1^3`. This bounds the term by `B_1^3 delta` up to
   the already fixed normalizations.

All interactions are accounted for: each global dot connects a plus and a
minus slot in one component, and coincident descriptions are collapsed.
The two directional dots between different positions are different slot
pairs. Endpoint mixing removes some raw Gram constraints; it does not add
an interaction outside the three classes. This yields the claimed fixed
`C_3 delta + o(1)` raw bound and hence its fourth-root consequence.

### Recursive approximation and tolerance order (lines 251–340)

The recursion is finite: every split increases the number of disjoint
groups by one, so a structured branch has at most `r-1` splits. Leaving a
remainder terminal avoids multiplying two uncontrolled remainders.
At each depth the number and bounds of pending terms are known from earlier
choices. One can choose its cut and empirical tolerances before computing
the next depth's complexity. Thus later large regularity bounds do not
force a circular choice of an earlier error. All these are constants
independent of `n`; no change in `M_0` is required.

Every twist equals one on the accepted key space: Section 6 imposes all
off-position plus/minus Grams in each component to be zero. Removing twists
from the structured approximation is therefore legitimate for reference
and accepted-query integrations.

When outside parameters are fixed in a terminal term, all binary phases
involving them become group weights. The remaining crossing phase and
four-copy test do not depend on their values. This justifies using one
exceptional set for every outside fixation. An extra orientation-only flag
can shrink the error; a general additional joint input filter cannot.

The factorized integration corollary is valid conditional on binary mixing
uniform over unary weights. As throughout that interface, 'bounded weights'
requires a fixed common sup bound (normally one); no error can be uniform
over arbitrarily large, unbounded-in-`n` norms.

## Section 11: reconstruction and challenges

### Global projection for independent leaf families (lines 132–211)

This calculation handles the actual pair-adaptive choices claimed. Truncated
`L^1` nets give `L^2` nets because values lie in `[0,R]`. With `m` net
representatives, both covariance operators have trace at most `T=m R^2`.
A unit eigenfunction of `C_A` with eigenvalue greater than `delta` has
pointwise bound `T/delta`, so a bounded finite partition can approximate
all such eigenfunctions.

For its complementary projection `Q`, the small-eigenvalue part has
operator norm at most `delta`, and the large-eigenvalue part contributes
at most `T epsilon^2`. Deterministic refinement preserves this bound.
I independently checked the trace identity:

    E sum_(a,b) |<f_(L,a),g_(L',b)> - <P f_(L,a),P g_(L',b)>|^2
      = Tr(Q C_A Q C_B)
      <= (delta + T epsilon^2) T.

It uses independent leaves exactly once. A pair-adaptive representative
choice is dominated by this nonnegative sum, and approximation of arbitrary
family members costs at most `4 R` times the `L^2` net error. Accuracy can
therefore be chosen sequentially after the net size is fixed. Multiplication
by a leaf-pair indicator cannot increase the absolute-error bound. This
argument would not justify replacing the independent leaf law by an
arbitrarily conditioned pair law; the section does not do so.

The preceding own-leaf-family requirement is substantive. Here it is met
only because each numerical option fixes the side's parameter predicates,
and all dependence on the other leaf is asserted to enter through an
orientation filter. Verifying that actual prepared admissibility has this
format belongs to the preparation audit.

### Common signature experiment (lines 222–366)

The request closure is countable, not finite, and that is sufficient. Each
finite stage has bounded complexity independent of `n`. Projection cells
are deterministic functions of global tuple keys chosen using leaf laws,
not sampled leaves. Their weak-product factors are deterministic global
unary-key tests. Each request can be assigned along the whole sequence;
arbitrary definitions at finitely many initial indices do not affect
limits. Padding term lists allows coefficients to be stored in fixed
compact coordinate boxes.

Cylinder mass consistency on a countable bit-sequence space gives actual
countably additive limiting measures. One may use the full Cantor product
and allow redundant/impossible signatures to have zero mass; this avoids
needing any extra closedness claim for the image of a signature map.
Clopen cylinders make all required finite-coordinate mass evaluations
continuous.

Mixed typicality for each fixed unary cylinder forces the total empirical
status measure to equal the reference measure in the limit. Since status
measures are nonnegative, they have densities in `[0,1]`. Taking martingale
limits of finite-cylinder density averages gives joint measurability in
array and signature. No pointwise convergence of the finite-`n` densities
is asserted or required.

For positivity, the necessary input is the strong, exact version of unary
positivity: for every deterministic global-key cell sequence with positive
limiting reference mass, a fixed lower fraction works for every relevant
orientation-selected basis assignment, with a cell-dependent onset allowed.
Apply it separately to countably many cylinders, pass each inequality to the
limit, and extend the resulting measure domination from the cylinder
algebra to all measurable sets. This yields the almost-everywhere lower
densities. It does not condition on an arbitrary nominal basis-bit cell.

The raw `GL_Z` symmetry is not used in Sections 10–11 to claim invariance of
`T` or of a filtered law. It is an input to the earlier positivity proof.
Here mixed almost-sure positivity is transferred through orientation filters
only by preservation of null sets. This respects the restricted symmetry
interface communicated by the algebra auditor.

The product-reference lemma supplies independence of unary projections in
the limiting tuple-reference law, uniformly for arbitrary finite global
unary test lists. That independence does not assert independence of statuses
before their common orientation has been integrated out.

Storing conditional laws as coordinates of `Z_n` is essential and valid.
Conditional on each leaf pair, the two orientation laws are a product.
Those same two laws are retained as coordinates; sampling their product
from the limiting record has the correct limiting continuous test
expectations. This uses continuity of products of probability measures on
compact spaces, not an interchange of disintegration and weak convergence.
Dropping flags and averaging recovers iid base arrays because this identity
holds at every `n`. Finite metadata and flags are discrete, so their
identities and passage probabilities are closed under this limit.
The assertions concerning prepared tables and predictions remain conditional
on their being encoded in that bounded metadata as Section 8 claims.

### Vanishing overlaps (lines 375–433)

Uniform integrability is essential; bounded total mass alone would not
suffice. Section 11 correctly invokes the uniform small-set conclusion
for all normalized leaf laws and orientation filters. Since a superlevel
set above `R` has reference mass at most `1/R`, the uniform conclusion gives
a deterministic asymptotic tail bound tending to zero. Cylinder inequalities
preserve `0 <= eta_R <= R rho`, monotonicity in `R`, and the total mass tail
bound. Hence the full limiting measure is the increasing supremum of these
absolutely continuous truncations.

For a finite partition, the projected overlap is
`sum_C eta_(A,R)(C) eta_(B,R)(C) / nu(C)`. Cells with vanishing reference
mass contribute at most `R^2 nu(C)`. On the other cells continuity applies.
This specifically eliminates the possible division-by-a-vanishing-cell
problem. Global projections and their refinement guarantee then pass zero
expected usable overlap through increasing cylinder partitions. Bounded
truncated densities converge in `L^2` under conditional expectations; their
products are dominated by `R^2`. Nonnegativity gives almost-sure zero
products for each truncation, and the increasing limit gives the assertion
for full densities. No general weak continuity of density products is used.

### Identification and obstruction (lines 452–579)

The actual weak-product estimate is used before any passage to the limit,
with numerical statuses as unary weights and admissibility as an
orientation-only flag. Exceptional mass is averaged with actual leaf
weights; it is never required to be small on each normalized leaf.
A flag chosen using the opposite leaf cannot enlarge the unconditional
bad-orientation mass in this independent two-leaf experiment.

Each structured term then factors by binary mixing. All its unary integrals
are finite combinations of stored status-cylinder coordinates. The
resulting expression is a continuous function of the stored conditional
laws and finite coordinates, so it has the required joint weak limit and
mean absolute error control.

The separate reference comparison extends from cylinder-simple bounded
unary functions to all bounded measurable ones by `L^1` approximation and
product telescoping. Its bound is deterministic and uniform over those
functions; only after establishing it does the proof insert the random
status densities. Thus there is no illicit substitution of a random test
into a merely fixed-test probability estimate.

The resulting density formula retains the mixture over a common side
orientation:

    G_Z(u) = kappa integral product_l h_(t_l,status_l)^theta(xi_l(u))
                        d alpha_Z(theta).

It does not replace this by a product of orientation-averaged marginals.
Finally, conditional independence of the two side draws and independence
of reference projections allow Fubini to express the overlap as the mean
of a product of nonnegative unary overlaps. Its vanishing implies the
claimed almost-sure obstruction, after a finite union over options.

## Scale and uniformity verdict

No step in these two sections needs a convergence rate uniform over the
countably many eventual tests. At fixed accuracy there are finitely many
bounded tests; each has its own eventual exponential estimate. A diagonal
subsequence handles the countable closure. `M_0` and construction constants
stay fixed. The subexponential endpoint inflation can be absorbed at each
fixed stage because `a_n N=o(n)`.

Likewise no effective quantitative lower bound on a compactness-produced
positive overlap is asserted here. The later collision argument must
correctly use positivity along a subsequence with its exponential margin;
that global implication is outside this primary audit.

## Unresolved dependencies and prohibited extrapolations

The local conclusion depends on independent validation of:

1. uniform frame-image/Gram normalization and Walsh interfaces;
2. histogram uniform integrability and own-leaf nets with their exact joint
   density caps;
3. typicality for arbitrary bounded global input-and-key test sequences,
   including repeated-label copies, under mixed caps;
4. binary mixing uniformly over all allowed orientation-dependent unary
   weights, with fixed positive `kappa`;
5. unary positivity for arbitrary deterministic global-key cells, uniformly
   over every selected low-rank effective space and basis;
6. preparation's bounded metadata, leaf law caps, positive table mass and
   exact orientation-only admissibility format.

The audit supplies no permission to substitute arbitrary joint input
filters, to condition a leaf pair and keep calling its leaves independent,
to infer small marginal caps on each normalized leaf, or to demand one
finite-`n` orientation good for all measurable key tests. None of those
stronger assertions was needed in the inspected local proofs.

## Cross-audit interface reconciliation

After completing the reconstruction above, I read `audit-geometry.md` and
`audit-preparation.md`, including the independent follow-up challenge of
unary positivity. Their exact source hashes agree with this report.
The listed dependencies above describe the limits of this auditor's primary
scope; they are not newly discovered gaps in the manuscript.

The geometry report covers the frame-image, Gram and Walsh interfaces used
by the four-copy calculation. The preparation/histogram report covers the
uniform integrability and own-leaf nets, repeated-label common-test
typicality, uniform binary mixing, mixed unary positivity, and the required
orientation-only table flags. In particular, it verifies that the side's
admissibility predicate factors after fixing the independent leaf pair.
The separate positivity reconstruction confirms the lower fraction for an
orientation-selected effective basis on a deterministic global-key cell;
it does not assert invariance of the filtered law or of `T`, and neither is
used here.

**No genuinely unresolved interface between those verified statements and
the uses in Sections 10–11 was identified.** This conclusion remains a
scoped internal audit: validity of the remaining phase/algebra/status/rare
branches and the full theorem must be established by their own audits and
the final whole-chain reconstruction, not inferred from agreement among
these local reports.
