# Internal audit: status constraints and rare overlap

**Scope and revision.** Read-only reconstruction of `build/sections/12-status-span.tex` (printed Section 13) and `13-rare-overlap.tex` (printed Section 14) in OpenAI, *A counterexample to Hadwiger's conjecture*, pinned repository commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Sources were read in full; adjacent definitions and precise dependency statements were inspected. This is a component audit, not independent verification of the whole paper.

SHA-256 of the audited sources:

```text
12-status-span.tex  4fba863525979503c82d6420ab58015e40f3e3772b98c024c11973ec6d067c20
13-rare-overlap.tex 64c67912930499eccb4d68b9be944ce99bf20515b5ec37d40085b0c220aaf1c1
```

**Verdict at this stage.** No independent false inference or counterexample was identified in these two sections. Their conclusions follow from the stated, strong preparation, positivity, histogram, weak-product, common-limit, realization and collision inputs. Those inputs are separately assigned audit obligations, not established by this report. In particular the proof has not been certified merely by reconstructing its concluding steps.

## 1. Exact interfaces on which this reconstruction depends

1. `prop:status-preparation`: after a single-unit restriction of mass `2^{-o(N)}`, the law retains joint density `2^{(D+o(1))N}` and individual marginal densities `M 2^{o(N)}`. Its final leaves satisfy the image bounds required by collision. In the no-prediction branch, the first effective spaces remain and iid unit pairs admit an injecting table with mass greater than `.99`. In predicted branches, the prediction errors vanish uniformly and the common classes and bit `c` are fixed. The rare branch additionally provides exact identities on the whole cut-profile space, compatible original leaf-pair mass at least `c0 N^{-4}`, and separate table-admissibility filters of mass at least fixed `a0>0`.
2. `lem:limit-model`: after averaging the leaf-pair record and dropping flags, the two orientation arrays are iid. Every feasible generic role/basis assignment has density bounded below almost everywhere relative to each common `(tag,q)` reference space. Finite discrete table data and positive table-passage mass survive. `prop:limit-overlap` forbids a usable passed option with positive matched unary overlap at every position under the vanishing-overlap hypothesis.
3. `lem:unary-positivity`: for any orientation-dependent effective space of dimension at most `K^2`, every member having total component rank at most `K`, each feasible tester-summary/basis assignment has the stated lower fraction on every prescribed sequence of common key sets with positive reference mass. The exceptional set may depend on the prescribed set; the proof here never assumes one finite-n exceptional set works for all sets simultaneously.
4. `thm:weak-product` supplies both its reference testing bound and its actual-query bound with orientation-dependent *unary* input weights. `lem:binary-mixing` has an exceptional set independent of those weights. Both apply under the mixed caps after a polynomial single-unit restriction. `lem:reference-product` supplies independent unary projections in the limit.
5. `lem:histogram-control` gives uniform small-set control and bounded-cardinality `L^1` nets, on each original normalized leaf, for all orientation-filtered query densities in each fixed numerical format. The net can be selected using its own leaf before the opposite leaf is sampled.
6. `lem:small-tables` supplies consistent binary prescriptions from scalar recipes. `thm:gradient-realization` applies to equal accepted keys. `prop:collision` charges retained-law mass and converts overlap `2^{-o(N)}` into four-hole probability `2^{-(k_max+.03)N-o(N)}`.

These interfaces are substantive mathematical inputs. Their validity cannot be inferred from the present sections' use of them.

## 2. Section 13: generators and dual constraints

### Available generators and surjection

For each pair of surviving labels and a common tag, fix a feasible `q` and any requested role/basis vector at either endpoint. The generic lower-density assertions make the product of the two aggregated status densities positive almost everywhere, hence its integral is positive. The aggregation contains finitely many tester and `p` statuses. At least one pair of finer statuses therefore has positive overlap. This yields a numerical generator above every base vector. Forgetting only two `p` bits consequently gives a surjection `V_ij -> B_ij` with kernel dimension at most two. The argument remains valid after exclusions whenever generic labels survive.

This uses the pointwise lower-density assertion, not merely nonzero separate marginal probabilities. That distinction is essential.

### `lem:status-duality`

The constraint map is linear over `F_2` on the direct sum of the four edge spans. The four coupled-equation coefficients are `s_j,r_i`. A relation supported only on the local constraints is zero because the projection onto `(q,h_A+h_B,x_A,x_B)` is surjective. Thus every nonzero obstruction has a nonzero coupled weight vector. Evaluating a general annihilating functional at the requested target gives exactly the sum of the displayed local right sides; the coupled targets are zero. This is standard finite-dimensional image/annihilator duality with all four edges retained.

