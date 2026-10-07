# Adversarial screen of raw supersaturation

Status: **No counterexample obtained; this is not a validity certificate.**

Scope: direct attempts to construct a probability law contradicting raw supersaturation, independently of the section-by-section proof audits. No Lean or finite model computation was used. No repository files were changed.

Source revision: `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

Inspected sources and SHA-256:

- `02-geometry.tex`: `763fb443a7973cedca448ba18fd5ee81c7928943afe5000169f714b72d7b1a9b`
- `03-distributions.tex`: `368e4688ce3d554193253fe2c4f9e30a6567969056d78c123fc7425168d627e4`
- `03-frame-laws.tex`: `ad79930a09c568a39ad767c936b178befd8115e20304a85176a191b085274e91`
- `14-parameters.tex`: `8dd92c10cddcc9d31c171120773035a54e4832d74ceba99322500e9d499c007c`

## Exact target

A unit is an ordered raw pair with no hole. Let `mu` be uniform on the finite raw frame space. The claim quantifies over every unit law `sigma` satisfying the pointwise bounds

`sigma_1 <= M mu`, `sigma_2 <= M mu`, `sigma <= 2^(D N) mu^2`,

where `M=2^1000`, `D=4000g`, `g=10^9+1`, `N=M0 n`. It concludes that two independent units have all four cross holes with probability at least `2^(-100gN)` for every sufficiently large `n`. All construction constants precede `n` and the law; in particular `d=dim B=p_*[1+(g^2+3)n]` grows linearly in `n` whereas `h` is fixed.

## 1. Exact and almost diagonal attacks fail the cap

For any law supported on the exact diagonal, the joint cap implies

`1 <= 2^(DN) mu^2(diagonal) = 2^(DN)/|Omega|`.

At each component every injective plus frame `[P,X]` occurs: the prescribed Gram constraints admit a minus completion, and the simultaneous general-linear action is transitive on plus frames. If `q=d+h`, the number of plus frames is

`I(N,q)=product_{j=0}^{q-1}(2^N-2^j) >= 2^(Nq-1)`

when `N>=2q` and `N` is large. Hence

`log2 |Omega| >= |E| [N(d+h)-1] = Omega(N^2)`.

The diagonal support therefore has vanishing maximum allowed mass. This excludes the tempting coupling `(O,O)`, despite its exactly correct marginals.

Agreement of the entire primal frame `P` at even one component has reference probability `1/I(N,d)`, again `2^(-Omega(N^2))`, so it cannot support an admissible law. Agreement on all but a fixed number of ambient rows of `P` has the same quadratic-order cost. These attacks do not exploit an overlooked exception in the joint cap.

Agreement of the full channel `X` at every component also fails: its reference probability is `I(N,h)^(-|E|)`, at most `2^|E| 2^(-|E|hN)`, and `|E|h>D` already for the displayed constants. This conclusion uses only the uniform injective channel marginal.

## 2. Fixed low-dimensional support attacks fail marginal control

If both endpoint laws are supported on a set `S`, marginal domination requires `mu(S)>=1/M`. For a fixed codimension-`c` ambient subspace, the event that a component's whole `P` image lies in it has probability at most `2^(1-cd)`. For fixed `c>=1` this tends to zero as `n` grows. A fixed finite union of such supports does not repair this.

This argument does not exclude adaptive shared subspaces, randomly mixed supports, or constraints on only boundedly many coefficient directions. Those are legitimate remaining adversarial choices, rather than automatically invalid examples.

## 3. Latent-feature couplings are genuinely allowed, but I did not make them conflict-free

There is a broad exact family worth distinguishing from the invalid diagonal law. Let `f` partition the uniform raw space into `L` cells of equal measure, and set

`rho(x,y) = L mu(x) mu(y) 1[f(x)=f(y)]`.

Then both marginals equal `mu`, and `rho<=L mu^2`. The hole relation is triangle-free. Mantel's inequality in each uniform finite cell implies that two independent elements of that cell have a hole with probability at most `1/2`. Thus `rho(unit)>=1/2`.

After conditioning on units, the resulting law satisfies

`sigma_i<=2mu`, `sigma<=2L mu^2`.

Consequently every such feature partition with `2L<=2^(DN)` yields an admissible adversarial law. Equal feature values may encode parity classes, short coordinate records, and bounded shared information. (Equal-size partitions are assumed here; none is asserted for an arbitrary requested cell count.)

I found no choice of the feature partition for which every pair of units in this support lacks a four-hole conflict. Equality of one or several parity records is not by itself an obstruction to the four cross equalities: those involve possibly different cut profiles. A valid counterexample would need an additional algebraic implication forbidding the entire four-hole event, not merely suppressing a chosen witness list.

## 4. Adaptive ambient-functional attempt did not close

If a fixed ambient linear functional `A` satisfies `A U_o=a` at every raw vertex in a set, that set has no holes: applying `A` to the shared-vector equation forces equal values of `a`, contrary to the hole parity requirement. This suggests coupling two endpoints that share such a certificate.

The obstruction is that a fixed certificate does not come with a raw set of measure at least `1/M`; no such positive-mass certificate class was obtained. Randomizing the certificate can restore marginal entropy, but units then have different certificates. For a cross shared tensor `xi`, the hole condition is compatible with `(A+B)(xi)=1`. Four such conditions are even in number and give no contradiction without an additional relation among the four shared tensors. I did not establish that relation.

Likewise, matching only a bounded number of primal or channel directions can fall within the `O(N)` correlation budget. It does not establish equality of the complete raw frames, and I found no deduction that forces all future hole witnesses into those stored directions. Promoting that deduction would repeat the exact ownership/compatibility issue the construction is meant to address.

## Judgement supplied by this screen

The elementary diagonal, fixed-support, and full-channel counterexamples do not satisfy the claimed hypotheses. Admissible correlated laws remain very broad, as the latent-feature construction demonstrates. No admissible law with provably absent or too-rare four-hole conflicts was obtained.

Therefore this independent adversarial screen supplies **neither a disproof nor a proof** of raw supersaturation. The claimed Hadwiger counterexample still requires the substantive distribution proof and its graph reduction to survive the separate audits. Failed simple attacks must not be reported as establishing validity.
