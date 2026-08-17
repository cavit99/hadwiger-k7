# Author-side audit: the connected one-miss reduction

**Verdict:** **GREEN** at the frozen revisions below.  This is an
adversarial self-audit, not an independent or external review.

```text
bda284fabf9a414f73dee683474be3cf00d1bc973bc4d51c8f43b8d7771ad607
  active/hc7_k7minus_sevenconnected_degree_eight_one_miss_reduction.md
b27f6cacd4122e01efb65d4d714f28d2a7da7ff7552768cbec2281d9de8ef5c0
  active/experiments/sevenconnected_connected_exterior_profiles/verify.py
342693e517d87de5b8018e1d2692aa1d1979a7350107c9d8452e757020dbe64b
  active/experiments/sevenconnected_connected_exterior_profiles/README.md
```

## 1. Host reduction

Contracting the connected exterior `C` produces exactly the quotient used
by the verifier: the image of `C` is adjacent to the seven vertices of
`J-r`, is nonadjacent to `r` and the centre `v`, and the centre is complete
to `J`.  A `K_6^-` model in `J` would extend with `{v}` to a `K_7^-`
model, so the local `K_6^-` exclusion used by the imported census follows
from the host hypotheses.

The missed vertex has no neighbour in `C`.  Seven-connectivity therefore
gives

```text
7 <= d_G(r)=1+d_J(r),
```

which is precisely the verifier's filter `d_J(r)>=6`.  Regenerating the
complete order-eight local catalogue leaves exactly the thirteen asserted
labelled pairs.  A direct check also confirms that every one has an
attached local vertex of degree three.  Such a vertex has the centre and
three local neighbours, so minimum degree seven gives it at least three
distinct neighbours in `C`.  Hence `|C|>=3`.

## 2. Rooted-shore lift

For any four-set `Z` in `J-r`, the seven-set `J-r` is the exact
neighbourhood of `C`.  The frozen closed-shore lemma, at SHA-256
`ba6dbfe1ca9e89041b1a77174844c24598984cbe76349a55c41f15b2e997cc03`,
makes `(G[C union Z],Z)` internally four-connected.  Its order is at least
seven.  Jorgensen's rooted-diamond theorem therefore supplies four
disjoint connected rooted bags with at most one missing mutual adjacency.
Every literal edge of `J[Z]` joins the corresponding bags, so a missing
adjacency, if present, is one of the nonedges tested by the verifier.

For a fixed `Z` and a fixed possible missing pair, the completed graph used
by the verifier adds exactly the rooted-bag adjacencies known in the host.
Substituting the four rooted bags for their root vertices preserves
disjointness, connectivity and every tested interbag edge.  This remains
true when a quotient branch set contains several roots: its connecting
edges all represent literal root edges or certified rooted-bag contacts.
Thus every positive finite certificate lifts to `G`.

## 3. Exhaustiveness and negative scope

The verifier imports the complete order-eight extension generator and the
exact connected-bag minor recursion from the frozen degree-eight census.
For each of the thirteen profiles it tests all `35` four-subsets of the
seven attached roots and every nonedge which could be the rooted diamond's
sole missing pair.  Nine profiles admit a universally valid four-set; the
canonical positive models have digest

```text
7f684013b80ac226fddbc73405c7698a9040a01aaf1e58c0d8d9d1b432fa0500.
```

The exact closing-set counts are

```text
5,3,3,3,3,5,15,15,6,0,0,0,0,
```

in the verifier's pinned profile order.  Hence the four displayed pairs
are exactly the residues of this method.  The zero counts say only that no
four-root completion of the stated form closes them; they do not construct
a seven-connected target-free host.  The theorem correctly makes no claim
about a full exterior.

The pinned command was rerun under NetworkX 3.6.1 and reproduced all
assertions and the digest.  No host-lift, quantifier or residue-count defect
was found.
