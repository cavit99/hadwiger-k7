# Independent cold audit: connected one-miss exterior reduction

**Verdict:** GREEN.

Pinned artefacts:

```text
bda284fabf9a414f73dee683474be3cf00d1bc973bc4d51c8f43b8d7771ad607  active/hc7_k7minus_sevenconnected_degree_eight_one_miss_reduction.md
b27f6cacd4122e01efb65d4d714f28d2a7da7ff7552768cbec2281d9de8ef5c0  active/experiments/sevenconnected_connected_exterior_profiles/verify.py
342693e517d87de5b8018e1d2692aa1d1979a7350107c9d8452e757020dbe64b  active/experiments/sevenconnected_connected_exterior_profiles/README.md
```

Contracting the connected exterior gives exactly the one-miss quotient
tested by the census.  The missed vertex has degree `1+d_J(r)` in the
host, so seven-connectivity gives the exact filter `d_J(r)>=6`.  A local
degree-three attached vertex has the centre and three local neighbours;
minimum degree seven therefore gives three distinct exterior neighbours
and hence the order needed for the rooted-diamond theorem.

For every selected four-set, the closed-shore separator lift is valid and
Jorgensen's rooted consequence supplies a rooted `K_4^-`.  A literal edge
between two roots guarantees the corresponding bag contact, so its sole
possible missing pair is among exactly the nonedges enumerated by the
verifier.  Replacing the four completed root vertices in a finite
certificate by the four rooted bags preserves disjointness, connectivity
and every certified quotient contact, including when a quotient bag uses
more than one root.

I reran the pinned verifier with NetworkX 3.6.1.  It regenerated the full
degree-viable catalogue, obtained thirteen profiles, eliminated nine by a
universally valid four-set, and left exactly

```text
(GhCKN{,7), (GhEJE{,7), (GjSKN[,7), (GhEMNw,7).
```

The canonical positive certificates reproduced digest
`7f684013b80ac226fddbc73405c7698a9040a01aaf1e58c0d8d9d1b432fa0500`.
The zero completion counts for the four residues are correctly stated
only as the limit of this method, not as host constructions.  The source
does not claim to treat the full exterior.  `py_compile` and
`git diff --check` pass.
