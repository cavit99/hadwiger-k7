# Triangle-free odd subdivisions and the contractibility boundary

**Status:** written proof and barrier to an intermediate classification
claim, with a separate internal audit at the exact hash recorded beside
this file. The results give counterexamples to proposed extensions of bipartite
contractibility. They do not resolve Hadwiger's conjecture, establish a
classification of contractible graphs, or replace the completed universal
bipartite theorem. Current status remains in the
[research ledger](../RESEARCH_LEDGER.md).

## Definitions and the exact external input

All graphs here are finite and simple. A graph is *contractible* when
every scheme of that graph contains its minor rooted at every prescribed
vertex. A *totally odd subdivision* replaces each edge by a path of odd
positive length, with different replacement paths internally disjoint.

For a graph `H`, define `M'(H)` on two copies `v_0,v_1` of every vertex
`v`. Its edges corresponding to `uv in E(H)` are

```text
u_0 v_1,  u_1 v_0,  u_1 v_1.
```

The prescribed root for `v` is `v_0`. The paths
`u_0,v_1,u_1,v_0` form an `H`-scheme: each nonroot `v_1` occurs only on
paths for edges incident with `v`, and no other root is internal.
Call `H` *M'-contractible* if this particular scheme has a rooted
`H`-minor. Thus failure of M'-contractibility implies failure of
contractibility, with an explicit finite host for each target.

A *shift automorphism* of a graph is an automorphism `pi` satisfying
`v pi(v) in E(H)` for every vertex `v`.

