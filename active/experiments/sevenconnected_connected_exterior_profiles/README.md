# Connected exterior: one-miss profile reduction

This experiment supports the unbounded reduction in
[`hc7_k7minus_sevenconnected_degree_eight_one_miss_reduction.md`](../../hc7_k7minus_sevenconnected_degree_eight_one_miss_reduction.md).

Among the `607` target-free one-component quotient profiles in the critical
local census, seven-connectivity forces the missed local vertex to have
degree at least six.  Exactly `13` profiles survive that necessary degree
test.  A closed-shore rooted `K_4^-` completion eliminates nine of them.
Exactly four resist every four-root completion of this form:

```text
GhCKN{ / 7
GhEJE{ / 7
GjSKN[ / 7
GhEMNw / 7
```

Run from the repository root:

```text
UV_CACHE_DIR=/tmp/uv-cache uv run python \
  active/experiments/sevenconnected_connected_exterior_profiles/verify.py
```

The script uses the exact minor engine and complete order-eight generator
already imported by the adjacent degree-eight profile verifier.  It checks
all four-root sets, every possible missing rooted adjacency, and pins a
digest of explicit models for one canonical completion per eliminated
profile.
