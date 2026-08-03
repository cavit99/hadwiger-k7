# Internal audit: density-safe atom reduction

**Audited theorem:**
[`hc7_k7minus_generalised_safe_atom_reduction.md`](hc7_k7minus_generalised_safe_atom_reduction.md)

**Theorem SHA-256:**
`5124821e57c6317c9433a53eac2e9f608f43f9dfd2c7777d5c79da090ab3ef7d`

**Verdict:** **GREEN.**  The three promoted conclusions in the draft are
computation-free.  This is a separate internal audit, not external peer
review.  The theorem applies only to a minimum counterexample with strict
surplus `q(G)>=1`.

## 1. Generalised criticality

For a density-safe edge `xy`, contraction changes the surplus by

\[
                     q(G/xy)=q(G)+3-c(xy)\ge q(G).
\]

Minimality therefore makes `xy` noncontractible, and the standard pullback
gives an exact order-seven cut containing its ends.

For an `\mathcal X`-fragment `A` meeting the degree-seven set `L`, the
audited safe-incident theorem supplies a density-safe edge with one end in
`A`; its certifying cut meets `A`.  If `A` avoids `L`, a leaf `z` in a
component of `A` has at most one neighbour there and at most seven on the
boundary.  Since `z` has degree at least eight, it has degree exactly eight,
is boundary-full, and has exactly one interior neighbour.

The boundary contains a vertex `s` of boundary degree at most three.  This
is immediate in the three-component case.  In the two-component case it
follows from the audited seven-vertex `K_5`-minor-free structure theorem;
the sole pentagonal-bipyramid exception is excluded by the displayed
`I_2\vee B_5` branch-set model.  Hence

\[
                       c(zs)\le4\le q+3,
\]

so the certifying cut for `zs` meets `A`.  These are exactly the two
conditions in Mader's definition of `\mathcal X`-criticality.  Mader's
Theorem 5.2 then gives atom order at most `7/2`, hence at most three.

## 2. Elimination of atoms inside the high-degree forest

Every component behind the atom boundary is boundary-full and is itself an
`\mathcal X`-fragment.  Thus the atom is one component and every opposite
component has at least its order.

- A singleton in `F` would have degree seven.
- An edge in `F` has two degree-eight, boundary-full ends and hence seven
  common neighbours.  The essential-edge order-six separation must contain
  every common neighbour, an immediate contradiction.
- A three-vertex atom in `F` is a path.  Its leaves are boundary-full and
  its middle vertex has at least six boundary neighbours.  Four of those
  roots support a rooted `K_4^-` in the opposite closed shore.  The displayed
  seven bags are disjoint and connected; the boundary vertex added to the
  first leaf repairs the otherwise missing leaf-to-leaf contact.  The only
  possible missing adjacency is therefore the one inside the rooted
  diamond.

This verifies that every atom meets `L`.

## 3. Three-component decoder

Atom minimality makes both opposite components nonsingleton, so the rooted
diamond theorem applies in either opposite closed shore.

For an edge atom, the two endpoints have at least five common boundary
neighbours.  For a path atom, splitting off a leaf loses at most one root on
the leaf side and at most one root on the remaining-edge side, again leaving
five common roots.  Four roots produce the diamond and the fifth joins the
unused opposite component to both atom pieces.

For a triangle atom, each vertex misses at most two boundary roots.  If four
roots see all three vertices, the three singleton triangle bags complete a
rooted diamond.  Otherwise the draft's three-set argument is exact: failure
of every singleton-versus-edge split would force the miss sets to be

\[
 \{x_2,x_3\},\quad\{x_1,x_3\},\quad\{x_1,x_2\},
\]

which leaves four common roots after all.  Hence a five-common-root split
exists.  This covers every connected graph on two or three vertices and
proves that a nonsingleton atom has exactly one opposite component.

## 4. Sparse-family audit and limitations

The draft correctly does **not** replace `\mathcal X` by a sparse family
`\mathcal R` of selected safe edges covering `L`.  For an
`\mathcal R`-fragment disjoint from `L`, the crossing edge `zs` produced by
the leaf argument need not have a degree-seven endpoint and need not belong
to `\mathcal R`.  An already selected edge in the fragment boundary need not
have any certifying cut which meets the fragment.  Therefore sparse-family
criticality, and hence the atom bound for that family, would be unsupported.

No finite triangle computation is used.  The theorem does not address the
zero-surplus case, and it does not eliminate the remaining singleton or
two-component atoms.  The companion four-distinct-miss path theorem is
computer-assisted and remains logically separate.

## 5. Inputs checked

The adjacent GREEN audits were checked for:

- the strict-surplus minimal-enemy structure;
- the degree-seven density-safe contraction;
- the essential-edge six-separation;
- the two/three-component seven-cut theorem;
- the seven-vertex `K_5`-minor-free structure theorem; and
- closed-shore rooted connectivity.

Mader's definitions and the half-connectivity atom bound match Theorems 5.1
and 5.2 in Kriesell's *Minimal Connectivity* and Section 7.2/Lemma 7.7 of
Chan's dissertation.  Jørgensen's rooted `K_4^-` consequence is used only
after the written closed-shore lemma supplies internal four-connectivity and
the shore has at least two vertices.
