# An order-seven equality shore forces an explicit `K_7^-` minor

**Status:** written reduction plus computer-assisted finite result; separate
internal audit GREEN in
[`hc7_k7minus_order_seven_equality_shore_elimination_audit.md`](hc7_k7minus_order_seven_equality_shore_elimination_audit.md).
The exact finite verifier is
[`hc7_k7minus_order_seven_equality_shore_elimination_verify.py`](hc7_k7minus_order_seven_equality_shore_elimination_verify.py).

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Terminal component theorem

### Theorem 1.1

Let `G` be a seven-connected graph with minimum degree at least eight and no
literal `K_5`.  Let `S` be a seven-vertex cut, and let `C,D` be distinct
components of `G-S`.  Suppose

\[
 |C|=7,\qquad \chi(G[C])\ge4,
 \qquad |E(G[C])|\ge13,                              \tag{1.1}
\]

and

\[
             |E(G[C])|+|E_G(C,S)|\le43.             \tag{1.2}
\]

Then `G` contains an explicit `K_7^-` minor model.

**Status:** written reduction plus computer-assisted finite result.

#### Proof

For \(v\in C\), put

\[
                              A_v=N_G(v)\cap S.
\]

Every neighbour of \(v\) lies in \(C\cup S\), so minimum degree eight gives

\[
                         |A_v|\ge8-d_{G[C]}(v).       \tag{1.3}
\]

For every nonempty \(X\subseteq C\), the open neighbourhood of \(X\)
separates \(X\) from \(D\).  Hence

\[
 |N_{G[C]}(X)|+
 \left|\bigcup_{v\in X}A_v\right|\ge7.              \tag{1.4}
\]

No element of \(S\) belongs to all four sets \(A_v\) indexed by a literal
`K_4` of `G[C]`, because those five vertices would form a literal `K_5`.
Finally, (1.2) is precisely

\[
                    \sum_{v\in C}|A_v|
                       \le43-|E(G[C])|.              \tag{1.5}
\]

Apply the finite allocation lemma in Section 2 to \(K=G[C]\).  It gives an
edge \(xy\in E(K)\), the six core bags

\[
 Q_0=\{x,y\},\qquad
 Q_1,\ldots,Q_5\text{ the singleton vertices of }C-\{x,y\}, \tag{1.6}
\]

and six distinct vertices \(s_0,\ldots,s_5\in S\).  Every \(s_i\) has a
neighbour in \(Q_i\), and the six connected sets

\[
                            B_i=Q_i\cup\{s_i\}       \tag{1.7}
\]

have all but at most one of their mutual adjacencies.

Let \(s_6\) be the unused member of \(S\).  Seven-connectivity gives
\(N_G(D)=S\), and therefore

\[
                            B_6=D\cup\{s_6\}         \tag{1.8}
\]

is connected.  It is disjoint from the six bags in (1.7) and adjacent to
every one of them through the literal boundary vertex \(s_i\in B_i\).
Thus (1.7)--(1.8) are the seven branch sets of an explicit `K_7^-` minor
model.  \(\square\)

## 2. Finite edge-contraction allocation

### Lemma 2.1

Let \(K\) be a connected graph on a seven-set \(C\), let \(S\) be a
disjoint seven-set, and let \(A_v\subseteq S\) for \(v\in C\).  Suppose:

1. \(K\) is literal-`K_5`-free, \(\chi(K)\ge4\), and
   \(\lvert E(K)\rvert\ge13\);
2. \(\lvert A_v\rvert\ge8-d_K(v)\) for every \(v\in C\);
3. \(\sum_{v\in C}|A_v|\le43-|E(K)|\);
4. for every nonempty \(X\subseteq C\),

   \[
       |N_K(X)|+\left|\bigcup_{v\in X}A_v\right|\ge7; \tag{2.1}
   \]

5. no element of \(S\) belongs to all four sets \(A_v\) indexed by a
   literal `K_4` of \(K\).

Then there are an edge \(xy\in E(K)\), the six bags \(Q_0,\ldots,Q_5\)
defined by (1.6), and an injection

\[
                         f:\{0,\ldots,5\}\longrightarrow S \tag{2.2}
\]

such that:

1. \(f(i)\in\bigcup_{v\in Q_i}A_v\) for every \(i\); and
2. among the fifteen pairs \(0\le i<j\le5\), all but at most one satisfy

   \[
   E_K(Q_i,Q_j)\ne\varnothing,
   \quad f(i)\in\bigcup_{v\in Q_j}A_v,
   \quad\hbox{or}\quad
   f(j)\in\bigcup_{v\in Q_i}A_v.                    \tag{2.3}
   \]

**Status:** computer-assisted finite result.

#### Exact finite reduction

