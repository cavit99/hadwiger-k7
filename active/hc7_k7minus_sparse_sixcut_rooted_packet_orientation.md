# Rooted-model packet orientation in a returned six-cut

**Status:** written unbounded proof, pending separate audit.  Five full
packets are always terminal, and a four-rooted `K_4` in one lobe forces
each other lobe to have full-packet packing number one.  Combined with the
audited forced-rooted-model theorem, this gives an exact packet-vector
orientation of the sparse three-component residue.  It does not bound the
excess of the unique model-bearing lobe.

Let `G` be a six-connected graph with no `K_7^-` minor, let `S` be a
six-vertex cut, and suppose that `G-S` has exactly three components.  A
connected subgraph of a component is an **`S`-full packet** if it has a
neighbour at every vertex of `S`.  Write `mu_S(C)` for the maximum number
of pairwise vertex-disjoint `S`-full packets in a component `C`.

Every component is `S`-full, so `mu_S(C)>=1`.

## Lemma 1 (five packets are terminal)

Across all three components of `G-S`, there are at most four pairwise
disjoint `S`-full packets.

### Proof

Suppose that `P_1,...,P_5` are five such packets.  Choose distinct roots
`s_1,...,s_4 in S`, and write `S-{s_1,...,s_4}={x,y}`.  The seven sets

```text
P_i union {s_i}  (1<=i<=4),   P_5,   {x},   {y}       (1)
```

are disjoint and connected.  The five packet bags are pairwise adjacent:
for two anchored bags, either anchor has a neighbour in the other packet,
and an anchored bag meets the bare packet through its anchor.  Every
packet bag meets both singleton roots by fullness.  Thus the only possible
missing adjacency in (1) is `xy`.  The seven bags form a `K_7^-` model, a
contradiction.  \(\square\)

## Lemma 2 (a rooted model makes the other lobes packet-thin)

Let `C,A,D` be the three components, let `Z subseteq S` have order four,
and write `S-Z={p,q}`.  If `G[C union Z]` contains a `Z`-rooted `K_4`
model, then

```text
mu_S(A)=mu_S(D)=1.                                    (2)
```

### Proof

Suppose that `A` contains two disjoint `S`-full packets `Q_1,Q_2`.  Let
`R_z`, `z in Z`, be the four bags of the rooted model.  The seven bags

```text
(R_z:z in Z),   Q_1 union {p},   Q_2 union {q},   D   (3)
```

are disjoint and connected.  The first four form a clique.  Each of the
last three meets every rooted bag through the literal root in that bag.
The two anchored packet bags are adjacent because `Q_2` has a neighbour
at `p`; and the bare component `D` meets them through its neighbours at
`p` and `q`, respectively.  Hence (3) is a `K_7` model, a contradiction.
Thus `mu_S(A)=1`.  Interchanging `A,D` proves the other equality.  \(\square\)

## Theorem 3 (exact packet orientation after the forced rooted model)

Assume additionally the returned-cut density identity

```text
|E(G[S])|+sum_C eta(C)=24+sigma,   sigma>=0,
```

where

```text
eta(C)=|E(G[C])|+|E_G(C,S)|-4|C|.
```

Then at least one lobe has a four-rooted `K_4` model.  If exactly one lobe
has any such model, the packet vector, up to permutation, is

```text
(1,1,1) or (2,1,1),                                  (4)
```

with the possible entry two belonging to the model-bearing lobe.  If at
least two lobes have rooted models, then the packet vector is exactly

```text
(1,1,1).                                              (5)
```

### Proof

The audited closure of the all-no-rooted-`K_4` branch supplies a rooted
model in some lobe `C`.  Lemma 2 makes the other two packing numbers one.
Lemma 1 and the lower bound one on every packing number give
`mu_S(C)<=2`, proving (4).  If another lobe also has a rooted model, apply
Lemma 2 with that lobe in the model-bearing role; it forces
`mu_S(C)=1` as well, proving (5).  \(\square\)

## Scope

The argument uses only literal full packets.  It does not assign the two
omitted roots to arbitrary four-root carriers.  The sole packet-rich
residue is therefore precise: exactly one lobe may bear all currently
known rooted models and have two full packets, whilst both opposite lobes
are packet-thin.  Eliminating that orientation requires an excess or
rooted-model theorem inside the unique rich lobe, not a further raw packet
count.

## Conditional closure target

The exact remaining local statement is the packet-weighted excess bound

```text
eta(C)<=5 mu_S(C).                                    (6)
```

If (6) holds for every lobe in this setting, then the entire sparse
three-component returned row is impossible.  Indeed, Lemma 1 gives
`sum_C mu_S(C)<=4`.  When `Delta(G[S])<=1`, the boundary is a matching and
has at most three edges, so (6) gives

```text
sum_C eta(C)<=20<24+sigma-|E(G[S])|.
```

When `Delta(G[S])>=2`, the audited connector--anchor packet completion
makes every packing number one.  Hence (6) gives

```text
sum_C eta(C)<=15<24+sigma-|E(G[S])|,
```

because the unresolved sparse boundary has at most six edges.  Both cases
contradict the returned density identity.

Statement (6) is **not proved here**.  It is recorded without weakening as
the sufficient unbounded theorem: five-rooted `K_5^-` models are already
terminal, so the substantive local target is to prove (6) under their
absence.  An order-independent proof of (6), rather than a finite packet
classification, would close the returned three-component programme.

## Dependencies

- The forced rooted-model input is
  [`hc7_k7minus_sparse_sixcut_no_rooted_k4_closure.md`](hc7_k7minus_sparse_sixcut_no_rooted_k4_closure.md),
  source SHA-256
  `23ee073a1df5ccca13dfab57e0307e152bb49183b72315554e298f0d9aaade49`,
  with adjacent GREEN cold-audit SHA-256
  `c83f04d601b88393037f62459a123620b89e77ec38f5972ddb513312348e91ac`.
- The returned density identity is the same audited input pinned in that
  source.
- The `Delta(G[S])>=2` packet-one conclusion is Corollary 4 of
  [`hc7_k7minus_sparse_sixcut_five_root_packet_reduction.md`](hc7_k7minus_sparse_sixcut_five_root_packet_reduction.md),
  source SHA-256
  `32c45ee41ee349e2499c82c49bd7a0af7cfd636620bbc7873edea4ca061e1100`,
  with adjacent GREEN audit SHA-256
  `b89582b3c4c4dfe0c03980c45c93b7fcad250241e6ef356273fd9f3fa2db7a89`.
