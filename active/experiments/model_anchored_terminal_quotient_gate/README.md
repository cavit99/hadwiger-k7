# A static quotient does not close the model-anchored response side

**Status:** deterministic bounded diagnostic and recorded route nonclosure.
This is not a theorem about the critical host, a counterexample to anchored
coordinate-response compression, or a counterexample to the `K_7^-`
six-colour conjecture.

The verifier is [`probe.py`](probe.py).

## 1. Question tested

Retain a spanning exact `K_7^vee` model

\[
                 P,B,C,R,U_2,U_3,U_4,
\]

where only `PB` and `PC` are absent.  The labelled proof of endpoint-support
capture can split the universal bag `R` into nonempty connected sets

\[
                         R=Y\mathbin{\dot\cup}R_0
\]

with nominated coordinate endpoints `p in Y` and `q in R_0`, both adjacent
to `P`, while `Y` is anticomplete to a named far branch set.  In the direct
capture proof that far branch set can be taken from the deficient twins
`B,C`.  Those are the two live-provenance rows.  The diagnostic also checks
the three other universal labels as broader hostile controls; it does not
claim that the current capture theorem supplies them.

The fixed-coordinate list-core theorem alone does not prove that the
complement of its critical core in `R` remains connected.  The concurrent
[model-anchored hull reduction](../../../results/hc7_k7minus_model_anchored_response_hull.md)
restores a connected split and iterates to a model-anchored stopping
configuration.  The experiment tests the static quotient of that stronger
configuration.  It does not encode whether the stopping side is itself
list-critical or contains appendages separated from the branch-set
complement by its critical core.

They do not.

## 2. Exact finite encoding

Contract the displayed connected sets to the eight named cells

\[
                       Y,R_0,P,B,C,U_2,U_3,U_4.
\]

The fixed contacts are:

* `Y` is adjacent to `R_0`;
* `B,C,U_2,U_3,U_4` form a clique in the branch-set quotient;
* `P` is adjacent to `U_2,U_3,U_4` and anticomplete to `B,C`;
* for each old neighbour of `R`, at least one of `Y,R_0` retains that
  contact; and
* because `p,q` are nominated `P`-neighbours on opposite sides, `P` meets
  both `Y` and `R_0`.

For a named far bag `D`, the profile additionally has `YD` absent and
`R_0D` present.  Thus there are `3^4=81` profiles for each choice of `D`.
The verifier checks `K_7^-`-minor exclusion exactly.  On eight vertices, a
seven-branch-set model uses either seven singleton cells or one adjacent
pair and six singleton cells, so this check is exhaustive.

### Coordinate partners

Name incident forest edges

\[
                           pp^*,\qquad qq^*.
\]

For distinct coordinate components, the quotient permits `p^*` in the
closed neighbourhood of the cell `Y` and `q^*` in the closed neighbourhood
of `R_0`.  Equal cell labels still permit two distinct actual partners
inside one branch set.  If `p,q` are the leaves of the sole possible
induced `P_3`, a common partner can occupy any cell in the intersection of
those two closed neighbourhoods.  If they are the two ends of one matching
edge, the fixed `Y-R_0` contact permits that placement as well.

These are only the consequences visible after branch-set contraction.
Componentwise inducedness constrains edges between the actual forest
vertices; it does not say which other quotient contacts have the same
witness.  The verifier therefore does not invent vertex-level nonedges
inside adjacent cells.

There is one further distinction.  Since `p in Y`, the singleton signature
on `pp^*` gives a proper exterior colouring of `G-Y`.  The singleton
signature on `qq^*` does so only when `q^* in Y`; otherwise the
monochromatic edge `qq^*` survives wholly outside the side.  The pair of
signatures is exterior-proper under the same vertex-cover condition.  The
verifier records that `q^*` may occupy `Y` in every surviving profile, but
does not turn this placement into an equality partition.

## 3. Exhaustive outcome

The exact counts are:

| named far bag | admissible profiles | `K_7^-`-minor-free profiles | distinct-partner cell pairs per survivor | common-partner cells per survivor |
|---|---:|---:|---:|---:|
| `B` | 81 | 51 | 24--48 | 3--6 |
| `C` | 81 | 51 | 24--48 | 3--6 |
| `U_2` | 81 | 48 | 24--42 | 3--5 |
| `U_3` | 81 | 48 | 24--42 | 3--5 |
| `U_4` | 81 | 48 | 24--42 | 3--5 |

Thus naming both nominated endpoints and both coordinate partners does not
remove the static survivors.

The direct retaining-core subcase is sharper still.  Require `R_0` to
retain all six old contacts and require `Y` to miss both deficient twins.
Only the three contacts `YU_2,YU_3,YU_4` remain optional.  All eight such
profiles are `K_7^-`-minor-free.

## 4. Maximally saturated survivor

There is a particularly sharp profile.  Let the only missing quotient
edges be

\[
                         YB,\quad YC,\quad PB,\quad PC.       \tag{4.1}
\]

