# A wheel on all five roots of a K5-scheme

**Status:** written proof; separate internal audit accompanies this source.
This is a deduction from existing reductions and the five-root wheel theorem.
No priority or comparative-significance claim is made.

All graphs are finite and simple. A scheme has a path for each target edge,
no other root internally, and a common target endpoint for every collection
of paths meeting at a vertex. A rooted wheel has five disjoint connected
bags containing the five prescribed roots, with the contacts of W4.
Its hub and cyclic order are not prescribed.

## Theorem

Every K5-scheme contains a W4 minor rooted at all five prescribed vertices.
No connectivity assumption on the host is needed.

### Proof

First pass to a properly endpoint-coloured scheme in a rooted minor.
For completeness, colour each nonroot by a common endpoint of the demands
using it, and give each root its own colour. Restrict the host to the paths
and contract each monochromatic component. Such a component contains at
most one root. On each demand, omit excursions within these components
and simplify the resulting walk. Every surviving vertex has one of its
endpoint colours, so all demands still satisfy the scheme condition.
The connected contraction preimages are disjoint and retain every root;
any rooted wheel in the quotient lifts through them.

Suppose the theorem fails, and choose a properly coloured counterexample
of minimum host order. A nonroot on just one demand can be eliminated:
contract its two-edge segment to the neighbours' common colour. The
neighbours include at most one root. All other demands survive, and order
decreases. Hence every nonroot belongs to at least two demands.

We apply the reductions of Sections 1–2 of the
[separator proof](../active/k5_scheme_separator_reduction.md).
Their applicability to this weaker conclusion requires checking the lift,
rather than citing its minimum-K5-counterexample statement.

Let S be a cut of order at most two. All roots whose colours are absent
from S lie in one component C0: their pair paths avoid S. A root-free
component cannot occur. A colour absent from S there would need two
distinct boundary vertices in each of two partner colours; a colour
present on S could then use only the single demand between boundary
colours. Both contradict the cut size or the two-demand membership.

A component containing only root a must have colour a on S, since four
demands leave it. Choose another root colour i absent from S. The prefix
of P_ai from a to its first boundary vertex has both ends coloured a
and contains an i-coloured nonroot. Any second demand through that vertex
would require two boundary vertices in a different partner colour, which
is impossible. Thus such a component is also excluded.

There is consequently no one-cut. At a two-cut, every component other
than C0 contains exactly two roots a,b, and S={s_a,s_b} has those colours.
Choose distinct outside root colours c,d. The exterior prefixes of
P_ac and P_bd are disjoint and join a to s_a and b to s_b. Grow these
two seeds to a connected partition of that component together with S,
and contract the two parts. They are adjacent and contain exactly their
respective original roots. Each of the six cross-demands retains its
outside suffix after its unique possible port; the three outside-root
demands avoid the exterior, and ab is now literal. We have a properly
coloured K5-scheme on fewer vertices, with fixed disjoint connected
preimages for all five roots. Any returned five-root wheel lifts, whatever
its hub and rim order. This contradicts minimality, proving that the
minimum counterexample is three-connected.

Retain the six demands between any four roots. They form a K4-scheme
avoiding the fifth root. K4 contractibility gives a minor rooted at those
four vertices. The
[five-root wheel theorem](hc7_rooted_wheel_extension.md) in the whole
three-connected host now gives the required wheel, a contradiction. QED

## Reservation in the critical host

Suppose chi(G)=7, every proper minor is six-colourable, and d(v)=8.
For every independent triple T in N(v), the
[whole-colour-class reservation](hc7_critical_colour_class_reservation.md)
supplies an independent set I with I intersect N(v)=T and a K5-scheme
in G-v-I rooted at R=N(v)-T. The theorem gives an R-rooted wheel avoiding
the entire I and v. Connectivity after deleting I is unnecessary.

In the two-triangle case, choose T={a,b,t}, one vertex from each triangle
and one endpoint of xy. A component of the wheel's complement in G-v
containing all of T would be full to all five bags through the literal
neighbourhood edges. Together with v it would give K2 join W4=Q.
Existence of that compatible component remains unproved. The theorem
proves neither labelled W4 contractibility nor K5 contractibility, C19
or HC7.

## Inputs

The separator source SHA-256 is
`5d7dc02cc98cd96817f0919e46212a27cc3831c67a7b84cb950aebedcca4cf96`;
its adjacent audit is
`679e9a0efa4f9b57168c4111bb5aee804db6b4570a4979b5d78d70b9f52b18f3`.
Only its reductions of order at most two are used.
The wheel source SHA-256 is
`f72e0b3d4254724a58f55b9445c0c173ea6c96e535416da47b1efc7fd5eb43b3`;
its adjacent audit is
`c93612165de23798c63922425fbd8d9e74407d2eb1a85b365853bd1343969178`.
The reservation source SHA-256 is
`6c40aab52c5e5c8dc822640ce3c801f6cc46e04b161fd49f108dfd6835116eb3`;
its adjacent audit is
`10d4ab2970bb45f41ffc228a5748cd4ee963016d4d89fe0db7ff11124abab636`.
Kündgen–Pelsmajer–Ramamurthi,
[*Finding minors in graphs with a given path structure*, Theorem 5.1](https://arxiv.org/html/1207.6141#S5),
proves fully rooted K4 contractibility with the same scheme definition.
Its statement and proof were inspected; their Lemma 3.3 also supplies
the root-preserving normalisation used above.
