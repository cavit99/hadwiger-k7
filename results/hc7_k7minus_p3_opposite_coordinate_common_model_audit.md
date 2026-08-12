# Internal audit: induced-path opposite-coordinate common model

**Verdict:** GREEN for Theorems 2.1, 3.1, and 4.1, Proposition 3.2,
Corollaries 4.2--4.3, Theorem 4.4, and the stated trust boundary.  This is a
separate internal mathematical audit, not external peer review.

## 1. Exact revision and inputs

The audited source is
[`hc7_k7minus_p3_opposite_coordinate_common_model.md`](hc7_k7minus_p3_opposite_coordinate_common_model.md),
with SHA-256

```text
3a2ded6ee2bbbe1e9735dd43f30bb7b0dcb193395ffc69fc64056ab7964a1cf7
```

The promoted source differs from the initially audited revision
`9260255fa82f5596e1399ba7bd39692d5ae432a03787f7f88b81bedd3b5e5de5`
only in its status header.  Its mathematical content is unchanged.

The checked hypotheses are exactly (1.1)--(1.5).  The source uses the
audited six-coordinate induced-forest reduction at revision

```text
cc2b56362d52a3ef23559a4a0e5cbf5eded5abbe7d54b57e73f66f74f1dd3405
```

for the componentwise-induced forest, the two seven-connected restorations,
and the placement of every order-six cut of `X`.  It also uses the established
case `HC_6` and Norin--Totschnig, Theorem 6, under the same density and order
hypotheses as that audited reduction.

Because `x-r-y` is induced and is a component of the forest disjoint from
`M_0`, neither `ux` nor `uy` is a forest edge.  Either edge would join the two
components of `X-S`, so neither lies in `X`.  Hence the asserted independence
of `\{u,x,y\}` is valid.

## 2. The two pair hosts

For each `z in \{x,y\}`, the graph `J_z` contains the seven-connected graph
`X+rz'` as a spanning subgraph.  Its seven-connectivity follows immediately.
A hypothetical five-colouring can be repaired after restoring `e` and `rz`
by assigning one new colour to the independent pair `\{u,z\}`.  Thus `J_z`
is exactly six-chromatic.

Contracting each nonempty subset of the vertex-disjoint pair `\{e,rz\}`
realises the three nonempty equality signatures.  A colouring with neither
pair monochromatic would extend to `G`, so no fourth signature occurs.

The same fresh-colour repair excludes a five-colouring of `Q_z=G/e/rz`.
Applying `HC_6`, absorbing unused vertices into a connected minor model, and
then expanding the contractions gives a spanning `K_6` model co-bagging both
specified endpoint pairs.

Finally, `J_z` is four-connected, has at least `4|V(J_z)|-2` edges, and has
order at least twenty-five.  The cited Norin--Totschnig theorem therefore
gives a spanning `K_7^\vee` model.  If either nominally absent branch-set
adjacency were introduced by restoring a deleted edge, the same bags would
give a `K_7^-` model.  Target exclusion consequently makes the lifted model
exact.

## 3. The common contraction model and its split

The graph `H_e` contains the six-connected graph `X` as a spanning subgraph,
and its two one-edge restorations are precisely `J_y` and `J_x`.  Its exact
six-chromaticity follows from the fresh-colour repair on the independent set
`\{u,x,y\}`.

The three deleted edges induce `K_2 dot-union P_3`.  Contracting any nonempty
subset therefore collapses neither an unselected forest edge nor an edge of
`H_e`.  Expansion realises all seven nonempty equality signatures, while the
empty signature would six-colour `G`.  The analogous repair proves that
`Q_e=G/e/rx/ry` is exactly six-chromatic.  Its spanning `K_6` model lifts to
one model in which `u,v` are co-bagged and the connected path `x-r-y` lies in
one bag.

For Proposition 3.2, every forest in a connected graph extends to a spanning
tree.  A spanning tree of the path-containing bag may therefore be chosen to
contain `rx` and `ry`.  Removing these two edges gives the three required
nonempty connected pieces.  Four foreign bags adjacent to all three pieces,
together with the three pieces, form seven branch sets with at most the
`B_xB_y` adjacency absent.  This is an explicit `K_7^-` minor model.  The
argument remains valid if the bag co-bagging `u,v` is the path bag or one of
the five foreign bags.

