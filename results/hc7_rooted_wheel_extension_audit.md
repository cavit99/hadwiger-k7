# Audit: extending four clique roots to a five-root wheel

**Source:** [the complete theorem and corollaries](hc7_rooted_wheel_extension.md).

**Exact source SHA-256:**
`f72e0b3d4254724a58f55b9445c0c173ea6c96e535416da47b1efc7fd5eb43b3`.

**Verdict:** GREEN — separate internal whole-source audit. No unresolved
mathematical gap was found in this revision. This is not external peer
review, a priority assessment or a claim that HC7 is complete.

## Scope and provenance

The reviewer, `universal_proof`, participated in the preliminary mandatory-path
and root-switch arguments. The parent assembled the standalone proof; this
audit separately read every line of the frozen draft and every line of the
final source, rather than relying on the earlier conceptual verdicts.

The initial draft had SHA-256
`93f80a565d6307608f31a632032cf2364c91b513a52d21da9fda13e9e7c01356`.
The review requested explicit treatment of the third port belonging to the
same bag in Section 3, and removal of X from A in Section 4's replacement
bags to avoid retaining the omitted terminal in two bags. The final source
contains both repairs. It also makes the contraction order and genuine
three-cut hypotheses explicit, strengthens the essentiality argument, and
specifies the chain endpoints and surviving-root qualifiers. The verdict
above applies to the final bytes, not to the unrepaired draft.

## Strongest inferences checked

- **Closed minimum-counterexample class.** The invariant is five distinct
  terminals together with some K4 model rooted at four of them. The omitted
  terminal may be used. Every selected contraction is terminal-legal,
  preserves three-connectivity, strictly decreases vertex order and has a
  fixed connected preimage. Changing the selected four roots is legitimate;
  it is never used to merge or discard two terminal labels.
- **Terminal triangle and essentiality.** The terminal kernel argument
  follows from the stated Wu input. Its six-vertex alternative with a
  universal terminal has a genuine two-cut. For an unused nonterminal,
  Wu's degree-three neighbours cannot be nonterminals or singleton selected
  bags; at most the two terminals of one bag remain, contradicting the
  required four neighbours.
- **Root-free components.** The boundary contraction and both ownership
  cases in Section 3 preserve every required contact. A mandatory p forces
  the w-component away from U; its putative remaining vertices would have
  actual boundary within {p,w}. The subsequent assignments certify every
  p-edge separately, which is enough for Wu's contradiction.
- **Mandatory chain in Section 4.** The prefix has boundary within
  {e,u,v} and meets both ports. If z is in that prefix, each surviving
  component still meets U, or {e,z} is an actual two-cut. The union X with
  the surviving U-component absorbs e,f, and also z when z belongs to X.
  Its boundary is therefore within {w,z}, or just {w}. Since w is not a
  selected root, every surviving selected root lies in that component.
  This justifies applying Section 3 to the other components. The
  mandatory-t case, bound of two nonterminals and all one-nonterminal
  contractions follow with the stated endpoint restrictions. In the final
  incomparable case, the bags use A-X and B-X, are disjoint, and exchange
  selected roots while retaining all outside contacts.
- **Root-incident closure.** Sections 5–6 need no theorem about a side
  carrying two selected roots. A cut through a selected root leaves a
  small side controlled by Sections 3–4. All two-terminal port cases give
  an actual legal contraction. A selected singleton obstruction must
  extend through its opposite port to realise three clique contacts.
  This forces the double-terminal bag and the displayed leaf structure.
  After switching its selected root, the final internal edge has neither
  a selected-root obstruction nor the omitted-root obstruction. The latter
  has two distinct neighbours in the other bag, which one remaining cut
  vertex cannot remove.
- **Universal colouring quantifiers.** Deleting a whole class from a fixed
  five-colouring gives an exactly four-chromatic graph whose retained set
  is colourful in every four-colouring. The fifth representative is
  distinct and reserved. In the edge-deletion corollary, the fresh-colour
  recolouring works for every five-colouring: the recoloured class members
  are independent and miss y. The resulting singleton x,y bags and five
  common-neighbour wheel bags give exactly K2 join W4 = K7-2K2.

## External inputs and limits

The only external input for the wheel-extension theorem is Wu's
contractible-edge statement, checked directly in the
[published abstract](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/contractible-elements-in-graphs-and-matroids/5556F945B4E534D2A8F017DE7E82BD5B).
The colourful-set corollary additionally uses Martinsson–Steiner
[Theorem 1.3 and its definition of a set-rooted minor](https://arxiv.org/html/2209.00594v1),
also inspected directly. It requires exactly four chromatic classes and
universal colourfulness, but does not prescribe the four representatives.

Finite searches informed the investigation but are not dependencies of
this proof or this verdict; this audit makes no new computational claim.
Neither a fixed topological K4 nor an arbitrary fan-to-bag allocation is
assumed. The proved application closes the stated
chi(G-{x,y})=5 branch. The alternative value six and the full C19, C21
and HC7 obligations remain outside the result.
