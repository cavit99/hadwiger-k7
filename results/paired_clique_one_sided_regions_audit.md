# Internal audit of the one-sided full-region theorem

**Verdict: GREEN.** Date: 8 September 2026.

The complete [source](paired_clique_one_sided_regions.md) was reviewed at
SHA-256 `d39271926d1cce2287de2369061b9c236a6355536bbd81b736661fbc4e6bed69`.
This covers the theorem for every `k>=2`, its reductions and lifts, and
the terminal-containing-cut corollary. No unresolved mathematical gap
was found within that scope.

## Provenance and inputs

The reviewer independently read the whole draft at SHA-256
`c39c9e6320dd5193a3ad40d6d20c6a0f8bd3d87b2adcd80d111c0030c556ff6a`,
including the changed terminal ownership conditions, and compared it
with the complete earlier full-region proof. The parent also conducted
a second internal source review before promotion. These are internal
reviews, not external peer review. The present reviewer had previously
audited the earlier full-region theorem, but did not author this new proof.

The final source was reread. Reversing exactly its status sentence and
two relative links recovers the reviewed draft hash; no mathematical
text changed. The earlier [source](paired_clique_full_regions.md) and
[audit](paired_clique_full_regions_audit.md) were read and their hashes
verified as `78121803cfc368cf0ff2e367d87dfc6747fbe888b0f3f5e994abdfe83ac5b8da`
and `fcac8b3ce460886ed52f0862cfddac28451df6a8280bc30b06622c63119c74ad`.
Hash agreement supplements the mathematical review; it is not its basis.

## Strongest checks

- Singleton-region induction deletes both reserved terminals. It is used
  only for `k>=3`, so the stated induction class closes.
- A permitted contraction has no R terminal and at most one S terminal
  in its connected preimage. The lifted separator has exactly k vertices:
  its two contracted-edge ends and one vertex in every other region.
  This excludes R vertices but permits S vertices, as required.
- The linkage spans after absorption. Non-S vertices occur in permitted
  edge cuts; S vertices are already linkage endpoints. The maximum cut S
  supplies their chain occurrences and the overlap for S--S region edges.
- The min/max cut argument remains valid with empty suffixes at selected
  S endpoints. Actual edges force overlapping occurrence intervals.
  Depth at most two gives an interval forest, whose connected spanning
  region is the same tree. The first cut therefore gives every claimed
  pairwise linkage contact, including paths of length one.
- In the corollary, each retained region component attaches to a retained
  cut port; the actual edge uv joins the two ports in its region. The
  other `k-1` original linkage paths avoid r and truncate to distinct
  ports, exhausting K. Thus the side theorem retains one original R root
  and one actual port in each of its disjoint bags.

The reduction of the earlier two-sided theorem also preserves all
hypotheses by assigning each S terminal to exactly one adjacent region.
The paired almost-clique target with only `k-2` regions remains open;
the side replacement supplies no unproved allocation for its last path.
Neither this audit nor the theorem establishes the project's global goal.
