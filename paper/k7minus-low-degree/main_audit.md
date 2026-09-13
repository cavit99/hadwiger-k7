# Internal audit: degree, defect and separators

**Verdict:** GREEN for the exact revision below, within the explicitly stated finite-computation and published-theorem dependencies.

**Audited manuscript:** *Degree, defect and separators in `K_7^-`-minor-free critical graphs*, 13 September 2026.

This is a separate internal mathematical audit by an agent other than the manuscript author, not external peer review or an originality assessment. The reviewer read all four TeX sources, reconstructed their strongest inferences and explicit minor models, read the two finite verifiers, and checked the source-proof and adjacent-audit chain. No unresolved mathematical gap was found in the final revision. The source audits were consulted; this was not a blinded review.

## Exact revision and provenance

All hashes are SHA-256 and were independently recomputed after the final source freeze.

| Manuscript input or artifact | SHA-256 |
|---|---|
| [main.tex](main.tex) | `5a5ec2e4d121eff1c92002bc9e3ed7988da0ac4aca8a4b2a782931aa25e93540` |
| [degree-eight.tex](degree-eight.tex) | `ecdc84a42e0d2206f2a3766c19a552d53c1bd4164719ce696e15ad0185b339bd` |
| [connectivity-defect.tex](connectivity-defect.tex) | `02e87d75ff70698532d66c7fce6a951ccf37eb1147ec4660d6c62963bbefb13b` |
| [seven-cuts.tex](seven-cuts.tex) | `e3ecc8b7c424d2750964dacb91f6e9b574ac689fd96a701e60300558e396ec6d` |
| [references.bib](references.bib) | `0cfaa614f2d68573ff16d0805e63a359c9bb90c991c24cb1938b07c33f579fdf` |
| [main.pdf](main.pdf) | `8eaceb77eaf7bc59229654c37b7de743c3bc4153c4064370e9b2da8d9026ec58` |
| [README and input manifest](README.md) | `6c3682e402d3dc7fec00cc60e28652c79a23bbc074d8107c201c33831f97f94a` |
| [Citation and originality scope](citation_novelty_review.md) | `f4c538aeb9cfade22743c2e9265e0e949a38040684bee4a34dbeb2292cdbf7c4` |

The pinned README is incorporated here as the mathematical input manifest: its table identifies all nine proof sources, their exact hashes and their adjacent audits; it also pins both finite verifiers. Every one of those nine proof hashes was recomputed and matched both the README and its adjacent audit. Both executable hashes also matched. Those checks establish source provenance; this verdict concerns the full manuscript adaptation, including its new self-contained separator proof.

The compact 11 August 2026 snapshot remains available at Git revision `f7b52aff0dfb2578bc30ade68f75df12671cf966`, under this same directory. Its source, bibliography and PDF hashes were respectively `461e7433e0b2695ead1d0a3f46724f32989b880389a75ba89bcbecbd219e59fa`, `42efaacd1e81ba0a582d140ef266212317e6960ed3a78909a9af26f018458175`, and `457bf0eefac1050d806dcb70dc86ac1e202cf542d4f90a9d76cce30ce5b4802c`. The old `main_audit.md` at that revision has hash `d373bf1f62f4d5ad402a002d158702cd654e004dff86b75b781ad161ad1bf7b7`. Its computation-free `25+tau` verdict is historical and was not transferred to the new sections.

## Editorial revision

The full review below is retained. A further independent review compared the final four TeX sources with the previously audited 19-page version. The revised manuscript has 17 pages, with unchanged font size and margins. The changes consolidate intermediate statements and repeated calculations; all requested theorem conclusions remain.

The merged neighbourhood classification uses the same seven-connectivity and unique-clique argument. The preliminary density bound is proved inside the minimum-degree argument. The shared contraction identities are unchanged. The finite lemma now states the fixed-labelled-graph uniqueness property actually used, with the four classification profiles retained in the pinned README. The exterior augmentation and final two-component deduction are written at their points of use. The unused edge-cover count is omitted. The complement lemma moved to the connectivity section, its only place of use; all seven explicit models are unchanged.

The changed passages were also reviewed in academic English. Adjacency wording now distinguishes disjoint branch sets from sets that intersect, British spelling is consistent, and branch-set notation is defined before its first table. No proof premise was replaced by an unexplained citation or removed during shortening.

## Retained low-degree argument

The dependency order is acyclic. The uniform linked-cliques theorem was checked in both the disjoint and intersecting cases, including the special overlap of order `r-1`. All claimed clique adjacencies survive the linkage contractions. Its `r=5` corollary gives at most one `K_5` subgraph in a six-connected `K_7^-`-minor-free graph.

For a degree-seven vertex, the colouring after contracting a nonedge with the centre yields the required rooted five-vertex model. Kempe paths avoid the contracted colour class, leaving the omitted neighbours available for the final model. The complement classification and the exceptional neighbourhood exclusion preserve this ownership. The fifth-root placement lemma was checked using its extremal helper sets and minimal rooted trees; its small-separator contradiction retains the roots. Norin and Totschnig's rooted `K^*_{4,2}` bound then gives the stated `4n+d-13` closure.

