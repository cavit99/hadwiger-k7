# Audit: a wheel on all five roots of a K5-scheme

**Date:** 9 September 2026.

**Verdict:** GREEN — separate whole-source internal review of
[the proof](k5_scheme_rooted_wheel.md), SHA-256
`523b649c85eeb5de453cda24340beb72cf58932a39f531c79e14621b208ac9d9`.

The reviewer participated in developing the changed induction argument
before separately reading these complete source bytes. This is an internal
mathematical audit, not external peer review or a novelty assessment.

## Strongest checks

- Normalisation contracts disjoint monochromatic components, each containing
  at most one original root. Every retained demand still uses its two endpoint
  colours; a foreign root cannot enter its image. The single-demand cleanup
  likewise preserves all five distinct roots and strictly decreases order.
- The minimum counterexample is to the **unlabelled rooted wheel** conclusion.
  No minimum-K5-counterexample theorem is silently applied. The root-free and
  one-root arguments exclude those sides of cuts of order at most two. The
  host is connected because it is the union of the ten root-to-root paths.
- At a two-cut, the exterior has exactly roots a,b and ports of those colours.
  The two differently coloured prefix seeds are disjoint and can be grown to
  a connected partition of the exterior plus both ports. Each contracted part
  owns exactly its original root. The six cross-demands have unique ports and
  untouched outside suffixes; the other three demands remain outside, and ab
  is supplied by the contact between the two parts. Thus a smaller full scheme
  is obtained, and **every** returned rooted wheel lifts through fixed preimages.
  This establishes three-connectivity for the changed induction predicate.
- The six demands on four roots give precisely a rooted K4-scheme, avoiding
  the fifth root. K4 contractibility and the stated three-connected wheel
  theorem therefore apply without prescribing the wheel's hub or rim order.
- In the corollary, the wheel avoids the whole independent class I and v.
  A complementary component containing T contacts each bag through its named
  root, and also contacts v. Adding that component and v gives exactly the
  required K2 join W4 model. The existence of the component is not asserted.

All six local input source/audit hashes in the proof match the files on disk.
The KPR primary statement and proof inspection was performed by the source
author; this audit checked its four-root application. No unresolved gap was
found in the deduction from those inputs. Labelled W4 contractibility, rooted
K5 contractibility, C19 and HC7 remain outside the proved conclusion.
