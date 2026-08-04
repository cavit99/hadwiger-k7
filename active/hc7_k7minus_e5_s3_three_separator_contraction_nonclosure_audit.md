# Internal audit: inherited four-cut after a three-separator contraction

**Verdict:** **GREEN** for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.

**Audited source:**
`active/hc7_k7minus_e5_s3_three_separator_contraction_nonclosure.md`

**SHA-256:**
`4f4a5658b061841e6a8318b469b51bc5f9dbe6ad31709d4bef35ad57b53d32b8`

No mathematical correction is required at this revision.

## 1. Neighbourhoods and the contraction count

In both order-three atomic forms, the degree-five leaf has

```text
N_G(t)={x,y,u_t,p,q}.
```

In the singleton form, `N_G(p)=T union {t,q}`.  In the edge form, every
neighbour of `p` lies in `{b,t,q} union T`, while `b` is not adjacent to
`t`.  The singleton lobes `x,y` have no neighbour in `A`.  Consequently,
in either form,

```text
N_G(p) intersect N_G(t) subseteq {q,u_t}.
```

The common neighbour `u_t` occurs only when it is one of the adhesion
vertices adjacent to `p`.  Contracting `pt` therefore removes its own edge
and at most two duplicate edges.  Since the minimum enemy has
`|E(G)|=4|V(G)|-7`, the quotient `J=G/pt` satisfies

```text
|E(J)|>=4|V(G)|-10=4|V(J)|-6.
```

No possible common neighbour has been omitted from this count.

## 2. Exact four-connectivity and the inherited cut

Let `z` be the contracted vertex.  If a cut of `J` of order at most three
avoids `z`, uncontracting `z` replaces it by the adjacent pair `p,t` in a
single component, so the same cut disconnects `G`.  If the cut contains
`z`, replacing `z` by `p,t` gives a cut of `G` of order at most four.
Both alternatives contradict five-connectivity.  Hence

```text
kappa(J)>=4.
```

The further singleton cut has

```text
N_G(q)={t,p,b} union R_0,          |R_0|=2.
```

After contracting `pt`, the vertex `q` has neighbourhood exactly

```text
N_J(q)={z,b} union R_0.
```

Deleting this four-set still separates the singleton `q` from the
nonempty opposite side of the old five-cut.  It is therefore an actual
four-cut of `J`, proving `kappa(J)=4`.  The proposition exhibits this cut;
it does not claim that it is the unique four-cut of `J`.  Thus the stated
nonclosure is exact: contraction guarantees no *new* cut because the
known cut already certifies the connectivity drop.

## 3. Norin--Totschnig Theorem 6

The primary source states precisely that every four-connected graph `H`
with

```text
|E(H)|>=4|V(H)|-8
```

has a `K_7^vee` minor unless `H` is isomorphic to `K_{2,2,2,2}`.  Here
`K_7^vee` is obtained from `K_7` by deleting two edges incident with one
vertex.  Proposition 1 verifies four-connectivity of `J`, and its density
is two edges above the theorem's threshold.  The exceptional graph has
eight vertices and twenty-four edges, whereas the bound for an
eight-vertex `J` is at least twenty-six.  The exception is therefore
genuinely impossible, and the conclusion

```text
K_7^vee is a minor of J
```

is valid.

The cited source was checked directly:

> S. Norin and A. Totschnig, *Every graph with no `K_7^vee`-minor is
> 6-colorable*, Theorem 6, arXiv:2507.03244.

## 4. Why the published conclusion does not close the atom

Because `J` is a minor of the target-free graph `G`, it cannot contain
`K_7^-`.  The theorem supplies only the weaker near-clique.  It neither
nominates the contracted vertex `z` nor prescribes which branch set has
the two missing adjacencies.

If a supplied model avoids `z`, the same branch sets use only untouched
vertices and have exactly the same inter-bag adjacencies in `G`; the model
does not automatically improve.  If it uses `z`, replacing `z` within
its bag by the connected pair `{p,t}` lifts the `K_7^vee` model, but no
published conclusion splits or reroutes that bag so as to create one of
the two missing adjacencies.  Recovering either missing edge would give
`K_7^-`, but that is an additional labelled assertion.

The final model-or-cut statement is therefore correctly presented as a
repair lemma for the remaining singleton atom, not as a proved dichotomy.
A distinct four-cut alone is also not claimed sufficient: the proposed
second outcome explicitly requires its lift to give strict lexicographic
high-excess descent.  The finite quotient calculation is labelled
diagnostic and is not used to infer an unbounded theorem.

The subsequent edge-atom reduction justifies narrowing the repair to the
singleton.  Writing `k=|N_G(p) intersect T|`, its two cases are exhaustive.
For `k=2`, the exact neighbourhood

```text
N_G(p)={b,t,q} union (N_G(p) intersect T)
```

has order five and its deletion isolates `p`; the exterior-connectivity
argument makes this precisely another singleton atom.  For `k=3`, the
density-safe `bq` contraction gives an exact companion cut.  Its only
surviving twin placement has boundary `{b,p,q,x,y}`, low side equal to the
`K_2` component of `G[S]`, and the rooted six-bag model in the high shore.
The four clique bags, the helper containing `y`, and the two low roots
form seven bags with at most one missing adjacency.  Hence that case gives
`K_7^-`.  The edge atom is therefore either relabelled as the singleton
atom or eliminated; it is not a further terminal case.

## 5. Dependencies and scope

The local atomic descriptions and the removal of the four-separator branch
were checked at these revisions:

```text
atomic six-boundary reduction:
eccb5d2e0181f0f7005bd7e86dce7f04b6bd9eb2f3eb5bd1e20a00a2f86afc34

companion-cut elimination:
225268556f3ab70e628cab8511e290658030c796aa3c15b9a6787f096de54654

edge-atom elimination:
47a65bd011a0cebe8e8a224a3cb9c984753461096ff746dafbbc408d664263a3
```

The argument proves neither that the inherited four-cut is unique nor
that every `K_7^vee` model fails to extend.  It identifies the first
unsupported labelled inference in this contraction route.  The edge atom
has been reduced to, or eliminated in favour of, the singleton case; that
singleton order-three atom remains open.  The note proves neither `(E5)`
nor the primary seven-connected density theorem.
