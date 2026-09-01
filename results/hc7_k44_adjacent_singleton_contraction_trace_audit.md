# Independent internal audit: adjacent-singleton contraction trace

**Verdict: GREEN.**  The exact source revision below is a valid unbounded,
computation-free reduction.  This is a separate internal mathematical
audit, not external peer review.

**Audited source:**
[`hc7_k44_adjacent_singleton_contraction_trace.md`](hc7_k44_adjacent_singleton_contraction_trace.md)

**Audited source SHA-256:**
`174baaa7a01d75048575760387f568bbf2ace15cef61e10a2dd5ed35372ca2ef`

## 1. Contraction cut

Contracting the exterior edge `ap` preserves the specified literal core and
target-freeness.  If the quotient were seven-connected, it would contradict
vertex-minimality.  Every quotient cut of order at most six contains the
contracted vertex; replacing it by `{a,p}` gives a cut of `G` of order at
most seven.  Seven-connectivity forces equality, so the preimage is exactly
`E={a,p} dotcup T`, `|T|=5`.

The audited seven-cut theorem then gives two or three components and the
subcubic boundary conclusion in the three-component case.  Every component
is adjacent to every vertex of `E`, since otherwise the other six boundary
vertices would separate it.

## 2. Five-rooted literal-core model

If a component `D_0` contains `S-T`, closed-shore rooted connectivity makes
`(G[D_0 union T],T)` internally five-connected.  After treating
`I=T cap S` as trivial paths, a separator below `5-|I|` from `T-I` to
`S-I`, together with `I`, would contradict that rooted connectivity.
Menger therefore gives five disjoint paths from `T` to distinct core
vertices.  Trimming at first core contact leaves the unused core vertices
free.

Any five core vertices root a `K_5`: the other three vertices enlarge three
distinct opposite-shore rooted bags, leaving one pure bag on each shore.
If two further components exist, `D_1 union {a}` and `D_2 union {p}` are
disjoint connected universal bags joined by `ap`, producing a genuine
`K_7` minor.  All paths, enlargements and branch sets are disjoint.

## 3. Two-component case

If `G[E]` had a `K_5` minor, its five branch sets together with the two full
component bags would form a `K_7^-` model whose sole possibly absent contact
is between the components.  Thus the boundary is `K_5`-minor-free.

If `S-T` meets both components, no opposite-shore pair can be split between
them because it has a literal core edge.  Hence `S-T` lies in one shore,
the other whole shore lies in `T`, and order gives
`T=S_i dotcup {x}`.  Both components meet `S_{1-i}-{x}`.

Otherwise one component `C_0` contains all of `S-T`, so the five-rooted
model exists there.  For the strengthened boundary conclusion, put
`I=E cap S` and `B=E-S`.  The identity `|S-E|=|B|+1` and closed-shore
rooted connectivity with all seven roots let Menger link the roots in `B`
to distinct vertices of `S-E`; the roots in `I` are trivial.  A deficient
linkage separator together with `I` would have order below seven, and a
target survives because of the extra vertex in `S-E`.  Thus there are seven
disjoint `E`-rooted bags with distinct core representatives and one unused
core vertex.

The representative-shore colouring is proper.  If a same-shore edge `uv`
existed, discard a root bag `q` distinct from its ends.  If `q` came from
the three-representative shore, the retained distribution is `2+4` and both
unused vertices lie on the two-representative shore.  If `q` came from the
four-representative shore, the distribution is `3+3` and one vertex is
unused on each shore.  In either case the two unused core vertices can be
assigned to opposite-shore rooted bags so that `u,v` are a prescribed pure
pair in a `K_6` minus a two-edge matching.  The edge `uv` repairs that pair,
leaving at least fourteen contacts.  The disjoint component `C_1` is
adjacent to all six retained roots, giving `14+6=20`, a contradiction.
Hence `G[E]` is bipartite with class orders three and four and the colouring
extends the literal shores.

The edge `ap` puts its ends in opposite classes.  Their possible neighbours
in `T` therefore have upper bounds two and three in some order, proving the
individual bounds and the sum bound five.  Any common neighbour in `T`
would form a triangle with `a,p`; in particular the unique common neighbour
in the singleton application is not in `T`.

Finally, the contact argument applies to every `T`-rooted `K_5` model, not
only to the constructed one.  If `p` met four rooted bags, those five clique
bags, `C_1 union {a}`, and `{p}` would have exactly the required lower bound

```text
10 + 5 + 1 + 4 = 20.
```

Fullness, `ap`, and the four assumed contacts account for the latter ten.
The bags are disjoint.  Interchanging `a,p` proves the same universal
three-bag contact bound for `a`.  This independently recovers the individual
degree bounds; the sharper sum bound comes from the proper boundary
colouring.

## 4. Three-component case

If `T` contained no whole literal shore, then `S-T` would meet both shores,
induce a connected complete bipartite graph, and lie in one component.  The
five-rooted model plus the other two components would give `K_7`.  Thus
`T=S_i union {x}`.  The extra vertex cannot lie in the opposite shore,
because its four literal neighbours in `S_i` would contradict the subcubic
boundary conclusion; hence it is exterior.  The opposite shore cannot lie
in one component by the same rooted construction, and therefore meets at
least two components.

## 5. Inputs and exact scope

The audit accepts the following adjacent GREEN inputs:

| input | source SHA-256 | audit SHA-256 |
|---|---|---|
| seven-cut component theorem | `cbd3ecb73bea0530797ad58080ae6db6052bfbf69f90af558283e3f250772ef8` | `8cd2f3adb52c8cfedd8fc3a11d47c67444dc9df62d6b5e79a78bfe914e533294` |
| closed-shore rooted connectivity | `ba6dbfe1ca9e89041b1a77174844c24598984cbe76349a55c41f15b2e997cc03` | `03738f53f8892c786dadd236c529c59b7045b3dc8371de22f0836f3721e5e43a` |

The remaining input is standard vertex-Menger.  There is no finite
enumeration or solver trust boundary in this result.

The theorem does not eliminate the remaining two-component profiles or the
three-component shore-split profile.  It does not close the
adjacent-singleton case, literal T44, T44, Conjecture 21, or `HC_7`.
