# Closing the degree-eight cycle-and-triangle case

**Status:** written proof. The adjacent audits record their separate internal
verdicts at the exact source hash.
All graphs are finite and simple. Write `Q=K_7-2K_2`, with two independent
edges deleted. Contacts between bags mean actual edges of the host.

**Theorem.** Let `G` be seven-connected with minimum degree at least eight.
Suppose a vertex `v` has degree eight and its neighbourhood consists of an
induced five-cycle `C` and a disjoint triangle `A`, with at most one edge
between them. Then `G` has a `Q` minor.

This closes the entire cycle-and-triangle neighbourhood case, for arbitrary
host order. It does not close the two-triangles-and-edge case or prove
Conjecture 19, Conjecture 21 or HC7. No colouring hypothesis is required.

## 1. An elementary contact construction

**Lemma.** Let four vertices `Z` span a cycle of length four in a graph
`F`. Suppose `J=F-Z` is three-connected and contains a triangle
`A={a0,a1,a2}`. Suppose `J` has a partition into connected adjacent
sets `U,V`, each contacting every vertex of `Z`. Adding a vertex `v`
adjacent to every vertex of `Z union A` produces a `Q` minor.

**Proof.** If `A` meets both parts, the seven bags `Z,{v},U,V` give
`K_3 join C_4=Q`. Otherwise interchange the parts so that `A subseteq U`.

There are three paths from the three distinct vertices of `A` to `V`,
disjoint outside `V`. Their endpoints inside `V` may coincide. To see
this directly, give each vertex of `U` capacity one, vertices of `V`
capacity three, and join a source to each vertex of `A` by a capacity-one
arc. Join `V` to a sink with capacity-three arcs and use capacity-three
arcs for host edges. A cut of capacity at most two consists only of
source arcs and at most two vertices of `U`. Some source root survives
both deletions and remains connected to `V` by three-connectivity of
`J`. Thus no such cut exists. An integral flow of value three saturates
all three source arcs. Vertex capacities then ensure that no path uses
another source root internally. Stop each path at its first vertex of
`V`; its portion in `U` is a connected seed containing its prescribed
`a_i`, and the three seeds are disjoint and each contact `V`.

Extend these seeds to a connected partition `U=U0 dotcup U1 dotcup U2`:
while a vertex is unassigned, connectedness of `U` supplies an edge from
the assigned union to an unassigned vertex, which is added to that edge's
region. The number of unassigned vertices strictly decreases. Each `Ui`
contains `a_i` and contacts `V`; the three regions are pairwise adjacent
by the original triangle `A`.

Call `z in Z` private to `Ui` if `Ui` is the only one of these regions
contacting `z`. If some `Ui` has no private vertex, replace the helpers
by `V union Ui` and the union of the other two regions. Both sets are
connected, adjacent, full to `Z` and contain vertices of `A`. The first
construction gives `Q`.

Otherwise each region has a private vertex of `Z`. These three vertices
are distinct. Choose one contacting region for each of the four cycle
vertices, retaining all three private choices. The resulting labels use
all three regions, with multiplicities `2,1,1`. Name the repeated region
`Ua` and the others `Ub,Uc`; let `b,c` be the uniquely labelled cycle
vertices. At least one neighbour of `b` on the four-cycle has label `Ua`,
since only one vertex has label `Uc`. Call that neighbour `a` and call
the remaining cycle vertex `d`; its label is also `Ua`.

Merge the adjacent cycle vertices `a,b` into the connected bag `X`, and
adjoin `c` to `Uc` through its selected contact, giving `Y=Uc union {c}`.
The five disjoint connected bags

`X, {d}, Ua, Ub, Y`

have every pairwise contact except possibly `{d}--Ub`. Indeed, contracting
one edge of the four-cycle makes `X,c,d` a triangle. These edges give
`X--{d}`, `X--Y` and `{d}--Y`. Selected labels give `X--Ua`, `X--Ub`
and `{d}--Ua`; the triangle `A` gives all three contacts among `Ua,Ub,Y`.
Both `{v}` and `V` contact all five bags: use their original cycle
contacts and, for the three regions, their `A` roots and their retained
contacts to `V`. Only `{v}--V` may additionally be missing. The pairs
`{d}--Ub` and `{v}--V` have distinct ends, so these seven bags contain
a `Q` minor. All bags are specified disjoint unions in the original
host; unused edges can be deleted. QED

## 2. Supplying the four cycle roots and the helpers

**Proof of the theorem.** Suppose for a contradiction that `G` is
`Q`-minor-free. The separately audited
[three-connectivity theorem](../results/hc7_cycle_triangle_complement_three_connectivity.md),
at SHA-256 `4e2b5b0b7b7294c30bdcdd1b4f147d12ba535dc3513508981160c5173d519228`,
applies with exactly these hypotheses. It gives three-connectivity of
`G-v-C`, which contains the triangle `A`.

Put `n=|V(G)|` and `q=e(G)-4n>=0`. Choose any edge `xy` of `C` and put
`c=|N_G(x) intersect N_G(y)|`. Since every degree is at least eight,

`2q=sum_w(d_G(w)-8)>=d_G(x)+d_G(y)-16>=2c-14`,

so `c<=q+7`. Set `F=(G/xy)-v`, and let `Z` be the four images of `C`.
The contraction removes exactly `c+1` edges and reduces the degree of
`v` to seven. Consequently

`|V(F)|=n-2`,

`e(F)=e(G)-c-8=4|V(F)|+q-c>=4|V(F)|-7`.

The graph `F` is five-connected: a separating set of at most four
vertices would lift, on adding `v` and replacing the contracted root
by `x,y` when necessary, to a separating set of at most six vertices
of `G`. Distinct surviving components remain separated under this lift.
Also `G` has order at least nine by its minimum degree, so `F` has at
least seven vertices. Thus `(F,Z)` is internally four-connected.

[Norin--Totschnig, Lemma 12](https://arxiv.org/html/2507.03244v1#S2)
states that an internally four-connected pair `(F,Z)`, with `|Z|=4`
and no `Z`-rooted two-helper model, has `e(F)<=4|V(F)|-10`.
Our stronger density bound therefore supplies four rooted bags and two
adjacent helpers, each contacting all four rooted bags. By
[the spanning-helper lemma, Lemma 3](../active/hc7_companion_helper_construction.md),
at SHA-256 `0c1ac8052f7734d8d0267381c030e177bd70010eded63d15fdca8c0db6d1f375`,
five-connectivity of `F` makes the root bags the four singletons `Z`
and the helpers a connected partition of `F-Z`.

Here `F-Z=G-v-C` is the three-connected graph obtained above. The four
roots span a four-cycle, and `v` in `G/xy` is adjacent to all of
`Z union A`. Apply the lemma to obtain `Q` in `G/xy`.

To lift, replace the unique occurrence of the contracted root by the
fixed connected set `{x,y}`. Each other vertex has its singleton
preimage. These preimages are disjoint, and every quotient contact has
an original edge between its preimages. All subsequent unions in the
lemma therefore remain connected and disjoint. This gives `Q` in `G`,
the required contradiction. No induction on a quotient, preservation of
critical colourings, or preservation of seven-connectivity after
contraction is assumed. QED
