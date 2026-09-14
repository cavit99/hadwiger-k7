# Independent audit of the local construction counterexamples

**Verdict: GREEN for all three stated counterexamples and the displayed exchange.**
None of the examples refutes the maximal-C construction, a separator-or-Q
alternative, Conjecture 19 or HC7. This is separate internal review, not
external peer review or a comparative-significance assessment.

**Source:** [vital_linkage_local_shortcuts.md](vital_linkage_local_shortcuts.md).

**Exact source SHA-256:**
`d1c8fb8a5ab6b19786db6d6f7382fa25d566fda4a0487f82794c84fc4893fa65`.

**Independence and revision.** On 14 September 2026,
`plan_objective_allocation` independently reconstructed all three examples and
their stated limitations. The reviewer did not construct these graphs.
The initial second section labelled its true negative conclusion as the
assertion being refuted. The pinned revision instead states the false
implication, and explicitly records the failure of proper-minor
six-colourability. These were exposition and scope corrections, not changes
to the constructions.
The additional colouring example was separately checked at the current hash;
the preceding two-example revision was pinned at
`6ada03b414c387c09e41a5aa66040cc00c491f1c4cdfebb241753cd1efadad90`.

## 1. The minimum separator need not avoid the terminals

The listed paths and extra edges create no A--B edge. In every linkage,
the path ending at b1 must enter through s, and the path ending at b2
through u: another B terminal cannot be internal to either path. Similarly,
the paths starting at a2 and a3 must use w and t. All four nonterminals
are therefore vital, and all six terminals are used by definition.

Each of the four displayed two-edge A--B paths has a different internal
vertex. A separator disjoint from the terminals must contain all four of
them. Removing those four vertices leaves two anticomplete triangles,
so the minimum rootless separator order is exactly four. The set
`{a1,w,t}` separates the surviving A terminals from B. The existing three
disjoint paths exclude every separator of order less than three, including
ones allowed to contain terminals.

The degree comparison in the scope paragraph is also valid: the maximum
H-degree is four, and a vertex in the actual H could have at most one
additional neighbour v outside H and C. Minimum G-degree eight would
therefore force a C-neighbour at every H vertex. All three displayed paths
have at least two vertices, so the existing terminal certificate applies.

**First unsupported inference:** that the chain of minimum linkage cuts
must contain one avoiding all six roots. All-vitality alone does not imply
this. The example does not disprove the stated version permitting an A--B
edge and one terminal in the cut, or a separator-or-terminal alternative.

## 2. Ordered attachments do not force a local inversion

### Graph hypotheses

The vertex counts are 24 in H and 31 in G. Directly from the edge list,
the short-path endpoints have degree nine, their middle vertices degree
eight, the heavy internal vertices degree ten, and its endpoints degree
eight. The C-degrees are twenty-two or twenty-three, and v has degree
eight. Its induced neighbourhood is exactly two triangles and the port
edge; in particular it contains no four-cycle.

The written connectivity proof handles all deletions of at most six
vertices. If all of C is removed, the surviving H+v is connected. Otherwise
at least ten internal heavy vertices survive and connect every surviving
C vertex. A surviving nonport joins both heavy endpoints to that component.
If an entire six-vertex block is deleted, no other vertex is deleted and
the short paths reach an adjacent block. If only ports survive in C, four
deletions have already been spent, so each short-path vertex has a surviving
internal heavy neighbour and each heavy endpoint retains one of its three
H-neighbours. The surviving v then joins the same component. This proves
the required seven-connectivity; the source does not assert connectivity
exactly seven.

The displayed seven vertices induce K7 and avoid v. Every edge respects
the given seven-colouring, including the edges from v to its two triangle
triples and ports. Hence `chi(G)=chi(G-v)=7`.

### Vitality and the quantifier over all linkages

For a heavy vertex t_j in block i, removing `{r_i,s_i,t_j}` separates
the earlier and later portions of H. At the first and last endpoints this
can delete all of A or B; these are legitimate separators under the
source's explicit terminal-allowing definition. Three disjoint paths must
meet the separator at three distinct vertices, so every member is vital.
The displayed cuts cover all vertices of H.

The forced-linkage argument also checks. At each block boundary only three
edges cross, while each of the three linkage paths must cross. Thus all
three edges are used. At the first boundary, the edges incident with the
A roots force the initial segments r0-r1 and s0-s1. At the second boundary,
the edges to the B roots force the continuations r1-r2 and s1-s2. Since a
simple path cannot leave one of those middle vertices and later return to
use its required edge, both short paths are exactly the displayed ones.
Removing them leaves just the heavy path. No alternative endpoint pairing
or linkage increases the number of contacted paths beyond one.

