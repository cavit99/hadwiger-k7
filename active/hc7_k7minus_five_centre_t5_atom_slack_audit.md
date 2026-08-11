# Internal audit of the order-fifteen five-root atom theorem

Audited file:
`active/hc7_k7minus_five_centre_t5_atom_slack.md`

Audited SHA-256:

```text
cef0f373ea433f72299cbc288a86274c0dae8414c8ee173c446320f01c310bab
```

**Verdict:** **GREEN.**  The coefficient-three atom identity, the proof
that every all-rainbow atom contains a `C`-vertex, the eliminations through
order eleven, and the simultaneous five-atom exclusions at orders twelve
through fourteen are correct under the stated minimally infeasible
all-rainbow hypotheses.  In particular, `|C|\ge15`.

This is a hash-pinned internal mathematical audit, not external peer review.
The theorem is an unbounded exclusion of the first seven possible shore
orders.  It does not synchronize the five witness paths at higher orders or
prove the `K_7^-` six-colour conjecture.

## 1. Scope and pinned dependencies

The audit checked the following exact local inputs.

| input | source SHA-256 | audit SHA-256 |
|---|---|---|
| five-centre two-cut reduction | `1917b5e3d183d44a2d905d2628272d10e4bc6f7ae0768b43cab0e9462b83332a` | `d01183c936d79ea2e07f956c2e89f7291df9cc28a5dab3dda6b093c8a69c4ea3` |
| global five-root palette alternative | `b26f9f0d12822f93af55e3aa566fc75b985dcb5a17daa4ea2b329c8efea274c3` | `765df0db1168001a212c77e5f871abe4725d4c92cc4e11ae8d887ff808f92e6a` |
| four-root atom construction used as a specialization check | `ae5e5a40a26c4886add226c7ebdee8c315b3c86348848a2d5bf89ee90e83846e` | `a36c0e863223ddf0857c531b73f06403dba71e1422f5a30d5df14c906ad1e0ba` |
| exceptional-neighbourhood theorem | `fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd` | `26be60e5389ec356dfd183d8a39e2a713e6db3695c807674daf7797fa1fcae2b` |

The two-cut theorem supplies the full components, the equality orientation,
the four colour-distinguished `p`--`q` paths in `C`, the full five-root
Du--Li--Xie--Yu bound, seven-connectivity, minimum degree eight, and the
fact that `C` is anticomplete to `D`.  The global palette theorem supplies
minimal infeasibility and the exact all-rainbow profiles

\[
       d_z=3,\qquad N_D(z)=K_3,qquad
       c_z=5-\rho_z,\qquad \rho_z\in\{0,1\},
\]

together with `2\le b\le5`.  The critical-host results cited there supply
`\alpha(G[N(z)])=3` and literal `K_5` exclusion.  These hypotheses are all
used; the proof does not claim the conclusion in the critical-completion
row or without root-minimality.

## 2. Scalar identities and the pole-contact bound

The degree sum over `C` is

\[
                         2m+h+(25-b)=8c+g.
\]

The definition of the full five-root slack is

\[
                         m+h+(25-b)=6c+1-s.
\]

Subtracting gives `m=2c-1+s+g`; substituting it back gives

\[
                         2s=4c-23+b-g-h.
\]

No sign assumption on `g+h-8` is used.  The four paths on the equality
shore use four different auxiliary colours.  Their first neighbours at
`p` and last neighbours at `q` are therefore distinct, giving four
incident `C`-edges at each pole and hence `h\ge8`.

## 3. Reconstruction of the coefficient-three identity

The completed seven-terminal graph has twenty terminal edges and

\[
                         R_5=6v(H)-21,
                         \qquad s=R_5-e(\mathcal G).
\]

After deleting one root `z`, minimal infeasibility supplies the four-root
witness path required by the constructive proof of Du--Li--Xie--Yu.  The
maximal restored component `L_z`, its path attachment set `U_z`, and the
literal atom satisfy

\[
 v(A_z)=r_z+k_z+3,
 \qquad e(A_z^+)\le3v(A_z)-7-2k_z.
\]

The lifting check has no omitted centre in the full five-root row.  A
two-linkage collection member which missed the contracted other-root
component would have whole-graph neighbourhood of order at most three,
because it lies in `C` and has no `D`-neighbour.  The path-direction
argument then keeps every collection member off the literal atom.  In the
critical complement, a collection member has neighbourhood of order at
most six, avoids the attachment set and poles, gains no neighbour in
`L_z`, and again has no `D`-neighbour.  Seven-connectivity makes that
collection empty.  Thus

