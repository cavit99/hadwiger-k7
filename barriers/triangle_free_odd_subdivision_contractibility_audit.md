# Audit: triangle-free odd-subdivision obstructions

**Status:** separate internal mathematical audit, 5 September 2026.
This is an internal agent audit, not external peer review.

**Audited source:** [the written proof](triangle_free_odd_subdivision_contractibility.md),
whole-file SHA256
`2fbd3199943469303fbac7ca820312bed8188a98d2429290e4ab34762061bc03`.

**Verdict: GREEN** for Lemma 1, Corollary 2, Theorem 3, Corollary 4,
the explicit obstruction to the proposed two-family classification,
and the stated necessary structural restriction. No unresolved gap was
found under the stated hypotheses. The hereditary M'-sufficiency claim
remains explicitly conjectural.

## Exact external statements

The primary [Kündgen--Pelsmajer--Ramamurthi paper](https://arxiv.org/pdf/1207.6141)
was checked at Definition 7.2, Definitions 7.3--7.4, Theorem 7.7 and
Lemma 2.2. The source's two-copy graph is exactly their construction,
with copy indices renamed. For a triangle-free target, their criterion
requires a matching covering the neighbourhood of the independent set,
and an adjacency-preserving permutation moving every remaining vertex
to a neighbour. The empty independent set is permitted. The hereditary
claim in Lemma 2.2 concerns full rooted contractibility, as used here.
Theorem 7.10's internal-vertex parity convention converts to precisely
two odd paths and one even path in the excluded triangle-free theta.

The [Benchetrit--Sebő primary paper](https://arxiv.org/pdf/1509.05586)
was checked at Theorem 2.2, Lemma 2.3 and Theorem A.1. Its
odd-`C_3^+` subdivisions are the skewed thetas used in the source.
Theorem A.1 requires a simple two-connected graph; both assumptions
hold in the stated application. Its parameter is the maximum number
of odd ears, not the minimum. The source correctly treats the
result as a necessary target restriction. Appendix A.2 does challenge
Cao's construction procedure; the source does not use that procedure.

## Positive weights and the strongest inference

For a nonempty independent set `S`, every weighted incidence at `S`
goes to `N(S)`. Equal incident sums therefore give `|S|<=|N(S)|`.
If equality held, strict positivity would forbid both edges inside
`N(S)` and edges from `N(S)` to the remaining vertices. There are no
edges from `S` to the remaining vertices by definition. Connectedness
would make `S,N(S)` a bipartition of the whole graph, contradicting
nonbipartiteness. This verifies strict inequality without any hidden
regularizability or fractional-matching input.

In Theorem 3 each original weight lies strictly between zero and `d`.
Alternating it with `d-w_e` on an odd replacement path leaves weight
`w_e` at both original ends and gives incident sum `d` at every new
vertex. Thus the weighting survives simultaneously on every edge path.
An original odd cycle remains odd, so the new graph is nonbipartite.

The crucial shift obstruction uses an actually subdivided edge, with
first vertices `x,u,v`. An automorphism preserves degrees. Since
`u` has degree two and `x` has degree at least three, the shift condition
forces `pi(u)=v`. Preserving the edge `xu` then forces `pi(x)` to be
a degree-at-least-three neighbour of `v`. On a path of length at least
five there is no such neighbour. On a path of length three it must be
the other original end `y`; simplicity of the base graph ensures that
`xy` is absent after its unique edge is subdivided. Both alternatives
contradict the shift condition. Minimum degree, simplicity and actual
subdivision are therefore substantive hypotheses, not dispensable
conveniences.

Strict neighbourhood expansion excludes every nonempty independent
set in the external criterion. The shift argument excludes the empty
set. Together they rule out every fully rooted model in the specified
host `M'(H)`, whose canonical paths are an actual `H`-scheme. There is
no inference from an unsuccessful particular contraction to the
nonexistence of all models.

## Classification scope and proof obligations

For `K_4` with all six replacement paths of length three, a theta's
branch vertices must be original vertices. Its three paths must use
the direct route and the routes through the other two original vertices;
their parities are odd, even, even. Every odd cycle is a subdivided
triangle, and any two share a complete replacement path. This checks
both claimed absent obstruction families. The example refutes their
sufficiency for contractibility, while Theorem 3 supplies the explicit
scheme with no rooted model.

A subgraph of a triangle-free contractible graph is triangle-free and
contractible. It can contain neither the excluded theta nor a totally
odd `K_4` subdivision. Thus the cited structural theorem applies to
each nonbipartite two-connected subgraph exactly as stated. It supplies
no branch-set allocation in an arbitrary scheme, and the source does
not claim otherwise.

These arguments are direct, so no induction parameter or minor-lifting
step is required. All conclusions concerning failed contractibility
preserve the specified canonical roots. No finite computation is a
premise of this audit. Publication priority, a full classification,
Hadwiger's conjecture and significance comparable to Norin--Totschnig
are not established here.
