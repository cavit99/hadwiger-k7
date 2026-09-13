# Audit: order loss under density surplus

**Verdict: GREEN — separate internal audit.** Reviewed source
[quantitative_density_contraction_order.md](quantitative_density_contraction_order.md),
SHA-256 `999502f1b82814d3647e479712825d2ca17ba1f4eb5a3f22e18c213ee25c1127`.
This is not external peer review or a proof of the density target.

The lower bound covers every minor model, including vertex and edge
deletions. Singleton bags from distinct cliques of one original part
remain nonadjacent after contractions elsewhere. Thus independence at
most `k-s` forces at least s cliques per part to have no singleton bag,
affecting at least `k^2 s` vertices. If d vertices are deleted and the
nontrivial bags have sizes b, the exact order loss is
`d+sum(b-1)>= (d+sum b)/2`. This proves the claimed lower bound without
restricting bag sizes or ownership.

For attainment, the paired-part matchings use distinct vertices and
exactly `k^2 s/2` edges. Each contracted pair has endpoints in different
parts, so its bag is adjacent to every remaining bag or singleton.
The untouched graph has independence number `k-s>=1`; adjoining the
universal clique preserves that number. The resulting order and ratio
therefore give equality and a ratio strictly above r for every stated s.

The edge count, order cap and chromatic number also check directly:
each part needs k colours and the complete joins require disjoint
palettes, giving `chi(G)=k^2=r`. The surplus tends to infinity, but the
constructed minor explicitly violates the all-minor independence bound.
The family refutes a sublinear order allowance per independence decrease;
it refutes neither the density target nor critical reduction R. No
unresolved assumptions or gaps were found in the stated result.
