# Internal audit: the reserved-core component bound

**Verdict: GREEN.**

**Audited source:** [the component bound](hc7_reserved_core_component_bound.md).

**Whole-source SHA-256:**
`2371cf108769929f459eff213047714762e4c05f2d183ebcfe00a4fec47296e2`.

This is a separate internal mathematical review, not external peer review.
The reviewer contributed to the earlier reserved-core deduction and to an
invalid proposed connectedness argument that was explicitly retracted.
The present three-case proof was written by another agent and independently
read in full here. The parent also reported a separate complete review.

## Exact inputs and revision checks

The historical frontier at Git `7bbcacb` has the stated SHA-256
`a7b7289d3e090414824b6d67b9abd5d456aadb765a2245bff3991c5783d6f5ea`.
The invoked scoped audit has SHA-256
`bd435dc374da1b58ba39ee77aa8f0414abf6245f51a2f287dbede3f8558148b8`.
Both hashes were checked, and the reserved-core deduction and its scoped
review were reread. They supply actual common ports, the contact of b
with one A bag, and all five H contacts and at least two B contacts for
each residual component. They do not assert that D is connected.

The original theorem's complete draft was independently checked at
`c363f4a2bbc1085fa8f4ba42393590e3f1ef2ba46eb584b19dce38c5a9949481`.
Reversing only the final status and two relocation links recovers those
bytes exactly. Removing its single historical-revision line then recovers
the original mathematical draft
`88f5f0804d28a09df192028839950f873c9f5d280eb7198c5572f8543355f791`.
No mathematical source change occurred during promotion. Its promoted hash was
`ac959b373ace3a6421d21a232f83d1caca5d408f7fbe42a3b5803e5c346874fb`;
the later appended corollary is reviewed separately below.

## Strongest constructions and ownership

The initial extra bags `U+b+p1` and `V+v+p2` are connected, adjacent and
full to a, B1, B2 and every selected component. In the first case the three
component bags attach respectively to a,x,y and are pairwise adjacent.
Each component misses at most one B root; the case hypothesis also limits
each B root to one omission. Thus the possible two holes are independent.

In the second case the two Bi-missing components contact Bj and attach
to x,y. The third component absorbs Bi. Its contacts with those two bags
use its x,y edges, and its Bj contact uses the literal B edge. The a bag
contacts all three component bags. Only a--Bj can be absent. The extra
bags remain full and disjoint; no old B-root path is used in either case.

The last case repairs the earlier ownership failure explicitly. Every
internal vertex of the old Bi--pi path lies in D, and all such vertices
form one connected set in a component adjacent to Bi. None belongs to
the three selected Bi-missing components. The path's endpoints are also
outside them, including when the path has no internal vertex. Therefore
`U+V(P_i)` is disjoint from all three allocated components and from
`V+v+pj`. The remaining two B roots are singleton core bags. Every chosen
component contacts both, so the five core bags form K5 and the two extra
bags are adjacent and full. These are seven fixed disjoint branch sets.

## Scope

The three cases exhaust the B-contact patterns of three components.
The conclusion is at most two residual components. The proof does not
settle either surviving component count, the root-port case, or the global
two-triangle construction. No new finite computation or external theorem
is a mathematical premise.

## Appended two-component shared-omission corollary

**Scoped verdict: GREEN.** The complete appended corollary was independently
read at SHA-256 `2434ad0bd10fa2805d134956c26e160524f63c851d18b6bf33139da9bb1f59e4`. Removing just its
section byte-recovers the previously reviewed `ac959b37...` source. The
reviewer checked the proposed construction before this exact-source read;
the corollary was written by the other agent. No earlier proof was altered.

The four added source/audit hashes match disk: contraction closure
`ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4` /
`26b2f5ad7226c7bb3f194cac8523f043d7ae6ca955036249f04ddc9fb6d94394`,
and the four-root packet
`b3fe07ea52e0e553c61edb59cd5b7da3719ae834d8803f21afb9bde90fc410a8` /
`e9bc147d6c0e48bba395dc5fe590ef8a8cc778914804e3c1f5d33c48e2eec628`.
Their invoked statements and the packet's boundary and degree hypotheses
were reread. No fresh primary-source inspection is claimed.

