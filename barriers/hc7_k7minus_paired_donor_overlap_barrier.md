# Boundary overlap does not synchronize two donor traces

**Status:** explicit finite counterexample to the local paired-donor
principle stated below; deterministic verifier included.  This is not a
counterexample to the `K_7^-` six-colour conjecture.  It is only
three-connected, four-chromatic, and does not contain the five-centre
near-clique data.

The construction tests the strongest part of the proposed two-donor
minimisation which can be stated without the full critical host.  It has
two donors in distinct named bags, one common deleted edge, one fixed
six-colouring, substantial boundary overlap, the forced cross-incidence in
both directions, and five protected contacts on each smaller donor.  Both
donors nevertheless admit trace-losing boundary inflation, while their
joint trace remains rejected and the graph has no `K_7^-` minor.

## 1. The false local principle

The following implication is false.

> Let `Y_1,Y_2` be disjoint geometric donors in distinct connected bags,
> joined by an edge `e`.  Suppose one proper six-colouring of `G-e`
> induces a rejected order-seven trace at both donors.  Suppose further
> that each donor has a proper co-connected subdonor with larger boundary,
> retaining five prescribed contacts but no longer rejecting the trace;
> that the two old boundaries overlap; and that `e` supplies cross-incidence
> in both directions.  Then either `G` contains a `K_7^-` minor or the
> fixed joint boundary trace extends through `Y_1 union Y_2`.

The construction below satisfies every premise and neither conclusion.
Thus boundary overlap, even together with a single literal operation and
substantial protected contact data, is not the missing synchronization
mechanism.

## 2. Construction

For `i in {1,2}`, put

\[
 U_i=\{a_i,b_i,c_i,r_i,w_i\},\qquad
 Y_i=\{a_i,b_i,c_i,r_i\}.
\]

Make each `Y_i` a `K_4`, add the edges

\[
 r_iw_i,\quad c_iw_i,\quad
 a_it_j\ (1\le j\le5),\quad
 r_it_j\ (2\le j\le5),
\tag{2.1}
\]

and add

\[
 e=a_1a_2,\qquad fw_1,fw_2,ft_1.                 \tag{2.2}
\]

There are no other edges.  Colour the vertices of `G-e` by

\[
\begin{array}{c|c}
0&a_1,a_2,f\\
1&r_1,r_2,t_1\\
2&b_1,b_2,t_2\\
3&c_1,c_2,t_3\\
4&w_1,w_2,t_4\\
5&t_5.
\end{array}                                             \tag{2.3}
\]

Every edge except `e` is properly coloured, and the ends of `e` have the
same colour.

## 3. The two individual traces

For `{i,j}={1,2}`, direct inspection gives

\[
 T_i=N_G(Y_i)=\{a_j,t_1,t_2,t_3,t_4,t_5,w_i\}.          \tag{3.1}
\]

Thus `|T_i|=7`.  The set `U_i-Y_i={w_i}` is connected, and the vertex
`f` is anticomplete to `Y_i`; hence `T_i` is an actual separator.  The
colouring (2.3) is proper on `G-Y_i`, so its partition of `T_i` is a legal
exterior trace.

The boundary neighbours of `a_i` use all six colours: `a_j` has colour
zero and `t_1,...,t_5` have colours one through five.  Consequently the
list

\[
 [6]-c(N(a_i)\cap T_i)
\]

is empty.  The singleton `{a_i}` is therefore a fixed-trace rejection
core, and the trace cannot extend through the closed donor side.

Now take the smaller co-connected donor `Y_i'={r_i}`.  Its boundary is

\[
 N_G(r_i)=\{a_i,b_i,c_i,w_i,t_2,t_3,t_4,t_5\},          \tag{3.2}
\]

of order eight.  The complement `U_i-r_i` is connected.  The smaller
donor is still anticomplete to `f`, so (3.2) is also an actual separator.
It retains the five literal contacts

\[
                         w_i,t_2,t_3,t_4,t_5.           \tag{3.3}
\]

The colours on (3.2) are exactly `0,2,3,4,5`, so colour one remains
available at `r_i`.  Thus the smaller donor accepts the fixed trace.  Both
donors have simultaneously undergone the boundary-inflating,
trace-losing replacement which the paired minimisation was intended to
prevent.

The overlap and cross-incidence are literal:

\[
\begin{aligned}
 T_1\cap T_2&=\{t_1,t_2,t_3,t_4,t_5\},\\
 T_1\cap Y_2&=\{a_2\},\\
 T_2\cap Y_1&=\{a_1\}.
\end{aligned}                                           \tag{3.4}
\]

## 4. The joint trace still fails

The donors are joined by `e`, and

\[
 N_G(Y_1\cup Y_2)=\{t_1,t_2,t_3,t_4,t_5,w_1,w_2\}.     \tag{4.1}
\]

Relative to this fixed boundary, each of `a_1,a_2` has the singleton list
`{0}`.  Since `a_1a_2` is an edge, the two-vertex graph on those endpoints
is a minimal non-list-colourable joint core.  Hence the common exterior
trace does not extend through `Y_1 union Y_2`.

This also illustrates why the fixed boundary must not be silently changed
after extracting the joint core.  With the lists fixed at (4.1), every
minimal joint core contains both ends of `e`; after relocalising to the
neighbourhood of a smaller set, an omitted endpoint can become a new
boundary vertex and the conclusion is lost.

## 5. Target exclusion

The verifier contains an explicit tree decomposition of width four.  Its
central bag is

\[
                         \{a_1,a_2,f,r_1,r_2\},
\]

with the four `t_2,...,t_5` bags, the `t_1` bag, and the two short bag
chains through `w_i,c_i,b_i` attached to it.  Every decomposition bag has
order at most five.

Treewidth is minor-monotone, while `K_7^-` contains a `K_6` subgraph and
therefore has treewidth at least five.  Thus

\[
                         K_7^-\npreccurlyeq G.           \tag{5.1}
\]

The graph is exactly three-connected and four-chromatic.  The latter
follows from either displayed `K_4` and the explicit four-colouring checked
by the verifier.

Run

```text
python3 barriers/hc7_k7minus_paired_donor_overlap_barrier_verify.py
```

The script checks the graph, both fixed traces, both inflated donors, all
protected contacts, the joint core, exact connectivity, an explicit
four-colouring, and the width-four tree decomposition.

## 6. Exact scope

The example does **not** satisfy the hypotheses of the hypothetical
critical host:

- it has connectivity and minimum degree three;
- it is four-colourable and is not contraction-critical;
- it has no five degree-eight centres or original equal/distinct pole
  response; and
- the five protected contacts in (3.3) are not certified owner/helper
  branch-set duties in the unique-owner model.

Accordingly it does not refute a cross-edge paired-donor **supply theorem**
which spends all of that global data.  It refutes the broad local inference
that overlap and a shared operation turn boundary inflation into
synchronization.  Any further paired theorem must use the full
relative-seven and labelled near-clique hypotheses at the step where the
two donor pieces are supplied; adding a weighted boundary-overlap potential
cannot suffice.
