# Audit of the bipartite scope and comparison review

**Status:** separate internal audit, 8 September 2026; not external peer
review.

**Verdict: GREEN for the scope deductions, literature wording and expressly
qualified assessment.** This verdict does not prove a ranking of mathematical
significance or completion of the research objective.

**Exact source:** [citation_novelty_review.md](citation_novelty_review.md),
whole-file SHA256
`dda2925dbb76d623369ca997048ac1a3df8299de5e764ebcc1fe53a662ffb178`.
The [manuscript](main.tex), checked here for literature wording and bibliography,
has SHA256
`6d804a715f8782ac84679a8a5715105cb28d2a7cf4a594c60aec5b1072b387b9`.
Its full proof revision is outside this scoped audit. The universal theorem
source remains at `3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`.

**Provenance:** the earlier deductions below were audited at Git `80ebbd2`,
review SHA256 `f0e54afd08ebe9106e0506a0e7478a4f15150e848e0d2914fc50dfda8cbfbd27`.
Both that hash and its manuscript hash `8cea0ca4838a7090b5fb4798c2c9ec670efe60017a6f7df1e79dc0d668c0b701`
were verified from Git. The current reviewer compared all changes, retaining
the earlier checks and their provenance. The parent and a separate agent had
checked those deductions; the latter also checked Lee's primary definitions.

The private four-cycle construction raises every target degree to at
least two while preserving bipartiteness and the scheme condition. Every
new host vertex is a prescribed root of the enlarged target, so none can
belong to an original root's bag. Restriction therefore preserves all
original bags, roots, connectivity and contacts. This is an implication
from BLR's intended rooted assertion, not reliance on its disputed proof.

In the family augmentation, the degree-one private leaf forces each old
root into its own family union. Every component left after deleting the
artificial vertices contains a correct root; a rooted forest splits it
without losing the existential cross-family contacts. Artificial edges
cannot supply those contacts. Thus this is an augmentation corollary.

Lee's demand equation gives positive total flow on every demand pair.
If two target vertices had the same image, minimum degree two and
bipartiteness provide independent incident demands whose positive paths
intersect at that image. This contradicts zero crossing congestion.
After injectivity, arbitrary positive path choices satisfy the full
scheme condition, including foreign-root exclusion. Fractional weights
and length-zero paths introduce no exception. No rounding input or
induction is required; the only minor lift is the audited universal one.

The parent separately inspected BLR v2 Section 1.2.2 and Lemma 3.13 for
the ambient-diameter distinction. The independent agent did not repeat
that particular primary check. The review claims neither its correction
nor a counterexample to a bounded-depth conclusion.

The added property `(*)` equivalence matches Kriesell--Mohr Definition 1:
one prescribed root per colour class and a bichromatic path for each required
edge give a scheme; colour normalisation and fixed-preimage lifting give the
converse. Neither optimality of the colouring nor connectivity of whole pairs
of colour classes is required. The cited work is arXiv:1911.09998v2 (2022),
not the authors' different published line-graph paper.

The current reviewer independently inspected published BLR pp. 13:10--13:11:
the intersection wording, explicit root-retention lemma and defective prefix
construction are correctly distinguished. The manuscript's displayed rooted
model of the eight-vertex example is connected, disjoint and has all four
required contacts. The counterexample refutes the construction, not existence.

KSJ Lemma 3.11 has an existential demand graph for each `h>=3`, with minimum
degree at least two and maximum degree at most three, forcing an unrooted
clique minor from an almost-embedding. Proposition 3.4 uses it for clique-flow
congestion; BLR duality remains in use. The cited KL Lemmas 4.3--4.4 construct
and extract subdivided targets. They supply no arbitrary rooted bipartite
extraction theorem: subdividing an existing scheme need not make the newly
independent segments disjoint. Bibliographic authors, titles, versions and
the KL proceedings pages/DOI agree with the inspected primary records.

The final manuscript differs from the reviewed `ad42f119b9df851718e631ac3f3b5976a33e61032e12ad0d52cb5cb7910c698b`
only by making the path collection nonempty and replacing the manual proof-end
symbol by `\qed`; reversing those edits reproduces that hash exactly.

The NT comparison identifies the actual colouring and density conclusions.
Its stronger evaluation is explicitly a comparative judgement, even under
hypothetical first-valid-proof credit, not a theorem or community consensus.
The search remains nonexhaustive; reported separate AI reviews are not used
as exact-revision proof certificates. **Unresolved:** publication priority
and the requested comparative advance. No mathematical gap was found in the
scope deductions checked here.
