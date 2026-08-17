# Full-exterior profiles at a degree-eight centre

This experiment supports the finite local lemma in the adjacent critical
degree-eight codegree-three dichotomy.

It regenerates all `542` order-eight local graphs satisfying the critical
neighbourhood conditions.  After adding a centre complete to the local
graph, exactly `56` quotients have no `K_7^-` minor.  Every one of those
`56` local graphs has at least four vertices of degree three.

The verifier also tests every four-root `K_4^-` completion.  This eliminates
`27` of the `56` profiles and leaves the following `29` graph6 codes:

```text
GhCKN{ GhEJC{ GhEJE{ GjSKLK GjSKNK GjSKL[ GjSKN[ GhdM@k GxaGis Gpq_is
GhEM`W GhEMdW GhEMbW GhEM`w GhEMdw GlO[PK GMs`KK GMs`Kk GhEMLo GhEMNo
GhEMJw GhEMNw GlgGiK GlgGik GhMIMc GhEK~_ GhEKzW GhEK~c GhEJ]o
```

Run from the repository root:

```text
UV_CACHE_DIR=/tmp/uv-cache uv run python \
  active/experiments/sevenconnected_full_exterior_profiles/verify.py
```

The script uses the exact minor engine and complete order-eight generator
already imported by the frozen degree-eight profile verifier.  It pins the
negative classification, explicit positive models, and explicit models for
one canonical four-root completion of every eliminated profile.
