# Pairwise path composition diagnostics

**Status:** finite mechanism diagnostics; not a theorem about a hypothetical
critical host and not part of the active proof spine.

These scripts test whether pairwise pole-path reservations or small
triangle-contact quotients can be composed into the one simultaneous
allocation needed by the five-centre two-cut argument.

The deterministic checks currently record three scoped findings.

1. `pair_cast_k5_search.py` finds a five-bag quotient satisfying its
   relative-seven boundary test in which every pair of centres can be
   reserved by some minimal `p`--`q` route, but no one route reserves all
   five.  Thus pairwise reservability does not imply common reservability
   at quotient level.
2. `pair_cast_mycielski_search.py` checks `9,081,072` instances of the
   corresponding Mycielski-shore model and finds no such pattern.  This is
   a negative search, not an unbounded theorem.
3. `two_triangle_neighbourhood_search.py` finds all `1,032` valid patterns
   in its simplified two-triangle incidence model to be target-free.  The
   model omits the full critical-host colouring quantifiers and therefore
   gives no graph-level counterexample.

The remaining scripts are exploratory cover, random-search, and palette
incidence probes.  None is a certificate for the full five-centre theorem.

Run the principal deterministic checks with the locked environment:

```text
.venv/bin/python active/experiments/five_pair_cast_composition/pair_cast_k5_search.py
.venv/bin/python active/experiments/five_pair_cast_composition/pair_cast_mycielski_search.py
.venv/bin/python active/experiments/five_pair_cast_composition/two_triangle_neighbourhood_search.py
```
