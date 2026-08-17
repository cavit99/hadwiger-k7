# Cold audit: returned two-component contraction and cross-shore composition

**Verdict:** **GREEN for the stated nonterminal results.**  The clique-
completion lemma, exact contraction-cut classification, density handoff,
`K_7^\vee` lift, six-connected near-model descent, pole constraints,
cross-shore rooted-helper composition, and equality witness all check.
Nothing in the source eliminates the full two-component row or claims the
Norin--Totschnig significance benchmark.

This is a separate cold mathematical pass, not external peer review.

## Audited revisions

| file | SHA-256 |
|---|---|
| [`hc7_k7minus_returned_two_component_contraction_descent.md`](hc7_k7minus_returned_two_component_contraction_descent.md) | `87fdc55007f32622a11f5050d6f0e9719e45af95c1e7e2d86f480a4a3a1338e3` |
| [`experiments/returned_two_component_equality_witness_verify.py`](experiments/returned_two_component_equality_witness_verify.py) | `e7960a8c3738ac3cb3c1f621a221db21cf94c5e7f1fa0a1fe2cc7df9896a2c56` |

Relevant audited local dependencies were also pinned:

| dependency | SHA-256 |
|---|---|
| fifth-root source | `81306114489449f1bd2d8521c4aefc216411f81bf6721c7763412d4a7a87c6c0` |
| fifth-root audit | `924d89d2a7c7645b9834a125d5851a342640a5c8aeb68f0c6acc667d435af1b2` |
| exact `K_7^\vee` separator source | `4845f5375581971aca7397bbac0e3eb930dd2943c9dca71f6264a24e2fa31c6e` |
| exact `K_7^\vee` separator audit | `9e6e3bae9e74429729ec8b06b8a9f6d932125135c0e0b8a7c92c660e3313767c` |
| Lo robustness source | `989b26475e5e3062cc880a1e2aba735b1c1b707e4e32f72aca553a2b337583dc` |
| Lo robustness audit | `8bbcf734970cd3fbb3829fcb95535c2d0b53754d3d147e2274d9c8c478372670` |

## 1. Primary-source hypotheses

The Norin--Totschnig paper was checked at arXiv:2507.03244v1.

- Its Theorem 6 says exactly that a four-connected graph `H` with
  `|E(H)|>=4|V(H)|-8` contains `K_7^\vee` as a minor unless
  `H` is isomorphic to `K_{2,2,2,2}`.
- Its Lemma 12 says exactly that, for a four-set `Z`, an internally
  four-connected pair `(H,Z)` with no `Z`-rooted `K^*_{4,2}` model has
  at most `4|V(H)|-10` edges.  The source uses four distinct root bags,
  two helper bags, all eight root--helper contacts, and the helper--helper
  contact.  No root--root contact is required.

These are precisely the forms used in Theorem 6 and Theorem 9 of the
audited source.  In particular, the strict integer inequality in Theorem 9
reaches the contrapositive threshold `4|V|-9` exactly.

Lo's Theorem 1.3 was checked at arXiv:2603.27973v1.  It states that every
four-connected non-planar graph of minimum degree at least five contains
`K_6^-`, and also contains `K_{3,4}` unless it is `K_6`.  Proposition 6.1
uses a five-connected graph of order at least eight, so every hypothesis
and the exception check are valid.

Primary sources:

