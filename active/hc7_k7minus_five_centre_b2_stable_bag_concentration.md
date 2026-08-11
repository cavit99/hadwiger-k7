# Stable-bag concentration in the all-rainbow `b=2` row

**Status:** written proof; separate internal audit GREEN at the revision
recorded in the adjacent audit.
This note combines the shore-confined rooted `K_5` with the retained-root
four-root witness.  It proves that, in a target-free `b=2` configuration,
all contacts of the four retained centres are concentrated in the two pole
bags and at most one triangle-root bag.  Together with the private-contact
theorems, this leaves two triangle-root bags adjacent to exactly one centre
and places at least six distinct retained-centre-private contacts in the
other three bags.  The concentration conclusion is unbounded, but it does
not by itself split one of those three bags and hence does not close the
branch.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Use the all-rainbow `b=2` outcome of the separately audited
[global five-root palette theorem](hc7_k7minus_five_centre_t5_global_palette.md).
Thus

\[
 S=Z\mathbin{\dot\cup}\{p,q\},
 \qquad
 Z=\{z_p,z_q,y_1,y_2,y_3\},
\tag{1.1}
\]

where `z_p` is adjacent only to `p` among the poles, `z_q` is adjacent
only to `q`, and the three vertices `y_1,y_2,y_3` are pole-free.  The
components `C,D` of `G-S` are connected and full to `S`.

Fix a pole-free centre `z`, put `A=Z-\{z\}`, and write

\[
                         T_z=N_D(z)=\{t_1,t_2,t_3\}.
\tag{1.2}
\]

The separately audited rainbow-triangle theorem gives a rooted `K_5`
minor in `G[D\cup\{p,q\}]`, with connected pairwise disjoint bags

\[
                         P,Q,B_1,B_2,B_3,
\tag{1.3}
\]

where `p in P`, `q in Q`, and `t_i in B_i`.

## 2. A spanning rooted model

### Lemma 2.1 (spanning extension)

The model in (1.3) may be chosen so that its five bags partition
`D\cup\{p,q\}`.

#### Proof

Start with any rooted model (1.3).  If a component `R` of the vertices not
yet covered by its bags remains, connectedness of
`G[D\cup\{p,q\}]` gives an edge from `R` to some bag.  Add all of `R` to
that bag.  Connectivity, disjointness, every old bag adjacency, and all
five prescribed roots are preserved.  Repeating this operation gives a
spanning rooted model. \(\square\)

## 3. The concentration theorem

Choose a `p`--`q` path witnessing feasibility of the `C`-rooted instance
on `A`, and let `K` be the component after deleting the path which contains
all four vertices of `A`.  Define the connected set `X` exactly as in the
separately audited
[two-private-contact theorem](hc7_k7minus_five_centre_two_private_contacts.md):
it consists of `z`, the open part of the witness path, and every other
path-complement component met by `z`.  That theorem proves that

\[
 X\cap K=\varnothing,
 \qquad X,K\text{ are connected and adjacent}.       \tag{3.1}
\]

Both sets are disjoint from all five bags in (1.3).  Moreover, `X` is
adjacent to every one of those bags: the path ends give its adjacencies to
`P,Q`, and the three edges `zt_i` give its adjacencies to `B_i`.

### Theorem 3.1 (stable-bag concentration)

Suppose `G` has no `K_7^-` minor.  In every spanning rooted model
(1.3), the set

\[
                         N_D(A)=\bigcup_{a\in A}N_D(a)
\tag{3.2}
\]

meets at most one of `B_1,B_2,B_3`.  Consequently, after relabelling,

\[
                         N_D(A)\subseteq P\cup Q\cup B_1,
\tag{3.3}
\]

and

\[
                         E_G(A,B_2)=E_G(A,B_3)=\varnothing.
\tag{3.4}
\]

#### Proof

The component `K` contains both pole-incident centres `z_p,z_q`, because
the omitted centre `z` is pole-free.  Hence the edges `z_pp,z_qq` make
`K` adjacent to `P,Q`, respectively.

