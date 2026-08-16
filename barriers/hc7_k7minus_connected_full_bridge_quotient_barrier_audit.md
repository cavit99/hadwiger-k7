# Internal audit: connected-full bridge quotient barrier

**Verdict:** **GREEN** for the exact barrier and verifier revisions below.
The displayed order-eleven graph has the claimed boundary and attachment
topology and has no `K_7^-` minor.  This is a separate internal
mathematical audit, not external peer review.

## 1. Exact revisions

The audited source is
[`hc7_k7minus_connected_full_bridge_quotient_barrier.md`](hc7_k7minus_connected_full_bridge_quotient_barrier.md),
with SHA-256

```text
73434c773d628c8cfe3e3b83e508193592c1c4559ec93d1cff807e0d182b7819
```

The retained verifier is
[`hc7_k7minus_connected_full_bridge_quotient_barrier_verify.py`](hc7_k7minus_connected_full_bridge_quotient_barrier_verify.py),
with SHA-256

```text
f0678c00e08811b7862b400fdec2f093c29ade2fe40148df93a1255c28cae20f
```

## 2. Boundary and quotient topology

The graph6 decoder uses the standard short-code order and re-encodes its
result to `G@aIZ_`.  The decoded boundary has eight vertices and the ten
listed edges

```text
04 05 16 17 23 27 37 45 46 56.
```

Direct enumeration gives clique number three and independence number
three.  Thus the boundary is `K_4`-free and has exactly the exceptional
independence parameter claimed in the barrier.

The quotient construction adds exactly twenty-three edges: eight from the
full pole `z`, seven from `a`, seven from `b`, and the edge `ab`.  Together
with the ten boundary edges this gives order eleven and size thirty-three.
The verifier checks all contacts literally:

```text
N_X(z)=X,  N_X(a)=X-{0},  N_X(b)=X-{1}.
```

It also checks that `ab` is the only edge among `z,a,b`.  Hence `R-X` has
the two components `{z}` and `{a,b}`.  The latter is connected and full at
`X` because its two misses are distinct.  Deleting its literal bridge
`ab` leaves two connected one-miss pieces, each with seven boundary
contacts.  This is the connected-full topology required for the stated
counterexample; using the same miss on both sides would not have been
sufficient, because their union would then be nonfull.

## 3. Exhaustive minor check

The verifier starts from eleven singleton bags and repeatedly performs
one of the two operations permitted in a branch-set construction:

1. delete a bag, representing unused quotient vertices; or
2. merge two touching bags, representing an edge contraction.

Bag families are stored as sorted tuples of disjoint vertex masks.  The
enumeration reaches exactly

```text
1, 44, 810, 8076, 47385
```

states at bag counts eleven through seven.  The program independently
checks disjointness and connectedness of every terminal bag in addition
to preserving those properties by construction.

The enumeration is exhaustive in both directions.  Given any seven-branch
minor model, first delete every unused vertex and then contract a spanning
tree of each connected branch set; this produces its canonical seven-bag
state.  Conversely, every merge follows an actual quotient edge, so every
enumerated bag is a valid connected branch set.

A seven-bag family is a `K_7^-` model precisely when at least twenty of the
twenty-one bag pairs touch.  The pinned terminal histogram has maximum
nineteen, attained by 590 states, and contains no state at twenty or
twenty-one.  The complete 56,316-state stream has the pinned digest

```text
8e76ba088cc1a21e772d160c5284bb6d38df807af33651eb848a712d304a5642.
```

The verifier therefore establishes exhaustive absence of a `K_7^-` minor,
not merely absence of a literal subgraph or of one prescribed model shape.

## 4. Exact refutation and limitations

The barrier refutes exactly the universal quotient implication stated in
its Section 1: exceptional boundary topology, one full pole, a connected
full two-vertex exterior image, and at least seven boundary contacts on
each side of its bridge do not force `K_7^-` in the quotient.

This is not a counterexample to any critical-host theorem.  The finite
graph is not asserted to be seven-connected, seven-chromatic,
minor-critical, or to meet the critical density bound.  It does not carry
the remote operation cube, the associated boundary-colouring languages,
or a fixed exact `K_7^\vee` model.  Interior branch-set structure in an
actual host can also supply models absent from its three-image quotient.
Consequently operation-preserving descent, response-to-model alignment,
and other critical-host arguments remain available.

The barrier is also distinct from the both-full two-exterior-component
row: that row has an additional full exterior component and a separately
audited seven-type boundary restriction.  The existing support-six
single-bridge barrier concerns a different boundary and target-model
configuration, so the present retained example is not a duplicate of it.

## 5. Trust boundary and mechanical checks

The proof uses no external package or literature theorem.  Its trust
boundary is the standard-library graph6 decoder and the explicit finite
state enumeration described above.  Expected state counts, the complete
state digest, the full terminal contact histogram, and all construction
parameters are pinned in the verifier.

The verifier runs successfully with assertions enabled, compiles with
`py_compile`, all local links resolve, and the three files pass Git
whitespace checking.  No ledger, index, manifest, or theorem file was
changed for this barrier package.
