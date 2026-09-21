# Audit: degree-seven interior-edge recolouring

**Verdict: GREEN — separate internal audit of the stated conditional
normalizations.** This is not external peer review and does not establish
the degree-seven case or HC7.

## Audited source and scope

The audited source is
[the working proof](hc7_degree7_colour_repair_working.md), with SHA-256

```text
37881e15f59234d46312aa77835437a32de46da88d6622d7ad7ce7d68f40c4ec
```

This audit checks Propositions 2.1, 3.1 and 4.1, Corollary 3.2, and the
stated limits of their conclusions. The source was read and its hash
checked on 21 September 2026. The audit assumes the original host
hypotheses and the established boundary-language inputs stated in
Section 1; it does not independently reaudit their complete dependency
chain. No computation or external literature is required for the audited
deductions.

The final pin incorporates only the audit-status link and the more precise
Section 3 heading. Reversing those two textual edits reproduces the
originally audited source hash; the mathematics is unchanged.

## Inference checks

1. **Exceptional connections and the exact reverse operation.** Swapping
   the component of one endpoint in `A-h` makes the endpoint colours
   different and therefore restores `h`. Every resulting colouring of
   `A` uses six boundary colours. A component interchange introduces at
   most one new boundary colour, so the initial response must have five.
   Increasing five to six requires splitting a repeated pair between the
   unique missing colour and its old colour. Applying the same argument
   to the other endpoint component puts one pair member in each component.
   This also covers the case in which the endpoint colour is the old
   repeated-pair colour, rather than the missing colour. The vertex `u`
   joins precisely these two components, since its two neighbours in the
   layer are the pair members. Restoring `h` after the interchange joins
   exactly the two old components, making it a separating edge of the
   asserted full bichromatic component. The bounds on `q` follow.

2. **Proposition 3.1: one interchange gives all five internal connections.**
   The singleton-colour endpoint connection is internal by Proposition
   2.1. Since `u` has only that singleton root as a neighbour in the
   relevant layer, the hypothesis that the root misses the endpoint
   component places `u` in a different component as well. Interchanging
   this other component preserves properness on the original `G-h` and
   leaves both endpoint colours equal to `delta`. On the boundary, only
   the singleton root changes; both repeated pairs remain intact. The
   new colour of `u` is `i`, so every other endpoint layer omits `u` and
   its globally forced connection lies in `A-h`. The `delta-i` endpoint
   component is unchanged. As an independent check of the last inference,
   `delta` is now a singleton boundary colour, which directly gives
   `q=0` by Proposition 2.1.

3. **Corollary 3.2: minimization over the complete response family.** Fixing
   a labelled six-colour palette makes this family finite; it is nonempty
   by proper-minor colourability. Proposition 2.1 gives `0<=q<=2` and
   the stated possible locations of the endpoint colour. When that
   colour is missing and `q>0`, any singleton root outside its endpoint
   component would invoke Proposition 3.1 and contradict minimality.
   This comparison concerns actual colourings of one fixed graph. It
   does not require the family to lie in a single Kempe component.

4. **Proposition 4.1: the missing-colour move.** The endpoint colour is
   different from both interchanged colours, so both endpoints retain
   it. The component containing `u` contains the nominated singleton
   root. Exactly that root changes on `S`, leaving five boundary colours
   and the same two repeated pairs. Applying Proposition 2.1 to this
   new response gives precisely the stated possible exception; its
   persistence is not assumed.

## Unresolved construction

No gap was found in these conditional deductions. They do not prove that
a response with `q=0` admits an edge repair: all five internal paths may
share vertices of the endpoint colour. Nor do the exceptional component
systems supply disjoint connected branch sets with the required boundary
contacts. Repeated missing-colour moves have no established strictly
decreasing parameter when the exception persists.

The remaining obligation is therefore still a `K7` model or a proper
six-colouring restoring `h` with at most five colours on `S`. The audited
source supplies neither and expressly records this nonclosure. No
criticality is transferred to a quotient, and no counterexample to the
degree-seven target is claimed.
