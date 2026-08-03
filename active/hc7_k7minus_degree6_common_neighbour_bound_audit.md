# Audit: degree-six common-neighbour bound

**Verdict:** GREEN.

**Audited source:**
`active/hc7_k7minus_degree6_common_neighbour_bound.md`

**SHA-256:**
`e157c0e8fa5805cee15888abb9a002d35d51d7e877154e7eee1a37627732493e`

## Statement checked

The source proves that a five-connected graph `H` on at least nine vertices
with no `K_7^-` minor, a degree-six vertex, and at least four common
neighbours on every edge satisfies

```text
|E(H)| <= 4|V(H)| - 9.
```

## Claim-by-claim check

1. For `z in N(v)`, every common neighbour of `v,z` lies in `N(v)`.
   Hence the four-common-neighbour hypothesis makes the complement of
   `H[N(v)]` a matching.

2. Two disjoint paths filling two distinct matching non-edges leave at most
   one missing adjacency among the seven bags consisting of `{v}` and the
   six neighbourhood vertices.  This is an explicit `K_7^-` model.  Thus
   the proof does not import the stronger `K_7^vee`-exclusion used in the
   source paper.

3. Five-connectivity gives at least five attachments from every component
   outside `N[v]` to `N(v)`.  The pigeonhole uses in the proof are exact:
   five vertices among three pairs contain both ends of two pairs, and four
   vertices contain both ends of at least one pair.

4. If all three missing pairs have an exterior common neighbour, either two
   different common neighbours give disjoint length-two paths, or the common
   neighbour is shared.  In the latter case `|V(H)|>=9` leaves another
   vertex outside `N[v]` and the shared common neighbour.  A component there
   supplies the second disjoint path.

5. The separation argument is precisely Norin--Totschnig Claim 3.15.  The
   five prescribed paths follow from the set-to-set form of Menger's
   theorem.  In the two-paths theorem, the crossing outcome fills two
   matching non-edges, and its separation outcome lifts to a cut of order at
   most four in `H`.

6. In the disk outcome, an edge on the open side cannot have three common
   neighbours in the disk: nested triangles would separate a vertex from
   the four boundary terminals.  Restoring the deleted separator vertex
   raises the common-neighbour count by at most one.  This is the second and
   only other use of the four-common-neighbour hypothesis.

7. In the final application of the two-paths theorem, a separator of order
   at most three lifts, after restoring `u_1,w_1`, to an order-at-most-five
   separation with `N[v]` on one side.  Five-connectivity and the preceding
   separation exclusion rule it out.

8. The outer-face edge bound and final accounting are correct.  If
   `n'=|V(H-{v,u_1,w_1})|`, then

   ```text
   (3n'-7) + (n'-4) + 12 + 2 = 4n'+3 = 4|V(H)|-9.
   ```

## Hypothesis audit against the published proof

The adapted portion is Claims 3.12--3.15 and lines 471--475 of Norin and
Totschnig's proof of Theorem 6.  That portion uses:

- order at least nine;
- five-connectivity;
- a degree-six vertex;
- the four-common-neighbour property; and
- exclusion of the explicit `K_7^-` model in the two-pair observation.

It does **not** use minor-minimality, edge-maximality, the equality
`|E(H)|=4|V(H)|-8`, or exclusion of every `K_7^vee` minor.  Those stronger
hypotheses are used earlier in the published proof to derive the listed
local properties, not inside this degree-six subargument.

## External trust boundary

The proof invokes the Robertson--Seymour--Thomas two-paths theorem in the
form quoted as Theorem 13 by Norin and Totschnig.  The audit checks the
hypothesis transfer and both uses of its three outcomes, but does not
reprove that external theorem.

No unresolved mathematical gap was found.  This theorem is a conditional
local bound; it does not establish that an arbitrary extremal enemy has the
four-common-neighbour property.
