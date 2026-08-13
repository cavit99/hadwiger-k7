# Internal audit: protected matching edge and the six-fan alternative

## Verdict and revisions

**GREEN for Theorem 2.1 and Proposition 4.2.**  This is a separate internal
audit, not external peer review.  It checks the theorem note at revision

```text
bd79ccab741f81a41b888b9f719bd0ebe7fda2a210e08d9397b5274c70968c02
```

of
[`hc7_k7minus_protected_matching_six_fan_response.md`](hc7_k7minus_protected_matching_six_fan_response.md).
The exact finite counterprofile verifier has revision

```text
34607b3251b8e263ae018107d843663b280f1a5cbe3f2f9dcf4acc53da2cc596
```

and was rerun successfully.  The finite one-contact and three-arm screens
have the narrower diagnostic status stated in the theorem note and their
own experiment report; they are not promoted by this audit.

## 1. The exact order-seven separation

Apply the fan form of Menger's theorem in `H-w`.  If no six-arm fan from
`x` to distinct members of `Q` exists, there is a set `S` of order at most
five separating `x` from `Q-S`.  The component `A` containing `x` is
disjoint from `Q`.  Since `N_G(u)=Q dotcup {v}`, the vertex `u` has no
neighbour in `A`, and

```text
N_G(A) subseteq S union {v,w}.
```

The sets `A` and `{u}` lie on opposite sides.  Seven-connectivity therefore
forces equality throughout:

```text
|S|=5,\qquad N_G(A)=S \dot\cup \{v,w\}.
```

The edge `wx` crosses this order-seven separation.  Removing `A` deletes
the sole monochromatic restored edge under the fixed colouring of `G-wx`.
If the resulting boundary partition extended through the `A` side, a
permutation of the six colour names would glue the two colourings and
six-colour `G`.  The rejected exterior trace conclusion is therefore
valid and retains the original edge and colouring.

The theorem does not retain ownership in an independently chosen rooted
minor model.  The note states this limitation explicitly.

## 2. The mate-protected parity proposition

With terminals `T=Q union {w,x}`, the terminal-kernel theorem leaves at
most two nonterminals.  If `x` has no `Q` neighbour, zero or one
nonterminal contradicts minimum degree three.  With two nonterminals
`a,b`, the vertex `x` must see `w,a,b` and cannot belong to either Wu charge
set.  The two disjoint charge sets therefore partition the eight vertices
of `Q union {w}` into two four-sets.  Each of those eight terminals has
degree two in `L[T]`, while `x` has degree one.  The induced terminal degree
sum is seventeen, contradicting the handshaking lemma.  Proposition 4.2 is
sound.

Protecting the second centre changes the terminal count and permits an
extra terminal neighbour of `x`; the parity proof then fails.  The note
does not infer a simultaneous two-centre contact.

## 3. Finite counterprofile and scope

The retained verifier checks that the displayed ten-vertex graph is
three-connected, has the selected edge and six direct `x-Q` contacts, has
no `K_7^-` minor, and has no `Q`-rooted `K_5^-` model.  Its output is

```text
GREEN protected matching six-fan counterprofile: kappa=3, six direct arms, no K7-minus or Q-rooted K5-minus minor
```

This exact finite diagnostic shows that the encoded uncoloured fan data are
insufficient for a rooted branch-set transfer.  It records a route
nonclosure, not a counterexample to the critical-host theorem: the graph is
only three-connected and carries no critical colouring response.

The first unsupported inference is exactly the one recorded in the note:
six paths in the original graph may have one common retained-side
attachment, while the required rooted branch-set adjacencies belong to an
independently contracted model.  Neither Menger's theorem nor the
terminal-kernel theorem exchanges those quantifiers.
