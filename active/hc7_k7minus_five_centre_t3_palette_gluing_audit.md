# Independent audit: three-root palette gluing

**Verdict:** GREEN.

**Audited source:**
`active/hc7_k7minus_five_centre_t3_palette_gluing.md`

**Source SHA-256:**
`e072f3edbffcf3f2116998213863feb6a6b53c3717cd2798fae94aa3ca79cc36`

This is a separate internal mathematical audit, not external peer review.  The
hash above identifies the exact theorem revision checked.  No source repair is
required.

Relative to the theorem revision originally checked, the source changes only
its audit-status metadata; no theorem or proof text changed, so the GREEN
verdict is retained.

## 1. Contraction-colouring criterion

In Lemma 1.1, `R union T` and `L union T` are connected and contain at least
two vertices.  Contracting a spanning tree of either set therefore gives a
proper minor.  On pulling a colouring back to the opposite closed side:

- all vertices of `T` may receive the contraction colour because `T` is
  independent;
- every edge from `T` to the retained side was represented at the contraction
  image; and
- every endpoint of an `L`--`R` edge avoids the contraction colour.

Thus both claimed closed-side colourings are proper.  A perfect matching in
the complement of the forbidden-position relation is exactly a permutation
of the five nonboundary colours on one shore, and it makes every `L`--`R`
edge proper.

The Hall count in Lemma 1.2 is exact.  A deficient set of `k` columns forces
at least `k(6-k)` forbidden positions.  For `k=2,3,4` this is respectively
`8,9,8`, while `k=1` and `k=5` give precisely a full column and a full row.

## 2. Theorem 2.1

If at most two selected centres have a pole edge, the split

```text
L=C,    T=S-P,    R=D union P
```

satisfies every hypothesis of Lemma 1.1.  The only crossing edges are the two
`C`-contacts of each centre in `P`, so there are at most four and neither Hall
exception can occur.

In the remaining case every selected centre has a pole edge.  The helper
normalisation is valid.  For each root bag, if its contacts with the two
helpers do not form one common singleton, a minimal tree through the root and
two distinct helper-contact vertices has a nonroot contact as a leaf.  Moving
that leaf to its corresponding helper preserves:

- connectivity of the diminished root bag and enlarged helper;
- the contact from that root bag to both helpers, using the tree edge back to
  the moved leaf for one contact and the other chosen portal for the other;
  and
- every required adjacency of the rooted `K^*_{4,2}` model (which imposes no
  root--root adjacencies).

This contradicts maximal helper order.  Likewise, a component outside all
six bags that meets a helper can be absorbed into that helper.  Consequently
the helper union has at most the four root portals as neighbours in `J`.
The opposite component `D` makes the resulting separation genuine.  Seven-
connectivity therefore forces all four portals and all three selected centres
into its neighbourhood.  Pigeonhole then gives one helper adjacent to two
selected centres.

For the decisive colouring, the two contracted sets in (2.9) are connected,
disjoint, and their contraction is proper.  The helper edge, one helper--
centre contact, and that centre's pole edge give the asserted triangle
`v_0 v_2 z_1`.  Pulling the colouring back makes the four boundary vertices
`r,s,p,q` monochromatic, makes `z_1,z_2` distinct, and makes every selected
centre avoid the boundary colour.  All pulled-back edges were represented in
the minor, and the four boundary vertices are independent, so this colouring
is proper on its closed shore.

The opposite contraction gives a proper colouring of the other closed shore
with the same monochromatic boundary.  There are exactly six crossing edges.
A full forbidden row is impossible because their right endpoints are only
three centres.  A full forbidden column is impossible because `z_1,z_2` have
distinct colours, so any one right-side colour occurs on at most two centres
and is incident with at most four crossing edges.  Lemma 1.2 therefore glues
the shore colourings and proves Theorem 2.1.

## 3. Dual-shore reduction