\[
                         e(\mathcal G_1)le6v(H_1)-21-k_z.
\]

The exact decompositions are

\[
\begin{aligned}
 e(\mathcal G)&=e(\mathcal G_1)+e(A_z^+)+4,\\
 v(H)&=v(H_1)+v(A_z)-k_z-2.
\end{aligned}
\]

The added four edges are precisely the completion edges from `z` to the
other four roots; the completed pole incidences at `z` belong to `A_z^+`.
Substitution gives

\[
\begin{aligned}
 R_5-e(\mathcal G)
 &=3\bigl(v(A_z)-k_z-3\bigr)
   +\delta_{{\rm pl},z}+\delta_{{\rm crit},z}\\
 &=3r_z+\delta_{{\rm pl},z}+\delta_{{\rm crit},z}.
\end{aligned}
\]

This checks the coefficient `3`, both deficits, and the absence of an
additional boundary term.

## 4. Nontriviality of a rainbow atom

If `r_z=0`, the component is the singleton `z` and all `C`-contacts lie
on the induced witness path.  For `\rho_z=0`, five path vertices contain
an independent triple, which together with any vertex of the anticomplete
`D`-triangle violates `\alpha(N(z))=3`.

For `\rho_z=1`, let `p` be the adjacent pole.  The endpoint `p` sees at
most one of the four path contacts.  The other three contain an independent
pair `a,b` missed by `p`.  Literal `K_5` exclusion forces `p` to miss some
vertex `t` of the `D`-triangle, since otherwise
`\{z,p\}\cup N_D(z)` is a `K_5`.  Then `p,t,a,b` is an independent
four-set in `N(z)`.  Thus every `r_z\ge1` and the atom identity gives
`s\ge3`.

## 5. Local planar calculations

When `r_z=1`, write `L_z=\{z,v_z\}`.  The edge `zv_z` is compulsory.
The completed atom degree of `z` is `c_z+2=7-\rho_z`, while every edge
at `v_z` is retained in the atom.  Correcting for the internal edge gives

\[
                         e(A_z^+)=d_G(v_z)+6-\rho_z.
\]

Since the planar upper bound is `k_z+5`, its exact slack is

\[
 \delta_{{\rm pl},z}=k_z-d_G(v_z)-1+\rho_z.
\]

Minimum degree gives `k_z\ge9-\rho_z`.  The other four roots lie in the
opposite component after deleting the witness path, so none is adjacent to
`v_z`; hence `N_Z(v_z)=\{z\}`.  This also proves that the five `v_z` are
distinct whenever all atoms have `r_z=1`.

For `r_z\ge2`, the planar graph on the `r_z+1` vertices of `L_z` has at
most `3r_z-3` internal edges.  Degree summation over `L_z` therefore gives

\[
 e(A_z^+)\ge8r_z+7-\rho_z-(3r_z-3)
            =5r_z+10-\rho_z.
\]

Comparison with `3r_z+k_z+2` gives

\[
 k_z\ge2r_z+8-\rho_z,
 \qquad c\ge3r_z+8-\rho_z.
\]

The special `r_z=1` calculation is necessary; applying the planar
`3v-6` bound to a two-vertex `L_z` would lose one edge.

## 6. Audit of the rows `c=8,9,10`

The scalar inequality is

\[
                         2s\le4c-31+b.
\]

For `c=8`, `s\ge3` forces `b=5,s=3`, hence `r_z=1` and `\rho_z=1` for
every centre.  But `k_z\ge8>c-1`.

For `c=9`, the row `b\le4` has `s\le4`; a pole-free centre then has
`r_z=1` and `k_z\ge9>c-1`.  In the row `b=5`, `s\le5` forces all atoms
to have `r_z=1`, and `k_z=8`.  The eight path vertices induce at most
seven edges, while `v_z` has at most seven `C`-edges after its compulsory
edge to `z`.  Thus `m\le14`, contradicting `m\ge20`.

For `c=10`, `s\le7`.  The general local estimate excludes `r_z\ge2`.
If a pole-free centre exists, then `k_z=9` and the same count gives
`m\le15<22`.  In the all-pole-incident row, `k_z=9` gives
`m\le16<22`; hence every `k_z=8`.

For the last row, write `C=U_z\dot\cup\{v_z,w_z\}`.  There is no edge
`v_zw_z`, and

\[
                         m\le7+7+8=22.
\]

