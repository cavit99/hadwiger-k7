# Internal audit: stable-bag concentration in the all-rainbow `b=2` row

**Verdict:** **GREEN** for Lemma 2.1, Theorem 3.1, Corollaries 3.2 and
4.1, and the stated scope at the exact source revision below.  This is a
separate internal mathematical audit, not external peer review.

## 1. Exact revision checked

The audited theorem source
`hc7_k7minus_five_centre_b2_stable_bag_concentration.md` has SHA-256

```text
a36c4ce68dfe6a08c21ba759eb363a2ac8bfccc59c1105ee953ac159aca1d910
```

The audit also checked the theorem's direct uses of the separately audited
global five-root palette theorem, rainbow-triangle rooted-`K_5` theorem,
and two-private-contact theorem.

## 2. Spanning extension

The extension in Lemma 2.1 is valid.  Every uncovered component of
`G[D union {p,q}]` has an edge to the already covered union because that
host graph is connected.  Absorbing the entire component into an incident
bag preserves connectedness and disjointness and cannot destroy an old
interbag edge or a prescribed root.  Iteration therefore gives a spanning
rooted model.

## 3. Seven-bag composition and concentration

The omitted centre `z` is pole-free, so the four retained centres in `K`
include both pole-incident centres.  Their literal incident-pole edges make
`K` adjacent to the pole bags `P,Q`.  A retained-centre contact in a stable
bag makes `K` adjacent to that bag.

The two-private-contact construction gives disjoint connected adjacent
sets `X,K`, both disjoint from the five opposite-shore model bags.  The
path ends join `X` to `P,Q`, and the three edges from `z` to its prescribed
triangle contacts join `X` to all three stable bags.  Thus, if retained
centres meet two stable bags, the seven displayed connected sets are
pairwise adjacent except possibly for `K` and the third stable bag.  They
are an explicit `K_7^-` minor model.  This verifies the contradiction in
Theorem 3.1.

Because the rooted model is spanning, all vertices of `N_D(A)` lie in its
five bags.  Meeting at most one stable bag is therefore exactly the stated
containment in `P union Q union B_1` after relabelling.

## 4. Clean bags, boundary count, and private census

For either remaining stable bag `B_i`, concentration excludes every
retained-centre neighbour.  The omitted centre meets it through its unique
root `t_i`; its other two `D`-neighbours lie in the other stable bags.
Hence `N_Z(B_i)={z}` and `t_i` is private.

The opposite shore `C` is nonempty and has no edge to `B_i`, so
`N_G(B_i)` is a vertex separator.  Seven-connectivity gives order at least
seven.  Removing its unique centre member `z` leaves at least six boundary
vertices in `D union {p,q}`, proving (3.7).

Among the four retained centres, the two pole-free centres have two
private contacts each by the audited two-private-contact theorem, and the
two pole-incident centres have one each by the audited rainbow-triangle
theorem.  Contacts private to different centres cannot coincide.  All six
belong to `N_D(A)` and hence to `P union Q union B_1`, proving Corollary
4.1.

## 5. Scope

The proof is unbounded in the shore order.  It does not prove that one of
`P,Q,B_1` can be split while preserving the rooted model adjacencies, nor
that the two centre-clean stable bags can be rerooted.  The source states
this remaining obstruction explicitly and does not claim closure of the
`b=2` row or of the full two-cut branch.
