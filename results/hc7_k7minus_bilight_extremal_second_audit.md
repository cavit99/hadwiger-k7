# Second internal audit: the 4-bilight extremal theorem

**Verdict:** GREEN.

The verdict is within the stated external-theorem and finite-verifier
trust boundaries. This is an internal mathematical audit, not external
peer review.

**Audited source:**
[hc7_k7minus_bilight_extremal.md](hc7_k7minus_bilight_extremal.md)

**Source SHA-256:**
`4ffbe9fc80a47713173a5f260759959da9397379ff26c2b18754eba5e97a560f`

The source proves that every finite simple 4-bilight graph on `n>=3`
vertices with at least `4n-2` edges contains `K7^-`, and consequently
that every `K7^-`-minor-free graph is six-colourable. The latter is C21;
neither conclusion asserts HC7.

## Scope and independent reconstruction

This audit combines two complementary reconstructions, both checked
against the source hash above. One independently checked Sections 1--3,
5--6 and the first saturation argument of Section 8. The other
independently checked the complete degree-five reduction in Section 4,
the local contraction lemma it uses, the end argument of Section 6,
and Sections 7--8 through the C21 implication. Thus the initial density
and orientation chain is not attributed to the terminal audit, nor is
the paired-square and terminal chain attributed to the first scope.

Both checks attacked the mathematical inferences, including inherited
connectivity, fragment properness, density after each operation, the
minimum-order class, and the ownership of all model bags. Neither
treats another audit's verdict as a replacement for these checks.

## Exact local inputs

The following source hashes were checked directly.

| Input | SHA-256 |
|---|---|
| [Five-root helper theorem H2](five_root_one_missing_contact.md) | `078ba860d4cdde187cdc6e618a4e1842dd623523dbefbe3ead06544c7d8afa18` |
| [Rooted star and triangle lemmas](hc7_c21_rooted_density_low_degree_reduction.md) | `431bd7d7d2b5bcb59e385781234c6d7ed6824f62ee50eb8ddf49e69da792cef2` |
| [Local quasi-five-connectivity lemma](hc7_c21_helper_degree_six.md) | `85927a0f7d1af6229930fd67f7144eac35b934c54ad504539a34d39e209020ee` |
| [Rooted dart lemma](rooted_dart_nonroot_degree_five.md) | `37dcf256f64fca7c49a1bd4ec66021371fba9a7863bf9523597ba4b898ecfad2` |
| [Degree-seven quotient theorem](../active/hc7_k7minus_degree7_common_neighbour_exclusion.md) | `663c1b7e0de9b0951de89801d52baf4aae12535d7807547d19d04fc10b00c4b0` |
| [Degree-seven verifier](../active/hc7_k7minus_degree7_quotient_verify.py) | `ac0c37438d802930a0aa80bfd1d6491101da3df9a55fac1e1cf3db5ae1b7e445` |

H2's complete proof was also independently reconstructed in the
[second H2 audit](five_root_one_missing_contact_second_audit.md), whose
SHA-256 is `3797c8ffba6dcfeedb7b0d608e6e16719805c9e5cff3d7798e13fe2b10be5df4`.

## Initial reductions and low-side construction

