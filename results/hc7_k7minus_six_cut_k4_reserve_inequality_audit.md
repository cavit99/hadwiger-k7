# Internal audit: `K_4`-reserve inequality

**Audited source:**
[`hc7_k7minus_six_cut_k4_reserve_inequality.md`](hc7_k7minus_six_cut_k4_reserve_inequality.md)

**Audited source SHA-256:**
`997dd39a178d7b8e3f528aa25d5c7db8b4cfd0eeb61619b0e5a427124f9ff929`

**Verdict:** **GREEN.**  The theorem and degree-sum corollary are correct.
The proof is computation-free.  This is a separate internal mathematical
audit, not external peer review.

## Connectivity lifts

Fix a shore `X` and let `Y` be the opposite shore.  A separation of
`(H[X\cup Z],Z)` of order at most three with nonempty open side in `X`
becomes, after deleting its separator together with `r,s`, a cut of `H` of
order at most five separating that open side from `Y`.  This contradicts
six-connectivity.  The same argument for the five-root pair adds only the
omitted vertex `s` to a separator of order at most four.  Both asserted
internal-connectivity properties are exact.

## Rooted-model composition

The fifth-root augmentation lemma applies to
`(H[X\cup Z\cup\{r\}],Z\cup\{r\})` and puts `r` in a helper.  The four
root bags are pairwise adjacent because their nominated vertices induce the
literal clique `H[Z]`; the helpers are adjacent by the definition of
`K^*_{4,2}`.  The connected opposite shore is adjacent to every root bag
and to the helper containing `r`.  Only its adjacency to the other helper
may be absent, so the seven disjoint connected bags form `K_7^-`.

Consequently the rooted model is absent.  Norin--Totschnig, Lemma 12,
applies at the correct internal-connectivity level and gives

\[
 |E(H[X\cup Z])|\le4|X|+6.
\]

Subtracting the six literal clique edges gives exactly the shore inequality
in Theorem 1.

## Essential-edge algebra

The audited essential-edge identity is

\[
 \delta_A+\delta_B=21+q(G)-|E(G[S])|.
\]

Writing `t=|E_G(\{r,s\},Z)|` and
`\varepsilon=\mathbf1_{rs\in E(G)}`, one has

\[
 |E(G[S])|=6+t+\varepsilon
\]

and, importantly,

\[
 |E_G(A\cup B,\{r,s\})|
 =d_G(r)+d_G(s)-t-2\varepsilon.
\]

Each edge from `\{r,s\}` to `Z` is counted once in the degree sum, whereas
`rs` is counted twice.  Substitution cancels `t` and gives

\[
 d_G(r)+d_G(s)\ge15+q(G)+\varepsilon.
\]

The corollary assumes the `4n-2` density, so `q(G)\ge0`; its degree-seven
consequence follows.

## Scope and unresolved obligations

The result requires a literal `K_4` in the six-boundary.  It neither forces
such a clique nor combines the inequalities from different essential-edge
cuts.  It does not produce a seven-connected density-preserving
contraction or prove the primary target.

The external rooted bound was checked in Sergey Norin and Agnès Totschnig,
[*Every graph with no `K_7^\vee`-minor is 6-colourable*, Lemma 12](https://arxiv.org/abs/2507.03244).
