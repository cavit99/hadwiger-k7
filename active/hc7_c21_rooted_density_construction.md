# Conjecture 21: rooted density construction

**Status, 21 September 2026:** conjectural construction towards the sole
selected conditional target, Norin–Totschnig Conjecture 21. Neither that
conjecture nor HC7 is proved here. The user's completion criterion remains
HC7 or our own theorem of comparable significance to Norin–Totschnig.

## 1. Changed external input

Dvořák, Norin and Rahman, *Every graph with no K7= minor is 6-colorable*,
[arXiv:2609.17760v1](https://arxiv.org/html/2609.17760v1), submitted
15 September 2026, state:

- Theorem 1.1: every `Q=K7-2K2`-minor-free graph is six-colourable.
- Theorem 1.3: every five-connected graph of order `n>=6` with
  `e>=4n-7` contains Q.
- Theorem 1.6: a minor-minimal non-six-colourable `K7^-`-minor-free graph
  is seven-connected and has `e>=4n-2`.

Their first theorem resolves Conjecture 19. Their density theorem directly
excludes our former remaining host: seven-connectivity implies
five-connectivity, minimum degree eight gives `n>=9` and `e>=4n`.
No neighbourhood or exterior-colouring case remains for that application.
These are external preprint results. The statements and this implication
have been inspected; we have not independently reconstructed their whole
proof. They are not our own completion of the user's objective.

## 2. Selected target and retained inputs

Prove that every finite `K7^-`-minor-free graph is six-colourable.
Equivalently, rule out its minor-minimal seven-chromatic counterexample.
Our audited [rooted-helper closure](../results/hc7_k7minus_degree7_rooted_helper_closure.md)
already gives minimum degree eight, `e>=4n`, and exclusion of literal K5
in this host. Thus the new external `4n-2` lower bound is not an improvement
over our present reduction.

We are testing a construction using rooted density across separators.
A sufficient broader theorem would give a `K7^-` minor in every
six-connected graph with `e>=4n`; its
[retained frontier](hc7_k7minus_sixconnected_4n_sparse_threecut_frontier.md)
has both two- and three-component obligations. Alternatively, a construction
may use the actual proper-minor six-colourings and avoid that broader theorem.
The exact root labels and branch-set ownership must survive either choice.

## 3. Immediate two-helper construction

For a graph F with five prescribed roots S, write
`rho4(F)=|E(F)-E(F[S])|-4|V(F)-S|`. It is **4-light** if every nonempty
root-free vertex set Y with at most four neighbours outside Y satisfies
`|E(F[Y])|+|E_F(Y,V(F)-Y)|-4|Y|<=0`.

Dvořák–Norin–Rahman Theorem 2.9 gives, when `rho4>=2`, five rooted bags and
two helper bags with either:

- both helpers full to all roots, with their mutual contact optional; or
- adjacent helpers, each missing at most one root contact, with the two
  possible missing contacts having distinct root ends.

The latter outcome has two missing contacts. Combining it with a rooted K5
on the other side proves Q, but does not prove `K7^-`.

**Candidate, unproved:** every 4-light five-rooted graph with `rho4>=2`
has such seven bags with at most **one** missing contact among the ten
root–helper pairs and the helper–helper pair. Root–root edges are not
required. Both helper bags avoid all prescribed roots.

This is a construction test, not an established equivalent of Conjecture 21.
Even if proved, its use in a complete density or critical-host induction
would require a separate proof of preservation and termination.

**First unresolved step in the tested induction.** Contracting an edge can
destroy 4-lightness. A positive fragment with at most four boundary vertices
in the quotient can lift to a five-rooted side of density exactly one.
The proposed density-two induction does not apply to that side. The old
theorem supplies only the two-missing-contact outcome. Contracting the side
to a boundary star can restore the density budget, but preservation of
4-lightness is unproved when a new fragment has the star centre on its
boundary. No recursion may skip this case or assume criticality in a proper
minor.

## 4. What the joint-centre attack supplied

The preceding attack found no independent completion before the external
C19 result was discovered. Its common-colouring constraints give signed
parity obstructions and original-host odd cycles through selected centres;
certificates for different colour pairs still need not have compatible
ownership. Two disjoint four-cliques and the guaranteed linkage likewise
do not supply all missing contacts. These are unpromoted deductions and
route nonclosures, not new completed cases.

The [audited six-cut application](../results/hc7_five_root_density_sixcut.md)
closes the complete four-, five- and six-edge boundary cases for arbitrary
host order. Retaining the sixth boundary vertex as a nonroot gives a full
rooted K5 without discarding its incidence edges. The zero- through
three-edge cases and the separate two-component case remain open. This
is a new application of external machinery, with no priority or
NT-equivalence claim.

The [star-replacement counterexample](../barriers/five_root_star_replacement.md)
shows that a density-preserving boundary-star contraction can destroy
4-lightness even when five external root paths exist. It does not satisfy
all restrictions of a minimal counterexample to the candidate. A valid
replacement using those additional restrictions remains possible.

Most discovery effort goes to constructing the missing contacts. Independent
checking targets the contraction and lifting steps once a complete candidate
exists. Further manuscripts, asymptotic improvements, T44 and formalisation
are not parallel campaigns.