The blocks attached to consecutive short-path vertices occur in strictly
increasing heavy-path order. The two edges between short paths likewise
join their corresponding ends. No pair of cross-edges reverses either
pair of path orders, so the splitting inversion cells in question are absent.

### Exchange and exact remaining scope

The path `t0-c2-t17` uses a nonport of C and is disjoint from the unchanged
short paths. Its complement in G-v is exactly the five surviving C vertices
and the sixteen internal heavy vertices. They form one connected set C'
containing both ports, with order twenty-one. Every short-path vertex has
a neighbour among the released heavy vertices. Both new heavy-path ends
contact C', and c2 contacts the surviving C vertices. The terminal
certificate therefore applies with fixed disjoint original-host bags.

**First unsupported inference:** replacing global maximality of C by
vitality and an optimal contact count in the fixed H, then inferring a
splitting inversion or a separator of order at most six. This example
satisfies those local hypotheses and has no such small separator, but its
explicit exchange improves C from six vertices to twenty-one.

The proper K7 also gives a Q minor and violates the proper-minor colouring
hypothesis. Thus neither Q exclusion nor global C-maximality is retained.
The exterior chromatic condition alone does not repair these losses: here
`chi(G-N[v])=5`, since its heavy P16 is joined to `K4-c4c5`, and r1,s1 can
use a colour on that four-vertex graph. This supplies both a five-colouring
and a literal K5 in the exterior. It is the critical-host conditions,
not the numerical exterior branch, that fail.

## 3. Incompatible responses of separate exterior components

The exterior induced graph is exactly an isolated x and the edge ab, hence
is bipartite and has precisely the two stated components. Since x sees all
of the three-vertex path, a three-colouring of P+x forces P to alternate
the other two colours. Conversely every proper colouring of P with
`p0=p2` extends to x. For the component ab, the two triangles force
`a=b` if `p0=p2`, contradicting their edge. If `p0!=p2`, all three path
colours are distinct and the displayed extension is proper. Both separate
graphs contain a triangle, so their chromatic numbers are exactly three.

The full graph has centre p1 adjacent to every vertex of the chordless
five-cycle `p0,x,p2,b,a,p0`. It is therefore four-chromatic: the rim needs
three colours and the centre needs another. Equivalently, the two proven
boundary conditions cannot hold together, while a fourth colour suffices.

**First unsupported inference:** a whole four-chromatic obstruction over a
path and bipartite exterior can be assigned to one exterior component.
The missing information is simultaneous compatibility of those components'
colouring responses on the path. The example does not supply the five-class
flag, the three-path normalisation or the actual critical-host assumptions,
and no failure under those additional hypotheses follows from this review.

## Verification and limits

An independent auxiliary reconstruction through
`UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache uv run python3` checked the 31-vertex
edge list, degrees, colouring, literal K7, all eighteen displayed three-cuts,
and the complete 6-to-21 exchange. The written connectivity, forced-linkage
and separator arguments above establish the counterexamples without
enumerating all linkages or searching for absent minor models.

No unresolved mathematical gap was found in the pinned claims. The examples
do not establish a universal improving exchange or close the zero-contact
path case of the prism construction.

## 4. Six-colour quotient: separate incremental audit

**Scoped verdict: GREEN**, 14 September 2026, by
`plan_objective_allocation`, who did not construct this example. Source SHA-256:
`c1dd453108102231b9c3c18d2d927e57ccd82a45ada8e20aed11f6de42f77554`.
Only Section 4 is reviewed. Earlier source bytes equal Git `e8aa4f3`;
all earlier audit bytes, revision pins and qualified scopes are preserved.

The layer two-separators force both vertices into every linkage, proving
vitality. Every five-set has two nonedges between nonconsecutive layers,
excluding literal K5-minus. Alternating complementary palettes force
`chi(Z+v)=5`, hence `chi(J)=6`. The displayed colouring, minimum degree
five and four-cut `{p,v} union L_1` also check directly.

For no-Q, at most four model bags meet a clique four-separator of J'.
Q's five-connectivity forbids bags avoiding it on both open sides. Retain
the side containing all such bags. Each retained piece of a bag touching
the separator reaches one of its owned separator vertices; clique edges
reconnect those pieces. Any lost contact was between two separator-touching
bags and is restored by their distinct owned clique vertices. All seven
bags remain nonempty and disjoint. Repeating localises the model to one K6,
which has too few vertices. Q is five-connected because deleting at most
four vertices leaves at least three, each missing at most one adjacency.

No finite enumeration is a premise. Only the listed quotient inference is
refuted; no seven-connected critical preimage or global case closure follows.
