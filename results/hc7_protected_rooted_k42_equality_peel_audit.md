# Internal audit: protected rooted-equality peel

**Audited source:**
[`hc7_protected_rooted_k42_equality_peel.md`](hc7_protected_rooted_k42_equality_peel.md)

**Audited source SHA-256:**
`c473a584ef855077f550608b02e615ea5aaa9251447efac92588eba45ff3618b`

**Verdict:** **GREEN.**  The protected-label refinement, coefficient-four
edge accounting and terminating reduction are correct.  The proof is
computation-free.  This is a separate internal mathematical audit, not
external peer review.

## Source-level check

The contractions were checked against the proof of Norin--Totschnig,
Lemma 12.  Its normalisation gives four minimal root paths ending at
distinct portals `Z'` and two maximal anticomplete helpers whose external
neighbourhoods lie in `Z'`.  A rooted model on either helper side extends
along the root paths, so each helper-side pair excludes the corresponding
rooted `K^*_{4,2}` model.  Its internal four-connectivity is the closed-side
consequence of the order-four helper separation and the internal
four-connectivity of the original rooted pair.

Completing `Z'` to a clique cannot create the forbidden rooted model.  The
added edges join distinct nominated root bags, while the target requires
only root--helper and helper--helper adjacencies.  Lemma 12 therefore gives

\[
 |E(J[V(J_i)\cup Z'])|-|E(J[Z'])|\le4|V(J_i)|
\]

for each helper.

## Contractions and labels

When a helper is nonsingleton, the published rooted-`K_4^-` construction
contracts both helpers into their portal set, deletes exactly the helper
vertices from the resulting vertex set, makes the portal set complete, and
preserves internal four-connectivity.  The total simple-edge loss is at
most four per removed helper vertex.

When both helpers are singletons `u_1,u_2`, the first contraction
`u_1v_1` loses at most four edges.  If it does not preserve the rooted
connectivity, the separation analysis in the cited proof gives, after
relabelling the portals, the repair

\[
                         J/u_1v_2/u_2v_4,
\]

which loses at most eight edges and restores internal four-connectivity.

If outcome 2 fails, neither helper meets `T`.  Thus every removed vertex is
unprotected.  Each contraction absorbs an unprotected helper into a portal;
in the two-helper repair the targets are distinct portals.  No two labels
in `Z\cup T` are identified, and a protected portal remains the labelled
surviving vertex of its contracted bag.  A rooted model in the resulting
minor would lift to one in the original graph.

Starting from `4|V(J)|-10`, the edge-loss bounds give the same lower bound
for the smaller pair.  Internal four-connectivity and exclusion of the
rooted `K^*_{4,2}` model let Lemma 12 supply the reverse inequality, so
equality is exact.  At least one helper vertex is removed, making iteration
well founded.

## Scope and unresolved obligations

The theorem concerns a rooted pair.  It does not prove that substituting
the smaller pair into a five- or seven-connected host preserves host
connectivity, external incidences or the separator from which the pair
arose.  It also does not classify the terminal equality pairs.  These are
genuine remaining hypotheses, not consequences of the peel.

The primary source checked was Sergey Norin and Agnès Totschnig,
[*Every graph with no `K_7^\vee`-minor is 6-colourable*, proof of Lemma 12](https://arxiv.org/abs/2507.03244).
