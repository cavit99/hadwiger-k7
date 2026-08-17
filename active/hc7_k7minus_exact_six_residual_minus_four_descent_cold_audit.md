# Cold audit: the minus-four residual portal descent

**Verdict:** **GREEN** at the pinned revisions below.  This is an independent
internal audit, not external peer review.

## Pinned source, verifier, and input theorem

```text
557b10d311f008962a1d0d65ba713a6f1c02d2b5dcdd74c7f5ce26baedbd65c9
  active/hc7_k7minus_exact_six_residual_minus_four_descent.md
a3246b99e012beb808d0006b8801af5d876913fcc5a600a5be2f0f0d138599cd
  active/experiments/exact_six_residual_portal_minus_four/verify.py
9e1742e20e89f1df3cdb02f944873cc48dbc61bb6830e8e1a8be16b50b214eb1
  active/hc7_k7minus_exact_six_residual_portal_collapse.md
3df2585010cd685c346a1149b36bf89fe9ec95c1dfab0b0a7222e54dd765dd1d
  active/hc7_k7minus_exact_six_residual_portal_collapse_cold_audit.md
```

Relative to the initially audited source
`8eb7e8ee427aba62d841bb1e46d29f611fe1c0ddc0706c886898426d08a71d6b`,
the final source changes only the status from audit-pending to independently
cold-audited; its statements and proofs are unchanged.

The remaining six pinned dependency hashes in the source also match their
current files.  In particular, the rerooting/additivity theorem, ordinary
minor contraction gate, and order-seven ordinary-minor theorem are pinned at
the exact audited revisions quoted there.

## 1. Quotient contractions and the first allocation

Contracting each connected packet `P_i` and each connected outer component
`A,D` is legitimate.  These four sets are pairwise disjoint.  Packet fullness
gives each contracted `p_i` all six contacts in `Z union R`; outer-component
fullness gives each of `a,d` all six contacts in `S=Z union Q`.  The quotient
uses only actual edges of `G`.  Any seven-bag model in it consequently lifts
by undoing these connected contractions.

For `e+c>=1`, the previously proved cross-edge cap gives `e+c<=2`; hence
`e+c+z>=3` supplies a portal edge `r_i z_0`.  In allocation (5), the first
four bags have the following complete contact check:

* `p_1` sees the three allocated `Z` vertices, `z_0`, and both portals;
* `p_2+z_1` sees the two outer bags through their fullness at `z_1`, sees
  `z_0` through `p_2`, and sees both portal bags through `p_2`;
* `a+z_2` sees `d+z_3` through an outer-to-root edge, sees `z_0`, and sees
  the two portal bags through `aq_1,aq_2`;
* `d+z_3` similarly sees `z_0` and both portal bags.

Thus these four bags contact all six others.  Among the last three bags, the
two portal bags contact through `r_1r_2` or a crossed `R`--`Q` edge, and
`z_0` contacts the bag containing its adjacent portal.  At most one of the
twenty-one pairs is absent.

## 2. The second allocation

If `e+c=0`, then `z>=3`.  Three simple incidences from two portals into `Z`
force one portal, relabelled `r_1`, to have two distinct neighbours
`z_1,z_2`.  In allocation (6), every displayed bag is connected.  The only
contacts not immediate from packet or outer fullness are also present:

```text
{p_1,r_2} -- {a,q_2}       via r_2q_2,
{a,q_2}   -- {d,z_4}       via q_2D,
{q_1,r_1} -- {z_j}         via r_1z_j,  j=1,2.
```

Checking the remaining pairs leaves only `{z_1}{z_2}` possibly absent.
The second allocation is therefore another genuine `K_7^-` model.  The two
allocations exhaust `e+c+z>=3`, proving `e+c+z<=2` without a finite-order
assumption on `L`.

## 3. Charge and fragment-closed descent

After portal collapse, the only internal edge of `R` contributes `e`.
Exactly two matching edges, `c` crossed edges, and `z` common-root edges run
from `R` to `S`.  Hence the arithmetic is exactly

```text
eta_S(R)=e+(2+c+z)-8=e+c+z-6<=-4.
```

Fragment additivity then gives `eta_S(C)<=eta_T(L)-4`.  Hereditary rerooting
and relative six-connectivity make the fragment eligible for the stated
fragment-closed minimality argument.  Since `mu_T(L)=2`, minimality gives
`eta_T(L)<=10`; since the original residual has `mu_S(C)=1`, a counterexample
has integer excess at least six.  Therefore equality is forced throughout:

```text
(eta_T(L), eta_S(C-L), eta_S(C))=(10,-4,6),
e+c+z=2.
```

If the original excess is at least seven, the same inequality instead gives
`eta_T(L)>=11>5 mu_T(L)`, so the proper fragment is a strictly smaller
counterexample.  No ordinary minor is asserted to descend into `L`; the
source correctly identifies this as the remaining class-transfer obstacle
for induction restricted to the ordinary-minor branch.

## 4. Independent verifier rerun and scope

The standard-library verifier reran under Python 3 and compiled successfully.
Its exact output was

```text
three_edge_profiles=156 canonical_orbits=12
full_profiles=1536 profiles_reduced=1470
three_edge_witnesses=12 min_contacts=20
two_edge_profiles=54 canonical_orbits=7 bad_orbits=5 safe_orbits=2
two_edge_bad_witnesses=5 min_contacts=20
PASS
```

The code independently constructs the forced twelve-object quotient,
canonicalises by all `Z` permutations and simultaneous portal exchange,
checks connectedness and at least twenty of twenty-one contacts in every
certificate, and verifies that every profile with at least three optional
edges contains a certified three-edge subprofile.  Its two-edge table is a
boundary guardrail: the two entries called `safe` are simply the two orbits
not supplied with a forbidden-model certificate, not a claim that either is
realisable in the original host.  The theorem does not rely on that table.

Within the stated unbounded residual and fragment-closed scope, no defect was
found.  The result does not prove the packet-weighted inequality in the
remaining equality row, transfer an ordinary minor into the derived
fragment, or prove Conjecture 21 or `HC_7`.
