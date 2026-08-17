# Second cold audit: the complete order-seven ordinary-minor synthesis

**Verdict:** **GREEN** at the pinned revision below.  This is a second
independent internal audit, not external peer review.  I reconstructed the
Hall split, the four imported branches, and the host composition before
consulting the first synthesis audit.

## 1. Pinned source and dependencies

The audited source is

```text
6005366ee90407ec9207fc3d07cc52dd84b28b9cfec254d2f583ed5c1e818a20
  active/hc7_k7minus_sparse_sixcut_order_seven_ordinary_minor_completion.md
```

The mathematical source first read in this audit had SHA-256
`836535c3db469ab1b1965ba4d1570dd4881ff44ea5ce79ef888c9f0d552bb9b5`.
The final pinned revision changes only the status line to record the first
completed synthesis audit; its theorem, proof, dependency block, and scope
are unchanged.

I recomputed all fifteen dependency hashes in its Section 3.  Each matches:
the Hall-profile source and audit, the four terminal sources, their four
verifiers, the two `i=1` audits, and the `i=2`, `i=3`, and `i=4` audits.
Thus this synthesis imports the exact revisions it names.

## 2. Spanning normalisation and exact Hall exhaustion

Let the five ordinary branch bags have union `M`.  Every component of
`C-M` has an edge to `M`, since `C` is connected and `M` is nonempty.
Absorbing each such component into one bag it meets preserves that bag's
connectivity, bag disjointness, and every old quotient contact.  Hence the
five bags can indeed be assumed to partition the seven vertices of `C`.

If their root-incidence graph has a five-bag matching, adjoining the five
matched roots gives connected, disjoint rooted bags and preserves the
ordinary quotient.  This is already the asserted punctured model.

Otherwise let `I` be inclusion-minimal deficient, write `i=|I|`, and let
`U` be the union of its bags.  Hall deficiency, relative six-connectivity,
and `|C|=7` give the equality chain

```text
6 <= |N_C(U)|+|N_S(U)|
  <= (7-|U|)+(i-1)
  <= 6.
```

Consequently

```text
|U|=i,       |N_S(U)|=i-1,       N_C(U)=C-U.
```

Since `I` consists of `i` nonempty disjoint bags whose union has order
`i`, all its bags are singletons.  Every proper subfamily is Hall-sufficient;
in particular, for each `u in U`, the set `U-{u}` has a matching onto the
entire `(i-1)`-set `N_S(U)`.

For completeness, the complementary matching follows directly rather than
from an implicit bag-level assertion.  For nonempty `Y subseteq C-U`, apply
relative connectivity to `U union Y`.  Since

```text
|N_C(U union Y)| <= 7-i-|Y|,
```

one obtains

```text
|N_S(Y)-N_S(U)| >= |Y|.
```

Hall therefore matches the `7-i` individual vertices of `C-U` bijectively
to the `7-i` roots outside `N_S(U)`.

The deficient family is nonempty.  It cannot have order five: then all five
spanning model bags would be singleton bags and could not partition seven
vertices.  Hence `1<=i<=4`, exactly the four cases cited in the source.

## 3. Assumptions passed to the four terminal branches

For `i=1`, the Hall equalities make the unmatched singleton root-invisible
and universal to `C-{u}`.  The complementary six vertices are perfectly
matched to `S`, while the other four old model bags partition them and have
at most one missing mutual contact.  They therefore form the required
spanning ordinary `K_4^-` model.  These are precisely the inputs of the
pinned `i=1` theorem; `eta_S(C)>=6` is used here and nowhere else.

For `i=2`, minimality makes the unique root in `N_S(U)` adjacent to both
singleton poles and no other root adjacent to either.  The other five
vertices have their complementary perfect matching.  The three remaining
old bags have connected quotient, so their union induces a connected
five-vertex complement.  Relative connectivity gives each pole internal
degree at least five.  These are exactly the pole-and-tree theorem's
hypotheses; no excess or packet condition is imported silently.

