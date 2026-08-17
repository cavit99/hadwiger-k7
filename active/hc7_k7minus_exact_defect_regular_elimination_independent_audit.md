# Independent cold audit: exact-defect regular elimination

**Verdict:** **GREEN**, subject to the finite-computation and imported-
theorem trust boundaries stated below.  The order-25 elimination, the
hexagonal-bipyramid propagation, and the mixed `8/9` corollary all follow
from the displayed hypotheses.  This is an independent internal audit,
not external peer review.

## Audited revision and reproduction

The audited theorem is
[`hc7_k7minus_exact_defect_regular_elimination.md`](hc7_k7minus_exact_defect_regular_elimination.md)
at SHA-256

```text
0750a839063730f515f17868677e8fca546011e540e22180a4d990b7b468e6c0
```

The verifier and reproduction note are:

```text
67fd89db3e97933a950dd1ad256c59141bfab3aec85ba8485014105981f20b95
  active/experiments/defect25_regular_elimination/verify.py
e351db441c640b651a24d0966fba32b0f6bcf8802efb3ae0e72e324ee4158b67
  active/experiments/defect25_regular_elimination/README.md
ff6a929a94dd162d2e3b08e25bf3b7aa7845b70b2511a15772f84776a122092c
  uv.lock
```

Using the repository virtual environment with NetworkX `3.6.1`, I ran

```text
.venv/bin/python -B \
  active/experiments/defect25_regular_elimination/verify.py
```

and independently reproduced