The external proof input is Kündgen--Pelsmajer--Ramamurthi,
[*Finding minors in graphs with a given path structure*](https://arxiv.org/pdf/1207.6141),
Definitions 7.3--7.4 and Theorem 7.7:

> A triangle-free graph `H` is M'-contractible if and only if it has an
> independent set `S` such that a matching from `S` to `N_H(S)` covers
> `N_H(S)`, and `H-(S union N_H(S))` has a shift automorphism.

The empty independent set is allowed. The matching must cover the
neighbourhood, not merely `S`.

## A positive-weight obstruction

**Lemma 1.** Let `J` be a connected nonbipartite graph. Suppose its edges
have strictly positive real weights `w_e` and there is `d>0` such that
the incident weights sum to `d` at every vertex. Then
`|N_J(S)|>|S|` for every nonempty independent set `S`.

**Proof.** All weight incident with `S` goes to `N_J(S)`, so

```text
d |S| = w([S,N_J(S)]) <= d |N_J(S)|.
```

If equality holds, every edge incident with `N_J(S)` has its other end
in `S`, since every edge has positive weight. Consequently there are no
edges inside `N_J(S)` or from `S union N_J(S)` to its complement.
Connectedness implies `V(J)=S union N_J(S)`, making `J` bipartite, a
contradiction. This also excludes `|S|>|N_J(S)|`. ∎

**Corollary 2.** If a triangle-free connected nonbipartite graph `J`
has the weights of Lemma 1 and has no shift automorphism, then `J` is
not M'-contractible and therefore is not contractible.

**Proof.** For nonempty `S`, Lemma 1 prevents a matching from `S` from
covering `N_J(S)`. For empty `S`, the remaining condition in KPR
Theorem 7.7 would be a shift automorphism of `J`. Both possibilities
are excluded. The explicit counterexample host is `M'(J)`. ∎

This uses the positive weighting as a stated hypothesis. It does not
invoke an unverified regularizability characterization.

## An unbounded family of odd-subdivision obstructions

**Theorem 3.** Let `F` be a connected nonbipartite simple graph of minimum
degree at least three. Suppose `F` admits strictly positive edge weights
whose incident sum is the same positive number `d` at every vertex.
Let `H` be a totally odd subdivision of `F` which is triangle-free and
in which at least one edge is actually subdivided. Then `H` is not
contractible. More precisely, `M'(H)` has its canonical `H`-scheme but
has no rooted `H`-minor.

**Proof.** Write `w_e` for the weight of an original edge `e`.
For every edge, `0<w_e<d`, because each end has other positively
weighted incident edges. Along the odd replacement path for `e`, give
successive edges the alternating weights

```text
w_e, d-w_e, w_e, d-w_e, ..., w_e.
```

Every internal vertex now has incident sum `d`; every original vertex
still has its original incident sum `d`. The weights are strictly
positive. Subdivision preserves connectedness, and replacing an odd
cycle by odd-length paths preserves its odd parity. Thus `H` satisfies
Lemma 1.

It remains to exclude a shift automorphism `pi`. Choose a subdivided
edge with replacement path beginning `x,u,v,...,y`, where `x,y` are
original vertices. Its length is odd and at least three. The original
vertices have degree at least three and every internal vertex has degree
two. Since `pi` preserves degrees and sends each vertex to a neighbour,
`pi(u)=v`. The edge `xu` therefore requires `pi(x)` to be a neighbour
of `v` of degree at least three.

If the replacement path has length at least five, both neighbours of
`v` have degree two, which is impossible. If it has length three, its
vertices are exactly `x,u,v,y`, so `pi(x)=y`. But `x` and `y` are not
adjacent in `H`: their original edge was subdivided, and simplicity of
`F` excludes a second original edge joining them. This contradicts the
shift condition. Hence `H` has no shift automorphism. Corollary 2
completes the proof. ∎

Every connected nonbipartite regular simple graph of degree at least
three satisfies the weighting hypothesis by giving every edge weight
one. Thus the theorem is not restricted to one base graph or one degree.
Replacing every edge by a path of length at least three automatically
ensures the triangle-free hypothesis.

**Corollary 4.** Every triangle-free totally odd subdivision of `K_4`
is not contractible.

**Proof.** Use `F=K_4`, edge weights one and `d=3`. Triangle-freeness
ensures that at least one edge was subdivided. Theorem 3 applies. ∎

## What the family does and does not rule out

**Barrier to an intermediate classification claim.** Excluding skewed
thetas and connected cacti containing two odd cycles is not sufficient
for triangle-free contractibility. For example, replace every edge of
`K_4` by a path of length three. Corollary 4 excludes contractibility.
It contains neither proposed obstruction:

- A theta subgraph can branch only at two original `K_4` vertices.
  Its three internally disjoint paths must use the direct replacement
  path and the two paths through the remaining original vertices. Their
  parities are odd, even, even. A skewed theta instead has two odd paths
  and one even path.
- Every odd cycle is a subdivided triangle of the original `K_4`.
  Any two share an entire replacement path, so they cannot be the two
  cycles of a cactus subgraph. All other cycles come from four-cycles
  and are even.

The first unsupported inference in the proposed two-family
classification is therefore its sufficiency direction. This does not
refute a classification with further obstructions, or the stronger
candidate below.

**Conjectural target, not a theorem.** A finite graph is contractible if
and only if every one of its subgraphs is M'-contractible.

Necessity follows from KPR Lemma 2.2 and the definition of `M'(H)`.
No sufficiency proof is given here. In particular, neither a positive
canonical two-copy construction nor a finite list of such constructions
justifies lifting an arbitrary scheme. The universal bipartite theorem
proves sufficiency on the full bipartite subclass only.

## Applicable structure and the remaining proof obligation

Benchetrit--Sebő,
[*Ear-decompositions and the complexity of the matching polytope*](https://arxiv.org/pdf/1509.05586),
Theorem 2.2 and Lemma 2.3 give a full-degree characterization: in a
2-connected nonbipartite graph, absence of skewed thetas is equivalent to
every pair of odd cycles having an odd number of common edges, and to
the existence of a totally odd circuit basis.

Their Theorem A.1 states that a 2-connected simple skewed-theta-free
graph has no totally odd `K_4` subdivision if and only if the maximum
number of odd ears in an ear decomposition is at most one. Together
with Corollary 4 and KPR Theorem 7.10, this restricts every nonbipartite
2-connected subgraph of a triangle-free contractible target to that
class. It does not establish contractibility of that class: a proof
must still allocate all rooted branch sets through arbitrary schemes
and handle attachments at cut vertices. Appendix A.2 of the same
primary paper explicitly refutes parts of Cao's proposed construction
procedure, so that procedure cannot fill the missing step.

The next substantive positive obligation is a scheme reduction for this
structural class, with all roots and branch-set ownership preserved and
a strictly decreasing host parameter. A forbidden-subgraph condition on
the target alone does not supply such a reduction or its lift.
