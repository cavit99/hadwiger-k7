# Internal audit: density localisation across the labelled six-boundary kernels

**Verdict:** **GREEN** for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.  The reduction remains
conditional on the selected minimum-`E5` setting and does not prove `(E5)`.

## 1. Audited revision and dependencies

**Audited source:**
`active/hc7_k7minus_e5_six_boundary_localisation.md`

**SHA-256:**

```text
7d3c5a9cb2e7e952cd026a5a104fe48d6ca504e7fcc89ba1bcc461ecc9978c50
```

The following exact dependency revisions were checked.

| dependency | SHA-256 |
|---|---|
| second-contraction reduction | `3218c292213fbf7e9cf6e7e6a38b2c3cef0c05801a4359cbd956a28daf3ef93e` |
| its GREEN audit | `8b1940800b9848d5c88cbca5449d1ce25e9ef831931206377150e629a2c5f9cf` |
| missed-root mass theorem | `3311e4640584e8223fc9c71c2cd22d7e06aabd7f65efa6ebd017fc1adc4d29e8` |
| its GREEN audit | `641dab5f1102d9cc5b5f57e73d53c9be936d45bc0df91d8c1a6730a661b82111` |
| finite extension theorem | `bfe0a330bbcefe655f8a7c853be4944a39adbadf810991cb0d4185552ae9094f` |
| its GREEN audit | `fb0061b16b485289069635d52054c72462a09d59f46a6756fc75a2d8ab561381` |
| sparse three-component reduction | `176910c63cfdd115ed0b1212b0588cd65e1892ef534e5eb7c3524a2b2b3badfd` |
| singleton-contraction classification | `e4720b2641033396aabf333cc97d9f401df4577f8a6f337a44d7ca6aba0ac1c2` |
| boundary-complement selection reduction | `6c881f87026f3116fa01749a1dc665dd93642a482a90ba37d404b83e2976db8e` |

The last three sources have adjacent GREEN audits at their current pinned
revisions.  Norin--Totschnig Lemma 9 was already checked directly in those
audits: an internally four-connected four-root pair with no rooted `K_4`
model has at most `3|V|-7` edges.

The imported kernel labels, shore orders, degree-five endpoint, exact excess
identities and selected data `(a,Phi,rho)=(a,11,2)` agree with the audited
second-contraction reduction.  In particular, direct substitution gives

```text
sum eta_P = 16-|E(G[P])|   for K_2 and P_3,
sum eta_P = 15-|E(G[P])|   for K_3.
```

## 2. Two six-full `P_3,K_3` components

The mass theorem bounds the number of six-full components by one in the
favourable orientation and three in the other orientation.  The finite
theorem excludes three and, after contracting two selected components,
excludes any additional component by retaining a full singleton minor of
it.  Its exact negative catalogue is precisely equation (2.1).

### Boundary degree one

The degree-five endpoint `u=1` has its boundary neighbour, the low centre
and three neighbours in the two six-full components.  Hence one component
contains two distinct `u`-neighbours `x,y`.  If there were no two disjoint
paths from `x,y` to distinct vertices meeting roots `3,4,5`, the two-set
form of Menger's theorem would give a separator of order at most one.  A
component containing one of `x,y` but no such portal could meet outside
itself only the separator and roots `u,0,2`, contradicting
five-connectivity.

The two paths can be extended along a spanning tree of the connected
component to adjacent connected parts partitioning it.  Both parts meet
`u`, and their combined portals to `3,4,5` occur on both sides.  Contracting
the parts and the other six-full component gives exactly a host in finite
Theorem 2.1(1).  Its target-free contact patterns put every portal to
`3,4,5` exclusively on one common side, so the constructed split is
positive.  All contractions are of connected sets and every encoded contact
is an actual edge; the finite minor model therefore lifts.

### Boundary degree two and the rooted compositions

Degree five forces one `u`-neighbour in each of the two six-full components.
Choosing the component of larger excess gives the two lower bounds (2.3).

For every omitted root `j`, each displayed three-bag list is connected and
disjoint from the four `Z_j`-rooted bags.  Its adjacencies were checked
explicitly:

- for `j=2`, the only possible missing pair is `{f_2}` with `D`;
- for `j in {3,4,5}`, the only possible missing pair is `{j,f_2}` with the
  rooted bag at `2`; and
- for `j=0`, the only possible missing pair is `{d,f_2}` with `D`.

In the last case `12` is present because boundary degree two at `u=1` in
the catalogue (2.1) forces it.  Thus any rooted `K_4` gives the target.

If the rooted pair is internally four-connected, Lemma 9 applied to
`G[C union Z_j]` gives the displayed inequality.  Writing
`e(C)+e(C,P)=4|C|+eta_P(C)`, using `p_C(u)=1` and
`p_C(j)<=|C|`, yields exactly

```text
eta_P(C)<=6-|E(G[Z_j])|.
```

If internal four-connectivity fails, adding `u,j` to a rooted separator
gives an exact five-cut.  At least one of the four roots in `Z_j` survives
the separator; together with the other six-full component and the connected
low kernel it lies in a central component of order at least three.  The
universal high-excess component therefore has order at least `a` in that
central side, leaving at most two vertices on all far sides.

