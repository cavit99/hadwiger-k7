# Internal audit: composed manuscript revision

**Verdict:** GREEN.

**Audited manuscript:** [`main.tex`](main.tex), titled *Minimum Degree Eight
and a Rooted-Web Reduction in `K_7^-`-Minor-Free Contraction-Critical
Graphs*, dated 9 August 2026.

**Manuscript SHA-256:**
`453fc248f4192e5e5f1487c364ae71610b68013effc6e3983575c63de5a4fcd7`

**Bibliography SHA-256:**
`e4bc442048d7894ef46ae3200802c3e68fa85baedef3a87ef9debb6b2c9a5e35`

**Built PDF SHA-256:**
`1de1eae5b8b6376de58f23ec621cba098142370bcb902e0a70569c0ff97a87e7`

These hashes identify the exact source, citation surface, and inspected
build. This is a separate internal mathematical audit, not external peer
review.

## 1. Dependency chain

The proof order is acyclic.

1. Albar's theorem and minor minimality give chromatic number seven. Mader's
   theorem gives seven-connectivity.
2. The uniform two-clique theorem implies that a six-connected
   `K_7^-`-minor-free graph has at most one `K_5` subgraph.
3. The degree-seven neighbourhood argument uses the
   contraction-critical independence bound, Kriesell and Mohr's rooted-minor
   theorem, and Mantel's theorem. It leaves two possible neighbourhoods;
   uniqueness of the `K_5` removes one. Hence every degree-seven vertex lies
   in the same possible `K_5`, so `n_7<=5` and parity gives `m>=4n-2`.
4. Norin and Totschnig's rooted `K^*_{4,2}` bound, together with the
   additional-vertex placement lemma, proves the `4n+d-13` closure. At
   degree seven, the preliminary density exceeds this threshold. Thus
   `n_7=0`, `delta(G)>=8`, and `m>=4n`.
5. The closure contrapositive excludes every `K_5`. Jakobsen's defect bound
   and the degree identity then give `n_8>=25+tau`; every degree-eight
   neighbourhood is `K_4`-free.
6. The equality `R(5,4)=25` supplies an independent four-set `U` of
   degree-eight vertices. The proof that `G-U` is three-connected,
   nonplanar, and six-chromatic is independent of the later web analysis.
7. The Fabila-Monroy and Wood theorem gives the rooted `K_4`/web
   alternative. In the web case, seven-connectivity gives the literal
   separator `U dotcup T`. The minimum lift-order formula, its submodularity,
   and pointwise equality yield the fixed-orientation lattice and sign-region
   bounds.
8. The Kempe argument forces one of the two alternating bichromatic
   components through `U-{r}`. The proof that `G[T]` is not `K_3` uses two
   proper-minor colourings and does not depend on any omitted quotient lemma.
9. The edge-deletion theorem reconstructs its colouring locally. Two
   capacitated Menger arguments give either the five controlled paths or a
   strictly smaller component behind a seven-vertex separator. This outcome
   preserves a boundary colour class. The independent fan construction has
   five residual branch sets whose contact graph has at most eight edges;
   nine contacts would give a `K_7^-` model.
10. The final corollary uses only seven-connectivity, nonplanarity, and the
    four-connected rooted-`K_4` theorem. The extremal reduction therefore
    needs only the stated seven-connected `m>=4n` hypothesis.

The rooted-web lattice agrees with the separately promoted theorem at source
hash
`e7fcf00c9bdbd2fcbab78bb13d4244a659f4f7db0ae45a97cfbd9a8d599a0ee3`.
The self-contained edge-response argument agrees with the promoted operation
theorem at source hash
`4d4ca474cb9d9f28632077f0a89d79c0fc36840f3eb2600c745e0ea2150f2f98`.

## 2. Concision and terminology

The manuscript uses standard graph-theoretic terms: branch sets,
separations, separators, open sides, components, rooted minors, Kempe
components, and fans. Project-internal terms were removed from the rendered
paper. The remaining word “centre” refers only to the standard centre of a
fan. Historical internal LaTeX labels were left unchanged because they are
not reader-facing.

The private-triangle argument, the `n_7=4` amplification, the one-sided
trace lemma, the two-universal-vertex quotient, and the extensive `E5`
casework are not dependencies and do not appear. The separately audited
research note retains ancillary refinements that would lengthen this paper.

## 3. Claim boundary

The manuscript does not eliminate the web outcome, prove the open
seven-connected `4n` extremal hypothesis, settle Norin and Totschnig's
Conjecture 21, or prove Hadwiger's conjecture for `t=7`. It correctly states
that Hadwiger's conjecture is known for `t<=6` and open for every `t>=7`.

## 4. Build and visual inspection

`tectonic main.tex --keep-logs` completed successfully. The log has no
undefined reference, citation, box, or PDF-string warning. All twelve
bibliography entries are used. The PDF has 16 letter-size pages. All pages
were rendered at 110 dpi and visually inspected; there is no clipping,
overlap, or illegible material.

Independent human specialist validation remains necessary before
publication.
