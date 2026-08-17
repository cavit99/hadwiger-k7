# Cold audit: rooted-`K_4` portal orientation and hereditary descent

**Audit status:** GREEN, with the minimal-counterexample conclusion read with
its stated class-closure hypothesis.

**Source audited:**
[`hc7_k7minus_sparse_sixcut_rooted_k4_portal_descent.md`](hc7_k7minus_sparse_sixcut_rooted_k4_portal_descent.md),
SHA-256

```text
bf66968759fb4250b6c1d036e0d3acf61343efd2f6aa7396bd184409f5d39260
```

The current source SHA-256 is
`6118da0fbbca965c241c8ff5259552744f96c2364d50f95ef0a8b87355be168c`.
The only later change removes an extra blank line at end of file; the text
and mathematical revision are unchanged.

## 1. Portal count and orientation

The exact cut is `T=A union {p,q}`, where `A` has four vertices.  Since
`p,q` belong to both boundaries, the exchanged sets have the same order and

```text
|A intersect S|=4-|T-S|.
```

Every member of `A intersect S` is one of the four distinct roots in `Z`, so
these boundary portals occupy distinct rooted-model bags.  The audited support
lemma confines all four portals to at most two bags.  Therefore at most two
portals are boundary roots and `|T-S|>=2`; the upper bound four is immediate.
The three orientation descriptions for exchange orders two, three, and four
then follow exactly.

## 2. Exact-fragment legality

Completing `S` to a clique adds no edge incident with `L`, so `N_F(L)=T`
remains exact.  The set `T-S` contains at least two internal vertices and is
disjoint from `L`, whilst `S-T` is nonempty.  Hence `L` is a component of
`F-T` remote from the old-boundary residue.  These are precisely the
hypotheses of the pinned six-boundary rerooting corollary.  It excludes every
punctured `T`-rooted model in `L`.

The excess identity is the pinned exact additivity identity.  Edges incident
with `L` are counted in `eta_T(L)` and all remaining edge and vertex terms in
`eta_S(C-L)`; no connectedness assertion about `C-L` is needed.

## 3. Conditional minimality fork

For every nonempty `X subseteq L`, all its neighbours lie in `L union T`.
There is a vertex in another component of `G-S` outside its closed shore, so
six-connectivity gives at least six neighbours.  Thus the derived rooted pair
is internally six-connected.  It is strictly smaller: `T-S` contains an
internal vertex of `C-L`.

Accordingly, in any class genuinely closed under these derived rooted pairs,
minimum-order counterexample induction applies.  When `eta_T(L)>=6`, the
inductive dichotomy returns either a punctured rooted model or two `T`-full
packets; the former is excluded by hereditary rerooting, leaving the latter.
For integral excess below the threshold, `eta_T(L)<=5`.  This proves the
stated fork.

The qualification is material and correctly retained in the source: if the
local theorem were formulated only for a stable boundary, or only for an
original `S`-component, closure under the generally nonstable derived boundary
`T` would first need proof.  The corollary does not assert that closure or that
two `T`-packets transfer to two `S`-packets.

## 4. Verdict

The orientation, exact-cut use, rerooting dependence, additivity, and
conditional induction conclusion are sound.  The source accurately leaves
the two-copy packet-transfer problem unresolved.
