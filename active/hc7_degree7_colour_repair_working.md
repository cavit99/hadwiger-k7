# Degree-seven interior-edge recolouring: exact repair normal form

**Status:** written working proof with a
[separate internal audit](hc7_degree7_colour_repair_working_audit.md). This is a
conditional refinement of the [degree-seven construction obligation](hc7_c21_rooted_density_construction.md#4-what-remains-towards-hc7),
not a closure of that case or of HC7.

## 1. Fixed original host and response family

Let `G` be a finite seven-connected graph with chromatic number seven,
no `K7` minor, and every proper minor six-colourable. Fix `u` of degree
seven, and put

\[
 S=N_G(u),\qquad C=G-N_G[u],\qquad A=G-u.
\]

The established inputs give nonempty connected `C`,
`alpha(G[S])<=2`, and the following exact boundary languages:

* every six-colouring of `A` has exactly one repeated pair on `S`;
* for every `h=xy` in `E(G[C])`, every six-colouring `phi` of `G-h`
  has `phi(x)=phi(y)` and two or three disjoint repeated pairs on `S`.

Fix such an edge `h` and a response `phi`. Write `gamma=phi(x)=phi(y)`.
For another palette colour `theta`, call its endpoint connection
**internal** if `x,y` lie in one component of `(A-h)[gamma,theta]`.
An endpoint connection not internal is called **exceptional** below.
These terms refer to literal two-colour subgraphs of the fixed host;
they are not minor-model labels.

All five endpoint connections exist in `G-h`: otherwise a component
interchange separates the endpoint colours and restores `h`, six-colouring
`G`. Let `q(phi)` be the number of exceptional connections. Proper-minor
criticality supplies the nonempty response family, and non-six-colourability
is applied to every modified response constructed below. No quotient is
assumed critical.

## 2. Every exceptional connection is the old separating-edge move

### Proposition 2.1

Suppose `theta` is exceptional. Let `D_x,D_y` be the distinct components
of `(A-h)[gamma,theta]` containing `x,y`. Then:

1. Exactly five colours occur on `S`. Write `delta=phi(u)` for its unique
   missing colour.
2. The colour pair `{gamma,theta}` is `{delta,r}`, where the `r`-block
   is one of the two repeated boundary pairs, say `e_1={a,b}`.
3. The components `D_x,D_y` contain opposite members of `e_1`, one each.
   The full corresponding component of `G-h` is exactly
   `D_x union {u} union D_y`; within that component the only neighbours
   of `u` are `a,b`.
4. Interchanging the two colours on `D_x` and restoring `h` gives a
   six-colouring `c` of `A` with the other repeated pair `e_0` as its
   sole repeated boundary pair. In the full `c`-bichromatic component
   joining `a,b`, the restored edge `h` is an `a-b` separating edge.

In particular, a response with four boundary colours has all five
connections internal. If it has five boundary colours, then `q(phi)<=2`
when `gamma` is missing on `S`, `q(phi)<=1` when `gamma` colours a
repeated pair, and `q(phi)=0` when `gamma` colours a singleton of `S`.

#### Proof

Interchange `gamma,theta` on `D_x`. This is proper on `A-h` and makes
`x,y` differently coloured, so restoring `h` produces a proper
six-colouring of `A`. Its trace on `S` must have exactly six colours.
A two-colour component interchange can introduce at most one colour on
`S`. The initial response has at most five boundary colours; hence it
has exactly five, and this interchange increases that number by one.

For such an increase, exactly one of the two interchanged colours must
initially be missing from `S`. It is the unique missing colour `delta`,
which is also `phi(u)`. The other colour `r` must occur both inside and
outside `D_x`. Boundary colour classes have size at most two, so its
block is a repeated pair and `D_x` contains exactly one member. Applying
the same argument to the interchange on `D_y` puts the other member in
`D_y`.

Adding `u` connects precisely these two components: its neighbours in
this layer are exactly the two boundary vertices of colour `r`. Thus
the full component has the asserted form. The interchange on `D_x`
leaves the other repeated boundary pair untouched and splits `e_1`.
It also leaves the vertex set and the uncoloured graph of the two-colour
layer unchanged. Restoring `h` joins precisely `D_x,D_y`, so this edge
is a separating edge between the two roots of `e_1`. The final bounds
follow by counting the two repeated boundary colours. QED.

This is an exhaustive converse to the
[prescribed-response separating-edge construction](../results/hc7_degree7_tight_pole_edge_localization.md#3-a-separating-edge-carries-the-exact-response).
It gives no new descent: a single interchange that restores `h` uses
all six colours on `S`, exactly as that construction predicts.

## 3. A sufficient condition for removing every exceptional connection

### Proposition 3.1 (singleton component interchange)

Suppose `phi` has five boundary colours and
`phi(x)=phi(y)=phi(u)=delta`, where `delta` is absent from `S`.
Let `r_i` be a singleton boundary root of colour `i`, and let `K_i`
be the `delta-i` component of `G-h` containing `x,y`. If `r_i` is not
in `K_i`, then a single Kempe interchange in `G-h` produces another
response `psi` such that

\[
 |\psi(S)|=5,\qquad \psi(x)=\psi(y)=\delta,
 \qquad q(\psi)=0.
\]

The two repeated boundary pairs are unchanged.

#### Proof

By Proposition 2.1 the `delta-i` endpoint connection is internal,
because `i` is a singleton boundary colour. The vertex `u` has only
one neighbour in this layer, namely `r_i`. Thus if `r_i` is outside
`K_i`, so is `u`. Interchange `delta,i` on the other component `L_i`
containing `u,r_i`.

The endpoint component `K_i` is unchanged, so `x,y` retain colour
`delta` and their internal connection in this layer. On `S`, only
`r_i` changes, from `i` to `delta`. Consequently five colours still
occur, the two repeated pairs are unchanged, and the new missing
boundary colour is `i=psi(u)`.

For each other alternative colour `j!=delta,i`, the `delta-j` layer
does not contain `u` in the new response. Its global endpoint connection
therefore lies wholly in `A-h`. The `delta-i` endpoint connection was
already retained inside `K_i`. All five are internal. QED.

### Corollary 3.2 (normal form over the full response family)

Choose `phi` minimizing `q(phi)` over all six-colourings of the one
fixed graph `G-h`. Then exactly one of the following holds.

1. `q(phi)=0`: all five endpoint connections are internal.
2. `q(phi)=1`, and either the equality colour belongs to a repeated
   boundary pair, or it is absent from `S` and every singleton boundary
   root belongs to its corresponding endpoint component.
3. `q(phi)=2`: the equality colour is absent from `S`, and all three
   singleton boundary roots belong to their corresponding endpoint
   components.

#### Proof

The response family is finite and nonempty. Proposition 2.1 bounds
`q(phi)` and determines where its equality colour can occur. In the
absent-colour case, any singleton root outside its endpoint component
would give `q=0` by Proposition 3.1, contradicting minimality when
`q(phi)>0`. QED.

This minimization compares actual colourings of the same original
edge-deletion graph. It does not assume that independently supplied
colourings lie in one Kempe component. The proof of Proposition 3.1
constructs the precise interchange that is used.

## 4. The one-exception case has operation-specific missing-colour moves

### Proposition 4.1

Suppose `q(phi)=1` and the equality colour `gamma` occurs on a repeated
boundary pair. Put `delta=phi(u)`. For any singleton boundary root
`r_i` of colour `i`, interchange `delta,i` on the component containing
`u`. The resulting response `psi_i` has the same two repeated pairs,
the same endpoint equality colour `gamma`, and exactly five boundary
colours. Its only possible exceptional connection is the `gamma-i`
connection. If that connection is exceptional, its two components in
`A-h` contain opposite members of the same `gamma`-coloured boundary
pair.

#### Proof

Neither endpoint has colour `delta` or `i`, so both keep colour
`gamma`. The only boundary root using either interchanged colour is
`r_i`, which is adjacent to `u` and hence belongs to its component.
It changes to `delta`, while `u` changes to `i`. All other boundary
vertices and both repeated pairs are unchanged. The final conclusion
is Proposition 2.1 applied to this particular new response. QED.

## 5. Exact global residue

The foregoing does not prove that `q=0` permits edge repair. It says
that no single endpoint-separating Kempe interchange exists in that
response. Five internal paths can still share vertices of the endpoint
colour. The [critical-pinch barrier](../barriers/hc7_near_k7_critical_pinch_kempe_barrier.md)
shows why ordinary edge criticality and seven-connectivity cannot be
used to declare them disjoint; its example is not fully minor-critical
or `K7`-minor-free.

In the two-exception case, write the repeated pairs as `b_1,b_2` of
colour `beta` and `c_1,c_2` of colour `eta`. There are literal components
`D_beta,x`, `D_beta,y`, `D_eta,x`, `D_eta,y` attaching the two endpoints
to opposite members of their respective pairs. Same-layer components
are disjoint. Opposite-layer components may intersect at vertices of
colour `delta`; in particular

\[
 D_{\beta,x}\cap D_{\eta,y}\quad\hbox{and}\quad
 D_{\beta,y}\cap D_{\eta,x}
\]

are not proved empty. These intersections prevent assigning the union
of the two `x` components to an `x` bag and the union of the two `y`
components to a disjoint `y` bag. Corollary 3.2 adds three literal
singleton-root contacts to the other three endpoint components, but
does not assign their shared endpoint-colour vertices to disjoint bags.

In the one-exception case, Proposition 4.1 moves the unique missing
boundary colour among the singleton colours through explicitly coupled
responses. Neither the number of exceptions nor a host-order parameter
strictly decreases if each new response again has one exception. A
purported induction on these moves therefore has no established strict
parameter, and no smaller critical graph is obtained.

The first unsupported step in a completion remains one of two forms:
turn these coupled component systems into disjoint connected branch sets
with all required original boundary contacts, or prove a longer
recolouring that restores `h` while leaving at most five colours on `S`.
The response normalization preserves the entire boundary partition where
claimed, but supplies neither conclusion. It is route nonclosure, not a
counterexample to the degree-seven target.
