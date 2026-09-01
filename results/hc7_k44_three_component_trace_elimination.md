# Elimination of the three-component adjacent-singleton trace

**Status.**  Written unbounded theorem; the adjacent audit identifies the
exact checked revision.  No finite computation is used.

Here `K_7^-` denotes `K_7` with one edge deleted.

## 1. Theorem

Let `G` be a vertex-minimal seven-connected `K_7^-`-minor-free graph
containing a specified literal `K_{4,4}` with shores `S_0,S_1`.  Let
`a,p,b in V(G)-(S_0 union S_1)` satisfy

\[
\begin{aligned}
 N_G(a)&=\{p,b\}\mathbin{\dot\cup}O,\\
 N_G(p)&=\{a,b\}\mathbin{\dot\cup}K,\\
 |O|&=|K|=5,\qquad N_G(a)\cap N_G(p)=\{b\},\\
 (N_G(a)\cap(S_0\cup S_1))
 &\cap(N_G(p)\cap(S_0\cup S_1))=\varnothing .       \tag{1}
\end{aligned}
\]

Suppose that the contraction trace of `ap` gives an exact seven-cut

\[
 E=\{a,p,x\}\mathbin{\dot\cup}S_0,                  \tag{2}
\]

where `x` is exterior to the literal core, and that `G-E` has exactly
three components.  Suppose also that `S_1` meets at least two of those
components, as forced by the audited exact
[contraction-trace theorem](hc7_k44_adjacent_singleton_contraction_trace.md).
Then `G` contains a `K_7^-` minor, a contradiction.

Consequently the three-component whole-shore trace of an adjacent singleton
pair cannot occur.

## 2. Two component pieces and two core vertices

Write the components of `G-E` as `C_0,C_1,C_2`.  Seven-connectivity makes
each component full to `E`.  Distribute the four vertices of `S_1` among
the three components.  Up to order, the nonzero distributions are

\[
                         3+1+0,\qquad 2+2+0,
                         \qquad 2+1+1.                \tag{3}
\]

Choose two components meeting `S_1`, relabel them `C_0,C_1`, and choose
one vertex `s_i in C_i cap S_1` from each, so that at most one chosen
component contains only one vertex of `S_1`.  For `3+1+0` choose the
components of sizes three and one; for `2+2+0` choose both components of
size two; and for `2+1+1` choose the component of size two and either
component of size one.

A component containing exactly one core vertex `s_i` is not the singleton
`\{s_i\}`.  Otherwise fullness to `E` would make `s_i` adjacent to both
`a,p`, contrary to the disjoint core label sets in (1).  Thus, for each
chosen component, `C_i-s_i` is nonempty.  Choose a component `W_i` of
`C_i-s_i`; in a chosen component containing at least two vertices of
`S_1`, choose `W_i` to contain another such vertex.

Since `W_i` is a component after deleting `s_i` from a component of
`G-E`,

\[
                         N_G(W_i)\subseteq E\cup\{s_i\}.          \tag{4}
\]

Seven-connectivity therefore says that `W_i` misses at most one vertex of
`E`.  If the chosen component contains at least two vertices of `S_1`,
then `W_i` contains a retained member of `S_1` and is adjacent to every
vertex of `S_0`.  The possible chosen one-core component also sees every
vertex of `S_0` except perhaps one, say `q`; if it misses `q`, equation
(4) and seven-connectivity force it to see `s_i`.

Attach `s_0,s_1` to two distinct singleton roots in `S_0`.  If the
one-core piece misses a root `q`, attach its removed core vertex to the
`q`-rooted set and attach the other removed vertex to a different root.
Otherwise choose any two distinct roots.  The four resulting connected
core branch sets have at least five of their six mutual contacts: the two
sets containing a vertex of `S_1` are universal to the other core sets.
Thus they form a `K_4^-` quotient.  Both `W_0,W_1`, and the untouched
component `C_2`, are adjacent to all four core branch sets.

## 3. Making the three component bags pairwise adjacent

Put

\[
                         P_0=\{a,p,x\}.               \tag{5}
\]

Equation (4) shows that each `W_i` sees at least two vertices of `P_0`.
We use the following elementary fact.  If `A_0,A_1` are subsets of a
three-set and `|A_0|,|A_1|\ge2`, then there are distinct

\[
                         r_0\in A_0,\qquad r_1\in A_1            \tag{6}
\]

such that `r_1 in A_0` or `r_0 in A_1`.  If the intersection has at
least two elements, choose two distinct common elements.  If it has order
one, use that common element for one representative and a different
element of the other set for the second.

Apply this fact with `A_i=N_E(W_i) cap P_0`, and let `r_2` be the remaining
vertex of `P_0`.  Define

\[
 B_0=W_0\cup\{r_0\},\qquad
 B_1=W_1\cup\{r_1\},\qquad
 B_2=C_2\cup\{r_2\}.                                \tag{7}
\]

These sets are pairwise disjoint and connected.  The condition in (6)
gives the contact `B_0B_1`.  Fullness of `C_2` to `E` gives the other two
contacts, so the three sets in (7) form a triangle.  Section 2 shows that
all three are universal to the four core branch sets.

The quotient on these seven branch sets has at least

\[
 \underbrace{3}_{B_0B_1B_2\text{ triangle}}
 +\underbrace{12}_{\text{all component-to-core contacts}}
 +\underbrace{5}_{\text{core }K_4^-}=20.             \tag{8}
\]

It is therefore a `K_7^-` minor, proving the theorem.  \(\square\)

## 4. Exact scope

The theorem is a direct, computation-free elimination of the entire
three-component response in the adjacent-singleton contraction trace.  It
uses only seven-connectivity, the literal core, the exact trace, fullness
of the three components, and the disjoint label sets of the adjacent
singletons.  The unique common neighbour `b` and the subcubic conclusion
for `G[E]` are not needed.

Together with the separately audited two-component literal-shore-split
elimination, this leaves only the two-component core-concentrated
rooted-contact profile among the contraction responses to an adjacent
singleton pair.  It does not eliminate that profile, a nonsingleton
minimum blocker, the literal `K_{4,4}` case, T44, Conjecture 21, or `HC_7`.
