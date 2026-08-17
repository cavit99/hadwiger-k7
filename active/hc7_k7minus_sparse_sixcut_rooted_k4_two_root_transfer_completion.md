# Complete packet transfer in the two-rooted-`K_4` orientation

**Status:** proved unbounded theorem; independently twice cold-audited.  The
exceptional `(2,0,1)` transfer row cannot occur in the two-exchanged-root
orientation of the rooted-`K_4` portal descent.  Thus two disjoint
derived-boundary-full connected subgraphs force two disjoint
original-boundary-full connected subgraphs.

Write `K_7^-` for `K_7` with one edge deleted.  Let `G` be a six-connected
graph with no `K_7^-` minor.  Let

```text
S={z_1,z_2,x_3,x_4,p,q}
```

be a six-cut such that `G-S` has at least three connected `S`-full
components.  Fix one of them, `C`, and choose two others, `A,D`.

Suppose that the closed `C`-shore contains a rooted `K_4` model

```text
M_1,M_2,M_3,M_4
```

on the respective roots `z_1,z_2,x_3,x_4`, using only
`C union {z_1,z_2,x_3,x_4}`.  Suppose also that `L subseteq C` is a
connected exact fragment, disjoint from all four model bags, with

```text
N_G(L)=T={z_1,z_2,p,q,r_1,r_2},                     (1)
```

where `r_1,r_2 in C` both belong to `M_1 union M_2`.  Thus `M_1,M_2` are
the two support bags and this is exactly the two-root orientation returned
by the rooted-`K_4` portal descent.

Assume that `L` contains two disjoint connected subgraphs `P_1,P_2`, each
adjacent to every vertex of `T`.

## Theorem 1 (complete two-root transfer)

The component `C` contains two disjoint connected subgraphs, each adjacent
to every vertex of `S`.

Equivalently, in this rooted-`K_4` orientation,

```text
mu_T(L)<=mu_S(C).                                   (2)
```

### Proof

Suppose for a contradiction that `mu_S(C)=1`.  The audited exact
two-packet transfer theorem then puts the return in its unique exceptional
row, and the audited portal-collapse theorem gives

```text
C-L=R={r_1,r_2}.                                    (3)
```

Put

```text
Z_0=S intersect T={z_1,z_2,p,q},
Q=S-T={x_3,x_4}.
```

After relabelling `R,Q`, the portal-collapse theorem supplies the literal
matching edges

```text
r_1x_3,             r_2x_4,                         (4)
```

and at most one crossed `R`--`Q` edge.  Let

```text
e=1_{r_1r_2 in E(G)},
c=the number of crossed R--Q edges,
z=|E_G(R,Z_0)|.                                     (5)
```

The minus-four quotient lemma proves, in a target-free host, that

```text
e+c+z<=2.                                           (6)
```

Equation (3) and disjointness from `L` make the four rooted bags exact:

```text
M_1={z_1} union R_1,       M_2={z_2} union R_2,
M_3={x_3},                 M_4={x_4},               (7)
```

where `R_1,R_2` partition `R`.  Every portal belongs to a support bag by
hypothesis.  Connectedness of the two support bags requires at least two
edges among the portal edge and the `R`--`Z_0` incidences.  Indeed, if the
portals are split, each two-vertex support bag needs its root--portal edge;
if they lie together, the three-vertex support bag needs two edges.
Consequently

```text
e+z>=2.                                             (8)
```

Equations (6)--(8) force

```text
c=0,                e+z=2.                          (9)
```

We now eliminate the two possible portal allocations.

### Case 1: the portals are split between the support bags

Relabel the portals within (4) so that

```text
M_1={z_1,r_1},              M_2={z_2,r_2}.
```

Connectedness gives the two incidences `z_1r_1,z_2r_2`, so (9) says that
they are the only `R`--`Z_0` incidences and that `r_1r_2` is absent.  The
rooted model contacts now force the literal boundary edges

```text
z_1z_2,       z_1x_4,       z_2x_3,       x_3x_4.   (10)
```

For example, no portal or crossed edge can supply the
`M_1`--`M_2` contact, so it must be `z_1z_2`; the other three assertions
follow identically from the displayed singleton bags in (7).

The seven bags

```text
P_1,                 P_2,
{z_1},               {z_2},
{x_3,r_1},           {x_4,r_2},
A union {p}                                           (11)
```

