# High labelled shores reduce to surplus one or two

**Branch:** `research/labelled-shore-descent`  
**Baseline:** `93079280ceedd5754105446e27bb76985ad8ffc0`  
**Status:** experimental written proof; independent audit pending.

This note supplements
[`strict_surplus_labelled_shore_descent.md`](strict_surplus_labelled_shore_descent.md).
It identifies the exact remaining numerical range after the corrected
eligible-shore recursion.

Throughout, let `G` be a minimum-order, then minimum-size, seven-connected
`K_7^-`-minor-free graph with

\[
q=q(G)=|E(G)|-(4|V(G)|-2)\ge1.
\]

For a connected set `C`, put

\[
k(C)=|N_G(C)|,
\qquad
\eta(C)=|E(G[C])|+|E_G(C,N_G(C))|-4|C|.
\]

Call `C` contraction-eligible when

\[
\eta(C)\le q+k(C)-4.
\]

## 1. Two-vertex shores and safe edges are identical

### Lemma 1.1

Let `uv` be an edge of `G` and put `P={u,v}`.  Then

\[
q+k(P)-4-\eta(P)
   =q+3-|N_G(u)\cap N_G(v)|.                         \tag{1.1}
\]

Consequently `P` is contraction-eligible if and only if `uv` is a
density-safe edge.

### Proof

Write

\[
c(uv)=|N_G(u)\cap N_G(v)|.
\]

The open neighbourhood of the edge has order

\[
k(P)=d(u)+d(v)-2-c(uv).
\]

Moreover

\[
\eta(P)
 =1+(d(u)-1)+(d(v)-1)-8
 =d(u)+d(v)-9.
\]

Substitution gives (1.1).  The right side is also the exact surplus of
`G/uv`.  `\square`

## 2. Every edge has at most six common neighbours

### Lemma 2.1

For every edge `uv` of `G`,

\[
                         c(uv)\le6.                    \tag{2.1}
\]

### Proof

Positive surplus and minimum size make `G` edge-minimal
seven-connected.  Apply the audited essential-edge six-separation theorem
to `uv`.  In `G-uv` there is a six-cut `S` whose two components contain
`u` and `v`, respectively, and `uv` is the sole edge of `G` between those
components.

A common neighbour of `u,v` cannot lie in either open component: its two
incident edges would give another cross-edge.  Every common neighbour
therefore lies in `S`, proving (2.1).  `\square`

## 3. The high-shore reduction

Assume that `C` is a connected labelled separator shore lying inside one
branch set `D` of the selected `K_6` model, is anticomplete to the named
uncontacted bag `U`, and contains at most one prescribed root.  The
corrected eligible-shore theorem applies to every internal density-safe
edge of `C`: its two ends form a connected eligible subset of `C`, remain
anticomplete to `U`, and contain at most the same one root.

### Theorem 3.1

Suppose `C` is non-singleton and no outcome of the eligible-shore theorem
is accepted: there is no threshold-preserving seven-connected proper
minor, exact-seven cut handoff, legal model reroute, or strict smaller
labelled shore.  Then every edge `uv` of `G[C]` satisfies

\[
                         c(uv)\ge q+4.                  \tag{3.1}
\]

In particular,

\[
                         q\le2.                        \tag{3.2}
\]

More precisely:

- if `q=2`, every internal edge of `C` has exactly six common neighbours;
- if `q=1`, every internal edge has five or six common neighbours.

### Proof

If an internal edge `uv` had `c(uv)<=q+3`, Lemma 1.1 would make the
pair `{u,v}` contraction-eligible.  Applying the corrected eligible-shore
theorem to this pair gives one of the excluded outcomes.  Hence (3.1)
holds for every internal edge.

The shore is connected and non-singleton, so it contains an edge.  Combine
(3.1) with Lemma 2.1:

\[
                         q+4\le6.
\]

This gives (3.2) and the two sharpened rows.  `\square`

### Corollary 3.2

For `q>=3`, every non-singleton labelled separator shore immediately
re-enters the eligible recursion.  Thus the entire high-shore obstruction
is absent in surplus at least three.

A singleton is never numerically high: for `C={v}`,

\[
\eta(C)=d(v)-4=k(C)-4,
\]

so the strict high inequality would require `0>q`.

## 4. Exact remaining problem

After the corrected eligible recursion and Theorem 3.1, the unresolved
strict-surplus states are confined to:

1. a singleton/root gate; or
2. `q in {1,2}` and a non-singleton shore every one of whose internal
   edges lies in five or six triangles.

The second state is not a generic high-excess shore.  Every internal edge
has an essential six-separation, and at `q=2` its six common neighbours
are exactly the six-cut.  A completion must couple those overlapping
six-cuts to the named missed model bag and the singleton/root terminal.
Ordinary support-mask enumeration or unlabelled boundary density does not
supply that coupling.
