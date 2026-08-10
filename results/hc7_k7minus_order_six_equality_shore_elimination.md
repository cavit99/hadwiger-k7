# An order-six equality shore forces an explicit `K_7^-` minor

**Status:** written reduction plus computer-assisted finite result; separate
internal audit GREEN in
[`hc7_k7minus_order_six_equality_shore_elimination_audit.md`](hc7_k7minus_order_six_equality_shore_elimination_audit.md).
The deterministic generator and certificate-checking driver is
[`hc7_k7minus_order_six_equality_shore_elimination_verify.py`](hc7_k7minus_order_six_equality_shore_elimination_verify.py).

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Terminal component theorem

### Theorem 1.1

Let `G` be a seven-connected graph with minimum degree at least eight and no
literal `K_5`.  Let `S` be a seven-vertex cut, let `C` be a component of
`G-S`, and suppose there is another component `D` of `G-S`.  If

\[
 |C|=6,\qquad \chi(G[C])\ge4,
 \qquad |E(G[C])|\ge11,                              \tag{1.1}
\]

then `G` contains an explicit `K_7^-` minor model.

**Status:** written reduction plus computer-assisted finite result.

#### Proof

For \(v\in C\), write

\[
                            A_v=N_G(v)\cap S,
\]

and let \(J=\overline{G[C]}\).  Thus

\[
 |E(J)|\le4,
 \qquad |A_v|\ge 8-d_{G[C]}(v)=3+d_J(v).             \tag{1.2}
\]

For every nonempty \(X\subseteq C\), its full open neighbourhood separates
\(X\) from \(D\).  Seven-connectivity therefore gives

\[
 |N_{G[C]}(X)|+
 \left|\bigcup_{v\in X}A_v\right|\ge7.               \tag{1.3}
\]

In particular, every vertex of `S` has a neighbour in `C`.  Moreover, no
vertex of `S` is adjacent to all four vertices of a literal `K_4` in
`G[C]`, since those five vertices would induce a literal `K_5` subgraph.

The finite incidence lemma verified in Section 2 now gives an injection

\[
                         f:C\longrightarrow S        \tag{1.4}
\]

such that \(vf(v)\) is an edge for every \(v\in C\) and all but at most one
nonedge \(uv\) of \(G[C]\) satisfies

\[
             f(u)v\in E(G)\quad\hbox{or}\quad
             f(v)u\in E(G).                          \tag{1.5}
\]

For each \(v\in C\), put

\[
                              B_v=\{v,f(v)\}.         \tag{1.6}
\]

These six sets are pairwise disjoint and connected.  A core edge joins the
corresponding two sets, while (1.5) joins the sets corresponding to every
but at most one core nonedge.  Hence the six sets form a `K_6^-` minor
model, with possibly no missing adjacency.

Since `G` is seven-connected, `N_G(D)=S`.  Let `s_0` be the unique boundary
vertex outside `f(C)`.  The set

\[
                              B_7=D\cup\{s_0\}        \tag{1.7}
\]

is connected and disjoint from the six sets in (1.6).  It is adjacent to
every `B_v`, because `D` has a neighbour at each literal vertex `f(v)` of
`S`.  Thus (1.6)--(1.7) are the seven branch sets of an explicit `K_7^-`
minor model.  \(\square\)

## 2. Finite incidence lemma

### Lemma 2.1

Let \(K\) be a graph on a six-set \(C\), let \(S\) be a disjoint seven-set,
and write \(A_v\subseteq S\) for \(v\in C\).  Suppose:

1. \(K\) is literal-\(K_5\)-free, \(\chi(K)\ge4\), and
   \(\lvert E(K)\rvert\ge11\);
2. \(\lvert A_v\rvert\ge3+d_{\overline K}(v)\) for every \(v\in C\);
3. for every nonempty \(X\subseteq C\),

   \[
       |N_K(X)|+\left|\bigcup_{v\in X}A_v\right|\ge7; \tag{2.1}
   \]

4. no element of \(S\) belongs to all four sets \(A_v\) indexed by a literal
   \(K_4\) of \(K\).

Then there is an injection \(f:C\to S\) with \(f(v)\in A_v\) for every
\(v\) such that all but at most one edge \(uv\) of \(\overline K\) obeys

\[
                       f(u)\in A_v
                    \quad\hbox{or}\quad
                       f(v)\in A_u.                  \tag{2.2}
\]

