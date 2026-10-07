# Internal algebra audit: moments and gradient realization

Date: 2026-10-07.

Status: separate internal audit of the exact sources identified below. The substantive arguments in Sections 5 and 6 have been reconstructed without an identified counterexample or unsupported algebraic inference. This verdict is conditional on the explicit definitions and parameter hypotheses listed below. It does not certify the later occurrence estimates, Raw supersaturation, or the main theorem. No Lean verification or execution of release-supplied code was performed.

## Revision and scope

Repository: `openai/math`, commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

Source directory: `preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/build/sections/`.

Primary audited sources:

| Source | SHA-256 |
| --- | --- |
| `04-moments.tex` | `63f77fce3714b1d74667be3ca67b2b024a8c136f70933248309f855f8ed3c70d` |
| `05-realization.tex` | `db694b0fd414c1ba4419c0af9cbec9cf29b2276375cc0ba58a35012dfc01a619` |

Interfaces inspected, without treating the entire surrounding sections as audited here:

| Source | SHA-256 |
| --- | --- |
| `02-geometry.tex` | `763fb443a7973cedca448ba18fd5ee81c7928943afe5000169f714b72d7b1a9b` |
| `03-frame-laws.tex` | `ad79930a09c568a39ad767c936b178befd8115e20304a85176a191b085274e91` |
| `14-parameters.tex` | `8dd92c10cddcc9d31c171120773035a54e4832d74ceba99322500e9d499c007c` |
| `preamble.tex` | `2f7af1f50a6b84551b057c5dd311419b51a8dd2434c5c4eb371d3ab9af2de32b` |

The preamble numbers theorem-like environments jointly within sections. Thus the relevant named statements are Lemma 5.2 (Label support), Lemma 5.5 (Uniform mixing forms), Lemma 6.2 (Table flags and binary prescriptions), and Theorem 6.3 (Gradient realization). Numbering is derived from the source, not from a compiled PDF.

Permanent sources: [Section 5](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/build/sections/04-moments.tex), [Section 6](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/build/sections/05-realization.tex).

## Hypotheses retained throughout

All algebra is over F_2. The selector monomials have degree at most j_*, the base coordinates are affine-linear, and W is the span of the point moments v(s,z)v(s,z)^T. The tag spaces W_l require specified entire O-blocks to vanish. The cut domain consists of x_{ll'} = w_l + w_{l'} with w_l in W_l. In particular, its component matrices are symmetric Boolean moment matrices, not arbitrary matrices.

The pin spaces are nominal subspaces of the direct sum of the two endpoints' primal and channel spaces. Their total dimension, summed over components and signs, is at most K. Pins may mix endpoints and channels. Individual projected spaces S_{i,e}^± are projections, not intersections. Each fixed endpoint and sign consequently satisfies sum_e dim S_{i,e}^± <= K. The separate protected channel projections H_{i,0}^± and chosen complements H_{i,1}^± are used with their actual signs.

The parameter requirements used locally are R_* = 2K+40; j_* >= 10(K+1)(R_*+20); sufficiently many selector bits b; A = 10(K+1)p_*(g^2+5); s_0 = 4 ceil(A); J > 100(s_0+K^2+1); then sufficiently large r_0 with h = 1000r_0; then sufficiently large M_0; and finally sufficiently large n. The tag count is the specified odd g > 2. The relevant choices are acyclic within these sections.

## Section 5 reconstruction

### Lemma 5.1: base moments and selector independence

The explicit point-matrix sums produce a basis for all symmetric matrices satisfying Z_ii = Z_0i. The zero point supplies the constant entry; zero plus one unit point supplies the three entries associated with one base bit; the four-point sum on a two-bit coordinate plane supplies the symmetric off-diagonal pair. These supports are independent and exhaust the free coordinates.

For u distinct selectors, the product of u-1 separating affine coordinate functions isolates any specified selector. It remains a Boolean polynomial of degree at most u-1, even when coordinates repeat. Therefore the evaluation vectors are independent when j_* >= u-1. This is used below only within the stated interpolation budget.

### Lemma 5.2: label support

The following potentially delicate steps were checked separately.

