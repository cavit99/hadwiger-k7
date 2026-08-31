# Archive

This directory preserves superseded, retracted, frozen, and exploratory
research artifacts.  Nothing here belongs to the current proof spine merely
because it is retained.  Current status is recorded only in
[`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md), and live targets are listed
in [`../active/INDEX.md`](../active/INDEX.md).

The principal reader-facing preserved material is:

- [`manuscripts/`](manuscripts/), including the clearly marked historical
  rooted-web DRAFT;
- dated snapshots of the former research ledger, which preserve the proof
  spine as it stood at each pivot; and
- route-specific checkpoint directories, whose local `README.md` files state
  whether they are frozen, superseded, retracted or retained only as
  computational evidence.

For selected current proofs, use [`../results/README.md`](../results/README.md)
rather than searching this directory.

Historical scripts were written while they lived under `active/`.  A script
that imports a retained helper from that directory, or expects the bundled
dependency runtime there, should be invoked from the repository root with:

```sh
PYTHONPATH=active:active/runtime/deps python3 archive/<script>.py
```

An archived script may also depend on an environment or optional solver that
is no longer part of the current verification suite.  Its source is preserved
for provenance; only scripts named by a current result or audit are required
to run in continuous integration.
