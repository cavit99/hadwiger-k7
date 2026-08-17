# Degree-eight full/one-miss quotient census

**Status:** computer-assisted finite result supporting the live
seven-connected codegree-two investigation.  It is not an unbounded
codegree theorem.

Let `J` be an eight-vertex graph satisfying

```text
delta(J)>=3,   K_6^- is not a minor of J,
K_4 is not a subgraph of J,   alpha(J)=3.
```

Add a vertex `v` complete to `J`.  An exterior image is nonadjacent to `v`
and adjacent to all of `J`, or to all but one vertex of `J`.

The verifier proves the following exact finite statements.

1. There are `542` eligible unlabelled local graphs.  Of their `4,878`
   one-image profiles, `663` are `K_7^-`-minor-free, on `155` local
   graphs.  Every one of those `155` graphs has connectivity two or three.
   Thus a single contracted exterior component does not prove a
   codegree-two conclusion.
2. Of the `24,390` profiles with two nonadjacent exterior images, exactly
   four are `K_7^-`-minor-free.  In all four, `J` has graph6 code
   ``GMs`KK`` and the missed pair is one of

   ```text
   (3,5), (3,6), (4,5), (4,6).
   ```

   This cubic graph consists of the two diamonds on
   `{0,1,3,4}` and `{2,5,6,7}`, joined by `07` and `12`.  The two misses
   lie in the opposite adjacent twin pairs `{3,4}` and `{5,6}`.

The second statement applies to exterior components of arbitrary order:
contract each connected component to one image.  It reduces the
two-component case to one explicit boundary profile.  Seven-connectivity
then eliminates that profile by a rooted `K_4^-` model on
`{2,3,4,6}`.  The computation-free argument is written in
[`hc7_k7minus_sevenconnected_degree_eight_exterior_connectedness.md`](../../hc7_k7minus_sevenconnected_degree_eight_exterior_connectedness.md).
The verifier also checks the four direct completion rows used there.

## Reproduction

From the repository root run

```text
UV_CACHE_DIR=/tmp/uv-cache uv run python \
  active/experiments/sevenconnected_codegree2_profiles/verify.py
```

NetworkX `3.6.1` is pinned by the repository lockfile.  The verifier imports
the audited exact minor engine and complete order-eight extension generator
from
[`hc7_k7minus_sixconnected_degree_eight_low_codegree_verify.py`](../../../results/hc7_k7minus_sixconnected_degree_eight_low_codegree_verify.py).
It checks each positive minor model and pins sorted certificate digests for
both censuses.
