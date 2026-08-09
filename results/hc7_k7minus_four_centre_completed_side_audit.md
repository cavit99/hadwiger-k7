# Internal audit: four-connectivity of the completed exact-cut side

Audited file:
`results/hc7_k7minus_four_centre_completed_side.md`.

Audited mathematical revision SHA-256:

```text
e49006f5adce10a1ed103bbb434f072bcd8d930377b363d869071f005975ff9f
```

Promoted source SHA-256:

```text
ae424dc24a95ab8afe9b6ea93dd850b727dcd4bf8f00ee72a8fd11eaf312e846
```

Relative to the audited mathematical revision, the promoted source replaces
`pending` in the opening status with a link to this GREEN audit, renames the
Section 4 heading as a rooted-minor criterion, and expands the final vague
reference to augmentation into the exact alternatives: the prescribed
rooted `K_6^-` minor or trace-preserving descent.  These changes affect only
status and terminology.  No hypothesis, conclusion or proof step changed.

**Verdict:** **GREEN** for both revisions above.

This is a separate internal mathematical audit, not external peer review.
The three stated results were reconstructed from the definitions and the
audited dependencies pinned below.  No minor model in the auxiliary
completed graph is transferred to the original graph.

## Four-connectivity of the completed side

The minimum trace-admissible component `C` has at least two vertices:
if it were a singleton, its neighbourhood would be the seven-vertex cut,
contrary to `delta(G)>=8`.  Hence
`F=H[C union T]+binom(T,2)` has at least five vertices.

Suppose that `F-Z` is disconnected for `|Z|<=3`.  The case `T subseteq Z`
is impossible because it forces `Z=T` and leaves the connected graph
`H[C]`.  Otherwise `T-Z` is a nonempty clique and therefore lies in one
component of `F-Z`.  Any other component `X` lies in `C`.  It is a proper
subset of `C`: if `Z` meets `C`, a vertex of `C` has been deleted; if
`Z subseteq T`, a surviving boundary vertex has a neighbour in the
undeleted set `C` and puts a vertex of `C` in the component containing
`T-Z`.

Every actual edge of `G` from `X` to another vertex of `C union T` is also
an edge of `F`.  Since `X` is a component of `F-Z`, no such edge can avoid
`Z`.  The components `C,D` are anticomplete, so

```text
N_G(X) subseteq U union Z.
```

The nonempty set `D` lies outside `X union N_G(X)`.  Thus `N_G(X)` is a
vertex cut.  Seven-connectivity, `|U|=4` and `|Z|<=3` force

```text
|Z|=3  and  N_G(X)=U dotunion Z.
```

The two-component normal form then makes `X` one component of
`G-(U union Z)` and puts the intact connected set `D`, including `x_j`, in
the other.  Seven-connectivity makes both components adjacent to every
boundary vertex.  Since `Z subseteq C union T`, the new selected closed
side `X union U union Z` is contained in the old one
`C union U union T`.  The accepted colouring restricts, the same colour
can be assigned to `r`, all nominated terminals still avoid `X`, and the
named bichromatic component is unchanged in the fixed coloured graph.
This is a trace-admissible exact cut with a smaller selected component,
contradicting minimality.  Theorem 2.1 follows.

## Rooted-connectivity consequences

Apply the closed-side rooted-connectivity lemma with

```text
A=C,  S=U dotunion T,  R=D.
```

All of its hypotheses hold: `|S|=7`, both outer sets are nonempty, and
there is no `C-D` edge.  It gives internal `|Q|`-connectivity of
`(G[C union Q],Q)` for every nonempty `Q subseteq S`.

For `Q=U`, the rooted graph has at least `|C|+4>=6` vertices.  This checks
the order hypothesis in Jorgensen's rooted-diamond theorem, in the form
quoted as Norin and Totschnig, Lemma 10.  Internal four-connectivity then
gives the claimed `U`-rooted `K_4^-` model in the original graph
`G[C union U]`.  Taking `Q=U union P` for any two-set `P subseteq T`
gives internal six-connectivity of `(L_P,U union P)`.  Corollary 3.1 is
therefore exactly the cited closed-side lemma plus the rooted-diamond
consequence; it does not use an edge added in `F`.

