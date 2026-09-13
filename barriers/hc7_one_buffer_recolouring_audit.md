# Audit of the one-buffer recolouring obstruction

**Source:** [the construction](hc7_one_buffer_recolouring.md), SHA-256
`adafebe8e3517607e8f72973883f3542e152cf92a664829be39538d991cf41d6`.

**Verdict: GREEN** for the stated eighteen-vertex counterexample to the
universal colouring normal form. This is a separate internal audit, not
external peer review. No computation is needed for the verdict.

## Construction and positive certificates

The vertex count is `1+3+3+2+3+6=18`. Only S is adjacent to v, and its
induced edges are exactly those of the two triangles and xy. The exterior
is `K3 join C6`, hence is connected and five-chromatic. Every A vertex
meets P, every B vertex meets p0, and both ports meet p1, verifying fullness.

The displayed six-colouring respects every listed edge type. In particular,
wi shares its colour only with its omitted A neighbour; adjacent cycle
vertices have distinct residues modulo three, including the edge w5w0.
The P colours are distinct from every A and cycle colour. The additional
B and port attachments meet p0 of colour 4 and p1 of colour 5 respectively.
Vertex v has colour 4 and sees only colours 1,2,3.

The clique `A union P` supplies the matching lower bound of six on the
chromatic number. Its six singleton bags and the entire cycle give a K7
minor: the cycle is connected, disjoint from the clique, and contacts each
P vertex and each A vertex. This checks an unrestricted minor certificate.

## Strongest inference and all colouring choices

Fix any proper six-colouring of this graph. Since `A union P` is K6,
its vertices receive six distinct colours, with no preferred naming.
Each wi sees five of these six vertices: all of P and exactly the two
A vertices other than `a_(i mod 3)`. Its only possible colour is therefore
the colour of that omitted A vertex. This forces the cycle's three-colour
pattern in every six-colouring, not merely in the displayed certificate.

Consequently W uses all six colours. Every wi sees the other two A colours
on its cycle neighbours and all three P colours within W. Every pi sees
the other two P colours and all three A colours on the cycle. Thus every
W vertex sees each other colour within W, for every six-colouring.

Now assume a response as defined in the source exists, with arbitrary
proper phi, arbitrary proper c, and any colour t absent from c(S).
The two conditions on M make its stated extension proper: independence
handles edges inside M; avoidance handles edges from M to boundary colour
6; and every original boundary collision belongs to M. All other edges
retain proper colours. Since phi takes values only in `{1,...,5}`, M is
exactly the final colour-6 class within W and is nonempty.

Choose u in M and set `i=phi(u)`. The universal property just proved gives
a W neighbour z of final colour i. Since `i!=6`, z is outside M and retains
`phi(z)=i`, contradicting the original proper colouring phi on uz.
This does not restrict `c(x)`, `c(y)`, or any other boundary colour. It
covers `c(x)=6`, arbitrary missing t, and every five-colouring of W.
It also excludes using a larger independent set of movers: the same
argument applies to any resulting colour-6 class whose complement retains
phi, or the necessary conditions fail already for its subset M.

## Exact scope and unresolved obligations

There is no gap in the audited proposition. The graph has degree-four B
vertices and degree-three ports, has chromatic number six, and contains a
proper K7 minor. It satisfies neither the actual minimum-degree bound nor
seven-chromatic criticality nor the excluded-minor condition. Therefore
the audit establishes no obstruction to selecting this normal form under
all the actual critical-host hypotheses. HC7, Conjecture 19, and the
requested HC7-or-comparable-theorem objective remain unresolved.