### `lem:status-global-prediction`

The exchange of iid units interchanges the existence events `E_s,E_r`. If their union has mass at least `.1`, then `P(E_s)>=.05`. Fixing a relation with `s_j=1` makes two conditionally independent binary expressions agree at almost every common signature. Since the mismatch probability for independent bits is `a(1-b)+(1-a)b`, both expressions must be deterministic there.

Using one opposite generic label compares *all* surviving first-side labels and flavors against the same function; offsets are not selected separately for different labels. For a fixed opposite array:

- If `r_i=0`, generic positivity of all opposite role/basis assignments forces the opposite basis coefficients and beta coefficient to vanish. Only offsets `0,q` remain.
- If `r_i=1`, there is at most one deterministic opposite expression `p+c'x+alpha'h`, even across differing permitted exclusion sets. Two exclusion sets share a generic label because the universe exceeds `2B_*`; subtracting two claimed expressions and varying every role/basis assignment forces equal coefficients, then equal functions. This contributes that unique function and its translate by `q`.

There are at most four offsets for each endpoint and two choices of `j`, hence at most `2*4^2=32` pairs. Fubini supplies one opposite array with first-side mass greater than `.04`. One fixed pair of functions serves mass at least `.04/32=.00125`.

The transfer back to finite keys is legitimate conditional on the common model: approximate the two binary signature functions in reference measure by finite-cylinder functions. Since each unfiltered unary status measure totals exactly the reference measure, the replacement adds at most epsilon to every relation error. For fixed cylinders, the maximum over finitely many unary types and minimum over finitely many numerical coefficient/exclusion records are continuous functions of the status coordinates. Portmanteau on the strict error event gives prelimit mass at least `.000625`. A diagonal subsequence makes the error uniform and tend to zero. This exceeds the prediction threshold `10^{-6}` by a factor of 625, so negligible trimming cannot exhaust the margin. Unit-dependent marks and alpha coefficients are allowed by `def:prediction`; no unsupported common-mark requirement is being imposed.

### `lem:status-predicted`

Substituting the exact limiting predictions in a dual relation and varying generic role/basis assignments yields

```text
c_ij=s_j lambda_Ai, c'_ij=r_i lambda_Bj,
beta_ij=s_j d_i=r_i d_j,
s_j f_i+r_i f_j=gamma_ij q.
```

Hence `s_j e_i=r_i e_j` for all four index pairs. The cases are exhaustive: two zero classes; exactly one nonzero class (both weight vectors equal its support indicator); two equal nonzero classes (all four weights one); or two unequal nonzero classes (no nonzero solution).

For zero classes, exactification gives `p+a=T(lambda,.)`. Evaluating each coupled sum at the local targets gives `c+u(Delta)=0`, precisely rare/empty-status compatibility.

For nonzero coincident classes with support `S`, the `gamma` terms cancel: the defining functional equation is symmetric in indices and diagonal-zero, and `q` is not identically zero. The role terms total `|S|d` in `F_2`. The `a(lambda)` basis terms total `|S|c+|S|c=0`. The remaining cross contractions total `|S|d` by the prepared phase equation, so they cancel the role terms. This checks signs and support multiplicities for both support sizes one and two.

### `lem:status-span`

On the no-prediction branch, obstructable unflagged iid arrays have mass `<.1` and passed injecting tables have mass `>=.99` in the same limiting experiment. Their intersection has mass `>.89` by the union bound; no independence of these two events is required. Predicted branches use the retained positive mass of compatible tables and the preceding algebra.

### `lem:fresh-lists`

Every span has excess dimension at most two above its fixed base space. Exclusions can only decrease the span and preserve its full base projection while labels remain. Thus the sum of the four excess dimensions drops at most eight times. Deleting at most 100 labels per endpoint at each drop consumes at most 800 labels, and leaves a state stable under any further deletion of at most 100 labels per endpoint. The stated no-prediction bound `B0+900<B_*` and selector inequality leave ample labels; the predicted branch also includes its stored exceptions.

For any reserved label set in this allowance, let `H` be generated by zero-base words of lengths one to three with disjoint endpoint labels. Two lifts of the same base vector have equal classes modulo `H`: compare both to a third fresh lift. Fresh lifts of `b,c,b+c` prove additivity of the lift class. A zero-base generator itself lies in `H`. Therefore `V/H` is isomorphic to the base and `H=ker(pi)`.

