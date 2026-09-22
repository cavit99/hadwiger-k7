# Audit: the whole two-triangle degree-seven neighbourhood case

Date: 22 September 2026.

**Verdict: GREEN for the stated structural alternative and the entire
original-host consequence, including both chromatic branches.** The
reviewed [source](hc7_two_triangle_case_closure.md) has SHA-256
`4d28c778b4eb668a0b322f6f8b989af75aaab510aad9ced7f7a141722349b1d4`.
No unresolved inference was found in this implication chain. This is a
fresh separate internal reconstruction, with an additional independent
reconstruction of the earlier dependencies, not external peer review.
The theorem closes this one degree-seven neighbourhood configuration.
It does not close the other degree-seven configurations, degrees eight
and nine, or HC7.

## Review and promotion provenance

The original reviewed source was
the pre-promotion draft, SHA-256
`018b597756c847b0f9df9502b4ddb90919c4c1c4bd28e5b5630de297d76b0cf5`.
Its new two-connected dependency was originally reviewed at SHA-256
`992c31e7deb7f7e0dd9bc4a137ca2228ff6fa47c64b6a42320b2591ace17ac83`.
On 22 September 2026 both proofs and their adjacent audits were promoted
into `results/`. The reviewer inspected the complete source diffs:
only status wording, relative/navigation links and the now-discharged
pending-audit qualifications changed. No mathematical statement,
construction, case, count or lift changed. The verdict applies to the
promoted source hash above and dependency hashes below.

## Exact statement audited

Let J be a finite simple five-connected graph with an ordinary K5 minor
and two vertex-disjoint anticomplete literal triangles P,Q. Put
T=P union Q. Suppose every nonempty X contained in V(J)-T has at least
six distinct neighbours outside X. Then J has a K5 model whose five
branch sets each meet T, or J-z is planar for some z outside T.

Consequently, if a finite simple seven-connected graph G has chi(G)>=7
and a vertex u with exactly seven neighbours P union Q union {r}, where
P,Q are anticomplete triangles and r is adjacent to every vertex of
P union Q, then G contains a K7 minor. The conclusion uses precisely
these premises; contraction-criticality is not required.

## Immutable proof dependencies

All four mathematical dependencies were read at the following hashes.
The first three had adjacent internal audits before this review. Their
proofs were freshly reconstructed; their prior verdicts did not replace
that reconstruction. The fourth received its new adjacent audit as part
of this whole-chain review.

| Proof | SHA-256 |
| --- | --- |
| [Extremal prism](hc7_two_triangle_extremal_prism.md) | `8d617e35d5bc6fac0f25b5f418c6f35e976d282d883401199084e15c6d258222` |
| [Path-containing web cell](hc7_two_triangle_web_path_cells.md) | `21d22e189e0cb1e0f5a536aec3267577645bc8c37af94a888dbb3f3098ae4e50` |
| [Cutvertex exclusion](hc7_prism_remainder_cutvertex_exclusion.md) | `dfe9546cf960a39eb6b87f1d18f70bc3ee8c4200e6b3e046a4bd81c2855ad42c` |
| [Two-connected cell exclusion](hc7_prism_two_connected_cell_exclusion.md) | `b765f99f798f0251bf2c152011cc637ede2d6bd091b125b0064f969e7ec7c84c` |

