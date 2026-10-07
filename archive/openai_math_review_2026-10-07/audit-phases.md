# Independent local audit: collision and phase arguments

Status: separate internal audit; no local contradiction or unsupported inference found in the audited arguments, conditional on the explicitly listed dependencies. This is not a certification of the claimed counterexample or its full proof.

Audited revision: `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

Exact primary-file SHA-256 hashes:

- `06-collision.tex`: `562df1b42179ebf7426d805487bb477cb7325bc16917a1f1031d5aa6f26e8b89`
- `07-phases.tex`: `1a9cc928b4a3aee0acc755d9d2d89d6e8717516e3bb386ef241d6369818f4b1f`

Scope: the full contents of these two files, with relevant definitions and interface statements inspected in `02-geometry.tex`, `03-frame-laws.tex`, `05-realization.tex`, and the numerical ledger `14-parameters.tex`. This audit reconstructs the pivotal deductions rather than checking prose alone. It does not independently establish the gradient-realization theorem, the peeling theorem, the eventual overlap bound, or the proof's later status classifications. No computational experiment was needed for the local deductions below.

## 1. Collision criterion

**Dependencies actually required.** The query must be a product experiment conditional on its two leaves; its acceptance on each side must be unary. The (k) nominal key directions must be independent modulo pins, jointly across both endpoints and separately by component/sign. The normalized leaf law must satisfy the final exact-image bound for *all* ranks, not merely bounded ranks. Gradient realization must produce a target depending only on the numerical records and must require fewer than (.01N) tested Gram bits. These are substantial external dependencies, not consequences of this section.

**Pruning and independence (lines 98–179).** At fixed leaves, key (q), and parameter pair ((a,b)), opposite pin/key images are fixed. Each record cell is therefore a condition on one orientation only, although its definition can use the opposite parameters. The two conditional orientation laws remain independent. Crucially, the proof does not intersect cells over different opposite parameters.

If the mass of every removed A-cell is below $\tau=2^{-(k+.01)N}$, its collision-mass loss at key (q) is at most (L_n\tau\beta_b(q)). Summing keys costs no factor $\lvert\mathcal K_n\rvert$, since $\sum_q\beta_b(q)\le1$. Converting probability to the overlap integral then multiplies by $\lvert\mathcal K_n\rvert$. Thus total overlap loss is at most

\[
2|\mathcal K_n|L_n\tau\le 2^{1+Cn-.01N}.
\]

This is exponentially small once (M_0) makes the record count exponent strictly less than (.005N). No hidden union over parameter choices is needed: their probability weights are averaged.

**Retained-cell entropy (lines 181–202).** A prescribed rank-(t) tuple modulo pins and keys, together with the known key images, is a rank-(k+t) exact-image event modulo pins. Dividing its original upper probability by the cell mass gives exponent

\[
-(1-2\zeta)t+.01+2\zeta k\le-.95t
\quad(t\ge1).
\]

Here $2\zeta k\le.002$. This arithmetic holds also for (t=O(n)). It would not follow from an image bound valid only for fixed-size tuples.

**Fourier step (lines 204–255).** The kernel of quotienting both factors of a tensor product is exactly the sum of tensors with a frozen factor. A zero quotient character is consequently one, because target and actual forms agree on frozen entries. For a nonzero quotient matrix of rank (t), a rank factorization uses a rank-(t) tuple on each unit. The two cross orientations use opposite signs, so their nominal ranks add. Applying the Walsh operator norm to independent tuples with point masses at most $2^{-.95tN}$ yields $2^{-.45tN}$. There is no need for separate independence of Gram bits. At fewer than (.01N) tested bits, agreement has probability at least $2^{-.02N}$.

**Final mass accounting.** The collision probability is at least $2^{-o(N)}/|\mathcal K_n|$. The independent-query success event is contained in the four-hole event, even if a single orientation pair has multiple query certificates. Returning from the normalized restricted law to the original law costs the square of its restriction mass, still $2^{-o(N)}$. The exponent $k_{\max}+.03<100g$ is correct. Boundedly many shapes/options cost only a constant. I found no local defect in this implication.

## 2. Rank growth without a cover

The deterministic rank inequality is valid: putting projected tensors on separate formal summands gives block-diagonal rank at least the number of nonzero tensors, and applying the two addition maps loses at most their kernel dimensions $\delta_C+\delta_R$.

For a random ordering of the realized mode spaces, submodularity gives decreasing expected increments (a_t). For the dyadic tail quantities, the first-half average is at least (f_{j+1}), giving

\[
v_j\le f_j-f_{j+1}+\tfrac12v_{j+1}.
\]

Summation yields $\sum_{j<m_r}v_j\le2(f_0-f_{m_r})-v_0+v_{m_r}\le2r$, using (0\le v_{m_r}\le f_{m_r}). The two modes therefore have a scale with deficit at most a quarter of the remaining count. Low original rank then forces at least $q_rs/2$ remaining tensors into the exposed cover. Although the exposed subset was selected using the realized list, the union bound over disjoint fixed sets (E,J) repairs that adaptivity: conditional only on (E), the (J) tensors are independent. The resulting $4^sp^{q_rs/2}$ bound follows. I found no omitted independence assumption here.

## 3. Phase alternative

**No large cover.** Expanding the even moment against iid channels gives the stated $2^{-h\operatorname{rank}(\sum\Delta_j)}$ upper bound after discarding signs. Selecting both endpoints only improves it. The marginal comparison to iid channels is unconditional and has an (h)-dependent constant, which is harmless as (n\to\infty). A union over at most $C_r2^{2rN}$ rank-bounded candidate values of the adaptive $\Delta_B$, followed by the original joint density cap, is paid by $\Gamma=D+2r+10$. Thus the eventual adaptive mark is legitimately inserted.

**Large-cover offsets.** After deleting exceptional primal spans meeting the fixed cover, quotient projection is injective on each endpoint's primal span. Equality of the quotient tensors permits a common shortest factorization with unique endpoint lifts. Their difference has the displayed three-term expansion. Choosing independent offset bases gives independent companion tuples within each component and mode. Changing the reference endpoint changes companions only by combinations of recorded offsets. The record count $2^{2r^2s+O(1)}$ and its (.002N) allowance are valid because $s\le10^{-12}(1+r)^{-4}N$.

**Singleton estimates and a conditioning trap that is avoided.** The transpose-injectivity bound is *not* valid for a space chosen using the same channel, nor uniformly after conditioning on arbitrary primal frames. The uses here avoid those assertions: singleton tests fix A's offset list and test the independent B marginal; fixed-cover tests use a globally fixed ambient cover; fresh-probe tests use witnesses fixed by averaging before B is sampled.

For the subsequent conditional output count, a different argument is used. At fixed offset record, enumerate the nominal representation of B's companions, prescribe its primal images, and condition on the primal frames. Freeze the finite channel coefficient lists. On the full-rank event, prescribing their images costs at least $(N-\dim\mathcal B)t_A$ bits under independent channels in the appropriate annihilators. Ignoring the equations that generated the frozen coefficients enlarges the event; it does not falsely assert their independence. Enumeration of coefficient lists is constant in (n). This gives the joint point bound claimed in the source and the $2^{-.481N}$ retained contribution after record summation. The discarded contribution is only a fixed small constant, which is appropriate for the first alternative.

**Frequent-output argument (lines 483–547).** If frequent-pair mass exceeds $\delta$, positive B-mass sees frequent A-mass at least $\delta/2$. At each probe step, failure to produce a fresh offset is below $\delta/4$ because the previous offset span is a cover of dimension below (d_0). Averaging therefore fixes (L_0) probes with independent selected witnesses and successful B-mass at least $q_*$. Witness selection depends only on probe lists. The unconditional B-marginal transpose bound can then remove less than $q_*/2$.

The most important adaptive-counting point is lines 509–520. Under raw $\mu^2$, conditioning on endpoint 2 and endpoint-1 primal frames, then enumerating the nominal companion tuple, determines its ambient value (z). There is no extra $2^{t_BN}$ enumeration. The lists $\mathcal F_v(m,z)$ are then fixed. Their projected output choices cost at most $2^{.51L_0N}$; the full-rank channel output count costs at least $2^{-.99L_0N}$. The exponent $D+.012-.48L_0+O(n/N)$ is negative. The remaining Walsh exponent (-.245N), even after the (.004N) record count, is also negative. I found no local gap in this branch.

## 4. Injection and tiny-cover consequences

**Injection on accepting pairs.** For a fixed accepting set of mass at least $2^{-.01N}$, the mixed marginal cap controls intersection of a new entire primal span with all previously selected witness spaces. Hence a B with failure probability above $\eta$ has an $\ell$-probe all-failure test of probability at least $c^\ell$ using independent witness spaces. Conversely the raw B channel costs $2^{-(h-K)\ell}$, witness enumeration costs $2^{K\ell}$, and adaptive protected coefficient spaces cost only a constant in (n). The union over the stipulated $2^{C_sN}$ accepting family is paid by the displayed lower bound on (h). Small accepting sets contribute at most their threshold, not the threshold times the family size. The exponential error is negligible relative to inverse-polynomial acceptance. The family-size hypothesis remains essential.

**Tiny-cover part (a).** The entropy argument for an alternating kernel is valid. On the retained row set, a row basis has (O(N)) evaluations, each with vanishing probability of zero; their total entropy is (o(N)). A largest fiber has mass at least $2^{-o(N)}$. All rows are constant on this fiber, and the zero diagonal forces the fiber's entire alternating kernel to vanish.

**Tiny-cover part (b).** Over $\mathbb F_2$, $(1+F)\odot(1+F)^T=I$ on an incompatible set because (F(A,A)=0). Hadamard-product rank at most $(1+\operatorname{rank}F)^2$ bounds its size. Sampling $R_N^2+1$ points, including possible repetitions, then gives the stated $\Omega(N^{-4})$ compatible-pair lower bound. The four even/even Fourier characters contribute exactly one quarter of this probability to either all-zero or all-one four-bit pattern; the other twelve have exponential error. This parity calculation is correct.

**Tiny-cover part (c).** At most (4K_1) support-image pins determine the two old marked tensors. At most (2d_0) channel-image pins determine both functionals on the cover tensor space. Their scalar metadata has bounded length in (n), and nominal support descriptions have (O(n)) length. Conditional on the separate peeling theorem, the claimed leaf measurability and preservation of inverse-polynomial pair mass follow.

## Verdict and limits

No counterexample or first unsupported step was found inside the two assigned sections. Their difficult local arguments withstand the reconstructions above. The audit does **not** justify a global validity verdict: the collision theorem is conditional on a deterministic gradient completion, uniform all-rank leaf entropy, and an actual subexponential overlap bound; the phase application still requires the later preparation/status branches to meet their hypotheses. Those interfaces must be checked independently before the manuscript's claimed Hadwiger counterexample can be accepted.
