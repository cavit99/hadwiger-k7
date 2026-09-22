# An oriented consequence of the two-triangle construction

**Status:** working deduction; not separately audited. This strengthens
root placement in the [structural two-triangle proof](../results/hc7_two_triangle_case_closure.md). It does not close
the split-clique degree-seven case or HC7.

The [current four-root construction](hc7_split_clique_rooted_construction_working.md)
works directly in the original host without the oriented strengthening
below. The [maximal-partition exchanges](hc7_split_clique_exchange_working.md)
develop this conditional route; the
[three-colour counterexample](../barriers/hc7_split_clique_three_colour_rooted_minor.md)
records a failed colouring shortcut. None closes the case.

## Oriented structural conclusion

Let J be five-connected, contain an ordinary K5 minor and two disjoint
anticomplete literal triangles P,Q. Suppose every nonempty root-free
set X, disjoint from P union Q, has at least six neighbours in J.
Fix either triangle, say Q.

Then either J-z is planar for some z outside P union Q, or J-Q has a
partition A,B into two nonempty connected sets, each adjacent to all
three vertices of Q and each containing a vertex of P. The two parts
are adjacent, since J-Q is connected.

This is obtained by strengthening the conclusion of the existing
structural proof, not by applying its stated T-meeting conclusion.
Here is the exact change in its contradiction hypothesis and why the
argument still has its inputs.

Assume no such partition exists. The proof of the extremal prism
normalisation, with Q as the singleton triangle, uses this assumption
only to prohibit a pair of Q-full helpers splitting P. Its initial
triangle-retaining minor exists from the ordinary K5 minor. Every
shadow transfer and maximality comparison through the four numbered
structural conclusions keeps Q singleton. Hence it still constructs
the same exact induced prism and connected remainder E. No subsequent
locality statement or simultaneous-exchange corollary is needed here.

For each rail R_i, a K4 model in J-V(R_i) rooted at the other four cap
vertices would extend by the fifth bag R_i to a K5 in which each of P
and Q occupies three distinct bags. Regard the Q-containing bags as
root bags. The other two bags contain distinct P vertices. The
singleton-triangle normalisation only enlarges those two helpers, so
it keeps these P vertices throughout and yields exactly the forbidden
partition. Therefore all three rooted K4 obstructions, and thus all
three ordered web descriptions, remain available.

In the path-cell, cutvertex and two-connected-cell proofs, the absence
of a T-meeting K5 is subsequently used only through these rooted K4
obstructions, including opposite-corner paths on the two-rail cycle.
The actual small-boundary arguments, cell projections and disk edge
counts retain their hypotheses. If J-z is nonplanar for every root-free
z, they give the same contradiction. This proves the stated oriented
conclusion, subject to independent verification of this premise change.

## Shared host for the K3 disjoint union K4 case

Let G be seven-connected, seven-chromatic and K7-minor-free, with every
proper minor six-colourable. Let u have exactly seven neighbours,
forming an anticomplete triangle P and clique D of order four. Put

    C=G-N[u],       M=G-({u} union D)=G[P union C].

For every r in D, apply the oriented conclusion to

    J_r=G-{u,r},       Q=D-{r}.

The graph J_r is five-connected. It has chromatic number at least five:
a four-colouring plus two fresh colours for u,r would colour G with six
colours. HC5 therefore gives an ordinary K5 minor. Its root-free
six-neighbour condition follows from seven-connectivity, since u has no
neighbour outside P union D. The planar alternative is impossible:
four-colour J_r-z, give the nonadjacent pair u,z colour five and r colour
six.

Consequently, for every r in D, the SAME graph M has a connected
partition

    M=A_r disjoint union B_r,

with both parts meeting P and each adjacent to all three vertices of
D-{r}. If both also had r-neighbours, the seven bags

    {u},   ({d}:d in D),   A_r, B_r

would be a K7 model: D is a clique, each helper meets P and therefore
sees u, and A_r,B_r are adjacent. Since d_G(r)>=7, r has at least three
neighbours in C, so it sees at least one part. Orient the partition so

    N_C(r) subseteq B_r,       N_G(r) intersection A_r is empty.

Then A_r is full to D-{r}, while B_r is full to all of D.

Thus these are four whole spanning K7-minus-an-edge models in a single
actual host, with deficient pairs r,A_r. They are not
merely four independently rooted K5 models with unspecified ownership.

The common graph M is three-connected. If deleting at most two vertices
separated it, the surviving vertices of the literal triangle P lie in
one component. Any other component X lies in C; its G-boundary is
contained in those at most two deleted vertices together with D, because
u has no neighbour in C. This is a cut of order at most six, impossible.
Moreover every P vertex has degree at least six in M, every d in D has
at least three M-neighbours, and each nonempty X subseteq C satisfies

    |N_M(X)| + |N_D(X)| >= 7.

## The joint construction and its remaining contact loss

With the preceding orientation, every `B_r` is adjacent to all four
vertices of `D`, whereas `A_r` misses only `r`. Choose distinct `r,s`
for which `B_r intersection B_s` contains a vertex of `P`; such a pair
exists because four nonempty subsets of the three-element set `P`
cannot be pairwise disjoint.

The union `A_r union A_s` is connected, since both parts meet the
literal clique `P`, and is adjacent to all four vertices of `D`.
Let `K` be the component of `M-(A_r union A_s)` containing the surviving
`P` vertices. They lie in one component because `P` is a clique.
Absorb all other components into `A_r union A_s`: each has a neighbour
in that connected union. This gives two connected, P-meeting parts of M.
If K is adjacent to all D, these parts finish the K7 model.

The entire intersection `B_r intersection B_s` does contact both r and
s: all r-neighbours lie in B_r, and B_s has an r-neighbour; symmetrically
for s. Those contacts need not lie in K. The other two D vertices may
have no neighbour anywhere in the intersection.

This is the first unresolved inference. Neither intersection
connectivity nor retention of its four required contacts is proved.
The choices of r,s and of all four partitions remain free, as do the
proper-minor colourings of the original host. No recursive decrease or
colouring lift is asserted. A proposed common spanning-tree realisation
of the four partitions would need its own proof; treating their cuts
as compatible tree cuts would merely assume the missing compatibility.
