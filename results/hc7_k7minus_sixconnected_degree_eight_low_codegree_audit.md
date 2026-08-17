# Internal audit: six-connected degree-eight low-codegree theorem

**Verdict:** GREEN.  The theorem is correct within the stated
finite-computation trust boundary.
This is an internal mathematical audit, not external peer review.

## Exact revisions

The audited theorem is
[`hc7_k7minus_sixconnected_degree_eight_low_codegree.md`](hc7_k7minus_sixconnected_degree_eight_low_codegree.md),
SHA-256

```text
06d35e4059848517e65e48b04c592e948bbc8e4407501de75520cfa3e9d22844
```

The mathematical revision first audited had SHA-256
`b71679860eb466882f5bf8b92dd63e4a5742180df2fbdefc2c593a03f52b1e89`.
The only change between that revision and the final hash above is the
status paragraph recording and linking the two GREEN audits; no theorem
statement, hypothesis, proof, calculation, or scope claim changed.

The verifier is
[`hc7_k7minus_sixconnected_degree_eight_low_codegree_verify.py`](hc7_k7minus_sixconnected_degree_eight_low_codegree_verify.py),
SHA-256

```text
d721c181a8388feb7901e8ab04f704c19679cfb56551752756a45733f28d6fdc
```

## Finite lemma

Every order-eight graph is an extension of an order-seven atlas graph.
The invariant used for bucketing is isomorphism-invariant, and exact
isomorphism testing is performed within each bucket.  The minor recursion
is exhaustive: deletion removes unused vertices, while successive mergers
along spanning trees produce every connected branch set.  Every returned
model is checked for disjointness, connectivity, and at most one missing
interbag adjacency.

The pinned run under NetworkX 3.6.1 reproduces the counts

```text
424 local classes; 55 K_6^--minor-free classes; 2,035 profiles;
2,031 positive certificates; four negative profiles;
digest 8b9b31cae19b10a9e958a51dd2c8ef12193b655ec7ab2163b67b638dfc646501.
```

As an independent audit check, exhaustive enumeration of all seven-bag
partitions of the four negative ten-vertex quotients confirmed that each is
target-free.  Repeating it for all twenty-eight missed pairs in each fixed
labelled local graph confirmed that the displayed pair is unique.  Each
pair is an edge and both ends have local degree four.

## Unbounded host reduction

If the exterior of the degree-eight centre is empty, six-connectivity gives
minimum local degree five, so the audited complement lemma supplies a
`K_6^-` minor.  Otherwise every exterior component has at least six
boundary neighbours.  Contracting one whole component and deleting the
others produces exactly the quotient in Lemma 1, so every quotient is
target-free.  Uniqueness for the fixed labelled local graph forces every
exterior component to miss the same pair.  Its two vertices consequently
have total degree `1+4=5`, contradicting six-connectivity.  No bounded-order
assumption is made on the host or its exterior components.

## Contraction and defect consequences

At density `4n`, Jakobsen's strict noncockade bound gives average degree
less than nine.  Six-connectivity supplies minimum degree six, and the
hash-pinned degree-six and degree-seven results, together with Theorem 2,
exclude the assumption that every edge has codegree at least four.

For the defect ladder, contraction of the supplied edge preserves
coefficient-four density and lowers connectivity by at most one.  In the
six-connected base case the quotient is at least five-connected, which
excludes every nontrivial four-sum cockade; density excludes both base
graphs.  Thus Jakobsen gives `D(G/e)>=25`.  Exact accounting,

```text
D(G/e)=D(G)-7+2c(e),
```

and `c(e)<=3` give `D(G)>=26`.  Induction gains at least one unit of defect
per additional unit of connectivity, proving `D(G)>=20+r`.  The critical
host identity `D=b-tau` therefore gives `b>=27+tau`.  This deduction is not
circular: the low-codegree theorem and Corollary 3 do not use the defect
ladder.

## Returned cut

For a minimum-order six-connected enemy, contraction gives

```text
|E(G/uv)| >= 4|V(G/uv)|+s.
```

The quotient is at least five-connected and cannot be six-connected by
minimality.  A five-cut avoiding the contraction vertex would already cut
the original graph; every five-cut therefore contains that vertex and
lifts, after splitting it, to an order-six cut.  The audited exact six-cut
localisation theorem then gives fullness, two or three components, and the
boundary bounds.  Its identity with `q_G=s+2` is exactly

```text
|E(G[S])| + sum_i eta_i = 24+s,
```

which yields the two displayed excess lower bounds `13+s` and `16+s`.
The theorem correctly leaves both returned rows open.

## Second independent cold audit

**Independent verdict:** **GREEN** for the final theorem hash
`06d35e4059848517e65e48b04c592e948bbc8e4407501de75520cfa3e9d22844`
and verifier hash
`d721c181a8388feb7901e8ab04f704c19679cfb56551752756a45733f28d6fdc`.
This audit was conducted separately from the audit above and attempted to
falsify both the finite classification and every unbounded deduction.

### Independent finite checks

