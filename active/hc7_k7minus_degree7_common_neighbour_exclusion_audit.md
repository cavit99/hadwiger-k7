# Audit: saturated degree-seven exclusion

**Verdict:** GREEN within the stated finite-computation trust boundary.

**Audited theorem source:**
`active/hc7_k7minus_degree7_common_neighbour_exclusion.md`

**Theorem SHA-256:**
`663c1b7e0de9b0951de89801d52baf4aae12535d7807547d19d04fc10b00c4b0`

**Audited verifier:**
`active/hc7_k7minus_degree7_quotient_verify.py`

**Verifier SHA-256:**
`ac0c37438d802930a0aa80bfd1d6491101da3df9a55fac1e1cf3db5ae1b7e445`

## Mathematical reduction

Let `v` be a degree-seven vertex and `S=N(v)`.  For an edge `vs`, every
common neighbour of its ends lies in `S`.  Thus four common neighbours on
every edge imply `delta(H[S])>=4`, equivalently
`Delta(complement(H[S]))<=2`.

Because the host has at least nine vertices, an exterior component `C`
exists.  Its neighbourhood is a subset of `S`; six-connectivity gives at
least six distinct neighbours there.  Contracting all of `C` to one vertex
and deleting the other exterior components produces exactly a graph covered
by the finite lemma.  The contracted vertex represents one connected branch
set, so every quotient certificate lifts literally to the original host.

No bounded-order assumption is made on `C` or on any other part of the host.

## Verifier audit

The finite universe is complete for the following reasons.

1. Every simple graph of maximum degree at most two is a disjoint union of
   paths and cycles.  Component multisets of total order seven therefore
   parametrize its isomorphism types.  The generator produces 29 distinct
   signatures, the expected count.

2. An attachment set of order at least six is either the full seven-set or
   omits one named vertex.  The verifier checks all eight choices for each
   complement type, for 232 cases in total.

3. A seven-bag minor model in a nine-vertex graph uses seven, eight, or nine
   vertices.  Enumerating every subset of those orders and every partition
   into seven nonempty bags is exhaustive.  The verifier obtains 750
   candidates.

4. A candidate is accepted only after always-active checks of branch-set
   disjointness, nonemptiness, connectivity, and the number of missing
   interbag adjacencies.  At most one missing pair is exactly the definition
   needed for a `K_7^-` minor.

5. The model checker is tested on a literal `K_7^-` positive instance and
   on padded `K_6` and `K_{2,2,2,2}` negative instances.  These tests would
   detect the principal errors of accepting six bags, accepting two missing
   adjacencies, or treating disconnected padding as part of a branch set.

## Fresh execution

The recorded command was rerun under ordinary Python:

```text
python3 active/hc7_k7minus_degree7_quotient_verify.py
```

It returned:

```text
complement types: 29
full-or-one-missed attachment cases: 232
model support orders: {7: 67, 8: 102, 9: 63}
certificate digest: b98ac56930aa7044c3a6a7c029b75cd85feb39f4dabd8476a0ba7f08ccdb7306
GREEN: every quotient contains a certified K_7^- minor
```

The certificate digest is checked by the verifier and is stable under the
recorded enumeration order.

## Scope and unresolved obligation

The theorem is a computer-assisted unbounded result.  It proves that a
six-connected `K_7^-`-minor-free graph in which every edge has at least four
common neighbours cannot have a degree-seven vertex.

It does not prove the four-common-neighbour hypothesis for a general host.
That hypothesis remains the exact upstream obligation in the saturated
minimal-enemy argument.
