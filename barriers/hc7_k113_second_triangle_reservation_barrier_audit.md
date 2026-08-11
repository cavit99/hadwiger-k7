# Internal audit: second-triangle reservation barrier

Audited file:
`barriers/hc7_k113_second_triangle_reservation_barrier.md`

Audited SHA-256:

```text
3b639abe1452ee28b6ea15afa869c236013814dceab49f81e04aec515e532312
```

**Verdict:** **GREEN** as a counterexample to both intermediate statements
in Section 1, with the scope in Section 4.

This is a hash-pinned internal mathematical audit, not external peer
review.

## 1. Construction and scheme check

For `H=K_{1,1,3}`, the graph before the two triangle edge sets are added
is exactly the ten-vertex graph `M'(H)`: two copies of each vertex, with
`u^r v^s` present precisely when `uv in E(H)` and at least one of
`r,s` is two.  Giving both copies of `u` colour `u` is proper, and adding
the two stable-colour triangles preserves properness.

For each edge `uv`, the displayed walk

\[
                         u^1-v^2-u^2-v^1
\]

is a simple bichromatic path.  A clone `u^2` occurs only on paths whose
demand edge is incident with `u`; the same is immediate for each root
`u^1`.  Hence these seven paths satisfy the full scheme condition.  The
construction therefore has all the local fixed-colour connections assumed
by the refuted statements.

## 2. Containment capacity

After the other four roots and the other two stable pairs are reserved,
the only possible first step from `a^1` toward `a^2` is through `p^2` or
`q^2`.  Thus a connected branch set containing both vertices consumes one
of those two clones.  The three stable bags are disjoint, so three such
bags require three distinct connectors from a two-set.  This proves the
failure of the set-root containment conclusion.

## 3. Reserved-adjacency capacity

With the second triangle kept outside the model,

\[
             N(a^2)=\{p^1,p^2,q^1,q^2,b^2,c^2\}.
\]

The vertices `p^1,q^1` are reserved as singleton roots, and `b^2,c^2`
are reserved in the second triangle.  Therefore a branch set rooted at
`a^1` and adjacent to `a^2` must contain `p^2` or `q^2`.  The same holds
cyclically for `b,c`, so at most two stable bags can meet their prescribed
adjacency.  The weaker conclusion is also false.

## 4. Scope

The example refutes only a direct scheme-theoretic strengthening of
contractibility.  It does not satisfy seven-connectivity, criticality, or
the five-centre exact-cut hypotheses.  No claim is made that those extra
host conditions cannot force the desired placement by another mechanism.