are pairwise disjoint and connected.  The last five bags form a clique:
the four contacts in (10), the two support-bag edges
`z_1r_1,z_2r_2`, and the fullness of `A` supply all ten pairs.  Each of
`P_1,P_2` contacts every one of those five bags through, respectively,
`z_1,z_2,r_1,r_2,p`.  Thus only `P_1P_2` may be absent, and (11) is a
`K_7^-` model, a contradiction.

### Case 2: both portals lie in one support bag

By symmetry take

```text
M_1={z_1,r_1,r_2},           M_2={z_2}.
```

If `e=1`, then (9) gives `z=1`.  Let `u in Z_0` be the root incident with
the unique portal--`Z_0` edge, and write
`Z_0-{u}={u_1,u_2,u_3}`.  The seven bags

```text
P_1,                  P_2 union {u_1},
A union {u_2},        D union {u_3},
{u},                  {x_3,r_1},        {x_4,r_2}    (12)
```

are connected and disjoint.  The first four contact every other bag.  The
last two portal bags contact through `r_1r_2`, and `{u}` contacts the one
containing its portal neighbour.  Hence at most the other pair among the
last three bags is absent, so (12) is a `K_7^-` model.

It remains that `e=0` and `z=2`.  Connectedness of `M_1` and (9) force

```text
z_1r_1, z_1r_2 in E(G),
```

with no other `R`--`Z_0` incidence.  The rooted model now forces

```text
z_1z_2,       z_2x_3,       z_2x_4,       x_3x_4.   (13)
```

Using the same seven bags as in (11), the last five again form a clique:
this time their contacts are supplied by (13), the two edges from `z_1`
to the portals, and fullness of `A`.  The two packets contact all five
through `z_1,z_2,r_1,r_2,p`.  Once more only the packet pair may be absent,
giving a `K_7^-` model.

All portal allocations contradict target-freeness.  Hence
`mu_S(C)` is not one.  The general five-packet cap gives `mu_S(C)<=2`,
whilst one-packet transfer gives `mu_S(C)>=1`; therefore
`mu_S(C)=2`, proving the theorem.  \(\square\)

## Corollary 2 (the `k=2` portal branch is closed)

In a fragment-closed minimum-counterexample proof of

```text
eta_U(X)>=6
  => a punctured U-rooted K_5^- model or mu_U(X)>=2,
```

the two-exchanged-root outcome of the rooted-`K_4` portal descent is
terminal.  Hereditary rerooting excludes the rooted outcome in the proper
fragment; if excess forces two `T`-full connected subgraphs in `L`,
Theorem 1 transfers both to `S`.  Thus this orientation creates neither a
two-copy linkage obstruction nor an exceptional equality row.

The theorem does not settle the three- or four-exchanged-root portal
orientations.  It also does not prove the displayed local assertion; it
closes the complete `k=2` branch whenever that assertion, or another
argument, supplies the two derived full subgraphs.

## Pinned dependencies

```text
99b59c50f39b43653348997e137d799ff47d8c9e7f402b8dc330e481fd424416
  active/hc7_k7minus_exact_six_two_packet_transfer_obstruction.md
fd9bb404244c0dc247a9d30480e83bfec356ca2d686a64f23e91cfa5164cfc46
  active/hc7_k7minus_exact_six_two_packet_transfer_obstruction_cold_audit.md
9e1742e20e89f1df3cdb02f944873cc48dbc61bb6830e8e1a8be16b50b214eb1
  active/hc7_k7minus_exact_six_residual_portal_collapse.md
3df2585010cd685c346a1149b36bf89fe9ec95c1dfab0b0a7222e54dd765dd1d
  active/hc7_k7minus_exact_six_residual_portal_collapse_cold_audit.md
557b10d311f008962a1d0d65ba713a6f1c02d2b5dcdd74c7f5ce26baedbd65c9
  active/hc7_k7minus_exact_six_residual_minus_four_descent.md
6c998571d6152a0faa671281d210acd0f6b8b226d048ff32cb98984654cd2eea
  active/hc7_k7minus_exact_six_residual_minus_four_descent_cold_audit.md
6118da0fbbca965c241c8ff5259552744f96c2364d50f95ef0a8b87355be168c
  active/hc7_k7minus_sparse_sixcut_rooted_k4_portal_descent.md
55f1b477cc665f633ca036d06e373d44c1c559f71ddc98fc6f312aa12ce94262
  active/hc7_k7minus_sparse_sixcut_rooted_k4_portal_descent_cold_audit.md
```
