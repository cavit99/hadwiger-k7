# Independent internal audit: weighted-splitter small-atom reduction

**Verdict: GREEN.**  The exact theorem revision identified below is a valid
unbounded reduction.  It proves the exact obstruction to a safe
three-contractible edge, a spanning tree of three-contractible edges in the
absence of the four-label triangle terminal, and a reduction of any complete
system of tight blockers to a connected atom of order at most three with the
stated local and transverse structure.

This is a separate internal mathematical audit, not external peer review.

**Audited source:**
[`hc7_k44_weighted_splitter_small_atom_reduction.md`](hc7_k44_weighted_splitter_small_atom_reduction.md)

**Source SHA-256:**
`bc4f7d38d94beed2d86b9858a2290fd1cb85af398653b5b16a5d3231f80eb2db`

## 1. Audit method

The audit was performed as a hostile line-by-line reconstruction rather than
as a strategic review.  In particular, it:

1. checked every quotient set in the safe-contraction lemma, separating sets
   containing the contracted vertex from sets avoiding it and retaining the
   co-spanning blocker case;
2. independently derived the submodularity, component, Hall-deficiency, and
   local resource inequalities;
3. checked the graphic translation of Costalonga's matroid theorem, including
   circuit--cocircuit parity, the structure of a graphic triad, and the passage
   from vertical contraction to simplification of a graph contraction;
4. reconstructed the ballast augmentation `J`, verified
   `kappa(J)=7`, and matched every hypothesis of Mader's generalized atom
   lemma for an arbitrary connected blocker of every relevant tree edge;
5. audited all resource-set intersections and boundary counts in Corollary
   4.2, including the co-minimum three-vertex blocker argument; and
6. built the bags in every case of Corollary 4.3 and checked disjointness,
   connectivity, weights, pairwise contacts, and spanning coverage.

No finite census, solver result, or bounded-order inference is used in this
verdict.  The result is a written unbounded theorem.

## 2. Exact contraction and tight-set algebra

Lemma 2.1 is exact.  If a quotient set contains the contracted vertex, its
preimage has the same vertex boundary and label union.  If it avoids the
contracted vertex, its boundary loses one vertex exactly when both ends of the
contracted edge lie in the old boundary.  Since every old value is at least
seven, failure occurs exactly at an old tight set.  This includes a set such
as `V(C)-{u,v}` with a two-vertex boundary; no unjustified lower bound on the
boundary order is used.

Lemma 2.2 correctly lifts all three terminal configurations.  If the
contracted vertex is unused in either nonspanning model, the bags remain
unchanged.  Otherwise the unique bag containing it is replaced by the full
preimage containing the contracted edge.  Connectivity, label weight,
disjointness, quotient contacts, and the spanning condition in the four-bag
case are all preserved.

Lemma 3.1 is valid: closed-neighbourhood cardinality and label-union
cardinality are coverage functions, subtraction of `|X|` is modular, and a
component of a tight set has a resource boundary contained in a seven-resource
boundary while itself having at least seven resources.  The two resource sets
are therefore equal.  Consequently every blocker may be replaced by any of
its connected components without changing its boundary.

Lemma 3.2 correctly uses the deficiency form of Hall's theorem.  For
`X=V(C)-P(U)`, all graph-boundary vertices lie in `P(U)` and `X` uses no label
of `U`; the empty-`X` case is handled separately.  The maximum deficiency is
at most `m-7`, so seven distinct label--vertex incidences exist.

## 3. Contractible tree and generalized atom

The proof of Lemma 3.3 correctly excludes adjacent degree-three vertices: the
two singleton bags have weight at least four, the connected complement has
weight at least five, and the three bags are pairwise adjacent.  In the cycle
matroid, binary circuit--cocircuit parity makes a nonempty triangle--triad
intersection have order two.  The corresponding three-edge bond can meet a
graph triangle only in the star of a degree-three triangle vertex; otherwise
one obtains a cut vertex, a two-vertex separator, or a vertex of degree at
most two.  Hence each matroid triangle meets at most one triad.  Costalonga's
Theorem 1.5 then supplies a spanning set of vertically contractible elements;
a basis inside it is a graph spanning tree, and every one of its edges is
three-contractible after graph simplification.

For Theorem 4.1, the augmented graph `J` is seven-connected.  Deleting at most
six vertices cannot separate a `C`-side component from the surviving ballast
clique without deleting all of its at least seven boundary resources.  A
tight blocker gives a seven-vertex separator in the other direction, so the
connectivity is exactly seven.

The ballast also handles co-spanning blockers correctly.  A blocker in `C`
has order at most `|V(C)|-2`, whereas a fragment meeting the ballast clique
contains at least `|V(C)|+1` clique vertices outside its seven-vertex
boundary.  Thus a minimum `\mathcal S`-fragment lies wholly in `C`.  Its
components have the same boundary, so minimum order makes the selected atom
connected.

For every tree edge `ab` incident with the atom and every connected tight
blocker `X`, the set `T=partial X` is a minimum separator containing `a,b`.
With `a in A` and `b in A union N_J(A)`, all hypotheses of Mader's generalized
atom lemma hold.  It gives

\[
 A\subseteq T,
 \qquad
 |A|\le \frac12|T-N_J(A)|.
\]

This proves universally, not merely for one selected blocker, that
`|A|<=3`, `A subseteq N_C(X)`, and
`|partial A intersect partial X|<=7-2|A|`.  For a crossing tree edge, its
outside endpoint belongs to the intersection; at order three the intersection
is exactly that one vertex resource.

