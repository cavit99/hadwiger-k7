# Audit: sparse three-component five-cut elimination

**Verdict:** GREEN for the theorem as stated.

**Audited source:**
`active/hc7_k7minus_e5_three_component_sparse_elimination.md`

**SHA-256:**
`176910c63cfdd115ed0b1212b0588cd65e1892ef534e5eb7c3524a2b2b3badfd`

This is an internal mathematical audit, not external peer review.  The
source eliminates every three-component five-cut row at exact `E5` density
for which all three lobe excesses are at most three.  In the remaining
four-edge star boundary it first eliminates every row having two lobes of
excess at least three, then uses the full rooted-`K_4` obstruction
classification to eliminate the remaining concentrated row.  It does not
eliminate every high-excess row over another sparse boundary, prove `(E5)`, prove the
seven-connected `4n-2` theorem, or settle Conjecture 21.

## 1. Pinned internal inputs

The dense five-cut theorem, including fifth-root augmentation and the
triangle-free three-component boundary, was checked at

```text
81306114489449f1bd2d8521c4aefc216411f81bf6721c7763412d4a7a87c6c0.
```

The separate theorem reducing a minimum `E5` enemy to exact density was
checked at

```text
71a69c7214469105422e87993be50e7cb89730605a17f7cdf448057b1702078f.
```

The external rooted inputs are Norin--Totschnig Lemmas 9 and 12.  Their
forms used here are, respectively,

```text
internally four-connected and no Z-rooted K_4
    => e(H)<=3|H|-7,

internally four-connected and e(H)>=4|H|-9
    => a Z-rooted K^*_{4,2} model.
```

## 2. Exact accounting and the lobe lemmas

For a lobe `L`, omitted boundary vertex `t`, root set `Z=S-{t}`, and
`p(t)=|E_G({t},L)|`, completing only `Z` gives

```text
e(G[L union Z]+K_Z)=4|L|+delta-p(t)+6,
e(G[L union S]+K_Z)=4|L|+delta+6+d_J(t).
```

These are the two identities in Lemma 1.  If `p(t)<=delta-1`, the first
meets the rooted six-bag threshold.  Otherwise `p(t)>=delta`; under
`delta+d_J(t)>=5`, the retained vertex `t` has augmented degree at least
five, excluding the only new singleton open side.  Every other rooted
separation of order at most three extends, after adding `t` to the
separator when necessary, to an internal separation of the original
five-rooted shore of order at most four.

The virtual edges completing `Z` join different nominated root bags.
They can be deleted because a `K^*_{4,2}` model requires only
root--helper and helper--helper adjacencies.  Fifth-root augmentation then
places `t` in a helper in the original internally five-connected shore.

For the avoidant rooted `K_4`, omission of `t` gives

```text
e(G[L union Z])
 =4|L|+delta-p(t)+|E(J-t)|
 >=3|L|+delta+|E(J-t)|.
```

Thus `delta+|E(J-t)|>=6` exceeds the no-rooted-`K_4` bound by one.  The
model is genuinely contained in `G[L union Z]` and hence avoids `t`.

## 3. Root-overlap-free composition

Lemma 2 uses three distinct lobes.  The rooted `K_4` model in the first
lobe avoids `t`; the rooted six-bag model in the second has `t` in one
helper; the third lobe is retained whole.  Merging corresponding root bags
is legitimate because the two shore models meet only at their four literal
roots.  The retained lobe contacts all four merged roots and the helper
containing `t`, and may miss only the other helper.  The seven displayed
sets are therefore disjoint connected branch sets with at most one missing
adjacency.

## 4. Numerical rows and boundary classification

At exact density,

```text
delta_1+delta_2+delta_3=13-|E(J)|.
```

The boundary is triangle-free, so it has at most six edges.  Under
`delta_i<=3`, the complete list is:

```text
|E(J)|=6:  {3,3,1} or {3,2,2};
|E(J)|=5:  {3,3,2};
|E(J)|=4:  {3,3,3}.
```

For six edges, Mantel equality gives `K_{2,3}` and a degree-three omitted
vertex supplies the two rooted models.  For five edges, the only
triangle-free graphs are `C_5` and a four-cycle with a pendant edge; a
degree-two vertex again supplies them.  All uses involve distinct lobes,
so the retained seventh branch set is available.

In the four-edge row, Lemma 1 and absence of the terminal composition give

```text
d_J(s)<=1 => p_i(s)>=3,
d_J(s)>=2 => p_i(s)>=|L_i|+2-d_J(s).
```

Connectedness gives

```text
sum_{s in S}p_i(s)<=3|L_i|+4.
```

