# Separate internal audit: bipartite-flow prefix counterexamples

**Status:** separate internal audit.

**Verdict: GREEN.** The verdict covers only the stated intermediate-claim
counterexamples. Audited on 5 September 2026 by the
parent agent independently of the construction-note author. This is not
external peer review or an audit of the paper's spectral conclusions.

## Exact revisions

- [Written construction](bipartite_flow_prefix_construction.md), SHA-256
  `f87c9ff55d22528296858876ba724ea9fc1f0a3138427f49d6226a5e6205f4ee`.
- [Certificate verifier](../active/experiments/bipartite_contractibility/flow_prefix_counterexample.py),
  SHA-256 `a3a1ed5d4ac3d7473ab1cbccd6eccf822cb2457544772f7d832d334b56d08820`.
- Published source PDF: SHA-256
  `486fffa16995ab4ad9a323dd9adb60775bdfa3b6607e6e0cd0dc8abc9a9b54ad`;
  source links and version qualifications are in the construction note.

## Source and mathematical checks

The auditor independently read arXiv:0808.0148v2, pp. 9--10, and the
published PDF, pp. 13:10--13:11. The published definition reverses the
intersection wording; that apparent typographical error is explicitly
distinguished from the substantive prefix failures. The examples meet
the v2 independent-intersection convention. They are not claimed to meet
the literal reversed convention in the published display.

The seven-vertex example is a valid ordinary scheme. Computing the first
foreign left-star vertices gives the stated prefixes, and the proposed
right branch `{x,b_0}` has no edge. Each `y_i` is a suffix vertex that
belongs to a different prefix from the same left root. This directly
refutes the exclusion used in Lemma 3.5.

The eight-vertex example is a valid coloured scheme: all nonroots have
degree four, every path alternates its endpoint colours, and independent
demand edges have disjoint paths. The prefix construction leaves the left
roots singleton and places both left clones in both right branches. This
directly refutes Lemma 3.6. Its first unsupported inference confuses being
past an earlier stopping point with belonging to another left star.

Both displayed alternative rooted models are connected, disjoint, contain
the four required roots and have all four required contacts. Thus the
examples do not refute the main minor-existence statement under its intended
intersection convention. The general singleton-prefix observation follows
from coloured-scheme path membership and minimum target degree two.

## Verification and limits

The deterministic verifier was read and run through the project environment.
It prints complete path systems, computed prefixes, failed inclusions and
valid rooted-model certificates for both examples. Both records pass.
The written counterexamples do not rely on a finite-search extrapolation.

No gap was found within the stated scope. A different proof could establish
the external minor statement; no claim about its truth, the universal
bipartite target, or the paper's spectral consequences follows from these
counterexamples alone.
