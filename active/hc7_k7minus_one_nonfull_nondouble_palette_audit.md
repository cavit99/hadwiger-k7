# Internal audit: shore-localized one-nonfull response

**Audited source:** `hc7_k7minus_one_nonfull_nondouble_palette.md`

**SHA-256:**
`37b58be796053f8d1fe82b43626c0fdcad747f996d2bae6c606333505b193d17`

**Verdict:** **GREEN**, conditional on the cited one-nonfull reduction.
The deductions made in this source are computation-free.  Its application to
the critical host inherits the computer-assisted frozen-129/defect-two trust
boundary used upstream to prove `|D|<=4`.
This is a separate internal mathematical audit, not external peer review.

## Dependencies checked

| Input | SHA-256 |
|---|---|
| One-nonfull attachment reduction | `2b269e7ecea09f695991689e2a6db64d928aedb141ea8cfbf85d14f84fc70617` |
| Palette-permutation linkage | `2b0c30b9d8566f6da4959df145bf0f527249bf887dfa844d19a98e524080a9f2` |
| Two-colour separation or five-core | `e8ac71370bbefbd9bd7bd717b335a8e9179499fdbbe554a1c61d37a4e0701f93` |
| Five-core compression | `45e3d2e1a8aab16690c3941e5013c0f5bdc296ab257cea042dab1ceec7cb5557` |

Each listed revision has an adjacent GREEN internal audit.  The present audit
does not independently reproduce the upstream finite classification.

## Mathematical check

The common neighbourhood of `u,x` is exactly `D`.  If
`G-{u,x}` were five-colourable, the standard recolouring argument would force
one common neighbour in every colour, contradicting `|D|<=4`; deletion of
`u` supplies the reverse six-colour upper bound.  Thus the non-double-critical
palette hypothesis is exact.

In a six-colouring of `G-ux`, every `alpha,beta` Kempe component joining the
two ends can be confined to `F union S union {u,x}`.  Every possible
`E`-to-shore edge in that two-colour graph ends at a beta-coloured vertex of
`S`, already in the component containing `u`; hence `E` cannot join that
component to a different shore component.  The endpoint and internal-colour
claims for a colour absent from `c(D)` follow literally.  The separate
palette-permutation linkage correctly retains simultaneous vertex
disjointness only up to an endpoint-colour permutation.

In the five-core branch, the displayed seven branch sets have no possible
missing adjacencies except those from the outside pole to four rooted bags.
Contact with three bags would therefore give a `K_7^-` model, so at least two
bags are missed.  Such a missed bag avoids `S`; its required adjacency to
`x`, which is anticomplete to `E`, places the whole connected bag in `F`.
All branch-set disjointness and adjacency claims check.

## Exact limitations

The result does not bound a returned two-colour separator above by seven,
make the two shore bags boundary-full, or align the five labelled Kempe paths
with the four rooted minor bags.  It therefore does not eliminate the
one-nonfull case, prove exceptional-centre connectivity, or prove the
`K_7^-` six-colour conjecture.
