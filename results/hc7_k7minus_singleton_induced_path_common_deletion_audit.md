# Independent audit of the fresh induced-path common-deletion theorem

## Verdict

**GREEN** at the exact source revision

```text
55c636ad3f47310fc467daf8ad464e8162cc4343281dc612837117f76b1aef87  results/hc7_k7minus_singleton_induced_path_common_deletion.md
```

This is a separate internal audit, not external peer review.

## 1. Common-deletion connectivity

The cited incident-pair lemma applies to the two edges `uv,uw`.  Its only
failure of six-connectivity would give `d_G(u)=7`, which is excluded by the
critical-host bound `delta(G)>=8`.  Thus the common deletion `Q` is
six-connected.

If a six-set `T` separates `Q`, the seven-connected restoration
`Q+uw=G-uv` forces `uw` to join distinct components of `Q-T`.  Adding one
edge makes the graph connected, so there are exactly two such components.
Six-connectivity makes both full to `T`.  This justifies the component
choice `u in A`, `w in B` and every use of fullness in Theorem 2.1.

Only the deleted edges can cross between `A` and `B` in `G`.  Consequently

```text
N_G(A)=T+{w}             if v is in A or T,
N_G(A)=T+{v,w}           if v is in B.
```

These are disjoint unions.  The opposite open side is nonempty: if
`v notin B` and `B={w}`, fullness would give `N_Q(w)=T`, hence
`d_G(w)=7`; if `v in B`, connectedness of `B` and the nonedge `vw` force a
third vertex in `B`.  The displayed set is therefore the actual boundary,
of order seven or eight, rather than merely an upper bound for it.

## 2. Retained colouring responses

The three colourings have monochromatic-edge sets `\{uv\}`, `\{uw\}` and
`\{uv,uw\}`.  Since `u in A`, deleting `A` meets every such edge, so all
three restrictions to `G-A` are proper.  If any induced boundary partition
extended through the intact closed `A`-side, a permutation of colour names
would align the two boundary colourings and give a six-colouring of `G`.
All three traces are therefore rejected.

The edge `uw` has `u in A` and `w in N_G(A)`, so the singleton-`\{uw\}`
corner is a selected response on the returned boundary.  When `A={u}`,
fullness excludes `v in T`, and the exact identity
`N_G(u)=T+{v,w}` follows.

## 3. Path-contraction saturation and split

In a colouring expanded from the path contraction, every outside neighbour
of `u,v,w` avoids their common colour.  A colour missing at `u` permits
recolouring `u`; if both leaves miss colours, the two leaves can be
recoloured independently because `vw` is absent.  The saturation conclusion
of Lemma 3.1 follows.

A spanning tree of the co-bagged branch set may be chosen to contain both
path edges.  Deleting those two tree edges gives the three connected split
pieces in the source.  Four foreign `K_6` branch sets meeting all three
pieces yield seven branch sets whose sole possible missing adjacency is
between the two leaf pieces, hence a `K_7^-` minor.

## 4. Scope

The theorem terminalises only the failure of seven-connectivity of this
fresh induced-path deletion.  In the seven-connected outcome it does not
allocate the colour witnesses among four foreign model bags, and it does not
align the separately existential `K_6` and exact `K_7^vee` models.  The
source records both limitations and states the remaining inference only as
an unsupported target.
