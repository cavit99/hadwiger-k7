# Internal self-audit: five-centre model-anchored visibility

**Verdict:** **GREEN as a self-check.**  The centre-score transfer, the
maximality and pigeonhole argument, the prescribed two-centre capture and
the preservation of the centre through fixed-coordinate core and hull
reduction are correct at the pinned revision.

This audit was written by the same agent as the theorem.  It is not a cold
independent audit and is not external peer review.

## Exact revision

The checked source is
[`hc7_k7minus_five_centre_model_anchored_visibility.md`](hc7_k7minus_five_centre_model_anchored_visibility.md),
with SHA-256

```text
2558204c09967912132cc27d321bf863ecae1878d89e2c4595606917edae76a9
```

The proof is computation-free.  The direct dependencies checked at their
current revisions are

```text
d0d3aa3574d747a3164f29febff1fa8fd6f37b0899415cd97a515005c5de5f43  results/hc7_k7minus_five_centre_common_matching_reduction.md
4845f5375581971aca7397bbac0e3eb930dd2943c9dca71f6264a24e2fa31c6e  results/hc7_k7minus_exact_k7vee_separator_dichotomy.md
0473dc5826585e87935d3acf04c9c9579f8ecf52d92f076a9a44e7907c8b2da1  results/hc7_k7minus_fixed_coordinate_response_core_reduction.md
7cc1da7567f05e10bb7089c4b6dcd0706e9a0daa406063e7ba986d3d283c9512  results/hc7_k7minus_model_anchored_response_hull.md
```

Each dependency has a separate GREEN internal audit.

## 1. Direct centre operation

For each centre `z`, the common-matching theorem supplies a colouring of
`H=G-M` with singleton signature `{e_z}`.  Restoring the other four
matching edges leaves a proper colouring of `G-e_z`; after restoring
`e_z`, that edge is the sole monochromatic edge.  Any set containing `z`
therefore removes the only defect from its exterior.

If a nonempty set `D` is anticomplete to the selected connected side, it
lies outside the side and its open neighbourhood.  The neighbourhood is
an actual separator.  A boundary extension with the same equality
partition aligns by a permutation of the six colours and glues to a
six-colouring of `G`.  This checks Lemma 1.1.  No saturation or colouring-
name identification is being used implicitly.

## 2. Monotonicity of the centre score

Let a centre `z in U_i` be invisible to `P`.  The chosen tree edge on a
`P`-portal--`z` path divides `U_i` into connected nonempty sets `A,W`, with
the old `P`-portal in `A` and `z in W`.

If `W` loses a foreign adjacency, its corresponding foreign branch set is
literally anticomplete to `W`.  Hence `W` is the required proper anchored
side, contains the nominated centre, and has connected complement `A`.

Otherwise `W` retains all five foreign adjacencies.  Enlarging `P` by `A`
and replacing `U_i` by `W` preserves every required branch-set adjacency.
If `A` meets `B` or `C`, at most the other deficient pair remains absent,
giving an explicit `K_7^-` model.  If it meets neither, the new model is
still exact and spanning.

For the score

```text
|(P union N(P)) cap Z|,
```

no old centre is lost.  A centre formerly inside `P` stays there; a centre
outside the enlarged bag which was adjacent to old `P` remains adjacent to
that unchanged subset; and a centre in `A` is newly inside `P`.  The
nominated centre `z` was not formerly counted and becomes adjacent through
the tree edge.  Thus the increase is strict.  A noncentre matching endpoint
inside `A` neither changes nor obstructs this argument.  This is precisely
the point at which the centre score is stronger than reusing the all-
endpoint proof verbatim.

## 3. Maximality and pigeonhole

There are finitely many spanning labelled exact models, so a maximum centre
score exists.  A centre in `P` has the named far bag `B`; a centre in `B`
or `C` has the named far bag `P`.  Its singleton response boundary is its
eight-vertex neighbourhood.  Thus those placements give the exact bounded
alternative in Theorem 3.1.

If no centre occupies `P,B,C`, all five lie in the four universal bags.
At a maximum, Theorem 2.1 forces every centre to be adjacent to `P`, unless
the target or an anchored centre side has already occurred.  Pigeonhole
then gives two distinct literal centres in one universal bag, both selected
as `P`-portals.

The prescribed-portal rerun of the exact near-clique dichotomy was checked
at those same two vertices.  In the retaining-core case, the returned
component contains the selected portal avoided by the core.  In the
opposite-gate case, the gates contain the two selected portals separately.
A set missing a twin bag has that bag as a named far side.  If the relevant
sets meet both twins, the audited transfer constructs the target minor.
Consequently the separator outcome cannot replace the two centres by an
unlabelled third endpoint: it contains one of the nominated centres.

## 4. Persistence through the existing descent

The response side contains the centre `z`, an endpoint of the fixed edge
`e_z`.  If the mate `x_z` is outside the side, the fixed-coordinate core
theorem forces the unique contained endpoint `z` into every minimal list
obstruction.  If the mate is also inside, it forces both endpoints.  Every
anchored hull contains that core.  Iteration therefore preserves `z`, the
same edge, the same colouring, the same containing bag and the same named
far bag.

This verifies Corollary 3.2 and answers the label-preservation question
affirmatively.

## 5. Trust boundary

The theorem does not assert that deleting the centre leaves its universal
branch bag connected.  Thus the exact order-eight singleton response cannot
automatically replace the larger anchored side while preserving the same
branch-set split.  It also does not show that a later boundary has order
eight, that two shore partitions coincide, or that the target minor is
forced in every case.

No material gap was found in the proved reduction.  Before promotion, the
theorem should receive a cold independent audit.
