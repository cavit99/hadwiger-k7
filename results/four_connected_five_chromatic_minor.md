# A six-vertex minor in four-connected five-chromatic graphs

**Status:** written proof, with a [separate internal audit](four_connected_five_chromatic_minor_audit.md). Novelty is
unassessed. This is a lower-order deduction, not a proof of Conjecture 19,
HC7 or an independently substantiated NT-comparable theorem.

All graphs are finite and simple. Write `Q6=K6-2K2` and `Q7=K7-2K2`,
where the two deleted edges are independent. A minor model consists of
pairwise disjoint nonempty connected bags with the required contacts.

## Inputs

- [The five-root wheel extension](hc7_rooted_wheel_extension.md),
  source SHA-256 `f72e0b3d4254724a58f55b9445c0c173ea6c96e535416da47b1efc7fd5eb43b3`;
  [separate internal audit](hc7_rooted_wheel_extension_audit.md),
  SHA-256 `c93612165de23798c63922425fbd8d9e74407d2eb1a85b365853bd1343969178`.
  In a three-connected graph, a K4 rooted at four of five distinct
  vertices extends to a W4 rooted at all five. The hub is unspecified;
  the fifth root may already belong to the initial model.
- Martinsson–Steiner, [Theorem 1.3](https://arxiv.org/html/2209.00594v1):
  if C meets every colour class in every proper four-colouring of a
  four-chromatic graph, it has a K4 model with a distinct member of C in
  each bag. The primary statement and set-rooted definition were inspected
  for Section 7 of the pinned wheel source and recorded in its audit.
- Brooks, [*On colouring the nodes of a network*, p. 194](https://doi.org/10.1017/S030500410002168X):
  a graph of maximum degree at most four with no K5 component is
  four-colourable. This is the primary statement with its parameter n=4.

## Theorem

Every four-connected Q6-minor-free graph other than K5 is four-colourable.
Equivalently, every four-connected graph H of order at least six with
`chi(H)>=5` contains a Q6 minor.

**Proof.** Choose a vertex-minimal induced subgraph J of H that is not
four-colourable. Deleting any vertex makes it four-colourable, and
restoring that vertex costs at most one colour. Thus `chi(J)=5`, J is
connected, and `chi(J-z)=4` for every vertex z of J.

If `J=K5`, choose a component D of `H-V(J)`. Its neighbourhood lies
in V(J) and has at least four vertices: a smaller neighbourhood would
separate D from a surviving J vertex, contrary to four-connectivity.
The five singleton J bags and D therefore give K6 with at most one
edge absent, which contains Q6.

Otherwise Brooks' theorem supplies `z in V(J)` with `d_J(z)>=5`.
The set `C=N_J(z)` meets all four colour classes in every proper
four-colouring of J-z; a missing colour would extend that colouring
to J. Martinsson–Steiner therefore supplies a K4 model in J-z rooted
at four distinct members of C. Choose a fifth member and let T be
these five vertices.

The ambient graph H-z is three-connected and contains this same K4
model. Apply the five-root wheel extension there, obtaining five bags
rooted at T. This uses no connectivity assertion about J-z, and the
fifth root need not have been unused. Each returned bag contains an
actual neighbour of z. Adjoining the disjoint singleton bag {z} gives
`K1 join W4=Q6`. All six bags lie in H, with the original roots and
their z-edges retained. QED

## A universal vertex in the six-chromatic target

**Corollary.** A five-connected six-chromatic graph H of order at least
seven with a universal vertex u contains a Q7 minor.

**Proof.** The graph H-u is four-connected, has order at least six and
has chromatic number five, since u is universal. Apply the theorem in
H-u and keep its six actual bags. The singleton {u} contacts every one
of them, so these seven fixed bags give `K1 join Q6=Q7`. QED

The case without a universal vertex remains open. The theorem supplies
no prescribed attachment of a Q6 model to another vertex or component.
