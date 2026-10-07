# Scoped internal audit: preparation and histograms

Status: separate internal audit of the specified source sections. No false
intermediate statement or fatal unsupported inference was identified in the
arguments reconstructed below. This is a scoped, conditional assessment; it
does not verify the claimed Hadwiger counterexample or the full paper.

Source revision supplied by the parent audit:
`adc7f1241b42e322a6451854ab7e4b4c146bf78a` (`openai/math`).
Audit date: 2026-10-07. Local sources were read, not edited.

SHA-256 of the principal source files:

- `08-preparation.tex`:
  `5b2a1c278d9fb1fb26f06ebb4b93139cd51590f1274eaa6bd5f9233245e71e70`
- `09-histograms.tex`:
  `675d50021e381ed42d94b135c334067ea4ed2f9bda1aa097b4f2b37143974ee3`

## Scope and retained obligation

The paper must prove raw supersaturation for every admissible unit law, not
only for independent endpoints, and then transfer it to a finite graph.
Specifically, `03-distributions.tex`, `thm:raw-supersaturation`, requires
four cross holes with probability at least `2^(-100 g N)` whenever the two
endpoint marginals are bounded by `M mu` and the joint law by `2^(D N) mu^2`.
Here `N=M0 n`, all construction constants precede the unit law, and `n` is
the only unbounded parameter.

I independently reconstructed the main proofs of both assigned sections,
including their statistical arguments. I read the construction, raw
supersaturation statement, relevant frame-law and mixer statements/proofs,
the parameter ledger, and the uses of these interfaces in Sections 11–13.
I did not independently audit the phase alternative, full realization,
collision lift, weak-product theorem, common-limit model, or scalar-span
closure. There was no computation or numerical experiment in this audit.

## Preparation: claims whose deductions checked

1. **Exactification (`lem:empty-status`, 08:175–233).** Conditional on the
   stated one-point frame law and fixed marginal cap at this stage, replacing
   each predictor by its asymptotic multiple of `q` incurs average `o(1)`
   error. A finite union and Markov restriction give unitwise uniform `o(1)`
   errors. The error polynomial has base degree at most two, so error below
   `1/4` implies exact vanishing at each allowed base point. Its selector
   degree is at most `2j*`; the excluded-selector budget is strictly below
   the minimum nonzero support `2^(b-2j*)`, so the identity extends to every
   selector. Summing the same shared-only atom over all odd `g` tags kills
   the linear terms and forces the coefficient of `q` to be zero. Point
   atoms span the cut space, yielding the claimed whole-space identity.
   The fixed marginal cap is used before a possible subexponential fiber
   restriction, which is the correct order for this `o(1)` argument.

2. **Affine slices (`lem:synthetic-slice`, 08:243–314).** The constant
   coordinates in two affine batches force `a=a'` in a nominal relation;
   the remaining matrix `[z0+z0', L_Z, L'_Z]` has independent uniform bits.
   This yields nominal dependence probability at most
   `(2^(2d+1)-1)2^(-n)`. On independence, the two-batch frame law differs
   from the product law only by finitely many mutual Gram constraints and
   an exponentially unlikely loss of injectivity. Every nonzero mutual
   character has cross bit-rank at least `N`, so the Walsh bound gives
   `O(2^(-N/2))`. This proves the stated uniform variance estimate for a
   prescribed common test. It does not cover a test selected from the
   queried orientation, and that stronger conclusion is not used here.

3. **Zero tensor difference (`lem:zero-delta`).** Given the sparse-profile
   input from `lem:raw-intersections`, the retained pure testers all have
   coefficient one when the two alpha bits differ. The right side of
   `eq:pure-prediction` is indeed a sum of at most
   `s1=(g-1)(h+2J K1)` affine products. The tester-room inequality is an
   eventual lower bound on `r0` after `J,K1` are fixed, because `h=1000r0`
   and `(g-20000)/2>0`. Routing the synthetic Gram into distinct retained
   ordered tester pairs gives a positive probability depending only on
   fixed constants; it leaves `Z` coefficients uniform. The common test
   asks for existence of an affine-product representation and thus does
   not contain the unit-specific mark. The finite collection of slices
   bounds each cross-coefficient matrix by rank `2s1`, while shared-only
   parity makes their sum `I_(2g s1+1)`. Rank subadditivity contradicts
   this. There is no need to realize the entire large synthetic tester in
   one local pure-flavor slice.

4. **Mass accounting in `prop:status-preparation`.** Subject to the phase,
   tiny-cover, injection and peeling inputs, the final deductions preserve
   the necessary probability scales. In case (iii), an injection failure
   at most `.001` times compatible pair mass implies that a fixed positive
   fraction of compatible leaf pairs have conditional injection success
   at least `1/2`. There are at most a fixed number `Q` of table values in
   each bounded leaf-pair coordinate format. A table attained with mass
   at least `1/(2Q)` is compatible because the old support is pinned. Its
   admissibility event factors into one filter on each independent
   conditional orientation law. Their product mass is at least
   `1/(2Q)`, so each separate factor has this lower bound. No uniform
   pigeonhole over ambient leaf images is required.

