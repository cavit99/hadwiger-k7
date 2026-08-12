# Cold audit: dominated-singleton saturated five-root reduction

## Verdict

**GREEN for the stated dominated-singleton application, with one formal
scope qualification.**  I independently checked
[`hc7_k7minus_dominated_singleton_rooted_five_reduction.md`](hc7_k7minus_dominated_singleton_rooted_five_reduction.md)
at source SHA-256
`c7a8ae5457fef4925aaed616889a8aaab6fc6db92f5798c4a2af1387e96f0433`.

The source correctly proves the five-chromatic saturated-set reduction, the
two apex lifts, and the five-connected nonplanar remainder.  It also scopes
the Kelmans--Seymour theorem, the Dominating 4-Colour Theorem, the universal
five-terminal theorem and Holroyd's conjecture correctly: none of them is
silently promoted to the missing `Q`-rooted `K_5^-` model.

The sole qualification is expository.  Proposition 3.2 chooses five vertices
of `Q`, so it requires `|Q|>=5`.  This is automatic in the intended
dominated-singleton application, where Section 1 records `|Q|>=7`, but it is
not a consequence of the more abstract hypotheses preceding Theorem 2.1.
Thus Proposition 3.2 should be read in the application state (or with the
additional hypothesis `|Q|>=5`).  No live deduction is affected.

## 1. Colour-class decomposition

Let `Gamma=c^{-1}(0)`.  The colouring `c` is proper in `G-uv`; hence every
edge of `G[Gamma]` would have to be the sole deleted edge `uv`.  Since both
ends of `uv` have colour zero, this gives exactly the facts used later:

* `Gamma-{u}` is independent;
* `u` is anticomplete to `Gamma-{u,v}`;
* every vertex of `Q=N_G(u)-{v}` lies outside `Gamma`; and
* `N_G(u)∩K=Q` for `K=G-Gamma`.

The identity

\[
 K=G-\Gamma=(G-\{u,v\})-(\Gamma-\{u,v\})
\]

is therefore correct.

The restriction of `c` to `K` uses at most the five nonzero colours.  If
`K` were four-colourable, four colours on `K`, a fifth colour on
`Gamma-{u}`, and a sixth colour on `u` would properly colour `G`.  In
particular, `uv` is proper because `v` receives the fifth colour.  This
proves `chi(K)=5` without assuming that all six colours occur in `c`.

## 2. Universal five-colour saturation

The proof correctly quantifies over an arbitrary proper five-colouring of
`K`.  If a colour is absent from `Q`, assigning it to `u` and assigning one
fresh sixth colour to `Gamma-{u}` is proper because:

* every neighbour of `u` in `K` belongs to `Q`;
* `Gamma-{u}` is independent;
* its sole possible neighbour of `u` is `v`; and
* `u` and `v` receive different colours.

Thus the conclusion is genuinely that **every** five-colouring of `K` uses
all five colours on `Q`; it is not merely saturation in the originally
chosen colouring.

## 3. Minor-model lifts

Every member of `Q` is adjacent to both `u` and `v`, and `uv` is an edge.
Consequently, if five disjoint connected branch sets each meet `Q`, the
singleton bags `{u}` and `{v}` are adjacent to all five and to each other.
It follows exactly that:

* a `Q`-rooted `K_5` model in `K` lifts to a `K_7` model in `G`; and
* a `Q`-rooted `K_5^-` model in `H=G-{u,v}` lifts to a `K_7^-` model in
  `G` (or to a `K_7` model if the nominally missing adjacency is present).

The first conclusion is stronger than needed under `K_7^-`-minor
exclusion, since a `K_7` contains `K_7^-` as a minor.  The branch sets in
`H` may contain vertices of `Gamma-{u,v}`; this causes no problem because
their intersections with `Q` alone supply the two apex adjacencies.

## 4. Five-connectivity, nonplanarity and external inputs

