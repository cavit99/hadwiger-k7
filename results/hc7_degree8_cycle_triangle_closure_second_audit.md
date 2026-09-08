# Second independent audit of the cycle-and-triangle closure

Date: 8 September 2026.

**Verdict: GREEN — written proof under the stated hypotheses.**

This audit pins [the complete source](hc7_degree8_cycle_triangle_closure.md)
at SHA-256:

    791f0068e7b6907cf7414d9286477df68c7ad75661ac3c6b913897bee2469bfc

I independently read the entire exact source and checked its two pinned
direct inputs against disk. I also checked the contact construction before
the full source was written; the verdict here concerns the complete source,
including its imported hypotheses and application. No source edit was made.

## Strongest inferences checked

- **Exact hypothesis transfer.** Assuming absence of \(Q\), the stated
  seven-connectivity, minimum degree eight and degree-eight neighbourhood
  satisfy the cycle-complement three-connectivity theorem. It supplies
  three-connectivity of the required graph \(G-v-C\), rather than of the
  different complement \(G-v-A\). No chromatic hypothesis is imported.
- **Common-neighbour and density counts.** With \(q=e(G)-4n\), all degree
  excesses are nonnegative. For a cycle edge \(xy\) with \(c\) common
  neighbours, \(d(x),d(y)\ge c+1\), hence \(2q\ge2c-14\).
  Contraction loses exactly \(c+1\) edges, and the subsequent deletion of
  \(v\) loses seven. Thus \(e(F)=4|F|+q-c\ge4|F|-7\), exceeding the
  rooted-helper threshold.
- **Quotient connectivity.** A cut of order at most four in \(F\) lifts,
  after restoring \(v\) and expanding a deleted contracted root to
  \(\{x,y\}\), to an actual cut of order at most six in \(G\).
  When the contracted root survives, its connected expansion remains in
  its one surviving component. The order condition is also satisfied:
  \(|G|\ge9\) and \(|F|\ge7\). Five-connectivity and therefore the required
  internal four-connectivity follow.
- **Rooted-helper inputs.** Norin--Totschnig Lemma 12 is used in its
  retained exact form: absence of the four-root two-helper model in an
  internally four-connected pair gives \(e(F)\le4|F|-10\).
  Lemma 3 of the pinned helper source applies in five-connectivity and
  makes the roots singleton and the helpers a partition of \(F-Z\).
  I rechecked its finite optimization and actual four-vertex boundary
  argument; no root-root contact is needed during that optimization.
- **Three simultaneous seeds.** A cut of capacity at most two in the
  displayed network can delete only source arcs and U-vertex capacities.
  These deletions leave an A root connected to V in the three-connected
  graph \(J\). A full integral flow saturates the three source arcs and
  prevents internal traversal of another source root. Truncating at first
  entry to V gives disjoint U-seeds even when their V endpoints coincide.
  The proof does not require three distinct vertices of V.
- **Connected partition and private contacts.** Greedy extension preserves
  each seed and terminates with a connected partition of U. The original
  A triangle supplies all three inter-region contacts. A region with no
  private root can be donated while both resulting helpers remain full
  to Z, connected, adjacent and meeting A. Otherwise three distinct
  private roots force the exhaustive four-root label pattern \(2,1,1\).
  The singly labelled vertex \(b\) necessarily has a cycle neighbour
  with the repeated label.
- **All seven final bags.** The five bags \(X,\{d\},U_a,U_b,Y\) retain
  nine of their ten contacts: three from the contracted cycle, three
  from the selected labels and three from the A triangle. Both V and
  \(\{v\}\) contact each of those five bags. Thus, among all 21 pairs,
  only \(dU_b\) and \(vV\) can be absent, and those pairs are independent.
  All seven bags are connected and disjoint. Replacing the unique
  contracted-root occurrence by its fixed preimage \(\{x,y\}\) preserves
  every contact and the complete ownership partition.

## Inputs and scope

The exact direct-input hashes checked were:

- [Cycle-complement three-connectivity](../results/hc7_cycle_triangle_complement_three_connectivity.md):
  4e2b5b0b7b7294c30bdcdd1b4f147d12ba535dc3513508981160c5173d519228.
- [Spanning helpers, Lemma 3](../active/hc7_companion_helper_construction.md):
  0c1ac8052f7734d8d0267381c030e177bd70010eded63d15fdca8c0db6d1f375.

Their underlying written results and the explicitly stated external rooted
bound remain dependencies. No finite computation is a mathematical premise.
No substantive correction or unresolved inference was found in this source.

This is separate internal review, not external peer review. The theorem
closes the entire stated cycle-and-triangle neighbourhood case at arbitrary
host order. It does not close the two-triangles-and-edge case or establish
Conjecture 19, Conjecture 21, HC7, or the user's full completion criterion.