The boundary of the atom contains the fixed tree edge `xy`.  If that boundary
had order at most three, contracting `xy` would leave a separator of order at
most two between the nonempty atom and a nonempty exterior remainder.  Hence
the boundary has order at least four and the atom uses at most three labels.
The local inequality (8) is direct resource accounting.  Its sharpened form
is valid because equality for a proper set seeing `x,y` would produce a
smaller tight set whose boundary contains the same fixed edge of the tree,
contrary to the precise minimality used in the theorem.

## 4. Three-vertex transverse pair

Corollary 4.2 is GREEN.  For a crossing edge `ab` and connected blocker `X`,
the one-resource intersection gives

\[
 A\cap X=\varnothing,
 \quad A\subseteq N_C(X),
 \quad L(A)\cap L(X)=\varnothing,
 \quad N_C(X)\cap B=\{b\}.
\]

Every neighbour in `X` of an atom vertex lies in `P=X cap B`, so `P`
collectively dominates `A`; the remaining boundary vertices `B_0` are
anticomplete to `X`.  The four vertex resources `A union {b}` leave exactly
three resources in `partial X`.  With

\[
 D=N_C(X)-(A\cup\{b\}),
\]

the vertex and label parts give `|D|+w(X)=3`, while

\[
 N_C(A\cup X)=(B-P)\mathbin{\dot\cup}D.
\]

Together with the disjoint label unions, this yields exactly

\[
 \lambda(A\cup X)=10-|P|.
\]

The global boundary inequality therefore gives `|P|<=3`, and domination
gives `|P|>=1`.  Since `X` is itself a tight set whose boundary contains the
tree edge `ab`, atom minimality gives `|X|>=3`.

When `|X|=3`, it is another minimum atom for the same tree.  Applying (8) to
its two-vertex subsets proves `|P|>=2`.  If `|P|=2`, each member of `P` is
adjacent to both vertices of `A-{a}`; if `C[X]` is a path, the unique vertex
outside `P` cannot be an endpoint, so the two members of `P` are exactly the
path endpoints.  Finally, `X` is adjacent to all three atom vertices, giving
exactly a four-bag `K_4` model when `C[A]` is a triangle and a `K_4^-` model
when `C[A]` is a path.  No weight condition is silently attached to this
last unweighted quotient statement.

## 5. Components outside a three-vertex atom

Corollary 4.3 is GREEN.  Every component `H` of `C-A` has boundary exactly
`A`; a smaller boundary would be a separator of order at most two.  Thus
`w(H)>=4`.  Three such components, paired with the three atom vertices,
give three pairwise adjacent connected bags of weight at least four, so
terminal-freeness forces at most two components.

If `C[A]` is a triangle, one component can be reserved as the fourth bag and
one different component attached to each atom vertex of weight below three.
The triangle edges and the fact that every component has boundary `A` make
the four bags pairwise adjacent.  Leftover components attach to an atom bag,
so the model spans.  Therefore the number `m` of components satisfies
`m<=d`.

If `C[A]=u-v-w`, inequality (8) and its sharpened form make both endpoints
carry every label in `Q`.  Reserving a component `H_0`, attaching a second
component `H_1` to `u`, and using an edge from `H_1` to `w` supplies the
missing endpoint contact.  A further component is needed for `w` exactly
when `|Q|<3`, and one for `v` exactly when `w({v})<3`.  The four bags are
connected, pairwise adjacent, of weight at least three, and can absorb all
leftover components.  Hence a spanning three-label `K_4` model exists at the
threshold stated in the source, and its absence gives exactly (17).

## 6. Repairs checked before hash pinning

The hostile audit identified and checked the following repairs before the
source hash above was frozen:

- the graphic triangle--triad and vertical-contraction translations were
  made explicit;
- the Mader application was quantified over an arbitrary connected blocker;
- the sharpened local inequality was tied to minimum order relative to the
  fixed spanning-tree edge;
- terminal lifting was split into the used and unused contracted-vertex
  cases for nonspanning models; and
- a proposed `K_7` sharpness illustration was removed because its selected
  three-set was not a minimum atom for any spanning tree.

The final audited revision contains these repairs.  The removed illustration
is not used by any theorem or corollary.

## 7. External inputs and trust boundary

Two non-elementary external results are accepted at their published stated
strengths rather than reproved here.

- J. P. Costalonga, *A splitter theorem on 3-connected binary matroids and
  inner fans*, Journal of Combinatorial Theory, Series B **173** (2025),
  204--245, Theorem 1.5.  The audit checked that the theorem's rank and
  triangle--triad hypotheses match `M(C)` and independently checked the full
  graphic translation used in Lemma 3.3.
- W. Mader, *Generalizations of critical connectivity of graphs*, Discrete
  Mathematics **72** (1988), 267--283, in the exact formulation reproduced as
  Lemma 5.1 of M. Kriesell, *Minimal Connectivity*, arXiv:`1101.2357`.  The
  audit checked every `\mathcal S`-atom and separator hypothesis in the
  application, including co-spanning blockers and the universal blocker
  quantifier.

Hall's theorem and the standard graphic connectivity equivalence for cycle
matroids are used only in the elementary forms reconstructed above.

## 8. Exact unresolved scope

The following **small transverse-atom completion lemma remains open**:
in a labelled three-connected graph satisfying (2) and avoiding all three
terminal configurations, exclude each of the four atom shapes together with
the companion blockers (9) for the fixed spanning tree, including the exact
three-vertex transverse structure (13)--(16) and component restrictions
(17).

This is still an unbounded problem.  The atom has at most three vertices, but
its boundary and companion blocker lie in an exterior of arbitrary order.
In the three-vertex case, the missing step is a rooted positive-weight
partition inside the one or two remaining components, not another finite
boundary count.

Accordingly, the audited theorem does **not** prove the weighted splitter
theorem, the literal `K_{4,4}` case of T44, T44, Norin--Totschnig Conjecture
21, or `HC_7`.