Equivalently, the quotient is `K_8-K_{2,2}`, where the four deleted edges
join `\{Y,P\}` to `\{B,C\}`.  The set `R_0` retains every old contact,
while `Y` meets `P,U_2,U_3,U_4` and is anticomplete precisely to the two
deficient twins.  This is the most favourable contact profile produced by
the retaining-core case.

It has no `K_7^-` minor.  Seven singleton cells retain at least two of the
four missing edges.  If one edge is contracted, an endpoint outside
`\{Y,P\}` or `\{B,C\}` can repair the two missing contacts of at most one
vertex in those pairs; the other vertex still misses both vertices of the
opposite pair.  Contracting `YP` or `BC` also leaves two missing contacts.
Hence every seven-branch-set quotient has at least two absent adjacencies.

The coordinate labels do not disturb this survivor.  The possible cells
for `p^*` are

\[
                         Y,R_0,P,U_2,U_3,U_4,
\]

and every one of the eight cells is possible for `q^*`.  There are therefore
48 ordered cell placements for two distinct partners and six possible cells
for a common `P_3` partner.  Taking `p,q` as the ends of one coordinate edge
is also statically possible.

There is a sharper singleton realisation.  Take every cell to be one
vertex and nominate `Y-R_0` as the selected edge.  Then `R_0` is adjacent
to every neighbour of `Y` other than itself:

\[
                         N(Y)-\{R_0\}\subseteq N(R_0). \tag{4.2}
\]

Thus the selected edge has exactly the dominated-mate geometry left by the
singleton two-edge fork.  Both ends are already adjacent to `P`.  Moving
`Y` into the pole branch set and leaving `R_0` as the residual universal
bag preserves the exact model, but it does not increase the number of
coordinate endpoints in `P\cup N(P)`: the mate was visible before the
move.  Hence maximal endpoint visibility alone does not close the
dominated-edge residue.

This is an actual eight-vertex graph assertion, not an inference that one
vertex in a nonsingleton quotient cell dominates all neighbours represented
by adjacent cells.  Its scope remains static: `K_8-K_{2,2}` is
six-colourable, has minimum degree five, and does not carry the critical
host's missing-empty signature assertion or its seven-connectivity.  It
therefore does not refute a terminalisation theorem which spends those
global hypotheses.

If `Y` contains a second actual forest vertex, the saturated profile also
permits two distinct coordinate edges with `p^* in P` and `q^* in Y`.
Both singleton signatures, and their two-edge signature, then meet `Y` and
are legitimate exterior responses at the level of the vertex-cover
criterion.  If `Y` is a singleton, this placement is unavailable and the
only original forest responses are the incident ones; the quotient cannot
infer a second coordinate response merely from the endpoint `q`.

The quotient contains large cliques because its vertices are contracted
branch sets.  This does not contradict the absence of a literal `K_5` in
the critical host.  Likewise seven-connectivity and minimum degree do not
descend through arbitrary branch-set contraction.

## 5. Information deliberately not encoded

The `255` nonempty signatures of `G-F_8` are properties of **different
six-colourings of one uncontracted graph**.  A signature restricts to a
proper exterior colouring of `G-Y` only when `Y` meets every monochromatic
coordinate edge.  In particular, a singleton forest endpoint normally
carries only its one incident singleton signature.  No uncoloured contact
quotient can express the universal missing-empty-signature assertion, the
surviving boundary equality partitions or their Kempe components.
Attaching the names of eight forest edges to quotient cells does not encode
that information.

The quotient also omits:

* the fixed singleton-signature colouring at `pp^*`;
* vertex-minimal noncolourability of `Y` from the boundary lists induced by
  that colouring;
* multiplicities and actual vertices in `N_G(Y)`; and
* the internal paths which witness connectivity and redundant branch-set
  contacts after a transfer inside `R`.

Consequently the full punctured cube cannot legitimately be added as a
finite static constraint here.

## 6. Decisive nonclosure and smallest repair

The diagnostic excludes a contact-only completion of the anchored response
argument.  Even the saturated exact model, two separated nominated
endpoints, named coordinate partners and quotient-level target exclusion
leave a survivor.  In its singleton-cell realisation, the survivor also has
a dominated selected edge and both of its ends are already visible to the
pole.  Thus neither domination nor maximal endpoint visibility repairs the
static argument.

The smallest useful additional input is therefore **colour-sensitive and
internal to the split bag**.  For the fixed singleton response at `pp^*`,
one needs a theorem which either transfers a connected coloured part of
`R_0` into `Y` while retaining the foreign model contacts, or turns the
blocked transfer into a boundary of order seven or eight carrying the same
edge and exterior colouring (or into a partition extending through both
shores).  In the saturated survivor, a valid transfer making `Y` meet
either `B` or `C` immediately gives a `K_7^-` model; the quotient cannot say
whether such a Kempe-valid transfer exists.

Thus the next proof must couple one actual singleton-signature colouring to
the internal witnesses of the exact model.  More static endpoint or contact
labels cannot close the branch.

## 7. Reproduction

From the repository root run

```text
python3 active/experiments/model_anchored_terminal_quotient_gate/probe.py
```

The script uses only the Python standard library, asserts the full count
table, the saturated survivor and a positive target control obtained by
adding one deficient-twin contact, and prints a `GREEN` line.
