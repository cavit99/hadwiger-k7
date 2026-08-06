# The `q=1,2` high shore has a low-degree spine

**Status:** experimental computation-free reduction; independent audit
pending.

Retain a minimum strict-surplus enemy `G` and an unresolved non-singleton
labelled shore `C` from the high-shore reduction.  Thus

\[
q\in\{1,2\},
\qquad
c(uv)=|N(u)\cap N(v)|\ge q+4
\quad(uv\in E(G[C])).                                  \tag{1.1}
\]

Let `L` be the degree-seven vertices and let `F=G-L`.  The audited
strict-surplus theorem says that `G[F]` is a forest.  Let `K` denote the
unique possible literal `K_5` of `G`.

## Theorem 1 (reserve-blind vertices have shore degree at most two)

If

\[
v\in C\cap(L-K),
\]

then

\[
                         d_{G[C]}(v)\le2.              \tag{1.2}
\]

### Proof

The degree-seven vertex `v` is reserve-blind, so the canonical
six-boundary theorem applies at `v`.  Put

\[
H_v=G[N(v)].
\]

The six-vertex boundary argument in
`safe_root_leaf_or_low_branching.md` shows that at most two vertices of
`H_v` have degree at least five.

For an internal neighbour `u in N_C(v)`,

\[
d_{H_v}(u)=|N_G(u)\cap N_G(v)|=c(uv)\ge q+4\ge5.
\]

Thus every internal neighbour of `v` belongs to that at-most-two set,
proving (1.2).  `\square`

## Corollary 2 (the exact `q=2` local shapes)

Assume `q=2` and let `v in C cap(L-K)`.

1. If `d_C(v)=1`, with neighbour `u`, then
   \[
   N(v)-\{u\}=N(u)\cap N(v).                           \tag{2.1}
   \]
   Hence the essential-edge six-separation for `uv` is the canonical
   separation which isolates the singleton `v` behind the six-set
   `N(v)-{u}`.
2. If `d_C(v)=2`, with neighbours `u,w`, then `uw in E(G)`; in particular
   `v,u,w` form a literal triangle inside `C`.

### Proof

Every internal edge has exactly six common neighbours by the high-shore
reduction.  Since `v` has degree seven, the six vertices of
`N(v)-{u}` are all common neighbours of `u,v`, proving (2.1).  If `w` is
a second internal neighbour, it belongs to `N(v)-{u}` and hence is
adjacent to `u`.  `\square`

## Corollary 3 (a bounded-degree vertex exists in every high shore)

Every unresolved high shore `C` contains a vertex of shore degree at most
six.  More sharply, it contains a vertex of shore degree at most two unless
all its degree-seven vertices lie in the unique possible `K_5`.

### Proof

If `C` contains a reserve-blind degree-seven vertex, use Theorem 1.  If it
contains no degree-seven vertex, then `C subseteq F`, so `G[C]` is a tree
and has a leaf.  In the remaining case, every degree-seven vertex of `C`
lies in `K`, of which there are at most five.  The graph induced by the
vertices of `C cap F` is a forest.  A leaf of that forest has at most one
neighbour in `C cap F` and at most five neighbours in `C cap K`, giving
shore degree at most six.  If `C cap F` is empty, then `|C|<=5`, so every
vertex has shore degree at most four.  `\square`

## Exact endpoint

At `q=2`, every reserve-blind vertex on the high shore is therefore either
on the canonical singleton side of an unsafe edge or is the centre of an
internal triangle.  At `q=1`, the same vertices form paths and cycles of
shore degree at most two, but an internal edge may miss one of the other
six neighbours.

This reduction is unbounded, but not terminal.  The canonical singleton
orientation in (2.1) can be self-similar, while the triangle orientation
requires a labelled triangle contraction or a strict cut descent.  The
five vertices of the unique possible `K_5` are the only locations at which
the low-degree spine can fail.