The general form of the Jakobsen lemma requires five-connectivity and order at least nine. The order excludes both base cockades, and five-connectivity excludes every nontrivial four-sum cockade. Its applications retain both hypotheses: the critical host has minimum degree eight before the first use, its contracted graph has order at least 24, and the quotient in the defect induction retains density `m>=4n`, which forces order at least nine.

The later deductions were recalculated: first `n_7<=5` and `m>=4n-2`, then no degree-seven vertex, `delta>=8` and `m>=4n`. The rooted closure's contrapositive excludes a `K_5` using total degree excess. Jakobsen's strict noncockade bound gives `D=9n-2m>=25`. With minimum degree eight the exact identity is `D=n_8-tau`, proving the initial `25+tau` estimate and the existence of degree-eight vertices.

## Computation-free degree-eight improvement

The independent-triple argument uses the eight-vertex classification and an exterior component with at least seven boundary neighbours. The displayed seven bags in the square-of-a-cycle case are disjoint and connected and miss at most one adjacency.

The rooted-deletion lemma's connectivity reduction is exhaustive. In the four-connected case the wheel classification supplies the required local form; in the three-cut case, component orders two and three and all listed path/triangle cases are accounted for. The five-bag table models work, and the roots admitting such a model meet every vertex's neighbourhood. That property repairs the one possible missing attachment in the almost-full exterior quotient.

Every degree-eight vertex therefore has an incident edge of codegree at most three. Contracting it leaves a six-connected `K_7^-`-minor-free graph of sufficient order for the strict noncockade bound. The identity `D(G/e)=D(G)-7+2c`, with `c<=3`, gives `D(G)>=26` and hence `n_8>=26+tau`. This chain, including the written finite case distinctions, has no computer-search premise.

## Finite quotients and the broader defect theorem

The computation-free complement lemma for local minimum degree five was checked against every displayed path/cycle row. It is used only in the broader degree-eight theorem.

The manuscript correctly isolates one computer-assisted lemma with two parts. The nine-vertex part covers every seven-vertex local graph of minimum degree four and every attachment to at least six local vertices. The ten-vertex part covers every eight-vertex local graph of minimum degree four without a `K_6^-` minor, with the same attachment lower bound. For each fixed labelled local graph, the statement allows at most one attachment producing a `K_7^-`-minor-free quotient. If it exists, the missed set is an adjacent pair of degree-four vertices. This is exactly the property needed by the host reduction; the four negative profiles remain in the reproducibility note.

The verifier logic was independently read. For order nine, the 29 maximum-degree-two complement types and all eight attachments give 232 cases; all 750 possible seven-bag partitions over supports of orders seven through nine are included. For order ten, the complete order-seven atlas and all vertex extensions cover every local graph. Isomorphism filtering uses exact tests within invariant buckets. Deleting unused bags and merging adjacent bags is an exhaustive minor recursion. Both positive certificate checks verify nonemptiness, disjointness, connectivity and all but at most one interbag adjacency. Both programs include known positive and negative calibrations.

The manuscript author reran both pinned executables successfully on 13 September 2026, reproducing:

| Finite input | Reported coverage | Certificate digest |
|---|---|---|
| Nine-vertex quotients | 232 checked positive models | `b98ac56930aa7044c3a6a7c029b75cd85feb39f4dabd8476a0ba7f08ccdb7306` |
| Ten-vertex quotients | 424 local classes, 55 survivors, 2,035 profiles, 2,031 positives and four negatives | `8b9b31cae19b10a9e958a51dd2c8ef12193b655ec7ab2163b67b638dfc646501` |

This manuscript reviewer did not repeat those exhaustive runs. The editorial changes alter neither verifier nor any finite input, so the recorded runs remain applicable. The prior [degree-eight result audit](../../results/hc7_k7minus_sixconnected_degree_eight_low_codegree_audit.md) records independent partition checks of the four negative quotients and the unique missed-pair property. Its exact record has SHA-256 `1e8ebfd4acb8f27aeb7b3fdf331e8431c813f3c4a01533ca72908124ff84b547`; the [degree-seven result audit](../../active/hc7_k7minus_degree7_common_neighbour_exclusion_audit.md) has SHA-256 `3611d9634d0ebd12f642a822009e0ebab7dc93baf16473d894a6431a30a227eb`. The independent negative checker is recorded as an audit experiment, not as a separately retained executable. The reproducible programs and their trust boundaries are accurately stated. The environment files at this audit were `pyproject.toml` SHA-256 `889ff4d85a544eff14feb7d78c3701ba2ea5660b5c332ca20941828f9690a1c3` and `uv.lock` SHA-256 `ff6a929a94dd162d2e3b08e25bf3b7aa7845b70b2511a15772f84776a122092c`, including NetworkX 3.6.1.

