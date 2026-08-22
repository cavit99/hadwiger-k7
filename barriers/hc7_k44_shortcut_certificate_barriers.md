# Exact barriers to local `K_{4,4}` shortcut certificates

**Status:** two exhaustive finite RED tests.  They refute proposed local
certificate implications, not T44.  Every graph in the two families below
fails seven-connectivity.

## 1. One fat triangle on a shore

Start with a literal `K_{4,4}`.  Between three vertices on one shore, replace
the three edges of a triangle by respectively `a,b,c` internally disjoint
paths of length two, where `a,b,c` are positive and `a+b+c=7`.  There are
fifteen ordered profiles.

The self-contained verifier
`hc7_k44_fat_triangle_certificate_barrier_verify.c` enumerates every
spanning seven-bag minor model in each profile.  No profile has a
`K_7^-` minor; the largest quotient has 18 of the required 20 contacts.

The enumeration is complete.  In a connected graph, unused components of
a model may be absorbed into adjacent bags.  A spanning seven-bag model on
`n` vertices has a spanning forest of exactly `n-7` internal edges.  The
verifier enumerates every such forest and computes its quotient.

## 2. Alternate paths around one split branch edge

Split one shore vertex of `K_{4,4}` into adjacent vertices `s,t`, distribute
the four opposite-shore contacts as `1+3`, `2+2`, or `3+1`, and add between
one and six internally disjoint length-two `s-t` paths.  The eighteen
resulting graphs are all target-free.  The largest seven-bag quotient has
15 contacts.

The exhaustive verifier is
`hc7_k44_one_split_theta_certificate_barrier_verify.c`.  Thus even six
alternate paths around a split edge do not by themselves reconstruct the
literal core.  A valid lifting theorem must use how path interiors attach to
the rest of a seven-connected host.

## 3. Reproduction

```bash
cc -O3 barriers/hc7_k44_fat_triangle_certificate_barrier_verify.c \
  -o /tmp/t44-fat
cc -O3 barriers/hc7_k44_one_split_theta_certificate_barrier_verify.c \
  -o /tmp/t44-split
```

Run `/tmp/t44-fat a b c` for the fifteen positive triples summing to seven,
and `/tmp/t44-split left q` for `left in {1,2,3}` and `q in {1,...,6}`.
Exit status one with `NO_TARGET` is the expected RED certificate.  The
reproduced aggregate is

```text
fat_profiles=15 unexpected_status=0 max_quotient_edges=18
split_profiles=18 unexpected_status=0 max_quotient_edges=15
```

Pinned verifier hashes:

```text
14aae8c4fa35859a336573d41e69981234e7a121ed18027239572ad12423eb55  hc7_k44_fat_triangle_certificate_barrier_verify.c
7804e3af454721a792652c58ac8cd9b2f84b0ad9bf5087812f409c3aef78f2b5  hc7_k44_one_split_theta_certificate_barrier_verify.c
```

## 4. Sharpest current local near-miss

The tetrahedral literal-core family from the promoted portal-`K_4`
dichotomy is sharper.  It has order 12, 34 edges, connectivity four and
minimum degree four.  Its three shore-split orbits each have an explicit
seven-bag quotient with exactly 19 contacts, while the clique-sum proof
excludes a 20-contact quotient.  It is therefore one edge short in the
strongest possible exact sense, but is definitively not a T44
counterexample.
