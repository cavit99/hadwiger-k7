# Internal audit of the unique-owner connector reduction

**Status:** separate hash-pinned internal audit.

**Verdict:** **GREEN for the written theorems and exact nonclosure.**  The
three surviving pole-incidence orbits, the opposite-side-deficiency bounds,
the imported four-boundary-rooted `K_4` theorem, the contracted-shore
pole--owner merge, its exact deficiency table, and the displayed terminal
minor models are valid under their stated hypotheses.  Corollary 3.5
correctly applies the spanning star-nonadjacency dichotomy and has exactly
the four displayed exceptions.  Proposition 3.6 and Theorem 3.7 validly
remove those exceptions and reduce every unique-owner pattern to a
forbidden minor or an actual nested separator.  The note correctly does
not claim that the resulting separator is trace-preserving, that the final
connector exists, or that the five-centre two-cut branch is closed.

## Audited revision

This audit checks the material revision of
`hc7_k7minus_five_centre_owner_nonedge_connector.md` at SHA-256

```text
307706b79fe81a1056b5c10fac2deee92787ecd465fff27c7e787b7adf35ffb9
```

The current source SHA-256 is
`338babb0b0a7ac1ed61756e150c653d7888ae9a67d01b86407cde5f1d0a80fdb`;
the only subsequent source change was the status line recording this GREEN
audit.

The immediately preceding GREEN audit checked source revision
`928c00c0fbccc3e078f33c727517acb1ce85a74cb2c40a12b084f605d400d063`,
whose material revision was
`4caaa752ea571144f98981e35b2860edb6ed64543210e53c8accd6980e7a229f`.
Earlier GREEN audits checked source revisions
`5ce603c2ed74d53fed672e3577382455eac1c6bc39c8cfc41648a238810350fb`
and
`7112d651f1f9b94cf076aa6010b43cea0c68b9504bc8343cd7bb9c46b44c9deb`,
whose material revisions were respectively
`c664fdbb1c91d71fbff8bd6bb93bc4f572b326c2a2c654b230d56d08955b4b76`
and `c0cadf0fb7ba28aab8522e662304f83e1d51f21b75e12b990eb66b8b9ecd53f6`.
The present audit preserves that coverage and additionally checks
Proposition 3.6, Theorem 3.7, their spanning-model hypotheses and contact
counts, and the revised exact nonclosure statement.

The principal pinned dependencies checked were:

| dependency | source SHA-256 | audit SHA-256 |
|---|---|---|
| critical-completion model lift | `09ea5813b843a17e667d3f8cd4cebbf8094f2bceb39955d2ed873638e4f9afbf` | `5d34d44730031b7df2bd59de0d6c409f893810d37bc9e5d714990e55ffbfd5e8` |
| universal four-boundary rooted `K_4` | `0a2511508c313e06c47cf7837e823299be4dc665d0572a4a3b53fdde4a44191f` | `45bc4a6444615cee16f466491ec69a996d3fdc6b7eeffeacac2ab77170536493` |
| multiple-missing-adjacencies separator dichotomy | `b9c02238a4142647005745b96b7d94377fb897c3d589081388dca0a6718edad2` | `2641d766420090d76d42f7b7f40544ee78ba8ed57219f6e6ac737194b3cf0ee9` |
| five-centre two-cut reduction | `1917b5e3d183d44a2d905d2628272d10e4bc6f7ae0768b43cab0e9462b83332a` | `d01183c936d79ea2e07f956c2e89f7291df9cc28a5dab3dda6b093c8a69c4ea3` |
| three-root palette reduction | `e072f3edbffcf3f2116998213863feb6a6b53c3717cd2798fae94aa3ca79cc36` | `13e0657f12d6afa9b556dff279d8ef59a7423e4a398f8af4365e624367107623` |
| global five-root palette theorem | `b26f9f0d12822f93af55e3aa566fc75b985dcb5a17daa4ea2b329c8efea274c3` | `765df0db1168001a212c77e5f871abe4725d4c92cc4e11ae8d887ff808f92e6a` |
| synchronized-path theorem | `d044a7c7765d5b72b8aa469a188323bb48597cf22a9e6f318c82bccdf6afbedc` | `803c1a7fd1a69bd568fe5122fff1012f44ed7f4b2ffb17a6fd3a9e6fde1b0f4f` |

