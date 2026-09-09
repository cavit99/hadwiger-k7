# Five rooted bags with two degree-five exceptions

**Status:** written proof; a [separate exact-source audit](hc7_five_root_two_degree_five_exceptions_audit.md) is recorded beside it.
This is a possible construction input, not a closure of C19 or HC7.
No novelty or comparative significance is asserted.

Graphs are finite and simple; set neighbourhoods are external. A rooted
model has disjoint connected bags containing its prescribed roots separately.

**Theorem.** Let `S={b,c,r,s,t}` be five distinct roots of G, with
`rst` a literal triangle, and put `D=V(G)-S`. Suppose `|D|>=3`, every
nonempty subset of D has at least five neighbours, every D vertex has
degree at least five, and at most two D vertices have degree five.
Then some `u in {r,s,t}` is admissible: there is an S-rooted model
with every pair of bags adjacent except possibly one of `ub,uc`.
Only one admissible triangle endpoint is asserted.

## Input

We use the four alternatives of Norin--Totschnig Theorem 8 as recorded
in [the degree-six source](../results/hc7_five_root_degree_six.md),
SHA-256 `289c5ad015b6c392ea69e8e26e15eba54b4eba7cb155789edd76b3dbb5c9f9a4`,
and its [separate audit](../results/hc7_five_root_degree_six_audit.md),
SHA-256 `6f13ffd37126c78a697b5752574fe06b6fd13b68dabb0d63e4e39d76a8f1d065`.
For four roots these are a rooted K4, an order-two rooted trisection,
the specified rooted separation of order at most three, or a plane
drawing with all roots on one face. The exact separation and trisection
conditions, and the earlier primary inspection, are retained there.
The changes here are the small endpoints and the degree-sum deficit.

## Two-nonroot endpoints

Consider the same boundary hypothesis with `D={p,q}` and both degrees
at least five. The only configuration with no admissible triangle root
is the following, up to exchanging p,q and triangle labels:

```text
pq is an edge; p misses exactly r and q misses exactly s;
there are no edges between {b,c} and {r,s,t}; bc is optional.
```

In this configuration every root has degree at most four. To verify
the classification, if pq is absent, both nonroots see all five roots,
and `b+p,c+q,r,s,t` form a rooted K5. If one nonroot is universal,
assign it to one helper and the other nonroot to an adjacent helper;
the latter misses at most one triangle root. If both degrees are five
and pq is present, each misses exactly one root. They cannot miss the
same root, by the boundary condition on D. If an omitted root is a
helper, assign the nonroots to the opposite helpers; again at most
one helper--triangle contact is missing.

It remains that p misses r and q misses s. Any helper--triangle edge
gives a model. By symmetry take its helper to be b. An edge br gives
`b+p,c+q,r,s,t`; an edge bs gives `b+q,c+p,r,s,t`. An edge bt gives
`b,c+q,r,s+p,t`, whose only possible hole is br. All displayed sums
are actual connected bags. Conversely, when no helper--triangle edge
exists, a singleton helper can contact two triangle bags only if p,q
occupy distinct triangle bags. Both helpers would then be singleton
and miss the third triangle bag. Otherwise each helper must own one
nonroot, leaving the two holes at r and s. Thus no admissible model
exists, even allowing unused nonroots or both in one bag.

## Root-preserving reductions

Choose a counterexample with minimum `|D|`. Every root sees D, since
`N(D)=S`. Suppose a root a has the unique D-neighbour p. Contract ap
and retain label a. A surviving nonroot misses old a, so its degree
and every nonroot-set boundary are unchanged, with p replaced by a.
The triangle and all five root labels survive, and any admissible
model lifts through the fixed preimage `{a,p}`.

If `|D|>=4`, this is a smaller graph in the theorem's class. If
`|D|=3`, the two-nonroot classification applies. A bad endpoint would
have both survivors of degree five, so p originally had degree at
least six. The merged root then has degree at least `d(p)-1>=5`,
contrary to the bad endpoint's root-degree bound. Consequently every
root of the counterexample has at least two D-neighbours.

