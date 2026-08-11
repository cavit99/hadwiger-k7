# Internal audit: the `b=2` common-hole transition

**Verdict:** **GREEN** for Lemma 2.1, Theorem 3.1, Corollary 3.2,
Theorem 4.1, Corollary 5.1, and the stated scope at the exact revisions
below.  This is a separate internal mathematical audit, not external peer
review.

## 1. Exact revisions checked

| source | SHA-256 |
|---|---|
| `hc7_k7minus_five_centre_b2_common_hole_transition.md` | `8dd19d32589ec2a42b4525d445bdcb55e443150dae4a08133f6c30ff1c03bbee` |
| `hc7_k7minus_five_centre_b2_rectangle_locks.md` | `8843b2c86dbf6ccc6555fd198246c5c9f8a85ffa9ffc69b67f6e40a58d0e3674` |
| its audit | `032d3db40cf89b7ef05bc2bda4825b3bbacfc44515427531f2758ab36c1477ac` |
| `../results/hc7_two_root_kempe_orientation_transition.md` | `83d49aff3cd363765b83d111c2b52e2eec2ba545a757792f499cec9f5b9e2c9c` |
| its audit | `5aebb2adaac4df4a23348f280e1c797e6d18bc876e77faff4d93a8d94c83ca4a` |
| `../results/hc7_k7minus_five_centre_two_cut_reduction.md` | `1917b5e3d183d44a2d905d2628272d10e4bc6f7ae0768b43cab0e9462b83332a` |
| its audit | `d01183c936d79ea2e07f956c2e89f7291df9cc28a5dab3dda6b093c8a69c4ea3` |

## 2. Common-hole orbit

In a colouring with common hole `r`, the unique `s`-coloured contacts of
the two centres cannot lie in different `r`--`s` components.  Swapping
one such component would change exactly one four-contact row from
`Omega-{r}` to `Omega-{s}`.  The two rows would then have intersection
three.  With the two centre colours chosen from the disjoint nonempty
lists, the resulting forbidden-position relation has two rows of order
four but contains no full row or column and no `2 by 4` or `4 by 2`
rectangle.  The audited eight-position Hall criterion therefore gives an
avoiding permutation and a forbidden six-colouring of `G`.

Thus the two contacts lie in one component.  Swapping it changes both
rows from hole `r` to hole `s`, because neither row initially has an
`r`-coloured contact and each has exactly one `s`-coloured contact.  This
proves every step of Lemma 2.1 and reaches all five holes directly from
the initial one.

## 3. Fixed five-chromatic core

The switches use only colours in `Omega`, so the `gamma` colour class is
fixed and independent.  The restriction gives a five-colouring of `X`.
If `X` were four-colourable, the fixed independent class and the two
nonadjacent omitted centres could be assigned two fresh colours, yielding
a six-colouring of `G`.  Hence `chi(X)=5`.

For an arbitrary five-colouring of `X`, if each of the two contact sets
missed a colour, the omitted centres could receive their respective
missing colours and the independent class a fresh sixth colour.  The
centres are nonadjacent, so the missing colours need not agree.  This
verifies the universal colourful-set cover.

In the orbit colouring, the exact support formula

```text
(Omega-{r}) union (Omega-L_x)
```

correctly combines the equality-shore contacts with the non-`gamma`
opposite-shore triangle contacts.  It equals all of `Omega` exactly when
`r` is not in `L_x`, proving the orientation table and both exclusive
orientations.  A paired-rooted `K_5` in `X` then has the asserted literal
`K_7^-` completion with the two nonadjacent centres.

## 4. Orientation-changing separator

For `r in L_p` and `s in L_q`, the orbit switch changes the unique
colour-dominating root from `z_q` to `z_p`.  Each dominating root sees all
five `Omega` colours in `X` and its incident pole supplies `gamma`; the
other root misses the designated hole.  The hypotheses of the separately
audited two-root orientation-transition theorem therefore hold with the
two colourings differing exactly on `K_{rs}`.

That theorem supplies adjacency to both roots, the actual full-neighbourhood
separation, order at least five in `H`, and one neighbour in each untouched
colour class.  The `s`-side identification follows from the disjoint-list
formulas on the fixed `D`-shore.  The component is proper because equality
with all of `C` would make `G[C]` bichromatic, contradicting the audited
bound `chi(G[C])>=4`.

Finally, when all three pole-free centres lie in the boundary, they account
only for the untouched `gamma` class.  The three other untouched colour
classes require three further boundary vertices.  This gives the displayed
orders six and three after deleting all five centres.

## 5. Scope

The source correctly does not infer a paired-rooted model from the two
exclusive orientations.  Its transition separator is strict but need not
have the anchored five-centre two-cut form.  No closure of the `b=2` row
or of the full order-at-least-eight branch is asserted.