If `N_D(A)` met two distinct stable bags, say `B_i,B_j`, then the centre
edges witnessing those intersections would make `K` adjacent to both
bags.  Thus, among the five model bags, `K` would be adjacent to `P,Q`
and at least two stable bags.  The seven disjoint connected sets

\[
                         X,K,P,Q,B_1,B_2,B_3
\tag{3.5}
\]

would be pairwise adjacent except possibly for the pair consisting of
`K` and the remaining stable bag: the five model bags form a clique,
`X` is adjacent to all of them and to `K`, and `K` has the four displayed
model-bag adjacencies.  They would form a `K_7^-` minor, a contradiction.

The spanning property puts every vertex of `N_D(A)` in one of the five
bags.  The first conclusion therefore gives (3.3) after relabelling, and
(3.4) is the same assertion written as centre--bag nonadjacency. \(\square\)

### Corollary 3.2 (two centre-clean stable bags)

The bags `B_2,B_3` in (3.3) satisfy

\[
                         N_Z(B_i)=\{z\}
                  \quad (i=2,3),                     \tag{3.6}
\]

and their roots `t_2,t_3` are private to `z` among the five centres.
Moreover,

\[
                         |N_{G[D\cup\{p,q\}]}(B_i)|\ge6
                  \quad (i=2,3).                     \tag{3.7}
\]

#### Proof

Equation (3.4) says that no retained centre meets either bag.  The centre
`z` meets `B_i` through `t_i`.  Since its only `D`-neighbours are the
three roots `t_1,t_2,t_3`, which lie in distinct bags, this proves (3.6),
and in particular makes `t_2,t_3` private.

The nonempty opposite component `C` lies outside
`B_i\cup N_G(B_i)`, so `N_G(B_i)` is a separator.  Seven-connectivity and
(3.6) give

\[
 7\le |N_G(B_i)|
   =1+|N_{G[D\cup\{p,q\}]}(B_i)|,
\]

which is (3.7). \(\square\)

## 4. The private-contact census inside three bags

### Corollary 4.1 (six retained private contacts in three bags)

In the notation of Theorem 3.1, the union `P\cup Q\cup B_1` contains at
least six pairwise distinct vertices which are private contacts of centres
in `A`.

#### Proof

Besides `z`, there are two pole-free centres in `A`.  The separately
audited two-private-contact theorem gives at least two private contacts for
each of them.  The two pole-incident centres `z_p,z_q` each have at least
one private contact by the separately audited rainbow-triangle theorem.
Contacts private to different centres are necessarily distinct.  This
gives at least six distinct vertices of `N_D(A)`, all of which lie in
`P\cup Q\cup B_1` by (3.3). \(\square\)

Together with the two private roots in Corollary 3.2, the five contact
triangles therefore contain at least eight pairwise distinct private
vertices.  More importantly for a terminal model, the obstruction is now
localized: two stable bags have no retained-centre edge at all, while all
six retained private vertices have been concentrated in the other three
bags.

## 5. Exact remaining split

Theorem 3.1 makes the two-reservation question exact.  If a rooted model
can be chosen so that contacts of the retained centres reach two stable
bags, (3.5) is already the forbidden minor.  Otherwise every spanning
rooted model has the concentration (3.3), two centre-clean stable bags
with the six internal boundary contacts in (3.7), and six private contact
vertices in the other three bags.

A terminal continuation must split or reroot one of `P,Q,B_1` so that it
retains a contact with `K` while transferring another retained-centre
contact to `B_2` or `B_3`.  Connectivity of a bag alone does not justify
that split: the required model adjacencies may all be supported beyond one
cutvertex of the bag.  No such splitting theorem is asserted here.

## Dependencies and claim status

- the two full shores, all-rainbow profiles, and `b=2` incidence come from
  the separately audited global five-root palette theorem;
- the rooted `K_5` model comes from the separately audited rainbow-triangle
  theorem; and
- the connected witness sets `X,K` and the private-contact counts come
  from the separately audited two-private-contact theorem and
  rainbow-triangle theorem.

The spanning extension, concentration theorem, and displayed consequences
are proved here.  The final bag split is an explicit open step, not an
asserted conclusion.