## 4. Six-cuts and returned responses

Let `R` be a six-cut of `H_e`.  Each of the single-edge restorations
`H_e+rx` and `H_e+ry` is seven-connected.  A single added edge can reconnect
`H_e-R` only when there are exactly two components and its two ends lie in
different components.  Since the two restoration edges share `r`, their
placement is necessarily `r in A` and `x,y in B`, with none of these vertices
in `R`.

If `A=\{r\}`, six-connectivity gives `N_{H_e}(r)=R`; restoring the only two
deleted edges incident with `r` gives (4.2).  Otherwise, moving `r` to the
boundary removes both path edges from the open-shore interface.  If `e` also
crosses, moving its `B`-end to the boundary removes the last possible
cross-edge, and the residual `B`-side remains nonempty because it contains
the two distinct leaves not incident with `e`.  The displayed order-seven
and order-eight separations are therefore actual separations of `G`.

For any connected open component `K`, its exact neighbourhood `N_G(K)` is a
subset of the displayed separator.  Seven-connectivity gives
`|N_G(K)|>=7`, so its order is seven or eight.  Deleting an edge from `K` to
its neighbourhood and restricting a six-colouring of that proper minor gives
the claimed colouring response on `N_G(K)`.  The source correctly does not
identify this response boundary with the whole displayed separator.

Corollary 4.2 is valid under its deliberately strong hypothesis: it excludes
every order-seven or order-eight proper-minor response, including fresh and
unanchored ones.  The singleton case also yields a proper order-eight
separation because `|V(G)|>=25`.  Thus every possible six-cut is excluded and
`H_e` is seven-connected.  This conclusion is asserted separately for each
chosen crossing edge `e`.

In Corollary 4.3, when `e` is the unique member of `M_0` crossing the original
two shores, restoring `M_0-\{e\}` joins neither shore to the other.  Hence the
same six-set and the same two components survive in `H_e`, and all three
deleted coordinates cross them as stated.

## 5. The two geometric linkage families

Completing `S` to a clique in either closed shore gives a six-connected
torso.  Indeed, after deleting at most five vertices, all remaining vertices
of the completed clique lie together; any component outside it would have a
neighbourhood of order at most five in `H_e` and would be separated from the
opposite shore, contradicting six-connectivity.

The Fan Lemma then gives an `r`--`S` fan in the first torso and separate
`x`--`S` and `y`--`S` fans in the second.  Truncating at first boundary visits
and matching equal boundary ends proves the two six-path families.  Within
each family the paths share their nominated endpoints and no other vertices;
the two families are not claimed to be mutually disjoint.

For a connected subgraph `P` containing `x,y`, applying the Fan Lemma from a
vertex of `P`, truncating at the boundary, and then deleting each initial
segment through `P` up to its last visit produces six `P`--`S` paths disjoint
outside `P`.  Concatenation with the fixed first-shore fan gives the asserted
`r`--`P` paths.  These conclusions are geometric only: no bichromatic,
proper-minor-response, or branch-bag labels are preserved.

## 6. Exact unresolved scope

No proof gap was found in the displayed proved statements, subject to their
explicit hypotheses and the audited upstream inputs.  The note nevertheless
does **not** prove any of the following:

* that four foreign `K_6` bags meet all three pieces of the split path bag;
* that the equality-signature cube determines branch-set labels;
* that the two linkage families form a simultaneous twelve-path system or
  are mutually disjoint away from their separately named endpoints;
* that the geometric linkages retain Kempe colours or proper-minor response
  provenance;
* that a response returned by Theorem 4.1 inherits a selected coordinate or
  model label; or
* that the induced-path case, the six-coordinate forest reduction, or the
  `K_7^-` six-colour conjecture is closed.

The first unsupported inference remains precisely the triple-contact
allocation required by Proposition 3.2.  The proposed triple-split exchange
statement is a conjectural target, not a proved consequence of the present
note.  No finite enumeration is used.