- Sergey Norin and Agnès Totschnig,
  [*Every graph with no `K_7^\vee` minor is 6-colourable*](https://arxiv.org/abs/2507.03244),
  Theorem 6 and Lemma 12.
- O.-H. S. Lo,
  [*A characterization of graphs with no `K_{3,4}` minor*](https://arxiv.org/abs/2603.27973),
  Theorem 1.3.

## 2. Clique completion

After deleting a set `X` of at most five vertices from a closed lobe, the
completed boundary `S-X` is a nonempty clique.  For each component `K` of
the deleted lobe,

```text
N_G(K) subseteq (X cap C) union S.
```

Its open neighbourhood separates it from the opposite component, so it
has order at least six.  At least `6-|X|` of those neighbours survive in
`S-X`.  Thus every surviving lobe piece attaches to the same boundary
clique.  This proves genuine six-connectivity, including the endpoint
`|X|=5`.

If the opposite component is first contracted, the same proof works when
the pole survives and reduces to the preceding proof when it is deleted.
The resulting pole plus completed boundary is indeed a literal, but
virtual, `K_7`.  The source correctly refuses to lift it: a single full
component does not realise arbitrary pairwise boundary contacts.  The
singleton-component example is enough to refute that bare inference.

## 3. Exact quotient cuts

Let `d` be the contracted component.  A cut of order at most four which
avoids `d` would also separate the original graph: every surviving
boundary vertex is already in the component containing `d`, and splitting
`d` adds no edge to the retained open component.  Hence every small cut
contains `d`, and deleting `{d} union Z` leaves literally the retained
closed shore minus `Z`.  This proves both the four- and five-connectivity
tests in Lemma 3.

For `|Z|<=2`, every component of the retained open shore minus `Z` has at
least `6-|Z|>=4` surviving boundary neighbours.  Two closed-shore
components containing retained-shore vertices would therefore require at
least eight distinct boundary vertices.  Unless the whole retained shore
was deleted, there is exactly one such component and every other component
is boundary-only.  The main component consumes at least `6-|Z|` of the
`6-|Z cap S|` surviving boundary vertices, leaving at most `|Z cap C|<=2`.
This proves the order bound on `R`.

All neighbours of `R` outside the opposite component lie in `Z`.  Since
`N_G(R)` is an actual separator, six-connectivity gives

```text
|N_D(R)| >= 6-|Z|.
```

At `|Z|=1`, the counting forces one deleted retained-shore vertex, one
boundary vertex in `R`, its unique possible retained-shore neighbour, no
other boundary neighbour, and at least five opposite-shore neighbours.
At `|Z|=2`, `R` is a singleton or edge with at least four opposite-shore
neighbours.  The analogous `|Z|=3` count leaves only the stated
complementary `3+3` split when there is no boundary-only component.  No
connectivity claim stronger than these alternatives is made.

## 4. Density and the exact `K_7^\vee` lift

The quotient accounting was recomputed independently:

```text
n(H_C)=|C|+7,
m(H_C)=4|C|+eta(C)+e_S+6,
m(H_C)-(4n(H_C)-8)=eta(C)+e_S-14.
```

The two quotient surpluses sum to `e_S+s-4`.  More importantly, direct
averaging of `eta(A)+eta(B)=24+s-e_S` shows that one quotient reaches the
`4n-8` threshold already at `e_S=3`; the endpoint is equality.

If that quotient is not four-connected, Lemma 4 applies.  A dense
singleton retained shore is impossible because its excess is two and
`e_S<=11`.  A retained shore of order two is an edge, has excess
`p-7`, and the inequalities give exactly `e_S>=9` and
`p>=21-e_S`.

If the quotient is four-connected, Norin--Totschnig Theorem 6 applies.
In the exceptional `K_{2,2,2,2}`, the degree-six pole and its sole
non-neighbour are partmates.  The other six vertices induce
`K_{2,2,2}` with twelve edges, contradicting `e_S<=11`.

The model lift is safe.  The quotient is already a target-free minor of
`G`, so neither of the two absent centre contacts can appear while unused
components are absorbed to make the model spanning.  Replacing the pole
inside its bag by the connected component which it represents preserves
bag connectivity and every old contact.  If fullness creates either
absent contact, only the other remains absent and the result is `K_7^-`.
Thus target exclusion makes the spanning lifted model exact.

For `e_S<=2`, the maximum-excess quotient has respectively at least
`4n-10` or `4n-9` edges.  In the five-connected branch, order at least
eight and `4n-10>3n-6` give non-planarity and Lo applies.  The source
correctly labels both returned minors as unrooted and nonterminal.

## 5. Six-connected near-model descent

The earlier audited proof was rechecked with connectivity lowered by one.
The only numerical use of seven-connectivity in that proof is the first
pigeonhole step.  Here `N(X)` is an actual separator and has at least six
vertices spread among four neutral bags, so one neutral bag still contains
two distinct `X`-portals.

The retaining-core transfer is valid: the donor complement is connected,
retains all five foreign contacts, and moving the selected component into
a twin repairs one centre--twin nonedge.  If the piece misses both twins,
its open neighbourhood is an actual separator.

In the unavoidable-core branch, the two opposite gates are nonempty,
connected, disjoint, and have disjoint nonempty monopoly sets.  If neither
gate returns a separator, both meet both twins, so neither twin is
monopolised.  Two disjoint nonempty monopoly sets among only three neutral
labels force one set to have order one.  Moving that gate into the centre
loses at most one contact and yields the target.  At separator order six,
a missed component contact would leave a five-cut, proving fullness.

Thus Lemma 5 is GREEN at connectivity six.

## 6. Pole position and splitting

The pole-position claims are immediate but target-sensitive.  The lifted
component is adjacent to every boundary vertex.  If it lies in the
deficient bag, either twin containing a boundary vertex repairs one of the
two absent pairs.  If it lies in a twin, a boundary vertex in the deficient
bag does the same.  A neutral pole bag repairs neither missing pair merely
by gaining contacts, so no stronger conclusion is asserted.

For Lemma 8, the five selected external bags really form `K_5`: when the
pole bag is deficient use any five of the foreign `K_6`; when it is a twin
or neutral, omit the deficient bag.  The component `W`, singleton pole,
and external `K_5` then have every contact except at most one pole--external
contact.  This proves the split certificate.  The source now distinguishes
the quotient bag `R_H` from its lifted counterpart, so no bag-identification
ambiguity remains.

The simultaneous two-orientation paragraph claims only two separate exact
models and two separate residues.  It does not infer an unsupported
incompatibility.

## 7. Cross-shore rooted-helper composition

For the `A`-shore, completing the four roots `Z_A=S-{a,x}` gives

```text
4|A|+eta(A)-a_A(a)-a_A(x)+6 >= 4(|A|+4)-9.
```

The rooted pair is internally four-connected by adjoining the two omitted
boundary vertices to any forbidden separator.  Lemma 12 therefore returns
the rooted two-helper model.  Added edges have both ends at distinct roots;
they cannot lie within a branch bag, supply a root--helper contact, or
supply the helper--helper contact.  Deleting them preserves the model.

The five-root closed shore is internally five-connected by adjoining the
one omitted boundary vertex to a forbidden separator.  The pinned
fifth-root lemma puts `x` in a helper.  The symmetric construction puts
`y` in a helper on the `B`-shore.

Merging equally labelled bags is legitimate: the two bags intersect only
in their common literal boundary root, whilst all open-shore vertices are
disjoint.  The `x`-label is universal through the `A` model, the `y`-label
through the `B` model, and the other three labels form the assumed literal
triangle.  Hence the five labels form `K_5`.  Each residual helper meets
all five labels.  The residual helpers lie in opposite open components,
so their mutual pair is the sole missing pair.  This is an explicit
`K_7^-` model.

## 8. Equality witness and falsification scope

For a path of order `c`, the internal edge count `c-1` and attachment
vector `(c,c,c,c,1,1)` give excess `c+1`.  The strict supply inequality
holds only on the low--low pair.  Two aligned paths therefore have no two
distinct supply edges with a common endpoint, even though the displayed
boundary contains six triangles.

The checker was rerun with Python's standard library and returned

```text
GREEN returned two-component equality witness n=17 m=68 kappa=6
deletions_checked=9402 excesses=(6, 7) boundary_triangles=6
compatible_supply_triples=0 target_status=not_asserted
```

It checks every deletion of at most five vertices and checks that deleting
the six boundary vertices separates the two paths.  Its stated scope is
exact: it is a counterexample only to forcing compatible supply pairs from
the excess inequalities, not a target-free graph and not a counterexample
to the actual rooted-model statement.

## Final scope assessment

All numbered implications and all endpoint constants in the source are
GREEN.  The strongest output is an unbounded target-sensitive trichotomy
and an unconditional cross-shore composition lemma.  The source leaves
three genuine residues: a small dense lobe or pinned atom, density control
after the nested separator, and coupling the two pole-portal partitions.
These are not retrospectively described as a major theorem.  The stated
Norin--Totschnig benchmark disclaimer is accurate.
