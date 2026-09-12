# Global edge codegree and two contraction consequences

**Status:** written proof; a separate internal audit accompanies this source. These are
structural deductions; no global colouring conjecture or closed induction
is claimed. All graphs are finite and simple, and all quotients are
simplified. Put `Q=K7-2K2`, `W4=K1 join C4`,
`c_H(xy)=|N_H(x) intersect N_H(y)|`, and `q(H)=e(H)-4|V(H)|`.

## Exact inputs

The following source and adjacent-audit hashes were checked for this draft.
The NT statement was previously inspected in the cited source; this draft
uses its recorded statement and does not claim a new literature audit.

| Input | Source SHA-256 | Audit SHA-256 |
| --- | --- | --- |
| [NT Theorem 8 statement](../results/hc7_five_root_almost_clique.md#external-input) | `de183e350c412739c05a744e811304454ba90856efee9e097813c70617bba9cd` | `dc7db3d391ef2701516d64dd32e7546d40e2e4171406193f17d8feadcc4abb47` |
| [Five-root wheel extension](../results/hc7_rooted_wheel_extension.md) | `f72e0b3d4254724a58f55b9445c0c173ea6c96e535416da47b1efc7fd5eb43b3` | `c93612165de23798c63922425fbd8d9e74407d2eb1a85b365853bd1343969178` |
| [Two-edge contractions, Theorem 1](../active/hc7_companion_two_edge_contractions.md#1-a-six-connected-class-closed-for-one-literal-exclusion) | `fe0cd007483e61d5de4164a116c089f6c6842fd815c64ffeaa6ba4e58daa1b16` | `4f67fcd5a6ed384c971f7580a6541a465157175cabc9f8399504ba923768752a` |
| [Four-clique contact bounds](../results/hc7_four_clique_complement_contacts.md#contact-bounds) | `945cfac070104f2b0994fcb6dcfafcc04fa32cbe22cbafb81ab2eac4c0b8d83a` | `b7dee4a1bdb9472c1224a59284e396fe9f2a8d611f996b3a95cbfa20c2e83fec` |
| [Contraction closure, Corollary 3](../active/hc7_companion_contraction_closure.md#3-a-contact-restriction-beside-a-literal-four-clique) | `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4` | `26b2f5ad7226c7bb3f194cac8523f043d7ae6ca955036249f04ddc9fb6d94394` |

We use the following immediate consequence of the first two inputs:
every five vertices in a four-connected nonplanar graph root a W4.
Indeed, NT Theorem 8 gives a K4 rooted at four of them: four-connectivity
excludes its separation alternatives, and nonplanarity excludes its plane
alternative. The wheel extension retains all five roots, including when
the fifth already belongs to the initial model.

## 1. Every original edge has codegree at most four

**Theorem 1.** If G is seven-connected, `delta(G)>=8`, and G has no Q
minor, then `c_G(xy)<=4` for every edge xy.

**Proof.** Put `P=G-{x,y}`. It is five-connected and has minimum degree
at least six. A finite simple planar graph of order at least three has
`sum_z(6-d(z))>=12`, so P is nonplanar. If xy had five distinct common
neighbours, these vertices would root a W4 in P by the preceding input.
Each wheel bag meets both x and y. Adding the two adjacent singleton
bags `{x},{y}` gives `K2 join W4=Q`, a contradiction. QED

No chromatic hypothesis or chosen degree-eight vertex is used.

## 2. Every first quotient has the same codegree bound

**Theorem 2.** Under Theorem 1, for every edge ab the graph `H=G/ab`
is six-connected and Q-minor-free, has minimum degree at least seven
and at most four vertices of degree seven, and its merged vertex has
degree at least ten. Every edge of H has codegree at most four. Both H
and every quotient `H/xy`, for `xy in E(H)`, have no literal K5-minus
subgraph.

**Proof.** A cut of order at most five in H lifts to a cut of order at
most six in G, replacing the merged vertex by a,b if it is deleted.
Thus H is six-connected. Its merged degree is

```text
d_H(ab)=d_G(a)+d_G(b)-2-c_G(ab)>=10.
```

Every other vertex loses at most one neighbour. It has degree seven only
if it was a degree-eight common neighbour of a,b, so there are at most
four such vertices. Minor exclusion lifts through the fixed connected
preimage `{a,b}`.

For any edge xy of H, the graph `P=H-{x,y}` is four-connected and has
minimum degree at least five. A degree-five vertex of P must have had
degree seven in H, so there are at most four of them. If P were planar,
Euler's inequality would require at least twelve degree-five vertices:
all other vertices contribute at most zero to `sum_z(6-d_P(z))`.
Hence P is nonplanar. Five common neighbours of x,y would again root
a wheel in P and, together with `{x},{y}`, give Q. Thus `c_H(xy)<=4`.

H satisfies every hypothesis of the cited two-edge-contractions
Theorem 1, which excludes a literal K5-minus in H and in every H/xy.
This applies whether xy meets the first merged vertex or avoids it. QED

## 3. A paired four-clique quotient with positive excess

**Theorem 3.** Suppose G satisfies Theorem 1 and R is a literal K4
such that `F=G-R` is four-connected and nonplanar. There is a perfect
matching M of R such that the quotient J obtained by contracting its
two edges is six-connected and Q-minor-free, with

```text
q(J)>=q(G)+2>=2,    delta(J)>=7,
at most one vertex of degree seven.
```

The two merged vertices p,q are adjacent and each has degree at least
nine. This applies to `R={v} union A` in the actual two-triangle critical
host, using the complement facts already recorded in the contact source's
application (or exchanging A and B).

**Proof.** Contraction-closure Corollary 3 gives at most two R-neighbours
per F vertex. Every R vertex has at least five F-neighbours, since its
other three clique vertices account for exactly three neighbours.
Deleting any triangle of R leaves G connected, by seven-connectivity.
The contact theorem therefore bounds by five the total number of F
vertices with two R-neighbours.

For a perfect matching M of R, let D(M) count those vertices whose two
R-neighbours form an edge of M. Each such vertex is counted by exactly
one of the three perfect matchings. Their three D-values sum to at most
five, so choose M with `D=D(M)<=1`.

The six edges inside R become the single edge pq, losing five edges.
A vertex of F loses one R-contact exactly when it is counted by D;
all other F-edges and R-contacts are retained. Consequently

```text
|V(J)|=|V(G)|-2,    e(J)=e(G)-5-D,
q(J)=q(G)+3-D>=q(G)+2.
```

Outside p,q, only these D vertices lose degree, each by one. Thus all
outside degrees are at least seven and at most one is seven. If ab is
one matching edge, its two other clique vertices are common neighbours,
so Theorem 1 gives `|N_F(a) intersect N_F(b)|<=2`. Therefore its pole
has degree `1+|N_F(a) union N_F(b)|>=1+5+5-2=9`.

Consider a cut of at most five vertices in J. If it contains at most
one pole, it lifts to at most six vertices of G and cannot separate J.
If it contains both poles, the surviving graph is F with at most three
vertices deleted, which is connected. Hence J is six-connected.
Its Q-minor exclusion follows by lifting through the two disjoint
matching edges. The degree/Euler argument from Theorem 2 also gives
`c_J(xy)<=4` for every edge; the two-edge-contractions Theorem 1 excludes
a literal K5-minus in J and every J/xy. QED

**Iteration remains unproved.** All displayed contractions decrease order
and have fixed disjoint connected preimages, so any resulting Q model
lifts. A further arbitrary edge contraction of J, however, guarantees
only five-connectivity and may lower its sole degree-seven vertex to six.
The excess remains at least one, since
`q(J/xy)=q(J)+3-c_J(xy)>=1`, but the six-connected degree class needed
for another application is not preserved. No edge avoiding both failures,
closed separator reduction, or six-chromatic quotient is established here.
