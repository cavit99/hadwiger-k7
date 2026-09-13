# Internal manuscript audit

**Verdict: GREEN.** Date: 13 September 2026.
**Status:** separate internal mathematical review; not external peer review.

## Current revision and editorial review

A reviewer separate from the manuscript editor independently checked the
complete copyedit diff against the source and PDF saved before editing.
The final artifacts are:

| Artifact | SHA-256 |
|---|---|
| [Current source](main.tex), including its bibliography | `3b799e0e2a02a223a41943a18f9cc2cc092057e3dbbd7b639c6faa79cbe735b5` |
| [Current six-page PDF](main.pdf) | `b85406452a383e5f7bd71bd886818dc46fe7091b44df5a78ba6d75fbc62ffdbc` |

There are no other TeX inputs. The review used `before.tex` and
`before.pdf` in the temporary editorial backup, verified at the earlier
source and PDF hashes below. The earlier audit text had SHA-256
`76f7a80aaad9fcc2a98498d7b682157673e413e592fa812c1f2909afbe30ec8d`.
Its full mathematical review and provenance remain recorded here.

The first copyedit submitted for this review had source hash
`bb261b49ba5892ed72ea3f8f6f5f473524d7de0ef331265d291ec52b2649f7f7`
and PDF hash
`98cc966aa21cbdbebf4830e4a383c9b4f35a99381c9739127d863e29fe3f53ff`.
The reviewer requested one wording clarification: “no connectivity
assumption on G” became “no global connectivity assumption on G”.
The parent accepted this clarification and authorised the reviewer to
apply it and rebuild. This preserves the explicit terminal-linkage
hypothesis while distinguishing it from connectivity of the whole host.
No mathematical statement or proof step changed.

## Earlier full mathematical review and provenance

The parent reviewer, who did not author the manuscript, read the complete
pre-copyedit source at SHA-256
`141cf321eb94afc108f0b4f03e7834d484dd764a8f2ceb624dccbe4c7aa0455a`.
That revision contained its bibliography in the same file, with no other
TeX inputs. Its PDF had SHA-256
`afef9f40260b606e9315c57a2f9b95402f4ff165340156aba30bd9914aef3034`.

The mathematical reading first covered source hash
`4e4fc80337cb918c172b1a67f1e2c9dd2684c24965dbc6cc318dbbbb803a3ee0`.
The change to that reviewed revision replaced only the two bibliography
references to arXiv v2 with v3. The cited definitions and Theorem 3.1 in v3 were
separately inspected. The reviewer selected the theorem package and
supplied literature positioning during editing; this was not a blinded
review or an independent discovery of the underlying argument.

The originating written proofs and their adjacent audits were read and
their exact hashes checked:

| Input | Source SHA-256 | Adjacent audit SHA-256 |
|---|---|---|
| [Full-region theorem](../../results/paired_clique_full_regions.md) | `78121803cfc368cf0ff2e367d87dfc6747fbe888b0f3f5e994abdfe83ac5b8da` | `fcac8b3ce460886ed52f0862cfddac28451df6a8280bc30b06622c63119c74ad` |
| [One-sided theorem](../../results/paired_clique_one_sided_regions.md) | `d39271926d1cce2287de2369061b9c236a6355536bbd81b736661fbc4e6bed69` | `87b67f02bc56f196223a44d3fad291640b8a402313ca5eaeeed08299b0a9afe7` |

## Strongest inferences checked in the full review

1. **Closed induction and terminal ownership.** With k−1 regions covering
   the k vertices of S, precisely one region contains two terminals.
   The singleton step occurs only for k at least three and deletes both
   reserved terminals before invoking the smaller theorem. Components
   outside the regions either can be absorbed or are avoided by a full
   linkage. A permitted contraction contains no R terminal and at most
   one S terminal, so its fixed preimage gives a valid lift. The
   lexicographic parameter (k, host order) strictly decreases.

2. **Endpoint-sensitive separators.** The lifted cut from a failed
   contraction has exactly k vertices. Its two region-edge ends leave
   a budget of k−2, which must meet every other region and therefore
   cannot include an R terminal. S terminals may be cut. A full linkage
   meets each cut exactly once; every non-S region vertex occurs in an
   edge cut. This proves the spanning claim without assuming a linkage
   disjoint from the regions.

