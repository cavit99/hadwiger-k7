# Separate internal audit: forcing prescribed roots

**Status:** separate internal audit.

**Verdict: GREEN.**
Audited on 5 September 2026 by the parent agent, independently of the
agent that wrote the proof. This is not external peer review.

## Exact revision

- [Theorem source](bipartite_weak_to_rooted.md), Theorem 1 and Corollary 2.
- SHA-256: `358782d3cf3ddc9d06cec3babd2824266c6eade2a11811797b85e488a75fefd8`.

## Checks

The construction adds disjoint pendant four-cycles at the prescribed
vertices, with `N_i=i(m+1)`. It is polynomial in the input orders, retains
bipartiteness, and makes the enlarged target have minimum degree two.

The forcing argument uses outside **vertices**, not the number of boundary
edges. Distinct target neighbours require distinct neighbouring branch
sets, and hence distinct outside vertices. A connected branch set avoiding
all prescribed host roots is confined to the original graph minus those
roots, or to the three-vertex interior of one attached cycle. The respective
outside-neighbour bounds `m-1` and `2` are valid.

Disjointness then makes the original target branch sets use exactly one
prescribed root each. A connected set using only root `r_j` cannot enter
attachments at any other root. Each of its own attached cycles contributes
at most two outside neighbours. The gap between successive `N_i` forces
the resulting root permutation to be the identity.

Restricting the original branch sets to the original host preserves their
connectivity, because every attachment meets that host at just one vertex.
Contacts between distinct original branch sets cannot occur inside an
attachment. The converse model extension is immediate and also works for
isolated target vertices. Empty targets are explicitly excluded from the
nontrivial counting argument.

The scheme extension in Corollary 2 satisfies both root exclusion and the
common-endpoint intersection condition. Disconnected target components
have disjoint scheme unions, and isolated roots can be restored separately.
The assumption is universal over enlarged targets, including targets whose
size depends on the original host. No implication from weak contractibility
of one fixed target to its rooted contractibility is asserted.

## Unresolved assumptions and limits

No gap or unresolved mathematical assumption was found in these two
statements. They do not establish universal bipartite contractibility, and
use no disputed external flow theorem. Novelty and significance have not
been established. The proof is independent of finite computation.
