# Pairwise contact of the common-hole Kempe components

**Status:** written proof; separate internal audit GREEN at the revision
recorded in the adjacent audit.
This note proves a simultaneous-switch consequence of the common-hole orbit
in the all-rainbow `b=2` row.  The four relevant Kempe components pairwise
touch.  A separate explicit barrier shows that this intersection condition,
even together with the relative seven-connectivity inequality, does not by
itself force paired branch sets or a strict separation.

Throughout, `K_7^-` denotes `K_7` with one edge deleted, and two vertex sets
*touch* if they intersect or an edge has one end in each set.

## 1. Setting

Use the notation and conclusions of the separately audited
[common-hole transition theorem](hc7_k7minus_five_centre_b2_common_hole_transition.md).
Fix \(r\in\Omega\) and its proper six-colouring `phi_C^r` of
\(G[C\cup T]\).  The independent boundary set `T` has colour `gamma`, and
each of the two four-contact sets

\[
                       N_C(z_p),\qquad N_C(z_q)                 \tag{1.1}
\]

uses every colour of `Omega-{r}` exactly once.  For
\(s\in\Omega-\{r\}\), let `K_s` be the `r`--`s` component containing the
`s`-coloured contacts of both centres.  The common-hole theorem proves that
this component exists and that interchanging `r,s` on it changes the common
hole from `r` to `s`.

Retain the fixed opposite-shore colouring `phi_R` and the nonempty disjoint
availability lists \(L_p,L_q\subseteq\Omega\) from the separately audited
[`b=2` rectangle theorem](hc7_k7minus_five_centre_b2_rectangle_locks.md).

## 2. Simultaneous switches

### Theorem 2.1 (pairwise Kempe contact)

If `G` is not six-colourable, then the four components

\[
                         \{K_s:s\in\Omega-\{r\}\}               \tag{2.1}
\]

pairwise touch.

#### Proof

Suppose that `K_s,K_t` are disjoint and anticomplete for distinct
\(s,t\in\Omega-\{r\}\).  Simultaneously interchange `r,s` on `K_s` and
`r,t` on `K_t`.  This gives another proper colouring: each individual
interchange is a Kempe switch, and there is no edge between the two sets
on which the two switches use the common colour `r`.  The monochromatic
boundary set `T` is unchanged because it has colour `gamma`.

Before the switches, each contact set in (1.1) has colour support
`Omega-{r}`.  Its unique `s`-coloured contact lies in `K_s`, and its unique
`t`-coloured contact lies in `K_t`.  The simultaneous switches therefore
replace both of these colours by `r`.  Each of the two contact sets now
uses only the three colours

\[
                         \{r\}\cup(\Omega-\{r,s,t\}).            \tag{2.2}
\]

Choose one colour from each of the disjoint nonempty lists `L_p,L_q` for
the two erased centres in `phi_R`.  The two colours are distinct.  In the
contraction-colouring gluing criterion, all forbidden positions now lie
in those two rows and the three columns in (2.2).  Thus the forbidden
relation has at most six positions and contains no full row or column, no
`2 by 4` rectangle, and no `4 by 2` rectangle.  The exact Hall criterion,
Lemma 2.1 of the rectangle theorem, supplies an avoiding permutation.
The two shore colourings then glue to a proper six-colouring of `G`, a
contradiction.  Hence `K_s` and `K_t` touch. \(\square\)

### Corollary 2.2

The common-hole orbit is not merely four separate connections between the
two contact sets.  In every one of its five colourings, the four connections
form a pairwise-touching family of connected subgraphs, each containing the
same-coloured contact of each centre.

## 3. Exact limit of the conclusion

Pairwise contact is not enough to synchronize the four roots.  The explicit
[pairwise-Kempe relative-connectivity barrier](../barriers/hc7_b2_pairwise_kempe_relative_connectivity_barrier.md)
has all four components meeting in one vertex.  It also has a relative
seven-vertex boundary for which every nonempty proper vertex set on the
shore has boundary at least eight.  Nevertheless, it has no four disjoint
connected sets each meeting both contact sets.

The barrier does not realize the five-centre host.  It identifies the first
unsupported inference precisely: Theorem 2.1 plus relative
seven-connectivity alone does not imply a paired-rooted `K_4` model or a
strict exact order-seven separation.  Any use of the pairwise-contact
family must additionally exploit the exact pole/centre contact profile,
proper-minor colouring responses, or stronger model structure.

## Dependencies and claim status

- the common-hole colourings and individual `r`--`s` connections are the
  separately audited common-hole transition theorem;
- the disjoint lists and exact Hall criterion are the separately audited
  `b=2` rectangle theorem; and
- the failure of the purely local continuation is an explicit written
  barrier, linked above.

The simultaneous-switch deduction and pairwise-contact theorem are proved
here.  No paired-rooted minor, new separation, or closure of the `b=2` row
is claimed.
