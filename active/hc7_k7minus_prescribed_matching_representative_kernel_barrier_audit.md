# Self-audit: prescribed matching representatives and the kernel barrier

**Verdict:** **GREEN as a self-check** for Theorem 1.1 and for the stated
encoding, arithmetic and scope of Diagnostic 2.1.  The theorem is an
unbounded, computation-free consequence of the audited five-centre matching
construction.  The diagnostic remains a route nonclosure, not a promoted
computer-assisted theorem, because the exact order-eight catalogue has not
received an independent audit.

This audit was written by the same agent as the source.  It is not a cold
independent audit and is not external peer review.

## Exact revisions

The checked source is
[`hc7_k7minus_prescribed_matching_representative_kernel_barrier.md`](hc7_k7minus_prescribed_matching_representative_kernel_barrier.md),
with SHA-256

```text
e11288c4a75e0343472eb225498a828eb7a4c5bdbeae15ce6274a9c3e3e7a958
```

The diagnostic and its reproduction note are

```text
05ef17908c9d1c81aefa68ca4a2d530d8b9c9a05a5e661d21058db415a32917f  active/experiments/dominated_singleton_exact_eight_kernel_absorption/probe.py
3e760593a99cee665cb35a0b4ca5362168ec1be95d5c260318312f8341aeb682  active/experiments/dominated_singleton_exact_eight_kernel_absorption/README.md
```

The direct mathematical inputs were checked at

```text
d0d3aa3574d747a3164f29febff1fa8fd6f37b0899415cd97a515005c5de5f43  results/hc7_k7minus_five_centre_common_matching_reduction.md
c81a3f7d656a4ef02a69ab88b311acc3601d9103aedbf6b6380c54cee350a3c3  results/hc7_k7minus_dense_branch_rotation_visibility.md
53d4778ffbbf7af539262a10a077ca2849e7c7d38ca4beea12be6c6c5a3dc70b  results/hc7_eight_terminal_rooted_carrier_trichotomy.md
3c4efc5ca2480abee3892b88fac231136ef57077beca5ebadd5cf414ad0c2c0f  active/hc7_eight_terminal_exact_bundle.md
```

The first three inputs have separate GREEN audits.  The last is deliberately
an active catalogue draft: its order-eight and order-nine censuses retain the
trust boundary stated there.

## 1. Prescribed-representative proof

The definition

\[
                         K_w=\bigcap_{I\in\mathcal I_w}I
\]

and \(y\notin K_w\) give an independent triple `I_w` which avoids `y`.
Thus `y` belongs to the corresponding five-set `R_w` and is eligible as the
prescribed representative.

After fixing `y`, each of the other four five-sets loses at most that one
vertex and hence has order at least four.  For a subfamily of order
`1<=k<=4`, its union contains any one of its members, so it has order at
least four and therefore at least `k`.  This is the complete Hall check; no
intersection or independence assumption between the four sets is missing.

The resulting five representatives are distinct.  None can be another
centre because the five centres are independent and each representative is
a neighbour of its own centre.  Hence the five selected edges are a
matching.

The proof of the audited common-matching theorem is uniform in these
choices.  Its contraction argument supplies every nonempty signature and
excludes the empty one.  For the prescribed singleton, the star-contraction
colouring makes the independent triple monochromatic and gives the five
vertices outside it five pairwise distinct further colours.  Assigning the
centre the colour of `y` therefore makes the prescribed edge, and no other
edge, monochromatic.  This verifies every conclusion of Theorem 1.1.

## 2. Extra-root-edge encoding

An order-eight carrier is a 28-bit graph on roots `0,...,7`, with root `7`
the protected centre.  For each of the 425 previously failed compositions,
the new loop does the following for every absent pair `(q,7)`:

1. add exactly that rooted edge;
2. recompute the possible owners of root `7`, including `q` after the edge
   is added;
3. absorb root `7` into every legal owner; and
4. apply the exact deletion-contraction test for a `K_5^-` minor after
   adjoining the fixed graph on `Q`.

This correctly models the quotient effect of a selected edge `wy` when `w`
and `y` occupy different rooted bags and their adjacency was absent from the
retained carrier.  It deliberately grants every missing rooted edge without
claiming that a host matching mate can be placed in the corresponding bag.

The assertions in the script pin the complete histograms

```text
FCQ`_  {0:30, 2:80, 3:40, 4:60}
FCQb_  {0:6, 2:24, 3:18, 4:26}
FCp`_  {0:15, 1:28, 2:35, 3:14, 4:49}
```

and the zero-forcing profiles

```text
(3,3,3,3,3,3,3,5), protected-root degree 5: 20+4+14=38
(3,3,3,3,3,3,3,7), protected-root degree 7: 10+2+1=13.
```

Thus the resistant total is `38+13=51`, while `425-51=374` failures have
at least one forcing rooted edge.  For protected-root degree seven the set
of absent incident edges is empty, so those thirteen records are correctly
counted as resistant rather than silently omitted.  For degree five the
script explicitly tests both absent incident edges.

The reproduced default run ended with the asserted output and exit status
zero on 12 August 2026.

## 3. Trust boundary and logical conclusion

The diagnostic does not encode the literal neighbourhood of the protected
centre, the set `K_w`, a matching mate's position inside a lifted branch
set, or the rejected boundary colouring.  Its failures therefore refute
only the quotient implication that one freely chosen extra incident rooted
edge always closes.

Conversely, a forcing rooted edge in one of the other 374 records is not a
host theorem.  One still needs a supported neighbour in that particular
rooted bag, and the selected edge must create the missing bag adjacency.
The four choices of protected centre come with separately existential rooted
models, so their placements cannot be combined without a common-model
theorem.

Finally, the catalogue generator's order-eight exhaustiveness has not been
independently audited.  This self-audit checks the downstream loop and its
quantifiers but does not improve that upstream status.  The 803 order-nine
residues are untouched by the extra-edge screen.  No closure of the
dominated-centre branch, the eight-coordinate branch, the `K_7^-`
six-colour conjecture or `HC_7` is claimed.
