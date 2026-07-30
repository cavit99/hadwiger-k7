# Internal audit: both-full shore reduction

The audited file is `results/hc7_k7minus_both_full_shore_reduction.md`.

The promoted source SHA-256 is
`8aa99a023ae2247dd24835a158c17677d1e3da218c9a431be36891e54119b758`.

**Verdict:** **GREEN** for the exact promoted revision.

The mathematical content was cold-audited at SHA-256
`f2f5cf20838a55c47b2ff28eb7cf04dad936dea61880e58f059d92e1cb5ad1ef`.
The subsequent changes only reflowed the Lemma 5 hypothesis and promoted
the status paragraph; they did not change a hypothesis, conclusion, model,
or calculation.  This is a separate internal mathematical and computational
audit, not independent human review or external peer review.

## Exact dependencies and verifier

The audited dependency revisions are:

- exceptional-neighbourhood completion:
  `fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd`;
- three-full-component boundary classification:
  `1d976b6ece78b66c08a87df36cfc3f31a3e8511d57aa6990aeaa28c7c67c76b3`;
- four-full-subgraph triangle completion:
  `bd0f4cd57a8973918380fb2cfc799b6c9120b8b00cacefb7bf23b81dba6ee486`;
- Kriesell--Mohr conversion as used in the degree-seven theorem:
  `04e085032a096ef3fd508ca4ee287ef82417a718ae3d95646ae4cbd0b911ed2e`; and
- retained boundary verifier:
  `168c56fdeb52c9835f95796750c82a0c06dfcad7781ca4a9a07affdfab07eb2f`.

## Host lifts

The shore-confined completion has seven disjoint connected branch sets.
The star bag and unused full component are adjacent to each other and to
all five rooted bags, so only the rooted near-model's one missing contact
can remain.

For every two-vertex boundary deletion, a `K_4^-` model combines with
the centre and the two oppositely anchored full components.  The three
nonboundary bags are connected, pairwise adjacent, and complete to the
four model bags.  This proves the unbounded diamond-deletion reduction.

## Finite classification

The verifier was rerun with nauty and reproduced all stated counts:
12,346 order-eight graphs, 2,076 exceptional boundaries, 15
diamond-deletion survivors with lambda distribution `5:1,6:7,7:5,8:2`,
and seven host survivors.  The two certificate digests are

```text
6e2633b0f4999a1d09fb98f38f7c268044cada0095be8e84aa4b8fe72d879ebe
bf063de64c772c1c9c1c83cba7dc39d11bb9c214f3e101595889fe63f25861a0
```

and the reserve-shape distribution is two `P_5`, three
`P_3\mathbin{\dot\cup}K_2`, and two
`2K_2\mathbin{\dot\cup}K_1` types.  A separate agent reconstructed the
graph6 census, exact deletion/contraction recursion for `K_4^-`, every
clique odd-cycle transversal, every minimizing independent triple, and the
reserve shapes.  It independently confirmed that both lambda-eight types
contain a triangle.  No encoding or completeness defect was found.

## Dynamic demand lemma and packet residue

Contracting the independent three-edge star gives a proper-minor colouring
whose triple has one colour and whose other five boundary vertices are a
rainbow transversal.  Every reserve nonedge has a bichromatic path whose
interior lies wholly in one exterior component.  If one shore supports all
but one of at most seven demands, Kriesell--Mohr Theorem 7 applies to the
selected at-most-six-demand graph inside that literal shore.  Literal
boundary edges supply all nondemands, leaving at most one missing rooted
contact.  The union identity for the two support sets then proves
`2 <= |A_E|,|A_F| <= q-2`, even when a demand is supported in both shores.

For lambda six and seven, two disjoint full packets in one component plus
the reserve `P_3` give a rooted `K_5^-`.  For lambda eight, three exterior
packets together with the centre are four disjoint full subgraphs, and the
classified boundary triangle gives a `K_7` model.  Positivity therefore
forces both exterior packing numbers to equal one.

## Scope

No unresolved mathematical hypothesis, branch-set defect, or finite
encoding error was found.  The result leaves seven exact packet-one
boundary types.  It does not construct a one-shore rooted `K_5^-`, close
shore allocation, prove the `K_7^-` six-colour conjecture, or prove `HC_7`.
