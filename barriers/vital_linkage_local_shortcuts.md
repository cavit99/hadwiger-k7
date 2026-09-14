# Limits of local steps in the three-path construction

**Status:** explicit counterexamples with written verification and a
[separate internal audit](vital_linkage_local_shortcuts_audit.md).
These examples do not refute the global maximal-component
construction, Conjecture 19, or HC7. The current construction is in the
[prism draft](../active/hc7_two_triangle_prism_construction.md).

An A--B linkage consists of three vertex-disjoint paths using all vertices
of the disjoint triples A and B as their six ends. Pairings are free;
no terminal occurs internally. A vertex is vital if every such linkage
uses it. A separator may contain terminals and separates the surviving
sets `A-S` and `B-S`.

## 1. All-vitality does not supply a rootless minimum separator

**Assertion refuted.** If A and B are triangles, H has no A--B edge,
and every vertex of H is vital, H has an A--B separator of order three
disjoint from `A union B`.

Take triangles `A={a1,a2,a3}`, `B={b1,b2,b3}`, four further vertices
`s,w,u,t`, the three paths

```text
a1-s-b1,       a2-w-u-b2,       a3-t-b3,
```

and the additional edges `a1-u` and `w-b3`. These are all the edges.
There is no A--B edge. The displayed paths give a linkage.
Every linkage must use s and u, which are respectively the only
non-B neighbours of b1 and b2. Similarly w and t are the only non-A
neighbours of a2 and a3. Thus every vertex is vital.

The four two-edge paths

```text
a1-s-b1,       a1-u-b2,       a2-w-b3,       a3-t-b3
```

force a rootless separator to contain all four internal vertices.
Deleting those four vertices does separate A from B, so the minimum
rootless separator order is exactly four. In contrast, `{a1,w,t}` is a
separator of order three. Three disjoint paths rule out a smaller one.

**First unsupported inference and scope.** A chain of minimum cuts can
process the rails at different times; it need not contain a rootless cut.
This does not refute a separator-or-terminal-model alternative. Indeed,
all H-degrees here are at most four. If this H occurred as `G-v-C` in
the actual minimum-degree-eight host, every H vertex would have a
C-neighbour: its other neighbours contribute at most five to its degree.
The displayed rails would then satisfy the terminal contact condition.
This example makes no claim about the variant allowing one A--B edge
and asking for a cut with at most one terminal.

## 2. Ordered fans can have no splitting cell and no small separator

**Assertion refuted.** Suppose G is seven-connected, seven-chromatic,
has minimum degree eight, and has a degree-eight vertex v whose
neighbourhood induces two triangles A,B and an edge xy. Let C be a
connected complementary component containing x,y, and let `H=G-v-C`
be all-vital. Even after maximising the number of C-contacted rails over
all H-linkages, absence of a splitting inversion cell forces
a vertex cut of order at most six.

This assertion deliberately omits global maximality of C and proper-minor
criticality. Those omissions are essential to the example below.

### Construction

Let H contain the three paths

```text
P1 = r0-r1-r2,
P2 = s0-s1-s2,
P3 = t0-t1-...-t17.
```

For `i=0,1,2`, join both ri and si to all six vertices of
`Ti={t_(6i),...,t_(6i+5)}`. Add `r0-s0` and `r2-s2`.
Thus `A={r0,s0,t0}` and `B={r2,s2,t17}` are triangles, with no A--B edge.

Add `C={c0,...,c5}` inducing `K6-c4c5`, and put `x=c0`, `y=c1`.
Join every C vertex to every tj, except for the four omitted edges
`x-t0`, `x-t17`, `y-t0`, `y-t17`. Finally add v adjacent exactly to
`A union B union {x,y}`. There are no other edges.
The orders are `|H|=24`, `|G-v|=30`, `|G|=31`.

### Verification of the numerical and neighbourhood hypotheses

The neighbourhood of v induces exactly `2K3 + K2`, so contains no four-cycle.
The four zero-rail endpoints have G-degree nine; r1,s1 have degree eight.
Each internal tj has degree ten; t0,t17 have degree eight. Every C vertex
has degree at least twenty-two, and v has degree eight. Hence `delta(G)=8`.

For seven-connectivity, delete a set S of at most six vertices. If all of C
is deleted, then `S=C` and the remaining graph `H+v` is connected.
Otherwise, the surviving C vertices and surviving `t1,...,t16` lie in one
connected component K: every C vertex sees all sixteen of these vertices,
and at least ten survive.

If a nonport C vertex survives, every surviving tj belongs to K. A surviving
ri or si has a surviving neighbour in its six-vertex block unless that
entire block is S. In that exceptional case all zero-rail vertices survive,
and a neighbour along its zero rail reaches an undeleted adjacent block.
Thus every surviving zero-rail vertex also lies in K.

