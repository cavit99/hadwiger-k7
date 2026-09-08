# Internal audit of the matching quotient and coupled colourings

**Verdict: GREEN.**

No gap was found in Theorems 1--2 or their stated
scope. This is a separate internal mathematical audit, not external peer
review or completion of Conjecture 19, HC7 or the two-triangle case.

The complete [source](hc7_two_triangle_matching_colour_host.md) was checked
at SHA-256 `2e20d9ec5ad9e8ed918b43ee8a30718f4b096cf460ab125d4a8ff7de220629ae`.
The mathematical text was first read at
`ec6fc709bc59e592ea55f5996e3a69f3119e7d24f462892f072cd5c68f9b562d`;
reversing only the final status sentence exactly recovers that hash.
No mathematical source change was requested or made during this audit.

## Inputs and independence

Both invoked source statements were reread, and both source/audit pairs
match the exact hashes printed in the audited source:

- Contraction closure: source
  `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`,
  audit `26b2f5ad7226c7bb3f194cac8523f043d7ae6ca955036249f04ddc9fb6d94394`.
- Two-triangle exterior: source
  `e51564c9ffd857d15eb3d1de9c5cfa4ce9b9bfac514ac3188ac5379e2a745776`,
  audit `5ff953f5f2b019fee85fb810af8619bae929f8dbd12559ccb01a6f4b1fbeb50d`.

The new matching-colouring argument was independently checked from its
complete written proof. The inherited results have the internal audits
just identified; no fresh primary-literature inspection or finite
enumeration is claimed as part of this verdict. The legacy parity note
is not a dependency.

## Strongest inference checks

**Actual pairs and chromatic number.** Connected-set contraction closure
first limits the joint x/y contacts into each triangle, then limits all
A--B edges to at most one. Thus the selected six endpoints induce exactly
the two stated possibilities and admit an independent transversal of the
three actual matching edges. A hypothetical five-colouring of H expands
with only those three edges monochromatic. Recolouring a transversal with
a new sixth colour repairs every one, preserves all other edges and v,
and contradicts the original chromatic number. Hence chi(H)=6.

**Connectivity and degrees.** A cut of at most three vertices in F lifts
with v to at most six original vertices, except for all three pair roots.
That exception leaves W+a+b connected by the exterior theorem. Two A
contacts at a W vertex forbid every other neighbourhood contact outside
A; the same holds for B. Therefore no W vertex loses a neighbour in two
different matching contractions, and deleting v costs it nothing. The
selected endpoint avoidance and the unique possible A--B edge prevent
extra losses at the three merged vertices. The untouched vertices a,b
lose at most the three neighbours counted in the source. These arguments
give precisely the displayed lower bounds; they do not assert criticality
of either quotient.

**Exact four-boundary lift.** For nonempty X in W, a four-vertex F-boundary
expands to at most seven actual vertices. Since v survives and misses X,
seven-connectivity forces all three pair roots into that boundary and
both endpoints of every pair into its original lift. If the fourth
vertex were a or b, X would have no W-boundary; connectedness would force
X=W, contradicting fullness to the other untouched root. The remaining
vertex is therefore in W-X, as claimed.

**All colourings and transversals.** One fixed five-colouring of F expands
to the stated edge-deleted graph and restricts properly for every
independent transversal T. For each such T, four colours on G-v-T would
extend using separate fresh colours on T and v. In every five-colouring,
T can instead take a sixth colour; a repeated colour on the five actual
remaining neighbours would free an old colour for v. Thus the claimed
chromatic number and universal rainbow assertion both hold. A Kempe swap
between disconnected root components also frees an old colour for v,
forcing each required bichromatic path. These are proper endpoint-coloured
schemes; no minimum degree of their selected path unions is needed.

Every original pair preimage remains fixed and disjoint. The proof does
not unite paths from different transversals, invoke K5 contractibility,
or obtain Q by separating a contracted pair inside an arbitrary model.
The chi(F)=6 branch and the simultaneous minor allocation remain open.
