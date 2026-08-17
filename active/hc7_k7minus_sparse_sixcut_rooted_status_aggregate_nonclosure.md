# The rooted-status aggregate system does not close either packet orientation

**Status:** exact negative result with a deterministic verifier.  The
audited four-root no-model inequalities and cross-lobe singleton-transfer
bounds admit both surviving packet vectors at the exact returned density.
This is a barrier to that aggregate linear programme, not a target-free
graph construction.

Let `S` be a six-set and let `C_0,C_1,C_2` be three `S`-full components.
Write

```text
eta(C)=|E(C)|+|E(C,S)|-4|C|.
```

For a four-set `Z subseteq S`, let `R_i(Z)` record whether the closed
`C_i`-shore has a `Z`-rooted `K_4` model, and let

```text
n_i(Z)=|{v in C_i:Z subseteq N(v)}|.
```

The aggregate system considered here consists of the following audited
consequences.

1. If `R_i(S-{p,q})` is false, then

   ```text
   |E(C_i)|+sum_{z in S-{p,q}} a_z+|E(G[S-{p,q}])|
       <=3|C_i|+5.                                    (1)
   ```

2. Always `n_i(Z)<=2`; if `R_j(Z)` holds for another lobe, then
   `n_i(Z)<=1`.
3. Equivalently after summing singleton incidences,

   ```text
   sum_{v in C_i} binom(|N(v) cap S|,4)
       <=30-|R_j union R_k|.                          (2)
   ```

4. Some rooted status is present; five full packets are forbidden; and a
   rooted model in one lobe makes each other lobe packet-thin.
5. The exact returned density identity holds:

   ```text
   |E(G[S])|+sum_i eta(C_i)=24.                       (3)
   ```

## Theorem (exact aggregate nonclosure)

There are two explicit six-connected graphs of order `32` and size `128`,
each with a six-cut `S` and exactly three components, satisfying every
condition above.  Their data are

```text
G[S]          (eta(C_0),eta(C_1),eta(C_2))   packet vector
one edge                 (17,3,3)               (1,1,1)
independent              (18,3,3)               (2,1,1).
```

Thus (1)--(3), singleton-transfer, and packet orientation cannot by
themselves contradict either surviving packet vector.

### Construction

Both thin lobes are triangles.  Their three vertices have boundary
neighbourhoods

```text
0123, 0145, 2345.                                    (4)
```

Each root occurs twice.  Every two labels in (4) cover all six roots, so
the lobe is full and has packet number one.  Every vertex has total degree
six, the closed lobe is internally six-connected, and

```text
eta=3+12-4*3=3.                                      (5)
```

With independent boundary, exhaustive rooted-bag allocation finds no
four-rooted `K_4` in a thin lobe.  With boundary edge `05`, it finds the
exact five rooted four-sets pinned by the verifier.  In either case all
remaining instances of (1) hold.

The rich lobe has twenty vertices.  Its internal graph is the square of a
twenty-cycle with three disjoint edges removed in the packet-one case and
two disjoint edges removed in the packet-two case.  Every vertex has a
three-element boundary label.  The complete label lists are frozen in the
verifier.  They have the following properties.

- Every closed rich lobe is internally six-connected.
- Every four-set has a rooted `K_4` model with four bags of order two.
- No vertex has four boundary neighbours, so `n_0(Z)=0` for every `Z`.
- In the first construction only vertex `0` sees root `5`, forcing packet
  number one.
- In the second only vertices `0,10` see root `5`, and the disjoint edges
  `01` and `10,11` are two full packets, forcing packet number two.
- The rich excess is respectively `17` and `18`.

The boundary edge `05` in the packet-one case supplies the last incidence
needed for degree six at root `5`; in the packet-two case the two rich
neighbours of root `5` do so.  Direct computation gives global
connectivity six in both cases.  Equations (2) and (3), every pointwise
capacity, and every packet implication then check literally.

### Why this is not a host counterexample

For each of the six choices of an omitted root, the rich lobe contains a
five-rooted `K_5^-` with five two-vertex bags.  The two thin full lobes
complete that model to `K_7^-`.  The constructions therefore deliberately
violate target exclusion at the five-root level.  They prove that a
four-root status variable and its singleton incidence shadow do not retain
the target-sensitive information needed to detect that violation.

Consequently, further optimisation of this aggregate MILP cannot close
the sparse row.  A successful argument must use a five-rooted-model
dichotomy, the packet-weighted excess theorem, or another constraint which
recognises the multi-vertex rooted bags rather than only common-four
singletons.

## Exact verification

The deterministic verifier

```text
active/experiments/sparse_sixcut_rooted_status_aggregate/verify.py
```

has SHA-256

```text
81fecdeab0a4df0591ee48f076932e415a635a5caf6abd49841d304b6e4b623b.
```

It checks all `2^20-1` nonempty internal subsets in each rich lobe,
exhausts all rooted allocations in the thin lobes, verifies every
displayed two-vertex rooted witness, checks both packet numbers, rebuilds
the two whole graphs, and obtains

```text
GREEN sparse-six-cut rooted-status aggregate nonclosure
packet-111: boundary=[(0, 5)] etas=[17, 3, 3] packets=(1, 1, 1) order=32 size=128 kappa=6
packet-211: boundary=[] etas=[18, 3, 3] packets=(2, 1, 1) order=32 size=128 kappa=6
rooted_status_digest=f9715fd15b51f3a5aec2845c279ba08c5f930014e8bc82438f1fec60769417d3
five_root_witness_digest=438e6fb39a5394cf0d11ab0d6101ab8adee2a2d4befe7cdfbf457a764658eeac
```

## Audited inputs

- no-rooted branch closure: source
  `23ee073a1df5ccca13dfab57e0307e152bb49183b72315554e298f0d9aaade49`,
  cold audit
  `c83f04d601b88393037f62459a123620b89e77ec38f5972ddb513312348e91ac`;
- singleton transfer: source
  `0940ce049a348dc752be5460ec98ed4f7a2872d57d15e4c1181d442853ae1d88`,
  cold audit
  `264913c1c2fa83c74a362cba49773c5e1c8bf58fbca86fdf40b90c36fcc9dbef`;
- packet orientation: source
  `efe0df2eaa66e26f80544d990bbbe321cc12e829ca7854d8ff27dc953a3bc990`,
  cold audit
  `1e58bc785d0ebf5305ce92ac0b18b2fe23f488ae5799f244b9709fbf7fd7bf8b`;
- five-root terminal lemma: source
  `32c45ee41ee349e2499c82c49bd7a0af7cfd636620bbc7873edea4ca061e1100`,
  audit
  `b89582b3c4c4dfe0c03980c45c93b7fcad250241e6ef356273fd9f3fa2db7a89`.
