# Internal audit: labelled six-boundary kernel screen

**Verdict:** **GREEN** for the pinned theorem and computational artefacts.
This is a separate internal mathematical and computational audit, not
external peer review.

## 1. Audited revisions

| artefact | SHA-256 |
|---|---|
| theorem: `hc7_k7minus_e5_six_boundary_kernel_screen.md` | `8d88540972595703378926f57b99270603d51ec1123976e9d7a024a6f3535ea1` |
| exhaustive generator and primary checker | `6fbd2a4976cd1c5a8e26ed5015358cbca5fa4d6801035bf0b527081f6290aec2` |
| retained certificate JSON | `4b148b7a4bd2845e1311e5e67a1d6706048c3791d6cd29bf12676cb37e5fd905` |
| independently implemented checker | `05e9ddc3254d14745118cc2dc98b029e3e402e27ff40b7e39ee4b4356fb3e3c2` |

The theorem statement, host definitions, thresholds, sharpness statement,
proof description and scope were all checked at the displayed theorem hash.

The supplied source artefacts had SHA-256 values

```text
attack note:       15e048b30c7356bd7ef86e0f67048c1e56e65bf2b47a5d95bb55b28531e849df
original screen:   b2c84d009efb199996a543839dee1bb2cc63bc9bb2cb5b7b2d38ced6140b5f62
certificate JSON:  4b148b7a4bd2845e1311e5e67a1d6706048c3791d6cd29bf12676cb37e5fd905
```

The retained screen changes documentation, rejects optimised execution,
hardens metadata checking and adds the six sharpness sanity cases.  Its
host construction, positive enumeration and generated certificate bytes
are unchanged.

## 2. Host encoding

Both implementations independently reconstruct the boundary vertices
`0,...,5` and use the same mathematical definition, but share no code.

- For the `K_2` kernel, the low vertices have boundary neighbourhoods
  `{0,1,2,3}` and `{0,1,4,5}` and are adjacent to each other.
- For the `P_3` kernel, its centre has boundary neighbourhood `{0,1,2}`
  and both ends have boundary neighbourhood `{0,3,4,5}`.
- The `K_3` kernel adds the edge between those two ends.
- The opposite representative is adjacent either to exactly five boundary
  vertices, with every missed root enumerated, or to all six.
- No edge joins the representative to a low-kernel vertex.

These are exactly the three labelled families stated in the theorem.  The
hosts have orders nine and ten, so direct enumeration of seven connected
branch sets is finite and exhaustive.

## 3. Positive certificate coverage

Fresh generation produced

```text
adjacent_singletons_k2_five_full: 726
crossing_twins_p3_five_full:      726
crossing_edge_k3_five_full:      3456
adjacent_singletons_k2_six_full: 121
crossing_twins_p3_six_full:      1941
crossing_edge_k3_six_full:       4944
total:                           11914
```

The regenerated JSON was byte-identical to the retained file and had the
pinned SHA-256 above.  The counts equal the complete labelled catalogues:
all boundary masks at or above the six stated thresholds, multiplied by
all six missed-root choices in the five-full cases.

For every record, the independent checker verifies strict JSON schema and
types, the boundary mask and edge count, the permitted missed root, exact
catalogue membership, uniqueness, nonempty and disjoint branch-set masks,
branch-set connectivity, and at most one missing quotient adjacency.  It
also checks that no case is absent.  The quotient counts are

```text
complete K_7 quotient:        452
exact K_7^- quotient:       11462
```

The supplied generator's built-in checking mode reuses its host builder and
model validator, so it is not by itself an implementation-independent
audit.  The companion checker was written separately, imports no generator
code and independently reconstructs the complete case universe.  Its
agreement closes that trust-boundary issue for the retained certificate
file.

## 4. Sharpness

The six recorded boundary masks have respectively one fewer edge than the
positive threshold:

```text
K_2 five-full: mask  4095, missed root 3, 12 edges
P_3 five-full: mask 29439, missed root 5, 12 edges
K_3 five-full: mask 13055, missed root 5, 11 edges
K_2 six-full:  mask 23550,                  12 edges
P_3 six-full:  mask 12927,                  10 edges
K_3 six-full:  mask  6463,                   9 edges
```

For each order-nine host, the independent checker tests all 750 partitions
of every possible used subset into seven bags.  For each order-ten host it
tests all 11,880.  It finds no seven connected branch sets with at most one
missing quotient adjacency.  Thus every threshold is sharp within its
displayed labelled family.

The primary screen also passes the positive `K_7^-` sanity case and the
negative `K_7^vee` and complement-of-`P_8` sanity cases.

## 5. Reproduction

The following commands were rerun successfully:

```bash
python3 results/hc7_k7minus_e5_six_boundary_kernel_screen.py sanity
python3 results/hc7_k7minus_e5_six_boundary_kernel_screen.py generate \
  --output /private/tmp/e5-six-boundary-kernel-certificates.json
python3 results/hc7_k7minus_e5_six_boundary_kernel_screen.py check \
  results/hc7_k7minus_e5_six_boundary_kernel_certificates.json
python3 results/hc7_k7minus_e5_six_boundary_kernel_certificate_check.py
```

The scripts use only the Python standard library and are deterministic.
The generator refuses optimised Python execution because its internal
validation uses assertions; the independent checker uses explicit failures.

## 6. Exact scope

There is no unresolved finite-encoding or certificate gap at the pinned
revisions.  The theorem proves six statements only for the displayed
labelled hosts of orders nine and ten.  It does not prove that an arbitrary
unbounded shore can be represented by one vertex, that every live `E5`
configuration reaches one of the three kernels, the proposed kernel-
localisation lemma, `(E5)`, or the seven-connected `4n-2` target.
