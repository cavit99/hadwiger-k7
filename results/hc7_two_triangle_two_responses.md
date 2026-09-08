# Only one triangle root can occur on a tight exterior boundary

**Status:** written proof; a separate exact-source internal audit is recorded beside it.
This strengthens the exterior-helper theorem. It does not close the
two-triangle case, Conjecture 19, or HC7.

Graphs are finite and simple. Set neighbourhoods are external. Write
`Q=K_7` minus two independent edges; rooted bags are connected, pairwise
disjoint, and retain their prescribed roots separately.

**Theorem.** Suppose `G` is seven-connected, `delta(G)>=8`, has no
`Q` minor, and `d(v)=8`. Suppose
`N(v)=A dotcup B dotcup {x,y}`, where `A,B` span triangles and `xy`
is an edge; extra edges are allowed. Put `W=G-N[v]` and `H=G-v-B`.
Define

`A_4={s in A : s in N_H(D) for some nonempty D subseteq W with |N_H(D)|=4}`.

Then `|A_4|<=1`. The symmetric assertion holds for B. No colouring
assumption is used.

**Corollary.** For at least two vertices `s in A`, every nonempty
`X subseteq W` has at least four neighbours in `H-s`. For each such s,
`H-s` has a rooted `K_4` at `(A-{s}) union {x,y}`.

## Inputs

We use the following separately audited proofs at these exact hashes:

- [Exterior helpers, Sections 1--4](hc7_two_triangle_exterior_helpers.md),
  SHA-256 `b3fe07ea52e0e553c61edb59cd5b7da3719ae834d8803f21afb9bde90fc410a8`;
  [audit](hc7_two_triangle_exterior_helpers_audit.md), SHA-256
  `e9bc147d6c0e48bba395dc5fe590ef8a8cc778914804e3c1f5d33c48e2eec628`.
  This supplies four-connectivity and minimum degree six of H, the
  all-A-boundary exclusion, and the internal-four/nonroot-degree-six
  rooted `K_4` packet. It also gives `d_H(w)>=7` whenever `w in W`
  sees an A vertex.
- [Five-root degree-six theorem](hc7_five_root_degree_six.md),
  SHA-256 `289c5ad015b6c392ea69e8e26e15eba54b4eba7cb155789edd76b3dbb5c9f9a4`;
  [audit](hc7_five_root_degree_six_audit.md), SHA-256
  `6f13ffd37126c78a697b5752574fe06b6fd13b68dabb0d63e4e39d76a8f1d065`.
  With five roots containing a triangle, nonroot minimum degree six
  and nonroot-set boundary at least five, it gives a rooted `K_5^-`.
  At least two triangle vertices are admissible as the triangle
  endpoint of its sole possible missing edge; the other endpoint is
  one of the two nontriangle roots.

The boundary exclusion needed below is proved here, so the proof does
not depend on a changing technical frontier. No fresh literature
inspection or finite computation is used.

## 1. Tight boundaries meet only one neighbourhood root

**Lemma 1.** If nonempty `D subseteq W` has `|N_H(D)|=4` and its
boundary meets A, then it contains no other vertex of `N(v)`.

**Proof.** Write `T=N_H(D)`. In G the boundary is contained in
`T union B`; since v is outside this boundary, seven-connectivity gives
`N_G(D)=T union B`, a seven-set denoted S. Any component of
`G-(D union S union {v})` containing a neighbour of v has at least
seven contacts among `S union {v}`: D remains outside its boundary.
It therefore misses at most one S vertex. For any five roots in S
containing a triangle, the side on those roots and D satisfies the
degree-six theorem: deleting the other two S vertices loses at most
two neighbours from every D vertex and every nonempty D-set boundary.

If T contains all of A, the all-A-boundary exclusion in the first input
already gives Q. If it contains exactly two A vertices s,t, let u be
the third. Use the five roots `B union {s,t}`. The component Y containing
u sees s,t and v through their literal edges, and misses at most one B
root. Choose an admissible B centre different from that possible omitted
root. The five-root model, Y and v give Q: their only possible holes
are the core's centre--s/t hole and Y's different B omission.

It remains to consider `T={s} union P` with `s in A` and P meeting
`{x,y}`. If both x,y lie in P, take the component Y containing `A-{s}`.
It sees s,v and at least one of x,y; choose such an endpoint z. Apply
the packet at `B union {s,z}`. Y can now miss only one B root, so an
admissible centre avoiding that root again gives Q with Y and v.

