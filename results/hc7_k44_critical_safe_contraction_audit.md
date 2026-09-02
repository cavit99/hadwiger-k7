# Independent internal audit: critical literal-`K_{4,4}` safe contraction

**Verdict: GREEN.**  The theorem and colouring corollary are valid at the
exact revision identified below.  The safe contraction is an unbounded
conclusion, but it inherits one computer-assisted finite lemma from the
audited singleton-atom theorem.  No new computation occurs here.

This is a separate internal mathematical audit, not external peer review.

**Audited theorem:**
[`hc7_k44_critical_safe_contraction.md`](hc7_k44_critical_safe_contraction.md)

**Theorem SHA-256:**
`51e9b3b574e44a3a12efa7c986b16b3e40489503501e4f01064417a60eda9a45`

## 1. Hypotheses and connectivity

The definition in (1) is exactly seven-contraction-criticality: `G` is
seven-chromatic and every proper minor is six-colourable.  The graph is
finite and simple, the displayed `K_{4,4}` is a specified subgraph on the
eight-vertex set `S`, and extra edges in `G[S]` are permitted.  The order
hypothesis gives `|V(G)|>=15`, so no small complete-graph convention affects
the use of Mader's theorem.

Mader's theorem gives seven-connectivity.  For every nonempty
`Y subseteq V(C)`, the set

\[
                   N_C(Y)\mathbin{\dot\cup}L(Y)
\]

contains every neighbour of `Y` outside `Y`.  If it had order at most six,
at least one vertex of the eight-vertex set `S` would remain outside it, so
its deletion would separate `Y` from that vertex.  Hence
`|N_C(Y)|+w(Y)>=7`, including when `Y=V(C)`.  These are exactly the boundary
inequalities required by the singleton-atom theorem.

## 2. The singleton contradiction

Assume that `C` has no safe three-contractible edge.  The cited audited
singleton-atom theorem has precisely the current hypotheses: a finite simple
seven-connected `K_7^-`-minor-free graph, a specified literal `K_{4,4}`,
and an exterior of order at least seven.  Its item 6 gives a singleton
all-edge atom `A={a}` whose full neighbourhood

\[
                         Z=N_G(a)
\]

has order seven and whose induced graph `G[Z]` is bipartite with class
orders three and four.  Thus `d_G(a)=7`, and the class of order four is an
independent subset of the open neighbourhood `N_G(a)`.

Dirac's neighbourhood inequality therefore gives the incompatible bounds

\[
  4\le \alpha(G[N_G(a)])
     \le d_G(a)-7+2=2.
\]

This proves Theorem 2.1.  In particular, "safe" has exactly the meaning
stated in the source: simplifying `C/uv` remains three-connected and the
union-labelled exterior retains all boundary inequalities.  It does not
mean that the ambient minor `G/uv` remains seven-connected.

## 3. Proper-minor colouring and the five bichromatic paths

For the selected edge `uv`, contraction strictly decreases the number of
vertices, so `G/uv` is a proper minor and has a colouring with at most six
colours.  Pulling it back across the contraction gives a proper colouring of
the edge-deleted graph `G-uv` in which `u` and `v` have a common colour
`alpha`.

The pulled-back colouring must use all six colours.  If it used at most five,
one endpoint could be recoloured with an unused sixth colour; the edge `uv`
could then be restored, yielding a six-colouring of `G`, contrary to
`chi(G)=7`.

There are consequently five other colours.  Fix one of them, `beta`.  If
the `alpha`--`beta` component containing `u` did not contain `v`, swapping
`alpha` and `beta` on that component would preserve properness and give the
two endpoints different colours.  Restoring `uv` would again six-colour
`G`.  Therefore `u` and `v` lie in the same `alpha`--`beta` component for
each of the five choices of `beta`, and each component contains the claimed
bichromatic path.

The corollary does not assert that these five paths are internally disjoint,
induced, exterior-contained, or otherwise compatible with one another.
None of those stronger properties follows from the Kempe-swap argument.

## 4. External citations

The cited source was checked at `arXiv:2507.03244v1`.  Its Theorem 15 states
Dirac's bound for independent sets in `G[N[v]]`; the order-four set above is
also an independent set in that closed neighbourhood, so the displayed open
neighbourhood form used here follows immediately.  Its Theorem 16 states
that every `k`-contraction-critical graph is seven-connected for `k>=7`.
Thus both external results are invoked at their stated strength.

The link to the critical-host degree-seven closure was also checked.  Its
Corollary 3 proves `delta(G)>=8` under the present critical-host hypotheses.
That citation is a consistent independent cross-check, not a dependency of
the direct Dirac proof.

## 5. Pinned repository inputs and inherited trust boundary

The direct audited repository input is pinned as follows.

| item | SHA-256 |
|---|---|
| singleton-atom theorem | `775a4f5a6cf2f455a2ca54a232146fd2f4b22a1c88e7e38770b26bfb83df8e07` |
| singleton-atom audit | `616278d73a0c978a98f972de6efe17786132d91198bceedf8b806dbf50824d88` |
| singleton-atom verifier | `fc6e0eb9173bfd24a9c823b0f5f0634ae10ed93a5a707e048268015733e97250` |

The adjacent singleton-atom audit pins its own relied-on audited sources.
Those source hashes were independently recomputed here:

| inherited source | SHA-256 |
|---|---|
| literal exterior three-connectivity | `4b863b62699f62131e874d22bda0af127fb29c73de7da82da46c1f3d3e34811a` |
| weighted-splitter small-atom reduction | `bc4f7d38d94beed2d86b9858a2290fd1cb85af398653b5b16a5d3231f80eb2db` |
| four-portal triangle completion | `965a92a736c4d9c891ebbd37f1bfd81415b864faea01c19e7b12adcac9787920` |
| exact seven-boundary double-cone theorem | `88b93cb80a4bd916fed0d10b68e74d0caba5c7c62492f8f667e59c0bef8a900e` |
| at-most-three components behind a seven-cut | `cbd3ecb73bea0530797ad58080ae6db6052bfbf69f90af558283e3f250772ef8` |
| closed-shore rooted connectivity | `ba6dbfe1ca9e89041b1a77174844c24598984cbe76349a55c41f15b2e997cc03` |

For completeness, the non-dependency cross-check has source hash
`6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67`
and audit hash
`360a121c2ca33bc81b6300551203956f9bca6c00866d3c524bfe3602c9744407`.

The inherited finite trust boundary is exactly the one stated in the
singleton-atom audit: Python integer, tuple and set semantics; successful
assertion execution; the explicit eleven-vertex construction; the complete
restricted-growth enumeration; and the stated automorphism action.  The
present proof adds no finite search and infers no unbounded statement from a
new order bound.

## 6. Exact unresolved scope

After contraction, `G/uv` is six-colourable and need not be seven-connected
or seven-contraction-critical.  The theorem therefore supplies one safe
edge in the original critical host but cannot be reapplied to obtain an
inductive sequence of safe contractions.  It covers neither exteriors of
order at most six nor nonliteral branch models.  It does not prove the
literal case of T44, T44, Norin--Totschnig Conjecture 21, or `HC_7`.
