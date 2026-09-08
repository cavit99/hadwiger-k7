# The two nonroot ports cannot occur in a globally maximised core

**Status:** written proof; separate exact-source internal audit recorded beside it.
This closes the specified reserved-core branch. The case where both ports
are their B roots, and the full two-triangle construction, remain open.
All graphs are finite and simple; Q is K7 with two independent edges deleted.

**Theorem.** Suppose G is seven-connected, has minimum degree at least
eight, is Q-minor-free and seven-chromatic, and every proper minor is
six-colourable. Let d(v)=8 and

`N(v)=A dotcup B dotcup {x,y}`,

where A,B are triangles and xy is an edge. Choose a vertex a of A with
no neighbour in `B union {x,y}`. Such a choice exists. Keep a fixed.
For every `b in E={z in B : z misses x,y}`, consider all K4 models in
`G-{v,a,b,x,y}` rooted at `(A-{a}) union (B-{b})`. Choose one maximising
|M|, where M is the union of its two A-rooted bags, over all these b and
all these models; subject to this, minimise the two B-rooted bags. Then its two
common-contact ports cannot both be nonroots.

The eligible set E has at least two vertices. The maximum is over all
eligible omitted B roots, not just a preselected b. All original A roots
are retained separately in each model under comparison.

## Audited inputs

We use the following exact sources and adjacent separate internal audits:

- [Contraction closure](../active/hc7_companion_contraction_closure.md), source
  `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`;
  [audit](../active/hc7_companion_contraction_closure_audit.md)
  `26b2f5ad7226c7bb3f194cac8523f043d7ae6ca955036249f04ddc9fb6d94394`.
  We invoke edge and connected-three-set literal K5-minus exclusion and
  Corollary 3's neighbour restriction outside a literal four-clique.
- [Whole-class reservation](hc7_critical_colour_class_reservation.md), source
  `6c40aab52c5e5c8dc822640ce3c801f6cc46e04b161fd49f108dfd6835116eb3`;
  [audit](hc7_critical_colour_class_reservation_audit.md)
  `10d4ab2970bb45f41ffc228a5748cd4ee963016d4d89fe0db7ff11124abab636`.
  Its two-triangle corollary supplies each four-root model used above.
- [Connected residual component and Lemma 3](hc7_reserved_core_component_bound.md), source
  `b02d2c88ebf4879b45e36031d9bf9b7ac0722d8c7302a26d7637d8ba3fcf0e3c`;
  [audit](hc7_reserved_core_component_bound_audit.md)
  `7851c856c4a37b92fc1dcea6c823d25c55718eaf575e723c118eaa65d48bf923`.
  Its stated maximised-core input gives the actual ports and boundary;
  Theorem 6 makes the residual set connected. Lemma 3 gives a rooted K4
  with nonroot-set boundary at least four, nonroot degree at least five,
  and at most one degree-five nonroot.
- [Contraction-boundary repair](hc7_reserved_core_contraction_boundary.md), source
  `da0e3fd73fb52815d01bdfd7d9e56a0fd9d1bca4c93bb2d332fc0f4fe67de571`;
  [audit](hc7_reserved_core_contraction_boundary_audit.md)
  `d2348e8500d49aeda6a9d8d220ce3b3fe41c0e5edf2e680749aa76e9a2683dc5`.
  Its final corollary verifies the four-neighbour condition after the
  specific bB1 contraction. The present proof repairs the remaining
  ownership issue by comparing eligible omissions.

No fresh external theorem or finite computation is invoked.

## 1. Choice of reservation and the connected full component

Contracting xy against the untouched four-clique v+A shows that x,y
collectively contact at most one A vertex. The same applies to B.
There is at most one A--B edge: two edges with different A ends are
forbidden by contracting the B triangle against v+A; two with the
same A end are forbidden symmetrically by contracting the A triangle.
These contractions have connected preimages of order at most three.
Thus at most two A vertices are excluded when choosing a, and |E|>=2.
For every b in E, the four vertices a,b,x,y induce only xy, so the
reservation theorem supplies the required initial four-root model.

