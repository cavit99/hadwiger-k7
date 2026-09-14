# A neighbourhood case and the exact five-colouring extension problem

**Frozen on 14 September 2026.** Retained discovery record; current status is in the research ledger and technical frontier.

**Original status:** written proof in a working draft; no pinned-revision separate
audit or promotion is claimed. The neighbourhood proof received a separate
in-conversation check of its branch-set construction. The augmentation
target, C19, HC7 and the comparative completion criterion remain open.

All graphs are finite and simple. Write `Q7=K7-2K2` and `Q6=K6-2K2`,
with independent omitted edges. A model has disjoint nonempty connected
bags and every required contact.

## 1. A five-chromatic neighbourhood forces Q7

**Theorem.** Let H be five-connected, with at least seven vertices.
If some vertex z satisfies `chi(H[N_H(z)])>=5`, then H contains Q7.

The inputs are exactly the critical-core extraction and five-root wheel
extension used in [the lower-order theorem](../results/four_connected_five_chromatic_minor.md):
Brooks' theorem, Martinsson--Steiner Theorem 1.3 for a colourful set in a
four-chromatic graph, and the [five-root wheel theorem](../results/hc7_rooted_wheel_extension.md).
The latter takes a three-connected ambient graph and any five distinct
roots, four of which root K4, and returns a W4 model rooted at all five.
The additional root may already belong to the initial model.

**Proof.** Choose an induced vertex-minimal non-four-colourable graph
`J` inside `H[N_H(z)]`. Then `chi(J)=5`, and `chi(J-a)=4` for every
vertex a of J.

If `J=K5`, the vertices of J together with z give a literal K6. Choose
any component D outside these six vertices. Its neighbourhood contains
at least five clique vertices: otherwise its at-most-four-vertex boundary
separates D from a surviving clique vertex. The six singleton clique bags
and D give K7 with at most one omitted edge, hence Q7.

Otherwise Brooks supplies a vertex a of J with `d_J(a)>=5`. The set
`N_J(a)` meets every colour class in every four-colouring of `J-a`, since
a missed colour would extend to J. Martinsson--Steiner gives a K4 model
in `J-a` rooted at four actual vertices of `N_J(a)`. Choose a fifth member
of that neighbourhood.

The ambient graph `H-{z,a}` is three-connected and contains the same K4
model. The wheel theorem supplies five disjoint connected bags forming
W4, each containing one of the five chosen neighbours of a. All those
roots also lie in `N_H(z)`, because J lies there. Thus each wheel bag
contacts both a and z, the edge az is present, and neither a nor z is
used by the wheel. These five bags and the singleton bags `{a}`, `{z}`
form `K2 join W4=Q7`. The only possible omissions are the two independent
diagonals of the wheel rim. QED

**Corollary.** Let H be five-connected, six-chromatic and of order at
least seven. If `H-N_H[z]` is independent for some z, then H contains Q7.

**Proof.** The set `V(H)-N_H(z)`, consisting of z and all its nonneighbours,
is independent. Therefore `chi(H)<=chi(H[N_H(z)])+1`; the neighbourhood
has chromatic number at least five, and the theorem applies. QED

Neither result requires the augmentation target's minimum-degree bound.
This closes an arbitrary-order subclass only. In particular it does not
handle triangle-free six-chromatic hosts.

## 2. The full boundary-colouring response is retained

**Exact reformulation.** Let H satisfy the connectivity and order
hypotheses above and have no Q7 minor. Fix any z, put `C=N_H(z)` and
`W=V(H)-N_H[z]`. Then `H[C]` is four-colourable. H is five-colourable
if and only if some proper colouring `phi:C->{1,2,3,4}` makes `H[W]`
colourable from the lists

`L_phi(w)={1,2,3,4,5} - phi(N_H(w) intersect C)`.

**Proof.** Section 1 gives the four-colourability assertion. A list
colouring of W and phi together properly colour `H-z`; assigning colour
5 to z is valid because its neighbours are precisely C. Conversely,
relabel any five-colouring of H so that z has colour 5. Its restriction
to C uses only the other four colours, and its restriction to W respects
exactly the displayed lists. QED

All these lists contain colour 5. If `H[W]` is independent, the extension
is immediate. If `H[W]` is a matching together with isolated vertices,
the extension exists for a fixed phi exactly when there is no matching
edge ab with `L_phi(a)=L_phi(b)={5}`. Equivalently, every matching edge
must have an endpoint whose C-neighbourhood misses an old colour in
this same phi. This follows by colouring one endpoint of each edge with
an available old colour and the other with 5.

## 3. First unsupported repairs

The general step is to produce a single phi admitting the list extension,
or an original-host Q7 model. Four-colourability of C alone supplies
neither. For a matching W, failure of all extensions says that for every
phi some edge has two endpoints seeing all four colours. The bad edge
may depend on phi; reversing those quantifiers is unsupported.

Even when W is a single edge ab and both neighbourhoods are therefore
universally colourful, separately extracted rooted K4 models need not
have simultaneous ownership. The present argument does not turn them
into a common wheel contacted by both a and b. Passing to a critical
core does not preserve ambient connectivity, and contracting an edge
does not preserve the sixth colour or the minimum-degree bound. Thus
neither a closed recursive class nor a complete augmentation proof is
asserted here.
