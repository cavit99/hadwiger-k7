# Cold audit: five-centre model-anchored visibility

**Verdict:** **GREEN.**  The centre-score transfer, maximality argument,
prescribed two-portal use of the exact `K_7^vee` dichotomy, and preservation
of the literal degree-eight centre through the fixed-coordinate core and
anchored hull are correct at the pinned revision.

This is a separate internal mathematical audit, not external peer review.
The proof is unbounded and computation-free.

## Exact revision

The checked source is
[`hc7_k7minus_five_centre_model_anchored_visibility.md`](hc7_k7minus_five_centre_model_anchored_visibility.md),
with SHA-256

```text
2558204c09967912132cc27d321bf863ecae1878d89e2c4595606917edae76a9
```

The direct dependencies were checked at the following revisions:

```text
d0d3aa3574d747a3164f29febff1fa8fd6f37b0899415cd97a515005c5de5f43  results/hc7_k7minus_five_centre_common_matching_reduction.md
4845f5375581971aca7397bbac0e3eb930dd2943c9dca71f6264a24e2fa31c6e  results/hc7_k7minus_exact_k7vee_separator_dichotomy.md
0473dc5826585e87935d3acf04c9c9579f8ecf52d92f076a9a44e7907c8b2da1  results/hc7_k7minus_fixed_coordinate_response_core_reduction.md
7cc1da7567f05e10bb7089c4b6dcd0706e9a0daa406063e7ba986d3d283c9512  results/hc7_k7minus_model_anchored_response_hull.md
```

Each dependency has a separate GREEN internal audit.  I also rechecked the
specific portions invoked here rather than relying only on those verdicts.

## 1. The literal centre response

For each `z in Z`, the punctured Boolean response theorem supplies a
six-colouring `c_z` of `H=G-M` with signature exactly `{e_z}`.  Restoring
the other four matching edges therefore gives a proper colouring of
`G-e_z`; after restoring `e_z`, that edge is the sole monochromatic edge.
Deleting any set containing `z` removes this only defect.

If a nonempty set `D` is anticomplete to such a connected set `Y`, then
`D` is disjoint from `N_G[Y]`.  Thus `N_G(Y)` is an actual separator.  An
extension through the closed `Y`-side inducing the same equality partition
on the boundary can be aligned with `c_z` by a permutation of the six
colour names and glued to `c_z|G-Y`.  This would six-colour `G`.  Lemma 1.1
and the lower bound from seven-connectivity are therefore exact.

## 2. The centre-score transfer

Let `z in U_i` be nonadjacent to `P`, and choose a `P`-neighbour `q in U_i`.
These vertices are distinct.  Extending a `q`--`z` path to a spanning tree
of `G[U_i]` and deleting its edge incident with `z` produces two nonempty
connected parts `A,W`, with

```text
q in A,  z in W,  and an edge between A and W.
```

If `W` misses a foreign branch set, then it is the asserted centre-bearing
side, while `A=U_i-W` is connected and the missed branch set is a genuine
far set.  The original edge `e_z` and colouring `c_z` apply by Lemma 1.1.

Otherwise `W` retains all five foreign adjacencies.  Replacing `P,U_i` by
`P union A,W` gives connected, disjoint branch sets with every required
adjacency.  If `A` meets `B` or `C`, the seven bags miss at most the
adjacency to the other twin and hence explicitly form a `K_7^-` model.  If
`A` meets neither twin, they remain a spanning exact `K_7^vee` model.

For the score

```text
|(P union N_G(P)) intersect Z|,
```

no previously counted centre is lost.  A centre in old `P` remains inside
the enlarged bag; one outside the enlarged bag which met old `P` still
meets the unchanged subset `P`; and one transferred with `A` is now inside
the enlarged bag.  The nominated `z` was not previously counted and is now
adjacent to `A` across the deleted tree edge.  The increase is therefore
strict.  The position of a noncentre matching mate `x_w` has no bearing on
this score.  This verifies Theorem 2.1, including its strict maximality
step.

## 3. Placement cases and prescribed two-centre capture

There are finitely many labelled spanning exact models, and the initial
model makes the maximisation class nonempty.  If a centre lies in `P`, the
twin `B` is anticomplete to its singleton; if it lies in `B` or `C`, the
bag `P` is anticomplete to its singleton.  Its boundary is exactly its
eight-vertex neighbourhood.  These are precisely the bounded alternatives
in Theorem 3.1; no connected-complement assertion is made there.

Otherwise all five centres occupy the four universal bags.  At a
centre-score maximum, Theorem 2.1 forces each of them to be adjacent to
`P`, unless the target or a centre-bearing side has already occurred.
Two centres `p,q` consequently lie in one universal bag and are both
literal `P`-portals.

The exact `K_7^vee` separator proof permits any two distinct `P`-portals in
that bag to be prescribed.  In its retaining-core case, the component
selected after avoiding one portal contains the other prescribed portal.
In its opposite-gate case, the two canonical gates contain `p` and `q`,
respectively.  A returned set missing a twin bag has that connected twin as
a named far set; if the relevant sets meet both twins, the audited transfer
constructs the forbidden minor.  Thus a separator alternative contains one
of the same literal centres, rather than merely an unlabelled endpoint.
This verifies the only nonformal use of the prescribed portals.

## 4. Preservation through the core and hull

Every returned side contains `z`, an end of `e_z`.  If `x_z` is outside
the side, the fixed-coordinate core theorem forces the unique contained
end `z` into the minimal list obstruction.  If `x_z` is also inside, it
forces both ends into that core.  An anchored hull contains its core.

After either case, the new side still contains `z`; moreover, a mate which
was outside cannot enter a smaller side, while a mate which was inside is
retained with `z`.  The same argument can therefore be iterated.  The edge,
colouring, containing branch set, connected branch-set complement and
named far bag are preserved exactly to the extent asserted by the hull
theorem.  Corollary 3.2 is correct.

## 5. Exact limitation and effect on the campaign

The source correctly declines to infer that `U_i-z` is connected.  The
larger returned side can have a connected complement in `U_i` while the
deletion of its contained centre disconnects that bag.  The same issue is
present for a centre lying in `P`, `B` or `C`: the singleton response is
valid and has order eight, but the complement of the singleton inside its
model bag is not asserted to be connected.

Consequently this theorem **localises but does not close** the
eight-coordinate branch.  It removes the endpoint-label ambiguity and
ensures that any terminal anchored side still contains a literal
degree-eight centre.  If the terminal side is the singleton `{z}`, the
existing degree-eight singleton analysis becomes applicable with the
original matching edge.  The theorem does not force that singleton,
establish the dominated-neighbourhood case, terminalise an order-eight
boundary, synchronise the two shores, or construct `K_7^-` in every case.

No material gap or unstated hypothesis was found in the proved reduction.
