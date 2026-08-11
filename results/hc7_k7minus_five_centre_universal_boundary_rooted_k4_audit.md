# Internal audit: universal four-boundary rooted `K_4`

**Verdict:** **GREEN.**

**Audited source:**
[`hc7_k7minus_five_centre_universal_boundary_rooted_k4.md`](hc7_k7minus_five_centre_universal_boundary_rooted_k4.md)

**Audited source SHA-256:**

```text
0a2511508c313e06c47cf7837e823299be4dc665d0572a4a3b53fdde4a44191f
```

This is a hash-pinned internal mathematical audit, not external peer
review.

## 1. Checked local inputs

The audited
[five-centre two-cut reduction](hc7_k7minus_five_centre_two_cut_reduction.md),
at SHA-256

```text
1917b5e3d183d44a2d905d2628272d10e4bc6f7ae0768b43cab0e9462b83332a
```

supplies every global hypothesis used here: `G` is seven-connected;
`V(G)=C dotunion S dotunion D`; `C,D` are nonempty components of `G-S`
and hence are anticomplete; and, after orienting the opposite responses,
`chi(G[D])>=5`.

The audited
[closed-shore rooted-connectivity lemma](hc7_closed_shore_rooted_connectivity.md),
at SHA-256

```text
ba6dbfe1ca9e89041b1a77174844c24598984cbe76349a55c41f15b2e997cc03
```

applies with `A=D`, `R=C`, and every nonempty `Q subseteq S`.  For a
four-set `Q`, it excludes exactly the separations of `J_Q=G[D union Q]`
having `Q` on one closed side, a nonempty root-free open side, and order at
most three.  No ordinary four-connectivity assumption is substituted for
this relative statement.

Both recorded dependency hashes agree with their adjacent GREEN audits.

## 2. Checked external theorem

The published primary source was checked directly: Ruy Fabila-Monroy and
David R. Wood, *Rooted `K_4`-Minors*, *Electronic Journal of Combinatorics*
20 (2013), P64, Theorem 15,
<https://doi.org/10.37236/3476>.

Theorem 15 applies to an arbitrary finite graph with four distinct
nominated vertices.  The members of `Q` are distinct because `Q` is a
four-set.  Under the proof's contrary assumption, the theorem says exactly
that `J_Q` is a spanning subgraph of a graph in one of classes `A`--`F`.
The definition of `H^+` and the six class definitions establish all facts
used in the source:

1. every nominated vertex belongs to the base graph;
2. each added set `X_T` is disjoint from the base and is a clique;
3. its only neighbours outside `X_T` are the vertices of one triangle
   `T`; and
4. every class base is planar.

The theorem imposes no independence requirement on the nominated vertices,
so possible edges inside `Q` cause no missing hypothesis.

## 3. Added-clique separator check

Because `J_Q` is a *spanning* subgraph of `H^+`, it has the same vertex set
as `H^+`.  Thus a nonempty `X_T` cannot be ignored merely because some of
its incident edges are absent from `J_Q`.

Choose a component `W` of `J_Q[X_T]`.  Components are used here because
`J_Q` may omit edges of the clique present in `H^+`.  There is no `J_Q`
edge from `W` to `X_T-W`, and no `H^+` edge from `X_T` to the rest of the
base outside `T`.  Therefore

\[
                         N_{J_Q}(W)\subseteq T.
\]

The vertex sets

\[
 V(J_Q)-W,qquad W\cup N_{J_Q}(W)
\]

form a separation.  The first contains all roots because all nominated
vertices lie in the base graph; the second has nonempty open side `W`; and
the intersection has order at most three.  This is precisely forbidden by
the local connectivity input.  Hence every added clique is empty.

This argument also covers singleton components and the cases in which
`J_Q` omits some or all edges from `X_T` to `T`.

## 4. Planarity and chromatic contradiction

With every `X_T` empty, `H^+=H`.  The finite bases in classes `A`--`C`
are planar.  The bases in `D`--`F` are obtained from the displayed plane
graphs by attaching nominated degree-two vertices along outer-face edges,
which preserves planarity.  Hence `J_Q`, as a subgraph of `H`, is planar.

The graph `G[D]` is an induced subgraph of `J_Q`, so it too is planar.
The Four Colour Theorem gives `chi(G[D])<=4`, contradicting the audited
two-cut conclusion `chi(G[D])>=5`.  The contradiction proves the rooted
minor for the arbitrary four-set `Q`, and therefore for every four-set in
`S`.

## 5. Scope

The proof is unbounded in the orders of `C,D` and needs no finite search.
It proves existence separately for all 35 four-subsets of the seven-vertex
boundary.  It does not synchronize the resulting branch sets or by itself
compose them into a `K_7^-` minor.  No unresolved hypothesis or inference
was found in the stated theorem.
