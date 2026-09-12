# A rooted six-bag obstruction with singleton clique contacts

**Status:** explicit counterexample to the assertion below; a
[separate internal audit](hc7_full_contact_six_root_packet_audit.md) is recorded beside it. This does not refute the actual C19 construction or HC7.

Write `Q6=K6-2K2`. The refuted assertion is that six distinct roots
`R={r0,r1,r2,r3},p,q`, with R a literal K4 and pq an edge, admit a
Q6 model rooted at all six whenever the connected nonroot set C has:
minimum degree at least six in the whole packet; at least five external
neighbours for every proper nonempty subset; contacts with all six roots;
at most two R-neighbours per vertex; at most five double-contact vertices;
and the containment condition `N_R(u) subseteq N_R(x)` on every nonroot
edge ux whose endpoint x has two R-neighbours.

## Construction

Let `A={a1,...,a5}` and `B={b1,...,b5}`. Take C to be the two K6
cliques `A union {w}` and `B union {w}`, with no A--B edges. Add R as a
K4 and the edge pq. Both p and q see every A vertex and no other C vertex.
Add `a1r0,a2r1`, and give `b1,...,b5` the respective unique R-neighbours
`r0,r1,r2,r3,r0`. There are no further edges. In particular w has no
root neighbour, and there are no R--{p,q} edges.

Every A vertex has degree seven or eight, every B vertex has degree six,
and w has degree ten. All R-contact sets have size at most one, so the
double-contact bound and containment condition hold. C is connected and
its full external neighbourhood is precisely the six roots.

For the boundary check take nonempty `X subseteq C`, and put
`k=|X intersect A|`, `l=|X intersect B|`. A set of l positive B vertices
has at least `max(1,l-1)` distinct R-neighbours. If `w notin X`, then:

- For k=0 the boundary size is at least `6-l+max(1,l-1)>=5`.
- For l=0 it is `6-k+2+h`, where h counts a1,a2 in X. This is at
  least five: k<=3 is immediate, k=4 forces h>=1, and k=5 forces h=2.
- For k,l>0 it is at least `11-k-l+2+(l-1)=12-k>=7`.

If `w in X`, its nonroot boundary has size `10-k-l`. This alone is at
least five when k+l<=5. Otherwise k,l>0, and the root boundary gives
at least `2+(l-1)` more neighbours, for a total at least `11-k>=6`.
Thus all required proper subsets have boundary at least five. Equality
occurs for X=B, whose boundary is `{w} union R`.

## No rooted model

Delete r0,r1. In the resulting graph, w separates `{p,q}` from
`{r2,r3}`. Any Q6 model rooted at the six specified vertices would give
two vertex-disjoint paths from `{p,q}` to `{r2,r3}`, avoiding r0,r1:
the required contacts between these two root pairs contain a perfect
matching, since deleting at most two independent edges from their K2,2
leaves one. Realise its two edges inside the four distinct owning bags.
Both paths would have to contain w, a contradiction. This argument permits
arbitrary expansion of every root bag and unused nonroot vertices.

## Exact limitation

Full contact of C with the six roots does not provide six-neighbour
boundaries for its proper subsets, nor does the stated five-boundary
condition force the desired simultaneous rooted model. Adding contact
containment alone does not repair this inference.

The example fails essential actual-host hypotheses: it contains literal
K6 subgraphs and even the K7 on `A union {p,q}`, hence fails both literal
K5-minus exclusion and Q7-minor exclusion. It also cannot be such a side
of the four-connected actual complement F: B has only one non-R packet
neighbour, w, so restoring the two omitted cut vertices gives at most
three F-neighbours. In an actual side, four-connectivity additionally
forces `|N_packet(X) minus R|>=2` for every nonempty `X subseteq C`.
The disjunction “a rooted Q6 or an unrooted Q7” is also unaffected: this
host has a Q7 already. No stronger actual-side construction or complete
C19 case is refuted.
