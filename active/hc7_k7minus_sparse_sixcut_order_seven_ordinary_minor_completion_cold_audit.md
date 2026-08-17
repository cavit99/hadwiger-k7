# Cold audit: ordinary near-five minors at shore order seven

**Status:** separate internal cold audit.  This is not external peer review.

## Audited revision and verdict

The audited synthesis is
`hc7_k7minus_sparse_sixcut_order_seven_ordinary_minor_completion.md`,
SHA-256

```text
6005366ee90407ec9207fc3d07cc52dd84b28b9cfec254d2f583ed5c1e818a20.
```

Relative to the initially audited revision
`836535c3db469ab1b1965ba4d1570dd4881ff44ea5ce79ef888c9f0d552bb9b5`,
this final revision changes only the status line to record the completed
independent cold audit.  The local theorem, corollary, proof, dependency
pins and benchmark statement are unchanged.

**Verdict: GREEN.**  The spanning normalisation, Hall split, exhaustion of
the four deficient-family sizes, application of the four pinned terminal
theorems, and the returned-cut `K_7^-` composition are correct.  Every pinned
hash matches the named local artefact.  I found no unresolved assumption or
gap within the stated order-seven theorem and corollary.

## 1. Spanning normalisation and the Hall split

Let the five branch sets of the ordinary `K_5^-` model have union `M`.  Every
component of `C-M` has an edge to `M`: otherwise it would be a component of
the connected graph `C` disjoint from the nonempty set `M`.  Absorbing each
such component into one branch set that it meets preserves that branch set's
connectivity, preserves disjointness, and cannot destroy an old quotient
contact.  The resulting five branch sets therefore partition all seven
vertices, exactly as required by the order-seven Hall profile.

If the root--branch-set incidence graph has a matching saturating the five
branch sets, adjoining the five distinct matched roots makes each bag
connected and preserves its ordinary quotient.  This is already the desired
punctured rooted model.

Otherwise, take an inclusion-minimal deficient family `I`.  The pinned Hall
profile correctly gives

```text
|U|=|I|=i,       |N_S(U)|=i-1,       N_C(U)=C-U,
```

and hence makes every member of `I` a singleton branch set.  Minimality says
that `I-{u}` is Hall-sufficient for every singleton `u`; because both its
size and the available root set have order `i-1`, this gives the stated
perfect matching from `U-{u}` onto `N_S(U)`.  The complementary Hall argument
gives the vertex-level perfect matching from `C-U` to the other roots.

A deficient family is nonempty and contains at most the five model bags.  If
`i=5`, all five spanning model bags would be singletons and their union would
have only five, not seven, vertices.  Thus `1<=i<=4`, so the four listed cases
are exhaustive; there is no omitted fifth Hall profile.

## 2. Applicability of the four terminal theorems

For `i=1`, the Hall equations make the singleton universal to the other six
shore vertices and anticomplete to all roots.  The complementary six vertices
have a perfect matching to `S`, and the other four original branch sets give
a spanning ordinary `K_4^-` model there.  These are exactly the hypotheses of
the pinned `i=1` theorem.  This case, and only this case, uses
`eta_S(C)>=6`.

For `i=2`, the Hall data, the spanning five-bag model and relative-six
condition are precisely the inputs of the pinned pole-and-tree theorem.  It
returns the rooted model without an excess or packet assumption.

For `i=3`, the same Hall data give the three singleton deficient branch sets,
the two-root Hall path, the four-vertex complementary matching, collective
domination, and the two complementary original branch sets used by the
pinned internal-support theorem.  Its sole target-free residual has Hall
leaves of total degree at most five, so condition (1.1) excludes it.

For `i=4`, the four deficient branch sets are singletons and the fifth
original branch set is the connected three-vertex complement.  The Hall
matchings and quotient contacts are exactly those used by the pinned
four-plus-three incidence theorem.  That theorem needs no further relative,
excess or packet hypothesis after the Hall return.

Thus every matched or deficient Hall outcome produces the required rooted
model.  The synthesis does not infer an unbounded statement from these four
finite cases.

## 3. Dependency integrity and reproduction

I recomputed every SHA-256 listed in Section 3 of the synthesis.  All fifteen
hashes match exactly: the Hall theorem and its audit; the four terminal
theorems; their four verifiers; and the five listed case audits (two for
`i=1`, one for each of `i=2,3,4`).

I reran the four case verifiers.  Their terminal data were

```text
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

The `i=3` source compiled with the prescribed
`-std=c11 -O2 -Wall -Wextra -Werror -pedantic` flags before execution.  The
other three checks use only the Python standard library.

## 4. The returned-cut corollary

Deleting edges internal to `S` makes the boundary stable without changing
`C`, its ordinary minor, `e(C)`, `e(C,S)`, or `eta_S(C)`.  It also does not
change any `C`--`S` or internal-`C` neighbourhood used in (1.1).

Six-connectivity implies (1.1) here.  If a nonempty `X subseteq C` had fewer
than six neighbours in `(C-X) union S`, that neighbour set would separate
`X` from either `C-X` or, in all cases, from the other components of `G-S`.
The assumed two additional components make the far side nonempty.  This
would be a vertex cut of order at most five, a contradiction.

If `eta_S(C)>=6`, Theorem 1.1 gives five rooted bags using `S-{x}`.  Let
`A,D` be two other connected `S`-full components.  The additional bags

```text
A union {x},       D
```

are connected and disjoint from each other and the old five bags.  For every
old bag, its root in `S-{x}` has a neighbour in each of `A` and `D`, so both
new bags contact every old bag.  Since `D` is `S`-full, `x` has a neighbour
in `D`, giving the contact between the two new bags.  They are therefore
universal in the seven-bag quotient.  The old quotient has at most one
missing pair, so the seven bags form a `K_7^-` minor.  This contradicts the
hypothesis and proves the integer bound `eta_S(C)<=5`.

## 5. Scope and significance

The result completely closes the ordinary-`K_5^-` branch at shore order
seven and excess at least six, extending the previously proved order-at-most
six rooting theorem by the first nonliteral order.  It does not cover shores
of order at least eight, order-seven shores without an ordinary near-five
minor, the unbounded coefficient-four local theorem, Conjecture 21, or
`HC_7`.  The source states these limitations plainly and correctly places
the result below the campaign's primary Norin--Totschnig benchmark.
