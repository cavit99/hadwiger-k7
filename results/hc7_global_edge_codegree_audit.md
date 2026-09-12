# Independent audit: global edge codegree and contraction consequences

**Audited source:** [hc7_global_edge_codegree.md](hc7_global_edge_codegree.md),
SHA-256 `741b99349c61e632c3d9cd4711f339280b1f2044ca40d30fbdc8e49e9b17c0a5`.
**Reviewer:** separate internal audit by `exterior_joint_model`, 12 September 2026.
**Verdict: GREEN.** All three theorems and the stated additional consequences
follow from the pinned inputs. No unresolved inference was found.

## Inputs and first two theorems

I checked all five source hashes and all five adjacent-audit hashes against
current bytes; each audit also identifies the corresponding source hash.
I inspected the exact NT alternative as recorded there, the wheel theorem,
two-edge-contractions Theorem 1, the contact bounds, and Corollary 3.
Four-connectivity excludes both recorded NT cut alternatives; nonplanarity
excludes its plane alternative. The extension permits the fifth root to
belong to an initial bag. Thus the five-root wheel consequence is applicable.

In Theorem 1, deleting two vertices leaves five-connectivity and minimum
degree six. Euler excludes planarity. The five common roots contact both
untouched endpoint bags, and `K2 join W4` is exactly `K7-2K2`.

In Theorem 2, every cut of size at most five lifts to at most six vertices.
The merged degree is exactly `d(a)+d(b)-2-c(ab)>=10`. Only old degree-eight
common neighbours can become degree seven, so there are at most four.
After deleting any two endpoints, minimum degree is five and at most four
vertices have degree five; Euler requires at least twelve. This verifies
the new codegree bound without assuming planarity is contraction-invariant.
The six-connected class in the cited two-edge theorem has precisely the
needed hypotheses, including when the next edge meets the merged vertex.

## Paired contraction and limits

Corollary 3 bounds each outside vertex's clique contacts by two. The contact
theorem applies because clique vertices have at least five outside neighbours
and deleting any clique triangle leaves G connected. Its total bound of five
makes the three matching counts sum to at most five, so one count is at most one.
The exact loss is five internal edges and one contact per counted vertex:
`e(J)=e(G)-5-D`, hence `q(J)=q(G)+3-D`. No other contacts coalesce.
Only those D outside vertices lose degree. Each pole has one other-pole
neighbour and at least eight outside neighbours, using `c_G(ab)-2<=2`.

For a cut of size at most five, zero or one deleted pole gives a preimage
of size at most six in G. Two deleted poles leave F minus at most three
vertices, connected by the explicitly assumed four-connectivity of F.
The two edge preimages are disjoint and connected, so all minor models lift.
Deleting two vertices of J leaves at most one degree-five vertex; the same
Euler argument and the cited two-edge theorem therefore apply to J as well.

This audit accepts the pinned prior results as inputs, without a new primary
literature audit. It establishes no further contraction closure, chromatic
preservation, C19, HC7, or comparative-significance claim.
