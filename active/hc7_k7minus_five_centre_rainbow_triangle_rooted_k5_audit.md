# Internal audit: rainbow-triangle rooted `K_5`

Audited file:
`active/hc7_k7minus_five_centre_rainbow_triangle_rooted_k5.md`

Audited SHA-256:

```text
891aed883d8082c18e0c502cd7be7c67760daec8ad973b8eefa8477a2f8c4a19
```

**Verdict:** **GREEN** for Theorem 2.1, Corollaries 3.1--3.2, and their
stated scope.

This is a hash-pinned internal mathematical audit, not external peer
review.  The result eliminates an unbounded subcase of the all-rainbow
five-centre row.  It does not close the private-contact or pole-free
residues.

## 1. Audited dependencies

| input | source SHA-256 | audit SHA-256 |
|---|---|---|
| global five-root palette alternative | `b26f9f0d12822f93af55e3aa566fc75b985dcb5a17daa4ea2b329c8efea274c3` | `765df0db1168001a212c77e5f871abe4725d4c92cc4e11ae8d887ff808f92e6a` |
| five-centre two-cut reduction | `1917b5e3d183d44a2d905d2628272d10e4bc6f7ae0768b43cab0e9462b83332a` | `d01183c936d79ea2e07f956c2e89f7291df9cc28a5dab3dda6b093c8a69c4ea3` |

The remaining external input is Kuendgen--Pelsmajer--Ramamurthi,
Theorem 6.2: `K_{1,1,3}` is contractible.  The cited theorem has exactly
the rooted-minor conclusion used in the source.

## 2. Scheme and shore-confinement check

The five roots `p,q,t_1,t_2,t_3` have the five distinct colours
`beta,delta,gamma_1,gamma_2,gamma_3`.  The global palette theorem supplies
the six pole--triangle bichromatic connections, and the distinct response
supplies the pole--pole connection.  No selected path can contain a
different boundary root, and every open interior lies in `D`.

If a vertex lies on every path in a family, its colour lies in every
corresponding pair of endpoint colours.  Since root colours are unique,
all demand edges in the family have the root of that colour as a common
endpoint.  This verifies the full multiple-intersection clause of an
`H`-scheme, not merely its pairwise version.  Contractibility therefore
gives five disjoint rooted `K_{1,1,3}` bags on the closed `D`-shore.  The
three literal triangle edges add precisely the three missing stable-part
adjacencies, producing the claimed rooted `K_5`.

## 3. Seven-bag audit

For a pole-incident centre `z`, orient the poles so that `zp` is an edge
and put `Y=C union (Z-{z})`.  The set `Y` is connected because `C` is
connected and every other centre meets `C`.  It is disjoint from `{z}`
and all five rooted bags.

The required adjacencies are complete:

- the five rooted bags form a `K_5` model;
- fullness of `C` joins `Y` to the `p`- and `q`-bags;
- a `C`-contact joins `Y` to `{z}`;
- `zp` and the three edges `zt_i` join `{z}` to four rooted bags; and
- if no `t_i` is private, a centre in `Z-{z}` joins `Y` to each
  triangle-rooted bag.

Only `{z}`--`B_q` may be absent.  The seven bags therefore give an
explicit `K_7^-` minor, proving that at least one contact is private.
If another centre had the same contact triangle, none of its three
vertices would be private, proving Corollary 3.2.

## 4. Scope

The proof neither manufactures a pole incidence for a pole-free centre
nor controls the remaining two contacts once one private contact exists.
No unresolved assumption or gap remains inside the three audited claims
at the pinned revision.
