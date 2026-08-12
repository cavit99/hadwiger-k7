# Separate internal audit: matching-lock boundary reduction

## Verdict and exact revision

**Verdict: GREEN, with the scope qualifications in Section 7.**

This audit checks the complete source file
[`hc7_k7minus_matching_lock_boundary_reduction.md`](hc7_k7minus_matching_lock_boundary_reduction.md)
at SHA-256

```text
d95c459737f7d94e8c212e8f3d90e2b5fbf762f46567d70e6e6d9dfb386dd244
```

The promoted source differs from the initially audited revision
`2e8ba58cbf3e94500416ea67cf890bdfaeaa0e955b5a722fccbe5033f2c81b16`
only in its status header and audit link.  Its mathematical content is
unchanged.

The large-boundary descent, its iteration to orders seven through nine,
the invocation of the audited degree-nine alignment theorem, the unlocked
transition reduction and the all-lock normal form are correct at this
revision.  The final model-allocation and label-preservation statements are
explicitly identified as open and are not used as proved implications.
This is an internal mathematical audit, not external peer review.

The three direct dependencies have the following current source hashes,
which agree with their adjacent GREEN audits:

```text
bce97974e2d3d543aaf9ae2f07ff13b61684ddc9cb6bdf08bacdb750c2be2c97  results/hc7_large_boundary_singleton_response_descent.md
1ea36e3e3ba933c5d15b9fa6577005cc4ae7d584907fe55d0b52b35a40508f12  results/hc7_tight_degree9_boundary_alignment.md
0159743557cc9c0de8a0d9e9f3969b9ecde20bb2bf50d5e8716cf6e54a1297d1  results/hc7_k7minus_matching_forbidden_signature_kempe_coupling.md
```

## 1. External hypotheses and the strict density bound

The source assumes that `G` is seven-connected and seven-chromatic, has no
`K_7` minor, and has every proper minor six-colourable.  These hypotheses
are at least as strong as those used at every invocation.

The strict estimate

```text
|E(G)| <= 5|V(G)|-16
```

is exactly Lemma 1.1 of the audited large-boundary result.  Mader's exact
bound first gives `5n-15`.  In Jorgensen's equality classification,
`K_{2,2,2,3}` has connectivity six, a nontrivial five-clique sum has an
order-five separator, and a single edge-maximal two-apex member is
six-colourable by four-colouring its planar remainder and assigning two
fresh colours to its apex set.  Seven-connectivity and seven-chromaticity
therefore exclude equality.  No `K_7^-`-minor exclusion is used in this
step or elsewhere in the source.

The use of `HC_6` is also at its exact strength: a `K_6`-minor-free graph is
five-colourable, while an exactly six-chromatic graph has a `K_6` minor.

## 2. An actual boundary is `K_6`-minor-free

Let `S=N_G(Y)` with `Y` connected and with a vertex outside `N_G[Y]`.
Every literal vertex of `S` has a neighbour in `Y`.  Consequently a
`K_6` model in `G[S]`, together with the connected branch set `Y`, would
be a `K_7` model.  Thus `G[S]` is `K_6`-minor-free and `HC_6` gives the
five-colouring used later in the equality case.  This argument requires
neither a prescribed root in each boundary branch set nor any assumption
on the number of components outside `S`.

## 3. Degree-sum calculation and strict descent

Write `b=|S|` and `n=|V(G)|`.  Under the contrary assumption that every
vertex outside `S` has degree at least `b`, the vertices outside `S`
contribute at least `b(n-b)` to the degree sum and seven-connectivity makes
the contribution of `S` at least `7b`.  Hence

```text
b(n-b)+7b <= 2|E(G)| <= 10n-32.
```

The three numerical cases in the source are correct.

- At `b=10` the lower bound is `10n-30`, already too large.
- At `b=11` it gives `n<=12`, whereas an actual boundary has a nonempty
  connected side and a nonempty exterior, so `n>=b+2=13`.
- At `b>=12` it gives

  ```text
  (b-10)n <= (b-10)(b+3)-2,
  ```

  and therefore `n<=b+2`.  Equality with the reverse inequality forces
  the two vertex sets outside `S` to be singletons.  They are nonadjacent
  because one lies in `Y` and the other outside `N_G[Y]`.  Five-colouring
  `G[S]` and assigning both singletons one fresh sixth colour contradicts
  `chi(G)=7`.

Thus some `w` outside `S` has `7<=d_G(w)<b`.  The graph `G-S` has at least
two components: `Y` is one and the nonempty exterior contains another.
Whichever component contains `w`, a different component lies outside
`N_G[w]`.  Hence `N_G(w)` is again an actual boundary, and its order is
strictly smaller.

For an incident edge `wx`, the proper minor `G-wx` has a six-colouring.
Its endpoints must be monochromatic, or restoring `wx` would colour `G`.
The restriction to `G-w` and the restriction to the operated closed
singleton side induce the same boundary partition.  If that partition
also extended through the intact singleton side, a permutation of colour
names would align the two boundary colourings and glue them to a
six-colouring of `G`.  This proves every response assertion in Theorem
2.1.

