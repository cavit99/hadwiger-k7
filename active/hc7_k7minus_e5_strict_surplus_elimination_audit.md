# Audit: exact density of a minimum `4n-7` enemy

**Verdict:** GREEN.

**Source audited:**
[`hc7_k7minus_e5_strict_surplus_elimination.md`](hc7_k7minus_e5_strict_surplus_elimination.md)
at SHA-256

```text
71a69c7214469105422e87993be50e7cb89730605a17f7cdf448057b1702078f
```

This audit checks the written theorem that a lexicographically minimum
enemy to `(E5)` cannot have positive surplus.  It does not audit or claim
the full statement `(E5)`.

## 1. Deletion criticality and common neighbours

If `q>=1`, deleting any edge retains at least `4n-7` edges.  A
five-connected deletion would therefore be a same-order, smaller-size E5
enemy, so every edge is five-removal-critical.

For `e=xy`, let `X` be a cut of `G-e` of order at most four.  If one end
of `e` belonged to `X`, restoring `e` would make no change after deleting
`X`, contradicting five-connectivity of `G`.  If `x,y` belonged to the
same component of `(G-e)-X`, restoring `xy` could not join any other
component.  Thus `x,y` lie in distinct components.  Any common neighbour
outside `X` would give the path `x-z-y` in `(G-e)-X`; hence every common
neighbour lies in `X` and `c(xy)<=4`.  No assumption about a specially
chosen deletion cut is missing.

## 2. Contraction accounting

Contracting `xy` removes the edge `xy` and one copy of each of the
`c(xy)` parallel pairs, so

\[
 |E(G/xy)|=m-1-c(xy).
\]

With `m=4n-7+q`, `q>=1`, and `c(xy)<=4`, this is at least

\[
 4n-12+q\ge4n-11=4(n-1)-7.
\]

If `G/xy` were five-connected, it would be a smaller E5 enemy.  Therefore
every edge is noncontractible and the hypothesis of Su's theorem is met.
The graph is noncomplete: the only complete five-connected graph below
the target order is `K_6`, which does not meet the E5 density threshold,
while every larger complete graph contains `K_7^-`.

## 3. External theorem matching

Schmidt's Theorem 4 states for a minimally `k`-connected graph that

\[
 |V_k|=\frac{|E|-|V|+c_F+|E(G[V_k])|}{k-1},
\]

with `c_F` the number of components induced by the vertices of degree
greater than `k`.  At `k=5` this is exactly equation (3) of the source.

Su's theorem states that every vertex of a contraction-critical
five-connected graph has at least two neighbours of degree five.  This is
also reproduced verbatim as Theorem 1 of Qin--Yuan--Su.  Applying it to
the degree-five vertices themselves gives
`delta(G[L])>=2`, and therefore `e_L>=ell` by the handshake lemma.

## 4. Algebra and terminal contradiction

Substituting `m=4n-7+q` and `n=ell+f` into Schmidt's identity gives

\[
 \ell-e_L=3f-7+q+c.
\]

The inequality `e_L>=ell` therefore gives `3f+c+q<=7`.

If `F` were empty, five-regularity and the density equality would give
`3n=14-2q<=12`, contradicting five-connectivity.  Hence `f,c>=1`, and
with `q>=1` the last inequality forces `f=1`; consequently `c=1`.

For the unique vertex `z` of `F`, the exact identity gives
`e_L=ell+3-q`.  Since every edge from `L` either lies in `G[L]` or ends at
`z`,

\[
 d(z)=5\ell-2e_L=3\ell-6+2q.
\]

Simplicity gives `d(z)<=ell`, so `ell<=3-q<=2`.  Then
`|V(G)|=ell+1<=3`, the final contradiction.

## 5. Scope

The proof uses positive surplus twice: edge deletion remains at the E5
threshold, and the common-neighbour bound makes every contraction
density-safe.  At `q=0`, deletion falls below the threshold and neither
minimal five-connectivity nor Su's theorem follows.  The source therefore
states exactly the proved conclusion and does not promote it to a proof of
`(E5)` or of the seven-connected `4n-2` target.