Equality with the global lower bound forces `s=3,g=0,m=22` and equality
in every local term.  Thus `v_z` has seven `C`-neighbours and only the
boundary neighbour `z`; `w_z` has eight `C`-neighbours and no boundary
neighbour.  The five `v_z` are distinct, each `w_z` is distinct from every
`v_y`, and the `w_z` are pairwise distinct because each has the unique
`C`-nonneighbour `v_z`.  These ten vertices exhaust `C`.

In the complement of `G[C]`, every `w_z` has degree one and every `v_z`
has degree two.  The second complement-neighbour of `v_z` cannot be a
`w_y`; it must be another `v_y`.  This makes the complement graph on the
five `v_z` one-regular, contradicting the parity of its degree sum.  The
order-ten exclusion is therefore valid.

## 7. Audit of the order-eleven elimination

If `c=11` and `b\le4`, then `s\le8`.  A pole-free centre cannot have
`r_z\ge2`, so it has `r_z=1` and `k_z\in\{9,10\}`.  The value ten gives
`m\le17<24`.  The value nine gives `m\le24`; equality would force
`s=3,g=0`, but its one leftover vertex is adjacent to all nine path
vertices and has degree at least nine.  Hence `b=5`.

Now `s\le9`, and the local estimate again makes every `r_z=1`.
The value `k_z=10` gives `m\le18<24`.  For `k_z=9`, with the notation in
the proof, the three nonnegative deficits satisfy

\[
                         x+y+t=4-s-g\in\{0,1\}.
\]

If the sum is zero, both the atom vertex and the leftover vertex have
degree at least nine, so `g\ge2`, whereas the scalar equation permits
`g\le1`.  If the sum is one, then `s=3,g=0`, but at least one of those two
vertices still has degree at least nine.  Hence every `k_z=8`.

The exact singleton formula then forces

\[
 d_G(v_z)=8,
 \qquad \delta_{{\rm pl},z}=0,
 \qquad \delta_{{\rm crit},z}=s-3.
\]

The definition of the attachment set leaves exactly two vertices in
`W_z`, both nonadjacent to `z,v_z`.  Finally, substituting `c=11,b=5` in
the global identities gives exactly

\[
 3\le s\le9,
 \qquad g+h=26-2s,
 \qquad m=21+s+g.
\]

No stronger equality for `s,g,h` is claimed.

The connectivity assertion also survives direct checking.  The other four
roots lie off `P_z`, so every internal vertex of `P_z` lies in `C`; its
open interior is connected and contains `U_z`.  Any component of
`C-V(P_z)` other than `\{v_z\}` cannot meet `v_z`, since it would then
belong to `L_z`.  Connectivity of `G[C]` forces it instead to meet an
internal path vertex.  Hence `G[C-\{v_z\}]` is connected.

Writing `a_z=|N_{\{p,q\}}(v_z)|`, the exact degree eight of `v_z`, its
unique centre neighbour `z`, and the fact that all its `C`-neighbours lie
in `U_z` give `d_C(v_z)=7-a_z`.  This degree-eight vertex is exceptional,
because a `K_4` in its neighbourhood would form a forbidden literal
`K_5` with `v_z`; therefore the pinned exceptional-neighbourhood theorem
gives `\alpha(G[N(v_z)])=3`.

If `a_z=0`, the seven `C`-neighbours lie on an induced path and contain an
independent four-set.  If `a_z=1`, the unique pole neighbour, being an
endpoint of the induced path, sees at most one of the six `C`-neighbours;
five remaining path vertices contain an independent triple, producing an
independent four-set together with the pole.  Both cases contradict the
neighbourhood theorem.  Hence `a_z=2`: every `v_z` sees both poles and has
five `C`-neighbours.  Exactly three members of `U_z` miss `v_z`; all are
adjacent to `z`, and they exhaust `N_C(z)-\{v_z\}` because that latter set
also has order three.

Those three vertices lie on the induced path `P_z`, so two of them are
nonadjacent.  They are both nonadjacent to `v_z`.  Any vertex of the
triangle `N_D(z)` is anticomplete to `C`; adjoining one gives an
independent four-set in `N(z)`, contrary to `\alpha(G[N(z)])=3`.  This
eliminates `c=11`.  Together with the audited exclusions of `c=8,9,10`, it
proves `|C|\ge12`.

## 8. Audit of the order-twelve elimination

For `c=12`, (4.3) makes every atom a singleton atom.  With

