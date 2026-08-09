# Internal audit: composed manuscript revision

**Verdict:** GREEN.

**Audited manuscript:** [`main.tex`](main.tex), titled *Minimum Degree Eight
in `K_7^-`-Minor-Free Contraction-Critical Graphs*, dated 9 August 2026.

**Manuscript SHA-256:**
`b1828c016bad15a096b1000096018ce0ee6b22b3943ffd9ce890fa8502b36e7d`

**Bibliography SHA-256:**
`75031e4826eddb423cbac2297295753c83e999672b05842afbd5579e2d0b7c85`

**Built PDF SHA-256:**
`6caa135f758e80fe31e2f048b3989781ee3ffb88738735487a66bb0b76543064`

The TeX and bibliography hashes identify the audited claim and citation
surfaces.  The PDF hash records the inspected build output for convenience;
it is not a substitute for the source hashes.  This is a separate internal
mathematical audit, not external peer review.

## 1. Composition and dependency order

The manuscript has an acyclic proof chain.

1. Albar's theorem and minor minimality give a seven-chromatic graph whose
   proper minors are six-colourable.  Mader's contraction-critical theorem
   gives seven-connectivity.
2. The uniform two-clique theorem gives at most one literal `K_5` in a
   six-connected `K_7^-`-minor-free graph.
3. The degree-seven neighbourhood argument uses the
   contraction-critical independence bound, the Kriesell--Mohr rooted-minor
   theorem and Mantel's theorem.  It leaves
   `K_4` disjoint union `K_3` or `K_1` joined to two disjoint triangles;
   uniqueness of the literal `K_5` removes the second graph in the critical
   host.
4. Every degree-seven vertex therefore lies in the unique possible `K_5`,
   so `n_7<=5`.  Degree summation and parity give `m>=4n-2`.  This argument
   does not use the former private-triangle theorem.
5. Norin--Totschnig Lemma 12, together with the manuscript's fifth-root
   helper augmentation, gives the closure
   `m>=4n+d-13` whenever a degree-`d` neighbourhood contains `K_4`.
6. At degree seven the closure needs only `m>=4n-6`; the preliminary
   `4n-2` bound therefore eliminates every degree-seven vertex.  Hence
   `n_7=0`, `delta>=8`, and `m>=4n`.
7. With `q=m-4n`, the closure contrapositive at the five vertices of a
   hypothetical `K_5` gives degree at least `q+14` at each.  Their combined
   surplus above degree eight is at least `5(q+6)`, contradicting the exact
   total surplus `2q`.
8. Jakobsen's defect bound and
   `9n-2m=n_8-sum_{i>=10}(i-9)n_i` give `n_8>=25+tau`.  The absence of a
   literal `K_5` makes every degree-eight neighbourhood `K_4`-free.
9. The resulting conditional extremal reduction requires only the
   seven-connected `m>=4n` statement.

Each theorem is stated before its proof, and no later conclusion is used to
prove an earlier step.

## 2. Rooted-model assembly

The Norin--Totschnig input is used with its exact threshold.  For
`F=G-v`, the manuscript hypothesis gives

```text
|E(F)| = |E(G)|-d >= 4n-13 = 4|V(F)|-9,
```

the contrapositive of their `4|V(F)|-10` exclusion bound.  Six-connectivity
of `G` makes `F` five-connected, supplying both rooted internal-connectivity
hypotheses.

The helper augmentation was checked bag by bag.  Maximising the helper
union and then minimising the root bags leaves at most one helper contact in
each root bag.  If the fifth root were outside the helper union, those four
contacts would form a forbidden separation.  The four literal edges of the
nominated `K_4` complete the root bags to a clique; the two helpers and the
singleton centre then form seven branch sets with at most one missing
adjacency, exactly a `K_7^-` model.

## 3. Scope and omissions

The private-triangle allocation and `n_7=4` amplification are not logical
dependencies and were correctly removed.  The extensive E5 and separator
casework is also absent.  Retaining the two-clique theorem and the complete
degree-seven neighbourhood proof is sufficient to make the capstone and
critical-host theorem self-contained.

The manuscript does not prove the open `m>=4n` extremal statement,
Norin--Totschnig Conjecture 21, or `HC_7`.  Its external trust boundary is
the exact cited statements; those citations received the separate review in
[`citation_novelty_review.md`](citation_novelty_review.md).

## 4. Build and presentation check

`tectonic main.tex --keep-logs` completed successfully.  The log contains no
undefined citation/reference warning and no overfull or underfull box
warning.  The resulting PDF has nine letter-size pages.  All nine pages were
rendered at 144 dpi and visually inspected; equations, theorem boundaries,
citations, running heads and the title-page footnote are legible, with no
clipping or overlap.

No unresolved mathematical inference was found in the composed revision.
Independent human specialist validation remains necessary before
publication.
