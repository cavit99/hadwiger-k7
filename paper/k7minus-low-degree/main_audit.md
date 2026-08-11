# Internal audit: compact low-degree draft

**Verdict:** GREEN.

**Status:** DRAFT; ready for independent specialist review, not submission.

**Audited manuscript:** [`main.tex`](main.tex), titled *Minimum degree eight
in `K_7^-`-minor-free contraction-critical graphs*, dated 11 August 2026.

**Manuscript SHA-256:**
`461e7433e0b2695ead1d0a3f46724f32989b880389a75ba89bcbecbd219e59fa`

**Bibliography SHA-256:**
`42efaacd1e81ba0a582d140ef266212317e6960ed3a78909a9af26f018458175`

**Built PDF SHA-256:**
`457bf0eefac1050d806dcb70dc86ac1e202cf542d4f90a9d76cce30ce5b4802c`

These hashes identify the exact source, bibliography and inspected PDF.
This is a separate internal audit, not external peer review.

## 1. Scope and provenance

The compact draft extracts the self-contained low-degree proof from the
historical rooted-web manuscript.  The predecessor mathematical source has
SHA-256
`453fc248f4192e5e5f1487c364ae71610b68013effc6e3983575c63de5a4fcd7`.
The proofs corresponding to its Sections 2 to 5 were retained.  The
abstract and introduction were rewritten, and all four-centre, Ramsey,
rooted-web, separator-lattice and edge-deletion material was removed.

## 2. Dependency chain

The proof order is acyclic.

1. The linked-cliques lemma proves that two distinct `K_r` subgraphs in an
   `(r+1)`-connected graph force a `K_{r+2}^-` minor.  Its `r=5` case gives
   at most one `K_5` subgraph in a six-connected `K_7^-`-minor-free graph.
2. Dirac's neighbourhood bound and Kriesell and Mohr's rooted-minor theorem
   give a rooted `K_5` for every nonedge in a degree-seven neighbourhood.
   The complement is then forced to be `K_{3,3}` plus an isolated vertex or
   `K_{3,4}`.  The unique-`K_5` corollary excludes the second possibility.
3. Norin and Totschnig's rooted `K^*_{4,2}` bound, together with the
   prescribed fifth-root placement lemma, proves the `4n+d-13` closure.
4. The local classification first gives `n_7<=5` and `|E(G)|>=4|V(G)|-2`.
   The rooted closure then excludes degree seven, so `delta(G)>=8` and
   `|E(G)|>=4|V(G)|`.
5. The contrapositive of the closure excludes every `K_5` subgraph.
   Jakobsen's defect bound and the degree identity give
   `n_8>=25+sum_{i>=10}(i-9)n_i`; degree-eight neighbourhoods are
   `K_4`-free.

No step depends on the omitted four-centre or rooted-web sections.

## 3. Claim boundary

The draft does not prove Norin and Totschnig's Conjecture 21 or Hadwiger's
conjecture for `t=7`.  It states the remaining sufficient extremal theorem
explicitly: every seven-connected graph with at least `4n` edges contains a
`K_7^-` minor.  That theorem remains open.

The proof uses no computer search.  The audit makes no priority claim.

## 4. Editorial and build checks

The retained proof prose received a light British-English edit.  The new
abstract and introduction were checked for inflated claims, stock
signposting, repetitive cadence and unnecessary passive constructions.
The final source contains no Unicode em dash, en dash or curly quotation
mark, and no LaTeX double-hyphen punctuation.

`tectonic main.tex --keep-logs` completed successfully.  The log has no
undefined reference, citation, box or PDF-string warning.  All ten
bibliography entries are used.  The PDF has eight letter-size pages, and
all fonts are embedded.  Every page was rendered at 110 dpi and inspected;
there is no clipping, overlap or illegible material.  `DRAFT` is prominent
on the title page and appears in the running heads.

Independent human specialist validation remains necessary before
submission.