Suppose next that b,c have exactly the same two D-neighbours p,q.
Contract the disjoint edges bp,cq. Surviving nonroots miss old b,c;
p,q are replaced by distinct roots, so all their degrees and set
boundaries are unchanged. The triangle survives and models lift.
For `|D|>=5` this contradicts minimality. If `|D|=4`, a bad two-vertex
endpoint would leave both degree-five exceptions among the survivors.
Thus p,q originally had degree at least six. Its absence of all
helper--triangle edges says that neither p nor q saw a triangle root.
Each then had at most five neighbours: the other three nonroots and
b,c. This is impossible.

If `|D|=3`, write `D={p,q,z}`. The vertex z misses b,c, so degree
at least five forces it to see p,q and all three triangle roots.
It has degree exactly five. At least one of p,q, say p, has degree
at least six and therefore sees at least two triangle roots. The bags
`b+p,c+q+z,r,s,t` give an admissible model: the second helper is full
to the triangle through z, the helpers meet through pz, and the first
helper misses at most one triangle root. Exchange p,q and b,c when
needed. This excludes the common-two-neighbour configuration entirely.

## Cofacial responses and the degree sum

All three triangle roots are inadmissible in the counterexample. Fix
one, u, and delete it, leaving the four roots b,c and the other two
triangle vertices. Every nonempty subset of D still has boundary at
least four. The rooted separation alternative is therefore impossible.

The rooted-K4 and trisection exclusions in Section 2 of the pinned
degree-six proof use only this boundary bound and the two normalizations
just proved, not degree six. In the rooted-K4 outcome, u must miss
both helper bags. Maximizing their union and minimizing the other two
bags leaves at most two actual ports out of the helper union; the
literal edge between the other triangle roots preserves their mutual
contact during transfers. The helper interiors would have boundary at
most four in G, so are empty. The two helper roots then have the
excluded common pair of D-neighbours. In a trisection, each specified
open part is its single root, the two common ports are nonroots, and
the retained triangle edge forces those isolated roots to be b,c,
giving the same excluded configuration.

Hence the planar alternative holds. The resulting graph is two-connected:
after deleting at most one vertex, every component contains a nonroot,
because each surviving root retains a D-neighbour. The internal-four
boundary bound puts at least three roots in each component, so there
cannot be two components. Its distinguished face
is consequently a cycle containing all four roots.

Put `k_a=|N_G(a) intersect D|`, `K=sum_(a in S) k_a`, and
`e_D=e(G[D])`. Let d be the number of degree-five vertices in D, so

```text
2e_D+K >= 6|D|-d,       d<=2,       k_a>=2 for every root a.
```

In the drawing for u, let h count nonroots on the distinguished face
and let `t_u=e(G[S-{u}])`. Euler's formula gives
`e(G-u)<=3|D|+5-h`. The facial cycle has at least `4-h` root--root
edges, so `t_u>=4-h`. Subtracting these edges and combining the bounds
yields

```text
e_D+K-k_u <= 3|D|+1,       2k_u >= K-d-2.
```

Sum over all three triangle roots and write `K_B=k_r+k_s+k_t`.
Then `K_B+3(k_b+k_c)<=3d+6<=12`, whereas the normalized root degrees
give a left side at least eighteen. This contradiction proves the
theorem. All inductions decrease nonroot order and retain actual
disjoint preimages; no simultaneous choice of the planar drawings is used.

## Application boundary

For a full-R component C at a four-cut of the actual C19 complement,
deleting v and two cut vertices leaves degree at least five, with at
most two possible degree-five exceptions if `|N(v) intersect C|<=2`.
However, only boundary at least four follows automatically after these
three deletions. This theorem requires five and cannot yet be applied
to that component without an additional argument.