1. The restricted pairing ranks r_j are nondecreasing because the matrices are nested principal submatrices. There are at most R_* increases. Between levels 4R_*+2 and 6R_*+4 there must be two consecutive zero increments: otherwise a binary sequence of 2R_*+2 increments without two consecutive zeros has at least R_*+1 nonzero increments. Thus the required three equal ranks occur with j+2 <= j_*.
2. If the restriction to V_j and the pairing on V_{j+2} have equal rank r, the image of V_j in Q = V_{j+2}/rad(B) has dimension exactly r and is all of Q. Its restricted radical is therefore the intersection with the full radical. No positivity assumption is required for this inference.
3. Multiplication by one selector bit is well defined on Q: a representative f in V_j with zero class pairs to zero with s_a g, and the images of g in V_j span Q. For commutativity and idempotence, replacing s_b f by a representative in V_j is legitimate because their difference is radical on V_{j+2}; it can be paired with s_a g in V_{j+1}. Thus the transferred product identity lies entirely inside the available degree range.
4. Commuting idempotents split into F_2 eigenspaces. Self-adjointness makes distinct joint eigenspaces orthogonal. The induced pairing on each summand is nondegenerate. The projected base-coordinate vectors define symmetric matrices Z_s with rank bounded by dim Q_s.
5. Products of selector multiplication operators recover all monomial classes through degree j, hence all moments through degree 2j. A selector interpolant e_s of degree at most |L|-1 represents the eigenspace projection. The Boolean identity for z_i e_s gives (Z_s)_ii = (Z_s)_0i. There is sufficient degree for these expressions.
6. The recovery of higher degrees is not an unproved flat-extension assumption. A first nonzero discrepancy of selector degree d' > 2j yields an identity submatrix indexed by equal-sized subsets A of its support U and complementary column subsets U minus A'. Off-diagonal unions have smaller degree; diagonal unions equal U. Both row and column degrees fit within j_* because d' <= 2j_*. This gives rank binomial(d',floor(d'/2)) > 2R_*, contradicting the rank bound for the difference.

The Laurent–Mourrain reference is motivational here; this reconstructed proof does not require importing a positivity-based flat-extension theorem.

A further consequence used in Section 6 is justified: when the label factors are independent, congruence to a direct sum shows that the matrix rank equals the sum of the label-block ranks. Removing selected label blocks therefore cannot increase rank or support size.

### Lemma 5.3: sparse pin-label exclusion

Choose a basis for the span of the sparse members of one projected pin space, using sparse members themselves. There are at most K. Comparing any other sparse member with its expansion in that basis uses at most (K+1)(R_*+14) labels. The selector interpolation budget makes their evaluation factors independent. Thus a new label cannot occur outside the union of the chosen basis supports.

This argument also deals with apparently nonunique sparse expansions: their differences are within the same independence budget. Summing the per-space bound over two signs and all components gives the stated, conservative B_0. The conclusion applies to arbitrary projected mixed pins; it does not assume each pin belongs to an individual endpoint.

The effective-space bounds follow from

- dim C_i <= sum_e dim S_{i,e}^+ dim S_{i,e}^- <= K^2;
- sum_e rank x_e <= sum_e dim S_{i,e}^+ <= K for x in C_i.

Enlarging pins enlarges each projected space and therefore C_i. Retaining old effective spaces introduces no incompatibility.

### Definition 5.4 and Lemma 5.5: atoms, flavors, and uniform mixers

Every flavor retains the full Z and # blocks. That requirement is essential in both mixer estimates and is explicitly present.

For the unary statement:

1. Every symmetric rank-r component has a factorization ZHZ^T with Z full column rank and H nonsingular symmetric. Taking a left inverse of Z proves the factorization without a diagonal or nonalternating hypothesis.
2. Counting the column matrices, middle matrices, and rank tuples gives a bound of the form 2^{p_*(g^2+3)Kn+O(1)}. The stated A is more than sufficient.
3. For a fixed profile and atom tag, the forward and reverse L/R restrictions give at most m_0 = 4J(g-1)K formal linear forms. Their formal quadratic is a sum of products on disjoint variable pairs. Since the profile is nonzero, every j contributes a nonzero block, giving polar rank at least 2J.
4. The actual restrictions of one random L need not be independent. The compatibility argument correctly allows that dependence. The full map L -> (Z_e^T L, L Z_f) has image codimension r_e r_f. Restricting to the free Z directions is a surjective projection of the ambient pair of matrix spaces, so it cannot increase this codimension. The induced distribution is uniform on its image and is dominated by 2^{r_e r_f} times the fully uniform law. Across both L and R families, the exponent is at most 2JK^2.
5. The union bound over s_0+1 independent row relations gives the stated corank probability. Multiplying by the profile count still tends to zero because s_0+1 > A. Non-Z values and flavors affect only affine shifts, so they require no growing union bound.
6. Restricting the formal polar form to a subspace of codimension at most s_0 loses rank at most 2s_0. Pullback by the surjection from the Z-coordinate space to its image preserves the remaining rank. The formal linear forms also give the claimed bounded-dimensional row-bit space independently of the non-Z fixing.

For the binary statement:

- Distinct selector evaluations make their Z direction spaces disjoint. For one arbitrary random matrix, the two ordered restrictions are independent off-diagonal blocks in a basis adapted to these spaces. A parity using one or both orders of that matrix is still uniform after the other matrices are fixed.
- For E alone, the # restriction is a uniform A, its transpose, or A+A^T. In the last case a square off-diagonal block on disjoint index sets is uniform. A full matrix has rank at least the rank of that submatrix.
- The elementary rank-factorization count yields exponentially small probability in n^2 for rank below n/5. The number of label pairs and indexed parities is fixed in n. The two mixer properties can therefore be imposed simultaneously before choosing any unit law or pins.

No assumption of symmetric random L/R matrices was made; such an assumption would invalidate the two-order independence argument, but it is absent from the construction.

### Remark 5.6: exact scope of the symmetry

A common invertible change of the Z input block at one vertex sends P,Q to P A_B,Q A_B and leaves channels fixed. Since E has zero Z rows and columns, A_B^T E A_B = E. All raw self-Gram conditions and injectivities are preserved, giving a bijection of the uniform raw frame space. A change of variables in the uniformly sampled Z bits also preserves empirical masses of tests depending only on the resulting key and unchanged tester data.

This does not imply invariance of T, of a capped unit law, of a leaf law, or of additional row-bit-filtered empirical masses. The remark explicitly excludes T-invariance. Any stronger use later requires a separate argument.

## Section 6 reconstruction

### Definition 6.1 and Lemma 6.2: tables and prescriptions

Admissibility factors into two unary filters because a stored pin's actual image is fixed on its leaf. Entries with both arguments pinned are fixed tests on the leaf pair. The effective-space basis is described inside a coordinate space of dimension at most K^2, so its description need not store unrestricted matrices of quadratic size in n. Nominal pin and projected bases cost O(n) bits, with a coefficient fixed before M_0.

Key independence modulo the table space follows after projecting a purported relation to each endpoint: it would express a sum of at most fourteen selected rays as a projected pin vector. Sparse-label exclusion removes every coefficient. Distinct labels and the nonzero affine constant coordinate then give independence. No distinctness across different endpoints is needed, because their nominal primal blocks are separate.

For the binary prescription, regard the two nonempty disjoint lists at one endpoint as coordinate vectors f_1,f_2. After fixing the diagonal, extending a symmetric form with prescribed pairings against f_1,f_2 is possible precisely when the two self-pairing conditions and one mutual consistency condition hold. Subtracting the prescribed diagonal reduces this to extension of an alternating form from two independent vectors, which is elementary linear algebra.

The two role-sum equations and the coupled p+a equation at the opposite unit give exactly the required mutual consistency. The signs and endpoint indices agree with p_z = u_{z'} U_z.

For each unordered pair of distinct atoms, one indexed product in T^1 can supply the desired off-diagonal correction while the other formal product factors vanish. Forward and reverse evaluations are distinct formal bits. All needed stars are nonempty, and a product linking the two stars always exists. This establishes a consistent formal bit prescription. It does not assert that arbitrary already fixed actual points realize those bits; that occurrence claim is explicitly deferred to the later binary-mixing argument.

### Theorem 6.3: hypotheses and conclusion

The theorem requires: lists of one to seven allowed atoms for each cross pair; matching tags and q bits; labels distinct across the two lists at each endpoint and outside its exclusions; the scalar recipes; the binary gradient prescriptions; actual equality of matched vector keys; and an admissible injecting table. It constructs abstract cross bilinear forms on the full nominal spaces, preserving every actual entry with a pin or key argument, and satisfying the gradient identities on the entire cut domain.

The theorem does not by itself assert that these abstract forms arise from actual frames with positive probability. That is a later theorem interface.

### Step 1: baseline, allowed changes, and the annihilator

The baseline splitting is legitimate: D is inside the table space, key directions are independent modulo that space, and a final complement can be chosen entirely in the primal coordinates. The small table and frozen entries agree on their overlaps by admissibility. The remaining blocks can therefore be filled as stated.

On the additional primal complement, channel evaluations factor through the opposite table-to-pin projection. Its rank is at most K. The remaining primal input space has dimension at most 2K+28. Consequently B_lin = 3K+28 bounds the baseline maps on both source endpoints together, independently of r_0,h,n.

The allowed changes preserve frozen entries even for mixed pins: the domain quotient kills source pins and keys; the range annihilates the channel projection of every target pin; and target keys are primal. Reciprocal changes in the same Gram block have a channel argument on the source side and hence do not change the primal-input map under consideration. Different target endpoints use different channel blocks. Their eventual primal contractions can be solved independently.

The annihilator argument was reconstructed as follows.

1. Annihilating arbitrary pure forms implies that the sum of the two endpoint tensors vanishes in the product of the barred quotients, component by component. Projection to an individual endpoint modulo its projected pins and keys is well defined. Thus each component matrix has rank at most 2K+28 <= R_*.
2. Apply Lemma 5.2. For a selected label, combine its component support with the at most fourteen key labels. Sparse-label exclusion says that a projected pin vector in this combined direct sum has zero component at that selected label. The selected block therefore vanishes modulo its one key ray in both factors, or vanishes outright if that atom does not use this component.
3. For a symmetric base moment block killed modulo a ray v=(1,y), write it as c vv^T + v d^T + d v^T. The identities Z_ii = Z_0i give d_i = d_0 v_i, so the two cross terms cancel. The block is c vv^T. This uses characteristic two and the affine constant coordinate explicitly.
4. Triangle relations among cut components separate label by label because at most 3R_* labels occur, within the interpolation budget. On a selected tag-star these relations force all its coefficients to agree. Subtracting that selected atom preserves membership in the cut domain and in the annihilator. The direct-sum rank observation above justifies the claimed nonincrease of component ranks.
5. For the remaining unselected support, contract the minus factor against a functional killing the projected pins and keys. Pure annihilation puts the resulting plus vector in D + keys + private channels. Projection to each endpoint and sparse-label exclusion removes all key coefficients. The decomposition H_0 direct-sum H_1 removes the remaining channel terms. Thus the vector lies in D^+ intersect B_i, an actual pin intersection rather than merely its projection.
6. Testing a derivative response with an arbitrary vector annihilating H_{z,0}^+ shows that its baseline Y_z evaluation vanishes modulo H_{z,0}^+. The table injection forces the vector itself to vanish. The reciprocal argument uses H_{z,0}^- and the X_z evaluation. These signs match Definition 6.1 and the allowed ranges.
7. Both contractions vanishing implies that the remaining tensor lies in the product of the projected pin-plus-key spaces. Its unselected support removes the key parts once more. The remaining cut profile belongs to C_i.

Every annihilator is therefore a sum of effective profiles and selected atoms. The target difference vanishes on both by the scalar and binary recipes and the baseline's frozen key values. The finite-dimensional image/dual-kernel identity proves relaxed linear solvability. It is unnecessary, and not claimed, that every effective profile itself annihilates the response space.

### Step 2: correction ranks and domain-preserving compression

For the tester part of r(v_{iz}), the odd q sum gives chi_*(w)=1. Consequently the coefficient of an allowed O_{d,t} tester at any tag is eta_S(w_t). There are at most seven nonzero such tag coefficients. Routing each through the edge to d contributes nothing at d because O_{d,t} is disallowed there. The conservative bound of fourteen ordinary testers per component is valid. The shared tester can be routed by stars; the contribution at a star center is zero since g-1 is even, and there is at most one consolidated shared tester per component. This proves the 15r_0 bound.

For T^1, each ordered component term has rank at most that of the relevant witness component. The witness is a sum of at most seven atoms, so the total component rank is at most 7(g-1). Both orientations and J indices give at most 14J(g-1), bounded by the stated 14J|E|.

The projections A_i^± kill the projected pins and keys. Their pulled-back forms are allowed pure quotient forms. The identity

M - A_+^T M A_- = (I-A_+)^T M + A_+^T M(I-A_-)

gives a residual rank at most 2K+28; it does not multiply the r_0 term by a pin-dependent constant.

Projecting the derivative output values through a linear section of their observable pairings with the opposite baseline spans preserves each derivative response and makes each derivative map's rank at most B_lin. Their extra product is itself an allowed pure form. The residual per-endpoint representation therefore has rank at most 2K+28+4B_lin = 14K+140.

The subsequent compression does preserve the domain. On each ordinary base block choose a kernel complement inside the common kernel K_0 of the forms being preserved, disjoint from the span U of vectors to fix. Projection along this complement fixes U, preserves the forms, and has rank at most dim U + codim K_0. Expanding along selector coordinates produces exactly the stated D_blk bound.

The same blockwise map is used on every component and both modes at a given endpoint. It fixes the constant coordinate and selector factor and never mixes allowed with disallowed base blocks. It therefore sends every allowed point moment to an allowed point moment and preserves the cut domain. It fixes each individual pin projection and key, hence each mixed pin after identity is taken on channels. It descends to the barred spaces; the only channel dimensions remaining in those quotients are bounded protected projections. This gives D_quo independent of r_0,h,n.

Precomposing an unrestricted pure solution on both arguments now preserves its value on every individual cut profile: the compressed profile stays in the domain and the target's representing forms are fixed. Its rank is at most D_quo. This is the substantive reason that compression works, beyond a generic low-rank factorization.

### Step 3: channel realization and simultaneous compatibility

Restoring the projected tester/mixer terms gives pure correction rank at most 30r_0 + 28J|E| + D_quo per component for one opposite endpoint. The allowed channel value spaces can additionally annihilate the opposite baseline and small-derivative images, each of dimension at most B_lin. Their codimensions are at most K+2B_lin, so their mutual dot pairing has rank at least h-2K-4B_lin.

The requirement 970r_0 > 28J|E| + D_quo + 2K + 4B_lin is sufficient with h=1000r_0, and its right side is fixed before r_0. A rank-r pure form can be factored through r pairs of channel vectors with Kronecker pairings. The extra orthogonality removes all unwanted cross terms on primal inputs. The quotient/range restrictions preserve every frozen pin and key entry.

The previously established independence on primal inputs permits repetition for both opposite endpoints and both unit roles. Each of the two cross Gram blocks has at most 8h dim B primal-channel entries per component, giving the stated total 16|E|h dim B = O(n). Equal keys and role parity then complete the hole equations, provided actual frames agree with the prescribed entries.

## Residual interfaces for the full-paper audit

The following claims are not consequences of this algebra audit and must be established elsewhere:

1. Appropriate leaves, pin budgets, and injected tables actually occur with the quantitative probability required for every capped unit law.
2. Unary scalar recipes and the joint finite binary bit prescriptions occur with sufficient mass for the selected atom flavors and tags. Lemma 6.2 supplies formal consistency, not this probabilistic assertion.
3. Actual frames satisfy the nominal cross-Gram prescription with the required collision probability, including every constraint caused by actual image dependencies. Theorem 6.3 only constructs abstract nominal bilinear forms.
4. Later uses of Remark 5.6 justify any conditioning or averaging beyond its exact raw-law/input-change symmetry.
5. The remaining parameter demands elsewhere can be met simultaneously with the local inequalities checked here, and their estimates establish the uniform Raw supersaturation theorem.

No substantive local inference in Sections 5 or 6 is left unsupported after the reconstruction above. This is a mathematical internal review at fixed source hashes, not formal proof certification, external peer review, or a validity verdict on the entire release.
