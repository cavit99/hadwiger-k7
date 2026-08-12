# The portal edge is a threshold cycle problem

**Status:** written reduction and recorded route nonclosure;
[separate internal audit GREEN](hc7_k7minus_portal_edge_cycle_threshold_audit.md).
This note does not prove the `K_7^-` six-colour conjecture or `HC_7`.

## 1. Setting

Use the notation of
[`hc7_k7minus_six_coordinate_forest_reduction.md`](hc7_k7minus_six_coordinate_forest_reduction.md).
Thus `G` is seven-connected with minimum degree at least eight,

\[
 F=M_0\cup\{a,b\},\qquad X=G-F,
\]

where `M_0` is a matching of order four and `F` is either a matching of
order six or the disjoint union of `M_0` and an induced path `s-r-t`.
In the row considered here, `X` is seven-connected.  Fix an edge

\[
                         e=pv\in E(X)                 \tag{1.1}
\]

from the exceptional bag `P` to a selected portal `v` in a universal bag
of the exact spanning `K_7^vee` model.  This note treats the clean case

\[
                         V(e)\cap V(F)=\varnothing.   \tag{1.2}
\]

The desired strengthening would put `e` and all six edges of `F` on one
cycle.  The point of this note is to identify exactly what the published
cycle theorems do and do not prove at these parameters.

## 2. The exact two-cycle reduction

### Theorem 2.1 (portal edge and six coordinates lie on at most two cycles)

Under (1.1)--(1.2), there are at most two pairwise vertex-disjoint cycles
of `G` whose union contains `F\cup\{e\}`.

If `F` is a matching, then for every `f=uw\in F` and every chosen end
`q\in\{u,w\}`, there is also a cycle containing

\[
                    (F-\{f\})\cup\{e\}\cup\{q\}.    \tag{2.1}
\]

If `F=M_0\cup\{rs,rt\}`, there is a cycle containing
`M_0\cup\{rs,e\}` and another containing `M_0\cup\{rt,e\}`.

#### Proof

First suppose that `F` is a matching.  Then

\[
                           L=F\cup\{e\}               \tag{2.2}
\]

is a set of seven independent edges in the seven-connected graph `G`.
Moreover

\[
                           G-L=X-e
\]

is connected, since `X` is seven-connected.  The main theorem of
Kawarabayashi on the Lovasz--Woodall conjecture therefore gives one or two
vertex-disjoint cycles whose union contains `L`.

For the second assertion, the six independent one-edge paths
`(F-{f}) union {e}` have total length six, and the selected endpoint `q`
is disjoint from all of them.  Apply Denley and Wu's generalisation of
Dirac's theorem with `s=6`, `t=1`, and connectivity `s+t=7`.  This gives
(2.1).

Now suppose that `F=M_0\cup\{rs,rt\}`.  Put

\[
                  G'=(G-r)+st,
       \qquad     L'=M_0\cup\{st,e\},                 \tag{2.3}
\]

where `st` is an artificial edge.  The graph `G-r`, and hence `G'`, is
six-connected.  The set `L'` consists of six independent edges.  The same
theorem of Kawarabayashi, now with even parameter six, gives one or two
vertex-disjoint cycles of `G'` covering `L'`.  Replace the occurrence of
the artificial edge `st` by the path `s-r-t`.  This produces one or two
vertex-disjoint cycles of `G` covering `F\cup\{e\}`.  Notice also that

\[
               G'-L'=X-r-e
\]

is connected, although evenness already suffices for the cited theorem.

Finally, `M_0\cup\{rs,e\}` and `M_0\cup\{rt,e\}` are each sets of six
independent edges.  Haggkvist and Thomassen's theorem puts either set on
one cycle of the seven-connected graph `G`. `\square`

The first outcome in Theorem 2.1 is the required portal-edge cycle.  The
only new residue is therefore a pair of vertex-disjoint cycles, with the
seven prescribed edges divided between them.  This is substantially
smaller than an arbitrary linkage-compatibility problem.

## 3. What a seven-edge-cut obstruction returns

The circuit theorem of Knappe and Pitz detects odd edge cuts rather than
simple-cycle obstructions.  In the present host its exceptional outcome is
already an exact vertex separation.

### Lemma 3.1 (a seven-edge cut gives an order-seven separation)

Let `Q=delta(A)` be an edge cut of order at most seven in `G`, with
`A` and its complement nonempty.  Then `|Q|=7`, the seven edges of `Q`
have distinct ends on each shore, and the set of their ends on either
shore is the boundary of a proper order-seven separation of `G`.

