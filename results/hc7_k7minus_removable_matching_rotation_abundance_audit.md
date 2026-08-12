# Internal audit: removable-matching rotation abundance

**Verdict:** GREEN for Lemma 2.1, Theorems 3.1, 4.1, 4.2 and 5.1,
and Corollary 4.3.  This is an internal mathematical audit, not external
peer review.

## 1. Exact revision and inputs

The audited source is
[`hc7_k7minus_removable_matching_rotation_abundance.md`](hc7_k7minus_removable_matching_rotation_abundance.md),
with SHA-256

```text
2f71bdf4f0510b7bb996d54403b505dc1b55fad4e3fcb249f064d172d9726dfa
```

The source was promoted from `active/` after the audit; only its status and
relative dependency link changed.  Its mathematical content is unchanged.

The matching-existence input is the audited
[`seven-removable matching reduction`](hc7_k7minus_seven_removable_matching_reduction.md),
at source revision

```text
d62491aad7d9a5474a6eeed355f4a6f31977c7bd1ce9a05bc1231d00a0a23e13
```

The external critical-cycle statement is Mader's Satz 1, in the equivalent
form restated as Theorem 2.1 of Chu's cited preprint.  The density input is
Theorem 6 of Norin--Totschnig.  Their hypotheses are used at exactly the
displayed thresholds: seven-connectivity and degree at least eight for the
Mader step, and four-connectivity with at least `4n-8` edges for the
near-clique model.  The order bound excludes the exceptional
`K_{2,2,2,2}`.

## 2. Replacement forests and the distinct-edge count

For a fixed coordinate `e_i`, the graph `K_i=H+e_i` is seven-connected.
Every vertex in `R union V(e_i)` has its full degree from `G` in `K_i`, and
hence has degree at least eight.  If a cycle survived after all
`i`-replacements were deleted, every edge of that cycle would be essential
for seven-connectivity in `K_i`.  Mader's theorem would then put a
degree-seven vertex on the cycle, a contradiction.  Lemma 2.1 is therefore
valid.

Let `D` be the union of the five replacement sets as a set of distinct
edges, and put `J=H-D`.  Each induced graph
`J[R union V(e_i)]` is a forest.  If `J[R]` has `c` components, its internal
edge count is `r-c`, and each pair `V(e_i)` sends at most `c+1` edges into
`R`.  Consequently

```text
sum_{x in R} d_J(x) <= 2(r-c)+5(c+1) <= 5r+5.
```

No edge of the original matching meets `R`, so its degree sum in `H` is at
least `8r`.  Deleting one distinct edge lowers that sum by at most two,
irrespective of how many coordinate labels the edge may carry.  Thus
`8r-2|D|<=5r+5`, proving

```text
|D| >= ceil((3r-5)/2) >= 20.
```

The passage from distinct edges to one coordinate is also sound:
`sum_i |F_i|>=|D|`, so some `F_i` contains at least four distinct edges.
No multiplicity of a single edge is being counted as four replacements.

## 3. Four-way cores, signatures and cuts

After fixing four alternatives `A` for one coordinate, each
`M_0 union {a}` is a matching whose deletion leaves a seven-connected
graph.  Therefore adding the three edges `A-{a}` to the common core gives
a seven-connected graph.  Deleting three edges can lower vertex
connectivity by at most three, so the core is four-connected.  Exactly
eight distinct edges were deleted, giving the required `4n-8` density.
Norin--Totschnig consequently supplies the spanning `K_7^vee` model.
Target exclusion correctly makes both nominally missing branch-set pairs
anticomplete even in `G`.

The `79` signature count is exact for the displayed subfamily, not for the
whole language.  Contracting a nonempty subset of `M_0 union {a}` is a
proper matching contraction.  Every other edge of `M_0 union A` remains a
nonloop literal edge: even if two alternatives share an endpoint, a
distinct alternative cannot have both ends in one contracted matching
edge in a simple graph.  The forced signatures are therefore the `15`
nonempty subsets of `M_0` and the `4*16` sets containing exactly one member
of `A`.

For a cut `S` of order at most six, every augmentation `L+(A-{a})` remains
connected after `S` is deleted.  Contracting the components of `L-S`
therefore gives `Q_S-a` connected for every label `a`.  It follows that
the quotient is bridgeless and has at most four vertices.  This statement
correctly permits parallel quotient edges, alternatives sharing endpoints,
and edges of `A` lost at the cut.  It does not infer that `A` is a matching
or that `L-S` has two components.

The same proof applies to each of the five four-element subsets of
`A union {e_i}`, so Corollary 4.3 is valid.  It supplies five existential
exact models on overlapping hosts; it does not supply one common model.

## 4. The six-coordinate fork

If two alternatives `a,b` are disjoint, then
`N=M_0 union {a,b}` is a six-edge matching.  Its deletion is obtained by
deleting one further edge from the seven-connected graph
`G-(M_0 union {a})`, so it is at least six-connected.  Contracting every
nonempty subset of `N` gives all `63` nonempty equality signatures on the
same graph, while an empty signature would six-colour `G`.  The density and
connectivity again exceed the Norin--Totschnig threshold, so the exact
spanning model conclusion is valid.

If no two of the five alternatives are disjoint, their edge family is
pairwise intersecting.  A pairwise-intersecting family of at least four
distinct edges in a simple graph is a star; the only other possibility is
contained in a triangle and has at most three edges.  Because the family
contains `e_i`, the star centre is one of its ends.  The star is retained
as a genuine alternative and is not silently eliminated.

## 5. Trust boundary

The audited theorem proves neither the `K_7^-` six-colour conjecture nor
`HC_7`.  In particular it does not prove:

- that the four alternatives in a common core are pairwise disjoint;
- a full punctured eight-coordinate cube or a `255`-signature family;
- that a low-cut quotient has exactly two components;
- compatibility of the five spanning near-clique models; or
- impossibility of the five-edge star.

The next valid proof obligation is to terminalise the six-connected
six-coordinate host or the explicit star alternative, possibly through
one of the exact low-cut quotients.  No simultaneous linkage or common
model choice is available without a further theorem.
