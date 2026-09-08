# Independent audit of the degree-eight cycle-and-triangle closure

**Verdict: GREEN.**

Date: 8 September 2026. This is a separate internal mathematical audit,
not external peer review. I independently read the complete final source
and attacked both the contact lemma and its structural application.

Audited source: [cycle-and-triangle closure](hc7_degree8_cycle_triangle_closure.md).
Whole-file SHA-256:
`791f0068e7b6907cf7414d9286477df68c7ad75661ac3c6b913897bee2469bfc`.

The theorem proves the entire stated cycle-and-triangle case for arbitrary
host order. Its hypotheses are seven-connectivity, minimum degree eight,
the specified degree-eight vertex, an induced five-cycle and disjoint
triangle in its neighbourhood, and at most one edge between them.
No chromatic-criticality hypothesis or finite enumeration is used.

## Strongest inferences

- **Three regions with preserved contacts.** In the split network a cut
  of capacity at most two uses only unit source arcs and vertices of `U`.
  Deleting their at most two corresponding original vertices leaves a
  source root and every vertex of `V`; three-connectivity gives a path
  between them. Hence a three-unit integral flow exists. Saturation of
  each source root's unit capacity prevents internal use of another root.
  Truncation at the first `V` vertex gives three disjoint seeds in `U`,
  even when their endpoints in `V` coincide. Greedy connected growth
  terminates by decreasing the number of unassigned vertices and retains
  each prescribed triangle root and each seed's contact with `V`.
- **Donation preserves both sides.** If a region has no private cycle
  root, the other two regions still contact all four roots and remain
  connected through their literal triangle edge. The donated region
  meets `V`, so the enlarged helper is connected and remains full.
  Triangle roots then lie in both helpers, giving the first terminal model.
- **The remaining contact assembly.** Private roots for distinct regions
  are distinct. Assigning the fourth root gives multiplicities `2,1,1`.
  The singly labelled vertex `b` has a cycle neighbour labelled `Ua`.
  After their edge is merged, `X,c,d` form a triangle. The five bags
  `X,d,Ua,Ub,Uc+c` have all nine stated contacts; only `d--Ub` is
  undetermined. Both `V` and the added `v` contact all five bags. Their
  own possible missing contact is disjoint from `d--Ub`. Each merger
  uses a specified edge, and no original vertex is owned by two bags.
- **Density and connectivity in the application.** Nonnegative degree
  excess gives `2c-14<=2q`. The simple edge contraction removes exactly
  `c+1` edges and reduces the surviving degree of `v` to seven. Thus
  `e(F)=4|F|+q-c>=4|F|-7`. A cut containing the merged vertex lifts by
  replacing it with `x,y` and adding `v`; otherwise add only `v` and keep
  the connected preimage `xy` on its surviving side. Both lifts contradict
  seven-connectivity, establishing five-connectivity of `F`.

## Exact inputs and lift

The three-connectivity source and both of its adjacent GREEN audits pin
`4e2b5b0b7b7294c30bdcdd1b4f147d12ba535dc3513508981160c5173d519228`.
Its structural hypotheses hold under the temporary assumption that `G`
has no `Q` minor. The spanning-helper source matches its GREEN audit at
`0c1ac8052f7734d8d0267381c030e177bd70010eded63d15fdca8c0db6d1f375`.
These source hashes were checked. The exact four-root density hypothesis
and adjacent helpers agree with the freshly inspected primary
[Norin--Totschnig Lemma 12](https://arxiv.org/html/2507.03244v1#S2).
Five-connectivity licenses the singleton-root, spanning-helper normalization.

Deleting the four cycle images leaves exactly `G-v-C`, so the imported
three-connectivity applies to the graph used by the contact lemma.
The sole nonsingleton preimage is the fixed connected pair `{x,y}`.
All later disjoint unions and contacts lift through it to the original
host. No root, colouring condition or ownership is discarded in that lift;
no quotient induction is asserted.

## Remaining scope

No substantive gap was found. The cycle-and-triangle case is closed under
the theorem's exact hypotheses. The two-triangles-and-edge case and the
global companion and Hadwiger conjectures remain unresolved; this proof
does not by itself achieve the user's global completion criterion.