```text
GREEN defect25 regular elimination finite inputs: bases=1044 extensions=133632 eligible=352 exact_miss_profiles=12672 k5_minor_free=2 hexagonal=2; D26_static_survivor=GMs`KK misses=3,5
```

## Defect-25 contraction arithmetic

At order twenty-five, the critical-host inequality

```text
n_8 >= 25 + sum_{i>=10}(i-9)n_i
```

forces all vertices to have degree eight.  Thus `m=100` and
`9n-2m=25`.  Contracting an edge of codegree `c` removes `1+c` edges, so
the quotient has order twenty-four and `99-c` edges.  Edge contraction
lowers seven-connectivity by at most one.  Its order excludes the two
Jakobsen base graphs, and six-connectivity excludes a nontrivial
four-clique-sum cockade.  Therefore the strict inequality gives

```text
2(99-c) <= 9*24-25 = 191,
```

and hence `c>=4`.  For every centre `z` and neighbour `x`, this codegree
is exactly the degree of `x` in `G[N(z)]`, so every order-eight
neighbourhood has minimum degree at least four.

The imported exceptional-neighbourhood result supplies exactly the other
two properties used by the finite step: no `K_4` subgraph and independence
number three.  No global regularity is encoded in the verifier.

## Exhaustiveness of the finite step

Every order-eight graph is obtained by adjoining one vertex, with one of
`128` neighbourhoods, to an order-seven graph in NetworkX's complete atlas.
Repeated isomorphism types do not affect exhaustiveness.  Eligibility is
tested literally as

```text
delta(H)>=4,   K_4 not subseteq H,   alpha(H)=3.
```

For each of the `352` eligible extension representations, the verifier
tests all `36` unordered equal-or-distinct pairs of one-vertex misses.
The two component images are interchangeable.  A full attachment is
covered by deleting one attachment edge to obtain a tested exact-miss
spanning subgraph; restoring the edge cannot destroy a minor.  Thus the
`12,672` quotient profiles cover every pair of attachments of boundary
degree at least seven.

The minor engine begins with singleton bags and recursively deletes a bag
or merges two touching bags.  Merges preserve connectivity.  Conversely,
contracting a spanning tree in every desired connected branch set and
deleting unused vertices realizes any minor model, so the search is exact.
At seven bags, twenty of twenty-one contacts are precisely a `K_7^-`
model; at five bags, all ten contacts are a `K_5` model.  The positive and
negative controls exercise both predicates.

This verifies both finite conclusions: two exterior components force the
target, and the only eligible `K_5`-minor-free neighbourhood is, up to
isomorphism, `C_6 join overline(K_2)` (appearing through two atlas
extensions).

## Connected-full exterior and hexagonal propagation

Seven-connectivity makes every exterior component adjacent to at least
seven of the eight boundary vertices.  The finite quotient therefore
rules out two components.  If the unique exterior misses a boundary
vertex `r`, eight-regularity makes `r` complete to the other seven
boundary vertices.  Removing `r` leaves a triangle-free order-seven graph
of minimum degree at least three.  A vertex of degree at least four has an
independent four-vertex neighbourhood; if every degree is three, the odd
degree sum is impossible.  Both contradict `alpha=3`, so the exterior is
full.

A `K_5` model in the neighbourhood, together with the centre and the
connected full exterior, gives seven bags with only the centre--exterior
contact missing.  The finite classification consequently forces every
neighbourhood to be the hexagonal bipyramid.

In that graph the two pole vertices have local degree six and the six rim
vertices local degree four.  Hence the codegree-six edges form a spanning
two-factor.  Across a pole edge, both endpoints have the same six rim
neighbours, inducing a `C_6`; this set is constant along each pole cycle.
It follows directly that there are no rim edges within a pole component
and that any rim edge between two pole components makes them completely
adjacent.  Since pole cycles have order at least four and every vertex has
exactly six rim neighbours, each pole component is paired with a unique
component of order six, and symmetry makes its own order six.  Connectedness
then forces `G=C_6 join C_6`, of order twelve, contradicting order
twenty-five.

## Mixed degree-eight/degree-nine corollary

When `tau=0` and there are twenty-five degree-eight vertices, every other
vertex has degree nine and the same defect calculation remains valid at a
degree-eight centre.  A boundary vertex missed by the exterior has at most
eight possible neighbours, so it cannot have degree nine; the preceding
fullness and local-classification argument applies.

For pole edges with both ends in the degree-eight set `B`, the common
rim-cycle propagation remains valid.  Four consecutive vertices in a pole
path, together with the six rim-cycle vertices, give the seven displayed
bags in the theorem; direct checking leaves only the `b_3b_5` contact
possibly absent.  Thus every component of `P_B` is a path of order at most
three.  Each such path sends exactly two pole edges out of `B`, so at least
eighteen do.

If there were exactly two degree-nine vertices, all eighteen of their
degree incidences would be those pole edges.  Hence `P_B` has exactly nine
components, no rim edge leaves `B`, and the orders of the rim-adjacent
components at every fixed component sum to six.  The nine positive orders,
each at most three and with total twenty-five, have exactly two possible
multisets:

```text
3^8,1        or        3^7,2^2.
```

For `3^8,1`, the singleton must meet two order-three components; either of
those would then need five further rim neighbours in unions of order-three
components, impossible.  For `3^7,2^2`, an order-three component cannot
meet an order-two component: the equation `3u+2v=6`, with only two
order-two components available, forces `(u,v)=(2,0)`.  The two order-two
components would then see at most one another, giving only two rather than
six rim neighbours.  This disposes of the second multiset that an earlier
draft omitted.  Degree-sum parity makes the number of degree-nine vertices
even, so it is at least four.

## Trust boundary and scope

The imported audited inputs are frozen at:

```text
fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd
  results/hc7_k7minus_exceptional_neighbourhood_completion.md
26be60e5389ec356dfd183d8a39e2a713e6db3695c807674daf7797fa1fcae2b
  results/hc7_k7minus_exceptional_neighbourhood_completion_audit.md
421544721b5084fe5dff280cd2299f0e4cb214ba39bc2b2fde5648fc393bcd83
  results/hc7_k7minus_two_literal_k5_exclusion.md
4b482d74f6a70c5d00b3f29f261a53a91c48b75750975005fce06f150f69aa24
  results/hc7_k7minus_two_literal_k5_exclusion_audit.md
```

Jakobsen's extremal theorem is used only through the already audited
non-cockade inequality.  The independent audit did not re-prove that
external theorem.

The `D=26` cubic survivor is correctly labelled a local route nonclosure,
not a critical-host counterexample.  The theorem eliminates order
twenty-five and the first mixed `8^{25}9^2` distribution, but it does not
eliminate the full `tau=0` layer and does not prove Conjecture 21 or
`HC_7`.
