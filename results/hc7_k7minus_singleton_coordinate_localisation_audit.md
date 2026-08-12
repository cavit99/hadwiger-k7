# Separate internal audit: singleton coordinate localisation

**Verdict:** **GREEN.**  The vertex-cover criterion, localisation of the
eight-coordinate signatures, the singleton two-edge fork, all three
contraction chromaticities, the connectivity and density entrance, and the
dominated-edge residue are correct at the revision below.  The theorem is a
conditional reduction and does not terminalise the eight-coordinate branch.

This is a separate internal mathematical audit, not external peer review.

## Exact revision

The audited source is
[`hc7_k7minus_singleton_coordinate_localisation.md`](hc7_k7minus_singleton_coordinate_localisation.md),
with SHA-256

```text
90c1a84a934ca2848c35152b3a0d0b089da55f308fa829f2add24addbcba8749
```

The initially supplied draft was strengthened during the audit by adding
the final `K_5`-model contact criterion in the dominated-edge case.  One
overbroad intermediate wording was corrected to require each relevant
branch set to be disjoint from `u,v`.  The pinned revision above contains
that correction and requires no further mathematical change.

## 1. Exterior colourings and the forest cube

For a proper colouring of `G-D`, the only edges which can be improper after
restoring `D` are precisely the members of `M_D(c)`.  Hence `c|G-Y` is
proper exactly when `Y` meets every such edge.  If the resulting boundary
partition extended through the intact closed side, equality of the literal
boundary blocks permits a permutation of colour names and gluing to a
`q`-colouring of `G`.  This verifies Theorem 1.1.

In the forced eight-coordinate host, a signature-`J` colouring has exactly
the edges of `J` monochromatic after restoration.  The singleton `\{u\}`
is a vertex cover of `J` exactly when

\[
                         J\subseteq\delta_{F_8}(u).
\]

The stated forest types are `8K_2` and
`6K_2\mathbin{\dot\cup}P_3`, so a degree-one forest endpoint retains only
its incident singleton signature, while the centre of the induced path
retains its two singleton signatures and their union.  Adding the other six
forest edges to `G-F_8` gives the common graph `G-\{e,f\}` without reducing
connectivity or disturbing the model.  Exactness was already asserted in
the fully restored graph `G`, so it also survives.  Corollary 2.1 is correct.

## 2. Exact response square at a fresh incident edge

If the dominated-edge alternative fails, choose
`w in N_G(u)-\{v\}` with `vw` absent.  Then `v-u-w` is an induced path and

\[
                             Q=G-\{uv,uw\}
\]

is a proper minor.  It is six-colourable.  Were it five-colourable, assigning
the fresh sixth colour to `u` would restore both incident edges and
six-colour `G`; hence `chi(Q)=6`.

All three nonempty signatures are realised on this one graph.

* The fixed colouring of `G-uv` remains proper after also deleting `uw`;
  `uv` is monochromatic and `uw` is proper.
* A six-colouring of `G/uw` expands to `Q` with only `uw` monochromatic.
  The edge `uv` survives the contraction and therefore has differently
  coloured ends.
* A six-colouring after contracting the induced path expands with both
  selected edges monochromatic.  The missing edge `vw` is essential here.

An all-proper signature would colour `G`, so these are precisely the three
possible signatures.  Each monochromatic-edge set is covered by `\{u\}`;
Theorem 1.1 therefore puts all three rejected traces on `N_G(u)`.  The
original `uv` colouring is indeed the first corner.

## 3. Contraction chromaticities and the co-bagged model

Each of `G/uv`, `G/uw` and `G/\{uv,uw\}` is a proper minor and hence at most
six-chromatic.  A five-colouring after a single contraction expands to a
six-colouring of `G` by retaining the contracted colour at one endpoint and
giving the other endpoint a fresh sixth colour.  For the double contraction,
give `v,w` the contracted colour and `u` the fresh colour.  This is proper
because `vw` is absent.  Thus all three contraction graphs are exactly
six-chromatic.

Hadwiger's conjecture for parameter six supplies a `K_6` model in the
double contraction.  The graph is connected, so unused components may be
absorbed to make the model spanning.  The contracted path vertex then lies
in one branch set, and expanding it co-bags all of `v,u,w`, exactly as
claimed.

## 4. Connectivity, density and the exact near-clique model

Deleting one edge lowers vertex connectivity by at most one.  Indeed, a
separator of order at most `k-2` in `J-e`, together with a suitable endpoint
of the sole restoring edge, would give a separator of order at most `k-1`
in a `k`-connected graph `J`.  Applying this twice to the seven-connected
host gives

\[
                              \kappa(Q)\ge5.
\]

The critical-host density gives

\[
                  |E(Q)|=|E(G)|-2\ge4|V(G)|-2,
\]

which is stronger than the `4|V(Q)|-8` threshold.  Theorem 6 of Norin and
Totschnig states that every four-connected graph at that threshold has a
`K_7^vee` minor unless it is `K_{2,2,2,2}`.  The use here is valid because
`Q` is five-connected and has order at least 25, excluding the eight-vertex
exception.  This was checked against the primary source:
[Norin--Totschnig, Theorem 6](https://arxiv.org/html/2507.03244#S1.Thmtheorem6).

Connectedness permits the model to be made spanning.  In the target-free
host neither nominal missing pair can already be adjacent in `Q`, and
restoring `uv,uw` cannot create either adjacency: in either case the same
seven bags would have at most one missing pair and give a `K_7^-` minor in
`G`.  The spanning model is therefore exact after restoration.

## 5. The dominated-edge residue

If no suitable `w` exists, then `v` is adjacent to every member of
`N_G(u)-\{v\}`, giving at least `d_G(u)-1>=7` common neighbours.  A triangle
in that set, together with the adjacent universal vertices `u,v`, would be
a literal `K_5`, excluded by the critical-host theorem.  A `K_5^-` model in
the same set, together with the singleton branch sets `\{u\},\{v\}`, would
be a `K_7^-` model.  Both exclusions are therefore correct.

In the fixed colouring, `u,v` share one colour and every other neighbour of
`u` avoids it.  If any of the six colours were missing from `N_G(u)`, that
colour could be assigned to `u` in the proper colouring of `G-u`, contrary
to the choice of the host.  Hence the displayed common-neighbour graph uses
all five remaining colours, exactly as stated.

For the final model criterion, let `A_1,...,A_5` be pairwise adjacent
connected branch sets disjoint from `u,v`, each meeting the displayed
common-neighbour graph.  Every `A_i` is adjacent to both singleton branch
sets `\{u\},\{v\}`, and `uv` supplies their mutual adjacency.  These seven
sets form a `K_7` model.  This verifies the added sufficient condition.  It
does not assert that the five colour witnesses occupy five different model
bags; the source correctly identifies precisely that missing alignment.

## 6. Scope

No step identifies the spanning `K_6` model from the double contraction
with the exact `K_7^vee` model obtained from density, or with the original
eight-coordinate exact model.  The second edge in the first alternative is
also generally not a member of `F_8`.  The source records both limitations.
In the dominated alternative it likewise distinguishes five colour
witnesses from contacts with five pairwise adjacent model bags.

There are no unresolved assumptions in the proved statements.  The result
does not eliminate the common induced-path alternative, the dominated-edge
residue, the eight-coordinate branch, Conjecture 21 or `HC_7`.
