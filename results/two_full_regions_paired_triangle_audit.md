# Audit: two full regions and a paired triangle

**Verdict: GREEN.**

Audited [source](two_full_regions_paired_triangle.md), SHA-256:

`7659e3472a9710eed5e7e059c71ba9af4922f4bacd49bf66048c7df6a5078766`.

This is a complete exact-source internal review, not external peer review.
The reviewer previously checked the proof sketch and contributed separator
uncrossing comments; the present review independently reread the complete
written argument, including the explicit trimming of the two-path linkage.
A second reviewer, `route_assessment`, separately read the same frozen bytes
and reported GREEN without a requested correction.

The strongest steps check as follows.

- Both elementary constructions retain exactly one terminal from each
  triple per bag. Trimming the two disjoint paths removes any extra
  terminals; growing their union through one hub preserves disjointness
  and supplies their mutual adjacency.
- Component absorption preserves the actual connected full hubs. A
  component touching only one terminal triple cannot occur on a full
  three-path linkage, because all six terminals are its distinct ends.
  Its deletion is therefore a valid strict reduction.
- Contracting an internal hub edge has a fixed connected nonterminal
  preimage. A failed three-linkage in the quotient gives, by set Menger,
  an exact three-vertex separator whose third vertex is in the other hub.
  Otherwise that intact hub connects surviving terminal sets. Singleton
  hubs and literal terminal-to-terminal linkage paths are disposed of
  before this step.
- Every hub vertex lies in such a separator, so every fixed three-linkage
  spans the graph. The ends of every internal hub edge lie on different
  paths. These facts justify the separator-vector description; they are
  not consequences of connectivity alone.
- The coordinatewise minimum of two separating vectors is separating:
  its strict prefixes lie in both original prefix unions, while any
  strict suffix vertex lies in a suffix union of a vector attaining the
  minimum at that coordinate. A crossing edge would violate that cut.
  The first-internal-vertex cut and the final all-in-one-hub cut follow
  with the stated actual vertices, including when the two middle-path
  neighbours coincide. The intact opposite hub contradicts the latter.

No unproved rooted-minor theorem or finite enumeration is a premise. The
proof establishes the stated unbounded theorem with an unspecified pairing;
whole-graph three-connectivity is not required. Its application to a K5
scheme still requires the two actual full disjoint regions and the stated
three-linkage hypothesis. It neither supplies those allocations in every
scheme nor establishes K5 contractibility. No mathematical gap remains in
the theorem audited here; its novelty and comparative significance are
outside this audit's scope.
