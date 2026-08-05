# A sharp finite screen for three labelled six-boundary kernels

**Status:** computer-assisted finite result with explicit branch-set
certificates and a separately implemented checker.  The adjacent
[audit](hc7_k7minus_e5_six_boundary_kernel_screen_audit.md) is GREEN for
the pinned revision.  This theorem concerns only the displayed graphs of
orders nine and ten; it is not an unbounded reduction and does not prove
`(E5)`.

Write `K_7^-` for `K_7` with one edge deleted.

## 1. The labelled host families

Let

```text
P={0,1,2,3,4,5}
```

and let `B` be an arbitrary graph on `P`.  Add a vertex `h`, anticomplete
to every low-kernel vertex below, in one of two ways:

- `h` is **five-full** if `N(h)=P-{r}` for a prescribed `r in P`;
- `h` is **six-full** if `N(h)=P`.

Add one of the following three labelled low kernels.  All edges not
specified here or in `B` are absent.

1. The `K_2` kernel has vertices `d,w`, the edge `dw`, and

   ```text
   N_P(d)={0,1,2,3},              N_P(w)={0,1,4,5}.
   ```

2. The `P_3` kernel has vertices `d,f_1,f_2`, edges `df_1,df_2`, and

   ```text
   N_P(d)={0,1,2},
   N_P(f_1)=N_P(f_2)={0,3,4,5}.
   ```

3. The `K_3` kernel is the preceding `P_3` kernel with the additional
   edge `f_1f_2`.

Thus the `K_2` hosts have order nine, while the `P_3` and `K_3` hosts have
order ten.

## 2. Finite theorem

### Theorem 2.1 (labelled six-boundary kernel screen)

Every host defined above contains `K_7^-` as a minor under the following
conditions.

| attachment of `h` | `K_2` kernel | `P_3` kernel | `K_3` kernel |
|---|---:|---:|---:|
| five-full | `|E(B)|>=13` | `|E(B)|>=13` | `|E(B)|>=12` |
| six-full | `|E(B)|>=13` | `|E(B)|>=11` | `|E(B)|>=10` |

Each of the six thresholds is sharp for its labelled family: with one
fewer boundary edge there is a choice of `B`, and of the missed root in a
five-full case, for which the host has no `K_7^-` minor.

### Proof by exhaustive certificates

Order the fifteen possible boundary edges lexicographically:

```text
(0,1),(0,2),...,(0,5),(1,2),...,(4,5).
```

The retained
[generator](hc7_k7minus_e5_six_boundary_kernel_screen.py) enumerates every
boundary mask in each stated edge range and every possible missed root.
For each host it enumerates every partition of every host subset into
seven nonempty branch sets.  It retains a certificate only when all seven
sets are connected and their quotient has at most one missing adjacency.

The resulting
[certificate file](hc7_k7minus_e5_six_boundary_kernel_certificates.json)
contains exactly 11,914 labelled cases:

| family | certificates |
|---|---:|
| `K_2`, five-full | 726 |
| `P_3`, five-full | 726 |
| `K_3`, five-full | 3,456 |
| `K_2`, six-full | 121 |
| `P_3`, six-full | 1,941 |
| `K_3`, six-full | 4,944 |

The standard-library
[independent checker](hc7_k7minus_e5_six_boundary_kernel_certificate_check.py)
does not import the generator.  It independently reconstructs all six
host families and their complete boundary-mask catalogues, then checks
the schema, coverage, disjointness, connectivity and quotient adjacency
of every certificate.  Of the retained models, 452 have complete `K_7`
quotient and 11,462 have quotient exactly `K_7^-`.

For sharpness, boundary masks

```text
family              mask     missed root
K_2 five-full       4095         3
P_3 five-full      29439         5
K_3 five-full      13055         5
K_2 six-full       23550         -
P_3 six-full       12927         -
K_3 six-full        6463         -
```

have respectively `12,12,11,12,10,9` edges.  The independent checker
enumerates every seven-branch-set partition of every host subset and finds
no `K_7^-` model in any of these six graphs.  This proves both the positive
table and its asserted sharpness.  \(\square\)

## 3. Reproduction and scope

From the repository root, run

```bash
python3 results/hc7_k7minus_e5_six_boundary_kernel_screen.py sanity
python3 results/hc7_k7minus_e5_six_boundary_kernel_screen.py generate \
  --output /tmp/e5-six-boundary-kernel-certificates.json
python3 results/hc7_k7minus_e5_six_boundary_kernel_screen.py check \
  /tmp/e5-six-boundary-kernel-certificates.json
python3 results/hc7_k7minus_e5_six_boundary_kernel_certificate_check.py
```

The regenerated JSON is byte-identical to the retained certificate file.
The finite theorem does not assert that every graph in the live `E5`
reduction contracts to one of these hosts.  Such a conclusion requires a
separate, unbounded reduction which preserves the labelled boundary and
the exact excess identities.