## 1. Pole-bag split and orbit classification

Deleting the essential added edge `pq` from the connected bag `B` leaves
exactly two components.  Thus the incidence encoding by `P`, `Q`, and `B`
is exhaustive.

Lemma 2.1 is valid in both degree-four and degree-five cases.  In the
degree-four case, if `R_j` is the unique owner bag missed by `B_p`, then
`B_q union R_j` is connected, the artificial edge makes it adjacent to
`B_p`, and at most the old `R_aR_b` adjacency can remain absent.  The poles
are in distinct bags, so the audited critical-completion lift applies.

The incidence count in Theorem 2.2 is exact.  If `m` owner bags are
two-sided, the two pole degrees sum to `5+m`; Lemma 2.1 bounds each by
three, so `m<=1`.  For `m=0`, the missing-edge owners are on opposite
sides, together on the degree-three side, or together on the degree-two
side.  For `m=1`, the two-sided bag is an ordinary owner with the missing
pair split, an ordinary owner with that pair together, or an endpoint of
the missing pair.  These are exactly the six table rows.

Each of the three displayed terminal contractions was checked bag by bag.
The possible missing pairs are respectively `B_qR_b`, `B_qR_b`, and
`B_qR_c`, as stated.  An independent enumeration of the seven-vertex graph
`K=J-x` reproduced the table (2.4):

```text
code    |E(K)|   max_v |E(K-v)|   max_{uv != B_pB_q} |E(K/uv)|
PQBPQ     16            12                       13
PQPPQ     15            12                       13
PPPQQ     15            12                       13
```

The completeness argument for seven bags on eight vertices is also sound:
such a model either uses seven singleton vertices or all eight vertices
with exactly one connected two-vertex bag.  The excluded contraction
`B_pB_q` is precisely the same-pole-bag placement, so it is correctly not
treated as a distinct-pole lift.

## 2. Opposite-side repairs

In Theorem 3.1, pair feasibility gives disjoint connected subgraphs: a
`p`--`q` path and a component containing `z_a,z_b`.  Splitting one path in
each subgraph repairs `B_pB_q` and `R_aR_b`.  The rooted instance contains
no other centre, so adjoining the remaining three centres as singletons
does not create an overlap.  Every nondeficient one-sided owner supplies
exactly its formerly absent pole-component adjacency, leaving at most the
one allowed missing edge.

## 3. Four boundary vertices root a `K_4`

Lemma 3.2 now invokes the promoted universal four-boundary rooted-`K_4`
theorem rather than repeating its proof.  The dependency has the same
five-centre two-cut hypotheses, the same oriented distinct-response shore
`D`, and the same boundary `S`; it concludes the required rooted model for
every four-set `Q subseteq S`.  Its source and GREEN audit hashes match the
table above, so this substitution loses no hypothesis or conclusion.

## 4. Three deficient owners

Theorem 3.3 has no hidden branch-set collision.  The four rooted bags lie
in `D union {p,q,z_i,z_j}`.  They are enlarged respectively by
`B_p,B_q,R_i,R_j`; every unselected centre remains an unused singleton and
is enlarged only with its own owner bag.  The rooted clique repairs the
pole-pair edge and both selected owner deficits.  A nondeficient unselected
one-sided owner is repaired by its own centre.  Thus, when at most two
owners are deficient, only `R_aR_b` can remain absent.  When exactly three
are deficient and include both `a,b`, selecting those two repairs
`R_aR_b`, and the third deficient owner supplies the sole missing edge.
Both constructions are valid `K_7^-` models.

## 5. Contracted-shore pole--owner merge

