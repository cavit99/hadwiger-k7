# Internal audit: geometry and frame laws

Status: separate internal audit of the specified local statements; no certification of raw supersaturation or the claimed Hadwiger counterexample.

Pinned source: `openai/math`, revision `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

Audited primary files and SHA-256:

- `02-geometry.tex`: `763fb443a7973cedca448ba18fd5ee81c7928943afe5000169f714b72d7b1a9b`
- `03-frame-laws.tex`: `ad79930a09c568a39ad767c936b178befd8115e20304a85176a191b085274e91`

Read for interface: introduction, raw supersaturation statement in `03-distributions.tex`, the field convention in `preamble.tex`, and the order of choices in `14-parameters.tex:1–135`. All fields below are F_2, as specified by `preamble.tex:28`.

## Verdict within scope

I did not find a false assertion or unsupported inference in the two primary files after reconstructing their arguments. Their conclusions are materially weaker than raw supersaturation. In particular, these files establish a triangle-free hole relation and probabilistic control of fixed frame-image prescriptions, but do not establish that a general capped unit law has even one four-hole conflict. The mixer-existence theorem and the entire conversion of the leaf estimates into overlap remain external inputs to this audit.

The following are the individually reconstructed conclusions, with their precise scope.

## Geometry

1. **Hole relation, `02-geometry.tex:22–76`.** For arbitrary finite coefficient and ambient spaces, injective maps U_i, linear functionals u_i, a fixed linear a, and symmetric bilinear T, the stated witness relation is symmetric, loopless, and triangle-free. In the triangle proof, for each fixed j, the two left-hand summands agree by U_i x_ik = U_k x_ki. For each fixed i, the two T terms agree by symmetry. In characteristic two their sums vanish, whereas the three edge parity equations sum to 1. The argument needs no uniqueness of witnesses. Sampling positions with repetitions therefore gives alpha(G) <= 2 and chi(G) >= ceil(m/2).

2. **Moment and cut definitions, `02:145–239`.** The coefficient coordinates really do realize all displayed monomials. For a majority intersection of W_l, every O-coordinate is forbidden at some participating tag because it is allowed at only (g-1)/2 tags. Projection deleting all O coordinates fixes an intersection matrix and maps W into W_*, proving the intersection claim. The kernel of the complete cut map is the constant W_* tuples. This makes a_t, a, b_t well-defined: a_t and a vanish on a constant W_* tuple, and b_t receives g-1 copies of the same scalar. Symmetry of T and the identity T(x,x)=a(x) follow directly, independently of any genericity claims about the mixers.

3. **Self-Gram matrix, `02:242–256`.** Because j_* >= 1, each term (s_rho+s'_rho) z_#^T M_rho z'_# is bilinear in the chosen coefficient vectors. It vanishes at coincident evaluations. The ordered tester matrices consequently give <E,w>=eta(w) on the whole moment span. Z-coefficient changes preserve E because E has no rows or columns involving Z.

4. **Raw frame law and embedding, `02:258–321`.** For N >= 2(d+h), the given explicit completion establishes nonemptiness, even for a singular E. Taking uniform law on this finite set is unambiguous. There are at most 2^{2|E_components|N(d+h)} frames; with d=p_*[1+(g^2+3)n], fixed h and fixed M_0, its logarithm is O(N^2). Injective P,Q give an injective tensor map x -> P x Q^T. The pairing convention is consistent: <Y X^T,P x Q^T> contracts Y^T P and Q^T X, so the stipulated annihilator equations imply u_o U_o=0. No transposition error was found.

## Frame distributions and their quantitative scope

5. **Paired-frame orbit, `03-frame-laws.tex:19–42`.** With A,B individually injective, B^T is surjective. The proof constructs an isomorphism commuting with the two surjections by first extending the isomorphism of their kernels and then choosing corresponding quotient lifts. This proves transitivity for *each fixed full Gram matrix*, including degenerate ones.

6. **Gram normalization, `03:44–61`.** Conditional on an injective p-frame, prescribing all pq Gram entries costs exactly 2^{-pq}. A nonzero coefficient combination of the q minus columns is uniform on an affine fiber with translation dimension N-p. The union bound gives the stated lower probability, and ignoring minus injectivity gives the upper bound. For bounded p,q and sufficiently large N the lower bound is positive. At p+q=N the displayed lower bound can equal zero; the proof does not claim a positive constant uniformly in such unbounded p,q.

7. **Frame-image laws, `03:63–160`.** Uniformity of the plus frame follows from the simultaneous primal/dual action. Given that frame, minus columns are uniform on the displayed product of affine spaces, conditioned only on minus injectivity. The common translation space has dimension N-d-h; a union bound over nonzero column combinations proves the claimed failure bound. Given P,Q, the allowed X and Y choices and their rank restrictions separate, proving the stated conditional independence. The individual channel marginal is uniform on injective h-frames. The joint channel marginal is dominated by independent uniform columns by at most 2^{|E_components|(h^2+2)}, using the full-Gram orbits. This is a fixed constant in n, not a constant uniform in h.

8. **All-ranks fixed-image cap, `03:85–159`.** This is the strongest estimate in the audited files. Replacing a tested tuple by a nominal basis makes the plus prescription uniform on t_+ independent ambient vectors before the small injectivity correction. Given both plus frames, each minus column retains an independent uniform part on the common annihilator of their combined span. That annihilator has dimension at least N-2(d+h), so the minus prescription costs at most 2^{-[N-2(d+h)]t_-}. After the finite component factors the total bound is at most 4^{|E_components|} 2^{-Nt+2(d+h)t_-}. Once 2(d+h)/N < epsilon/2 and the fixed prefactor is at most 2^{epsilon N/2}, this is at most 2^{-(1-epsilon)tN} for **every** t>=1, including t=O(n). In particular the proof is not silently using bounded rank here. It requires fixed nominal directions and fixed prescribed images for the event being estimated.

9. **Sparse intersection profiles, `03:166–234`.** Choosing 2D independent common-image vectors yields a rank-2D nominal zero-image constraint. There are only 2^{O(n)} such choices since D and the component count are fixed. The joint density cap 2^{DN} and the preceding image cap make their union exponentially unlikely after M_0 is chosen. For a shared tensor, injective left and right factors preserve matrix rank and its column space is contained in the plus-span intersection. Hence total component rank <=2D. At most 2D tag pairs can carry unequal representation values. Without a strict majority, at least g^2/4 unequal pairs would occur; g=10^9+1 and D=4000g satisfy g^2/4>2D. Subtracting the majority value, which lies in W_*, gives the unique majority-zero representation with <=4D/g=16000 nonzero entries. The trace identity is correctly oriented: Tr(P lambda Q^T)=Tr(E^T lambda)=<E,lambda>. The two sparse representations have a common zero tag because 8D/g=32000<g, yielding chi_*(w_1)=chi_*(w_2).

10. **Two peelings, `03:280–429`.** The first peeling operates on original unnormalized mass, so a selected rank-u part has mass >2^{-zeta N-(1-zeta)uN} but at most 2^{DN-(1-epsilon)uN}. Thus (zeta-epsilon)u<D+zeta, strictly below K_1 when epsilon<zeta/4. This comparison also controls a whole high-rank violating tuple; there is no unaccounted large jump. Since every step adds nominal rank, a leaf is reached, and removing entire nonempty leaves terminates on the finite sample space. This proves the claimed uniform density bound and correctly preserves actual leaf weights.

For a single-law restriction retaining q=2^{-o(N)}, discarding leaves with individual retained fraction below 2^{-zeta N} removes at most 2^{-zeta N}/q. The surviving normalized restrictions lose at most zeta N bits, absorbed into the change from 1-zeta to 1-2zeta for all t>=1. In the second peeling, the number of parts is bounded by 2^{O(n)+u_0N}, provided u_0 is the *total* number of extra image directions across all components and signs. The cutoff 2^{-(u_0+1)N} loses exponentially little. The renewed argument uses an unconditioned reference-image event containing each refined part; independence modulo old pins guarantees independence of the selected new lifts in the full nominal space. No unjustified reference conditioning on rare pin images is needed. The displayed K leaves more than enough slack for K_1+u_0 plus the new rank bound.

11. **Walsh estimates, `03:433–482`.** The normalized and subprobability estimates follow from H H^T=2^d I and ||alpha f||_2^2<=max(alpha)||alpha||_1. A cross form on global vector slots has matrix C tensor I_N and rank N rank(C). The statements require independent groups and bounded weights separable between the two groups.

## Interfaces requiring separate audit

These are limits of the verified statements, not counterexamples to their actual wording.

- **No conditional channel injection estimate is supplied.** The bound 2^{q-h+1} in `03:73–77,115–119` is for an unconditional random channel evaluated on a fixed ambient q-space. It fails under arbitrary conditioning on P,Q, or for directions chosen from the same frame: X^T vanishes identically on im Q. Later uses must establish that the tested directions are independent of the channel or pay an appropriate domination factor.
- **No independent-leaf law survives arbitrary pair conditioning automatically.** The restriction/trimming argument in `03:295–316,366–384` is a statement about a single mixed unit law. Conditioning two units on a relation between their leaves or on their cross table can introduce dependence; it needs additional arguments.
- **Per-leaf bounds do not retain the endpoint marginal caps.** Only the mixed law, restricted at relative cost 2^{-o(N)}, has endpoint marginals bounded by M2^{o(N)} mu. A normalized leaf has the joint 2^{O(N)}mu^2 bound. The manuscript itself notes this at `03:319–325`.
- **The image cap is for fixed prescriptions.** Adaptive selection is justified within the peeling because each current part is bounded by its selected fixed image event. A later union over many image events, or frame-dependent directions, is not free.
- **O(n) is not o(N).** The local uses of 2^{O(n)} counts have coefficients fixed by the early parameters; those costs can be absorbed by increasing M_0. Any later test-dependent coefficient introduced after M_0 is fixed needs separate treatment. The present files acknowledge this explicitly.
- **External conditional input:** existence and all required properties of L_j^{ef}, R_j^{ef}, M_rho from `lem:generic-mixers` were not audited here. The basic triangle-free relation does not require their genericity, but later supersaturation does.

No computational enumeration, Lean, installations, or repository changes were used. This is a direct mathematical reconstruction of the specified finite-dimensional lemmas. It does not establish the manuscript's global claim.

## Targeted follow-up: unary positivity

At the parent's request, I independently challenged `09-histograms.tex:754–928` (lemma `unary-positivity`), concentrating on fixed global key cells, GL_Z invariance, and the martingale selection of moved row spaces. Additional exact source hashes:

- `09-histograms.tex`: `675d50021e381ed42d94b135c334067ea4ed2f9bda1aa097b4f2b37143974ee3`
- `04-moments.tex`: `63f77fce3714b1d74667be3ca67b2b024a8c136f70933248309f855f8ed3c70d`

**Conditional local verdict:** I found no counterexample or gap in the GL_Z/martingale inference, assuming the stated first property and low-rank profile count of `generic-mixers`, and the one-endpoint typicality estimate. This verdict does not independently certify the generic-mixer existence proof or the later common-limit use of positivity.

### Reconstructed symmetry and conditioning

Fix a profile x and a starting endpoint frame o. Let S_G be the coefficient-space change that applies G to all Z coordinates and fixes all others. The transformed primal frames are P S_G and Q S_G, at every component of that endpoint. Since E has zero Z rows and columns, S_G^T E S_G=E, and the same coefficient change preserves all injectivities and channel-annihilator equations. This is a bijection of the finite raw frame space, with X,Y unchanged.

For the key map, K_{oG}(z)=K_o(S_G z). Because every flavor retains all Z coordinates, their input law is invariant under S_G. Every tester summary and q depend only on non-Z bits. Consequently the conditional input mass of a *fixed global key cell* A_n is exactly the same for oG and o. After the change y=S_G z, its event E_0={K_o(y) in A_n} is fixed, whereas the basis character becomes s_x(S_G^{-1}y). The argument never requires T itself to be invariant.

The common GL change at all components is essential and is the one actually specified. A component-by-component change would not reparameterize the atom's one shared Z input; that invalid change is not used.

### Reconstructed rowspace and martingale estimate

The conditional generic-mixer input supplies a fixed rowspace R_x in (F_2^n)^*, bounded in dimension independently of n and independent of non-Z values. For each fixing of those other values, the quadratic character has polar rank at least 2(J-s_0). Under G the support rowspace becomes the inverse-transformed copy of R_x, uniformly distributed among spaces of that dimension.

For any fixed u previously chosen rowspaces, their sum has dimension bounded independently of n. The chance that another uniform copy has intersection dimension greater than s_0 is at most O_u(2^{-s_0 n}); one may count s_0 independent domain vectors and their possible independent target images. Thus a family of transformations of proportion more than 2^{-2An}, restricted to one bias sign, contains any fixed number u of successive choices with intersection dimension at most s_0, once n is sufficiently large. Here s_0=4 ceil(A)>2A provides the needed exponential margin. Although u can be enormous as delta or gamma decreases, u is fixed before letting n grow, exactly as the lemma permits.

Let F_j include all non-Z inputs and the row bits from the first j choices. The j-th sign is F_j-measurable. Conditional on F_{j-1}, its own row bits are uniform on an affine subspace of codimension at most dim(R_j intersect sum_{k<j} R_k)<=s_0. Restricting its polar form loses at most 2s_0 rank. Its conditional mean therefore has magnitude at most 2^{-J+2s_0}=b_* pointwise, including after non-Z inputs are fixed. Consequently D_j=s_j-E(s_j|F_{j-1}) are genuine martingale differences, with pairwise zero covariance and second moments at most one.

For a cell of conditional mass delta'>=delta/2 on which all selected signs have conditional mean greater than gamma, Cauchy–Schwarz gives

    (gamma-b_*) delta' <= |E[1_E0 u^{-1} sum D_j]| <= sqrt(delta'/u).

Taking u>2/[delta(gamma-b_*)^2] contradicts this inequality. The intrinsic bias term is correctly b_* delta', rather than b_*: the pointwise conditional-mean estimate is what makes the lower fraction independent of the cell mass. There is no requirement for E_0 to be measurable with respect to F_u in this Cauchy–Schwarz step.

### Uniformity over adaptively chosen low-rank spaces

For fixed x, integration of the preceding transformation bound over o is legitimate because the good cell-mass event is itself GL_Z-invariant and raw frame measure is invariant. The resulting raw bad-event probability is <=2^{-2An}. A union over <=2^{An} nonzero profiles costs only the displayed exponential factor. An orientation-dependent C_i causes no extra issue: the good event already controls every eligible profile simultaneously, hence all nonzero linear combinations in any selected basis. It depends only on the queried endpoint and so transfers to the mixed law using its marginal cap, even if C_i was selected using both endpoints. Since M_0 is fixed and a_n->0, a_n N=o(n).

Fourier inversion then gives the stated (7/8)2^{-dim C_i} lower fraction. The generic tester-summary probability bound is also consistent: each retained independent r_0-product tester has both outcomes with probability at least 1/4, conditioning on its compatible total parity q cannot lower the probability of a fully specified summary, and combining the 3/4 key-cell mass fraction with 7/8 exceeds 1/2.

### Counterexample attempts and exact limitations

- A cell chosen as the zero set of a basis character would defeat positivity, but it is an input-and-orientation-dependent event, not a prescribed global key set. The manuscript explicitly excludes it at `09:915–927`.
- A cell selected separately after observing each frame could likewise contain only one basis status. That also violates the deterministic common-cell hypothesis. Permitting A_n to depend on the overall law does not permit it to depend on the particular sampled orientation.
- A cell with reference mass tending to zero is outside the delta>0 assertion. The martingale length may depend on a fixed delta; the proof does not establish a uniform onset of asymptotics as delta tends to zero.
- An arbitrary additional input filter can destroy positivity. Only orientation-only subfilters preserve the established almost-sure limiting positivity, and even those need appropriate control if a quantitative exceptional-mass conclusion is used after exponentially rare conditioning.

No violating example satisfying the stated deterministic-cell hypotheses was found.
