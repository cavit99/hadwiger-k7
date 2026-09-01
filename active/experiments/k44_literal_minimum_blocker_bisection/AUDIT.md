# Independent finite-encoding audit

**Verdict: GREEN at the stated bounded scope.**  A separate internal review
checked both encodings and reproduced the pinned output.  This is not an
audit of an unbounded theorem and is not external peer review.

Pinned revisions:

| file | SHA-256 |
|---|---|
| [`README.md`](README.md) | `edf25b53b9c71170c904fbedde6178a88f3be1576174739b32d9c6f68a7aee0a` |
| [`verify.py`](verify.py) | `2f363571456b2c89a1397a9f7d0e98e1a2ac1a987f8134b25afa437b860ab0e1` |
| [`output.txt`](output.txt) | `757239fa4c6898e519a988ce29543a949e63cc28217b228796df257327b6916a` |

An independent run under Z3 `4.16.0` and NetworkX `3.6.1` reproduced every
line of `output.txt`: symbolic orders four through six and all atlas hosts
of orders four through seven are UNSAT, with the stated host counts and
digests.

The symbolic reachability formula correctly enforces connectivity after
every deletion of zero, one or two vertices.  Boundary Boolean variables
count distinct internal and external resources.  The strict inequality is
imposed exactly on proper connected sets seeing both `a,b`.  Every ordered
disjoint connected adjacent helper pair and every omitted `h_0` are checked.

In the fixed-host formula, boundary fullness makes the resources missed by
the first shore and those supported wholly in it disjoint.  Optimizing
`h_0` therefore changes the pre-omission defect sum by one, so the closing
condition is exactly `r(U)+c(U)<=2`.  The multiple-attachment and special
`p` constraints agree with the adjacent written theorem.

The trust boundary is Z3's UNSAT answers, Python semantics, NetworkX's
graph atlas and connectivity implementation, graph6 serialization, and
successful assertion execution.  No independently checkable UNSAT
certificate is retained.  Nothing in this audit extrapolates beyond order
seven.
