# A connected-full bridge quotient need not contain `K_7^-`

**Status:** retained finite barrier;
[separate internal audit GREEN](hc7_k7minus_connected_full_bridge_quotient_barrier_audit.md).
The retained standard-library verifier is
[`hc7_k7minus_connected_full_bridge_quotient_barrier_verify.py`](hc7_k7minus_connected_full_bridge_quotient_barrier_verify.py).

## 1. The topology-only claim refuted

The following statement is false.

> Let `X` be an eight-vertex graph with no `K_4` and with
> `\alpha(X)=3`.  Add a vertex `z` complete to `X` and two adjacent
> vertices `a,b`, each adjacent to at least seven vertices of `X`, with no
> other edge among `z,a,b`.  If the connected set `{a,b}` is full at `X`,
> then the resulting graph contains a `K_7^-` minor.

This is the direct quotient statement one would need in order to rule out
a bridge `f` in the connected-exterior order-eight residue using only the
exceptional boundary conditions and the numbers of boundary contacts of
the two components of `C-f`.

## 2. An explicit order-eleven counterexample

Let the boundary graph on the literal vertex set

```text
X = {0,1,2,3,4,5,6,7}
```

have graph6 code

```text
G@aIZ_
```

and edge set

```text
04 05 16 17 23 27 37 45 46 56.
```

Add three vertices `z,a,b` as follows.

1. `z` is adjacent to every vertex of `X`.
2. `a` is adjacent exactly to `X-{0}` outside the edge `ab`.
3. `b` is adjacent exactly to `X-{1}` outside the edge `ab`.
4. `ab` is an edge, while `za` and `zb` are not edges.

Call the resulting graph `R`.  The verifier checks directly that

```text
|V(R)|=11,  |E(R)|=33,
omega(R[X])=3,  alpha(R[X])=3.
```

In particular, the boundary is `K_4`-free and has the exact independence
number required at an exceptional degree-eight centre.

The graph `R-X` has exactly the two components `{z}` and `{a,b}`.  Both
are full at `X`: the singleton is complete to the boundary, and the joined
component repairs its two distinct misses.  Deleting the literal bridge
`ab` splits the latter component into the connected pieces `{a}` and
`{b}`, each adjacent to exactly seven boundary vertices.  Thus `R` has
the exact connected-full quotient topology and full-or-one-miss profiles
used by the proposed shortcut.

### Theorem 2.1 (exact noncontainment)

The graph `R` has no `K_7^-` minor.

#### Finite verification

Start from the eleven singleton bags.  At each step the verifier either
deletes one bag or contracts two bags which are adjacent in `R`, retaining
a canonical sorted family of disjoint vertex masks.  It enumerates

```text
bag count       11    10     9      8       7
states           1    44   810   8076   47385
```

reachable states.  Every family of seven disjoint nonempty connected
branch sets occurs in this enumeration: delete every unused vertex and
contract a spanning tree inside each branch set.  Conversely, every
enumerated bag is connected by construction and is independently checked.

A seven-bag family models `K_7^-` exactly when at least twenty of its
twenty-one bag pairs are adjacent.  Across all 47,385 seven-bag states the
maximum is nineteen.  The complete state stream has SHA-256

```text
8e76ba088cc1a21e772d160c5284bb6d38df807af33651eb848a712d304a5642
```

and the verifier pins the full contact-count histogram.  Hence no
`K_7^-` model exists. `\square`

## 3. Exact consequence and scope

The counterexample proves that the exceptional boundary conditions

```text
K_4-free, alpha=3,
```

together with one full pole, two adjacent split images, at least seven
boundary contacts per image, and fullness of their union do not by
themselves eliminate a bridge-supported connected exterior component.
Repeating whole-component contraction or checking only those contact
profiles cannot close the connected-exterior order-eight residue.

This barrier does **not** assert that `R` is a minor-critical host or that
it can occur as the displayed quotient of one.  It does not reproduce
seven-connectivity, density, operation-labelled colourings, the 80-pattern
remote operation cube, or a fixed exact `K_7^\vee` model.  Any of those
additional host-level structures may still rule out the bridge case.  In
particular, the barrier does not refute an operation-preserving split
lemma, a response-to-model alignment theorem, or a critical-host closure.

The construction also does not address the both-full two-exterior-component
row, where an additional full exterior component and the audited seven
boundary types give a different quotient theorem.

## 4. Trust boundary

The mathematical claim is a finite statement about the displayed
eleven-vertex graph.  Its trust boundary is the retained deterministic
Python verifier and the correctness of exhaustive deletion/contraction
enumeration.  The program uses only the standard library, decodes and
re-encodes the graph6 boundary, verifies all attachment profiles, checks
connectedness and disjointness of every terminal bag family, and pins both
the state digest and the contact histogram.
