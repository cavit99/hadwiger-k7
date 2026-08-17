# Author-side audit: the critical full-exterior reduction

**Verdict:** **GREEN** for the theorem at SHA-256

```text
c7cb794dd0298b1cbe98ac4ee1bdbbf04f1e5c546ae26f195fcbb034602b0c0d.
```

This is an adversarial self-audit, not an independent or external review.

## 1. Component and degree reduction

The frozen exterior-connectedness theorem applies verbatim to the three
local hypotheses and gives at most one exterior component.  For a nonempty
component `C`, its neighbourhood lies in the eight-set `J`; omitting two
vertices would give a cut of order at most six, so it is full or one-miss.

In the one-miss case the missed vertex `r` has neighbours only in `J` and
at the centre `v`.  Thus the displayed identity

```text
d_G(r)=1+d_J(r)
```

is exact.  Minimum degree eight forces `d_J(r)=7`.  Directly decoding the
four frozen residues gives missed-vertex degrees `7,6,6,6`; the degree-seven
pair is `GhCKN{/7`, whose edge set is a universal vertex `7` joined to the
cycle

```text
01,12,23,34,45,56,60.
```

No isomorphism-dependent inference is hidden here: the verifier records
the graph6 code and the missed label as one labelled pair.

## 2. Exact reflection and extension

With `S=J-r`, deleting `S` leaves the two open shores `C` and `{v,r}`.
They are anticomplete because `v` has no exterior neighbour and `r` is the
vertex missed by `C`.  Both singleton subgraphs in the latter shore are
connected and `S`-full.

On the displayed cycle, `I_1={s_2,s_4,s_6}` and
`I_2={s_3,s_5}` are independent, while `s_0s_1` is an edge.  Lemma 1 of
the frozen critical seven-cut capacity theorem therefore applies with the
two non-singleton blocks assigned to `{v},{r}` and the two singleton
blocks retained as a literal clique.  Its contraction is proper and its
conclusion is an exact four-block equality partition on the opposite
closed shore `G[C union S]`.

Consequently exactly four of the six colour names occur on `S`.  The two
unused names can be given separately to `v,r`.  Their mutual edge is
proper; all their edges to `S` are proper; and neither vertex has an edge
to `C`.  This checks every edge added back and yields the claimed
contradiction.

The reflection source and its audit have SHA-256 hashes

```text
d4d650fee168fc2ff0e00a3b7b0faed6ff674ba8cd3c06c263f63c4170656f34
e8daca42d069e76d13cd317799bdc97f32e300268ec49078dd9dd2d255fff478.
```

The connectedness source has an independent cold audit at SHA-256
`cabdc970540a36c220cbadef367907735bb7f173bcd6a52f01f9bf4ed9947d53`.
The one-miss source/verifier hashes are pinned in the theorem, and its
adjacent author-side audit has SHA-256
`d60c0a1750ec34b9c12ed0fb35d5f2af66c63b1059d935fa227f3f8b776b0d61`.

## 3. Scope

The argument uses critical minor-colourability only through the reflection
lemma and uses minimum degree eight essentially.  It proves neither that
the exterior is nonempty nor that a connected full exterior is impossible.
No stronger conclusion is stated in the source.