A separate checker enumerated minor models as set partitions, rather than
by the verifier's contraction recursion.  For a ten-vertex graph and seven
branch sets, the numbers of partitions by support order were

```text
support order       7      8       9      10
partitions        120   1,260   4,620   5,880
total per graph                         11,880
```

The checker independently tested connectivity in every bag and counted
interbag nonadjacencies.  Its results were:

- all `89,676` pairs among the `424` local representatives were
  nonisomorphic;
- the `369` positive local classes had independently valid `K_6^-`
  certificates, while exhaustive partition enumeration rejected a
  `K_6^-` model in each of the other `55` classes;
- all `2,031` positive exterior profiles had independently valid
  `K_7^-` certificates;
- exhaustive enumeration of all `11,880` seven-bag partitions rejected a
  `K_7^-` model in each of the four negative quotients; and
- the recursive and partition engines agreed on `60` fixed-seed random
  ten-vertex graphs of densities ranging from `0.20` to `0.80`.

Scanning all `55(1+8+28)=2,035` profiles left exactly

```text
('GLNM^_', (5,6)), ('Gfwhmk', (0,1)),
('Gfwhm{', (0,1)), ('GxNg~k', (0,1)).
```

Each positive classification was therefore supported by a model checked
without the verifier's model-checking routines, and each negative
classification by exhaustive absence.  Four additional random relabellings
transported the unique missed pair correctly.  This rules out a hidden
dependence on the representative labels or graph6 labelling.  A fresh run
of the repository verifier also reproduced all stated counts and the
certificate digest
`8b9b31cae19b10a9e958a51dd2c8ef12193b655ec7ab2163b67b638dfc646501`.

### Independent proof reconstruction

The finite universe is complete.  Deleting any named vertex from an
eight-vertex graph gives an order-seven graph isomorphic to one of the
`1,044` atlas graphs, and transporting the deleted vertex's neighbourhood
gives one of the `128` extensions tested.  Isomorphism-invariant bucketing
cannot merge nonisomorphic graphs because the final comparison is exact;
the pairwise test above also found no duplicate representatives caused by
an invariant split.

For Theorem 2, `d_J(x)=c(vx)` is exact.  If the exterior is empty,
six-connectivity gives `delta(J)>=5`, so the separately audited
eight-vertex complement lemma applies.  Otherwise, every component of
`G-N[v]` has at least six neighbours in `N(v)`.  Contracting one entire
component creates no `vc` edge and gives precisely the finite quotient.
Because the labelled local graph `J` is fixed, uniqueness of its missed
pair forces every exterior component to miss the same adjacent degree-four
pair.  Both ends then have degree exactly five in `G`, the required
contradiction.  No finiteness assumption is made about any exterior
component.

For Corollary 3, density `m>=4n` forces order at least nine.  Jakobsen's
strict noncockade inequality gives average degree below nine, whilst
six-connectivity gives minimum degree at least six.  The three possible
minimum degrees `6,7,8` are excluded under the contrary assumption
`c(e)>=4` by the audited degree-six bound, degree-seven exclusion, and
Theorem 2 respectively.

For Corollary 4, contracting an edge of a six-connected graph leaves an
at-least-five-connected graph: a cut avoiding the new vertex lifts
unchanged, while one containing it lifts after replacing it by both ends.
The density calculation is

```text
m(G/e)=m(G)-1-c(e) >= 4n-4 = 4|V(G/e)|,
D(G/e)=D(G)-7+2c(e).
```

Jakobsen therefore gives `D(G/e)>=25`; `c(e)<=3` gives `D(G)>=26`.
The same connectivity lift and induction yield `D(G)>=20+r`, and the
critical-host identity `D=b-tau` gives `b>=27+tau`.

Finally, a five-cut of the contracted minimum enemy cannot avoid the
contraction vertex, and splitting that vertex lifts it to an actual
order-six cut of the original graph.  Substitution of `q_G=s+2` into the
audited localisation identity gives exactly

```text
|E(G[S])| + sum_i eta_i = 24+s,
```

and hence the lower bounds `13+s` and `16+s`.  No stronger composition
claim is inferred from these formulas.

The imported theorem revisions checked in this reconstruction were:

| input | SHA-256 |
|---|---|
| eight-vertex complement lemma | `2ffeb857f4c999abc14bc28cd4650332d9397a140c601929117376f38f637449` |
| degree-six common-neighbour bound | `e157c0e8fa5805cee15888abb9a002d35d51d7e877154e7eee1a37627732493e` |
| degree-seven common-neighbour exclusion | `663c1b7e0de9b0951de89801d52baf4aae12535d7807547d19d04fc10b00c4b0` |
| exact six-cut localisation | `f2a4480d27556996620117a68a8a7924dd61cf37bf5ec9e8cce4c953dfcc88af` |

Jakobsen's threshold was also checked in the exact form quoted as Theorem 2
by Albar: at least `9n/2-12` edges force a `K_7^-` minor or a
`(K_{2,2,2,2},K_6,4)`-cockade.  No counterexample, labelling gap,
quantifier error, circular dependency, or arithmetic error was found.
