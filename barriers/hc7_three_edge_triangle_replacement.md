# Triangle replacement can lower a loopless response to four colours

**Status:** explicit counterexample with a written proof and a
[separate internal audit](hc7_three_edge_triangle_replacement_audit.md).
This refutes a chromatic-retention step, not the Q target,
where `Q=K7−2K2` has independent missing edges.

The following implication is false, even for four-connected H: if χ(H)=5,
`F={ab,bc,de}`, and one proper four-colouring of H−F gives every endpoint
colour α and all three αβ component quotients are loopless triangles,
then `J=(H−de)+ac` is five-chromatic. The quotient retains the three F
edges between their two-colour components; it is an auxiliary multigraph.

Take independent sets `X={x0,x1,x2,x3}`, `Y={y0,y1,y2}` and
`Z={z0,z1,z2,z3}`. Put every X–Y edge except x0y1, and every edge from
Z to X∪Y. Add six vertices a,b,c,d,e,t, whose only mutual edges are F.
Their neighbourhoods in the three parts are exactly:

| Vertex | Neighbours in X∪Y∪Z |
| --- | --- |
| a | x0,y0,z0 |
| b | x2,y1,z1 |
| c | x3,y2,z2,z3 |
| d | x1,y0,z0 |
| e | x3,y2,z3 |
| t | x0,x1,y1,z2 |

There are no other edges. Colour these six vertices α and give X,Y,Z
three different colours. This properly colours H−F. In each layer the
marked component groups are `{a,d}`, `{b}`, `{c,e}`; t belongs to the
first group in the X layer, the second in Y and the third in Z. Thus F
joins the three components cyclically in every layer, without a loop.

Suppose H has a four-colouring. Since x3,y2,z3 form a triangle and are
all adjacent to c,e, necessarily c=e. The palette on Z is disjoint from
that on X∪Y and has size at most two.

If Z uses two colours, connected bipartite H[X∪Y] uses one colour per
shore. All of a,b,c,d use the two Z colours, and a=d because they share
z0. The path ab,bc forces a=c, contradicting de and c=e.

Suppose Z uses one colour. If the X and Y palettes are disjoint, at most
one shore uses two colours. When X does, t forces x0=x1; otherwise its
four neighbours display all four colours. Hence a=d. When Y uses two
colours, the shared neighbour y0 also gives a=d. In either case a,b,c,d
use those two colours, and the same path contradiction applies. With
one colour on each shore, a,b are forced to the same fourth colour.

If the X and Y palettes intersect, a shared colour σ occurs only on
x0,y1, the unique nonadjacent cross-pair. Their other vertices must use
one colour λ on X and a different colour μ on Y; Z uses the fourth
colour ρ. The lists then force a=λ, b=μ and c=d=e=σ, contradicting de.
This proves that H is not four-colourable.

An explicit four-colouring of J is
`X=(2,0,0,0)`, `Y=(1,2,1)`, `Z=(3,3,3,3)`, and
`(a,b,c,d,e,t)=(0,1,2,2,2,1)`.
Recolouring d with a fresh colour gives a five-colouring of H. Therefore
χ(H)=5 and χ(J)=4; the latter is at least four since restoring de could
otherwise four-colour H with one fresh endpoint colour.

## Connectivity and unaffected target

After at most three vertex deletions, the surviving β core is connected:
a Z vertex and some X∪Y vertices survive. Vertices c,t retain β neighbours.
If a,b,d or e loses all three β neighbours, these are all the deletions;
an F-neighbour survives and has a surviving β neighbour. Thus κ(H)≥4,
and the degree-four vertex a gives equality.

H already contains Q. Seven branch sets in its K3,3,3 subgraph are
`{x1,y0}`, `{x2,z0}`, `{x3}`, `{y1}`, `{y2}`, `{z1}`, `{z2}`.
Their only missing contacts are y1–y2 and z1–z2. Thus the false inference
is that preserving the three quotient triangles preserves χ=5. The
χ(J)=4 response must instead be used in the global construction. This
example refutes neither the target Q minor in H plus its marked apex nor
C19, and supplies no vertex-criticality claim or computational premise.
