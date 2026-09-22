# Two-separator construction in the clean prism webs

**Status:** frozen unaudited precursor, superseded by the
[two-connected cell exclusion](../results/hc7_prism_two_connected_cell_exclusion.md).
The argument
below resolves the specified isolated-gate state and its simultaneous
insertion. It does not resolve every clean cell in a two-connected E.
The selected target remains the entire six-chromatic case in the
[technical frontier](../active/hc7_c21_rooted_density_construction.md#completed-case-the-two-triangle-neighbourhood).

## Setting

Retain the original critical host, its extremal prism S with rails
R1,R2,R3, remainder E, the actual six-neighbour bound for nonempty
root-free sets, and the audited locality of non-cut vertices of E.
Assume E is two-connected. Roots have at least two E-neighbours and
rail-interior vertices at least four.

Use clean web completions of H_i=J-V(R_i) whose WHOLE cell interiors
lie in E and whose whole interiors from different views are disjoint.
A whole cell can be disconnected in the actual graph. Fix one cell C
of view i with actual gates

    B=N_{H_i}(C)={x,y,z} subseteq E,
    E-C = A disjoint union {z},

where A is connected and contains x,y, and z is isolated in E-C.
Thus N_E(z) is contained in C, and C is anticomplete to the two
surviving rails. We prove that z has no surviving-rail contact and
that the enlarged whole patch C+z admits planar insertion along x,y.

## 1. The isolated gate is visible in both alternate views

Suppose z lies inside a whole cell D of an alternate view j. All of
C is visible in that skeleton. Every E-neighbour of z is in C and
is therefore a D-gate. Locality and the J-degree bound give d_E(z)>=3,
so there are exactly three and they occupy D's entire facial triple.
Thus all S-neighbours of z lie on the deleted rail R_j.

Locality gives d_S(z)<=3, and d_G(z)<=d_E(z)+d_S(z)+1<=7, where the
only possible additional neighbour is r. Minimum G-degree is seven.
Hence d_G(z)=7 and z has exactly three S-neighbours, consecutive
vertices a,b,c on R_j. Any E-neighbour w of z lies in C and is
anticomplete to R_j, because R_j survives in the original view i.
Then {w,a,c} is an independent triple in N_G(z), contradicting
Dirac's bound alpha(G[N_G(z)])<=d_G(z)-5=2.

Therefore z, like all of C, is visible in both alternate skeletons.

## 2. No surviving-rail contact is possible

Let W be z together with every actual connected component of C
having a neighbour at z. W is connected and W-z is nonempty. Its
complement A'=E-W is connected: it contains A, and each remaining
actual C-component has its E-boundary in {x,y} and has an x/y
neighbour. Also N_E(W) is contained in {x,y}, and all S-neighbours
of W-z lie on R_i.

Suppose z contacts t on a surviving rail R_j; let k be the third
index. Every vertex of R_j has an A'-neighbour: W contributes at
most z to its E-neighbourhood, while roots have at least two and
interior vertices at least four E-neighbours. Choose d on R_j,
different from t.

The nonempty root-free set W-z has E-boundary in {x,y,z} and no
S-neighbours off R_i. The six-neighbour condition gives it at least
three distinct R_i-neighbours. Let a,b be the first and last
R_i-neighbours of W in the order from p_i to q_i.

No vertex v of the open interval R_i(a,b) can contact A'. Otherwise
connected W and A' give two vertex-disjoint opposite-corner paths
in H_k, with the W/A' passages using only E-vertices:

* If d precedes t on R_j, use
  p_i R_i a -- W -- t R_j q_j and
  p_j R_j d -- A' -- v R_i q_i.
* If d follows t, use
  p_i R_i v -- A' -- d R_j q_j and
  p_j R_j t -- W -- b R_i q_i.

The two-rail cycle and these diagonals give the forbidden four-root
K4 in H_k, which would finish with R_k. Extra z-contacts do not
affect disjointness; t need not be the only surviving-rail contact.

Now take the ACTUAL root-free set

    X=(W-{z}) union V(R_i(a,b)).

It is nonempty and need not be connected. Its E-neighbours outside
it lie in {x,y,z}, because A' avoids the open interval. Its remaining
S-neighbours lie in {a,b}: W-z has only R_i contacts, and the open
rail interval has no other prism exits. Thus

    N_J(X) subseteq {x,y,z,a,b},

contrary to the six-neighbour condition. Therefore z has no contact
on either surviving rail. This includes adjacent pairs and cap contacts.

## 3. Cofacial two-gate embedding of the enlarged whole patch

Put U=C union {z}. Its actual H_i-boundary is {x,y}, and E-U=A
is connected. All U vertices are visible in both alternate skeletons.
Choose an alternate view where x,y are not hidden in the same whole
cell. Such a view exists: if both are hidden together in one view,
whole-cell cross-view disjointness makes both visible in the other.
Choose a simple actual x--y path L in A.

Project each L portion inside an alternate cell to facial edges
between its gate endpoints. Those endpoints belong to A, avoiding U.
If x or y is hidden, insert that endpoint as one star in its face;
the two hidden endpoints occupy distinct faces. Its actual U-neighbours
are face gates, and its L exit is a gate outside U. The star preserves
the actual patch contacts and the projected path exit. Path edges
on face boundaries do not cross these stars.

This gives a plane supergraph containing the actual J[U union {x,y}]
and an x--y walk whose interior avoids that patch. Simplify to a path.
The path exposes both gates on one face; an existing xy edge already
suffices. Hence the WHOLE enlarged patch, including every component
of C and z, has an embedding with x,y cofacial. This does not assert
that the old three gates x,y,z are cofacial.

## 4. Simultaneous actual insertion

The actual z has NO H_i edge outside C: its E-neighbours lie in C,
and Section 2 removed its surviving-rail contacts. It is free to move
from the old skeleton into U. For a precise planar scaffold, retain
a new auxiliary placeholder z* at z's old skeleton position, with
the old COMPLETION incidences. It is not an actual graph vertex.
Inside the old facial triangle x,y,z*, insert the cofacial two-gate
patch U along x,y; its actual z is an interior patch vertex.

No other whole cell has an actual z contact. Any old face using z
can therefore retain the auxiliary z* as a scaffold corner without
changing that cell's actual boundary. Auxiliary vertices and edges
are discarded at the end. This changes no actual edge and uses no
completion edge as a minor-model contact.

The operations are compatible for all isolated-gate cells in the
same view. Original cell interiors are disjoint and the absorbed
gates were skeleton vertices. One gate cannot serve two enlarged
patches: its nonempty E-neighbourhood would be contained in two
disjoint cells. Nor can an absorbed gate be an ACTUAL external gate
of another enlarged patch, by the same neighbourhood condition.
There are no actual edges between different absorbed gates. Replace
all these gates by auxiliary placeholders and insert each enlarged
patch in its original face. This simultaneously resolves these cells
while preserving every actual vertex and edge.

## Remaining scope

The specified disconnected-complement state is resolved as a planar
insertion problem. Other three-Egate cells, and the general connected-
complement/two-separator integration, remain separate. This is not a
proof that all H_i are planar for every two-connected E.
