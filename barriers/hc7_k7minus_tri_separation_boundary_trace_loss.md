# An undecorated tri-separation reduction loses the original boundary

**Status:** barrier/counterexample to an intermediate claim.

This note refutes the claim that the Carmesin--Kurkofka reduction of an
ordinary three-separation determines its three original boundary vertices.
It does not refute their reduction construction, the canonical
decomposition, or the four-vertex exact-cut theorem in this repository.
The construction is not asserted to occur in a seven-connected
contraction-critical host; it shows only that tri-separation reduction by
itself does not retain boundary provenance.

## Construction

Let

\[
 T=\{a,b,c\},\qquad
 C=\{c_1,c_2,c_3,c_4\},\qquad
 D=\{d_1,d_2,d_3,d_4\}.
\]

Make `C` and `D` cliques.  There are no other edges except

\[
\begin{aligned}
 N(a)&=\{c_1,d_1,d_2,d_3\},\\
 N(b)&=\{c_2,c_3,d_2,d_3\},\\
 N(c)&=\{c_2,c_4,d_1,d_4\}.
\end{aligned}                                           \tag{1}
\]

Here (1) lists every edge incident with `a,b,c`.  The resulting graph `H`
has eleven vertices, twenty-four edges and minimum degree four.

### Lemma 1

The graph `H` is three-connected.

#### Proof

After deleting at most two vertices, both four-vertex cliques retain a
nonempty connected subgraph.  If both `b,c` survive, they cannot both lose
all neighbours in one clique: each of their four two-element neighbour sets
in `C,D` is distinct, while only two vertices were deleted.  If exactly one
of `b,c` survives, at most one clique vertex was deleted, so that vertex
still meets both cliques.  If neither survives, then `a` survives and no
clique vertex was deleted.  In every case a surviving member of `T` joins
the two cliques, and every other surviving member of `T` still meets one of
them.  Thus the remaining graph is connected.  The set `T` itself separates
`C` from `D`, so `kappa(H)=3`.  \(\square\)

## Two boundaries, one reduction

The ordinary three-separation

\[
                (C\cup\{a,b,c\},D\cup\{a,b,c\})       \tag{2}
\]

has boundary `\{a,b,c\}`.  On the `C`-side, the vertex `a` has the unique
neighbour `c_1`, while `b,c` each have two neighbours.  Its reduction is

\[
 A=C\cup\{b,c\},\qquad B=D\cup\{a,b,c\},              \tag{3}
\]

with mixed separator

\[
                         \{b,c\}\mathbin{\dot\cup}\{ac_1\}. \tag{4}
\]

Now consider the distinct ordinary three-separation with boundary
`\{b,c,c_1\}` and open sides

\[
                    \{c_2,c_3,c_4\},qquad
                    \{a,d_1,d_2,d_3,d_4\}.            \tag{5}
\]

On the second closed side, `c_1` has the unique neighbour `a`.  Reducing
`c_1` therefore gives exactly (3)--(4).  Both original separations are
nontrivial, and their common reduction is a strong nontrivial
tri-separation.

Hence the mixed separator (4) does not determine whether `a` or `c_1` was
the original boundary vertex represented by the edge `ac_1`.  In every
proper colouring they receive different colours, so the lost choice can
also change a boundary-colour label.

## Consequence

A label-preserving use of tri-separation reduction must retain, for each
replacement edge, its original boundary endpoint.  In an oriented reduced
separation, that endpoint's side membership identifies the side from which
it was removed; recording the side separately is optional.  This provenance
is sufficient to reconstruct the ordinary separation.  It does not by
itself preserve a Kempe component through torso contraction or expansion.
