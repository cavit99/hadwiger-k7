# Cold audit: order-seven theta singleton completion

**Verdict:** **GREEN** at the pinned revisions below.  This certifies the
counting reduction, all nineteen orbit representatives, the verifier's
coverage, and the returned-cut composition.  It is not external peer review.

## Pinned artefacts

```text
093c25e97ff5e5d627d12915c551418cd0039f5fb1f745dc03bdeb64148d7d75
  active/hc7_k7minus_sparse_sixcut_order_seven_theta_singleton_completion.md
f24ef3026763a595f4fc3cd9f61fc482b05d9ed281e99fe48f02b987746f51ff
  active/experiments/sparse_sixcut_order_seven_theta_singleton/verify.py
```

The source differs from the mathematical revision first audited only in its
status line: it now records the completed independent cold audit.  The
statement, proof, table, reproduction instructions, and verifier are
unchanged.

The standard-library verifier was rerun independently and reproduced

```text
checked_models=34560
order-seven theta singleton completion: PASS
```

## 1. Counting reduction

Each of the three theta graphs has six vertices and seven edges.  After the
perfect matching is made diagonal, the six diagonal incidences and the two
oriented incidences supported by each theta edge account for at most
`6+2*7=20` boundary edges.  Hence a total of at least `21` forces an
off-diagonal incidence `s_i w_j` for which `w_iw_j` is a nonedge.  This uses
neither relative connectivity nor a packet hypothesis.

The displayed canonical edge sets are respectively the unions of paths of
lengths `2,2,3`, `1,2,4`, and `1,3,3` between vertices `0,1`.  Each has
eight undirected nonedges and therefore exactly sixteen directed nonedges.

## 2. Bag templates and the orbit table

For `P(o;b)`, the bag rooted at `s_b` contains `w_b,u,w_o` and is connected
through the universal vertex `u`.  It contacts all four diagonal bags through
`u`; the required near-clique condition is therefore exactly five contacts
among those four bags.  For `F(o;a;b)`, the bag rooted at `s_a` contains
`w_a,w_o`, and every table use has an edge or the specified extra incidence
joining these vertices to the root.  The bag rooted at `s_b` contains `u`
and is universal to the other four bags.  Again only five of the six contacts
among the remaining four bags are required.

I reconstructed every representative directly from the canonical edge set
and the one directed incidence.  All five bags are connected and pairwise
disjoint, use five distinct roots, omit the stated sixth root, and have
exactly the possible missing contact printed in the last column.  In
particular, the bracketed entries correctly denote contact between the folded
bag and the indicated diagonal bag.

The computed automorphism groups give exactly the directed arc sets printed
in the nineteen rows.  The row orbits are pairwise disjoint and, within each
theta, their union has order sixteen, so no directed nonedge is omitted.
Simultaneous automorphism of roots and matched shore vertices preserves every
bag assertion.

As a separate adversarial check, I built the minimal graph containing only
the six diagonal boundary edges, one directed-nonedge incidence, the theta
edges, and the six edges from `u` to `W`.  An independent unrestricted
five-bag enumerator found a punctured rooted `K_5^-` in all `3*16=48`
labelled directed-nonedge cases, with no failure.

## 3. Verifier coverage and returned-cut consequence

The verifier reconstructs each theta and its full automorphism group, checks
the stated orbit equality and disjointness, and verifies root placement,
bag connectedness, bag disjointness, and all ten pairwise contacts.  Its
`6!` simultaneous relabellings cover every labelling supplied by a perfect
matching.  Thus its exact count is

```text
3 * 6! * 16 = 34560.
```

In the order-seven `i=1` Hall return, `C={u} union W`, the vertex `u` is
root-invisible and universal to `W`, and `W` has a perfect boundary matching.
For a theta core, `e(C)=6+7=13`, so

```text
eta_S(C)=13+e(C,S)-4*7=e(C,S)-15.
```

Hence `eta_S(C)>=6` supplies the theorem's threshold `e(C,S)>=21`.  To
complete the returned punctured five-bag model in the original three-lobe
setting, absorb the omitted root into one of the two other full components
and use the remaining full component as the seventh bag.  The absorbed root
supplies the contact between those two bags, while fullness supplies all ten
contacts to the rooted five-bag model.  Consequently only the model's one
allowed missing contact remains, giving a `K_7^-` minor.

No counting, orbit, bag-contact, confinement, or completion defect was found.
