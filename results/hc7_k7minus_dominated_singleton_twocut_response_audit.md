# Separate internal audit: dominated-singleton two-cut response

**Verdict:** **GREEN.**  The common-neighbour two-cut, the two opposite
incident-edge responses, the exclusive switch with the original coordinate,
the model-persistent edge count in Theorem 4.2, and the high-degree alignment
in Corollary 4.3 are correct at the pinned revision.  This is a conditional
reduction and does not terminalise the dominated-singleton alternative or the
eight-coordinate branch.

This is a separate internal mathematical audit, not external peer review.

## Exact revision

The audited source is
[`hc7_k7minus_dominated_singleton_twocut_response.md`](hc7_k7minus_dominated_singleton_twocut_response.md),
with SHA-256

```text
204365dd5d68e9b80d84b346fe0b796cd3bb817ac10f34c718de884b882b19d0
```

The mathematical draft initially checked had SHA-256
`937ccaee593618699b36460f5ef4c800fefbae1be7a27daf3ae84edca1b1deec`.
The only subsequent source change was the status link to this audit.  No
mathematical correction was required.

## 1. Imported neighbourhood structure

The prerequisite singleton-coordinate theorem is itself pinned and audited
at SHA-256
`90c1a84a934ca2848c35152b3a0d0b089da55f308fa829f2add24addbcba8749`.
In its dominated alternative it proves, for

\[
                   Q=G[N_G(u)-\{v\}],
\]

that `|V(Q)|>=7`, that `Q` is triangle-free, and that `Q` has no
`K_5^-` minor.  These are exactly the imported facts used in the new note.

## 2. Wood--Woodall and the actual separators

Lemma 4.2.1 of R. G. Wood and D. R. Woodall,
[*Defective Choosability of Graphs without Small
Minors*](https://doi.org/10.37236/181), states exactly that a
three-connected `(K_5-e)`-minor-free graph is a wheel, the triangular prism,
or `K_{3,3}`.  This was checked against the primary published paper.  Every
wheel and the triangular prism contains a triangle, while `K_{3,3}` has six
vertices.  Thus the lemma applies directly to `Q` and proves that `Q` is not
three-connected.  Since `|V(Q)|>=7`, there is consequently a set
`S subseteq V(Q)` of order at most two for which `Q-S` has at least two
components.

Put `R=G-\{u,v\}` and take distinct components `A,B` of `Q-S`.  Removing two
vertices from the seven-connected graph leaves `R` five-connected.
There are no `A-B` edges, and no vertex of `B` lies in `N_R(A)`, so
`N_R(A)` is a genuine separator in `R` and has order at least five.  Every
neighbour of `A` in `Q` lies in `S`; moreover

\[
              V(R)-V(Q)=V(G-N_G[u]).
\]

This yields at least `5-|S|` exterior neighbours.  The definition of `Q`
and domination by `v` make both `u` and `v` adjacent to every vertex of
`A`, and these are the only vertices absent from `R`.  Hence

\[
              N_G(A)=N_R(A)\mathbin{\dot\cup}\{u,v\},
              \qquad |N_G(A)|\ge7.
\]

The component `B` is disjoint from this boundary and remains on the far
side.  The symmetric assertions for `B` follow identically.  Theorem 2.1
therefore establishes actual separators, not merely neighbourhood-size
bounds.

## 3. Exact two-edge response languages

For `x in A`, `y in B`, the vertices `x,y` are nonadjacent, so `x-u-y` is
an induced path.  The graph

\[
                         L=G-\{ux,uy\}
\]

is a proper minor and is at most six-colourable.  A five-colouring could be
extended after assigning a fresh sixth colour to `u`, so `chi(L)=6`.

A colouring of `G-ux` supplies signature `\{ux\}`, and a colouring of
`G-uy` supplies `\{uy\}`: the deleted edge must be monochromatic, while
the other selected edge is present and therefore proper.  Contracting the
induced path and expanding its contracted vertex supplies
`\{ux,uy\}`.  The empty signature would colour `G`.  Thus these are exactly
the three nonempty signatures claimed in Theorem 3.1.

The singleton `\{u\}` meets every monochromatic deleted edge.  The side
`A` meets the sole monochromatic edge in the `\{ux\}` colouring, and `B`
does the same for the `\{uy\}` colouring.  The corresponding exterior
restrictions are proper.  Extension of any induced boundary partition
through the intact closed side would align by a permutation of colour names
and glue to a six-colouring of `G`.  All stated traces are therefore
rejected on the actual boundaries from Theorem 2.1.

For Proposition 4.1, domination supplies the present edge `vx`.  In
`G-\{uv,ux\}`, the empty signature again colours `G`, while simultaneous
equality on both deleted edges would give `c(v)=c(x)`, contrary to `vx`.
Colourings of the two single-edge deletions realise the two singleton
signatures.  The asserted exclusive language `\{uv\},\{ux\}` is exact.

## 4. The essential-edge count in Theorem 4.2

Spanningness of the fixed labelled model is used correctly: every
`x in V(Q)` belongs either to the branch set `R` containing `u` or to one
of the six foreign branch sets.

If `x in R-u`, the hypothesis that `R-u` is connected means that deleting
`ux` disconnects `R` only when it is the unique edge from `u` to `R-u`.
There is at most one such internal essential edge (and none when
`R=\{u\}`).

If `x` lies in a foreign branch set `J`, deleting `ux` can affect the fixed
model only when the labels `R,J` require adjacency and `ux` is their sole
inter-branch-set edge.  For each required foreign label there is at most one
such essential edge.  No connectivity of a foreign branch set is affected,
because `u` belongs to `R`.

Every label of `K_7^vee` has degree at most six.  When the label of `R` has
degree at most five, its required foreign contacts and the possible internal
edge total at most six.  When its degree is six, all six foreign labels are
required, but the named foreign branch set `D` is anticomplete to `u`.
No candidate edge `ux` enters `D`, leaving at most five essential foreign
edges and again at most one internal edge.  Thus at most six candidates are
essential in all cases.

Since `|V(Q)|>=7`, at least one edge `ux` is nonessential.  Deleting it
preserves connectivity of every branch set and every required labelled
adjacency.  Edge deletion cannot introduce either nominally absent
adjacency, so the fixed model remains exact.  The original colouring of
`G-uv` remains proper after deleting `ux` and gives the `\{uv\}` corner;
Proposition 4.1 supplies the exclusive `\{uv\},\{ux\}` response pair on
the same graph.  Theorem 4.2 is therefore valid with exactly the model
persistence claimed.

## 5. Corollary 4.3

The equality

\[
                       |V(Q)|=d_G(u)-1
\]

is immediate from the definition of `Q`.  If `d_G(u)>=10`, there are at
least nine candidate edges and, by Theorem 4.2, at least three are
nonessential.  A set `S` of order at most two cannot contain all three, so a
nonessential endpoint `x` may be selected in a component `A` of `Q-S`.

The common deletion retains the same labelled exact model.  A colouring of
`G-ux`, restricted further after deleting `uv`, has only `ux`
monochromatic among the two selected edges.  Since `x in A`, its restriction
to `G-A` is proper and gives the rejected trace on the actual boundary
`N_G(A)`, whose order is at least seven.  This proves the corollary.

## 6. Scope

The argument does not bound either returned boundary from above and does not
produce two opposite component edges which preserve one common model.  The
source records that the remaining requirement is a two-sided
model-persistent choice theorem.  There are no unresolved assumptions in
the proved statements, but they do not eliminate the dominated-singleton
alternative, the eight-coordinate branch, Conjecture 21 or `HC_7`.