Lift the target base by one fresh generator. A kernel of dimension at most two can be spanned by at most two zero-base words, each of length at most three; reserve labels before selecting the second. The list length is therefore at most seven and is nonzero even when a correction cancels some numerical status vector. Certificates and distinct labels distinguish occurrences. Processing four edges uses at most fourteen labels at an endpoint, plus bounded temporary comparisons, within the 100-label allowance. This is a valid short-representation argument despite the potentially large base dimension.

### `prop:positive-overlap`

There are finitely many numerical options independently of n. Negating the asserted positive subsequential overlap gives convergence to zero for every option. The common model then forbids usable passed options whose individual matched overlaps are all positive. The previous lemmas produce such a configuration on positive mass. Refining aggregated tester statuses is legitimate by a finite nonnegative sum; scalar recipes supply consistent binary prescriptions by the imported small-table lemma. Finiteness permits selecting one option with positive expectation. The argument does not need a pointwise uniform positive lower bound for the individual overlaps.

## 3. Section 14: rare overlap

### `lem:rare-large-set-hit`

For a fixed numerical request and key set W of reference mass at least delta, the claimed threshold is `c_hit=(1/4) kappa_min beta^4 delta`, with positive constants fixed independently of n. If the uniform superpolynomial bound fails, finite key spaces and finite requests provide a subsequence of deterministic W and one fixed request for which the bad event has probability at least `c n^{-p}`. Conditioning the *single-unit law* on this event multiplies both joint and marginal densities by at most `c^{-1} n^p`. Its log is `o(N)` since `N=M0 n` and M0 is fixed. The mixed caps and rank bounds persist. This does not claim preservation of the separately normalized old leaves.

Add W as a tuple signature bit, and close the countable test lists under weak-product approximants and their unary factors. At each finite stage the list complexity is bounded independently of n. Compactness gives a limiting reference rho, empirical status arrays theta, and averaged accepted measure tau. Every requested unary submeasure has density between beta and one: apply imported positivity to each fixed cylinder of positive limiting mass, discard its null exceptional event, and extend domination from the countable cylinder algebra. Feasibility and finite numerical formats persist as discrete data.

Both halves of weak-product comparison are required to identify

```text
d tau / d rho = kappa_request E_theta product_j h_j^theta(xi_j).
```

For actual queries, the status indicators are allowed unary weights, so the approximation and binary factorization apply. Finite products of recorded status integrals converge. For the reference side, its error bound is uniform over bounded unary key functions; extend first to cylinder-simple limiting densities, then to the h functions by L1 approximation and bounded domination. This identifies every tuple cylinder and hence the measures. It does not assert that W is a product set or use an illicit joint input filter.

With at most four positions, the density is at least `kappa_min beta^4` almost everywhere. Thus `tau(W)>=kappa_min beta^4 delta`, whereas each conditioned orientation gave mass below one quarter of this quantity. The contradiction proves the stated bound for each p. Its uniformity over deterministic W follows from the failure-sequence argument, not a simultaneous all-W event for each orientation.

### `lem:rare-superlevel-nets`

For a filtered density d with integral at least b0, its dominating original unfiltered leaf density has uniform small-set control. Since `nu{d>T}<=1/T`, choose T uniformly so that its integral on this set is below b0/4. Put `t=b0/4` and `delta0=b0/(2T)`. The region `t<=d<=T` carries at least b0/2 integral, hence at least delta0 reference mass.

An L1 epsilon-net representative f gives `W={f>=t/2}`. At most `2epsilon/t` of `{d>=t}` is omitted, so `nu(W)>=delta0/2` when `epsilon<=delta0 t/4`. Also `nu(W intersect {d<t/4})<=4epsilon/t`. The bounded family is formed over all orientation filters using the B-leaf alone. Constants t,delta0 precede epsilon; its later cardinality remains constant in n.

### `prop:rare-overlap`: recipes

Select one generic atom per cross edge with q=1. On side A choose all ordinary tester bits zero and the shared bit one, giving role zero. On side B choose one permitted ordinary bit one and the shared bit zero, giving role one. The generic flavor at any tag has permitted ordinary blocks, so these summaries are feasible. Select distinct allowed labels at each endpoint.

Prescribe basis values equal to `(a+cross contraction)|C_i`. Old lambda marks belong to the final effective spaces. By symmetry and the exact identity `p_i+a=T(lambda_i,.)`, these prescriptions imply that the coupled sum at each facing endpoint is `c+u(Delta)=0`. Hence all scalar recipe equations hold; the p bit is already fixed by the basis assignment and role, so no further p-status filter is necessary. Binary prescriptions and subsequent realization are imported exactly under these hypotheses.

