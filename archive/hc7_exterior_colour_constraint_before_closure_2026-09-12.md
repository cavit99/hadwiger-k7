# Exterior colouring constraint before complete branch closure

**Status:** frozen historical deduction, superseded by the
[exterior colour bound](../results/hc7_two_triangle_exterior_colour_bound.md).
This is not current status; consult [the ledger](../RESEARCH_LEDGER.md).

Preserved from the exterior-colouring block in
`active/hc7_k44_closure_frontier.md` at Git `9b8ab67`.
That complete source has SHA-256
`8bce5d2db2b3ed48088126af808d752ba6f0e0068d5ca46ebd134e8f8a7515d2`.
Its separate integration audit is preserved in the
[current frontier audit](../active/hc7_k44_critical_global_construction_audit.md#full-contact-responses-full-neighbourhood-marks-and-exterior-colouring).
The relative result link has the same target from this directory.
Only the final blank line is omitted.

**Exterior colouring constraint; written deduction.** In the actual host,
`chi(W)>=4`. To see that `G[N(v)]` is three-colourable, colour x,y with
1,2. C4-freeness leaves at most one vertex of each triangle adjacent to
`{x,y}`, and at most one A--B edge. Colour each triangle with 1,2,3,
initially assigning 3 to its attachment vertex. Permute the other colours
to satisfy the A--B edge unless it joins both attachment vertices. In
that case one attachment misses x or y: if both met both, they would
form a C4 with x,y. Give that attachment the colour of the missed vertex
and complete its triangle. This is the required three-colouring.
A three-colouring of W with a separate palette would now six-colour G,
giving v any W colour, a contradiction.

If `chi(W)=4`, more is forced. For every three-colouring of `G[N(v)]`
and every one of its colour classes U, `N_W(U)` meets every colour class
of every four-colouring of W. Otherwise reuse a missed W colour on U,
give the other two neighbourhood classes two fresh colours, and colour
v with a different W colour. This again six-colours G. Each neighbourhood
colouring has class sizes `3,3,2`, since each triangle uses all three
colours and x,y have different colours. Martinsson--Steiner Theorem 1.3,
as pinned in the [colourful-set source](../results/colourful_five_wheel.md),
therefore gives a K4 in W with every bag contacting U. For a pair class
`U={a,b}`, a bag may contact only a or only b; neither their distribution
nor the other classes' contacts to these same bags is prescribed.
The simultaneous construction and the `chi(W)>4` case remain open.
