# Internal audit: four-cycle exclusion at degree eight

**Verdict: GREEN.** The theorem, Lemma 1 and Corollary 2 hold below.
This is a separate internal mathematical audit, not external peer review
or a proof of Conjecture 19, Conjecture 21 or `HC_7`.

**Audited source:** [four-cycle exclusion](hc7_degree8_neighbourhood_four_cycle_exclusion.md).

**Whole-source SHA-256:**
`a0be7837d03dffd565313c8f29faf20226f5b116ec053ee8a82f27fd83865d10`.

## Inputs and scope

The three source hashes in Section 1 were checked against the actual files
and the revisions pinned by their adjacent GREEN audits:

- Connected-set contraction closure:
  `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`.
- Degree-seven rooted-helper closure:
  `6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67`.
- Spanning-helper construction:
  `0c1ac8052f7734d8d0267381c030e177bd70010eded63d15fdca8c0db6d1f375`.

Their exact connected-triple conclusion, density threshold and
five-connectivity hypothesis apply. The primary Norin--Totschnig text was
not freshly inspected for this audit. No finite census is used.

## Strongest inference checks

1. Contracting a connected set of at most three neighbourhood vertices
   leaves the untouched `v` adjacent to every quotient neighbourhood
   vertex. A diamond there would therefore be a forbidden literal
   `K_5^-` in the actual quotient. No quotient criticality is assumed.
2. For Lemma 1, `F=G-{v,z}` is five-connected and
   `e(F)=4|G|+q-7-d(z)>=4|F|-9` when `d(z)<=q+10`.
   The absence of the rim diagonal `zb` makes the extra common neighbours
   `x,y` distinct from `a,b,c`. Both helper inputs apply to four distinct
   roots; their spanning conclusion places `y` in one helper.
3. The seven displayed bags are actual disjoint connected sets. The edge
   from `x` to `U` connects the enlarged bag. The literal edges through
   `x,y` retain both endpoint-to-helper contacts, and the old helpers
   retain every contact to `a,b,c`. The only possible omitted pairs are
   `ac` and `zb`, with disjoint ends. No large helper is deleted, and no
   stronger five-rooted intermediate model is asserted.
4. An outside vertex with two adjacent rim contacts gives a diamond upon
   contracting the opposite rim edge; opposite contacts give `K_{2,3}`
   and then a diamond. Thus the attachment classes and `O` exhaust all
   possibilities. The two opposite, independent rim vertices force each
   stated parity union to be a clique. Opposite nonempty classes create
   a rim diagonal through the specified connected-triple contraction.
5. If `|O|>=2`, two members are adjacent to both remaining vertices of
   `X`, giving a diamond. If `|O|=1`, the forced repeated attachment class
   gives a diamond with its rim vertex. With `O` empty, each class has
   order at most two, so exactly two adjacent classes have order two.
   This argument covers all four outside vertices without enumeration.
6. The two distinct rim vertices consequently have local degree four.
   Lemma 1 forces each original degree to be at least `q+11`. Their
   surplus is at least `2q+6`, exceeding the total `2q`; all omitted
   terms are nonnegative by the original minimum-degree hypothesis.

## Spanning configurations

The additional triangle source and its GREEN audit match
`907384c665975c47f7850ee49da2d7f389802b077837c4285a3f00a81f5ef824`.
The corollary splits on two disjoint triangles, not on a unique triangle.
With two disjoint triangles and no remaining edge, the independent-set
condition forces the two singleton missed sets and their cross-edge.
The displayed connected-triple contraction then has all five diamond
contacts. This proves the first spanning configuration.

Otherwise `H-T` is triangle-free. An independent triple there must carry
all three labels. An unlabelled remaining vertex either extends an
independent pair with the omitted triangle root or gives a forbidden
two-edge path. Each labelled remaining vertex must meet its same-label
triple member; distinct labels then yield two disjoint triangles, while
equal labels yield a diamond. Thus `H-T` has independence number two and
is `C_5`. Distinct nonzero labels on this cycle are ruled out at distance
at most two. Two equal-label contacts either give a four-cycle or the
diamond obtained by contracting the other arc's three internal vertices.
Consequently the cycle and triangle have at most one cross-edge.

## Remaining obligations

No gap was found in these deductions. They leave two possible spanning
configurations, allowing the stated extra edges; neither is asserted to
occur in a critical counterexample. A global companion-minor construction
and the simultaneous root/helper allocation remain unresolved.
