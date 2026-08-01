# Internal audit: full-side vertex exclusion and minimum exterior

**Audited source:** `hc7_k7minus_one_nonfull_full_vertex_exclusion.md`

**SHA-256:**
`c13889297cbfafabc4056532ee86d49793cae2aa98e0c0c19b3f8759da4019bc`

**Verdict:** **GREEN.**  The two deductions are written and unbounded.  They
inherit the computer-assisted trust boundaries of the degree-eight
exterior-component bound and the uniform defect-two reflection theorem; no
new finite computation is used.  This is a separate internal mathematical
audit, not external peer review.

## Dependencies checked

| Input | SHA-256 |
|---|---|
| One-nonfull nested-cut theorem | `e1b54acdd971831786c0d8912d5e4189aaeedd84184540ed438e594aadb9b2e4` |
| Degree-eight exterior-component bound | `4ee48c6d71c994b166b29dcd969d64c3526e6b6b75fa8a849fae834cf95eea29` |
| Exact degree-seven neighbourhoods | `04e085032a096ef3fd508ca4ee287ef82417a718ae3d95646ae4cbd0b911ed2e` |
| Same-miss exclusion | `2b269e7ecea09f695991689e2a6db64d928aedb141ea8cfbf85d14f84fc70617` |

Each dependency has an adjacent GREEN internal audit.  The one-nonfull
nested-cut theorem itself invokes the frozen 129-boundary uniform
defect-two reflection result.

A fresh clean invocation of that retained verifier on 1 August 2026,

```text
uv run --with networkx==3.6.1 python \
  results/hc7_exact7_all_residual_defect2_probe.py
```

returned `boundaries=129`, `cells=3741`, `witnesses=3741`, `failures=0`,
and `CERTIFIED full-residual defect-two carrier reflection`.

## Full-side vertex check

For an `S`-full vertex `v` in the full exterior component, the singleton
`P={v}` is an allowed connected subgraph in the nested-cut theorem.  Its
attachment set `B` is a subset of the singleton, so `|B|<=1`.  The theorem
simultaneously gives

\[
                         |A|\le4,
 \qquad
                         |A|+|B|\ge6.
\]

Thus `|A|>=5`, a contradiction.  The proof of the cited theorem handles
exactly this inequality by applying uniform defect-two reflection to the
three disjoint connected subgraphs `\{u\},P,K`; that reflection produces a
six-colouring.  The new theorem therefore has one of the declared terminal
outcomes and is not a static boundary exclusion.

## Minimum-component check

The two-component literal-clique theorem removes every literal `K_5` and,
with the exact degree-seven theorem, raises minimum degree to eight.  A
singleton minimum component would be a false twin of its centre and would
extend a six-colouring of `G-u`, so the selected component is nontrivial.

For a degree-eight `v` in the selected component `E`, an internal neighbour
leaves at most seven neighbours in `X=N(u)`.  If the opposite component `F`
meets a boundary vertex missed by `v`, every additional component of
`G-N[v]` lies in `E` after deleting `v` and an internal neighbour, and is
strictly smaller than `E`.  Since `v` is exceptional, that contradicts the
minimum choice.

Otherwise seven-connectivity forces one missed vertex `y` and

\[
                         N_X(v)=N_X(F)=X-\{y\}.
\]

The same-miss exclusion supplies an attachment of `E` at `y`; hence `E` is
the full exterior component relative to `u`, while `v` sees all seven
vertices of the common set.  The full-side vertex theorem gives the required
contradiction.

## Exact limitations

The theorem proves connectivity for every degree-eight vertex inside one
selected minimum exterior component.  It does not prove connectivity for
the originally selected centre, force the selected component to contain a
degree-eight vertex, eliminate the general one-nonfull attachment pattern,
or settle the `K_7^-` six-colour conjecture or `HC_7`.