\[
 B=N_C(z)-\{v_z\},\quad X=N_C(v_z),\quad
 a=|N_{\{p,q\}}(v_z)|,\quad j=|B\cap X|,
\]

the boundary definition gives `U_z=B\cup X`, and the exact singleton
formula reduces to

\[
                         \delta_{{\rm pl},z}=2-a-j.
\]

Because one vertex of the anticomplete `D`-triangle can be added to any
independent set in `N_C(z)`, one has
`\alpha(G[N_C(z)])\le2`.  The vertices of `B` lie on an induced path, so
the members of `B` missed by `v_z` form a clique of order at most two.

For a pole-free centre, this forces `a=0,j=2`, zero planar deficit, and
`d_G(v_z)=k_z-1`.  At `k_z=9`, five path-neighbours of `v_z` missed by
`z` contain an independent triple, contradicting
`\alpha(G[N(v_z)])=3`.  At `k_z=11`, the induced-path count gives
`m\le19<26`.  At `k_z=10`, it gives `m\le27`, while the scalar and atom
identities plus the degree-nine atom vertex give `m\ge27`.  Equality makes
the unique leftover vertex adjacent to all ten path vertices and hence
forces at least two additional units of excess, contradicting `g=1`.
Thus every centre is pole-incident.

For a pole-incident centre, `j\ge1` and `a+j\le2`, leaving exactly

\[
                         (a,j)=(0,1),(0,2),(1,1).
\]

Minimum degree and the same degree-eight neighbourhood argument exclude
`k_z=8`; the edge count excludes `k_z=11`.  At `k_z=10`, the three cases
have respective triples

\[
 (\delta_{{\rm pl},z},d_G(v_z),m_{\max})
       =(1,9,27),(0,10,28),(0,10,27).
\]

The first and third contradict `m=23+s+g` immediately.  Equality in the
middle forces `s=3,g=2,m=28`, but both the degree-ten atom vertex and the
leftover vertex contribute at least two to `g`.  Hence `k_z=9`.  Its
positive-deficit case again has a degree-eight atom vertex with an
independent four-set in its neighbourhood.  Therefore every centre has

\[
 k_z=9,qquad d_G(v_z)=9,qquad
 a_z\in\{0,1\},qquad d_C(v_z)=8-a_z.
\]

The final simultaneous argument is exact.  For fixed `z`, the set
`W_z=C-(U_z\cup\{v_z\})` has order two.  If a distinct atom vertex
`v_w` lay in `U_z`, the induced path would give it at least six
nonneighbours within `C`, whereas its displayed `C`-degree gives only
`3+a_w\le4` nonneighbours in all of `C`.  Thus the four distinct vertices
`v_w`, `w\ne z`, would all lie in the two-set `W_z`.  This contradiction
eliminates `c=12` and proves `|C|\ge13`.

## 9. Audit of the order-thirteen elimination

For `c=13`, the only possible nonsingleton atom has `\rho_z=1,r_z=2`.
The size estimate forces `k_z=11`, and equality holds in both the planar
lower and upper estimates.  Thus the two `C`-vertices in `L_z` have degree
eight and form a triangle with `z`.  They see neither `D` nor another
centre.  Their degree sum leaves at most twelve edges to the eleven-vertex
set `U_z`; with their internal edge and at most ten induced-path edges,
this gives `m\le23`.  But the atom identity gives `s\ge6`, whereas the
global identity gives `m=25+s+g\ge31`.  Therefore every atom is a
singleton atom.

The local calculation from Section 8 applies unchanged.  For a pole-free
centre it excludes `k_z=9,11,12`, leaving `k_z=10,d_G(v_z)=9`.  The only
new tight case is `k_z=11`: its edge upper bound is thirty, and equality
would require `s=3,g=2`, while the degree-ten atom vertex and the
degree-at-least-eleven leftover vertex contribute at least five to `g`.

For a pole-incident centre, the three possible `(a,j)` pairs remain
`(0,1),(0,2),(1,1)`.  At `k_z=11` their respective triples

\[
 (\delta_{{\rm pl},z},d_G(v_z),m_{\max})
       =(1,10,30),(0,11,31),(0,11,30)
\]

are incompatible with `m=25+s+g`; in the only equality row, the leftover
vertex adds three units of excess beyond the three already contributed by
the atom vertex.  The endpoint rows are excluded exactly as before.  Hence
`k_z\in\{9,10\}`, `d_G(v_z)\in\{9,10\}`, and `a_z\le1`.