### `prop:rare-overlap`: exceptional mass and adaptive choices

Binary mixing and unary positivity for the full key cell give a uniform positive successful-query mass for every feasible request outside exponentially small mixed orientation mass. There are only finitely many requests. Markov over original B-leaves shows that outside exponentially small leaf mass, every admissibility filter of mass at least a0 retains at least fixed b0>0 query mass. These removed leaves cost `o(N^{-4})` under the independent original leaf-pair law, even before restricting to compatibility.

Build B-leaf all-filter nets, then set `delta=delta0/2`, `A0=(a0/2)c_hit(delta)`. Uniform original A-leaf small-set control yields eta so that any reference set of measure at most eta carries A-query mass below A0/2. Choose `epsilon<=min(delta0 t/4,eta t/4)`. All constants through the resulting net cardinality L are fixed independently of n.

For each fixed B-leaf, its at most CL relevant large sets are deterministic relative to an independently drawn A-orientation. The large-set hit estimate therefore bounds the averaged A bad probability by `CL e_n`. Markov shows that pairs with conditional bad probability above a0/2 have mass at most `2CL e_n/a0=o(N^{-4})` (take p=4 or larger and use fixed M0). This union covers every set in the preselected B family, so allowing the eventual table/filter to depend on the A-leaf introduces no extra uncharged adaptivity.

On every remaining compatible pair, at least a0/2 of A-orientations pass the selected admissibility filter and hit its feasible selected W; thus `integral_W d_A>=A0`. The request is fixed in the bounded leaf/table coordinates; all orientations in that filter meet its label and basis-format requirements. Let `H=W intersect {d_B<t/4}`. Then `nu(H)<=eta`, so

```text
integral d_A d_B >= (t/4)(integral_W d_A - integral_H d_A)
                    >= t A0 / 8.
```

At least `(c0/2) N^{-4}` compatible pairs remain after the two `o(N^{-4})` losses. The expected overlap is therefore at least `(c0 t A0/16)N^{-4}`, as claimed. Original normalized-leaf caps are used only for their nets/small-set controls, not for the polynomially restricted law in the earlier contradiction.

## 4. Completion and quantitative scope

Failure of a uniform sufficiently-large-n supersaturation theorem would give an increasing sequence of n and violating admissible unit laws. Fixing mixers before selecting these laws is expressly required. Preparation and the two overlap alternatives apply along subsequences to such a sequence. Positive constants and `N^{-4}` are both `2^{-o(N)}`. Returning from a retained single-unit law of relative mass `2^{-o(N)}` costs its square for two independent draws, still `2^{-o(N)}`, as charged by collision.

The resulting lower bound is `2^{-(k_max+.03)N-o(N)}`. With `k_max=56(g-1)`,

```text
100g - k_max - .03 = 44g + 55.97 > 0.
```

It exceeds the violating threshold `2^{-100gN}` eventually along every such sequence. This contradiction legitimately proves uniformity over admissible laws without requiring an explicit uniform numerical onset from each compactness step. The final passage to arbitrarily large graph orders then uses the separately audited raw-to-graph proposition and fixed `M0` in `m=2^{C0 g M0 n}`.

No standalone moment/row-rank estimate is proved in these two sections; the profile rank, basis dimension, binary mixing rank and construction-order inequalities are imported from the earlier sections and Appendix A. This report checks their precise uses, not their independent validity.

## 5. Outstanding status

This audit does not identify a failure or unresolved local step in the concluding status/rare-overlap mechanisms. The exact uses of preparation, mixed-law positivity and mixing, original-leaf all-filter nets, and product/common-limit comparison have been matched against their statements. The sibling reports `audit-preparation.md` and `audit-common-limit.md` record conditional internal passes for those inputs, and the parent reports completed checks of phase preparation, the parameter order, graph transfer and the uniform-law contradiction. These are matched interfaces rather than additional unexamined obligations of this scope.

At the time of this report, the only sibling verdict still awaited by this auditor is the algebra/collision audit: the applications of `lem:small-tables`, `thm:gradient-realization` and `prop:collision` match their precise source statements, but independent verification of those statements belongs to that assigned scope. There is no further unmatched interface identified within Sections 13–14. Component passes remain internal mathematical scrutiny, not external peer review or a formal verification of the full paper.

No repository files were edited; no Lean build, installation or external code was run. This report is an internal reconstruction of the named pinned sources, not external peer review.