#### Proof

Seven-connectivity implies seven-edge-connectivity, so `|Q|=7`.  Let
`S_A` be the set of ends of `Q` in `A`.  If `A=S_A`, put `m=|A|<=7`.
Every vertex of `A` has at most `m-1` neighbours in `A`, so minimum degree
eight gives

\[
 |Q|=\sum_{x\in A}d_{G-A}(x)
       \mathrel{\geq}m(9-m)>7,
\]

for `1<=m<=7`, a contradiction.  Hence `A-S_A` is nonempty.  The same
argument on the other shore shows that its vertices not incident with
`Q` are also nonempty.

Deleting `S_A` separates `A-S_A` from the opposite shore.  Thus
seven-connectivity gives `|S_A|>=7`; as `Q` has only seven edges,
`|S_A|=7`.  The symmetric argument gives seven distinct ends on the other
shore.  The claimed proper order-seven separations follow. `\square`

Consequently Knappe and Pitz's theorem gives the following exact
alternative for any seven prescribed independent edges in this host:

* either there is a closed trail containing them all; or
* an odd cut of order seven returns a proper order-seven separation as in
  Lemma 3.1.

A closed trail is not necessarily a cycle.  Replacing it by a simple cycle
without losing prescribed edges is precisely the point at issue.

## 4. Decisive route nonclosure

The following inference is not currently justified:

\[
 \begin{gathered}
 G\text{ is seven-connected},\quad
 L\text{ consists of seven independent edges},\quad G-L\text{ connected}
 \\
 \Longrightarrow\quad
 \text{one cycle contains }L.                        \tag{4.1}
 \end{gathered}
\]

Statement (4.1) is the parameter-seven instance of the
Lovasz--Woodall conjecture.  It is not the theorem proved by
Haggkvist--Thomassen: their conclusion for seven prescribed independent
edges requires eight-connectivity.  It is not the theorem of Denley--Wu:
at connectivity seven their path-and-vertex theorem requires at least one
prescribed vertex and hence permits total prescribed path length at most
six.  Kawarabayashi proves the one-or-two-cycle conclusion used in
Theorem 2.1, not the required one-cycle conclusion.

In the induced-path case, suppressing `s-r-t` converts the desired cycle
to the analogous parameter-six threshold problem for the six independent
edges `L'` in the six-connected graph `G'`.  Thus suppression does not
remove the missing unit of connectivity.

This is a route nonclosure, not a counterexample.  The critical host,
the exact `K_7^vee` model, and the 63 colouring signatures are substantial
extra hypotheses not present in the Lovasz--Woodall conjecture.  They may
still force the desired cycle.  What Theorem 2.1 shows is that the next
proof must use one of those extra hypotheses to merge two disjoint cycles;
connectivity alone cannot presently be cited to do so.

The narrow next target is therefore:

> **Two-cycle portal composition.**  If two vertex-disjoint cycles cover
> `F union {e}`, then the exact seven-bag model and the full punctured
> signature cube give either a `K_7^-` minor, an order-seven separation
> retaining a selected coordinate and the portal edge, or a rerouting
> which merges the two cycles while preserving all seven prescribed edges.

This target is strictly smaller than simultaneous composition of seven
independently chosen paths and does not require an unsupported quantifier
exchange.

## 5. External inputs

* R. Haggkvist and C. Thomassen, *Circuits through specified edges*,
  Discrete Mathematics **41** (1982), 29--34: `k` independent edges in a
  `(k+1)`-connected graph lie on one cycle; equivalently, independent paths
  of total length `k-1` in a `k`-connected graph lie on one cycle.
* T. Denley and H. Wu, *A generalization of a theorem of Dirac*, Journal of
  Combinatorial Theory, Series B **82** (2001), 322--326: independent paths
  of total length `s` and `t>=1` further prescribed vertices lie on one
  cycle in an `(s+t)`-connected graph.
* K. Kawarabayashi, *One or two disjoint circuits cover independent edges:
  Lovasz--Woodall conjecture*, Journal of Combinatorial Theory, Series B
  **84** (2002), 1--44: under the Lovasz--Woodall hypotheses the prescribed
  independent edges are covered by one or two vertex-disjoint cycles.
* P. Knappe and M. Pitz, *Circuits through prescribed edges*, Journal of
  Graph Theory **94** (2020), 3--17: a connected graph has a closed trail
  through prescribed edges exactly when it has no odd cut of at most their
  number.