Suppose the chosen maximum has two nonroot ports. Write
`A-{a}={A1,A2}`, `B-{b}={B1,B2}`, and let U,V be its A bags.
The maximum over omissions is also a maximum for its selected b, so
all the fixed-reservation input applies. Each B bag is a path from Bi
to its sole common contact pi with U,V; `p1,p2 in W=G-N[v]`.
Each pi contacts both U and V. The set `M=U union V` is connected and
has exact boundary `{v,a,b,x,y,p1,p2}`. In particular b contacts M.

The residual set

`C=(G-v-B)-(M union {a,x,y,p1,p2})`

is nonempty and connected, misses M, and contacts a,x,y,p1,p2 and b.
In fact C is full to B. If it missed Bi, that root would miss both C
and M and have possible neighbours only among the eight vertices
`{v,a,b,Bj,x,y,p1,p2}`, where `{i,j}={1,2}`. It misses a by our choice,
contradicting minimum degree eight. Choose the name B1 so that B1 is
also in E, which is possible because b is in E and |E|>=2.

## 2. A valid four-root model after contracting bB1

Form `F=G[C union B union {p1,p2}]/bB1`, and call the merged root q.
Its prescribed roots are q,B2,p1,p2, and its nonroots are C. The boundary
repair applies to this actual M,C and gives at least four F neighbours
for every nonempty subset of C.

At most one C vertex contacts all three of a,x,y: two such vertices
w,w' would, after contracting va, give a literal K5-minus on
`{va,x,y,w,w'}`, with only ww' possibly absent. A vertex contacting
both b and B1 misses a,x,y, by Corollary 3 at the four-clique v+B.
Such a vertex loses only one neighbour in F and retains degree at
least seven. Every other C vertex loses no degree at the bB1 merger
and loses at most two of a,x,y, apart from the at most one vertex
losing all three. Thus all nonroots have degree at least six except
possibly one of degree five. Lemma 3 supplies a rooted K4 in F.

Among its models, maximise |K1 union K2| for the p1- and p2-rooted bags
K1,K2; subject to this minimise the q-rooted bag Q. Keep the B2-rooted
bag R. The literal q--B2 edge guarantees their mutual contact throughout.
Take a spanning tree of Q. A nonroot leaf with no K1 or K2 contact
could be removed. A leaf contacting a helper could be donated to it
unless that leaf were the sole contact to the other helper. Consequently
every nonroot leaf must be the sole contact to both K1 and K2. There
can be at most one such leaf. The spanning tree is therefore either
the singleton q or a path from q to a common contact w. In the latter
case no earlier path vertex contacts either helper.

## 3. Lifting with an eligible omitted root

First suppose this path has positive length. Its first edge lifts to
an actual edge from b or B1 to its next vertex in C. Keep that endpoint
and the remaining path, and discard the other vertex of the merged pair.
This gives a connected bag full to K1,K2 and R, the last contact using
the literal edge from the retained B root to B2. All its vertices avoid
the discarded root. The four resulting bags form a rooted K4 at the
retained B root, B2,p1,p2 in the original graph.

Append K1,K2 to U,V respectively. Both unions are connected, all four
bags are disjoint, and all K4 contacts survive. If the retained endpoint
is B1 the omitted root is the old b; if it is b the omitted root is
the eligible B1. Either choice lies in the original maximisation class.
The new A union contains M and both old ports, so is strictly larger.

It remains that Q is the singleton q, whose original preimage is
`{b,B1}`. If B1 contacts both K1,K2, discard b and repeat the preceding
enlargement with B1 singleton. Otherwise b contacts at least one helper,
say Ki, since q contacts both. Keep b singleton and omit B1.

Choose one old A bag touched by b; call it U0, and call the other V0.
Append Ki to V0 and the other helper to U0. This assignment is connected
regardless of i: each old port p1,p2 contacts both old A bags. The new
b bag contacts U0 through its old edge and V0 union Ki through its
Ki edge. The retained B2 bag R is full to both enlarged A bags through
K1,K2, and b--B2 is literal. The two A bags are adjacent through their
old edge. These four bags again form a K4 rooted at A1,A2,b,B2, avoid
v,a,B1,x,y, and strictly enlarge M by the two ports.

Every case contradicts the maximum over eligible omitted B roots.
Thus the two-nonroot-port case is impossible. No old B-root path was
combined with a new C-side model, and no quotient edge inherited from
b was silently relabelled as a B1 edge. The two-root-port branch is
not settled by this argument. QED