The primary external statements were inspected again during the separate
dependency reconstruction. Costalonga--Zhou,
[*Triangle-roundedness in matroids*, Theorem 4](https://arxiv.org/html/1711.01618v3),
applies to a three-connected graph with a specified literal triangle
and an ordinary K5 minor. It retains the triangle's three original
edges as a triangle in a K5 minor, so its original vertices occupy
distinct branch sets. Fabila-Monroy--Wood,
[*Rooted K4-Minors*, Lemmas 2 and 7](https://arxiv.org/html/1102.3760v1),
give respectively the ordered spanning web when the opposite linkage
is absent and the rooted K4 when the specified cycle and linkage are
present. Neither use here needs an unstated connectivity hypothesis.
Their published theorems are external inputs, not independently
reproved in this audit. The original-host consequence also uses the
classical K5 case of Hadwiger's theorem and the Four Colour Theorem.

## Reconstructing the structural chain

Exclude both desired alternatives. Four-connectivity follows from
five-connectivity, so the extremal prism theorem applies with its
ordinary-minor and no-T-meeting-model hypotheses intact. Its initial
normalisation truly spans J: transferring a nonroot helper-contact
leaf preserves the triangle-root contacts while enlarging the helper
union; maximality and a separator of at most three vertices force
singleton P bags. The block-projection separator then forces the Q
block to be Q itself. Subsequent one- and two-vertex boundary arguments
show that every remaining component is the asserted induced rail.
Thus no omitted vertex or attachment is discarded in passing to E,S.

Every root has exactly three neighbours in S and degree at least five,
so it has at least two E-neighbours. Every rail-interior vertex has
exactly two S-neighbours; its root-free singleton has degree at least
six and hence four distinct E-neighbours. In particular |E|>=4.
Every vertex of E also has degree at least six. These counts supply all
later contact assumptions without criticality or a chromatic premise.

For every deleted rail R_i, a rooted K4 on the four surviving roots
would extend with R_i as a fifth bag. The actual cap edges provide its
contacts to all four root bags, and all five bags meet T. This proves
the forbidden-linkage and ordered-web premises for each H_i.

The path-cell proof applies to this exact partition and these contact
bounds. Its ownership argument treats arbitrary connected root-free
three-gate shores, not only cells. Cross-view intersection boundaries
account for both differently deleted rails. Its two clean-view patches
expose a common actual rail, and their outer root order permits the
two omitted cap edges after gluing. Hence a path-containing cell gives
J-z planar for some z in E, contradicting the excluded alternative.
All three fixed web completions are clean. The same proof gives
cross-view disjointness for all E-only shores of boundary at most three,
including disconnected whole cells.

The cutvertex exclusion now has every hypothesis, including
nonplanarity of J-z for every z in E. Its extension from a path cell
to an arbitrary three-gate rail-containing shore is justified by the
same ownership, complementary-shore and gluing arguments; it does not
assume the new shore was a cell. Its one-rail pocket argument represents
all complementary actual rail contacts, and the later ordering uses
the entire connected complement. The prefix and suffix separators
include cap exits even when a prefix or suffix is empty. Each cut has
a vertex on both sides. These arguments exclude every E-cutvertex.
Since E is connected with at least four vertices, J[E] is two-connected.

The new [two-connected audit](hc7_prism_two_connected_cell_exclusion_audit.md)
reconstructs the strongest remaining step in detail. In its pocket lemma,
the complement A has a visible vertex; each hidden actual A component
therefore has an A-gate. Projecting through only A-gates preserves every
actual A--rail contact at its original rail vertex while avoiding W.
A separate connected E projection puts W and this A projection on the
same side of the actual cycle. The W arc between extreme contacts
then excludes A from its pocket and the open boundary interval. The
final separator concerns actual vertices and includes all hidden gates.

For an actual cell component C, two-connectivity and the contact bounds
give at least two E-gates and at least four vertices in E-C. The
complement is connected with two gates. With three gates it is either
connected or is a connected two-gate component together with an isolated
third gate z. These are all gate distributions. The one-surviving-rail
gate case is excluded by actual opposite diagonals. In the isolated-z
case, absorbing z into the connected set used for those diagonals is
legitimate, and the final small-boundary set excludes z while counting
it once in its boundary. Its extra rail contacts cause no omitted exit.
Thus every actual cell is empty; no cofacial insertion is inferred.

Each actual H_i is now planar. Its connected E lies on one side of
the surviving-rail cycle; inducedness excludes cycle chords on the
other side. Taking that cycle as the outer face gives the three valid
disk bounds. Their sum is 3a+2d<=9e+2s-9, whereas the verified actual
degree bounds yield 3a+2d>=(3/2)(6e)+(1/2)(4s-12)=9e+2s-6.
This contradiction proves the structural alternative. No finite check,
induction, quotient or transferred criticality is involved.

## Original G: colouring and minor lift

Deleting u,r from a seven-connected G gives a five-connected J.
A four-colouring of J, with fresh colours on u and r, would six-colour
G. Therefore chi(J)>=5 and the classical K5 case of Hadwiger supplies
the ordinary K5 input. The argument makes no assumption that chi(J)=6.

For nonempty X contained in J-T, the exact neighbourhood of u ensures
that u has no neighbour in X. A J-boundary of size at most five, after
adjoining r, has size at most six in G. The vertex u remains outside
both X and that boundary, so this is an actual separator contradicting
seven-connectivity. This checks the quantified boundary condition for
all such sets, not only singletons.

In the first structural alternative, the five connected disjoint bags
lie entirely in J and each contains a T vertex. Both u and r are
adjacent to every T vertex, and ur is an edge. Adjoining the two
singleton bags gives seven connected disjoint pairwise adjacent bags.
There is no root-ownership or colouring compatibility gap in this lift.

In the second alternative, z lies outside T and also outside {u,r}.
The exact neighbourhood of u implies uz is not an edge. Four-colour
the planar J-z, give u,z a shared fifth colour, and r a sixth colour.
This colours every vertex and every edge of G properly, contradicting
chi(G)>=7. This step covers the previously separate five-chromatic
branch as well as the six-chromatic branch, and requires no
proper-minor colouring premise.

## Remaining scope

No unresolved assumption or gap was found beyond the explicit graph
hypotheses and cited external theorem inputs. The result rules out the
neighbourhood K1 joined to two disjoint triangles in any hypothetical
seven-contraction-critical counterexample, using its seven-connectivity.
It supplies no construction for the other degree-seven neighbourhoods,
degrees eight and nine, or the general HC7 target. It makes no priority
claim. Promotion changed only the metadata recorded above. Research-record
integration and validation remain separate steps.
