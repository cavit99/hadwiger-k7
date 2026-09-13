# A six-colourable host without a one-buffer response

**Status:** written counterexample to an intermediate colouring normal form,
with a [separate GREEN internal audit](hc7_one_buffer_recolouring_audit.md).
This does not refute Conjecture 19 or HC7.
All graphs are finite and simple. No computation is a premise.

## The unrestricted response being tested

Put `S=N(v)` and `W=V(G)-N[v]`. Choose a proper colouring
`phi:W -> {1,2,3,4,5}` and a proper `c:S -> {1,2,3,4,5,6}`. Define

```text
M = {w in W : phi(w)=c(s) for some adjacent s in S},
S6 = {s in S : c(s)=6}.
```

The proposed response requires that `M` be independent, that no edge join
`M` to `S6`, and that some colour `t` be absent from `c(S)`. Recolour M
with colour 6, retain phi on `W-M`, retain c on S, and give v colour t.
These requirements give a proper six-colouring. They allow c to use
colour 6 and allow v's colour to differ from the buffer colour. If c
uses all six colours, v has no available colour. Allowing extra movers
does not help: every collision vertex must move, and any permitted
superset would imply the same independence and avoidance conditions for M.

**Proposition.** There is an eighteen-vertex, six-colourable G with
`S=2K3 disjoint union K2`, `chi(W)=5`, and connected W meeting every
vertex of S, for which no such response exists, for any phi, c or t.

## Construction and positive certificates

Take disjoint triangles `A={a0,a1,a2}`, `B={b0,b1,b2}` and
`P={p0,p1,p2}`, a cycle `w0w1w2w3w4w5w0`, an edge xy, and v.
Put `S=A union B union {x,y}` and `W=P union {w0,...,w5}`.
Besides these triangle, cycle and edge edges, add precisely the following:

- every edge from v to S;
- every edge from P to `A union {w0,...,w5}`;
- the edges from each wi to `A-{a_(i mod 3)}`;
- every edge from p0 to B, and the edges p1x, p1y.

Thus `N(v)=S`, `d(v)=8`, and S induces exactly the stated configuration.
W is the join of K3 and C6, so it is connected and has chromatic number
`3+2=5`. The listed attachments make it meet every S vertex.

A proper six-colouring is

```text
ai=bi=i+1,     pi=i+4       (i=0,1,2),
wi=1+(i mod 3),             x=1, y=2, v=4.
```

The six vertices `A union P` form K6, so `chi(G)=6` exactly. They also
give six singleton bags which, together with the connected bag
`{w0,...,w5}`, form a K7 minor: the last bag contacts all six singletons.

## Why every response fails

In every six-colouring of G, the clique `A union P` uses all six colours.
Each wi sees P and the two A vertices other than `a_(i mod 3)`, so it
must receive the colour of that remaining A vertex. Consequently W uses
all six colours. Each wi sees the other two A colours on its two cycle
neighbours and all three P colours; each pi sees the other two P colours
and all three A colours on the cycle. **Every vertex of W therefore has
a neighbour in W of each of the other five colours.**

Suppose a response existed and consider its resulting six-colouring.
Since W uses all six colours, M is nonempty. Choose u in M and write
`i=phi(u)`, which is not 6. The displayed property supplies a neighbour
z in W whose final colour is i. Then z is outside M, so `phi(z)=i`.
This contradicts properness of phi on the edge uz. The argument covers
every boundary use of colour 6 and every available choice of t. QED

The construction has degree-four B vertices and degree-three ports,
is six-chromatic, and has a K7 minor. It therefore fails the actual
minimum-degree, criticality and excluded-minor hypotheses in the
[current construction](../active/hc7_k44_closure_frontier.md#75-a-neighbourhood-contact-construction).
It refutes the universal normal form, not its existence in that class.