NetworkX 3.6.1 supplies its complete atlas of unlabelled graphs on at most
seven vertices.  The adjacent verifier takes its order-seven members and
retains exactly those which are connected, have at least thirteen edges,
contain no literal `K_5`, and are not three-colourable.  Exactly 149 core
orbits remain.  Their sorted graph6 corpus has SHA-256

```text
39752dbad6b984399f40a66f0b8240aab5c9a1795cd376b4bf12284cdbe20748
```

For a fixed core, the verifier has 49 Boolean variables

\[
             a_{v,s}=1\quad\Longleftrightarrow\quad s\in A_v. \tag{2.4}
\]

It gives Z3 4.16.0 the following exact constraints:

1. the seven row lower bounds in hypothesis 2;
2. the total incidence upper bound in hypothesis 3;
3. all 127 relative-connectivity inequalities in (2.1);
4. the negative four-incidence constraint for every core `K_4` and every
   boundary vertex; and
5. nondecreasing seven-bit boundary columns, which removes only boundary-
   label symmetry.

Whenever Z3 returns a structural incidence system, a direct Python scan
checks every literal edge \(xy\in E(K)\) and all \(7!/1!=5040\) injections
in (2.2).  If the scan found no allocation satisfying (2.3), that incidence
system would be an explicit counterexample and the verifier would stop.
Otherwise it adds the exact symbolic negation of the first allocation found
and asks for another structural incidence system.  The added constraint says
that the allocation is either not incidence-respecting or leaves at least
two pairs in (2.3) unsatisfied.

This process terminates with `UNSAT` for every one of the 149 cores.  The
logic is exhaustive: at each iteration either a literal counterexample is
returned, or one genuine allocation is excluded; final `UNSAT` says that
every structural incidence system has at least one such allocation.  The
sorted invariant records consisting of the graph6 code, edge count, and
`UNSAT` status have combined SHA-256

```text
aaf1904440324ea01e3eb9a9e862da1b3664f9f8b7b7d5bfa578a3c103c3caca
```

The number and order of intermediate Z3 models are diagnostic only and can
vary between runs.  They are deliberately excluded from the pinned result
digest.

No unbounded claim is inferred from the finite run: Lemma 2.1 has already
fixed both \(|C|=7\) and \(|S|=7\) before invoking the verifier.  This proves
the lemma.  \(\square\)

## 3. Application to the five-centre two-cut

### Corollary 3.1

In the setting and response orientation of the audited
[five-centre two-cut reduction](../results/hc7_k7minus_five_centre_two_cut_reduction.md),
the equality-response component has order at least eight.

**Status:** written deduction, conditional only on the computer-assisted
finite Lemma 2.1.

#### Proof

The cited theorem gives

\[
 \chi(G[C])\ge4,\qquad |E(G[C])|\ge2|C|-1,
 \qquad |E(G[C])|+|E_G(C,S)|\le6|C|+1.              \tag{3.1}
\]

The separately audited
[order-six component theorem](../results/hc7_k7minus_order_six_equality_shore_elimination.md)
and the order-five theorem used before it already give \(|C|\ge7\).  If
\(|C|=7\), (3.1) gives the hypotheses (1.1)--(1.2), so Theorem 1.1 produces
the forbidden `K_7^-` minor.  Hence \(|C|\ge8\).  \(\square\)

## 4. Reproduction and trust boundary

With the project environment synchronized, run

```text
uv run --with z3-solver==4.16.0 python \
  results/hc7_k7minus_order_seven_equality_shore_elimination_verify.py \
  --jobs 4
```

The reference run prints 149 per-case records followed by

```text
UNSAT_cases=149/149
result_sha256=aaf1904440324ea01e3eb9a9e862da1b3664f9f8b7b7d5bfa578a3c103c3caca
```

The reference four-worker run took about 81 seconds; elapsed time is not a
pinned value, and neither are the diagnostic round counts or allocation
transcript hashes.  The verifier rejects a NetworkX or Z3 version different
from the two stated above.  It also offers `--case` for a selected graph6
core and `--enumerate-only` for the orbit census.

The computational trust boundary consists of CPython, NetworkX's
order-seven atlas, the explicit structural encoding and exhaustive
allocation scan, and Z3's SAT and UNSAT answers.  The adjacent separate
audit includes a cold full rerun.  Unlike the order-six theorem, this result
does not carry independently checked DRAT refutations; a proof-producing CNF
conversion would provide an additional check.

## Exact scope

This theorem terminally eliminates the order-seven equality shore and raises
the arbitrary two-cut residue to order at least eight.  It does not eliminate
larger equality shores, close the three-connected branch after deleting the
five centres, prove the `K_7^-` six-colour conjecture, or prove `HC_7`.