The external map was checked against
[Dvořák--Norin--Rahman, 2609.17760v1](https://arxiv.org/html/2609.17760v1):
Lemma 3.3 for maximal reducible replacement; Observation 4.1 and
Corollary 4.2 for extraction and isolator lifts; the proofs of
Corollary 5.3 and Lemmas 5.4, 5.5, 5.9 for the orientation argument;
and Theorem 2.6 with Lemma 5.6 for labelled root-clique completion.
Replacing their heavy condition by density at least two uses H2 while
retaining the required lightness, nonpositive-density and exterior-size
conditions. No density-one version of H2 is assumed.

The audit checked the minimum counterexample's class explicitly:
lexicographic order in `(v,e)`, order at least three, density at least
`-2`, 4-bilightness and target exclusion. A reducible replacement keeps
the required order and has a fixed rooted lift. Edge deletion uses the
exact `S-{u}` density identity and the replacement of a boundary vertex
by `u`; all cases where the restored edge joins the two fragments were
included. The retained fragments are nonempty. The degree-at-most-four
deletion and minimum-cut shore argument then establish ordinary
five-connectivity without assuming it on arbitrary minors.

For the low-side edge lemma, the weighted degree inequality gives a
vertex with `d(v)+d_S(v)<=8`. The star construction deletes only edges
between boundary vertices. Its five linkage paths have distinct roots
and ends, with trivial paths where a root is already a neighbour of
`v`. The star centre avoids every boundary vertex. Removing its end
from the associated path leaves a nonempty root bag, so the centre and
`{v}` are valid helpers. The opposite rooted clique joins corresponding
root bags only, preserving all helper contacts.

## Degree-five elimination

The localized unique-neighbour contraction lemma was reconstructed from
its corner inequalities. It needs a five-connected graph, a proper
five-fragment of order at least three, an opposite side of order at
least two, and one boundary vertex with a unique neighbour inside.
No contraction-criticality or minimum-fragment condition is imported.
Its quasi-five-connected conclusion implies 4-bilightness: both members
of a dense bifragment would have boundary four and at least two
vertices, giving a forbidden nontrivial four-cut.

For a degree-five vertex `v`, a nonedge `ab` in its neighbourhood gives
the smaller minor `J=G-v+ab`, with unchanged global density. The fixed
preimage of its retained vertex `a` is `{v,a}`. If `J` has a dense
bifragment, restoring `v` and deleting `ab` changes each fragment's
density by `k-c`, where `k` counts its neighbours at `v` and `c`
records incidence with `ab`. Positivity survives. The consistency
lemma forces a five-fragment `Y` of density one, and then
`rho_J(Y)=k=c=1`. Its boundary contains `b` in both graphs, `a` is its
unique neighbour of `v`, and its opposite side contains the other
positive fragment and has order at least two.

If `|Y|>=3`, the local lemma gives a density-preserving admissible
contraction. If `Y={a,c}`, minimum degree five and density one force
the exact degree-five neighbourhoods displayed in the proof. Contracting
`ac` loses exactly three parallel edges. A lifted density-one blocker
avoids their common triple `R` and contains `v,b`. The large case again
contracts; the two-vertex case forces the second displayed pair and
the cycle `a,c,b,v,a`, with the triples `R,D` outside it.

All intersections of those triples are covered. Intersection of order
at least two gives a cut of order at most four with a nonempty opposite
side. Intersection of order one gives a five-boundary and an opposite
side of density `18-e(G[S])>=8`. That side is nonempty and internally
five-connected; the full rooted clique there, together with the two
adjacent bags `{a,v}` and `{c,b}`, gives an explicit `K7` model.

If `R,D` are disjoint, every five-cut containing `a,v` also contains
`c,b`: otherwise one cut vertex has no neighbour on one open side and
can be removed from the cut. After contracting the codegree-zero edge
`av`, a dense bifragment therefore lifts to two sides meeting both
triples. One side `B` has a unique vertex of `R`. It cannot have order
one by positive density, or order two by the minimum degree at that
unique vertex. The local lemma applies to `B` and edge `ar`, whose
codegree is at most three. This is the final smaller admissible minor.

Every contraction retains at least eight vertices, preserves target
exclusion and lifts by replacing the merged vertex with its fixed
connected two-vertex preimage. The proof never transfers colouring
criticality to a quotient.

## Proper ends and six-connectivity

Properness is essential and is explicit in the final source. A
five-fragment with empty opposite side has density
`18-e(G[N(A)])>=8`, so a low fragment is proper. Degree summation rules
out proper five-fragments of orders one, two and three. In the end
lemma, `F`-fragments are proper fragments, and an end contains no such
fragment as a strict subset; these are distinct uses of properness.

The corner boundary contains both endpoints of the blocking family
edge even when that edge is internal to `A`. Equality at order five
would produce a strictly smaller `F`-fragment, with a nonempty opposite
side. Hence a nonempty `A`-corner forces `p+s+u>=6`, and the opposite
`C`-corner is empty. The two-corner, one-corner and zero-corner cases
all contradict the lower bound four on proper fragments; no case
requires an endpoint of the family edge to lie in the original boundary.

An inclusion-minimal low `F`-fragment is also an unrestricted `F`-end:
a heavy contained fragment would be nonadjacent to the heavy opposite
side. Thus the local end lemma legitimately applies to the edge
supplied by the low-side construction. This excludes every five-cut.

## Terminal degree calculations and finite boundary

Once the minimum graph is six-connected, any edge of codegree at most
three contracts to a five-connected, hence 4-bilight, smaller graph
with density at least `-2`. Therefore every edge has codegree at least
four. The exact equality `e=4n-2` gives average degree `8-4/n<8`;
minimum degree six leaves a degree-six or degree-seven vertex. The
inequality `binomial(n,2)>=4n-2`, with `n>=3`, already forces `n>=9`.
No eight-vertex exception enters either terminal branch.

Section 7 was reconstructed directly in the six-connected host. Two
exterior disjoint paths filling two missing matching pairs in `N(v)`
give an explicit `K7^-` model. The chosen pair with no exterior common
neighbour remains fixed. Applying the two-paths theorem to
`H-{v,u1,w1}` with order `u2,u3,w2,w3`, the separation outcome lifts
to a cut of order at most five, with `v` on one open side. Six-connectivity
excludes it directly. The disc outcome gives the exact count
`(3n'-7)+(n'-4)+12+2=4v(H)-9`. The external statement was checked as
Theorem 13 of [Norin--Totschnig](https://arxiv.org/html/2507.03244v1),
which quotes Robertson--Seymour--Thomas (2.4). This argument does not
depend on the older five-connected proof's auxiliary five-separation
argument or its endpoint labelling.

For degree seven, a whole exterior component has at least six
neighbours in the seven-vertex neighbourhood. Its contraction gives
exactly the prescribed nine-vertex quotient, and its fixed connected
preimage lifts every certified bag. The verifier's graph generation,
all 750 seven-bag candidates, connectivity and contact checks were
inspected. A fresh execution on 21 September 2026 used

```text
UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache uv run python3 active/hc7_k7minus_degree7_quotient_verify.py
```

and returned 29 complement types, 232 attachment cases, support orders
`{7: 67, 8: 102, 9: 63}`, and certificate digest

```text
b98ac56930aa7044c3a6a7c029b75cd85feb39f4dabd8476a0ba7f08ccdb7306
```

All cases passed, including the verifier's known positive and negative
instances. The computation proves this finite quotient lemma; the
written component contraction is what makes the host conclusion
unbounded.

## C21 and remaining trust boundaries

The final invocation of DNR Theorem 1.6 was checked in its exact primary
statement: a target-free graph of chromatic number at least seven with
every proper minor six-colourable has seven-connectivity and density
at least `4v-2`. A minor-minimal counterexample meets those hypotheses
and is therefore 4-bilight. The proved extremal theorem applies.

No unresolved inference was found in the audited source. The imported
external theorems, the separately audited rooted inputs and the stated
finite verifier remain its trust boundaries. The conclusion is C21
and the stronger stated density theorem, not HC7 or external peer
validation.
