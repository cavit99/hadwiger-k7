# Internal audit: second contractions and six-boundary kernels

**Verdict:** **GREEN** for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.

**Audited source:**
`active/hc7_k7minus_e5_s3_second_contraction_kernel_reduction.md`

**SHA-256:**
`3218c292213fbf7e9cf6e7e6a38b2c3cef0c05801a4359cbd956a28daf3ef93e`

The audit covers the whole source file at that hash.  Sections 2--4 and
Proposition 5.2 are computation-free.  Corollary 5.1 depends on the
separately promoted computer-assisted theorem discussed in Section 6 below.

## 1. Imported endpoint

The exact predecessor is Proposition 5 of
`active/hc7_k7minus_e5_s3_six_full_contraction_reduction.md`, at SHA-256

```text
4ab5afe3d8e8cee4f41577ec5e571b033a792a61babfe5e8e795d0961904b991.
```

It supplies all imported assertions used here: `H=G/uv` is
four-connected and meets `4|V(H)|-7`; every four-cut contains `z`; each
such cut exposes a degree-four singleton and a connected remainder of order
`a+1`; and lifting the cut gives an exact boundary-full five-cut in `G`.
The last property makes every returned singleton adjacent to both `u,v`
and of degree five in `G`.  The selected `(a,Phi,rho)=(a,11,2)` comparison
is also exactly the predecessor's selection.

## 2. Anchored singleton switch

Contracting `dz` loses at most

```text
1+|N_H(d) intersect N_H(z)|<=4.
```

An edge contraction of a four-connected graph is at least
three-connected, so failure of four-connectivity gives a three-cut.  It
must contain the contracted vertex and lifts to a four-cut containing
`d,z`; the predecessor normal form therefore exposes another degree-four
singleton `w` adjacent to both.

If `d,w` had at least two common neighbours besides `z`, a three-cut would
isolate `dw`.  If they had exactly one, the displayed four-set would leave
the nonsingleton component `{d,w}`, contrary to the exact singleton-plus-
connected-remainder form.  The graph has more than enough vertices for the
opposite side to be nonempty, since the imported lobe order satisfies
`a>=8`.  Hence

```text
N_H(d) intersect N_H(w)={z}.
```

The edge `dw` loses exactly two edges on contraction.  A three-cut after
that contraction would lift to a four-cut whose singleton is a common
neighbour of `d,w` other than the cut vertex `z`, a contradiction.  Lemma
2.1 is correct.

## 3. The `K_2` kernel and its excess identity

In the connectivity-drop case, both returned singletons must be adjacent
to both original endpoints: otherwise one would still have degree four in
the five-connected graph `G`.  Their two remaining outside-neighbour pairs
are disjoint by the common-neighbour equality.  The six-set `P` therefore
exposes exactly the stated labelled `K_2` component `T`.

The kernel has one internal edge and eight boundary contacts, so

```text
eta_P(T)=1+8-4*2=1.
```

The other components have total order `a-1`.  Substituting these values and
`|E(G)|=4(a+7)-7` gives

```text
sum_{K != T} eta_P(K)=16-|E(G[P])|.
```

No adjacency required by this calculation is merely inferred from a
contracted contact.

## 4. Nontrivial four-separation and crossing kernels

If `J=H/dz` is four-connected, the contraction-loss bound gives
`|E(J)|>=4|V(J)|-7`.  Five-connectivity would make `J` a smaller target-free
`E5` enemy, so the live quotient is exactly four-connected.

For an eligible nontrivial four-cut, the contracted vertex belongs to the
cut.  Lifting it inside `H` gives the five-set `Y`.  If a member of `Y`
missed an open side, deleting the other four vertices would either avoid
the common anchor or expose a nonsingleton side.  The imported normal form
excludes both.  Since `d` has degree four, sees `z`, and meets both sides,
`d` contributes at most two boundary edges.  Thus `|E(H[Y])|<=8`.
Expanding `z=uv` adds `uv` and at most three duplicated contacts, proving
the six-boundary bound `|E(G[R])|<=12`.  Both open sides have order at most
`a-1`.

