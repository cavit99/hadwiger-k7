# Internal audit: cross-edge paired-donor gate

**Verdict:** GREEN.  Two independent cold readings verified the
single-edge paired-response theorem, fixed-boundary core arguments, joint
boundary identity, private-inflation minimisation, conditional near-clique
absorption, and the stated five-centre nonclosure.  This note does not
close the two-cut branch.

This is separate internal mathematical review, not external peer review.

**Audited source:**
[`hc7_k7minus_five_centre_paired_donor_gate.md`](hc7_k7minus_five_centre_paired_donor_gate.md)

**Source SHA-256:**

```text
a5be155bf2ab3278727fbcbcb1e37190395aa747e48283308befe586a8625206
```

## 1. Single-operation quantifiers

For a proper six-colouring of `G-e`, non-six-colourability forces the two
ends of `e` to have one colour.  Deleting a donor containing one end
removes the only possibly monochromatic edge, so the induced boundary
partition is proper and is realised by the exterior.  Extension through
the donor side would glue to a six-colouring of `G`.

The converse is also exact.  A set containing neither endpoint either has
both endpoints in its boundary, making the induced partition improper, or
admits the restriction of the fixed colouring as an extension.  Two
disjoint genuine donors therefore contain different endpoints of `e`.
The theorem is correctly restricted to a single-edge deletion; it makes no
claim about a common deletion of two or more edges.

## 2. Fixed-list cores

For each donor, a minimal non-list-colourable induced subgraph is connected
and contains the appropriate endpoint.  The component construction inside
the model bag gives a connected core hull with nonempty connected
complement.  It stays inside the old donor, retains the named anticomplete
far bag and the same fixed trace, and preserves every condition imposed on
the growing complement.  Conditions imposed on the donor itself may be
lost, as the source explicitly records.

For the union of the two donors, the lists remain tied to the original
joint boundary.  If a minimal joint obstruction omitted one endpoint, the
fixed colouring would colour that obstruction: the only monochromatic edge
is internal to the full donor union and is then absent.  Thus both endpoints
belong to every minimal joint core.  This conclusion would not survive an
unannounced relocalisation of the lists, and the source states that limit.

## 3. Joint boundary and minimisation

The three sets

\[
 T_1\cap T_2,\qquad T_1\cap Y_2,\qquad T_2\cap Y_1
\]

are pairwise disjoint, and removing the two cross-incidence sets from
`T_1 union T_2` gives exactly `N(Y_1 union Y_2)`.  The displayed cardinality
formula follows.

For an admissible replacement `H_i`, every new boundary vertex is either
already in `T_i` or belongs to `Y_i-H_i`.  If all new vertices also
belonged to `T_j`, then

\[
                       N(H_i)\cup T_j\subseteq T_i\cup T_j.
\]

A strict inclusion improves the first lexicographic coordinate, while
equality and `H_i subsetneq Y_i` improve the second.  Hence an admissible
proper replacement has a new boundary vertex outside `T_j`; that vertex is
a discarded same-bag vertex anticomplete to the other donor.  The stated
three-way fork is therefore precise.

## 4. Conditional absorption

Under Theorem 4.1's explicit assumptions, the enlarged set `X'` and six
residual model bags are a connected partition.  If their contact graph has
at most one nonedge, they are the promised `K_7^-` branch sets.  Otherwise
the six residual bags' internal near-clique condition forces a missing edge
incident with `X'`.  The missed residual bag is a common far side for the
connected donor union, so its open neighbourhood is an actual separator.
Seven-connectivity gives order at least seven and fullness at equality.
The original colouring is proper outside the donor union and its boundary
partition is rejected inside, proving the response assertion.

## 5. Application and exact limits

The audit checked the unique-owner source directly.  It supplies one donor,
not two donor-eligible pieces containing the ends of one interbag edge.  Its
two canonical simultaneous sets lie in one bag and need not be adjacent,
have connected joint complement, or share a far bag.  Nor does an arbitrary
edge-deletion colouring retain the original equal/distinct `pq` response.

For donors in two ordinary owner bags, their joint boundary meets at most
the two corresponding centres, so it cannot itself be the five-centre
boundary required for minimum-side descent.  At exact order seven, fullness
comes from the donor theorem and the exactly-two-component conclusion from
the separately audited three-component seven-cut exclusion.  Neither
supplies the missing centre labels or response orientation.

The source correctly records a failure of the available proof mechanism,
not a counterexample to the full cross-edge supply theorem.  The common
multi-edge-deletion possibility, the two-cut branch, the Five-Centre
Exclusion Theorem, Conjecture 21 and `HC_7` all remain open.

## 6. Unresolved assumptions

None for Theorems 1.1, 3.1 and 4.1 or Propositions 2.1--2.2 as stated.
The host-level paired-donor supply theorem is not proved and is not assumed.
