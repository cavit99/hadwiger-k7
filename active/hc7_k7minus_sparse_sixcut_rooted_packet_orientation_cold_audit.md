# Independent cold audit: sparse six-cut rooted packet orientation

**Verdict:** GREEN.

Audited source:

```text
efe0df2eaa66e26f80544d990bbbe321cc12e829ca7854d8ff27dc953a3bc990  active/hc7_k7minus_sparse_sixcut_rooted_packet_orientation.md
```

The current source SHA-256 is
`4043882d33a80eef5934e59aa3632b3e969bf7c01f05d8f5153c8de541978671`.
The only post-audit change marks the source as independently audited; the
mathematical text is unchanged.

Five disjoint full packets give the seven displayed bags.  Four anchor
roots make four packet bags connected and mutually adjacent; each anchored
packet also meets the fifth packet, and both unabsorbed root singletons
meet every packet.  Only the singleton pair may be absent.  Thus the total
packet number is at most four, with no boundary-edge hypothesis.

For Lemma 2, the four rooted bags, `Q_1 union {p}`,
`Q_2 union {q}`, and the third full component are disjoint and connected.
Fullness supplies every root contact.  The two anchored packet bags meet
through the `p` contact of `Q_2`, while the third component meets them
through its `p` and `q` contacts.  These are seven pairwise adjacent bags,
so a rooted model in one lobe really forces both opposite packing numbers
to one.  This argument uses full packets, not the invalid arbitrary
four-carrier anchoring step.

Combining that lemma with the independently audited forced-root theorem
gives exactly the vectors `(1,1,1)` and `(2,1,1)`, with the entry two only
in the uniquely rooted lobe.  If a second lobe is rooted, reorienting Lemma
2 forces the remaining entry down to one.

The conditional calculation is also exact.  If
`Delta(G[S])<=1`, the six-vertex boundary is a matching of at most three
edges and total packet number is at most four, so the proposed bound
`eta<=5mu` would give total excess at most twenty, below
`24+sigma-b`.  If `Delta(G[S])>=2`, the audited connector--anchor theorem
forces all three packet numbers to one; total excess at most fifteen is
below `24+sigma-b` because the sparse boundary has at most six edges.

The source labels `eta<=5mu` explicitly as unproved and makes no claim
that the sparse row is already eliminated.  I found no bag, orientation,
arithmetic, dependency, or scope error.  `git diff --check` passes.
