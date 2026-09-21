# Independent audit: degree-five nonroot elimination

**Verdict:** GREEN.

The stated degree-six restriction passes a separate internal proof audit.
This is not external peer review or a proof of the stronger
helper target, Conjecture 21, HC7, or a theorem of the requested comparative
significance.

**Audited source:** [degree-five elimination](hc7_c21_helper_degree_six.md),
SHA256 `85927a0f7d1af6229930fd67f7144eac35b934c54ad504539a34d39e209020ee`.
The independently audited development draft had SHA256
`337a9920a94603c02ba76371ea80174be78f2dee9c285faf33a4f9bb23165b06`;
promotion changed its status, scope wording and relative dependency link.
The complete promoted proof was reread before pinning this audit.

The retained [degree and connectivity reduction](hc7_c21_rooted_density_low_degree_reduction.md)
has SHA256 `431bd7d7d2b5bcb59e385781234c6d7ed6824f62ee50eb8ddf49e69da792cef2`.
Its separately audited rooted-dart dependency has SHA256
`37dcf256f64fca7c49a1bd4ec66021371fba9a7863bf9523597ba4b898ecfad2`.
Those hypotheses, including the forbidden adjacent degree-five/codegree-three
pair, are inputs here rather than consequences of an assumed helper theorem.

## Strongest inference checked

The local contraction lemma was checked case by case against the proof of
[Kou et al., Lemma 1](https://arxiv.org/html/2509.25809v1#S2).
Although that source states a globally contraction-critical lemma, the
displayed crossing argument uses only the hypothetical nontrivial cut of
the selected contraction. In each corner inequality the opposite side
is nonempty. The two, zero, and one nonempty A-corner cases exhaust the
possibilities and give the asserted contradictions. No atom minimality
or global contraction-criticality is imported.

The completed root graph is ordinarily five-connected. Completing only
root edges changes neither root-free fragment boundaries nor their
densities. After contracting two nonroots, every original root retains
at least one nonroot neighbour and its four completed root neighbours.
Consequently the singleton opposite side of a purported positive
four-boundary fragment cannot be an original root. This checks the
otherwise delicate passage from quasi five-connectivity to rooted
4-lightness.

## Induction, density and ownership checks

- Deleting the degree-five vertex and adding the chosen missing edge
  gives density two and a genuine smaller rooted minor. The fixed
  preimage `{v,a}` contains at most one original root.
- A lightness violation in that minor has exactly five original
  neighbours, including the nonroot `v`, so its original five-side is
  proper. The displayed density inequalities force all four integers
  `rho4(H,Y), rho4(G,Y), k, c` to equal one.
- The unique neighbour `a` is a nonroot. The missing-edge endpoint `b`
  must already belong to the original boundary. This excludes a
  singleton side; minimum degree and the previously forbidden pair
  exclude a two-vertex side. Independence and minimum root degree
  exclude a singleton opposite side.
- The alternative contraction `va` has at most three common neighbours,
  is 4-light by the local lemma, and retains density at least two. Its
  fixed preimages preserve five distinct roots and all disjoint bags.
- In the completed-clique neighbourhood case the five linkage paths
  are paths of the original graph with interiors outside `N[v]`.
  Trimming the path ending at a chosen nonroot leaves a nonempty root
  bag. Every completed-clique edge actually used is incident with that
  nonroot, hence is an original edge. The two helpers and five root
  bags have ten of the eleven required contacts.

Both induction operations strictly reduce vertex count; the direct
construction requires no induction. No finite census is used. No gap
was found under the expressly retained minimal-counterexample inputs.
