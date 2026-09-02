# Literal-`K_{4,4}` minimum-blocker bisection screen

**Status:** deterministic computer-assisted bounded evidence.  No survivor
was found through blocker order seven.  This is not an unbounded theorem, an
independently checkable UNSAT certificate, a proof of the weighted splitter
theorem, or a proof of the literal `K_{4,4}` case of T44.

The screen concerns the following local residue.  Let `X` be the connected
shore of an inclusion-minimal tight blocker, with boundary

```text
D={a,b,k1,k2,k3,k4,k5},    H=D-{a},    K=H-{b}.
```

The edge `ab` belongs to the boundary graph.  Its presence is used in the
minor construction that gives the two-helper criterion; it is not an
additional variable in this local incidence screen.

## Formula

The verifier represents `G[X]` and the incidences between `X` and `D`.  It
requires:

1. `G[X]` is three-connected and every member of `D` has a neighbour in
   `X`;
2. every nonempty `W subseteq X`, including `W=X`, satisfies

   ```text
   |N_X(W)|+|N_D(W)| >= 7;
   ```

3. every proper connected `W subset X` which sees both `a` and `b` satisfies

   ```text
   |N_X(W)|+|N_D(W)| >= 8;
   ```

   because equality seven would make `W` a smaller connected blocker; and
4. no disjoint nonempty connected adjacent pair `U,V subseteq X`, oriented
   so that `U` sees `a`, satisfies the closing two-helper inequality for any
   `h0 in H`:

   ```text
   |H-(N_D(U) union {b,h0})|
       + |H-(N_D(V) union {h0})| <= 1.
   ```

For a spanning connected bipartition `U dotunion V=X`, put

```text
r(U)=|{k in K : N_X(k) cap U is empty}|,
c(U)=|{h in H : N_X(h) subseteq U}|.
```

The excluded inequality is then equivalent to `r(U)+c(U)<=2`.  Thus every
survivor must satisfy `r(U)+c(U)>=3` for every spanning connected
bipartition whose first side sees `a`.

The subsequently audited
[spanning-extension and split-count
corollary](../../../results/hc7_k44_spanning_two_helper_split_count.md)
shows that this restriction loses no positive witness: every unused
component can be absorbed whole into a side it meets without increasing the
defect.  Equivalently, if `s` is the number of split `K`-supports and
`epsilon_b=1` exactly when the second side misses `b`, the optimized defect
is `max(0,4-s+epsilon_b)` and the closing threshold is
`s>=3+epsilon_b`.

## Two encodings

The first encoding makes every internal edge and boundary incidence
symbolic.  It checks every disjoint connected adjacent pair, including pairs
which leave vertices unused.  This complete labelled encoding is UNSAT for
orders four, five and six.

The second encoding independently fixes each unlabelled three-connected
host from the NetworkX graph atlas and makes only its boundary incidences
symbolic.  It imposes the spanning-bipartition form of item 4, which the
spanning-extension corollary now proves equivalent for witness existence,
together with two proved consequences of minimum-blocker structure:

- every `k in K` has at least two neighbours in `X`; and
- some `p in N_X(a)` has `X-p` full to `H` and `|N_K(p)|<=2`.

It is UNSAT on all atlas hosts through order seven:

| `|X|` | unlabelled three-connected hosts |
|---:|---:|
| 4 | 1 |
| 5 | 3 |
| 6 | 17 |
| 7 | 136 |

In particular, spanning connected bipartitions already exclude every host
in this bounded range.  The unused-vertex form is not needed by the atlas
check.

## Reproduction and expected output

NetworkX `3.6.1` is pinned by the repository lock.  On the current local
toolchain, run from the repository root with the Homebrew Python that carries
`z3-solver`; the verifier locates NetworkX in the repository environment if
necessary:

```text
python3 active/experiments/k44_literal_minimum_blocker_bisection/verify.py
```

The pinned output is recorded in [`output.txt`](output.txt).  The four
graph-atlas host digests are asserted before any solver claim is printed.

## Trust boundary and scope

The finite trust boundary is Python and Z3 Boolean/pseudo-Boolean semantics,
Z3's `UNSAT` answers, NetworkX `3.6.1` graph-atlas completeness through order
seven, graph6 serialization, and successful assertion execution.  The two
encodings share Z3 but have different host representations and connectivity
implementations.  No DRAT-style or independently checkable UNSAT certificate
is retained.

The order bound is not a mathematical hypothesis of the live blocker
problem.  The experiment neither extrapolates from order seven nor enumerates
successive ambient exterior graphs.  It is a targeted local obstruction
screen for the already reduced minimum-blocker shore.
