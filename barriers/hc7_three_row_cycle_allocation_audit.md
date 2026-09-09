# Audit: three path rows with distinct contacts need not give Q

Date: 9 September 2026.

**Verdict: GREEN — independent internal whole-source review.** The
reviewed [source](hc7_three_row_cycle_allocation.md) has SHA-256
`e961fe0acca656c3685791eed662c425a4e661ab133140fa1d4a379653da5c08`.
Its written exclusion covers arbitrary Q minor models, not only models
respecting the three displayed rows.

## Strongest checks

- A hypothetical model can be extended to span the connected host.
  A bag containing p but no x vertex would be the degree-four singleton
  p, impossible in Q. Every remaining bag without an x vertex is a
  proper cycle interval of length at least three.
- Mergers of x vertices are initially allowed. With at most three
  x-containing bags, four cycle triples consume the whole cycle. Their
  two independent missing contacts exhaust Q's allowance, but a bag
  containing just one x vertex cannot contact all four triples. Thus
  exactly four x bags, one per x vertex, are forced.
- The three remaining intervals need at least two mutual contacts, so
  all donated cycle vertices form a single block of length at most three.
  Before donation the four x bags have four mutual edges, regardless of
  which contains p. Length zero or one cannot repair them. Length two
  adds at most one edge and forces interval lengths 3,4,3 with full
  outside contacts. Length three forces three triples, a complete x-bag
  graph, and full contacts at both end intervals.
- The three length-two and six length-three table rows exhaust the
  twelve starting positions for each length under those conditions. The
  forced end owners and every connected owner string were checked
  directly against the word. No third owner can connect through p or
  another x vertex, since every x bag contains exactly one x vertex.
  Length-two strings add no outside edge; the five feasible length-three
  cases add at most one, respectively 23,23,23,03,01. Both are insufficient.
- The displayed paths and four outside contacts realise the exact
  equal-pair transfer. The three cases for deleting two vertices cover
  all deletions and leave the graph connected. The given three-colouring
  respects every cycle, spoke, matching and p edge; a triangle proves
  that two colours do not suffice.

## Scope and provenance

This review uses the written structural classification and its explicit
table; no program or finite search is a premise. The reviewer had not
developed this cycle example and read the complete proof independently.
The review found the start-5 new-edge label, now corrected to 23 in the
pinned source. The parent authored the proof and Bacon had separately
checked it before this review. This is internal, not external peer review.

The host is three-connected with minimum degree three and chromatic
number three. It refutes the relaxed distinct-contact path-row condition,
not the transfer separator theorem or a construction using the actual
seven-connected, minimum-degree-eight critical host. C19 and HC7 remain
outside the claim.
