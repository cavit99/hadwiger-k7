# Second independent audit of the cycle-complement three-connectivity proof

Date: 8 September 2026.

**Verdict: GREEN — written proof under the stated hypotheses.**

This audit pins [the exact source](hc7_cycle_triangle_complement_three_connectivity.md)
at SHA-256:

    4e2b5b0b7b7294c30bdcdd1b4f147d12ba535dc3513508981160c5173d519228

I independently read the entire final source, including the unified capacity
argument in Section 2. The earlier separate-case draft at SHA-256
6aa02a8792d400d3db19f8762a9b4a24f972900a92b0bc6331e37cc159335477
was also reviewed; the final verdict is on the hash above.

## Strongest inferences checked

- **Actual separators.** The proof of two-connectivity and the boundary
  \(N_G(L)=C\cup T\) use original vertices and retain \(v\) outside the
  separated region. The three-component exclusion has three disjoint
  connected bags, all pairwise adjacent and full to the cycle.
- **All intersections of the cut with the triangle.** With
  \(k=|T-A|\), there are \(k+1\) source roots. A weighted cut of cost at most
  \(2k+1\) leaves a source, and its original boundary has at most
  \(2k+1+1+(2-k)=k+4\le6\) vertices. The component \(L\) survives outside it.
  Thus the unified proof covers \(k=0,1,2\).
- **Prescribed endpoints.** The initial paths to all \(T-A\) vertices
  exist in the stated side. Residual augmentation can preserve their
  terminal-to-sink flow: a simple augmenting path never leaves the sink.
  At full value every source uses its capacity two, preventing internal
  traversal of another source root. No initial individual path is
  assumed to survive augmentation.
- **The same-source bridge.** Its target set excludes the four terminal
  cycle vertices, so it lies in \(J-a_1\). Both cut vertices already belong
  to the other endpoint set. A bridge with interior avoiding both sets
  cannot make an excursion through \(L\). The retained T-path, the
  rerouted T-path and the untouched family's two C-paths have exactly
  the required disjointness. Endpoints at an A root or a T vertex cause
  no exception. Trimming terminal vertices leaves all donated sets
  inside \(K\).
- **Opposite-side hypotheses.** A matching of two cycle edges can keep
  any selected distinct pair of cycle contacts in different preimages.
  In \(G[L\cup C\cup T]\), the L-vertices retain their original
  neighbourhoods. Each loses at most one neighbour under the matching,
  and every nonempty L-set loses at most two boundary vertices.
  The designated five-root theorem therefore applies with nonroot
  degree at least seven and boundary at least five.
- **Seven-bag lift.** The two T-bags receive distinct A roots; \(D\)
  contains the third and remains disjoint from the complete model on
  the opposite side. The original singleton \(v\) contacts all six other
  bags. Designating a cycle root \(z\) contacted by \(D\) makes the only
  possible holes \(z t_i\) and \(D h\), with \(h\ne z\); these pairs are
  independent. All contraction preimages and donated sets are connected
  and pairwise disjoint.

## Inputs and scope

The source's two input hashes were checked against disk:

- cycle exterior theorem:
  6c5196ea71f77a1426d8bc24ef040e7fe85805ac0cb784d2d62d152a67303eb3;
- designated five-root almost-clique theorem:
  de183e350c412739c05a744e811304454ba90856efee9e097813c70617bba9cd.

The imported mathematical results remain dependencies, with their own
adjacent internal audits. No finite computation or external literature
search is a premise of this audit. No substantive correction to the final
source is requested, and no additional gap was found.

This is independent internal review, not external peer review. The result
proves three-connectivity of \(G-v-C\); it does not prove that the four support
sets and the A triangle admit a simultaneous connected bipartition.
The cycle case, Conjecture 19, and the user's global objective remain open.
