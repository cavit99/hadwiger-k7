# Cold audit: the order-seven `i=2` Hall completion

**Status:** separate internal cold audit.  This is not external peer review.

## Audited revisions

The audited theorem is
`hc7_k7minus_sparse_sixcut_order_seven_i2_completion.md`, SHA-256

```text
c31da46f7cdd1f45c849ddc40e03372f2c2a240143d3020ef4978ca56456a9a3.
```

Relative to the initially audited revision
`d36f4f0cbfd21247f69cb8ee685effea0dd2f415257944b853e5e3430e366de2`,
this final revision changes only the status line from audit-pending to
independently cold-audited.  Its theorem statement, proof, orbit table and
reproduction instructions are unchanged.

The audited standard-library verifier is
`experiments/sparse_sixcut_order_seven_i2_completion/verify.py`, SHA-256

```text
0f70f992c3f348781bff753605c74b19f41058e5cdb60306d47168434ddfcd78.
```

## Verdict

**GREEN.**  The Hall-profile deductions, the reduction to three tree types,
the two branch-set templates, the sixty-case enumeration, and the fifteen
displayed orbit certificates are correct.  No excess or packet hypothesis is
used.  I found no unresolved assumption or gap within the theorem's stated
order-seven `i=2` scope.

## Mathematical audit

### 1. Hall profile and connected complement

For a two-member inclusion-minimal deficient family, the audited order-seven
Hall profile gives two singleton model bags `U={p_0,p_1}` with

```text
|N_S(U)|=1,                 N_C(U)=C-U.
```

Call the unique root in `N_S(U)` by `q`.  Each proper one-member subfamily is
Hall-sufficient.  Its root neighbourhood is a nonempty subset of `{q}`, so
`q` is adjacent to each pole and neither pole has another root neighbour.
The complementary Hall matching is genuinely vertex-level: it matches the
five vertices of `W=C-U` bijectively to the other five roots.

The three original model bags outside `U` partition `W`.  They are connected,
and their three-vertex quotient loses at most the one pair that the full
five-bag near-clique quotient may lose.  It therefore has at least two edges
and is connected.  Joining the three connected bags along that quotient
proves that `C[W]` is connected.  This justifies taking a spanning tree of
`C[W]` later; no connectivity of an unproved auxiliary graph is assumed.

### 2. Pole degrees and monotone edge deletion

Applying relative six-connectivity to either singleton gives

```text
d_C(p_j)+d_S(p_j)>=6.
```

The preceding Hall argument gives `d_S(p_j)=1`, hence `d_C(p_j)>=5`.

If the pole edge is absent, both poles are complete to the five vertices of
`W`.  If the pole edge is present, each pole misses at most one vertex of
`W`.  The two misses cannot coincide, since `N_C(U)=W` says that every vertex
of `W` has a neighbour in `U`.  When one or both poles are complete to `W`,
deleting optional pole--`W` edges can create two artificial distinct misses.
Thus the adjacent-pole case reduces to an ordered pair of distinct misses.

Deleting down to a spanning tree of `C[W]`, and deleting the optional pole
edges just described, is logically sound: every rooted minor model found in
the reduced graph is also a model in the original graph.  There are exactly
three unlabelled trees on five vertices (path, star and fork), so the reduced
case list is exhaustive.

### 3. The two certificate forms

Template A omits `q`, uses all five diagonal roots, and puts the two poles in
two distinct diagonal bags.  Template B uses `{q,p}` as one bag, omits one
diagonal root `t_z`, and puts `w_z` and the other pole into a retained
diagonal bag.  In both forms the five bags contain five distinct roots and
partition all seven shore vertices.

The verifier represents only the shore part of each rooted bag.  Its
`rooted_connected` routine starts from all vertices of the shore mask adjacent
to the designated root and then performs exact reachability inside that
mask.  Its contact test checks both possible root-to-opposite-bag incidences
and all shore edges between the masks.  Consequently `valid` checks precisely
the required rooted-bag connectivity and quotient adjacency; it does not
replace multi-vertex bags by a one-vertex allocation surrogate.

For the nonadjacent-pole case, the verifier checks template A on each of the
three tree types.  A direct check also explains the construction: choose a
three-vertex path in the tree and place the two universal poles in the two
other diagonal bags.  The pole bags supply seven quotient edges and the path
supplies the remaining two.

For adjacent poles, the verifier enumerates

```text
3 tree types * 5 * 4 ordered distinct misses = 60 cases.
```

Template A closes forty-six cases and template B closes fourteen, with the
reported split

```text
path 12/8,       star 20/0,       fork 14/6.
```

The code separately constructs the automorphism orbit of every displayed
miss-pair representative, includes simultaneous exchange of the two poles,
checks the stated orbit size, removes the orbit from the complete twenty-pair
set, and verifies the named A or B witness itself.  The fifteen rows cover
all sixty cases without overlap.  This directly pins the human-readable
orbit table to the machine check.

The reduced graph retains seven boundary edges, namely `qp_0`, `qp_1`, and
the five diagonal matching edges.  Both the theorem and verifier use this
correct count; no unlisted boundary incidence is used by a certificate.

## Reproduction

I reran

```text
python3 active/experiments/sparse_sixcut_order_seven_i2_completion/verify.py
```

under two distinct `PYTHONHASHSEED` values and obtained in both runs

```text
unjoined universal cases=3
joined cases by tree={'path': {'A': 12, 'B': 8}, 'star': {'A': 20, 'B': 0}, 'fork': {'A': 14, 'B': 6}}
joined template counts={'A': 46, 'B': 14}
joined orbit rows=15 coverage=60 witnesses=PASS
order-seven i=2 direct completion: PASS
```

The verifier also passes `python3 -m py_compile`.

## Scope

The theorem closes the exact shore-order-seven Hall profile with deficient
family size two by producing the punctured rooted `K_5^-` model directly.
It does not address the order-seven `i=3` or `i=4` profiles, larger shores,
the unbounded packet-weighted local theorem, Norin--Totschnig Conjecture 21,
or `HC_7`.  Those limitations do not affect the stated result.