Substitution excludes `P_5` and `C_4` plus an isolated vertex, leaving
only `K_{1,4}` and the subdivided claw.  The arithmetic in every degree
row is exact.

## 5. Subdivided-claw equality

For the degree-two boundary vertex `u`, the source obtains a no-rooted-
`K_4` graph at equality in Norin--Totschnig Lemma 9.  Inspecting that
lemma's proof is sufficient: its trisection branches give at most
`3|V|-8`, so equality forces its planar outcome with all four roots on the
outer face.

For a plane simple graph with outer facial-walk length `lambda`, Euler's
formula gives

```text
e(H)<=3|V(H)|-3-lambda.
```

Equality at `3|V(H)|-7` and four distinct outer roots forces
`lambda=4`, so those roots occur consecutively on a four-cycle.  But the
literal boundary induced after deleting `u` has only two edges.  This is a
valid contradiction; no unproved equality classification is being added.

## 6. Cross-root elimination of the star

Let the star have centre `t` and leaves `x,y,r,s`, and let `A` and `B`
be any two lobes of excess at least three.  In the `A`-shore,
complete the roots `S-{x}` and add only `xr`.  The augmented graph has
at least

```text
4|A|+delta(A)+8 >= 4|A|+11 = 4(|A|+5)-9
```

edges.  If `p_A(x)>=2`, its possible singleton `x` has augmented degree at
least four.  If `p_A(x)=1`, omit `x`; the completed-root graph has at
least `4|A|+8`, one edge above the required threshold on `|A|+4` vertices.
Fifth-root augmentation yields a model with `x` in helper `U_x`, and only
`xr` may remain virtual.  The symmetric construction in `B` puts `y` in
helper `U_y`, with only `yr` possibly virtual.

The five cross-merged bags are disjoint because every boundary vertex is
in exactly one bag of each shore model, and corresponding ownership is
merged.  Absorbing the connected full lobe `C` into the bag rooted at `r`
does three jobs simultaneously:

- it preserves connectedness through the literal boundary vertex `r`;
- it realises the possible virtual adjacencies `xr` and `yr`; and
- it supplies the `r`-bag's contacts with the `t`- and `s`-bags.

The literal edge `ts` supplies the last adjacency among `t,r,s`.
Consequently the five merged bags form a `K_5` model.  Each remaining
helper `V_A,V_B` is adjacent to all five, while `V_A V_B` is the sole
possibly absent pair.  The seven listed bags therefore form an actual
`K_7^-` model in `G`.

## 7. Rooted-obstruction closure of every star row

If a lobe `L` contains a rooted `K_4` on the four leaves, the four rooted
bags, the singleton centre, and the other two full lobes are seven
disjoint connected bags.  All pairs are adjacent except possibly the two
retained lobes.  Thus target exclusion really does imply the absence of
that rooted model in every lobe.

Fabila-Monroy--Wood Theorem 15 then gives a spanning subgraph of a class
`A`--`F` obstruction.  Any lobe vertex in a clique added at a facial
triangle has, together with its component inside that clique, external
neighbourhood contained in the triangle and the omitted star centre.
This has order at most four, contradicting five-connectivity.  Hence the
whole lobe lies in the planar skeleton.

The six edge counts after deleting all nominated--nominated edges are:

```text
class A: ell=1, e(H)<=4;
class B: ell=2, e(H)<=9=3ell+3;
class C: ell=3, e(H)<=11=3ell+2;
class D: e(H)<=3ell+1;
class E: e(H)<=3ell+2;
class F: e(H)<=3ell+1.
```

For `D`, the four absent edges are the outer four-cycle.  For `E`, the
one absent edge joins the two nominated vertices already on the outer
four-cycle.  The counts agree exactly with the definitions of the six
classes in the cited paper.  Thus `e(H)<=3ell+3` universally.  Exact lobe
accounting gives

```text
e(H)=4ell+delta(L)-p_L(t)>=3ell+delta(L),
```

so every lobe has excess at most three.  Since the three excesses sum to
nine, Theorem 6 applies.  This closes the previously concentrated star
survivor without a finite graph enumeration.

## 8. Scope

The proof is unbounded and computation-free.  Its new terminal operation
is the cross-root merge in the star row, not a finite boundary-code
elimination.  The all-low-excess result leaves only three-component cases
in which at least one lobe has excess at least four.  The star-boundary
theorem closes all such rows when the boundary is `K_{1,4}`.
Concentrated high-excess rows over the other sparse triangle-free
boundaries still require a separate terminal theorem or strict
high-excess descent.
