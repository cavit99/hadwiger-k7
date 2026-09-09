# Audit of the degree-six four-boundary side counterexample

**Verdict: GREEN — separate cold whole-source internal audit.**
The [counterexample](hc7_degree_six_four_boundary_side.md) was read at
SHA-256 `f2f5dc47472ee40653928ebe51480ae353919abe8ecfa489057a21036d70a523`.
No gap or correction was found. This is internal review, not external
peer review or completion of C19 or HC7.

## Provenance and checks

Literature-repair supplied the construction and source. This reviewer
did not develop it and independently checked every argument in the
frozen source. No computation or external structural theorem is needed;
the following checks are direct from its vertex and edge lists.

1. **The attachment and counts are exact.** The listed two pentagons,
   cross-edges and poles triangulate a cylinder with its two caps; each
   vertex of P has degree five and `c,u0,u1` is a facial triangle.
   The three cases for deleting at most two vertices prove connectivity:
   two surviving poles are joined by a surviving cross-edge; with one
   pole deleted, each relevant vertex retains a cross-neighbour; with
   both deleted, the intact rings remain joined. Coning gives a
   four-connected H. The union identifies exactly K4 and has sixteen
   vertices and `42+13-6=49` edges. The stated degrees, including eight
   at p,q and six at all nine new vertices, agree with the edge list.

2. **Every nonroot subset has the asserted boundary.** For a subset
   meeting p or q, its G0-boundary contains five distinct vertices outside
   the whole subset; this also holds when both p,q are included. A subset
   of E leaves all four K vertices outside. If its H-boundary had order
   at most three, a surviving K vertex would witness disconnection,
   contradicting four-connectivity. Directly, `N(E)=K` and `N(D)=S`.

3. **The seven-vertex rooted obstruction covers all allocations.** A
   singleton helper needs p,q in distinct triangle bags to contact two
   of them. This leaves both helpers singleton and missing the third
   triangle bag. Otherwise both helpers must absorb one nonroot, leaving
   the distinct omissions at r and s. Unused vertices or assigning both
   nonroots to one helper cannot evade the singleton argument.

4. **Repeated attachment excursions do not invalidate projection.**
   Every rooted bag retains its actual root in G0 after deleting E.
   Each component of a disconnected remainder owns a K port, since any
   lost connecting path entered E through K. The clique on the ports
   owned by that same bag reconnects all its pieces. Each bag using E
   owns a port; two distinct such bags own distinct ports. Consequently
   any lost interbag contact is restored by a literal clique edge.
   No vertex is reassigned between bags and all five roots stay separate.

5. **Q-freeness holds for every model.** Q is five-connected and each
   vertex deletion leaves thirteen or fourteen edges on six vertices,
   so Q is nonapex. The cone H therefore excludes Q: deleting its
   apex-owning model bag leaves a minor of planar P. G0 excludes Q by
   its order and edge count. In the clique sum, at most four model bags
   meet K. The remaining vertices of Q induce a nonempty connected
   graph, forcing their bags onto one side. Restrict the K-meeting bags
   to that side and K; their own clique ports reconnect them and restore
   contacts. Contacts with bags avoiding K already lie on the retained
   side. This projects the whole Q model into an impossible summand.

The example refutes the stated relative-four, nonroot-degree-six,
Q-free five-root packet. It does not retain the seven-connected,
minimum-degree-eight, seven-chromatic critical host. Neither the stronger
relative-five packet nor an application using additional actual-host
constraints is refuted.

The source status line and audit link were updated after review; its
mathematical body is unchanged from the draft at SHA-256
`46ee32d6cdda36a8f4dddfcc78a5d716b1b2f5a16075c81153745ed34b990b73`. The current source hash includes that editorial change.
