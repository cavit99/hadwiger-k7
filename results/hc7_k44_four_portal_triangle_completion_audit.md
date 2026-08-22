# Independent audit wrapper: four-portal triangle completion

**Verdict: GREEN.**  At the exact revision below, a triangle of three
pairwise adjacent disjoint connected exterior bags, each adjacent to at
least four vertices of a specified literal `K_{4,4}`, forces a `K_7^-`
minor.

**Audited source:**
[`hc7_k44_four_portal_triangle_completion.md`](hc7_k44_four_portal_triangle_completion.md)

**Source SHA-256:**
`965a92a736c4d9c891ebbd37f1bfd81415b864faea01c19e7b12adcac9787920`

This adjacent note is only a wrapper around the already completed
[independent internal cold audit](hc7_k44_closure_local_normal_forms_audit.md).
It does not repeat or extend that audit and makes no fresh proof claim.

## Exact scope

The GREEN verdict covers the exhaustive finite core lemma, the ten explicit
fallback orbits, and the host-level lift obtained by first contracting the
three connected exterior bags.  Extra host vertices and edges are harmless;
the conclusion is therefore not limited to the eleven-vertex core used by
the enumeration.

Run the independent orbit-and-certificate verifier with

```bash
UV_CACHE_DIR=/tmp/t44-uv-cache uv run python \
  results/hc7_k44_four_portal_triangle_completion_verify.py
```

The expected output is

```text
core_models 1656
fallback_profiles 1140
orbits 10
orbit_sizes [36, 36, 36, 72, 96, 144, 144, 144, 144, 288]
sha256 755316af73023902cbe205ec2f0b914b25677a61a5fb77dc129567a46fe6f552
all_ten_certificates_valid
```

This theorem does not force such a triangle in a three-connected exterior,
prove the open core-sensitive trichotomy, or turn a nonliteral `K_{4,4}`
minor into a literal one.  It therefore does not prove T44, Conjecture 21,
or `HC_7`.
