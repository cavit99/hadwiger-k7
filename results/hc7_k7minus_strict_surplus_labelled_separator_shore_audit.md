# Internal audit: strict labelled separator shore at positive surplus

**Verdict:** GREEN for the exact source revision below.

**Audited source:**
`results/hc7_k7minus_strict_surplus_labelled_separator_shore.md`

**SHA-256:**

```text
8579527fb6abc6fe1f36948ac277a0997d170f0af473fa557cf643593a5c41c0
```

Independent hostile checks of the branch-set argument and the density and
contraction argument found no unresolved mathematical defect in this
revision.  This is an internal audit, not external peer review.

## 1. Imported canonical setting

The proof uses the adjacent audited canonical theorem at revision

```text
b1fdb62070dda275a9f2e6ddd1bc1642f16b7d55df4ab5de7565375a0d7db5d8  results/hc7_k7minus_strict_surplus_canonical_six_boundary.md
```

That source proves boundary fullness, the common realisation
`B_y=(V(G)-N[x]) union {y}`, existence of a spanning `K_6` model in `G-x`,
and the four-branch-set bound for each fixed `T_y`.  These are exactly the
imported facts used here.

## 2. Simultaneous contact and branch-set split

If the seven vertices of `N(x)` occupy at least five branch sets, one branch
set contains two of them.  Removing either of those two roots leaves the
corresponding set `T_y` meeting the same five branch sets, contradicting the
imported fixed-`T_y` bound.  Thus the simultaneous four-branch-set conclusion
is exact.

In the connected split `D=A dotunion B`, every other branch set meets at
least one side because it is adjacent to `D`.  Every branch set meeting only
one side is contacted.  Since `D` is contacted and at most four branch sets
are contacted altogether, there are at most three exclusive branch sets;
one orientation has at most one branch set meeting only the opposite side.
Absorbing `x` into the appropriate rooted half preserves every adjacency
except possibly that one.  The seven displayed sets therefore form the
claimed `K_7^-` model.

## 3. One-root separator shore

The spanning-tree construction supplies two disjoint connected one-root
subsets of a multiply rooted branch set, each with connected complement.
If both subsets meet every uncontacted branch set, the split lemma applies.
Otherwise one subset `C` misses an uncontacted branch set `U`.

The quantifiers and labels were checked explicitly:

- `C` contains exactly one neighbour `y` of `x`;
- all other vertices of `C` lie outside `N(x)`;
- the uncontacted `U` also lies outside `N[x]`;
- consequently `C subsetneq B_y` and `xy` is the unique edge from `x` into
  `C`; and
- `U` remains on a far side after deleting `N_G(C)`, so this neighbourhood
  is an actual separator and seven-connectivity gives order at least seven.

No upper bound on this separator is proved.  In particular, the source does
not call it an exact order-seven cut or a new canonical six-boundary shore.

## 4. Density and contraction accounting

Boundary fullness and the sole restored edge `xy` give

\[
 k(B_y)=7,
 \qquad
 \eta(B_y)=20+q-|E(G[T_y])|\ge q+10.
\]

For a connected `C`, contraction removes `|C|-1` vertices and replaces the
`4|C|+eta(C)` internal and leaving edges by exactly `k(C)` simple edges.
Therefore

\[
 q(G_C)=q+k(C)-4-\eta(C).
\]

The properness condition `|C|>=2`, target-freeness under taking a minor, and
minimum-order contradiction when `G_C` is seven-connected are all used
correctly.  Density and simplicity force `|V(G_C)|>=9`, so failure of
seven-connectivity supplies an actual cut of order at most six.

The contracted vertex must belong to that cut; otherwise expansion of the
connected set `C` leaves the quotient components separated and gives a cut
of `G`.  Removing the contracted vertex from the cut yields the stated set
`Z`, component contact bound, and exact order-seven cut when a separator of
order `7-|Z|` exists inside `C`.

## 5. Unresolved scope

The source correctly leaves three cases open:

1. a high strict shore need not inherit the canonical hypotheses;
2. a singleton shore need not have degree seven and has no proper whole-shore
   contraction; and
3. an eligible contraction failure may return only a nested exact cut, or
   may require an additional label-preserving rooted linkage theorem.

The result does not eliminate positive surplus or prove the `4n-2` target,
Conjecture 21, or `HC_7`.
