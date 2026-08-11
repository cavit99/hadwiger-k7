# Internal audit: four-colour projections of the `b=2` common-hole orbit

**Verdict:** **GREEN** for Theorem 2.1, Corollary 2.2, and the stated
scope at the exact revisions below.  This is a separate internal
mathematical audit, not external peer review.

## 1. Exact revisions checked

| source | SHA-256 |
|---|---|
| `hc7_k7minus_five_centre_b2_four_colour_projection.md` | `e35a159eb89cad1ba431a8d193f9e7b1a3844959b7587771fbf272d18f9555f7` |
| `hc7_k7minus_five_centre_b2_common_hole_transition.md` | `8dd19d32589ec2a42b4525d445bdcb55e443150dae4a08133f6c30ff1c03bbee` |
| its audit | `79e7bc8a4be7c5746389f5fd73e28b946862b3ee17616ad1f1dc7880a4db516a` |
| `../barriers/hc7_paired_colourful_planar_core_barrier.md` | `25d436688ed47f624fafc465249165ac889c43839e1c3a83d4930a90f1118630` |
| its audit | `43d1a0f23aeadbe31cff338070393524dbfb06adf7e67d5b8836fd63d0466c8f` |

The external input was checked against the statement already independently
verified elsewhere in the repository: Martinsson--Steiner, *Strengthening
Hadwiger's conjecture for 4- and 5-chromatic graphs*, JCTB 164 (2024),
Theorem 1.3.  It says that a colourful set in a four-chromatic graph roots
a `K_4` minor.

## 2. Chromatic drop and class extension

The set `V_r` is one colour class of `c_r|X` and hence is independent.
Its complement `Y_r` is four-colourable.  A three-colouring of `Y_r`,
extended by one fresh colour on `V_r`, would four-colour the exactly
five-chromatic graph `X`; therefore `chi(Y_r)=4`.

For `r in L_p`, the exact support formula from the audited common-hole
theorem excludes colour `r` from `S_p`, because `r` belongs to `L_p`.
Thus `S_p cap V_r` is empty.  Any proper four-colouring of `Y_r` extends
to a proper five-colouring of `X` by assigning one fresh colour to the
independent set `V_r`.  In that extension `S_p` misses the fresh colour,
so the universal two-root cover forces `S_q` to use all five colours.
Its part in `Y_r` consequently uses every one of the original four
colours.  This verifies the quantifiers in items 1 and 2.

## 3. Shore confinement

After `Gamma` and the two pole-incident centres are deleted, `Y_r` is the
disjoint union of its anticomplete `C`- and `D`-parts; all five remaining
boundary vertices belong to `Gamma`.  If neither shore contact set were
colourful in every four-colouring of its shore, choose one witness
colouring per shore and permute names so that their missed colours agree.
Their union would contradict the colourfulness of `S_q cap Y_r`.

The `D`-contact set has order at most three and therefore cannot use four
colours.  Hence the `C`-contact set is colourful in every four-colouring
of the `C`-part.  This also forces that part to be exactly four-chromatic.
The common-hole formula puts all four literal `C`-contacts of `z_q` in
that part: they have the four colours `Omega-{r}`, so none lies in either
deleted colour class.  Thus the colourful set is exactly `N_C(z_q)`.

Martinsson--Steiner now gives four disjoint pairwise adjacent connected
bags, each meeting this four-vertex set.  Disjointness makes the contacts
occur one per bag.  The singleton `{z_q}` is adjacent to all four through
those literal contact edges, proving the shore-confined rooted `K_5`.
The symmetric orientation is identical.

## 4. Scope

The proof roots one `K_4` model at one centre's four contacts.  It neither
makes the other centre's contacts colourful in the same four-chromatic
graph nor gives a model meeting both contact sets.  The cited barrier
shows that such paired rooting is not a formal consequence of two static
colourful-set assertions.  The source therefore states its nonclosure
accurately.
