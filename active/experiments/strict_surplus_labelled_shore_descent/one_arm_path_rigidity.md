# Rigidity of the sole root-free arm

**Status:** experimental computation-free reduction; independent audit
pending.

Retain the minimum singleton/root gate after the two-arm elimination.  Thus

\[
D-y=A_0\mathbin{\dot\cup}A,
\]

where `A_0,A` are the two components of `D-y`, the set `A` is root-free and
anticomplete to the named uncontacted bag `U`, and

\[
C=\{y\}\cup A
\]

is a minimum one-root blocker.  The multiply rooted donor `D` has minimum
order among spanning contact-maximal `K_6` models.

Let

\[
\Omega(A)=\{Q_i:\text{every }D-Q_i\text{ edge has its }D
                    \text{-end in }A\}.                \tag{1.1}
\]

The arm classification gives

\[
                         |\Omega(A)|\ge2.               \tag{1.2}
\]

## 1. The arm owns at most three duties

### Lemma 1.1

One has

\[
                         2\le|\Omega(A)|\le3.           \tag{1.3}
\]

Moreover the root side `C` misses at least one of the four foreign bags
other than `U`.

### Proof

Suppose first that `A` owns all four accessible foreign duties.  Put

\[
R=A_0\cup U.
\]

The six sets

\[
                         C,\ R,\ Q_1,Q_2,Q_3,Q_4       \tag{1.4}
\]

are a `K_6` model: `C-R` uses a `y-A_0` edge, `C` meets every `Q_i`
through `A`, `R` meets every `Q_i` through the old clique bag `U`, and the
four `Q_i` remain pairwise adjacent.  Both `C` and `R` are contacted by
different old roots of `D`, while `U` was uncontacted.  Hence (1.4) has one
more contacted bag than the original model, a contradiction.

The same construction works whenever `C` meets all four accessible bags,
regardless of ownership: `R=A_0 union U` still meets them through `U`.
Thus a target-free contact-maximal state has both conclusions. `\square`

## 2. The arm is a path with a unique gate

### Theorem 2.1

There is exactly one edge from `y` into `A`.  If its end in `A` is `g`,
then `G[A]` is a path with endpoints `g,h` for some vertex `h`.  The far
endpoint `h` owns at least two duties from `Omega(A)`.

### Proof

Call a vertex `v in A` transferable when `A-v` is nonempty and connected
and `D-v` is connected.  If such a vertex owned at most one foreign duty,
the same deletion/move argument used in the arm classification would
produce a spanning contact-maximal model with a strictly smaller multiply
rooted donor.  Hence every transferable vertex owns at least two duties.
Distinct transferable vertices own disjoint nonempty duty sets, all
contained in `Omega(A)`.

Suppose that `y` has at least two neighbours in `A`.  Every non-cutvertex
of `G[A]` is then transferable: after its deletion the connected graph
`A-v` still contains a neighbour of `y`.  A connected graph of order at
least two has at least two non-cutvertices.  They would own four disjoint
duties, contrary to Lemma 1.1.  Hence `y` has a unique neighbour `g` in
`A`.

Every non-cutvertex of `A` other than possibly `g` is transferable.  Since
`|Omega(A)|<=3`, there can be at most one such vertex.  On the other hand,
a connected graph of order at least two has at least two non-cutvertices.
Therefore `g` is a non-cutvertex and there is exactly one other
non-cutvertex, call it `h`.

A standard block-tree argument says that a connected graph with exactly two
non-cutvertices is a path: every block of order at least three or every
branching block-cut tree contributes at least three global
non-cutvertices.  Thus `A` is the path from `g` to `h`.  The vertex `h` is
transferable and consequently owns at least two duties. `\square`

## 3. Exact support rows

After relabelling, only the following two ownership rows remain.

### Two-owned row

\[
\Omega(A)=\{Q_1,Q_2\}.                                \tag{3.1}
\]

The endpoint `h` owns both duties.  Among `Q_3,Q_4`, at least one is
anticomplete to `C`; the other is either also anticomplete to `C` or is a
crossing bag met by both `A` and `A_0`.

### Three-owned row

\[
\Omega(A)=\{Q_1,Q_2,Q_3\}.                            \tag{3.2}
\]

The remaining accessible bag `Q_4` is anticomplete to `C`; otherwise
`C` would meet all four accessible bags and Lemma 1.1 would augment the
model.  Thus the connected split

\[
D=C\mathbin{\dot\cup}A_0
\]

has three `C`-only foreign bags and the two `A_0`-only bags `Q_4,U`.
The far endpoint `h` owns two or three of the three `C`-only duties.

## 4. Portal consequence

The arm neighbourhood is contained in

\[
\{y\}\cup\bigcup_{Q_i\ne U}N_{Q_i}(A).
\]

Seven-connectivity gives at least six literal arm portals in the accessible
foreign bags.  In the three-owned row they lie entirely in
`Q_1,Q_2,Q_3`, so one owned bag contains at least two distinct portal
vertices.  In the two-owned row, if both remaining accessible bags are
`A_0`-only, all six portals lie in `Q_1,Q_2`, and one owned bag contains at
least three.

The exact remaining operation is therefore a path-to-carrier bypass.  A
connected piece of a portal-rich owned bag which reaches an opposite
`A_0`-only bag, while its residual retains its old root and the other model
duties, gives a contact-increasing `K_6` model.  Failure is a literal locked
carrier attached to one endpoint of the path; support counts alone do not
eliminate it.