A far edge has cut excess at most two because `C` has only one
`u`-neighbour.  Exact complement accounting then gives the central pair
`Phi=13-delta(far edge)>=11`; a strict inequality improves `Phi`, while
equality has `rho=1<2`.  The selected potential excludes the edge.  A far
component is consequently a boundary-full degree-five singleton, and it is
the unique `u`-neighbour in `C`.

For `P_3`, substitution in the eight catalogue boundaries makes every one
of the five rooted upper bounds strictly smaller than (2.3).  The five
returned singletons must therefore be the same unique `u`-neighbour and
would give it six boundary neighbours.

For `K_3`, the same strict argument closes boundary sizes two and four.  At
size three, the strict omitted roots are exactly those listed in the source.
If both remaining rooted pairs also failed, the same singleton would again
have six neighbours.  Hence one pair is internally four-connected.  Equality
forces both `eta_P(C)=6` and `p_C(j)=|C|` for a remaining root `j`, so that
root is universal on `C`.

Splitting a spanning tree edge of `C` gives the exact 162-pattern finite
hosts: root `1` has its unique contact in one part, the universal root meets
both, and every other root meets at least one.  The finite theorem forces the
relevant portal set to one common exclusive part for every tree edge.  If
two different vertices carried those portals, an edge on their tree path
would separate them, so all portals lie at one vertex, namely the returned
singleton `c`.  Its four already forced boundary neighbours and the
universal root exhaust degree five.  Since a connected component of order
at most two has excess at most five, `eta_P(C)=6` implies `|C|>=3`; `c` must
then have an internal neighbour, a contradiction.  Theorem 2.1 is correct.

## 3. `P_3,K_3` localisation

After Theorem 2.1 there is exactly one six-full component.  The aggregate
mass bound leaves, for any missed root, one full edge or at most two full
singletons.  The finite theorem excludes a full edge and two singletons with
the same missed root in both orientations under the exact degree constraints
forced at `u`.

In the favourable tied-twin case the five-cut has high component order `a`
and data `(Phi,rho)=(11,2)`, so it is another globally selected pair.  The
earlier three-component classification, which uses only the minimum-order
coordinate before this stage, applies and makes its five-boundary
`P_3` disjoint union `K_2`; this is exactly the finite tied-twin catalogue.

Thus any surviving missed root occurs for one singleton only.  Deleting the
other five roots leaves that singleton and the connected central component
proved in the mass theorem.  Corollary 3.1 and the favourable boundary
bounds are correct.  The corollary does not assert that no other singleton
lies inside the central side for a different choice of missed root.

## 4. `K_2` alternatives

With two six-full components, the fixed neighbours of `u=0` and one contact
in each component exhaust degree five.  Thus `01` is its only boundary edge
and any additional opposite component must miss `u`.  Retaining one vertex
of that component produces the forbidden singleton extension.  The finite
theorem then gives the seven-edge bound, its unique equality boundary, and
exactly one `u`-neighbour in each component.

With one six-full component, a singleton whose missed root is unique gives
the stated self-similar cut.  Two singletons with a common missed root can
only miss `u`; the selected tied-cut classification and finite tied-twin
screen exclude them.  A full edge meeting `u` would use two neighbours when
only one degree slot remains, so the sole non-self-similar extension is a
full edge missing `u`.  The exact finite catalogue gives equation (4.1).

That edge has excess three.  Equation (1.1) therefore gives
`eta_P(C)=13-|E(G[P])|`.  The catalogue (4.1) makes `01` the only boundary
edge at `u`; degree five then gives two contacts from `u` to `C`.  Hence, for
`Q=P-{u}`,

```text
|E(G[C union Q])|
 = 4|C| + 13-|E(G[P])| - 2 + |E(G[Q])|
 = 4|C|+10
 = 4|C union Q|-10.
```

Theorem 4.1 is therefore correct.  Its alternatives are deliberately
nonexclusive because a self-similar cut may place further components in its
connected central side.

## 5. Scope

The source eliminates multiple-six-full `P_3,K_3` shores and shores with no
six-full component.  It correctly retains every kernel-level survivor:

1. one unbounded six-full component in each of the three kernel families;
2. a self-similar singleton exterior;
3. the `K_2` one-six-full/full-edge equality; and
4. the `K_2` two-six-full family.

It also retains both branches which precede kernel formation: repetition of
the anchored singleton normal form, for which deletion terminates only at the
quotient level and loses the original endpoint-incidence history, and every
both-endpoints separation.  The latter is known only to have at most eleven
boundary edges; all rows with at most ten remain open.

No unbounded conclusion is inferred merely from a negative finite host, and
every positive finite model used above arises from contractions of connected
sets with the encoded contacts, so it lifts to `G`.  There are no unresolved
assumptions or gaps inside the reduction at the pinned source hash.  The
single-six-full, self-similar and both-endpoints branches remain open, as do
`(E5)` and the principal seven-connected theorem.