## 4. Iteration and the degree-nine endpoint

Every new boundary has order at least seven by seven-connectivity and has
strictly smaller integer order while its order is at least ten.  Repeating
Theorem 2.1 therefore terminates at order seven, eight or nine.  Each
boundary produced during this numerical descent is an actual
singleton-side response; the operation and colouring may change from one
step to the next, as the source later records.

If the terminal order-nine boundary is `N_G(w)`, actualness gives
`G-N_G[w]` nonempty and the selected vertex has degree exactly nine.
These are precisely the additional hypotheses of the audited
degree-nine boundary-alignment theorem.  That theorem returns either an
operation-aligned full-neighbourhood response of order seven or eight, or
a component `C` and edge `wx` with

```text
N_G(C)=N_G(w),
```

both `C` and `{w}` full to this nine-set, `{x}` an exact boundary block in
every six-colouring of `G-wx`, and
`G[N_G(w)-{x}]` `K_5`-minor-free and four-colourable.  Corollary 2.2 does
not apply this conclusion to an arbitrary initial nonsingleton order-nine
response, and explicitly states that limitation.

## 5. Unlocked matching-edge transition

The audited forbidden-signature coupling theorem justifies the starting
facts in Theorem 3.1.  If `ab` is unlocked in colours `alpha,beta`, the two
components containing `a,b` each contain exactly one end of `cd`; both
deleted edges cross between the components; and switching either component
gives the opposite singleton response.  The two colourings agree literally
outside the switched component.

The two components cannot both dominate.  Distinct bichromatic components
have no edge between them in `H`, so their only edges in `G` are the two
independent restored edges.  Mutual domination forces each component to
consist of its two coordinate endpoints, and connectedness supplies the
other two edges of an induced four-cycle.  Contracting this cycle gives a
proper minor `L`.  A five-colouring of `L` would expand to a six-colouring
of `G` by colouring the two independent pairs of the cycle with the old
contraction colour and one fresh colour.  Thus `chi(L)=6`; `HC_6` supplies
a `K_6` model, which may be made spanning.  After lifting, the two
dominating components and the five foreign bags form a `K_7` model.

At least one crossed component `D` is therefore nondominating.
`N_G(D)` is an actual boundary of order at least seven, and the common
exterior restriction of the two switched colourings is proper in the
intact graph.  Its partition is rejected by the intact `D`-side.  Orders
seven and eight give outcome 1, order nine gives the literal common-trace
outcome 2, and a larger boundary invokes the valid descent and alignment
of Sections 3--4.  The descent may discard the original matching labels;
Theorem 3.1 does not claim otherwise.

## 6. The all-lock normal form

For an alternate colour `beta`, `K_beta` is a connected bipartite
component of the corresponding two-colour graph in `H`, and it contains
both ends of `e=ab`.  Those ends lie in the same bipartition class, so an
`a-b` path has even length and restoring `e` creates an odd cycle.
Conversely, recolouring one end of `e` with a third colour properly colours
`G[K_beta]`.  The other deleted edge is vertex-disjoint from `e` and was
already proper under the fixed colouring, so it does not invalidate this
recolouring.  Hence `chi(G[K_beta])=3`.

If `K_beta` is nondominating, its neighbourhood is actual.  The fixed
colouring is proper on `G-K_beta` because the sole monochromatic restored
edge lies inside `K_beta`, and it colours the operated side after deletion
of `e`.  The intact side must reject the common boundary partition.  The
same order reduction therefore gives outcomes 1--3 of Theorem 4.1.

If `K_beta` dominates, a `K_6` model in its complement would combine with
the connected dominating set to form a `K_7` model.  Thus the complement
is `K_6`-minor-free and at most five-colourable.  If it were at most
three-colourable, disjoint three-colour palettes on it and on
`G[K_beta]` would six-colour `G`; its chromatic number is therefore four
or five.

Finally, an outside vertex coloured `alpha` or `beta` cannot have an
`H`-edge into `K_beta`, since that would place it in the same bichromatic
component.  Domination forces any such contact to be one of the deleted
edges.  Both ends of `e` are already in `K_beta`, so only `f` can provide
it; at most one outside endpoint exists and `f` crosses into the
component.  This proves the final colour-distribution assertion and, when
the bounded response outcomes are excluded, the five-component all-lock
normal form.

## 7. Scope qualifications and unresolved assumptions

The source does not close the matching row.  In particular, none of the
proved arguments aligns a dominating lock component with four prescribed
foreign bags of the independently chosen spanning `K_6` model.  Nor does
the numerical boundary descent preserve the original matching edges,
minor-model labels or the original shore.  These are genuine remaining
requirements, stated accurately in Section 5 rather than silently
assumed.

The result is unbounded and computation-free.  Its trust chain includes
the established cases `HC_5` and `HC_6` through the cited audited
degree-nine theorem, and Mader's extremal bound and Jorgensen's equality
classification through the cited audited large-boundary theorem.  Before
external publication, those primary inputs should be cited with exact
theorem numbers where available; this is an editorial traceability point,
not a mathematical gap in the audited deductions.