5. **No-prediction interface.** Case (i) uses unconditional injection on
   independent units before subdivision by flags or tables. Its success
   mass is greater than `.99`. Later negligible trimming cannot invalidate
   the use made in Section 12: that section extracts prediction mass at
   least `.04/64=.000625`, with a strict fixed margin above the definition's
   `10^-6`. Multiplying by a retained proportion tending to one still
   contradicts no prediction on the original first-peeled law. An exact
   threshold without a margin would require care; the actual downstream
   argument has the needed margin.

6. **No parameter feedback detected.** Injection tolerances are fixed
   before `h`. The possibly much smaller table-filter mass `a0=1/(2Q)`
   is chosen afterward and enters only later limiting accuracy choices.
   Synthetic slice counts and positive Gram-conditioning probabilities
   are fixed in `n`; they can increase the asymptotic onset without
   changing `h`, `J`, or `M0`.

## Histogram and mixed-law estimates

### Many queries and entropy

The many-query argument (`lem:histogram-many-queries`, 09:222–316) survives
the potentially dangerous exponential leaf-density cost:

- Fresh `Z` coordinates bound nominal-dependence failure uniformly at
  each orientation, even with repeated labels and feasible tester/diagonal
  conditioning. Choosing a sufficiently small positive fixed `c1` makes
  `ell=floor(c1 n)` repeats nominally independent with exponentially high
  probability.
- For a nonzero cross-draw character, let `t` be the largest rank of a
  coefficient rectangle whose two sets of draw blocks are disjoint.
  A nonsingular `t` minor uses at most `t` blocks on each side. Once all
  entries incident to those blocks are recorded, any entry between two
  other distinct blocks is fixed by bordering the minor and using the
  maximality of `t`. The diagonal blocks are zero. This justifies the
  `2^(C k^2 ell t)` pattern count.
- Grouping those selected draw blocks into two Walsh factors gives
  `2^(-tN/2)`, and retaining the other independent cell probabilities
  loses at most `w_min^(-2t)`. For every fixed positive lower cell-weight
  bound, this term is absorbed by the `N` exponent as `n` grows. Thus the
  constants `c1,c2` need not depend on the partition accuracy.
- In the entropy proof, empirical high entropy and nominal independence
  have probability `1-o(1)` **uniformly conditional on each orientation**
  with high coarse entropy. Only the upper bound on that independent
  event is multiplied by `2^(C_L N)`. No raw `2^(-c n)` error is incorrectly
  paid through the much larger leaf cap.

For every bounded partition with positive limiting reference weights,
this gives the claimed bounded expected coarse conditional entropy,
uniform in the leaf and independent of the fixed partition complexity.
Flags contribute at most their fixed number `F` of bits by the entropy
chain rule.

### Small sets and all-filter nets

The resulting asymptotic small-set continuity is uniform over leaves:
a purported positive query mass on reference sets tending to zero can
be embedded in a two-cell partition of fixed mass `delta`; the entropy
bound would force `a log2(1/delta) <= C_H+1` for every delta, impossible.

For an orientation-and-flag filter, a sign split witnessing L1 error
greater than epsilon forces expected conditional-vector discrepancy
greater than epsilon. Pinsker and the entropy chain rule then force an
entropy increment. The proof handles adaptively varying reference cells:
at each fixed refinement depth pass to convergent weights, discard cells
of zero limiting reference mass using the already-proved small-set
continuity, and telescope on the surviving tree. Merging those zero-mass
cells into one positive cell before taking the final entropy upper bound
is legitimate, since their conditional mass vanishes in expectation.
This supplies a uniform bound on refinement depth, then on L1 net size.

The nets cover every orientation-only filter and any fixed bounded set
of parameter flags. They may depend on their own leaf. Nothing requires
the separately normalized leaf to have a small endpoint marginal cap.
Restriction to the key reference `cK_n` and use of normalized `nu_n`
does not increase L1 distances; the density receives the factor
`omega_n(cK_n)`. The small-set statement gives the claimed uniform
integrability of every unnormalized filtered histogram.

### Typicality with arbitrary dependence inside a unit

The one-endpoint variance proof is a bounded-batch comparison and works
uniformly for fixed external input-and-image data. For the paired case,
the first endpoint's marginal cap removes a bad set of first orientations.
For each remaining one, the corresponding second-input bad set has raw
probability at most `2^(-c n)`. If an orientation oversamples that set with
probability at least eta, `ell'=floor(c2' n)` successful independent-column
queries have conditional probability at least `(eta/2)^ell'`. Their raw
image probability is at most `2^(C2 ell'^2-c n ell')`. Taking `c2'`
sufficiently small gives a raw exception `2^(-Omega(n^2))`. This withstands
the joint `2^(C N)` density cap. The final second-endpoint comparison uses
its marginal cap. This argument does not assume independent endpoints in
the unit law.

