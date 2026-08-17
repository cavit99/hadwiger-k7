# Independent cold audit: the critical full-exterior reduction

**Verdict:** **GREEN**.  This is an internal independent audit, not external
peer review.

The audited source is

```text
active/hc7_k7minus_critical_degree_eight_full_exterior_reduction.md
SHA-256 c7cb794dd0298b1cbe98ac4ee1bdbbf04f1e5c546ae26f195fcbb034602b0c0d
```

No correction is required within the stated scope.

## 1. Exterior topology

The source applies the independently audited exterior-connectedness theorem
at exactly its hypotheses: seven-connectivity, a degree-eight centre, local
minimum degree three, no literal `K_4`, and independence number three.  Thus
the nonempty exterior has a unique component `C`.  Its neighbourhood is a
subset of the eight local vertices.  Seven-connectivity makes its order at
least seven, so the component is either full or misses exactly one local
vertex `r`.

If it misses `r`, then `r` has no neighbour outside `N[v]`.  Consequently

```text
d_G(r)=1+d_J(r).
```

The critical-host hypothesis `delta(G)>=8` forces `d_J(r)=7`; there is no
unmentioned exterior contribution.  The exact one-miss verifier was rerun
against NetworkX 3.6.1 and returned

```text
GREEN connected one-miss exterior reduction
degree_viable_profiles=13
rooted_completion_eliminated=9
residues=[('GhCKN{', 7), ('GhEJE{', 7),
          ('GhEMNw', 7), ('GjSKN[', 7)]
canonical_completion_digest=7f684013b80ac226fddbc73405c7698a9040a01aaf1e58c0d8d9d1b432fa0500
```

The missed-vertex degrees in these four labelled residues are respectively
`7,6,6,6`.  Decoding `GhCKN{` gives precisely a universal vertex `r` joined
to the seven-cycle on the other local vertices.  Hence the finite reduction
is used with the correct label and cannot discard another degree-seven case.

## 2. Boundary reflection

Let `S=V(J)-{r}`.  Then `G-S` has the anticomplete shores `C` and
`{v,r}`.  Both singleton subgraphs `{v}` and `{r}` are connected and
`S`-full, and they are adjacent to one another.  On the cyclic labelling
from the source,

```text
I_1={s_2,s_4,s_6},   I_2={s_3,s_5},   Q={s_0,s_1}
```

has `I_1,I_2` independent and `Q` a two-vertex clique.  Lemma 1 of the
critical seven-cut capacity theorem therefore applies exactly: assign the
two nonsingleton blocks to `{v},{r}` and retain the two singleton blocks in
`Q`.  The contraction is proper and its four block images form a clique.
The reflected colouring of `G[C union S]` consequently induces exactly the
four displayed blocks, so exactly four colour names occur on `S`.

The two unused names colour `v` and `r` distinctly.  Both vertices are
complete to `S`, they are adjacent to one another, and both are anticomplete
to `C`.  Every restored edge is therefore proper.  This gives a
six-colouring of `G`, contradicting `chi(G)=7`.

The reflection input was checked at

```text
results/hc7_k7minus_critical_seven_cut_capacity.md
SHA-256 d4d650fee168fc2ff0e00a3b7b0faed6ff674ba8cd3c06c263f63c4170656f34
```

and its adjacent GREEN audit is pinned at
`e8daca42d069e76d13cd317799bdc97f32e300268ec49078dd9dd2d255fff478`.

## 3. Dependency and scope check

The other frozen inputs have the source hashes stated in the theorem:

```text
3654719b95d3a6b3446d5c15630ee474b07725568cf38a4ad426d0a3635a1fcf
  exterior connectedness
bda284fabf9a414f73dee683474be3cf00d1bc973bc4d51c8f43b8d7771ad607
  one-miss reduction
b27f6cacd4122e01efb65d4d714f28d2a7da7ff7552768cbec2281d9de8ef5c0
  one-miss verifier
```

The first input has a separate independent cold audit.  The one-miss result
is an exact finite reduction plus an unbounded rooted-completion lift; the
fresh verifier run reproduced its pinned digest.

The conclusion is deliberately conditional on a nonempty exterior.  It
does not eliminate the connected full component, prove an incident
codegree-two edge, prove the universal six-connected `4n` theorem, or prove
the Norin--Totschnig conjecture.  No such conclusion is imported implicitly.
