# Internal audit: both-full component contractions

**Audited source:** `hc7_k7minus_both_full_component_contraction_dichotomy.md`

**SHA-256:**
`64159df71284e076a5c7ad6c1343e85bbb280fca1075036e52ff9ff2667bfca3`

**Verdict:** **GREEN.**  The new deductions are computation-free.  The final
dense four-connected branch uses Norin--Totschnig, Theorem 6, as an external
input.
This is a separate internal mathematical audit, not external peer review.

## Dependencies checked

| Input | SHA-256 |
|---|---|
| Exceptional-neighbourhood completion | `fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd` |
| Two-component literal-clique exclusion and density jump | `e1b54acdd971831786c0d8912d5e4189aaeedd84184540ed438e594aadb9b2e4` |
| Critical seven-cut capacity | `d4d650fee168fc2ff0e00a3b7b0faed6ff674ba8cd3c06c263f63c4170656f34` |

The cited repository revisions have adjacent GREEN internal audits.  The
statement of Norin--Totschnig's theorem used here is the four-connected
`4n-8` forcing theorem for `K_7^vee`, with exception
`K_{2,2,2,2}`.

## Mathematical check

The shore edge accounting gives

\[
 q_A=e_X+\Delta_B-16,\qquad q_B=e_X+\Delta_A-16.
\]

The critical density bound and `alpha(G[X])=3` imply
`q_A+q_B>=e_X-4>=3`; integrality therefore makes one contraction at least
`4|V|-6` dense.  The nonsingleton argument ensures both contractions are
proper minors.

Deleting at most two vertices from the uncontracted closed shore leaves
every surviving component attached to a surviving boundary vertex.  This
proves three-connectivity and shows that failure of four-connectivity is
exactly a separator `{a*,u,b_0}` with `b_0` a cutvertex of `G[X union B]`.
Every resulting block meets `X` and has exactly the neighbourhood stated in
the source.  Seven-connectivity forces five contacts in the original
contracted component.  Equality gives an actual order-seven cut.  The two
isolated boundary vertices contradict the critical `3,2,2` conclusion if
three components remain, so the asserted two-component packing alternatives
are exhaustive.

The wide-block edge count, the twin five-contact lemma, and the exclusion of
the Norin--Totschnig exceptional graph by the stronger `4n-6` density all
check.  A `K_7^vee` model in the contracted graph is correctly treated only
as a near model, not as a `K_7^-` contradiction.

## Exact limitations

The theorem does not make either whole-shore contraction seven-connected,
root the `K_7^vee` model at the contracted vertex, split a branch set
containing a twin, or eliminate the wide cutvertex-block residue.  It does
not eliminate the both-full case, prove exceptional-centre connectivity, or
settle the `K_7^-` six-colour conjecture.
