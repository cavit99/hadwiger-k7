# Internal audit: exact support-five legless-tripod elimination

**Verdict:** **GREEN.**

**Audited source:**
[`hc7_k7minus_support_five_legless_tripod_elimination.md`](hc7_k7minus_support_five_legless_tripod_elimination.md)

**Audited source SHA-256:**

```text
014ba7ef39e9c0fc2757a19ff53193d960966089f08e7e96c0fcb47532da991b
```

This hash identifies the exact theorem revision checked, including the
status link to this audit; that editorial status update did not alter the
theorem statement or proof.  The audit is a
separate internal mathematical audit, not external peer review.  No proof
gap remains within the exact setup of Section 1.

## 1. Scope of the verdict

The theorem is conditional on the complete support-five normal form stated
in its setup.  In particular, it assumes all of the following rather than
deriving them from an arbitrary two-cut of `F=G-Z`:

- nonadjacent poles `p,q` and exactly two full components `A,B`;
- no centre-pole edge;
- an induced `K_{1,2,2}` on the specified set `R`;
- the exact centre neighbourhoods `T_0,T_0,T_0,T_1,T_1` on `B`;
- a nonempty connected remainder `Q=B-R` with
  `N_F(Q)=R union {p,q}`.

The GREEN verdict therefore eliminates that exact normal form.  It does not
prove that every two-cut of `G-Z` has the form, and it does not supply an
exhaustive reduction from the general two-cut branch to the theorem's
hypotheses.

The displayed equality `|P_i|=5` follows from the assumptions: every centre
has degree eight, has three specified neighbours in `B`, has no neighbour
in `Z union {p,q}`, and has no further neighbour in `B`.  The additional
claims `alpha(G[P_i])=2` and `omega(G[P_i])<=3` are explicitly unused.

## 2. Relative boundary and the augmented graph

For every nonempty `X subseteq A`, its open neighbourhood has the disjoint
decomposition

```text
N_G(X)=N_A(X) dotunion {z_i : X meets P_i} dotunion L(X).
```

There is no omitted `B`-neighbour because `A` and `B` are distinct
components of `F-{p,q}`.  The set `B` remains outside both `X` and its
neighbourhood, so seven-connectivity applies and proves the relative-seven
inequality.

The proof that `hat J` is three-connected is valid.  After deleting at most
two vertices, every surviving special vertex lies in a component meeting
`A`.  For two such components with `A`-parts `X,Y` and
`k=|K cap A|`, relative seven-connectivity gives

```text
|M(X)|, |M(Y)| >= 5-k.
```

A type met on both sides places its unique representative among
`z_0,z_1,z_2,sigma,tau` in `K`, whence

```text
|M(X) cap M(Y)| <= 2-k.
```

Inclusion-exclusion in the five-element type set gives the incompatible
lower bound `5-2k`; the contradiction is strict for `k<=2`.

The nonplanarity count is also exact.  Replacing the incidences to `z_3,z_4`
by incidences to `sigma,tau` loses from a vertex of `A` only its possible
edges to `p,q`, so every such vertex has degree at least six in `hat J`.
The remaining degree contribution is

```text
3*6 + 2*5 + 3 = 31.
```

Thus the degree sum is at least `6|A|+31`, whereas a simple planar graph on
`|A|+6` vertices has degree sum at most `6|A|+24`.

## 3. External tripod statements and the order-three separation

I checked the cited primary source directly: N. Robertson, P. D. Seymour,
and R. Thomas, *Hadwiger's conjecture for `K_6`-free graphs*, Combinatorica
13 (1993), statements (3.4) and (3.5).  The theorem uses their conclusions
with the correct hypotheses:

- (3.5) gives either a tripod on the three feet or a disc drawing with the
  feet on the boundary when the specified order-at-most-two separation is
  absent;
- (3.4) makes an existing tripod legless when the specified order-three
  separation is absent.

Three-connectivity excludes the separation in (3.5), and nonplanarity
excludes the disc drawing.

Lemma 4.1 correctly excludes the remaining order-three separation.  Its
orientation and equality case were checked separately.  For a far-side
component with nonempty `A`-part `X` and `k` separator vertices in `A`, one
has `|M(X)|>=5-k`.  If `rho` is not in the separator, each met type needs
one of only `3-k` type representatives in the separator, a contradiction.
If `rho` is in the separator, equality forces:

- exactly `2-k` of `sigma,tau` into the separator;
- no original root into the separator; and
- all three original roots into the chosen far-side component.

Any nonempty `A`-set on the feet side would then see at most the two mixed
portals, the two poles, and the `k` separator vertices in `A`, giving
relative boundary at most `k+4<=6`.  Hence that `A`-set is empty.  For
`k=0`, this contradicts the required order of the feet side.  For `k=1,2`,
an endpoint foot outside the separator has five neighbours in `A`, all of
which would have to lie among at most two separator vertices.  These cases
are exhaustive because `rho` already occupies one of the three separator
positions.

A legless tripod is equivalently two triads meeting exactly in the three
feet.  Removing the artificial feet leaves two nonempty disjoint connected
sets `C_1,C_2`.  Each contains a distinct neighbour of `rho`, hence a
distinct centre from `z_0,z_1,z_2`, and each meets both `P_3` and `P_4`.
No artificial edge is used inside either set.

## 4. Audit of the seven branch sets

The four bags in `R` are pairwise adjacent and connected as claimed:

```text
K_0={r_0},  K_1={r_10,r_20},  K_2={r_11},  K_3={r_21}.
```

The bags `D_1=C_1 union {z_3}` and `D_2=C_2 union {z_4}` are disjoint and
connected because `C_1` meets `P_3` and `C_2` meets `P_4`.  They are
adjacent in both directions through `C_1 cap P_4`--`z_4` and
`C_2 cap P_3`--`z_3`.  Each is adjacent to all four `K_i`: its original
centre supplies the `T_0` adjacencies and its added centre supplies the
`T_1` adjacencies.

The first-hit path from `p` to `C_1 union C_2` exists because `A` is
connected and full to `p`.  Removing its final vertex makes the remainder
disjoint from both tripod interiors.  Joining that remainder to `Q` gives a
connected seventh bag `D_3`, since `Q` is connected and adjacent to `p`.
The equality `N_F(Q)=R union {p,q}` makes `D_3` adjacent to all four `K_i`,
and the final path edge makes it adjacent to at least one of `D_1,D_2`.

Consequently the seven branch sets are pairwise disjoint and induce every
required adjacency of

```text
K_4 join P_3 = K_7^-.
```

Extra adjacencies are harmless.  This completes the audit of the stated
conditional theorem.
