# Internal audit: seven exceptional degree-eight vertices

Audited file:
`results/hc7_k7minus_seven_exceptional_vertices_corollary.md`

Audited SHA-256:

```text
5cf181ca631ba0e4f6f5235ca4357faac5bdcce3acde5ba8e83dde0e05e1a388
```

**Verdict:** **GREEN** for the exact revision above.

This is a separate internal mathematical audit, not external peer review.

## Exact dependencies

| Dependency | SHA-256 |
|---|---|
| Density and exceptional-vertex reduction | `604d11d4276ce6a3c57a8375d702624a1c364b5123f122b7e9e3dc18d11bf8f4` |
| All-degree-seven clique exclusion | `e2e5f5dc6c4456413e306c7844771157c5f3d9663553c1170e33a298a8148bf5` |
| Exact degree-seven neighbourhood theorem | `04e085032a096ef3fd508ca4ee287ef82417a718ae3d95646ae4cbd0b911ed2e` |
| Three-literal-`K_5` exclusion | `5b5e399122b996186e861f5075e7808c8e6fe4353082256ee12d5074499d2574` |

The two direct dependencies have identical critical-host hypotheses.  Their
proofs are independent in the relevant direction: the `n_7<=8` theorem
does not use the earlier exceptional-vertex lower bound.

External inputs retained through these results are Jakobsen's extremal
inequality as quoted by Albar, the Four Colour Theorem in the non-two-apex
reduction, Turan's theorem, and Mader's connectivity theorem for noncomplete
contraction-critical graphs.

## Seven-vertex lower bound

With

\[
                  \tau=\sum_{i\ge10}(i-9)n_i,
\]

the first audited source gives

\[
                  25\le2n_7+n_8-\tau
\]

and

\[
                  n_7+n_8-b\le10.
\]

Consequently,

\[
 25\le(n_7+n_8-b)+n_7+b-\tau
    \le10+n_7+b-\tau,
\]

so

\[
                  b\ge15-n_7+\tau.
\]

The second source gives `n_7<=8`, hence

\[
                  b\ge7+\tau\ge7.
\]

All algebra and inequality directions are exact.  A vertex lies in a
literal `K_5` precisely when its neighbourhood contains a literal `K_4`,
so the two descriptions of an exceptional degree-eight vertex agree.

The exceptional-vertex subgraph is `K_5`-free: a five-clique of exceptional
vertices would itself be a literal `K_5` containing all five.  Turan's
theorem gives `ex(7,K_5)=18`; seven vertices determine twenty-one pairs, so
every selected seven contain at least three nonedges.

## Exact `b=7` layer

If `b=7`, then `7>=15-n_7+tau` and `n_7<=8` force `n_7=8` and `tau=0`.
Thus there are no vertices of degree at least ten.  The density inequality
gives `n_8>=9`, while clique coverage gives

\[
                         8+(n_8-7)\le10,
\]

so `n_8=9`.  Minimum degree seven then leaves only degree-nine vertices
outside the displayed degree classes, and summing degrees gives

\[
                         2m=9n-25.
\]

Parity forces `n` odd.  The eight degree-seven and two nonexceptional
degree-eight vertices lie in the union of at most two literal `K_5`s.  The
union must have order ten, hence consists of exactly two disjoint cliques.
The all-degree-seven exclusion and the exact count of two nonexceptional
degree-eight vertices force each clique to have degree pattern `7^4 8^1`.
The two cliques are the only literal `K_5`s and are disjoint, so the four
degree-seven vertices in either clique have no second literal `K_5`.
Lemma 2(2) of the audited density theorem applies to that clique with
fifth-vertex degree eight and gives `n\ge8+13=21`.  This conclusion is
conditional on `b=7`; the lower bound `b\ge7` alone does not imply it.

## Finishing corollary

A minor-minimal non-six-colourable `K_7^-`-minor-free graph has every proper
minor six-colourable.  Deleting one vertex, six-colouring the remainder, and
then giving the deleted vertex a fresh colour proves that its chromatic
number is exactly seven.

Mader's theorem formally concerns noncomplete contraction-critical graphs.
That qualification is satisfied: a complete seven-chromatic graph is
`K_7`, which contains `K_7^-`.  Thus the host is seven-connected and has all
hypotheses of the theorem.  An upper bound of six exceptional vertices
would contradict the proved lower bound of seven.

## Unresolved assumptions and scope

No internal algebraic gap, circular dependency, hypothesis mismatch, or
finite-computation dependency was found.  The published inputs remain part
of the external specialist-review boundary.  The theorem supplies no upper
bound on exceptional vertices and does not itself prove the proposed
six-colour theorem.