Lemma 3.1 correctly transfers infeasibility to `D`.  If a feasible path left
all five centres in a connected component `K`, a component of `K cap D`
would have at least two distinct contacts on the path: otherwise its
neighbourhood, contained in the five centres and at most one path vertex,
would contradict seven-connectivity.  Splitting the path between its first
and last contacts gives two adjacent end-subpaths, both adjacent to `K`.
Their contractions with `K` form a triangle and pull back to the forbidden
distinct response on `C`.

Two disjoint `S`-full connected subgraphs in `D` similarly yield the three
pairwise adjacent connected sets displayed in the source; the known
centre--pole edge supplies the only nonautomatic adjacency.  Hence
`mu_S(D)=1`.

For the five-root Du--Li--Xie--Yu application, every nonempty
terminal-avoiding member has neighbourhood at most six and lies in `D`, so it
would separate that member from `C`.  Seven-connectivity empties the
collection and gives the stated `6|D|+1` bound.  For an infeasible centre
pair, the two-root Seymour outcome gives neighbourhood at most three;
restoring the other three centres raises this to at most six.  The collection
is again empty, and the completed two-root graph is planar.  Since `D` is a
subgraph, this contradicts `chi(D)>=5`.  Thus every pair is feasible on `D`.

## 4. Slack algebra and rooted-density step

The identities in Lemma 3.2 were recomputed from

```text
8c+g_C = 2m_C+h_C+sum_i c_i
```

and the full five-root edge-bound slack.  They give exactly

```text
m_C       = 2c-1+s_C+g_C,
sum_i c_i = 4c-6-2s_C-xi_C.
```

For a minimal infeasible set of order `t`, the restricted Du--Li--Xie--Yu
bound has slack `sigma_C>=0`; subtracting it from the full bound gives (3.8).
Substitution gives (3.9), and for `t=2` gives (3.10).  Since `c>=6`, the three
omitted centres contribute `b_C(R)>=3`, whereas the selected pair has at
least four contacts.  The right side of (3.10) is at most zero, proving the
pair contradiction.

For `t=3`, the lower bounds on the two omitted-centre deficits and on the
three selected contacts force equality throughout (3.13).  This yields

```text
(c_r,d_r,rho_r)=(c_s,d_s,rho_s)=(6,2,0),
c_i=2 for each selected centre,
sigma_C=xi_C=0.
```

The remaining arithmetic is also exact: `h_C>=8`, `g_C>=0`, and
`xi_C=0` force `h_C=8`, `g_C=0`; hence `m_C+h_C=4c-5`.  For
`Q={r,s,p,q}`, the boundary is independent and

```text
e(G[C union Q])=4c+7=4|C union Q|-9.
```

The hash-pinned closed-shore lemma makes this rooted pair internally
four-connected.  Norin--Totschnig Lemma 12 bounds a rooted
`K^*_{4,2}`-free pair by `4|V|-10`, so the one-edge excess forces the rooted
model used in Theorem 2.1.

## 5. Dependencies and scope

The local dependencies checked were:

- `results/hc7_k7minus_five_centre_two_cut_reduction.md`, SHA-256
  `1917b5e3d183d44a2d905d2628272d10e4bc6f7ae0768b43cab0e9462b83332a`;
- its adjacent audit, SHA-256
  `d01183c936d79ea2e07f956c2e89f7291df9cc28a5dab3dda6b093c8a69c4ea3`;
- `results/hc7_closed_shore_rooted_connectivity.md`, SHA-256
  `ba6dbfe1ca9e89041b1a77174844c24598984cbe76349a55c41f15b2e997cc03`;
- its adjacent audit, SHA-256
  `03738f53f8892c786dadd236c529c59b7045b3dc8371de22f0836f3721e5e43a`.

The external inputs are Du--Li--Xie--Yu, *Linkages and removable paths
avoiding vertices*, Theorems 1.1 and 1.2, and Norin--Totschnig, Lemma 12.
Their specialisations used here agree with the already audited repository
applications.

There is no unresolved gap in the theorem as stated.  Its deliberate scope
is the no-singleton-contact branch with an inclusion-minimal infeasible root
set of order three.  It does not eliminate a singleton shore contact or a
minimal bad-root set of order four or five.

## Promotion recommendation

The exact audited revision is mathematically ready for promotion.  No source
edit is needed.