Otherwise, by symmetry, `T={s,x,p,q}` with `p,q in W`. Use roots
`B union {s,x}`. Let Y contain `A-{s}` and let Z contain y in the
displayed outside graph. Y sees s,v; Z sees x,v. If they coincide,
their common component misses at most one B root, and the previous
centre choice closes. If distinct, Y alone closes with v unless its
sole core omission is x: any other omission is a B root and can be
avoided by the centre choice. Similarly Z closes unless it misses s.
In the remaining case Y misses only x and Z misses only s among the
five roots. Take any packet. If its hole is `b-s`, use Y and the
connected bag `Z union {v}`; if its hole is `b-x`, use Z and
`Y union {v}`. If there is no core hole, use either choice. The merged
extra bag is full to all five rooted bags through v, and meets the
other extra bag through its v-edge. The two possible holes have
disjoint ends. All preimages lie on the indicated disjoint sides.
This proves the lemma. QED

## 2. Minimal tight regions are anticomplete

For each `s in A_4`, choose a witnessing nonempty set. Any component
of it has boundary contained in the same four-set; four-connectivity
forces equality, including the contact to s. Lemma 1 makes this
boundary `{s} union P_s`, with `P_s subseteq W` of order three.
Choose D_s inclusion-minimal among all connected regions of this form.
The degree bound `delta(H)>=6` implies
`|D_s|>=3`, since a vertex in a region of order at most two with
four external neighbours has degree at most five.

Suppose `s,t` are distinct members of `A_4`. For every nonempty `X subseteq W`,
`f(X)=|N_H(X)|>=4`: at least one of the five vertices `A union {x,y}`
would survive outside a smaller boundary. Moreover f is submodular,
since `f(X)=|N_H[X]|-|X|` and closed-neighbourhood cardinality is a
coverage function. If D_s and D_t overlapped, their union and
intersection would both have boundary four. The union's boundary
contains s,t, contradicting Lemma 1. Hence they are disjoint.

If an edge joined them, put
`a=|P_s intersect D_t|`, `b=|P_t intersect D_s|`, and
`c=|P_s intersect P_t|`. Here `a,b>=1`. Their union has boundary at
most `8-a-b-c`, while Lemma 1 and four-connectivity force at least
five neighbours. Thus `a+b+c<=3`.

If `a=1,b=2`, let p be the sole D_t vertex meeting D_s. A component
of `D_t-p` has boundary contained in t, p, and the one P_t vertex
outside D_s: all edges to the other two P_t vertices used p. This
contradicts four-connectivity. The remainder is nonempty because
`|D_t|>=3`. The case `a=2,b=1` is symmetric.

The only remaining case is `a=b=1`. Let q be the sole D_s vertex
meeting D_t. Any component L of `D_s-q` has boundary contained in s,
q, and the other two P_s vertices. Four-connectivity forces equality,
so L is a strictly smaller connected s-region of the prescribed form.
This contradicts minimality. Therefore D_s,D_t are anticomplete;
in particular both port sets lie outside both regions.

## 3. An outside path completes the two-region construction

Write `A={s,t,u}` and put `J=H-{s,t}`. This graph is two-connected,
and `N_J(D_t)=P_t`. In `J-D_t`, a component containing a vertex outside
P_t must contain at least two P_t vertices. Otherwise its unique P_t
vertex would be a cutvertex of J, with that nonport vertex on one side
and the nonempty set D_t on the other.

The vertex u and every vertex of D_s lie outside P_t. They must
therefore belong to the same component of `J-D_t`: two distinct
components would each require at least two vertices of the three-set
P_t. Choose a path there from u to D_s, and stop at its first P_s
vertex p. Such a vertex occurs before entry into D_s, because its
boundary in J is precisely P_s. The retained path avoids D_s,D_t,
s,t,B and v, apart from its endpoint p among the prescribed side roots.

In `G[D_s union B union {s,p}]`, every nonroot degree is at least six
and every nonempty nonroot set has at least five neighbours: only the
other two P_s ports were removed from its original seven-vertex side
boundary. Apply the degree-six theorem and extend only its p-rooted
bag along the retained path to u. The five bags remain connected and
pairwise disjoint. They have all contacts except possibly one.

The additional connected bag `D_t union {t}` is full to all five:
it sees B through D_t, the s bag through `ts`, and the extended p bag
through `tu`. The singleton v is also full to all five, through their
roots B,s,u, and meets the additional bag at t. These seven disjoint
bags give `K_2 join K_5^-=K_7^-`, which contains Q. This contradiction
excludes two members of `A_4` and proves the theorem.

For `s in A-A_4`, a nonempty W set with at most three neighbours in
`H-s` would have exactly four in H, including s, a contradiction.
Each W vertex has degree at least six in `H-s`: an s-neighbour had
degree at least seven in H, and a non-neighbour loses nothing. The
four-root packet in the first input, applied with nonroot set W and
roots `(A-{s}) union {x,y}`, proves the corollary.

This gives at least two successful deletions, without asserting one
model serves both. It supplies no complete two-triangle construction.