Every atom vertex consequently has at most five nonneighbours in `C`.
Membership in any other `U_z`, of order at least nine and inducing a
subgraph of a path, would give it at least six.  The four other distinct
atom vertices must all lie outside `U_z\cup\{v_z\}`, a set of order at
most three.  This verifies the final contradiction and `|C|\ge14`.

## 10. Audit of the order-fourteen elimination

For `c=14`, every nonsingleton atom has `r_z=2`.  If its two `C`-vertices
are `u,v`, direct subtraction from the planar bound gives

\[
 \delta_{{\rm pl},z}
   =k_z+1+\rho_z-d_G(u)-d_G(v)+e(G[L_z]).
\]

Since `u,v` see neither `D` nor another centre, the number of `C`-edges
incident with their pair is at most `k_z+2`.  This gives `m\le25` when
`k_z=12`.  In the only remaining case, `\rho_z=1,k_z=11`, the unique
leftover vertex gives

\[
 m=34-(x+t+\delta_{{\rm pl},z}+A),qquad
 m=33+\delta_{{\rm pl},z}+\delta_{{\rm crit},z}+g.
\]

Thus `t+g\le1`, while its degree gives `g\ge3-t`.  This contradiction
checks the exclusion of all nonsingleton atoms.

For singleton atoms the `B,X,a,j` calculation remains valid.  A pole-free
atom has `k_z\in\{10,11\}`: the larger values have edge upper bounds
twenty-three and thirty-three, and equality in the latter forces at least
seven units of excess instead of three.  A pole-incident atom has
`k_z\in\{9,10,11\}`.  At `k_z=12`, the exact rows are

\[
 (\delta_{{\rm pl},z},d_G(v_z),m_{\max})
       =(1,11,33),(0,12,34),(0,12,33),
\]

and the global lower bound or the leftover vertex excludes each.  The
smaller degree-eight rows are excluded by the already audited neighbourhood
argument.  Hence every atom vertex has degree at least nine, at most one
pole neighbour, and therefore at most six nonneighbours in `C`.

If one attachment set had order at least ten, none of the other four atom
vertices could lie on its path: such a vertex would acquire at least seven
nonneighbours.  The complementary set has order at most three, so this is
impossible.  The forced common row is exactly

\[
 \rho_z=1,quad r_z=1,quad k_z=9,quad d_G(v_z)=9,
 \quad\delta_{{\rm pl},z}=0,quad |W_z|=4,quad
 (a_z,j_z)\in\{(0,2),(1,1)\}.
\]

For the final incidence check, put `V=\{v_z:z\in Z\}` and `F=G[V]`.
The equality `U_z=B_z\cup N_C(v_z)` is literal.  A distinct atom vertex
cannot belong to `B_z`, since its unique centre neighbour is its own
centre.  Consequently

\[
                         v_w\in U_z\iff v_zv_w\in E(F).
\]

A vertex with `a_w=0` has only five `C`-nonneighbours and is therefore
isolated in `F`.  Along an edge `v_zv_w`, the endpoint `v_w` has six
nonneighbours, all forced into `U_z`; hence it is adjacent to every atom
vertex missed by `v_z`.  Every edge of `F` is dominating.  If `F` is
nonempty, no vertex is isolated, every `a_z=1`, and transitivity of
nonadjacency makes `F` complete multipartite.

Every `F`-neighbour of `v_z` lies on `P_z` and has exactly one pole
neighbour.  The two path endpoints can each see at most one such vertex,
so `\Delta(F)\le2`.  A nonempty complete multipartite graph of order five
and maximum degree two cannot exist: every part would have order at least
three.  Thus `F` is empty.

Now the four-set `W_z` consists exactly of the other atom vertices, and all
`U_z` equal the common nine-set `C-V`.  No other atom vertex can occur on
`P_z`, since it has at least seven neighbours in that nine-set.  The two
poles consequently have at most two neighbours in `C-V` altogether, and
the five atom vertices have at most five pole incidences.  This gives
`h\le7`, contradicting the independently supplied `h\ge8`.  The entire
order-fourteen row is therefore eliminated.

## 11. Terminal scope

The contradictions remove every row through order fourteen, so no
private-contact or rooted-minor analysis is needed there.  At order fifteen
and above, singleton atoms are no longer forced and the five atom paths
remain separately chosen.  The theorem therefore does not produce a common
boundary partition, a rooted `K_6^-` model, a shore-confined two-helper
packing, or a response-preserving strict two-cut.  No unresolved assumption
or proof gap remains inside the stated order-fifteen lower bound; the higher
all-rainbow rows remain open.
