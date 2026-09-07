# Internal audit: two contractions with degree deficits

**Verdict: GREEN.** Theorem 1, Lemma 2 and Corollary 3 hold at the
revision below. This is a separate internal mathematical audit, not
external peer review or a proof of the global colouring conjectures.

**Audited source:** [two-edge contractions](hc7_companion_two_edge_contractions.md).

**Whole-source SHA-256:**
`fe0cd007483e61d5de4164a116c089f6c6842fd815c64ffeaa6ba4e58daa1b16`.

The audit is deductive, with no finite enumeration or fresh online input.

## Exact input

The [five-connected helper theorem](hc7_five_connected_helper_closure.md)
has SHA-256
`d68986c2c5228b322c8f1c93fff532d4c5f5b49009448a827ea7204fe5016513`.
Its [GREEN audit](hc7_five_connected_helper_closure_audit.md) has SHA-256
`b7b90f05d50c1b85c401265b46b3c14e51bbb8ec77c1beae481bcebdd7c3a3f1`.
Both hashes were checked. That input supplies exactly the integer
contrapositive used here; inherited primary literature was not reread.

## Strongest step: private neighbours pay for the deficits

Minimum degree seven with at most five degree-seven vertices gives total
deficit at most five and `q>=-2`. For a literal `K_5^-` in `F`, charging
its three universal vertices and subtracting five for all omitted
deficits gives `3(q+6)-5>2q`. Counting a charged deficient vertex again
would only weaken this valid bound.

If an endpoint of `uv` has no private neighbour, its closed neighbourhood
is contained in the other's. Contracting the edge is then precisely the
graph obtained by deleting that endpoint, up to renaming the survivor.
It cannot create a forbidden subgraph after the first part of the proof.
Therefore any contraction alleged to create a new `K_5^-` has at least
one private neighbour at each endpoint, giving `t>=2`.

The edge quotient is five-connected by an actual cut lift, and remains
`Q`-minor-free. Two universal vertices of its alleged `K_5^-` avoid the
merged vertex and represent distinct original vertices outside `u,v`.
The exact endpoint identity `d(u)+d(v)=2c+2+t` makes the four charged
surpluses at least `2q+4+t`. After allowing all five possible units of
deficit elsewhere, this is strictly above `2q`. Neither the endpoint
degrees nor the number of common neighbours is implicitly bounded.

## Degree-eight application and ownership

For Lemma 2, a diamond-free neighbourhood induces a matching and isolated
vertices. Degree seven gives four independent neighbours. At degree six,
the six neighbours must be a perfect matching; the eighth vertex must
meet every transversal. If no matched pair had both ends adjacent to it,
one could choose a missed end from each pair. Thus such a pair exists,
and with the degree-six vertex it gives a diamond. This proves the
claimed maximum-degree bound without enumeration.

In Corollary 3, the first contraction is six-connected, has at most five
unmerged degree-seven vertices, and its merged degree is at least nine.
It satisfies every hypothesis of Theorem 1. The second edge is arbitrary,
including an edge incident with the first merged vertex. The critical
independence bound is justified by the stated independent-star contraction:
on expansion the four independent neighbours share one colour and the
other four neighbours use at most four more, leaving a colour for `v`.

The two-step minor lift uses disjoint connected preimages: either two
disjoint original edges, or one connected original three-set. No original
vertex is assigned twice, and host order strictly decreases at each step.

## Remaining obligations

No gap was found. The final quotient is not asserted to have six-connectivity,
minimum degree seven, bounded total deficit or chromatic criticality.
Thus this establishes the stated second contraction, not arbitrary
iteration, a compatible global model, or completion of the global target.
