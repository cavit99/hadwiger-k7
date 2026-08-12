# Eight-terminal carrier composition at a dominated centre

This exact finite diagnostic applies the audited eight-terminal rooted
carrier trichotomy directly to `G-u`, with all eight vertices of `N(u)` as
roots.  It tests every labelled `C8`, `K3,5` and `F8` carrier against the
three surviving common-neighbour graphs, after adjoining the dominating
boundary vertex `v`.

Run from the repository root:

```sh
UV_CACHE_DIR=/tmp/hc7-uv-cache uv run python active/experiments/dominated_singleton_eight_terminal_carrier/verify.py
```

A positive test is an exact `K6`-minus minor decision on the eight-vertex
quotient.  The rooted quotient lifts in `G-u`; adjoining the singleton
centre `u`, which is adjacent to every rooted bag, gives `K7`-minus in `G`.