**Status:** computer-assisted finite result.

#### Exact finite reduction

The complement \(J=\overline K\) has at most four edges.  The adjacent verifier
enumerates every labelled graph on six vertices with at most four edges,
rejects exactly those for which `K` contains a `K_5` or is three-colourable,
and canonically quotients by all `6!` vertex permutations.  Exactly ten
orbits remain:

\[
\begin{split}
 &K_3+3K_1,\quad 2K_2+2K_1,\quad P_4+2K_1,
 \quad \text{the paw}+2K_1,\\
 &P_3+K_2+K_1,\quad \text{a subdivided }K_{1,3}+K_1,
 \quad K_{1,3}+K_2,\\
 &C_4+2K_1,\quad P_5+K_1,\quad 2P_3.
                                                               \tag{2.3}
\end{split}
\]

Here the displayed graphs are the possible complements \(J\), not the cores
\(K\) themselves.

For each orbit, the verifier creates 42 Boolean variables

\[
             x_{v,s}=1\quad\Longleftrightarrow\quad s\in A_v. \tag{2.4}
\]

Its CNF has exactly the following clauses.

1. Explicit cardinality clauses encode (1.2), equivalently hypothesis 2.
2. For every one of the 63 nonempty subsets \(X\subseteq C\), explicit
   cardinality clauses encode (2.1).
3. One negative clause for each core \(K_4\) and boundary element encodes
   hypothesis 4.
4. Adjacent boundary columns are put in nondecreasing six-bit order.  This
   loses no incidence system because the seven elements of `S` are
   interchangeable in the lemma.
5. For each of the \(7!/1!=5040\) injections \(f\), distributed clauses state
   that either some assigned incidence `x_{v,f(v)}` is absent or at least
   two complement edges fail (2.2).

Thus the formula is satisfiable exactly when that orbit admits a set system
satisfying all four hypotheses but no injection in the conclusion.
CaDiCaL 3.0.1 returns `UNSAT` for all ten formulas.  The independent
`drat-trim` checker at revision
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985` verifies all ten emitted DRAT
refutations.  Consequently
no counterexample set system exists, proving Lemma 2.1.  \(\square\)

## 3. Application to the five-centre two-cut

### Corollary 3.1

In the setting and orientation of the audited
[five-centre two-cut reduction](../results/hc7_k7minus_five_centre_two_cut_reduction.md),
the equality-response component has order at least seven.

**Status:** written deduction, conditional only on the computer-assisted
finite Lemma 2.1.

#### Proof

The cited theorem already gives

\[
 \chi(G[C])\ge4,\qquad |E(G[C])|\ge2|C|-1.          \tag{3.1}
\]

It excludes `|C|<=5`.  If `|C|=6`, (3.1) gives eleven internal edges, so
Theorem 1.1 supplies the forbidden `K_7^-` minor.  Therefore `|C|>=7`.
\(\square\)

## 4. Reproduction and trust boundary

Install CaDiCaL and build `drat-trim`, then run from the repository root:

```text
python3 results/hc7_k7minus_order_six_equality_shore_elimination_verify.py
```

The reference run prints

```text
core_orbits=10
core_sha256=d9d88730ab2cd9712f1131aca905e15241e06cb790e63f25d64e71344b598c9e
cnf_corpus_sha256=8540146081d94bc2779d3049e1c5fba807748cb3a6052e8a4b770c6ec854a354
cnf_variables=42..42 cnf_clauses=34237..175448
UNSAT_cases=10/10 DRAT_verified=10/10 generated_proof_bytes=10339951
```

The proof-byte count may vary with the solver build.  The core and CNF
corpus hashes are deterministic and pinned in the verifier.  A generator-
only check is available as

```text
python3 results/hc7_k7minus_order_six_equality_shore_elimination_verify.py \
  --enumerate-only
```

The computational trust boundary consists of CPython, the explicit orbit
and CNF generator, CaDiCaL as proof producer, and `drat-trim` as independent
proof checker.  The mathematical obligations connecting the host graph to
the 42 incidence variables and the verified injection to the seven branch
sets are the written parts of Theorem 1.1.

## Exact scope

This theorem eliminates the order-six equality shore and raises the
unconditional two-cut residue to order at least seven.  It does not eliminate
larger equality shores, close the three-connected branch after deleting the
five centres, prove the `K_7^-` six-colour conjecture, or prove `HC_7`.