Deleting `u,v` from a seven-connected graph leaves a five-connected graph:
any separator of order at most four in `H` would, together with `u,v`, be a
separator of order at most six in `G`.

If `H` were four-colourable, two fresh colours on the adjacent vertices
`u,v` would six-colour `G`.  Hence `chi(H)>=5`; the Four-Colour Theorem then
implies that `H` is nonplanar.

The two external existence statements are used in their correct forms:

* He, Wang and Yu's Kelmans--Seymour theorem says that every five-connected
  nonplanar graph contains a subdivision of `K_5`;
* Theorem 1.1 of Girão, Illingworth, Mohar, Norin, Steiner, Tamitegama,
  Tan, Wood and Yip says that every graph without a dominating `K_5` model
  is four-colourable, so its contrapositive applies to `H`.

Both results are unrooted relative to `Q`.  The source correctly makes no
inference from a generic linkage into a `K_5` subdivision to five distinct
`Q`-rooted branch sets.

Primary sources checked:

* D. He, Y. Wang and X. Yu, [*The Kelmans--Seymour conjecture IV: A
  proof*](https://arxiv.org/abs/1612.07189), *Journal of Combinatorial
  Theory, Series B* **144** (2020), 309--358;
* A. Girão et al., [*The Dominating 4-Colour
  Theorem*](https://arxiv.org/abs/2605.10112), Theorem 1.1.

## 5. Universal five-terminal deficit

Subject to the application hypothesis `|Q|>=5`, any chosen five vertices of
`Q` are five distinct terminals in the five-connected (hence
three-connected) graph `H`.  The audited universal theorem therefore gives
a rooted

\[
                         F_5=K_1\vee P_4
\]

model.  The two singleton apex bags turn its guaranteed quotient into
`K_2\vee F_5`.  The edge count is exact:

\[
 |E(F_5)|=4+3=7,
 \qquad
 |E(K_5^-)|=9.
\]

Thus the *guaranteed* quotient is two internal bag adjacencies short of
`K_2\vee K_5^- = K_7^-`.  The source explicitly allows extra adjacencies in
the actual quotient, so it does not overstate this deficit.

## 6. Holroyd scope and trust boundary

For a five-chromatic graph, Holroyd calls a set colourful precisely when it
uses all five colours in every proper five-colouring.  His Strong Hadwiger
Conjecture would give a clique-minor whose five branch sets all meet that
set.  Thus applying its order-five case to `(K,Q)` would give exactly the
rooted `K_5` model needed for the apex lift.

This formulation is confirmed in A. Martinsson and R. Steiner,
[*Strengthening Hadwiger's conjecture for 4- and 5-chromatic
graphs*](https://arxiv.org/abs/2209.00594), which proves the first open case
`t=4`, not `t=5`.  The source therefore correctly treats the order-five
case as conjectural and uses it only to measure the strength of the missing
generic implication.

The exact proved endpoint is consequently:

* `K` is five-chromatic and `Q` is colourful in `K`;
* `H` is five-connected and nonplanar;
* unrooted `K_5` existence follows in `H`; but
* target exclusion forces every `K_5` model in `H` to have some branch set
  disjoint from `Q`.

The recorded double-saturation construction does not refute the live
dominated-common-neighbour statement: it lacks the host's
seven-connectivity and minor-criticality and has two different root sets
rather than one set adjacent to both apex vertices.  The proposed
dominated-common-neighbour rooted-model theorem remains unproved, as the
source states.

## Unresolved obligations

This audit does **not** certify any of the following:

1. the order-five case of Holroyd's conjecture;
2. existence of a `Q`-rooted `K_5^-` model in `H`;
3. a five-root allocation inside an arbitrary Kelmans--Seymour
   subdivision; or
4. conversion of the fixed exact model, second edge response, or actual
   response component into that rooted model.

Those are accurately recorded as the remaining route gap, not as proved
consequences.
