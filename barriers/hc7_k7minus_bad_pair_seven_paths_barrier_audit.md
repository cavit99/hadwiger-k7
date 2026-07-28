# Internal audit: bad-pair seven-path barrier

**Verdict:** GREEN.

**Audited note SHA-256:**
`56d4ba8793c2b9bd596cef9e0449f106f9296b722c096e670b66a369c24f67e6`.

**Verifier SHA-256:**
`25adaa447476d7637ef963de28c25fdda5dc34b441413d0346b7eba3b5fd1b36`.

This is a separate internal audit, not external peer review.

The 25 listed edges give `d(u)=d(v)=8` and `uv` absent.  Direct inspection
gives both neighbourhoods as `K_3` disjoint union `K_3` disjoint union
`K_2`, hence independence number three and no `K_4`.  The seven common
neighbours displayed in the note give seven internally disjoint length-two
`u`--`v` paths.

The five listed bags form a valid tree decomposition: every edge is covered,
and the bags containing each vertex form a connected subtree of the
four-leaf star.  The largest bag has order five, so the graph has treewidth
at most four.  Since `K_7^-` contains `K_6` and treewidth is minor-monotone,
the graph has no `K_7^-` minor.

The verifier independently checks the graph, neighbourhood invariants,
paths and tree decomposition.  The graph is not seven-connected or
contraction-critical, so the note's limited refutation scope is accurate.