If only ports survive in C, the four nonports have already been deleted,
leaving at most two further deletions. Each block has at least five internal
tj vertices, so every surviving zero-rail vertex reaches K directly.
Each surviving endpoint t0 or t17 has three H-neighbours, respectively
`{r0,s0,t1}` and `{r2,s2,t16}`; at least one survives and lies in K.
Finally, a surviving v has a surviving neighbour, since its degree is eight;
all such neighbours have already been placed in K. Hence `G-S` is connected.

The set `{c0,c1,c2,c3,c4,t1,t2}` is a proper K7 subgraph. Conversely, give
`c0,c1,c2,c3` colours `1,2,3,4`, and give c4,c5 colour five. Alternate
colours six and seven along P3. Give `r0,r1,r2` colours `1,2,1` and
`s0,s1,s2` colours `2,1,2`; give v colour three. This is a proper colouring,
so `chi(G)=7` exactly.

### Vitality, forced rails, and absence of inversion cells

For every `tj in Ti`, the set `{ri,si,tj}` is an A--B separator of order
three. Removing it separates the earlier blocks and heavy-path prefix
from the later blocks and suffix. The three displayed disjoint paths make
each such cut minimum. Every vertex belongs to one of these cuts, so every
vertex is vital: three disjoint paths must use all three vertices of a
minimum three-cut.

In fact, the displayed linkage is forced. Exactly three edges leave the
first block together with r0,s0: `r0r1`, `s0s1`, and `t5t6`. Every linkage
must use all three. The paths using the first two start at their respective
A-roots, and therefore begin `r0-r1` and `s0-s1`. At the second block
boundary the only crossing edges are `r1r2`, `s1s2`, and `t11t12`.
Their B-root endpoints force the first two paths to end `r1-r2` and
`s1-s2`. Thus both short rails are fixed, and the remaining path is P3.

C contacts all eighteen vertices of P3 and no vertex of P1 or P2.
The maximum number of contacted rails over all H-linkages is therefore one.
If `i<k`, every heavy neighbour of ri precedes every heavy neighbour of rk;
the same holds for the s-rail. Thus there is no pair of cross-edges reversing
the two rail orders, and in particular no adjacent inversion cell that
splits the heavy contacts. The only edges between the short rails join
their corresponding ends and do not form a reversed pair either.

### The valid exchange, and what the example does not refute

C is **not** globally maximal. Replace P3 by `t0-c2-t17`, keeping P1,P2.
The new complementary component is exactly

```text
C' = (C-{c2}) union {t1,...,t16}.
```

It is connected, contains both ports, and has order twenty-one rather
than six. The exchange consumes one C vertex and releases sixteen H vertices;
no other complementary component is left behind. Every vertex of both
short rails contacts C', as does every vertex of the new third rail.
The terminal certificate therefore applies.

**First false inference and unaffected scope.** Fixed-H vitality, optimal
contact count, ordered fans and the displayed numerical hypotheses do not
force a splitting cell or a small separator. An argument must still use
global maximality of C, proper-minor criticality, or a direct terminal exit.
This graph has a proper K7 avoiding v, so `chi(G-v)=7`; it has a Q minor
and is not contraction-critical. In particular it lacks the actual host's
proper-minor six-colouring response.
It is neither a counterexample to the maximal-C state nor to a
separator-or-Q alternative or the full two-triangle target. Its successful
exchange is a construction example, not a universal exchange theorem.

## 3. A chromatic obstruction need not lie in one exterior component

**Assertion refuted.** If P is a path, J-P is bipartite and J is
four-chromatic, some component K of J-P makes J[P union K] four-chromatic.

Take `P=p0-p1-p2`, an exterior singleton x adjacent to all of P, and an
exterior edge ab with `N_P(a)={p0,p1}`, `N_P(b)={p1,p2}`. These are all
the edges. The exterior has precisely the components {x} and {a,b}.

In a three-colouring of P+x, the P vertices use the other two colours,
so p0=p2; this condition also suffices. In a three-colouring of P+a+b,
the triangles p0p1a and p1p2b force a and b to coincide if p0=p2,
contradicting ab. If p0 and p2 differ, the colouring
`(p0,p1,p2,a,b)=(1,2,3,3,1)` works. Thus each component separately
admits three colours, but their demands on P are incompatible.
The whole graph is the odd wheel with centre p1 and rim p0,x,p2,b,a;
it is four-chromatic. Equivalently, a fourth colour extends either
displayed colouring, while the incompatible demands exclude three.

**First unsupported inference and scope.** A four-chromatic graph formed
from P and two whole colour classes need not identify one exterior
component that carries the obstruction. It can combine incompatible
boundary colourings. This example does not realise the entire five-class
chromatic flag, the three-path normalisation or the actual critical host.
It refutes that localisation step alone. Preserving selected coloured
vertices also does not establish their connectivity after deleting an ear;
the remaining argument must coordinate whole component responses.
