# Internal audit: literal exclusion after one contraction

**Verdict: GREEN.** All six numbered statements hold at the
revision below. This is a separate internal mathematical audit, not external
peer review or a proof of Conjecture 19, Conjecture 21 or `HC_7`.

**Audited source:** [contraction closure](hc7_companion_contraction_closure.md).

**Whole-source SHA-256:**
`ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`.

The mathematical text was first checked at
`3079c426f202d1d992b8c4586b6ad386b14f5a62f2d9ec26c5d7c1895b53748f`;
its initial final-status revision was
`318480c0fa262498483eb2e16fa1ff5195d8c5f5931a8eaeac8fcc00b0d23a92`.
The strengthened connectivity, general connected-set charge and automatic
triple closure were independently checked at
`2125065fa16711352e264c2655ca9594188ed302dbb494116a299866d0f4bc83`;
the current change replaces the pending-audit status only. No finite
screen or new external literature is used.

## Input and strongest inference

The invoked [five-connected helper theorem](hc7_five_connected_helper_closure.md)
has source SHA-256
`d68986c2c5228b322c8f1c93fff532d4c5f5b49009448a827ea7204fe5016513`.
Its [GREEN adjacent audit](hc7_five_connected_helper_closure_audit.md)
has SHA-256
`b7b90f05d50c1b85c401265b46b3c14e51bbb8ec77c1beae481bcebdd7c3a3f1`.
Both hashes were checked. The inherited primary input was not freshly
inspected during this audit.

Contracting an edge of a six-connected graph leaves a five-connected
simple quotient: a cut containing the merged vertex lifts with one extra
vertex, and any other cut lifts unchanged. Original minimum degree eight
gives quotient minimum degree seven, including the merged vertex. The
edge loss is exactly `1+c`, so the quotient excess is `q+3-c`.

A literal `K_5^-` has three vertices adjacent to its other four vertices,
even when the host contains extra edges. At least two, `x,y`, differ from
the merged vertex. The helper theorem applies at each because the quotient
is five-connected, is `Q`-minor-free, and has degree at least seven. Its
integer contrapositive gives `d(x),d(y)>=q+17-c` in the quotient.
The four original vertices `u,v,x,y` are distinct. Their degree sum is at
least `2(c+1)+2(q+17-c)=2q+36`. Thus their surplus above eight exceeds the
entire original surplus `2q`; all omitted original surpluses are
nonnegative. The cancellation is valid for every `c`, without a bound
on endpoint degrees or quotient excess.

## Local consequences and ownership

An unmerged vertex drops to degree seven precisely when it was an original
degree-eight common neighbour. Two incident edges among three common
neighbours, together with the contracted edge's endpoints, give all nine
required `K_5^-` edges. Hence those vertices induce a matching and isolated
vertices. The merged degree is seven exactly when its two seven-element
neighbour sets coincide, giving the stated endpoint-degree and `c=7`
conditions.

For Corollary 3, contracting `vu` retains the literal four-clique, with
only its `v` root expanded. The outside vertex `x` is distinct from both
endpoints, keeps its two old clique neighbours, and gains the merged
clique vertex through `ux`. These are three distinct contacts, giving a
literal `K_5^-` in the quotient. No branch vertex is reused.

## General connected sets and automatic triple closure

For a connected set `C`, the edge loss is exactly `m_C+D`, including all
duplicate external contacts. Two universal vertices of a quotient
`K_5^-` can be chosen outside its merged vertex, and correspond to distinct
original vertices outside `C`. Charging their degrees together with all
degrees in `C` gives exactly the stated lower bound `2q+4+b-D`.
Thus `D<=b+3` contradicts the total surplus; the quotient's explicit
five-connectivity is what licenses the helper theorem.

The two-contact multiplicity bound and triangle corollary are valid.
Two outside vertices full to a triangle would already give a literal
`K_5^-`, irrespective of any extra edge. For arbitrary connected triples,
one-edge closure first forbids `K_{1,2,3}`: the specified contraction has
only the pair of uncontracted three-part vertices missing. Choosing a
centre of the triple then makes three full outside neighbours impossible.
Hence `n_3<=2` and `D-b=n_3-n_1<=2`. A cut of order at most four in
the quotient lifts to at most six original vertices, so original
seven-connectivity supplies the required five-connectivity. These are
actual connected preimages; no colouring or criticality is inherited.

## Unresolved obligations

No gap was found in the stated deductions. A quotient minor lifts by
replacing its uniquely owned merged vertex with the connected original
set. Host order decreases, but the required connectivity, minimum degree eight
and chromatic criticality have not been retained. Thus unrestricted
iteration or a global near-clique augmentation does not follow.
