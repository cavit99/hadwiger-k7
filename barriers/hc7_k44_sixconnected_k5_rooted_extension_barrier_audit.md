# Independent internal audit: six-connected rooted-`K_5` extension barrier

**Verdict: GREEN at the exact revisions below.**  The displayed labelled
construction satisfies the five-support inequality, its clique augmentation
is six-connected, and no `K_7^-` minor model can keep all five added clique
vertices as singleton branch sets.  The construction does contain the
displayed unrooted `K_7^-` model, so its stated scope is exact.

This is a separate internal mathematical and computational audit, not
external peer review.

**Audited source:**
[`hc7_k44_sixconnected_k5_rooted_extension_barrier.md`](hc7_k44_sixconnected_k5_rooted_extension_barrier.md)

**Source SHA-256:**
`f2db7bb270fc22abc473f1859a50c3f37dc5a1baf89038b65318669ea27cd4b6`

**Audited verifier:**
[`hc7_k44_sixconnected_k5_rooted_extension_barrier_verify.py`](hc7_k44_sixconnected_k5_rooted_extension_barrier_verify.py)

**Verifier SHA-256:**
`30907951777503c3348a4dddd509cb5e3820b3e9fd4c7bc516b389756b351c1d`

## Checks performed

The dependency-free verifier reconstructs the graph from its 25 labelled
edges and independently encodes it as graph6 `JhfwEDbKgs_`.  Direct planarity
inspection confirms that it is the icosahedral graph with one vertex deleted
and that `0,4,10,6,7` bounds the exposed pentagonal face.  Deleting any set of
at most three vertices leaves the host connected, while its minimum degree is
four; hence its vertex-connectivity is exactly four.

All five supports have order at least two.  Exhaustion over every nonempty
proper connected vertex set gives the claimed score minimum six and the exact
histogram

```text
{6: 32, 7: 155, 8: 398, 9: 508, 10: 317, 11: 73, 12: 2}.
```

Exhaustion over every bond, counted once as an unordered bipartition, gives
52 with one split support, 172 with two, and 243 with three.  There is no bond
splitting four or five supports.  The written planar explanation agrees with
this computation: a bond is a cycle in the plane dual and therefore uses at
most two edges incident with the dual vertex corresponding to the exposed
face; only the remaining support can contribute one further split.

The five-clique augmentation has 16 vertices and 51 edges.  It remains
connected after deletion of any set of at most five vertices and has minimum
degree six, so its vertex-connectivity is exactly six.  The verifier exhausts
every ordered pair of disjoint nonempty connected exterior branch sets while
holding the five clique vertices as singleton roots.  The maximum possible
number of quotient contacts is 19, below the 20 required for `K_7^-`.

Finally, the seven displayed unrooted branch sets are pairwise disjoint,
connected, and cover all 16 vertices.  Exhaustive adjacency checking gives
exactly 20 of the 21 quotient contacts, with the sole missing pair
`{10}`--`{7}`.  They therefore form the asserted unrooted `K_7^-` minor model.

## Exact scope

This is a counterexample only to the intermediate claim that the
four-connected five-support inequality forces a bond splitting at least four
supports, equivalently to the associated canonical rooted extension with all
five clique vertices fixed as singleton branch sets.  It does not include
the distinguished supports `R_a,R_b`, strict minimum-blocker inequality,
eligible vertex, or exact three-cut data.  It is not a counterexample to the
literal `K_{4,4}` partition theorem, T44, Conjecture 21, or `HC_7`; nor does it
refute an unrooted six-connected `K_5` extension theorem.

The adjacent fixed-seed nonextension check further shows that this particular
labelled seed cannot be completed to the full two-helper blocker data while
failing the exact closing-bond criterion.  That is a separate finite fact
about this seed, not an unbounded exclusion of planar facial obstructions.
