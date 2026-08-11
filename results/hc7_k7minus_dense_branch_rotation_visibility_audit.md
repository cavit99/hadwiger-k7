# Internal audit: dense-branch rotation visibility

**Verdict:** GREEN for Lemma 1.1, Theorem 2.1, Corollary 2.2 and
Theorem 3.1.  The trace constructions retain their stated centre operation,
the two-support rerun of the exact `K_7^\vee` proof always captures a
selected support vertex in its separator outcome, and the exact-seven
fallback has the claimed labelled crossing-centre set.  This is a separate
internal mathematical audit, not external peer review.

## 1. Exact revision and checked dependencies

The audited source is
[`hc7_k7minus_dense_branch_rotation_visibility.md`](hc7_k7minus_dense_branch_rotation_visibility.md),
with SHA-256

```text
c81a3f7d656a4ef02a69ab88b311acc3601d9103aedbf6b6380c54cee350a3c3
```

The following promoted inputs were checked at these source revisions:

```text
4845f5375581971aca7397bbac0e3eb930dd2943c9dca71f6264a24e2fa31c6e  hc7_k7minus_exact_k7vee_separator_dichotomy.md
1041988a33b749bef5802dd21d3cd9419b5afc754735a20174bf5a13c0a56c96  hc7_k7minus_three_component_seven_cut_exclusion.md
fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd  hc7_k7minus_exceptional_neighbourhood_completion.md
d0d3aa3574d747a3164f29febff1fa8fd6f37b0899415cd97a515005c5de5f43  hc7_k7minus_five_centre_common_matching_reduction.md
```

Each has an adjacent GREEN internal audit.  The first two are the logical
inputs used in the proofs; the latter two supply the stated critical-host
provenance.  No finite computation or additional external theorem is used.

## 2. Boundary traces and the star constructions

Equality of the two boundary partitions is sufficient for gluing.  The
common blocks give a bijection between the colours used on the boundary;
it extends to a permutation of the six-colour palette.  After applying that
permutation to one shore, the colourings agree on the literal boundary.
Thus every exterior colouring produces a rejected partition exactly as
claimed.

For `y\in N_G(z)-K_z`, some independent triple `I` avoids `y`.  Contracting
the connected star on `z\cup I` and expanding a six-colouring gives one
colour on `I`.  All five vertices of `R=N_G(z)-I` avoid that colour.  They
must have five pairwise distinct colours: otherwise at most five colours
occur on `N_G(z)`, and a missing colour extends the colouring to `z`.
Assigning `z` the colour of `y` therefore makes `zy` the unique
monochromatic edge.  Deleting a set containing `y` but not `z` removes
that defect and preserves the exact exterior operation.

If the set contains `z`, restriction of a colouring of `G-z` gives the
second direct trace.  Hence absence of both constructions forces the set
to avoid `Z` and to meet each exceptional neighbourhood only inside
`K_z`.  When `|K_z|=3`, every independent triple equals `K_z`; if all three
vertices lay in the set, the same star-contraction colouring, with `z`
assigned their common colour after deletion, would give another direct
trace.  This proves the final bound of two.  The definition of `W` and the
claim that every set meeting it has a direct trace follow without an
unstated choice of colour names.

## 3. Capture of a selected support vertex

The proof of the exact spanning-`K_7^\vee` dichotomy was checked with the
two prescribed vertices `p,q\in N_G(P)\cap U_i` rather than with an
arbitrary duplicate pair.

In the avoidable retaining-core case, a core based at `p` and avoiding
`q` leaves a component `Y` containing `q`; interchanging the roles gives
the symmetric statement.  If `Y` meets `B` or `C`, the branch-set transfer
in the cited theorem gives the explicit `K_7^-` model.  If it misses both,
one of those connected twin bags is a far side of `N_G(Y)`, so the
neighbourhood is an actual separator.

In the unavoidable case, the canonical opposite gates contain `p` and
`q`, respectively.  A gate missing either twin again has an actual
open-neighbourhood separator.  If both gates meet both twins, their
nonempty disjoint monopoly sets lie among only three remaining universal
labels, and the cited proof gives a `K_7^-` model.  Consequently every
separator branch in the rerun contains at least one of the prescribed
vertices; no unmarked third set can be returned.

Membership of that vertex in `W` then supplies the claimed trace.  A
contained centre uses the centre-deletion construction.  A noncentre in
`W` lies in `N_G(z)-K_z` for some centre `z`; the star-edge construction
applies when `z` is outside `Y`, and centre deletion applies when `z` is
inside.  Seven-connectivity gives boundary order at least seven, and the
exact-order-seven fullness statement is precisely the final conclusion of
the cited dichotomy.

## 4. Corollary 2.2 counts

The spanning model and the anticompleteness of `P` to `B,C` give

\[
                         N_G(P)\subseteq U_1\cup\cdots\cup U_4.
\]

If no universal bag contains two vertices of `N_G(P)\cap W`, summing the
four unit bounds gives `|N_G(P)\cap W|\leq4`.  The nonempty connected bag
`B` is disjoint from `P\cup N_G(P)`, so `N_G(P)` is an actual separator.
Seven-connectivity gives `|N_G(P)|\geq7`, and therefore
`|N_G(P)-W|\geq3`.  No assumption that the four intersections are nonempty
or disjoint beyond the branch-set partition is hidden in this count.

## 5. Labelled exact-seven fallback

The identity `N_G(Y)=T` and connectivity of `Y` make `Y` a component of
`G-T`.  The audited seven-cut theorem gives exactly one other component
`D`, with both components full at `T`.

The set `D-Z` is nonempty.  If `D\subseteq Z`, connectedness and
independence of `Z` force `D` to be one centre.  That degree-eight vertex
would have all its neighbours in the seven-set `T`, a contradiction.
Thus deleting `Z` leaves a proper separation of `F` with boundary
`S=T-Z` and nonempty open shores `Y,D-Z`.

Every centre in `T\cap Z` has a neighbour in each component by fullness;
its neighbour in `D` lies in `D-Z` because `Z` is independent.  Conversely,
a centre outside `T` belongs to `D` and has no neighbour in the distinct
component `Y`.  Hence the crossing-centre set is exactly `T\cap Z`.
For a lift whose restriction to `F` is this separation, every vertex of
`S` and every crossing centre is compulsory, while each noncrossing centre
can be assigned to a compatible shore.  The literal separator `T` attains
the resulting order seven.

When all five centres lie in `T`, `S` has order two and is a two-cut of the
two-connected graph `F`.  Four centres give the stated labelled
order-three separation.  If `F` is three-connected, its proper separator
has order at least three, so `7-|T\cap Z|\geq3` and at most four centres
lie in `T`.  All three numerical conclusions are exact.

## 6. Trust boundary

No proof gap or hidden finite assumption was found.  The audit does not
promote any of the following stronger assertions:

- the five direct traces induce one common boundary partition;
- a returned separator has order seven, contains no centre, or is the
  neighbourhood of an exceptional vertex;
- `N_G(P)` necessarily contains five vertices of `W`, or two such vertices
  in one universal bag;
- the residue `|N_G(P)-W|\geq3` is impossible; or
- one rejected trace supplies an interior colouring, a compatible second
  operation, or a `K_7^-` model.

Accordingly the audited result is a visibility and labelled-fallback
reduction only.  It does not prove the `K_7^-` six-colour conjecture or
`HC_7`.