If one side `F` misses an endpoint, deleting that endpoint from `R` gives a
five-cut.  Its high-excess component cannot lie in `F`, whose order is at
most `a-1`; exact order accounting then forces `|F|=2` and high-side order
`a`.  If `F` is two singleton components, boundary fullness gives the twin
case.  If it is an edge, its excess is at most three.  Excess at most one
improves `Phi`, while excess two ties `Phi` and improves `rho`; hence excess
three is forced and both edge ends are complete to the five-cut.

The returned singleton `d` sees `u,v` and both low vertices.  The earlier
all-five-vertices-meet-both-sides conclusion, rather than boundary fullness
alone, supplies its fifth neighbour `b` in the opposite side.  Its degree
five then fixes every displayed contact and excludes all three vertices of
`U`.  The low subgraph is exactly `P_3` in the twin case and `K_3` in the
edge case.  Direct substitution gives the two identities

```text
sum eta_P(K)=16-|E(G[P])|     for P_3,
sum eta_P(K)=15-|E(G[P])|     for K_3.
```

The theorem correctly quantifies over any eligible nontrivial cut; it does
not assume a canonical first cut.

## 5. Host-level consequences

For a connected component with neighbourhood `P-{r}`, contracting that
component produces exactly the five-full representative in the promoted
finite theorem.  If the applicable boundary threshold is met, its certified
`K_7^-` model lifts through the contraction.  Otherwise the corresponding
exact identity gives excess at least four.  The component order is `a-1`
for `K_2` and `a-2` for `P_3,K_3`, so `P-{r}` supplies a strict
high-excess descent.  Corollary 5.1 is correct conditional on the finite
theorem.

For Proposition 5.2, a component `K` missing `r` remains a component behind
the five-cut `P-{r}`.  It is distinct from any component of order at least
`a`: the at least three vertices of `T union {r}` lie outside `K`, so
`|K|>=a` is impossible when only `a+2` vertices lie outside the cut.  The
universal high-excess component is therefore different from `K`, leaving
at most two vertices for `K`.  A singleton is complete to the five-set by
boundary fullness.  In the two-vertex case, equality forces the high
component to have order `a`; the same potential comparison makes the edge
excess three and hence both ends complete to the five-set.

This argument bounds each `P`-non-six-full component, but neither their
number nor the size of a `P`-six-full component.  If a `P`-six-full
component exists, deleting all other opposite components before contracting
it legitimately applies the six-full finite screen and gives the displayed
boundary bounds.

## 6. Computer-assisted dependency

The exact finite input is Theorem 2.1 of
`results/hc7_k7minus_e5_six_boundary_kernel_screen.md`, SHA-256

```text
8d88540972595703378926f57b99270603d51ec1123976e9d7a024a6f3535ea1.
```

Its adjacent audit independently validates all 11,914 positive
certificates and the six one-edge-below sharpness witnesses.  The active
source uses only its positive five-full thresholds for Corollary 5.1 and
its positive six-full thresholds for the subsequent boundary bounds.

## 7. Exact scope and surviving branches

The source explicitly retains the three gaps found during hostile review:

1. an exactly four-connected self-similar quotient whose four-cuts all
   retain the anchored singleton normal form;
2. the case in which every eligible nontrivial separation is met on both
   sides by both original contraction endpoints; and
3. the remaining opposite-shore configurations, including an unbounded
   number of labelled non-six-full singleton or edge components and one or
   more arbitrarily large `P`-six-full components.

No iteration through an enlarged contracted anchor is claimed.  No finite
incidence classification is promoted to an unbounded density theorem.  No
unresolved assumption remains inside the statements actually proved, but
the proposed kernel-localisation lemma, `(E5)` and the primary
seven-connected `4n-2` theorem all remain open.
