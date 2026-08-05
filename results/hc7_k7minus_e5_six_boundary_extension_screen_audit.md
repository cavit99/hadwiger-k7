# Internal audit: exact extension screens for the labelled six-boundary kernels

**Verdict:** **GREEN** for the finite theorems at the revisions pinned below.
This is a separate internal mathematical and computational audit, not
external peer review.  The verdict does not cover an unbounded reduction or
`(E5)`.

## 1. Audited revisions

| artefact | SHA-256 |
|---|---|
| finite theorem: `hc7_k7minus_e5_six_boundary_extension_screen.md` | `bfe0a330bbcefe655f8a7c853be4944a39adbadf810991cb0d4185552ae9094f` |
| primary exhaustive screen | `f4705afa63fd4653549726927fefdb25efbeae57763ab52e4319e978f5e8e3ef` |
| independently implemented exhaustive checker | `bc59c072510ad5e5fb684c8a63b68abbac31e68dd59f7172b850b5cb984dfd49` |
| deterministic checker driver | `c4569fa25afef7ae1d410d12d6bd1eb94077df3ab5563f3fbb2d717e8aa8db1b` |
| retained primary-screen output | `3cd13e6d330dccf072cc6103fd237b528ca9093679a80507cf7775e19d63b03c` |

The theorem definitions, ordinary catalogues, split-contact catalogues,
computational description and scope were checked at the displayed theorem
hash.  In particular, both equality split cases explicitly require root `1`
to have exactly one neighbour in the split component; this is the hypothesis
encoded by both implementations and gives the stated `162` contact patterns
per universal root.

## 2. Host encodings

Both implementations independently reconstruct the same labelled hosts.

- The boundary is the arbitrary labelled graph `B` on `P={0,1,2,3,4,5}`.
- The `K_2`, `P_3` and `K_3` low kernels have exactly the internal edges and
  boundary neighbourhoods displayed in the theorem.
- A six-full representative is adjacent to all six boundary roots and to no
  low-kernel vertex or other representative.
- A singleton missing `r` is adjacent exactly to `P-{r}`.  The full-edge case
  adds the edge between two such vertices.
- A split component is represented by two adjacent vertices.  Each root's
  contact type records adjacency to the first representative, the second, or
  both, and the other six-full component is represented separately.

No unlisted edge is introduced.  The ordinary hosts have orders ten, eleven
or twelve.  The split-contact hosts have order twelve.

## 3. Complete minor-model search

For a host of order `n`, a `K_7^-` minor is equivalent to seven pairwise
disjoint nonempty connected vertex sets, using an arbitrary subset of the
host vertices, whose quotient has at most one missing adjacency.  Both
programmes check exactly this condition.

The primary screen first chooses every used subset and then generates every
unlabelled partition of it into seven bags.  Its complete model-universe
sizes are

| host order | candidate partitions |
|---:|---:|
| 10 | 11,880 |
| 11 | 159,027 |
| 12 | 1,899,612 |

These counts independently equal

```text
sum_{k=7}^n binomial(n,k) S(k,7),
```

where `S(k,7)` is a Stirling number of the second kind.

The independent checker does not import the primary implementation.  It
generates the same complete universe by scanning the host vertices once and
choosing whether each vertex is unused, joins an existing canonical block,
or begins the next canonical block.  It independently rebuilds every host,
checks connectivity and quotient adjacency, and asserts the exact
target-free distributions and labelled mask sets rather than merely their
maximum edge counts.

The deterministic driver verifies the independent checker's source hash,
compiles it with strict C++20 warnings, executes it without OpenMP, and
checks its complete standard output.  It was rerun successfully and reports

```text
PASS independent E5 six-boundary extension check
ordinary hosts checked: 140498
portal hosts checked: 4536
total finite hosts checked: 145034
model universes: n=10 11880; n=11 159027; n=12 1899612
```

The checker also passes a positive `K_7^-` sanity host and the negative
`K_7^vee` and complement-of-`P_8` sanity hosts.

## 4. Ordinary catalogue verification

Every statement of Theorem 1.1 agrees with both exhaustive implementations
and the retained primary output.

- In the favourable `P_3` singleton case, the target-free boundary-edge
  distribution is `1:1, 2:7, 3:9, 4:3`; the three four-edge masks are exactly
  those displayed in the theorem.  The corresponding `K_3` distribution is
  `1:1, 2:4, 3:3`, with exactly the three displayed three-edge masks.
- All thirty tied-twin boundaries and all 1,024 full-edge boundaries in each
  favourable orientation contain the target.
- In the other orientation, all degree-compatible common-missed-root twin
  catalogues contain the target.  Joining the twin vertices only adds an
  edge, so the asserted full-edge conclusion follows by monotonicity.
- All 150 tied-twin `K_2` hosts contain the target.  The target-free `K_2`
  one-six-full/full-edge hosts are exactly the four boundaries
  `{01} union X`, where `X` is a subset of `{23,45}`.
- Of the 1,024 `K_2` two-six-full hosts, the target-free distribution is
  `1:1, 2:10, 3:37, 4:64, 5:54, 6:14, 7:1`.  Its unique seven-edge boundary is
  `01,12,13,14,15,23,45`, and adding a singleton missing `0` makes all 1,024
  hosts positive.
- All 32,768 three-six-full hosts contain the target for each of the `P_3`
  and `K_3` kernels.  In each two-six-full catalogue, the target-free hosts
  are exactly the sixteen boundaries described by equation (1.3), with
  distribution `1:1, 2:5, 3:7, 4:3`.
- Every displayed degree-compatible singleton extension of a two-six-full
  `P_3` or `K_3` host contains the target.

Thus all 140,498 ordinary hosts counted by the independent checker are
accounted for by the theorem's catalogues.

## 5. Split-contact verification

The two implementations agree on all 4,536 split-contact hosts.

- For each of the eight degree-one boundary masks and each of the `P_3` and
  `K_3` kernels, all `243` contact patterns are checked.  Exactly eighteen
  are target-free: roots `3,4,5` have one common exclusive side, while the
  remaining two nonfixed roots have arbitrary nonempty contact types.
- For the triangle boundary, both choices of universal root are checked over
  all `162` compatible patterns.  Exactly twelve are target-free, precisely
  those in which roots `3,4,5` have one common exclusive side.
- For boundary `01,12,34`, both choices of universal endpoint of `34` are
  checked over all `162` compatible patterns.  Exactly six are target-free,
  precisely those in which roots `0,1,2,5` have one common exclusive side.

The finite conclusion concerns the displayed contracted host.  When the two
split representatives genuinely arise by contracting two adjacent connected
parts with the encoded root contacts, any positive model lifts through those
contractions.  The computation does not itself prove that such a split exists
in an arbitrary unbounded component.

## 6. Precise scope

There is no unresolved finite enumeration, host-encoding or minor-search gap
at the pinned revisions.  The GREEN verdict proves only Theorems 1.1 and 2.1
for the finite labelled host families stated there.

It does not prove that every live `E5` configuration contracts to one of
these hosts, that a target-free finite quotient lifts to an unbounded
target-free graph, that density can be localised inside a six-full component,
that repeated singleton deletion preserves the required endpoint incidence,
the auxiliary statement `(E5)`, or the seven-connected `4n-2` target.
