# Earlier asymmetric five-bag extraction

**Status:** frozen working checkpoint, 22 September 2026; not separately
audited. The [three-contact closure](../results/hc7_split_clique_three_contact.md)
supersedes the missing-contact nonclosure below. The four-contact branch
remains open; consult the current technical frontier for its status.

**Working asymmetric colouring construction; no case closure or separate
audit.** Choose `p in P`, six-colour the proper minor `G/up`, and give
its merged vertex colour six. Let I be the other vertices of that colour.
Then I is an independent subset of C, anticomplete to p. The original
induced graph `K=G-({u,p} union I)` is five-colourable, and
`T=(P-{p}) union D` is colourful in every five-colouring of K. Otherwise
restore p and I in colour six and give u a colour missing from T.
This uses a minor with one fewer vertex only to obtain a colouring;
no criticality or connectivity is transferred to K.

The following extraction handles this whole auxiliary class. Let a
five-colourable graph K contain an anticomplete literal edge A and
four-clique D, with `A union D` colourful in every five-colouring.
Let X be the component of `K-D` containing A. Then either:

- X contacts all four D vertices; X and the singleton D bags form K5; or
- X misses exactly one `d in D`, and `K[X union (D-{d})]` contains a
  K5 minor rooted at all five vertices of `A union (D-{d})`.

To prove this, fix a colouring with D in colours one to four. The edge
A uses colour five and one other colour. If X missed two D vertices,
choose a missing boundary colour different from A's other colour.
Interchanging it with five throughout X preserves every boundary edge
and removes five from A, a contradiction. Hence X misses at most one
D vertex. The D-full case has the displayed model.

If X misses d, the same interchange proves that A uses exactly colour
five and d's colour in every colouring. Put `Q=D-{d}`. For each
`a in A,q in Q`, their bichromatic component in `K[X union Q]`
contains both roots: otherwise interchanging the component at a changes
A's forced pair of colours. This interchange extends to K, since X's
entire outside neighbourhood is Q. The six resulting paths form a
rooted K2,3 scheme: A has the two distinct colours absent from Q, and
every intersection has the colour of a common endpoint. Bipartite
contractibility supplies its rooted minor; the actual A edge and Q
triangle complete K5. All five bags lie in the stated original subgraph.

Applied above, these are explicit distributions of four D roots and
one P-meeting bag, or three D roots and two distinct P-rooted bags.
Neither supplies K7 yet. In the second distribution, two disjoint
paths from the omitted d to the two P roots exist in
`G-({u,p} union Q)`, which is two-connected. They need not avoid the
vertices used by the rooted K5 construction. The first distribution
likewise lacks the required contacts from p to the four D bags.
The independent class I does not automatically supply either lift.