For `i=3`, the profile gives three singleton Hall vertices, two deficient
roots, four complementary vertices and roots, collective domination of the
complement, and the two remaining connected model bags.  Minimality gives
the two-root Hall path used by the pinned classifier.  Its sole target-free
internal residual has each Hall leaf adjacent to only three shore vertices;
all its root neighbours lie in the two-set `N_S(U)`.  Thus its total open
neighbourhood has order at most five, contradicting (1.1).

For `i=4`, the four deficient bags are singleton vertices and the fifth bag
is the connected three-vertex complement.  Collective domination says each
complementary vertex has a neighbour in `U`.  The original quotient says
that the number of missing edges in `U` plus the number of members of `U`
anticomplete to the complementary bag is at most one.  Together with the two
Hall matchings, these are exactly the inputs of the fourteen-row
four-plus-three theorem.  It requires no additional excess, packet, or
relative-connectivity assertion after this return.

Thus every matched outcome and every possible deficient outcome returns a
punctured rooted `K_5^-` model.  The local theorem does not extrapolate any
of the finite case results beyond shore order seven.

## 4. Independent reproduction

I reran all four pinned checks.  The `i=3` verifier was rebuilt with

```text
cc -std=c11 -O2 -Wall -Wextra -Werror -pedantic
```

before execution.  The terminal records were

```text
total_labelled_survivors=720 all_have_7_edges
order-seven i=1 core classification: PASS

joined template counts={'A': 46, 'B': 14}
joined orbit rows=15 coverage=60 witnesses=PASS
order-seven i=2 direct completion: PASS

shape(3,1): supports=5391 matching_failures=0
shape(2,2): supports=4032 matching_failures=24 exact_coloured_failures=24
residual_orbits=1 representative=0x69e33 one_edge_failures=0
order-seven i=3 internal classification: PASS

K4: valid=3221 minimal=60 orbits=3
K4-minus-edge: valid=2161 minimal=48 orbits=11
order-seven i=4 completion table: PASS
```

These runs agree with the scopes used in the synthesis: the first branch
uses the excess threshold, the next two use relative connectivity, and the
last is terminal from the Hall data alone.

## 5. Stabilising the boundary and the `K_7^-` composition

Deleting edges internal to `S` changes none of `C`, `e(C)`, `e(C,S)`,
`eta_S(C)`, the ordinary minor, or any neighbourhood of a set
`X subseteq C` inside `(C-X) union S`.  It makes `S` stable, as required by
the local theorem.  The rooted model found in this edge-deleted graph is
also a model in the original graph.

Six-connectivity gives (1.1): if a nonempty `X subseteq C` had fewer than
six neighbours in `(C-X) union S`, removing those neighbours would separate
`X` from either the remainder of `C` or, in every case, from the two other
components of `G-S`.

Let the rooted five-bag model omit `x`, and choose two other connected
`S`-full components `A,D`.  The bags

```text
A union {x},       D
```

are connected and disjoint from one another and from the five old bags.
Each contacts every old bag through that bag's literal root.  Since `D` is
`S`-full, it has an edge to `x`, giving the contact between the two new
bags.  The seven-bag quotient therefore has no missing pair beyond the one
possibly missing in the rooted `K_5^-` quotient.  It is a `K_7^-` model in
the original host.

This contradiction proves the integer conclusion `eta_S(C)<=5`.  No edge
inside `S`, unproved contact between distinct open components, or fourth
component is used.

## 6. Scope verdict

No Hall, hypothesis-transfer, boundary-deletion, dependency, or branch-set
composition defect was found.  The synthesis correctly eliminates every
order-seven, excess-at-least-six lobe containing an ordinary `K_5^-` minor.
It does not treat larger shores, order-seven shores without such a minor, or
prove the unbounded coefficient-four theorem, Conjecture 21, or `HC_7`.