### Binary mixing

Conditional on the stated mixer properties, the same-endpoint pair ranks
are at least `n/5` for every nonzero relevant bit pattern. For opposite
endpoints, intersection dimension at least `n/10` between full plus
frames has raw probability `2^(-Omega(n^2))`, using the image bound and
`dim B/N` made small by `M0`. Outside that event, at least `9n/10` plus
directions are independent modulo the other plus frame. The other minus
frame supplies a uniform rectangular evaluation matrix on them before
its rank conditioning; reverse-direction terms use separate minus-frame
randomness. A fixed translation does not change the uniform law. The
low-rank count is quadratic-exponentially small. The joint density cap
therefore preserves the exception estimate.

For each nonzero full character, fixing other position inputs reduces
to one of these two-position Walsh estimates. Feasible tester or diagonal
conditioning has fixed reciprocal probability and can be included in the
two unary weights. Hence the exceptional orientations are independent
of all unary weights, including ones chosen from the full orientation.
This is the necessary uniformity for later status filters.

### Unary positivity on common key cells

I reconstructed the key step in `lem:unary-positivity` (09:794–884).
For a fixed low-rank profile, the sign has bounded row-bit dimension and
`Z` polar rank at least `2(J-s0)`. The raw frame law is invariant under a
common `GL_n(2)` change of the `Z` coordinates. After changing the uniform
input variable back, a fixed global key cell and tester summary are fixed,
while the sign's row space moves.

If more than `2^(-2An)` transformations have excessive conditional bias
on a cell of fixed positive mass, then for any fixed number `u` one can
select `u` such transformations, with a common bias sign, such that each
new row space meets the preceding span in dimension at most `s0`.
The excluded proportion is `O_u(2^(-s0 n))`, smaller than the selected
bias proportion since `s0>2A`. Conditional on all non-Z coordinates and
previous row bits, the new sign has mean at most
`b*=2^(-J+2s0)<gamma`. Its centered variables are adapted martingale
differences of second moment at most one. Thus

`(gamma-b*) delta' <= sqrt(delta'/u)`.

Choosing fixed `u>2/[delta(gamma-b*)^2]` contradicts `delta'>=delta/2`.
The intrinsic bias cost is `b* delta'`, not an absolute `b*`; this is why
the same fixed `J` and lower fraction work on arbitrarily small fixed
positive cells. `u` and the asymptotic onset can depend on delta.

Integration over the group action and a union over at most `2^(An)`
profiles leave an exponential exception. The cell-mass exception is
discarded only once, rather than once per profile. The resulting bound
is simultaneous in every low-rank profile and consequently supports an
orientation-dependent effective space and basis. Fourier inversion gives
the stated `7/8` fraction. Independent tester blocks each have both
parities of probability at least `1/4`; combining their probabilities
with the `3/4` empirical cell-mass estimate yields the advertised
`beta=2^(-K^2-1)4^(-(g^2+1))`.

The key-only restriction is essential and is maintained: conditioning on
the sign itself as an input event could eliminate the opposite basis
assignment. There is no simultaneous assertion for all global key cells
at a finite n; the later use must involve prescribed finite collections
and then a countable limiting construction.

## Interface checks and remaining dependencies

- One-unit restrictions of inverse-polynomial mass multiply the mixed
  joint and marginal density bounds by a polynomial. Since `M0` is fixed,
  their logarithmic cost is `o(n)` as well as `o(N)`. Thus typicality,
  binary mixing and unary positivity still apply to that restricted
  sequence. Arbitrary pair-dependent conditioning would not preserve
  independent leaves; no such preservation follows from these lemmas.
- The large-set contradiction in Section 13 restricts a **one-unit** bad
  event and uses the mixed-law lemmas. It explicitly refrains from using
  individually normalized old-leaf bounds after that restriction. Its
  subsequent all-filter nets refer to the original prepared leaves, so
  this particular interface matches Section 09's hypotheses.
- Uniform integrability lets Section 13 choose a height bound before the
  net accuracy; the leafwise all-filter net is selected before the
  opposite independent leaf. These are compatible with the claims proved
  in Section 09. The weak-product and limit-density steps that convert
  the unary lower fractions into a full tuple hit bound remain outside
  this audit's independent conclusions.
- The preparation proposition remains conditional on the preceding
  phase alternative, tiny-cover fiber/pinning argument, injection lemma,
  and algebraic statement that the selected table is sufficient. I checked
  their interfaces and read the injection proof, but did not independently
  reconstruct every preceding phase argument.
- The `GL_Z` positivity and binary mixing conclusions remain conditional
  on the construction's mixer lemma. Its relevant proof was read and the
  uses of its bounds were checked; the full construction of the mixers
  is assigned to the preceding-section audit.

Accordingly, this scoped audit supplies no basis for rejecting the paper
at Sections 08–09, but also no basis for calling the paper verified or for
changing the HC7 research standing. A complete verdict still requires the
other audited links of raw supersaturation and the graph transfer.
