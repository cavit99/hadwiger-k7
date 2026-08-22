# Independent audit wrapper: the three-portal tetrahedral dichotomy

**Verdict: GREEN.**  At the exact revision below, four pairwise adjacent
disjoint connected exterior bags, each adjacent to at least three vertices
of a specified literal `K_{4,4}`, force a `K_7^-` minor except for the
classified tetrahedral portal profile.  A spanning exterior model excludes
that profile by global portal coverage.

**Audited source:**
[`hc7_k44_three_portal_k4_tetrahedral_dichotomy.md`](hc7_k44_three_portal_k4_tetrahedral_dichotomy.md)

**Source SHA-256:**
`407aba726108fd83b41834505c5220312b16584ec91ad34b9a6c0aeb0ad3d554`

This adjacent note is only a wrapper around the already completed
[independent internal cold audit](hc7_k44_closure_local_normal_forms_audit.md).
It records that audit beside the result, without adding a proof claim or
expanding its scope.

## Exact scope

The verdict covers the exact profile classification, the nine positive
fallback orbits, the proof that all seventy tetrahedral profiles are
target-free, and the spanning-exterior exclusion.  The exceptional profile
has four portal sets `S-{s}` on one common four-set `S`; when the four bags
span the exterior, seven-connectivity forces at least seven core portals and
rules it out.

Run the independent orbit-and-certificate verifier with

```bash
UV_CACHE_DIR=/tmp/t44-uv-cache uv run python \
  results/hc7_k44_three_portal_k4_tetrahedral_dichotomy_verify.py
```

The expected output is

```text
core_models 3784
restricted_failures 1170
orbits 12 positive 9 negative 3
negative_profiles 70
orbit_sizes [2, 32, 32, 36, 36, 48, 48, 72, 144, 144, 288, 288]
sha256 95b9d40e6e9ff1778b364b0a883fe0d72e7f41f9f5d9258c31af215ea38272bf
tetrahedral_near_miss_orbits 3 quotient_edges 19
classification_and_certificates_valid
```

The theorem does not show that an arbitrary three-connected exterior has a
spanning portal-rich `K_4` model, eliminate every nonspanning tetrahedral
component profile, or reconstruct a literal core from a nonliteral
`K_{4,4}` model.  It therefore does not prove the literal closure theorem,
T44, Conjecture 21, or `HC_7`.
