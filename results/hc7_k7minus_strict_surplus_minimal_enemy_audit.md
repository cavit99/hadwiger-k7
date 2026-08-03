# Internal audit: strict-surplus minimal counterexamples

**Audited source:**
[`hc7_k7minus_strict_surplus_minimal_enemy.md`](hc7_k7minus_strict_surplus_minimal_enemy.md)

**Audited source SHA-256:**
`1a8531ffaec27ff17673b53798169c0952a3cf156e8c6a55763eb633ec13227e`

**Verdict:** **GREEN.**  The theorem is computation-free.  This is a
separate internal mathematical audit, not external peer review.
The revision differs from the initially audited source only by replacing
the pending-audit status line with the completed GREEN status; no theorem,
proof, dependency or scope statement changed.

## Dependencies checked

- [`hc7_k7minus_degree7_safe_contraction.md`](hc7_k7minus_degree7_safe_contraction.md),
  SHA-256
  `f69c7eefc74c6074173e5d4e0396e3c2a2a2635f0aba58c7b54f3559c2c16896`,
  with adjacent GREEN audit at that revision;
- J. M. Schmidt, *Tight bounds for the vertices of degree k in minimally
  k-connected graphs*, J. Graph Theory **88** (2018), 146--153,
  Theorem 4 and Lemmas 1--2, doi:`10.1002/jgt.22202`.

Schmidt's published notation agrees exactly with the source: `V_k` is the
set of degree-`k` vertices, `E_k` is the edge set induced by `V_k`,
`F=G-V_k`, and `c_F` is the number of components of `F`.  His Lemmas 1--2
state that `F` is a forest and `c_F+|E_k|>=k`; Theorem 4 states

\[
 |V_k|=\frac{|E(G)|-|V(G)|+c_F+|E_k|}{k-1}.
\]

The article attributes the two structural lemmas to the Mader sources
listed in the theorem note.

## Minimality and the exact counts

For `q(G)>=1`, deleting any edge retains the threshold
`|E|>=4|V|-2`.  If the deletion retained seven-connectivity, it would be
a smaller target-free counterexample.  Thus `G` is minimally
seven-connected and the Mader--Schmidt results apply with `k=7`.

Writing `n=ell+f`, direct substitution of
`|E(G)|=4n-2+q` into Schmidt's identity gives

\[
 6\ell=3n-2+q+c+e_L,
 \qquad
 3(\ell-f)=c+e_L+q-2.
\]

Since `c+e_L>=7` and `q>=1`, the latter integer identity gives
`ell>=f+2`.  Degree summation over `L`, followed by total degree
summation, gives exactly

\[
 |E_G(L,V(F))|=7\ell-2e_L,
 \qquad
 \sum_{z\in V(F)}(d_G(z)-8)=\ell-4+2q.
\]

Every nontrivial tree component of `F` has a leaf with at most one
neighbour in `F`; that leaf has degree at least eight and hence at least
seven distinct neighbours in `L`.  A singleton component has at least
eight.  The component-neighbour assertion is therefore valid.

## Safe contractions and exact cut pullback

The cited safe-contraction theorem applies separately at every
`x in L`.  It gives an incident edge `xy` with at most three common
neighbours and

\[
 q(G/xy)=q(G)+3-|N_G(x)\cap N_G(y)|\ge q(G).
\]

This sharper result correctly supersedes the earlier bespoke
``edge in at most four triangles'' argument; no such weaker argument is
used in the audited revision.

Minimality in order makes `G/xy` fail seven-connectivity.  The density
hypothesis excludes order eight for `G`, so the quotient has at least
eight vertices and admits a cut `X` of order at most six.  If the
contracted vertex `w` were outside `X`, splitting it back into the
adjacent vertices `x,y` would preserve the component containing `w` and
make `X` a cut of `G`.  Hence `w in X`.  Replacing `w` by `x,y` leaves
the same deleted graph and produces a cut of `G` of order `|X|+1`.
Seven-connectivity forces `|X|=6`, so the pullback is an exact
order-seven cut containing `x,y`.

Selecting one supplied edge for each vertex of `L` gives an edge set
covering `L`.  Each distinct edge covers at most two vertices of `L`, so
its cardinality is at least `ceil(ell/2)`, as claimed.

The added overlap conclusion is immediate but useful.  If a selected edge
has both ends in `L`, it gives the first alternative.  Otherwise the
selected edge at each `x in L` joins `x` to `F`.  If the endpoints in `F`
were all distinct, this would inject `L` into `F`, contradicting
`ell>=f+2`.  Thus two selected safe edges share an endpoint in `F` and form
the asserted two-edge star.  Both edges retain all the contraction and cut
properties already proved for the selected family.

## Scope

The stated limitation is accurate.  At `q=0`, edge deletion no longer
shows that a minimum enemy is minimally seven-connected, so the
Mader--Schmidt forest conclusions cannot be imported.  At positive
surplus, the theorem supplies a large family of density-preserving failed
contractions and exact seven-cuts, but proves neither that one contraction
retains seven-connectivity nor that the cuts combine into a `K_7^-`
model.  Their containing cuts may coincide or nest, so the safe two-edge
star does not itself supply a strictly smaller shore.  No closure of the
`4n-2` extremal target is claimed.
