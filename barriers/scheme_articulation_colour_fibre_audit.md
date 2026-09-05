# GREEN: independent audit of the two separation-transport barriers

**Status:** separate internal mathematical audit, 5 September 2026.
This is an internal agent audit, not external peer review.

**Audited source:** [the two explicit constructions](scheme_articulation_colour_fibre.md),
whole-file SHA-256
`e2fa53c70d73be7a912d007d5c6524804b6e37e154958db89bb295cdc8034594`.

**Verdict: GREEN.**

No unresolved assumption or mathematical gap was
found in either stated counterexample. Each received a check from an
agent other than its author: `route_assessment` checked the attachment
construction, and `universal_proof` checked the Whitney-transport
construction. This note records those reciprocal independent checks.
Neither construction disproves the current classification candidate.

## Attachment colour: the strongest ownership inference

The host is exactly the union of the four displayed paths. Its nine
vertices comprise the four distinct prescribed roots and five nonroots.
Every path is simple and root-free internally. The colours alternate
between the demanded endpoints, and all paths containing any fixed
vertex have its colour as a common endpoint. Thus the condition on
every collection of intersecting paths holds, not merely the condition
on pairs.

The critical neighbour sets are exactly

```text
N(v_1)={a_1,a},   N(v_2)={c_1,c},   N(b)={a_1,c_1}.
```

In any proposed model, `C_v` already contains root `v`. If it contains
`v_1`, a path within `C_v` from `v_1` to `v` must start through `a_1`:
the other neighbour `a` belongs to a different prescribed branch set.
Likewise, including `v_2` forces `c_1` into `C_v`. This reasoning allows
arbitrary connected branch sets; it does not assume induced sets,
small sets, or a particular choice of connecting paths.

After both forced inclusions, root `b` has no neighbour outside `C_v`.
Every path starting at `b` inside its disjoint branch set would need
such a neighbour. Hence `C_b={b}`, with no contact to `C_a` or `C_c`.
Those contacts are required, so the strengthened conclusion is false.
Unused vertices or larger branch sets cannot repair this obstruction.

The ordinary model in the source checks directly. The nontrivial bags
are the paths `a,v_1,a_1` and `c,v_2,c_1`; the other bags are singleton
roots. Their four required contacts are the listed actual host edges,
and all bags are disjoint and preserve their prescribed roots.

The two nonroots of colour `v` have degree two in this block host.
This is allowed by the exact refuted statement, which assumes a
properly coloured scheme but does not impose the stronger minimum
nonroot degree condition of a normalized coloured scheme. The source
does not claim to exhibit an extension to another target block. A
prior normalization or global gluing argument would still have to
preserve the data needed by the surrounding scheme; this example
does not rule out such a valid argument.

## Whitney switch: incidence incompatibility before any model lift

The two stated sides meet exactly at `u,v`. Swapping those endpoints
on the second side changes `vc,cd,du` to `uc,cd,dv` and leaves
`ua,ab,bv` fixed, so both targets are the displayed six-cycles.

The canonical length-three paths form a valid original scheme:
each nonroot `x_1` belongs only to paths demanded by edges incident
with `x`, and no prescribed root is internal. In particular, `u_1`
belongs to both paths displayed in the source. Under the proposed
one-sided demand relabelling, those paths would represent `ua` and
`dv`. Their endpoint sets are disjoint. Therefore they cannot retain
the common nonroot in any scheme of the switched target. This is
independent of both recolouring and the separate endpoint-reconnection
problem; neither can change the empty intersection of demanded
endpoint sets.

The claim is restricted to this incidence-preserving transport rule.
It does not assert that every possible rerouting fails, nor that
contractibility changes under a Whitney switch. The primary
[Kündgen--Pelsmajer--Ramamurthi paper](https://arxiv.org/html/1207.6141),
Theorem 4.2, was checked for the statement that every cycle is
contractible, which verifies the source's scope distinction here.

## Remaining obligations outside the verdict

The attachment example leaves open coordinated ownership of shared
colour vertices across blocks. The Whitney example leaves open a
different transport that changes path incidences and has a valid
root-preserving lift. Splitting a shared host vertex does not by
itself provide that lift: compatibility of the branch sets assigned
to its copies remains to be proved. No claim that an arbitrary
returned model is liftable is made in the audited source.

These are direct explicit counterexamples, not inductive reductions.
No decreasing parameter or computational search bound is assumed.
Neither full classification sufficiency nor Hadwiger's conjecture is
established by them.
