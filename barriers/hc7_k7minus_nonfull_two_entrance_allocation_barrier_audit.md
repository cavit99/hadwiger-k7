# Independent audit of the one-nonfull two-entrance allocation barrier

**Status:** separate internal mathematical and computational audit, GREEN.

This is an internal audit, not external peer review.

## Exact revisions audited

- barrier:
  [`hc7_k7minus_nonfull_two_entrance_allocation_barrier.md`](hc7_k7minus_nonfull_two_entrance_allocation_barrier.md)
- barrier SHA-256:
  `b816e68468030122d96478c83f0e7152998241d12f4e266a2dda65aa0c0c003e`
- retained verifier:
  [`hc7_k7minus_nonfull_two_entrance_allocation_barrier_verify.py`](hc7_k7minus_nonfull_two_entrance_allocation_barrier_verify.py)
- verifier SHA-256:
  `f374c2993c2f0d9954a8a60192987a6d21dd4e577ec6099c48ea19c26a015462`

## Verdict

**GREEN.**  The displayed graph has every stated incidence, is exactly
seven-connected and five-chromatic, has the claimed boundary-full packing
vector `(1,2)`, admits no two-full-plus-defect-two allocation on the rich
side, and contains the displayed explicit `K_7`-minor model.  The stated
scope as a barrier to the topology-only shortcut is correct.

The verifier was independently inspected and rerun with

```text
python3 barriers/hc7_k7minus_nonfull_two_entrance_allocation_barrier_verify.py
```

and returned

```text
PASS K7-minus one-nonfull two-entrance allocation barrier
order=13 edges=48 boundary=FCdeG alpha_Nu=3 K4_Nu=no
cuts_le6=4096 connectivity=7 packing=(1,2)
x_boundary_contacts=4 x_F_entrances=2 defect2_allocations=0
chromatic_number=5 explicit_K7_model=yes
scope=violates K7-minus exclusion and seven-chromatic criticality
```

## Checks performed

1. The construction has exactly 48 edges.  Direct inspection of the edge
   builder agrees with every incidence in equations (1)--(2), including
   `N(u)=S union {x}`, the four `x`--`S` contacts, the two distinct
   `x`--`F` entrance edges, and the absence of every unlisted edge.  The
   graph6 encoder returns `FCdeG`; this code also occurs in the promoted
   exact list of 28 one-nonfull boundary types.
2. The exceptional neighbourhood `X=N(u)` has independence number exactly
   three and no literal `K_4`.  Deleting `N[u]` leaves exactly the two
   connected components `E={e_0,e_1}` and `F={a,b}`.  The first misses
   `x`, while the second is collectively adjacent to every vertex of `X`.
3. Removing `S` leaves exactly `E` and `F union {u,x}`.  In `E`, every
   `S`-full connected subgraph contains `e_0`, so its packing number is
   one.  On the rich side, `{u}` and `{a,b}` are disjoint `S`-full
   connected subgraphs.  Exhaustion of all nonempty connected vertex
   subsets confirms that no third one can be added, so the second packing
   number is exactly two.
4. The connectivity loop checks all
   `sum_{i=0}^6 binomial(13,i)=4096` deletion sets of order at most six,
   and its fixed-point connectivity routine is correct.  None disconnects
   the graph.  The seven neighbours of `x` form a separator by isolating
   `x`, hence `kappa(G)=7`.
5. The verifier exhausts every connected subgraph of the four-vertex rich
   side.  Every pair of disjoint full subgraphs uses `u` in one member and
   both `a,b` in the other; the only possible residual vertex is `x`, whose
   support has order four.  Equivalently, the exhaustive search finds zero
   pairs of disjoint full subgraphs with a third disjoint connected
   subgraph meeting at least five vertices of `S`.
6. The vertices `{s_0,s_3,s_4,e_0,e_1}` induce a literal `K_5`, giving the
   lower bound `chi(G)>=5`.  Every edge was checked against the displayed
   five-colouring, giving the matching upper bound and therefore
   `chi(G)=5`.
7. The seven displayed branch sets partition all 13 vertices.  Each is
   connected, and all 21 unordered pairs have an edge between them.  They
   therefore form an explicit `K_7`-minor model and, in particular, place
   the graph outside the `K_7^-`-minor-free hypothesis class.

## Scope and limitations

The example refutes only the stated static implication from connectivity,
packing, the exceptional boundary restrictions, and two entrance edges.
It is not seven-chromatic, not a contraction-critical host, and not
`K_7^-`-minor-free.  It therefore does not refute the live terminal
disjunction, the one-nonfull reduction under all hypotheses `(H)`, the
`K_7^-` six-colour conjecture, or `HC_7`.

No claim of minimum graph order is made or audited.  The verifier is a
complete check of this explicit 13-vertex witness, not an enumeration of all
possible one-nonfull hosts.
