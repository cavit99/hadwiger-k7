# Independent finite-encoding audit

**Verdict: GREEN at the stated bounded scope.**  A separate internal review
checked both encodings and reproduced the pinned output.  This is not an
audit of an unbounded theorem and is not external peer review.

Pinned revisions:

| file | SHA-256 |
|---|---|
| [`README.md`](README.md) | `0750e980a408baa6a268aa9748537c5fe8aca52e325ac86b18231a66c8358ef7` |
| [`verify.py`](verify.py) | `2f363571456b2c89a1397a9f7d0e98e1a2ac1a987f8134b25afa437b860ab0e1` |
| [`output.txt`](output.txt) | `757239fa4c6898e519a988ce29543a949e63cc28217b228796df257327b6916a` |

An independent run under Z3 `4.16.0` and NetworkX `3.6.1` reproduced every
line of `output.txt`: symbolic orders four through six and all atlas hosts
of orders four through seven are UNSAT, with the stated host counts and
digests.

The README revision is presentational.  It now invokes the separately
audited [spanning-extension and split-count
corollary](../../../results/hc7_k44_spanning_two_helper_split_count.md), at
source SHA-256
`9e139106b9f5c47d1c12b7b24436f1890b6f50aa31c293689b2cb1fb3945da54`,
whose [GREEN audit](../../../results/hc7_k44_spanning_two_helper_split_count_audit.md)
has SHA-256
`3987cf8f68d36023805028c799221b5052d667770d8bfda47c5e14f115ead3f5`.
That corollary, not the solver code, proves that an arbitrary two-helper
witness can be enlarged to a spanning connected partition without
increasing its defect, and then gives the split-count identity.  Thus the
fixed-host encoding remains literally a spanning-partition encoding; the
external written corollary justifies treating its witness-existence test as
equivalent to the unrestricted two-helper test.  Neither `verify.py` nor
`output.txt` changed in this presentation update.

The symbolic reachability formula correctly enforces connectivity after
every deletion of zero, one or two vertices.  Boundary Boolean variables
count distinct internal and external resources.  The strict inequality is
imposed exactly on proper connected sets seeing both `a,b`.  Every ordered
disjoint connected adjacent helper pair and every omitted `h_0` are checked.

In the fixed-host formula, boundary fullness makes the resources missed by
the first shore and those supported wholly in it disjoint.  Optimizing
`h_0` therefore decreases the pre-omission defect sum by one when that sum
is positive, and leaves zero unchanged.  The closing condition is exactly
`r(U)+c(U)<=2`.  The multiple-attachment and special `p` constraints agree
with the adjacent written theorem.

The trust boundary is Z3's UNSAT answers, Python semantics, NetworkX's
graph atlas and connectivity implementation, graph6 serialization, and
successful assertion execution.  No independently checkable UNSAT
certificate is retained.  Nothing in this audit extrapolates beyond order
seven.