For Theorem 3.4, the seven displayed sets are disjoint and connected.
The shore bag `D` is adjacent to both pole bags by fullness and to every
enlarged owner bag through the corresponding centre.  The merged bag
`M=B_s union R_j union {z_j}` is connected because `B_sR_j` and
`z_jR_j` are edges.

Every possible missing pair is exactly one of the four listed types.  The
pair `MB_t` can fail only for a deficient one-sided `j`.  A remaining
owner bag can fail to meet `B_t` only when it is deficient and lies on
side `s`.  If `j` is not an endpoint of the owner nonedge, `R_a'R_b'`
remains the sole possible owner--owner nonedge.  If `j` is an endpoint,
its merged bag meets the other endpoint through `B_s` when that endpoint
lies on side `s`, and through the other centre when that endpoint is
nondeficient on side `t`; the stated fourth type is the only failure.
These four branch-set pairs are distinct, so their indicator sum is
formula (3.5).

An independent enumeration of (3.5), over every eligible deficient set
allowed by Theorem 3.3 and every permitted `(j,s)`, reproduced the complete
table:

```text
code    three deficient                              four deficient                                      five
PQBPQ   ade:2 bde:2                                  abde:3                                               n/a
PQPPQ   acd:1 ace:2 ade:2 bcd:1 bce:2 bde:2 cde:1  abcd:2 abce:3 abde:3 acde:2 bcde:2                  abcde:3
PPPQQ   acd:2 ace:2 ade:1 bcd:2 bce:2 bde:1 cde:1  abcd:2 abce:2 abde:2 acde:2 bcde:2                  abcde:3
```

The six entries of value one were also checked directly.  The listed
witnesses leave respectively the following single absent pairs:

```text
PQPPQ acd, (b,q):  M R_a'
PQPPQ bcd, (b,q):  M B_p
PQPPQ cde, (b,q):  B_p R_e'
PPPQQ ade, (b,p):  B_q R_a'
PPPQQ bde, (a,p):  B_q R_b'
PPPQQ cde, (a,p):  B_q R_c'
```

All other branch-set pairs have a literal edge identified in the theorem's
proof.  These are therefore six valid explicit `K_7^-` minor models, and
the exclusions in (3.6) are sound.  Entries of value at least two are
correctly stated only as limits of this construction.

## 6. Star nonadjacencies and the nested separator

The sets in (3.4) span `V(G)`: `B_p,B_q,R_a,...,R_e` partition
`C union {p,q}`, each centre is assigned to its unique owner bag, and
`D` is the remaining bag.  Therefore, whenever all absent pairs share a
common endpoint, that endpoint can play `X` in the audited
multiple-missing-adjacencies theorem and the other six bags are pairwise
adjacent.  If there are zero or one absent pairs, the same seven bags are
already a `K_7^-` model; if there are at least two, the cited dichotomy
applies exactly.

I independently enumerated the literal absent pairs from formula (3.5),
not merely their number.  Every row and choice in Corollary 3.5 has the
stated value of `r` and the stated common endpoint.  Searching every
permitted `(j,s)` for every admissible deficiency set found exactly four
sets for which there is neither at most one absent pair nor an
edge-star:

```text
PQBPQ  abde
PQPPQ  abce  abde  abcde
```

Thus (3.7) is exact for this pole--owner merge.  The dependency returns a
nonempty proper connected donor piece with connected complement and an
actual open-neighbourhood separator.  Seven-connectivity supplies the
order lower bound and the equality-case fullness, exactly as stated.  It
does not supply a seven-vertex separator or retain either shore colouring,
so the source correctly leaves this outcome nonterminal.

## 7. Near-clique donor dichotomy

Proposition 3.6 correctly weakens the six outside bags from a clique to a
clique with at most one edge absent.  Since `X` misses a nonempty outside
bag, `N_G(X)` is an actual separator.  Its at least seven vertices occupy
at most five contacted bags, so one contacted donor contains two distinct
portals `p,q`.

In the avoidable-core case, the connected complement `W` retains every
existing donor contact.  Absorbing the component `Y` containing the second
portal into `X` repairs every `X`-nonadjacency when `Y` meets all missed
bags.  The only possible nonedge left among the seven new branch sets is
the original one among the six `U`-bags.  If `Y` misses one of the bags
missed by `X`, that bag is a literal far side of `N_G(Y)`.