3. **The chain argument.** Spanning makes the strict-prefix/strict-suffix
   characterisation of separation exact, including an empty suffix at
   an S endpoint. Coordinatewise minimum and maximum preserve cuts.
   Projection between consecutive chain cuts prevents skipped vertex
   positions. Actual region edges force occurrence intervals to overlap;
   a common separator alone would not justify this inference. S–S edges
   have overlap at the maximum cut.

4. **Clique contacts.** Every cut meets every region, giving interval
   depth at most two within a region. The interval graph is a forest
   containing the connected actual region as a spanning subgraph, so
   they are the same tree. The first-vertex cut then supplies the edge
   within its unique repeated region. Fullness supplies every contact
   between different regions through the other path's R endpoint.
   The returned paths exhaust the terminals exactly once.

5. **Symmetric theorem and sharpness.** Adjoining each S terminal to
   exactly one adjacent region satisfies the one-sided hypotheses.
   The k=1 case is a path. With only k−2 added full singleton regions,
   two proposed bags avoid all added vertices and must be distinct,
   nonadjacent matching edges. This refutes the weakened symmetric
   statement for every k at least two.

6. **Construction.** Once all permitted contractions fail, the proof
   applies to any full linkage in the normalised graph. Thus the
   algorithm returns those paths without constructing a separator
   lattice. Each recursive call removes vertices, including the
   singleton case, and each uses polynomially many flow tests. The
   polynomial bound is uniform in k for supplied regions; a prescribed
   pairing or a method for finding the regions is not asserted.

Vertex Menger is the only external mathematical input. No finite search
is a premise. No unresolved mathematical gap or additional hypothesis
was found within the stated theorem and algorithmic scope.

## Independent review of the copyedit

Every theorem, lemma, proposition and corollary statement is byte-identical
to the pre-copyedit source. The bibliography is also byte-identical.
The reviewer read the full prose diff and the surrounding arguments,
with particular attention to these changes:

1. **The surviving terminal in the separator proof.** The reordered
   paragraph first notes that the two contracted edge ends avoid R, so
   a cut of size k removes at most k−2 members of R. If another region
   were untouched, its connectivity, fullness and retained S terminal
   would give a path from a surviving R terminal to S avoiding the cut.
   Thus each of the k−2 other regions consumes exactly one remaining
   cut vertex. The cut avoids R and meets each linkage path exactly once.
   The reordered proof preserves every endpoint and cut-size quantifier.

2. **Induction and branch-set ownership.** The singleton step still
   deletes both reserved terminals before invoking the smaller theorem.
   Every permitted contraction still avoids R and contains at most one
   S terminal. The simplified closing paragraph retains the decreasing
   parameters and the connected preimage used in each lift.

3. **Separator chains and contacts.** The strict prefix/suffix criterion
   retains selected S endpoints and their possibly empty suffixes. The
   interval-overlap proof still uses the actual region edge to force the
   second endpoint into the next cut. The proof then derives adjacency
   from the connected spanning subgraph of the interval forest. No edit
   substitutes shared cut membership for an actual edge.

4. **Sharpness and algorithmic scope.** The sharpness proposition and
   matching construction are unchanged and concern exactly the k−1
   regions in the symmetric corollary. Removing the repeated final scope
   paragraph does not assert that these regions are necessary in every
   individual host or promise a prescribed terminal pairing. The
   algorithm still assumes supplied regions, uses polynomially many flow
   tests and returns a linkage only after all permitted contractions fail.

The copyedit preserves the mathematical content covered by the earlier
full review. No new hypothesis, unsupported inference or unresolved gap
was found in the edited passages. This is an independent review of an
editorial diff, not a new discovery of the proof or a fresh literature
search.

## Scope of the verdict

The short rainbow-minor comparison correctly identifies an existing
terminology and the different input to the cited theorem. The separate
[focused assessment](citation_novelty_review.md) states its search limits.
This audit establishes neither originality nor publication priority,
prescribed pairing, HC7, nor NT-comparable significance.

For the earlier revision, the manuscript editor reported a warning-free
Tectonic build and inspection of all six pages; the parent verified its
source and PDF hashes. For the copyedit, the editor again reported a
warning-free build and visual inspection of all six pages.

After the audit-requested “global connectivity” clarification, the
reviewer rebuilt the PDF without warnings, rendered all six pages and
independently inspected the changed first page. The rendered images of
pages 2–6 were byte-identical to the editor's preceding images. No
clipping, overlap or undefined reference was found. The current source
and PDF hashes in the opening table were checked independently.
