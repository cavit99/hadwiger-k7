# Internal audit: feedback-boundary rooted-model barrier

**Verdict:** GREEN.  The displayed graph refutes exactly the stated
boundary-only two-set-transversal claim, and its exterior augmentation has
the asserted explicit `K_7^-` model.  This is a separate internal
mathematical audit, not external peer review.

## Exact revision

The audited source is
[`hc7_feedback_boundary_rooted_k5_transversal_barrier.md`](hc7_feedback_boundary_rooted_k5_transversal_barrier.md),
with SHA-256

```text
4fb8f0a7480181b386ed5a99d914003cd2f23994f8bc31e26f9e36edc57fd4a8
```

## Construction and hypotheses

For `Q=(K_2 vee C_5) dot-union K_1`, the join component has chromatic
number `2+3=5` and clique number `2+2=4`; adjoining an isolated vertex
changes neither.  Thus `Q` has order eight, is five-chromatic and has no
literal `K_5`.  The sets obtained by omitting one of the two universal
vertices each have order seven.

## Forced singleton bags

The isolated vertex cannot lie in any branch set of a `K_5` model.  If one
universal vertex, say `p`, were absent, at most one branch set could contain
the other universal vertex `q`.  Removing that branch set would leave four
pairwise adjacent connected branch sets inside `C_5`, a `K_4` minor of a
cycle, which is impossible.  Hence both `p,q` occur.

They cannot occur in one branch set, for then the other four branch sets
would again give a `K_4` minor in `C_5`.  Let their distinct bags be
`P_p,P_q`.  The remaining three bags form a `K_3` model in the unused
cycle vertices.  If either universal bag used a cycle vertex, the available
part of `C_5` would be a proper subgraph of the cycle and hence a forest;
a forest has no `K_3` minor.  Therefore `P_p={p}` and `P_q={q}`.

The first singleton misses `A=V(Q)-{p}` and the second misses
`B=V(Q)-{q}`.  No `K_5` model is consequently transversal to both named
sets, which proves the advertised counterexample.

## Exterior augmentation

After adding `x` complete to `A` and `y` complete to `B`, with `xy` absent,
the seven displayed bags are disjoint and connected.  The bags containing
`x,c_4` and `y,c_3` meet one another and every singleton bag.  The universal
singletons meet everything, and among the three cycle singletons only
`c_0c_2` is absent.  Thus exactly one required adjacency may be missing,
so the bags form a `K_7^-` model.

The construction therefore does not obstruct a theorem retaining the
exterior forest pieces.  Its scope statement and proposed repair are
accurate.
