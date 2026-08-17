# Independent cold audit: rooted-`K_4` singleton transfer

**Verdict:** GREEN.

Audited source:

```text
0940ce049a348dc752be5460ec98ed4f7a2872d57d15e4c1181d442853ae1d88  active/hc7_k7minus_sparse_sixcut_rooted_k4_singleton_transfer.md
```

The Menger step is valid.  In
`H=G[A union {p,q}]`, failure of two disjoint paths between the two
two-sets gives a separator of order at most one.  The empty separator is
impossible because `A` is connected and full at `p,q`.  Removing a
one-vertex separator leaves both terminal sets nonempty.  A component on
the `{x,y}` side lies in `A` and has all of its host neighbours in the four
omitted roots `Z` and the separator vertex.  The other two open lobes lie
on a far side, so this is a host cut of order at most five, contrary to
six-connectivity.

The resulting paths use distinct endpoints.  Their intersections with
`A` can be joined by a shortest `A`-path whose internal vertices avoid
both paths; absorbing those internal vertices preserves disjointness and
makes the two path bags adjacent.  Each path bag sees every rooted bag
through its common-`Z` endpoint, and the third full component sees the
path bags through `p` and `q`.  Together with the four rooted bags these
are seven pairwise adjacent connected bags.  Thus two common-`Z`
vertices in an opposite lobe are indeed impossible.

The incidence sums in Corollary 2 count each vertex exactly
`binom(a(v),4)` times.  The capacity-two carrier theorem is lowered to one
on precisely the union of the rooted-status and boundary-path families,
so the constants `30-|R_C union R_D|` and
`30-|R_C union R_D union Q(U)|` are exact upper bounds.

For Corollary 3, an internal leaf contributes at least five and an
internal degree-two vertex at least one to that incidence sum.  The
connected-graph degree identity gives
`h<=2 beta-2+n_1`; hence
`|A|<=M_A+2 floor(M_A/5)+2 beta-2`.  Substitution of `M_A<=15` gives the
stated tree bound nineteen.

The source carefully restricts the theorem to singleton common
neighbours and does not repeat the invalid arbitrary-carrier anchoring
inference.  I found no separator, bag-adjacency, counting, or scope error.
`git diff --check` passes.