The unbounded reduction is valid: contract one whole exterior component and delete the others. Six-connectivity supplies at least six literal boundary neighbours. In the degree-eight case, uniqueness forces every exterior component to miss the same pair, making those vertices have total degree five, a contradiction. With no exterior, six-connectivity instead supplies local minimum degree five. No bound on host order or component size is used.

The degree-six disc argument was checked against the primary two-paths theorem and Norin and Totschnig's proof. One point was clarified during review: Menger yields paths from an arbitrary five of the six neighbours, not from five preassigned neighbours. Those five contain two complete matching pairs, which the final manuscript relabels temporarily. The last disk application still uses the separately chosen pair with no common exterior neighbour. The lifted separators have the stated orders; the disc edge count gives exactly `m<=4n-9`. This adaptation uses neither edge-maximality nor `K_7^vee` exclusion.

At density `4n`, the average-degree bound and the degree-six, degree-seven and degree-eight exclusions supply an edge with codegree at most three. Its contraction preserves density and minor exclusion and loses at most one unit of connectivity. At `r=6`, the quotient is five-connected, excluding nontrivial cockades, and its density excludes the two bases; its defect is therefore at least 25. For `r>=7`, induction on `r` applies within the same graph class and gives `D>=20+r`. The induction parameter strictly decreases and all hypotheses are retained. Applying `r=7` to the critical host gives precisely `n_8>=27+tau`.

## Seven-cut closure

Every component of a seven-cut is full at its boundary by seven-connectivity. The explicit five-component model bounds the component count by four. Four components force the boundary to be a matching; its `3,3,1` independent partition is reflected across the two component pairs. The resulting six-colourings have the same exact boundary equality partition and glue after a palette permutation. This proof does not require the stronger packing-number statements in the source results.

For three components, the elementary seven-vertex lemma was reconstructed case by case. Each of its three forbidden boundary subgraphs gives the claimed minor model. Thus the boundary has at most nine edges and no `K_4`. The short critical-graph argument proves three-colourability without enumeration. Reflection rules out two colours or a singleton colour class, forcing class sizes `3,2,2`.

The reflection lemma contracts disjoint connected sets, uses a proper minor, and pulls a colouring back only onto the untouched closed shore. Its representative clique enforces distinct colours for distinct blocks; independence enforces a valid colour inside each block. No colouring is silently extended over a contracted component.

The final `3,2,2` theorem was checked independently of the minor exclusion. If two components realise the paired boundary blocks, proper-minor reflection gives aligned colourings of every piece. Otherwise the two incapable components admit the asserted planar completions. Added cycle edges cannot create a crossing of the prescribed terminal pairs. Humeau and Pous's web theorem applies to the edge-maximal completion on the same vertex set. A vertex behind a facial triangle would give a cut of at most six literal vertices after restoring the omitted three-set, contrary to seven-connectivity. The induced facial four-cycle and its at-most-three-colour precolouring therefore satisfy Diwan's five-colour extension hypotheses. The final extensions avoid the three-set's colour and agree on all shared roots. Added planar edges are used solely for colour extension, not asserted as edges of a minor of the original graph.

This excludes three components and proves exactly two for the critical host. It uses proper-minor six-colourability essentially and does not claim the same conclusion for arbitrary seven-connected `K_7^-`-minor-free graphs. References to the main theorem in the separator statements explicitly mean its hypotheses, so the assembly is not circular.

## Primary inputs, build and scope

The primary statements checked for their use here include [Norin and Totschnig, Lemma 12, Theorem 13 and Claims 3.12 to 3.15](https://arxiv.org/html/2507.03244v1), [Kriesell and Mohr, Theorem 7](https://arxiv.org/html/1911.09998v2), [Rolek, Song and Thomas, Lemma 2.1](https://arxiv.org/pdf/2208.07335v2), [Wood and Woodall, Lemma 4.2.1](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v16i1r92/pdf/), [Humeau and Pous, PDF Theorem 1.3](https://arxiv.org/pdf/2505.16431v2), and [Diwan, Corollary 1](https://arxiv.org/html/2306.04944v1). Humeau and Pous's HTML version numbers the web statement differently; the manuscript correctly cites the PDF number. The base colouring, connectivity and Jakobsen thresholds were also checked in [Albar, Theorems 1 to 3](https://arxiv.org/pdf/1402.2806).

The revising editor reports a warning-free Tectonic build with all 14 cited entries resolved and all 17 letter-size pages rendered and inspected. The three pages affected by the final equation-numbering change were inspected again. This reviewer verified the frozen source and PDF hashes and the PDF's 17-page letter-size metadata. The author's supplementary finite check of the computation-free degree-eight lemmas is corroboration, not a premise of this verdict.

The abstract, theorem statements, proofs, finite-dependency labels and README agree. The result is a set of necessary structural conditions for a counterexample. The sufficient seven-connected `4n` extremal assertion, Conjecture 21 and Hadwiger's conjecture for `t=7` remain unproved. No NT-comparable significance, publication priority or completed originality assessment follows from this audit.
