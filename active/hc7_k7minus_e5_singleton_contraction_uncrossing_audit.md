# Internal audit: singleton-contraction uncrossing

**Verdict:** GREEN for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.

**Audited source:**
`active/hc7_k7minus_e5_singleton_contraction_uncrossing.md`

**SHA-256:**
`e4720b2641033396aabf333cc97d9f401df4577f8a6f337a44d7ca6aba0ac1c2`

No mathematical correction is required at this revision.

## 1. Five-cut excess and singleton contraction

The proof that every five-cut has a component of excess at least four is
exhaustive.  At seven boundary edges, the selected two vertices cover the
missing edges, leave a triangle on the other three roots, and each have the
boundary degree required by the two-shore cross-root theorem.  The
star-complement row is covered by the existing star-completion theorem.

Contracting `xs` deletes exactly

```text
1+d_J(s)
```

edges.  Triangle-freeness and the exclusion of `K_{1,4}` give
`d_J(s)<=3`, so the quotient remains at the `E5` threshold.  Every cut of
order at most four in the quotient contains the contracted vertex; lifting
it gives an exact five-cut of `G`.  If the lifted cut omitted `y`, then
`y` would join all surviving boundary roots and any other component would
have at most four neighbours.  Thus the asserted form

```text
Q_s={x,y,s} union R_s
```

is correct.  If both members of `R_s` were roots, the connected full
component `A` would join the two surviving roots, so the final root-count
bound is also correct.

## 2. Root-only small sides and boundary classification

Every component behind `Q_s` is full to that cut and therefore contains a
surviving root.  The universal high-excess component has order at least
`a=|A|`; since only `a+2` vertices survive, all other components together
have order one or two.  A low component containing a vertex of `A` would
give that vertex degree at most four.  Hence the low side consists entirely
of roots and has neighbourhood exactly `C_s`.

The seven-edge equality case is correctly eliminated in both size rows.
When the high component has order `a`, the boundary complement is the
already eliminated triangle type; the boundary triangle also ensures that
there are only two components.  When it has order `a+1`, fullness of the
remaining singleton root creates a triangle in `J`.

The six graphs listed in the classification exhaust the triangle-free
graphs on five vertices with no isolated vertex and maximum degree at most
three.  Direct inspection confirms that the necessary small-side conditions
leave only

```text
P_3 disjoint union K_2,          P_5,          C_5.
```

The degree contradiction in the subdivided-claw row and the external-
neighbour counts for `K_{2,3}` and the pendant four-cycle are valid.

## 3. Yuan's theorem and fragment uncrossing

Yuan's Theorem 3 was checked against the primary paper.  In the notation
of the source, the published definition requires every fragment of `H` to
meet `S` and

```text
kappa(H-W')=3-|W'|
```

for every `W' subseteq S` with `|W'|<=1`.  The source verifies
`kappa(H)=3`, `kappa(H-s)=2` for every `s in S`, and the fragment-trace
condition both before and after a singleton deletion.  Yuan therefore
supplies four distinct fragments with pairwise disjoint, nonempty
`S`-traces, at least three of them singletons.

A singleton-trace fragment is one component behind its three-cut.  The
low/high dichotomy, the two-root anti-fragment conclusion, and the inclusion
of all but one vertex of `A` in a high fragment are correct.  Since
`a>=3`, any two high singleton-trace fragments intersect.  Standard
fragment uncrossing then forces their two-root anti-fragments to be
disjoint.

The high orientations are exactly as stated:

- none for `P_3` disjoint union `K_2`;
- the two endpoint orientations for `P_5`; and
- the edge opposite the trace in `C_5`.

These give the claimed intermediate degree-five-root counts.

## 4. Strict descent from a boundary-degree-two root

If `d_G(t)=5` and `d_J(t)=2`, then `t` has a unique neighbour `p` in
`A`.  Deleting

```text
(S-{t}) union {p}
```

leaves the component `{x,t,y}` with excess

```text
2+11-12=1.
```

The universal high-excess lemma therefore puts a component of excess at
least four strictly inside `A-p`, contradicting the minimum choice of
`A`.  This eliminates `C_5`.

The `P_5` exclusion is also sound.  A high singleton trace can occur only
at an endpoint, and after the preceding descent a literal degree-five
singleton trace can also occur only at an endpoint.  Yuan supplies at least
three distinct singleton traces, but `P_5` has only two endpoints.  Thus
the sole surviving boundary is `P_3` disjoint union `K_2`, with at least
three degree-one roots of degree five.

## 5. Distinct representatives and further contraction cuts

With three degree-five leaves contributing six boundary edges, the exact
identity

```text
|E(G[A])|+|E_G(A,S)|=4a+8
```

and the simple-graph bounds give `a>=6`.  At equality, four degree-five
leaves do not supply enough edges.  With exactly three, the only numerical
possibilities are `(14,18)` and `(15,17)` for the internal and boundary
edge counts.  They make `A` respectively `K_6-e` or `K_6` and leave a
remaining root complete to `A`, giving a literal `K_7^-` or `K_7`.
Thus `a>=7` is correct.

The Hall argument is complete.  Three two-sets with union of order at most
two, or four with union of order at most three, combine with the unused
roots to give a separator of order at most four between the leaf roots
together with `x,y` and the nonempty remainder of `A`.  Smaller subfamilies
satisfy Hall's inequality automatically.  Hence distinct representatives
exist.

For `t in T` and `p in P_t`, every common neighbour of `t,p` is either the
unique neighbour of `t` in `J` or the other member of `P_t`.  Contracting
`tp` therefore preserves more than the `E5` density threshold.  The
quotient is non-five-connected by minimality and at least four-connected
by the standard contraction bound, so it is exactly four-connected.  Each
four-cut contains the contracted vertex and lifts to an exact five-cut
containing `t,p`.  The universal high-excess lemma and minimum choice of
`A` then give a unique high component of order `a` or `a+1`, exactly as
stated.

## Scope and unresolved obligation

The source does not prove the stated distinct leaf-pair repair and therefore
does not prove `(E5)`.  Distinct representatives do not supply simultaneous
disjoint extensions of the leaf pairs or the ten adjacencies of an
`S`-rooted `K_5` model.  Nor does one returned cut have a high component
smaller than `A`.  This is correctly identified as the first unsupported
inference.

The verdict is conditional on the cited exact-density, connectivity,
component-count, dense-boundary, rooted-composition, seven-edge and
three-component theorems.  Their current source revisions and adjacent
GREEN audits support every form used here.

One non-blocking provenance issue remains outside this source: the older
seven-edge audit records historical hashes for two transitive dependencies,
although their current replacement sources have separate hash-pinned GREEN
audits.  This does not affect the present verdict.