## The six-terminal model

Let `B_q`, `q in U union P`, be the branch sets of a rooted `K_6^-` model
in `L_P`.  The connected set `D` is disjoint from `L_P`.  Since
`N_G(D)=U dotunion T`, it has an edge to every literal root `q`, and hence
is adjacent to every `B_q`.  The first six branch sets have at most one
missing adjacency.  Adding `D` as a seventh branch set leaves at most that
same missing pair and gives a `K_7^-` minor model.  Extra adjacencies do not
matter.  Proposition 4.1 is correct.

## Auxiliary edges and the remaining question

The edges in `binom(T,2)-E(H)` are virtual completion edges.  They are used
only to make `T-Z` a clique in the proof of Theorem 2.1.  The neighbourhood
argument remains in the original graph because the added edges have both
ends in `T`, whereas the separated component `X` lies in `C`.  The rooted
`K_4^-` model in Corollary 3.1 lies in `G[C union U]`, and the rooted
`K_6^-` model in Proposition 4.1 is explicitly assumed in the original
subgraph `L_P`.  Thus the note correctly warns that an arbitrary minor
model in `F` need not lift to `G`, and it never performs such a lift.

In the generalized-wheel branch, the audited canonical-leaf theorem gives
an actual edge `ab in E(H[T])`; this edge is not virtual.  With
`P={a,b}`, Corollary 3.1 and Proposition 4.1 reduce the unresolved branch
to the displayed question: a prescribed rooted `K_6^-` minor or a strict
trace-preserving separation.  The proposed separation outcome would indeed
contradict trace minimality.  If its
nonempty open side is `X subsetneq C` and its separator is a three-set `Z`,
then `N_G(X) subseteq U union Z`.  Seven-connectivity forces equality, the
two-component theorem makes the lifted cut exact, equality places
`Z subseteq C union T`, and the old colouring restricts to the smaller
closed side.  The fixed terminal `x_j in D` remains in the opposite
component.  Hence the resulting cut is trace-admissible.

The note poses this dichotomy; it does not prove it.  The linked finite
barrier is used only to show that internal six-connectivity, the edge `ab`
and a rooted `K_4^-` model are insufficient by themselves.  It does not
show that every suggested additional hypothesis is individually necessary.
The final sentence is therefore read as the specification of the intended
critical-host route, not as a minimality theorem for its hypotheses.

## Pinned dependencies

The local inputs used above are present at separately audited revisions:

```text
trace-preserving four-centre descent
cbbefe62836e889f44bae6e41ac52ac0ffe54e05dbe86e2fc200c8f9f2d918ab

four-centre rooted-web and exact-cut lattice
e7fcf00c9bdbd2fcbab78bb13d4244a659f4f7db0ae45a97cfbd9a8d599a0ee3

two-component normal form for seven-vertex cuts
1041988a33b749bef5802dd21d3cd9419b5afc754735a20174bf5a13c0a56c96

closed-side rooted connectivity
ba6dbfe1ca9e89041b1a77174844c24598984cbe76349a55c41f15b2e997cc03

generalized-wheel leaf descent
c04236752495ec7ff6e57b54cc498423be1b621c5ba3547739cec72b045db176
```

Jorgensen's rooted `K_4^-` theorem is used only in the form already checked
by the closed-side audit: an internally four-connected four-root pair on at
least six vertices has a rooted `K_4^-` model.  No unresolved inference was
found within the source's stated scope.  The note does not prove the
six-terminal dichotomy, eliminate the exact-cut outcome, prove the
`K_7^-` six-colour conjecture, or settle Hadwiger's conjecture for `t=7`.
