# Rooted-status aggregate nonclosure

This verifier certifies two explicit six-connected graphs at the exact
returned density.  Each has a six-vertex cut `S`, three `S`-full
components, order `32`, size `128`, and one of the two surviving packet
vectors:

```text
boundary       component excesses    packet vector
one edge          17,3,3               (1,1,1)
independent       18,3,3               (2,1,1)
```

The examples satisfy, exactly:

- the no-rooted-four-set Norin--Totschnig inequalities whenever the
  corresponding rooted model is absent;
- every general common-four singleton capacity;
- every capacity-one conclusion transferred from a rooted model in
  another lobe;
- the joint singleton-incidence bounds;
- the rooted-model packet orientation and total packet cap; and
- the returned identity `|E(G[S])|+sum eta(C)=24`.

Rooted status is not merely assigned arithmetically.  The verifier
exhausts every rooted-bag allocation in each three-vertex thin lobe and
pins explicit two-vertex-bag rooted `K_4` models for all fifteen four-sets
in each rich lobe.  It also exhausts the internal six-connectivity
condition and checks global vertex connectivity with NetworkX.

These graphs are **not** target-free and are not counterexamples to any
Hadwiger statement.  In each rich lobe, for every omitted boundary root,
five explicit two-vertex rooted bags form a `K_5^-` model.  The other two
full lobes therefore complete it to a `K_7^-` minor.  This is the point of
the experiment: aggregation by four-root status and singleton incidence
forgets the five-root terminal model, so those audited numerical
constraints alone cannot eliminate either packet orientation.

Run from the repository root:

```text
UV_CACHE_DIR=/tmp/uv-cache uv run python \
  active/experiments/sparse_sixcut_rooted_status_aggregate/verify.py
```

Frozen verifier SHA-256:

```text
81fecdeab0a4df0591ee48f076932e415a635a5caf6abd49841d304b6e4b623b
```

The pinned rooted-status and five-root transcript digests are

```text
f9715fd15b51f3a5aec2845c279ba08c5f930014e8bc82438f1fec60769417d3
438e6fb39a5394cf0d11ab0d6101ab8adee2a2d4befe7cdfbf457a764658eeac
```