If both components miss Bi, that root misses M and all D. The eight
listed remaining vertices are its entire possible neighbourhood, so
minimum degree eight forces every listed edge. For a vertex seeing
a,x,y, the actual contraction va then gives the nine stated edges on
`{va,Bi,x,y,w}`; Bi--w is the only possible omission. This correctly
uses edge-contraction closure in the original host.

In the fresh four-root host, each C1 vertex therefore loses at most two
neighbours, and every nonempty C1 subset loses at most the three boundary
vertices a,x,y. The surviving outside vertex v licenses the original
seven-neighbour bound. Thus the packet applies with degree six and
internal four-connectivity. Its preimages use only C1 and the four roots.

The extras M, C2+a and v+Bi are connected, disjoint and pairwise adjacent.
C2 supplies all four core-root contacts; v+Bi uses the forced Bi--p1 and
Bi--p2 edges, as well as v's B edges. M can miss only the Bj-rooted bag.
Hence the model has at most one hole. No old B-root path is retained.
This excludes a shared omission of B1 or B2; a shared omission of b and
the remaining one- and two-component allocations are not settled.

## One-deficit packet and the strict enlargement

**Scoped verdict: GREEN at source SHA-256
`953bed9c9bddc805c51819f1355e9deb535c6b5824186f6ab130ea877b9abec9`.** This
addition was written by the previous reviewer and independently checked
by the author of the original component bound and Corollary 2. That
checker had also examined the proposed application before this exact-file
review; no independence from those discussions or external review is
claimed. The earlier reviews retain their explicitly recorded scope.

At that revision, removing the final section and reversing its one preceding scope-sentence
change byte-recovers the reviewed `2434ad0b...` source. All four contraction
closure and packet source/audit hashes above were checked again, and the
complete pinned packet proof was reread.

For Lemma 3, both root absorptions preserve each surviving nonroot degree
and every surviving nonroot-set boundary, with separate connected root
preimages. The one-exception condition excludes orders one and two, so
both strict reductions retain a nonempty induction instance. The same
small-separation, trisection and two-connectivity arguments apply. The
facial upper and lower degree sums differ by at least five, including
all values of h; this establishes the stated stronger packet.

For Corollary 4, two vertices seeing a,x,y produce the nine required
edges after the actual va contraction. A component missing b consequently
loses at most three neighbours per vertex, with at most one loss of three;
every nonempty subset loses only the three possible boundary vertices.
The fresh model lies wholly in C+B1+B2+p1+p2. Its port bags adjoin U,V
disjointly, preserve all six rooted K4 contacts and add both old ports to
M. This contradicts the original maximum in the same graph, without
retaining either old B path or a colouring of M. Thus the earlier b-omission
qualification is superseded: every component contacts b. The one-component,
two-component and root-port allocations, and the whole case, remain open.

## Opposite omissions and shared-port unions

**Scoped verdict: GREEN at the current whole-source hash above.** The
same checker independently read the other agent's appended Corollary 5.
Removing only that section byte-recovers the reviewed `953bed9c...`
source; the preceding mathematics is unchanged.

For opposite omissions, each fresh host loses only a,x,y from its
component's boundary and has at most the single degree-five exception
already proved. The two hosts intersect exactly in b,p1,p2. Discarding
both b-rooted bags removes b; every retained bag excludes the other roots
of its model. Hence only equally labelled port bags can overlap, and
their unions are connected through the actual shared port. The four
Bi--port contacts and the port--port contact survive as actual edges;
the literal B1B2 edge supplies the sixth contact. Appending the port
unions to U,V preserves all four original roots in separate bags in the
same graph and strictly enlarges M by both ports. No old B path is used.
Thus two components cannot have opposite omissions; together with the
earlier corollaries, at least one is full to B. This still does not settle
the remaining component allocations or the whole two-triangle case.
