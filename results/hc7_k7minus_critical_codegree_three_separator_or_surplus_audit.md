# Author audit: critical codegree-three separator or positive surplus

**Audited source:**
[`hc7_k7minus_critical_codegree_three_separator_or_surplus.md`](hc7_k7minus_critical_codegree_three_separator_or_surplus.md)

**Source SHA-256:**
`fb2083fff6087ea3b192a63800b1aa0e1f7f496d47524e452964f616a12b79e0`

**Verdict:** **GREEN in this author-side audit.**  The proof is
computation-free and has also received two independent GREEN cold audits.
The result is a structural reduction, not a proof of Conjecture 21 or
`HC_7`.

## 1. Removing the endpoint-degree hypothesis

For `H=G-{v,x}`, vertex deletion gives `chi(H)>=5`, and proper-minor
minimality gives `chi(H)<=6`.  If `H` were five-colourable, then each of
the five colours would have to occur on a common neighbour of `v,x`:
otherwise move all `v`-adjacent vertices of one colour to a new sixth
colour, give `v` the vacated colour and `x` the new colour.  Independence
of a colour class and the absence of a common neighbour in that colour
make this recolouring proper.  Codegree at most four contradicts five
distinct colour witnesses.  Thus `chi(H)=6`.

The proof no longer needs deletion density.  Robertson--Seymour--Thomas,
the proved `t=6` case of Hadwiger, gives a `K_6` minor in every
six-chromatic graph.  Five-connectivity makes `H` connected, so unused
components may be absorbed one at a time into adjacent bags.  The result
is a spanning `K_6` model.  Neither step uses `d_G(x)` or `d_G(v)`.

The palette-permutation source assumes precisely seven-connectivity,
seven-chromaticity, proper-minor six-colourability and `chi(H)=6`.  It does
not impose an endpoint-degree bound.  Its use is therefore literal.

## 2. Common branch set with two distinct pole roots

For any spanning model, the connected bag `{v,x}` together with the six
model bags would give `K_7^-` if it contacted five of them.  Hence the
joint contact union has order at most four.

Let `W=N(v) cap N(x)` and suppose no common-contact bag contains distinct
pole neighbours.  Each common bag then contains exactly one member of
`W`, and the pole neighbourhoods in that bag are that same singleton.
If the members of `W` are not in distinct bags, the desired distinct-root
bag already exists.  Otherwise there are `|W|` common bags.

Because `3<=|W|<=4`, some one of the five saturated non-pole colours is
absent from `W`.  Its two pole-neighbours cannot lie in an old common bag,
cannot coincide, and cannot lie in the same new bag.  They therefore lie
in two distinct exclusive bags.  The contact union then has order at least
`|W|+2>=5`, a contradiction.  This checks both the codegree-three and the
slightly stronger codegree-four statement.

## 3. Split, missing contacts and the actual separator

Cutting an edge of an `a-b` path in a spanning tree of the common branch
set gives two nonempty connected adjacent pieces with the nominated roots
on the correct sides.  After adjoining the two poles, these two pieces and
the five foreign model bags give seven disjoint connected sets.  The two
pole-piece bags are adjacent through `vx`; the foreign five form a clique
minor.  Thus only the ten pole-piece--foreign contacts can fail.  At most
one failure would be a `K_7^-` model, so at least two contacts fail.

At least one piece `X_p` is therefore anticomplete to a foreign bag even
after its pole `p` is adjoined.  Both `N_G(X_p)` and
`N_G({p} union X_p)` are genuine vertex separators, not merely
model-relative contact sets.  The first contains `p`, because `X_p`
contains its nominated pole-neighbour; the second contains the other pole
through the edge `vx`.  Thus one of the two separators always contains the
specified endpoint `v`, regardless of which side supplies the absent
contact; in the critical-host application this is the degree-eight endpoint.
Seven-connectivity gives the lower bound seven for both.  At
equality, a component missing one boundary vertex would have a separating
neighbourhood of order at most six, proving fullness.

## 4. Critical-host dichotomy and arithmetic

The frozen critical-host input supplies a degree-eight vertex and density
`m(G)>=4n(G)`.  The generic six-connected degree-eight theorem supplies an
incident edge of codegree at most three.

At codegree three, Theorem 1 applies.  At codegree at most two, contraction
removes exactly `1+c` edges and one vertex, so

```text
m(G/vx)>=4n(G)-3=4n(G/vx)+1.
```

The contraction is six-connected, target-free and a proper minor.
Five-colourability would expand and recolour the degree-eight endpoint
with a new sixth colour, so it is exactly six-chromatic.  Expanding any
six-colouring to `G-vx` also proves the seven-root palette assertion: the
contracted colour is absent from `T=N(v)-{x}`, and every other palette
colour must occur there or it can be assigned to `v`.

No use of the former `tau>=18` incidence alternative remains in this
dichotomy.  Its two unresolved outputs are honestly retained: a
six-connected positive-surplus quotient, or a separator of unbounded order
whose boundary may always be required to contain the degree-eight endpoint.

## 5. External and repository trust boundary

The exact external input is N. Robertson, P. Seymour and R. Thomas,
*Hadwiger's conjecture for `K_6`-free graphs*, Combinatorica **13** (1993),
279--361, DOI `10.1007/BF01202354`.  Its conclusion is exactly that a
six-chromatic graph has a `K_6` minor.

The repository hashes listed in the source were checked locally.  The
palette theorem, the generic degree-eight low-codegree theorem, the
critical-host theorem, and the independently audited bounded-endpoint
split theorem all have the hypotheses used here.  No finite classifier,
unproved density theorem or endpoint-degree assumption enters the new
argument.
