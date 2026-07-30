# Internal audit: nonfull attachment reduction

Audited file:
`results/hc7_k7minus_nonfull_attachment_reduction.md`

Promoted source SHA-256:

```text
2b269e7ecea09f695991689e2a6db64d928aedb141ea8cfbf85d14f84fc70617
```

**Verdict:** **GREEN** for the promoted exact revision.

The mathematical content was cold-audited at SHA-256
`088419b2889d52d909f478985031e3e033f7ff19290bb8efa35143c66fcfc685`.
Promotion changed only the status paragraph.  This is a separate internal
mathematical and computational audit, not independent human review or
external peer review.

## Exact dependencies and verifier

| Item | SHA-256 |
|---|---|
| Critical seven-cut capacity | `d4d650fee168fc2ff0e00a3b7b0faed6ff674ba8cd3c06c263f63c4170656f34` |
| Degree-seven neighbourhood classification | `04e085032a096ef3fd508ca4ee287ef82417a718ae3d95646ae4cbd0b911ed2e` |
| Adaptive `(1,2)` boundary closure | `df8d47261337659ade312bf8a6dfab22453c92bae5841bbb6b6fd303eadf6533` |
| Packet-demand identity | `33c613cf30a897bed843fac25563fef2d223cfb98eb57403d63dc885eb3d1b90` |
| Uniform defect-two carrier theorem | `7957de3aeb635a9f48e1e1668e34f43abbba15cac270c0f716821b2925af3fd8` |
| Exceptional-neighbourhood completion | `fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd` |
| Retained boundary verifier | `d0414ca3171f9a29e78030874eaa61c5c8b7f2e0d0650c0b866654d56e82bee3` |

The separately retained carrier verifier has SHA-256
`20ef45d8235dd6ad12b3688545473cc0bed98b4231945ef0be54c7d13c033a6b`.
The frozen-residual predicate implementation checked during the audit has
SHA-256
`b30af6f324292347a830d8a7abfea6966a37bfc34c4cffabc99f3879c89ade60`.

## Host reductions

The connected-rich diamond lift is valid: the shortest joining path makes
the two rich full subgraphs adjacent without losing disjointness or
fullness.  Together with the thin full subgraph and four boundary bags it
gives seven connected branch sets with at most one absent contact.

If both exterior components miss the same vertex, the three components
behind the resulting order-seven cut are exactly the two exterior
components and the centre--missed-vertex edge.  Critical cut capacity makes
the last component packing-one.  Seeing all seven boundary vertices would
give two singleton full subgraphs; seeing six makes the missed vertex have
degree seven, and the exact neighbourhood classification produces the
forbidden literal boundary `K_4`.  The same-miss exclusion is therefore
complete.

For one nonfull component, the joined side contains the full exterior
component and the centre as two disjoint full subgraphs, while the opposite
component is full.  The packing vector is exactly `(1,2)`.  The edge,
connectivity, clique, independence, minor and robust-block restrictions all
follow with the orientations stated in the proof.

The frozen-129 application was checked explicitly.  Independence number
three and `K_4`-freeness exclude robust independent blocks of order at
least four; the theorem excludes the remaining independent-triple case.
If `H-{a,b}` had a `K_4` minor, it would give a `K_4^-` minor in `H-a`,
contrary to the vertex-deletion condition.  These are exactly the two
frozen-residual predicates.

For the defect-two application, orient the separation as
`A=F union {u,x}`, `S=X-{x}`, and `B=E`.  In `A`, the disjoint connected
subgraphs `F`, `{u}`, and `{x}` are respectively full, full and of defect at
most two if `x` sees at least five boundary vertices; `E` is full in `B`.
All cross-shore anticompleteness conditions hold.  The carrier theorem
would six-colour the host, so `x` has at most four boundary neighbours.
Minimum degree seven, the edge `ux`, and the absence of `x`--`E` edges then
give at least two `x`--`F` neighbours.

For distinct misses, every claimed bag was checked for disjointness,
connectivity and literal contacts.  The adjacent-miss cuts are both
connected-rich `(1,2)` cuts.  In the nonadjacent case each joined side is
packing-one, and the displayed six-boundary constructions give exactly the
stated `K_4` and vertex-deleted `K_4^-` exclusions.

## Finite census

The verifier reproduced

```text
order-seven graphs=1044 alpha3=578 K4-free=353 sparse=103
diamond-deletion=29 one-nonfull-residue=28
residue sha256=a045e1d21098d0789ea1c549ed00f380ab97df9120335ff24127f9c8a039eacd
edges 5:1 6:4 7:10 8:11 9:2; connectivity 0:9 1:15 2:4; chi3=28
clique-OCT vertex:21 edge:4 none:3
PASS K7-minus one-nonfull boundary census
```

A separate audit decoded the nauty catalogue independently and replaced
the verifier's deletion/contraction minor tests by direct connected-bag
enumeration.  It checked all 266 possible five-bag models on subsets of
seven vertices and all 140 four-bag models on subsets of six vertices,
with no predicate disagreement.  All 28 survivors lie in the frozen 129;
their codes, digest and reported spectra were independently reproduced.

## Scope

No unresolved hypothesis, model defect or finite-encoding error was found.
The census classifies possible literal boundaries and does not assert host
realisability.  The theorem remains conditional on the separately audited
frozen-129 and carrier results.  It does not close either the one-nonfull
carrier-extraction problem or the overlapping `(1,1)` case, and it does not
prove shore allocation, the `K_7^-` six-colour conjecture, or `HC_7`.
