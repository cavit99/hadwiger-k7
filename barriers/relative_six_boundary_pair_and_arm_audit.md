# Audit of the pair-path allocation barrier

Date: 12 September 2026.

**Verdict: GREEN** for the stated local counterexample, for every `m>=2`.
The [source](relative_six_boundary_pair_and_arm.md) has SHA-256
`65d7a300fc205fbb289d5eaedac2694837a2abb6463ec459401fb401c7a2bd85`.
The reviewed draft was `c2ec431187ebb436ec3b2f8df5c25cd9056ea2c2a3ebbbfb419db5177e2e5488`;
only its status paragraph changed after review.

Every path vertex has degree six, including both endpoints when `m=2`.
For any proper nonempty X-subset, a component interval has two distinct
external path-or-v neighbours in addition to u and the three P roots.
For the whole X, the two additional neighbours are v1,v2. Thus the
six-neighbour condition holds for every nonempty subset, not just intervals.

The prohibition on other roots as internal path vertices is essential:
under it the v1--v2 path uses all of X, whereas every u--P path uses X.
The claimed alternative arms exist by using opposite path endpoints and
distinct P roots. Each v root has only one X-neighbour, as the scope notes.

This is a separate internal mathematical review of the parent's construction,
not external peer review. No computation or external theorem is a premise.
The example refutes only the local simultaneous pair-and-arm allocation;
it does not refute the five-root target or establish any Hadwiger conclusion.
