# Audit: weaker wheel terminals

**Reviewed source:** [the complete counterexamples](hc7_weak_wheel_terminal.md).

**Exact source SHA-256:**
`6d99e559b22a93cc22dd2dc71b75c30d969913c33f18b8a56e54ac88b053625e`.

**Verdict:** GREEN — separate internal audit by `route_assessment`.
The [combined audit](../results/hc7_sealed_wheel_terminal_audit.md),
SHA-256 `462566264b6b2dab8a1c73656687ba17cb25563ff42c49867a5632934f18c45a`,
records the reviewed sources, provenance and full branch-set exclusion arguments. Its
nine-vertex edge-loss proof and eight-vertex degree proof establish
the original counterexamples. No unresolved mathematical gap was found.

## Revision and independent review

The initial split source had SHA-256
`40dd5b6e0dc0d82ef1fcacd8103f6f3766e1001d15b6ce7d4ce62f1aa7cbd675`.
Its Sections 2–3 reproduce the mathematical text of the previously
reviewed combined draft, SHA-256
`b3a85ae59a6aaaa2d587a383439fa609ce2d7b179bb538e011ddaf405524de5a`;
rejoining those sections with the promoted positive construction and
reversing its metadata changes recovers that exact hash.

`literature_repair` authored the original examples and the Section 4
strengthening. `route_assessment` independently checked the complete
strengthened source at SHA-256
`0675b014a15e9cf4143d6709ba4bba260a0f48d73165de08f43ab0760de9204d`.
Removing only its pending-audit sentence gave SHA-256
`78945cb2d1861eb293611b80022507f805fd8ccba6337568b965155ea026c815`.
The current revision also narrows the final application wording, explicitly
allowing constructions inside or splitting original preimages. This
separately checked correction changes no proof. This is an internal
mathematical audit, not external peer review or a finite-search verdict.

## Section 4: complete cores

The first completed graph is exactly the union of K6 and the stated
seven-vertex graph with 18 edges and holes `pt,qr,qs`, along the literal
K4 `{v,p,q,d}`. The second is exactly the union of the two displayed
K6 graphs along the literal K4 `{v,s,q,d}`. Each constituent excludes Q
by its order or edge count.

The projection from a proposed Q model in either union is valid. Its
bags avoiding the four-clique lie on one side, since deleting at most
four Q vertices leaves a connected graph. Each restricted clique-meeting
bag remains nonempty and reconnects through its own clique vertices.
Actual clique edges restore contacts between different such bags;
contacts to a bag avoiding the clique already lie on the retained side.
Thus the model would project to one constituent. No artificial clique
edge or unspecified branch-set lift is used.

Neither example satisfies the actual seven-connected, minimum-degree-eight
critical-host hypotheses. Completion excludes repairs confined to adding
edges inside the six indicated vertices with the triangle contacts fixed;
it does not exclude further vertices, bag splits or changed ownership.
No failure of C19 or HC7, or completion of the research goal, is asserted.
