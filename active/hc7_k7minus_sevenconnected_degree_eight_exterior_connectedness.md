# Exterior connectedness at a critical degree-eight centre

**Status:** computer-assisted proof, pending independent audit.  The finite
classification is exact and deterministic; the elimination of its sole
two-component residue is computation-free.

Write `K_7^-` for `K_7` with one edge deleted.

## Theorem

Let `G` be a seven-connected graph with no `K_7^-` minor, and let `v` be a
vertex of degree eight.  Put

\[
                         J=G[N_G(v)].
\]

Suppose

\[
 \delta(J)\ge3,\qquad K_4\not\subseteq J,
 \qquad \alpha(J)=3.                                  \tag{1}
\]

Then `G-N_G[v]` has at most one component.  In particular, if the exterior
is nonempty, it is connected.

The degree condition in (1) says exactly that every edge incident with `v`
has codegree at least three.  The other two conditions are the local
hypotheses available at a critical degree-eight centre.

## Proof

Suppose that the exterior has at least two components.  Every exterior
component `C` has

\[
                         N_G(C)\subseteq V(J).
\]

Seven-connectivity therefore gives `|N_G(C)|\ge7`.  Contracting any two
components to single vertices produces a minor consisting of `J`, the
centre `v`, and two nonadjacent exterior vertices, each complete to `J` or
missing one vertex of `J`.

The graph `J` has no `K_6^-` minor, since such a model together with the
universal singleton `\{v\}` would give a `K_7^-` model.  The exact quotient
classification described below now applies.  Up to relabelling,

```text
E(J)=03,04,07,12,13,14,25,26,34,56,57,67,
```

and the two contracted components miss one vertex from each of the twin
pairs `\{3,4\}` and `\{5,6\}`.  Relabel within the twin pairs so that the
components, say `C,D`, miss `3,5`, respectively.

There cannot be a third exterior component.  Its missed vertex would have
to lie in `\{5,6\}` when paired with `C`, and in `\{3,4\}` when paired with
`D`, which is impossible.  Thus `C,D` are the two exterior components and

\[
        N_G(C)=V(J)-\{3\},\qquad N_G(D)=V(J)-\{5\}.   \tag{2}
\]

In the displayed cubic graph, vertex `3` has three neighbours in `J`.
It is also adjacent to `v`, has no neighbour in `C`, and has degree at
least seven.  Consequently it has at least three distinct neighbours in
`D`, so

\[
                              |D|\ge3.               \tag{3}
\]

Put

\[
                             Z=\{2,3,4,6\}.
\]

Apply the closed-shore rooted-connectivity lemma to the seven-cut
`V(J)-\{5\}`, with open shore `D`.  It says that
`(G[D\cup Z],Z)` is internally four-connected.  By (3) it has at least
six vertices, so Jorgensen's rooted diamond theorem gives a `Z`-rooted
`K_4^-` model.  Write its four bags as `R_2,R_3,R_4,R_6`.

The literal edges `26,34` show that the possible missing adjacency between
these bags is one of

\[
                              23,24,36,46.            \tag{4}
\]

For each possibility, the following row gives seven disjoint connected
bags.  Here `C` denotes the whole component and juxtaposition with a
singleton means union.

| missing | seven bags |
|---|---|
| `23` | `1R_3`, `R_4`, `5R_2`, `R_6`, `07`, `v`, `C` |
| `24` | `R_2R_3`, `R_4`, `5`, `R_6`, `07`, `1v`, `C` |
| `36` | `R_2`, `R_4`, `5`, `R_6`, `07R_3`, `1v`, `C` |
| `46` | `R_2`, `R_3`, `5`, `R_6`, `07R_4`, `v`, `1C` |

Direct inspection using (2) and the displayed edge set of `J` shows that
all pairs of bags are adjacent except possibly, respectively, the pairs
`6--7`, `2--3`, `2--3`, and `2--3` in the order displayed within each
row.  Thus every row is a `K_7^-` model, a contradiction.  The exterior
therefore has at most one component. `\square`

## Exact finite input

The deterministic verifier enumerates every eight-vertex graph `J`
satisfying (1) and having no `K_6^-` minor.  There are `542` isomorphism
classes.  With two nonadjacent exterior images, each full to `J` or missing
one vertex, it checks all `24,390` profiles.  Exactly four avoid `K_7^-`:

```text
GMs`KK with missed pairs (3,5), (3,6), (4,5), (4,6).
```

It independently checks the four completion rows in the proof.  Run

```text
UV_CACHE_DIR=/tmp/uv-cache uv run python \
  active/experiments/sevenconnected_codegree2_profiles/verify.py
```

The verifier imports the audited exact minor engine and complete
order-eight extension generator from
[`hc7_k7minus_sixconnected_degree_eight_low_codegree_verify.py`](../results/hc7_k7minus_sixconnected_degree_eight_low_codegree_verify.py).

## Scope

The theorem eliminates every disconnected exterior under the critical
local hypotheses.  It does not eliminate the connected-exterior case and
therefore does not by itself prove that an incident edge has codegree at
most two.