In the unavoidable case, `Z_p,Z_q` are connected, have connected
complements, and are disjoint.  The index set in (3.10) omits only a
possible original donor nonneighbour.  If either monopoly set in (3.13)
were empty, the relevant connected complement would still meet every
*existing* donor contact and would be a forbidden retaining core.  Thus
both monopoly sets are nonempty.  A portal set contained in `Z_p` has no
vertex in the disjoint set `Z_q`, so its foreign bag is anticomplete to
`Z_q` and supplies the required far side.  No adjacency to the possible
six-bag nonneighbour is needed in this argument.

The order and equality-case fullness conclusions are the standard direct
consequences of seven-connectivity.  No hidden assumption that `X` misses
two bags is used.

## 8. Universal rooted-`K_4` spanning enlargement

Theorem 3.7 applies the audited rooted-`K_4` theorem to
`p,q,z_a,z_b`.  After contracting its four rooted bags, a multi-source
spanning forest assigns every remaining vertex of the connected closed
`D`-shore to exactly one root.  Expanding gives four disjoint connected,
pairwise adjacent bags which partition `D union {p,q,z_a,z_b}`.

Enlarging these bags as in (3.14) is disjoint and spanning.  The pole bags
meet their rooted bags at `p,q`; the owner bags `R_a,R_b` attach through
the ownership edges at `z_a,z_b`; and each ordinary owner is enlarged only
by its own centre.  The rooted clique repairs the pole-pair edge, every
pole contact at the two exceptional owners, and `R_aR_b`.  The old
owner-bag edges supply every other owner--owner contact.

The only candidate nonedges are therefore exactly

```text
PQBPQ: U_q U_d;                         U_p U_e
PQPPQ: U_q U_c, U_q U_d;                U_p U_e
PPPQQ: U_q U_c;                         U_p U_d, U_p U_e.
```

They are two pole-centred stars, and one star has at most one leaf in each
code.  With at most one absent edge the seven bags are already terminal.
Otherwise choosing the centre of the nonempty larger star as `X` leaves at
most one nonedge among the other six bags, so Proposition 3.6 applies.
This verifies every code and leaves no deficiency-pattern exception.

The revised nonclosure is exact.  If the donor piece lies in an ordinary
bag `U_i=R_i union {z_i}`, unique ownership and independence of the five
centres give `N_G(Y) cap Z subseteq {z_i}` whether or not `Y` contains
`z_i`.  Thus the argument cannot identify its separator with
`Z union {r,s}`; it also gives no upper bound of seven or retained boundary
partition.

## 9. Connector and synchronized-path residue

The four connector subgraphs have the exact boundary intersections needed
for disjointness.  The path `L` reconnects the two components of `B`, the
adjacent sets `Q_a,Q_b` repair the sole owner-bag nonedge, and the ownership
edges connect every enlarged owner bag.  The stated five-of-six adjacency
condition on `W` therefore leaves at most one missing branch-set
adjacency.

In Section 5, each rainbow contact triangle avoids the two-colour pole
path and belongs to a unique component after its open interior is deleted.
The synchronized-path attachment inequality gives the claimed bounds, and
the fact that `N_D(z_i)` is exactly its triangle gives the component
partition of `Z`.  Distinct components force every interior-`D`
`z_a`--`z_b` path to meet the pole path, exactly as stated.

## Unresolved scope

The audit does not establish any of the following, and the source does not
claim them:

- a five-boundary-rooted `K_5` on the `D`-shore;
- an owner-nonedge connector;
- a response-preserving smaller equality component; or
- closure of the order-at-least-eight five-centre two-cut branch.

Every unique-owner pattern now gives a forbidden minor or a nested
separator.  In a target-free host the exact residue is therefore the
non-trace-preserving separator outcome.  The simultaneous allocation and
rooted donor problems stated at the end of the source remain open.
