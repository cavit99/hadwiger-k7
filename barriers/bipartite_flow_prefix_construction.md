# Counterexamples to a bipartite-flow prefix construction

**Status:** written proof; barrier/counterexample to intermediate claims.
Separate internal audit forthcoming.
These examples refute two intermediate lemmas under the intended
independent-intersection definition specified below. They do **not**
refute the intended main minor statement or bipartite contractibility.

## Source and precise construction

The source checked is Biswal--Lee--Rao,
[*Eigenvalue bounds, spectral partitioning, and metrical deformations via
flows*, arXiv:0808.0148v2](https://arxiv.org/pdf/0808.0148v2),
9 August 2008, Section 2, pp. 6--7, and Lemmas 3.2--3.6, pp. 9--10.
The final published version was also checked: *Journal of the ACM* 57(3)
(2010), Article 13, [DOI 10.1145/1706591.1706593](https://doi.org/10.1145/1706591.1706593),
pp. 13:10--13:11. Its publisher PDF has SHA256
`486fffa16995ab4ad9a323dd9adb60775bdfa3b6607e6e0cd0dc8abc9a9b54ad`.
The prefix definitions and the same defective arguments for Lemmas 3.5
and 3.6 occur on p. 13:11.

There is an essential qualification when comparing the versions. The
published definition on p. 13:10 counts demand-independent paths that
are **vertex-disjoint**, whereas the preprint counts those that intersect.
The subsequent proof uses the latter meaning. After correcting that
apparent typographical reversal to the preprint's definition, the two
counterexamples below apply unchanged to the published prefix argument.
Our examples do not satisfy `inter=0` under the literal published wording.
The substantive finding here is the prefix-construction failure even
under the intended definition; it does not depend on that apparent typo.

An integral unit `H`-flow selects one path `P_uv` for every edge `uv` of
the demand graph `H`, whose vertices are injected into the host graph as
terminals. Its independent-intersection count is zero when paths for
edges with four distinct ends are vertex-disjoint. Lemma 3.2 states that
such a flow has an `H` minor when `H` is bipartite of minimum degree two.

For a bipartition `L,R`, put `V_v=union_{w in N_H(v)} V(P_vw)`.
For `a in L`, orient every `P_ab` from `a` to `b`. Let `hat P_ab` be the
prefix strictly before its first vertex in `union_{a' in L-{a}} V_a'`.
The proposed branch sets are

`C_a=union_b hat P_ab` and `C_b=V_b-union_{a in L} C_a`.

The following two assertions about these sets are false:

1. Lemma 3.5: `V(P_ab)-hat P_ab` is contained in `C_b`.
2. Lemma 3.6: for distinct neighbours `b,c` of `a`,
   `V(P_ab) intersect V(P_ac)` is contained in `C_a`.

## Seven-vertex counterexample to Lemma 3.5

**Proposition.** There is an integral unit `C_4`-flow with zero independent
intersections for which the proposed `C_b` is disconnected and the
assertion of Lemma 3.5 fails.

**Proof.** Take `H=K_{2,2}`, with roots `a_0,a_1,b_0,b_1`. Add distinct
vertices `x,y_0,y_1`. For `i in {0,1}`, take the paths

`P_i0 = a_i x y_i b_0`, and `P_i1 = a_i y_i b_1`.

The host consists exactly of these paths. Each path is simple, contains
no other root, and each pair with four distinct ends is disjoint. Thus
these paths give the required flow (and an ordinary `H`-scheme).
The first foreign left-star vertex on `P_i0` is `x`; on `P_i1` it is
`b_1`. Consequently the construction returns

`C_ai={a_i,y_i}`, `C_b0={x,b_0}`, and `C_b1={b_1}`.

There is no edge `xb_0`, so `C_b0` is disconnected. Also `y_i` belongs
to `P_i0-hat P_i0` but not to `C_b0`, refuting Lemma 3.5. Nevertheless,
the sets `{a_i,y_i}` for `a_i` and `{b_j}` for `b_j` give a rooted
`K_{2,2}` minor; `x` is unused. This proves the proposition. QED.

The first unsupported inference is in the first sentence of the proof
of Lemma 3.5: it excludes a suffix vertex from the **same** left branch
set. A vertex past the stopping point of one path may still lie in a
different prefix from the same left root. Here `y_i` does exactly that.

## Eight-vertex coloured counterexample to Lemma 3.6

**Proposition.** There is a coloured `C_4`-scheme with zero independent
intersections for which Lemma 3.6 fails and the proposed right branch
sets overlap.

**Proof.** Add to the same four roots distinct vertices `a'_0,a'_1,b'_0,b'_1`.
For every `i,j in {0,1}`, take

`P_ij = a_i b'_j a'_i b_j`.

Give `a_i,a'_i` colour `a_i`, and `b_j,b'_j` colour `b_j`. Colours
alternate properly on the paths, each nonroot has degree four and lies
on exactly two paths, and paths with four distinct ends are disjoint.
The paths therefore form a coloured scheme. Each prefix stops before
`b'_j`, since that vertex also lies on `P_(1-i)j`. Thus

`C_ai={a_i}`, and `C_bj={b_j,b'_j,a'_0,a'_1}`.

Both paths from `a_i` contain `a'_i`, which is outside `C_ai`.
Moreover, `C_b0 intersect C_b1={a'_0,a'_1}`, so the proposed sets are
not disjoint. An actual rooted model is

`D_ai={a_i}`, `D_b0={b_0,b'_0,a'_0}`, `D_b1={b_1,b'_1,a'_1}`.

Each right branch is a path, and every left root is adjacent to each
right branch at `b'_j`. This proves the proposition. QED.

The unsupported inference in Lemma 3.6 is that a vertex outside `C_a`
must belong to another left star `V_a'`. Its prefix may have stopped at
an earlier vertex of another star. In this example `a'_i` belongs only
to the left star `V_ai`, although the earlier `b'_j` stops its prefix.

## Scope and smallest useful repair

For every coloured bipartite scheme with minimum target degree two,
this construction actually leaves **all** left roots singleton. The
first vertex after a left root is either a right root on at least two
paths, or a nonroot of right colour on at least two paths. In either
case it belongs to another left star, so every prefix is just its root.
Any nonroot of left colour therefore contradicts Lemma 3.6.

These examples establish failures of the displayed construction and its
intermediate assertions, not failure of the intended existence statement
in Lemma 3.2, as stated in the preprint. Both examples have explicitly
certified rooted minors.
The [independent singleton-shore barrier](bipartite_scheme_singleton_shore_barrier.md)
also rules out repairing the universal argument merely by choosing the
opposite singleton shore. A useful repair needs a construction allowing
both shores to expand, or a global rerouting or rooted reduction with
proved preservation and lifting. Neither repair is supplied here.

## Deterministic certificate check

Run

```sh
uv run python3 active/experiments/bipartite_contractibility/flow_prefix_counterexample.py
```

The [verifier](../active/experiments/bipartite_contractibility/flow_prefix_counterexample.py)
prints both path systems, the computed prefixes and branch sets, exact
failures, and valid rooted models. It checks independent intersections,
the common-endpoint scheme condition, root preservation, and the coloured
conditions for the second example. Expected output is two JSON records
with `verified: true`. These are explicit finite certificates; the written
proofs above do not depend on exhaustive search.
