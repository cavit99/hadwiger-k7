# Internal audit of the order-seven equality-shore elimination

**Verdict:** **GREEN.**

**Audit date:** 2026-08-10.

**Audited theorem revision:**
`986194fa7953241f3bf8de084be45848cb40861566829635d6c78b0f14a5ac10`
for
[`hc7_k7minus_order_seven_equality_shore_elimination.md`](hc7_k7minus_order_seven_equality_shore_elimination.md).

**Audited verifier revision:**
`2fcd091e29b3f626b2b8d74ebc7035f430b08574d724a83e9396c7fdd595489d`
for
[`hc7_k7minus_order_seven_equality_shore_elimination_verify.py`](hc7_k7minus_order_seven_equality_shore_elimination_verify.py).

This is a separate internal audit of the written reduction, the exact finite
encoding, and a cold execution of the complete 149-case computation.  It is
not external peer review.

The mathematical theorem and executable encoding were frozen and cold-
audited at SHA-256 values
`b216080deaa4f8ce003b95956e44e507b2d9dff8af97ac6678b3e64f3d8a5f12`
and
`a1e8b1e056dab064b74b1d0fc9e355764d4279b1a25d13749bb6953ecde39847`,
respectively.  The promoted revisions pinned above change only the theorem's
status, audit link, reproduction path and trust-boundary wording, plus the
verifier's opening docstring from “lemma” to “theorem.”  That exact diff was
inspected; no statement, proof, constraint, search, digest or executable
semantics changed.

## 1. Host-to-incidence reduction

The translation from Theorem 1.1 to Lemma 2.1 is valid.

- Since \(C\) is a component of \(G-S\), every neighbour of a vertex of
  \(C\) lies in \(C\cup S\).  Thus minimum degree eight gives exactly the
  row lower bound
  \(\lvert A_v\rvert\ge 8-d_{G[C]}(v)\).
- For each nonempty \(X\subseteq C\), the open neighbourhood
  \(N_{G[C]}(X)\cup\bigcup_{v\in X}A_v\) separates the surviving vertices
  of \(X\) from the distinct component \(D\).  The two displayed parts are
  disjoint, so seven-connectivity gives (1.4), including the case \(X=C\).
- A boundary vertex common to the four incidence sets belonging to a
  literal \(K_4\) of \(G[C]\) would complete a literal \(K_5\).  Hypothesis 5
  of Lemma 2.1 is therefore forced by the host assumption.
- The identity
  \(\lvert E_G(C,S)\rvert=\sum_{v\in C}\lvert A_v\rvert\) makes (1.2) and
  the total-incidence bound equivalent.

The connectedness, order, edge-count, chromatic, and literal-\(K_5\)-free
hypotheses on the core are also transferred without loss.

## 2. Atlas coverage and structural encoding

NetworkX 3.6.1 supplies one representative of every unlabelled graph on at
most seven vertices.  The verifier restricts its order-seven representatives
by precisely the four core conditions in Lemma 2.1: connectedness, at least
thirteen edges, absence of a literal \(K_5\), and failure of a direct
three-colouring test.  The audit reproduced

```text
core_orbits=149
core_sha256=39752dbad6b984399f40a66f0b8240aab5c9a1795cd376b4bf12284cdbe20748
```

For each core, the 49 Boolean variables have the claimed incidence meaning.
The seven degree constraints, one total-incidence constraint, all 127
nonempty-subset relative-connectivity constraints, and every core-\(K_4\)
literal-\(K_5\) exclusion agree exactly with hypotheses 2--5 of Lemma 2.1.

The numerical code of a boundary column is its seven-bit incidence vector.
Requiring the seven column codes to be nondecreasing only chooses a sorted
representative of each boundary-labelling orbit.  Every incidence system can
be brought to this form by permuting \(S\), and the desired injection and its
repair conditions are invariant under that same permutation.  The symmetry
reduction therefore discards no mathematical case.

## 3. Allocation scan and lazy blocking

For every literal core edge, `core_bags` constructs the contracted edge bag
and the five remaining singleton bags.  `INJECTIONS` contains all
\(7!/1!=5040\) injections into \(S\).  The direct scan first checks that the
image assigned to each bag is incident with that bag, then checks precisely
the two possible boundary repairs for every nonedge of the six-bag core
quotient.  Existing quotient edges need no repair, so accepting when at least
\(r-1\) of the \(r\) quotient nonedges are repaired is equivalent to leaving
at most one of all fifteen bag pairs nonadjacent.

The lazy block is the exact negation of one terminal allocation.  If
\(r\le1\), incidence-respecting alone makes the allocation terminal, and the
block is `Not(valid)`.  If \(r\ge2\), the block is

\[
  \text{valid}\Longrightarrow
  \#\{\text{repaired quotient nonedges}\}\le r-2,
\]

which is exactly the negation of `valid` together with at least \(r-1\)
repairs.  Consequently a genuine counterexample incidence system would
satisfy every accumulated block and would eventually be returned.  An
`UNSAT` result after these exact blocks therefore proves that no such
incidence system exists for the fixed core.

## 4. Cold finite rerun

The frozen verifier was run with CPython, NetworkX 3.6.1, and Z3 4.16.0 via

```text
uv run --with z3-solver==4.16.0 python \
  results/hc7_k7minus_order_seven_equality_shore_elimination_verify.py \
  --jobs 4
```

It completed successfully with

```text
UNSAT_cases=149/149
result_sha256=aaf1904440324ea01e3eb9a9e862da1b3664f9f8b7b7d5bfa578a3c103c3caca
```

An earlier pre-audit revision incorrectly pinned a digest containing the
order of Z3's intermediate models.  Independent cold runs exposed that
those diagnostic transcripts can differ even though all 149 cases end in
`UNSAT`.  The audited revision corrects this: its pinned digest contains
only the sorted graph6 code, edge count, and final `UNSAT` status of every
case.  Round counts and allocation-transcript hashes remain visible
diagnostics but are not asserted as reproducible results.

## 5. Minor-model reconstruction and corollary

For the allocation supplied by Lemma 2.1, each
\(B_i=Q_i\cup\{s_i\}\) is connected, and the six bags are disjoint because
the \(Q_i\) partition \(C\) and the boundary assignment is injective.  The
allocation condition supplies all but at most one adjacency among them.

For a distinct component \(D\) of \(G-S\), its open neighbourhood is a
subset of \(S\) and is a vertex cut separating \(D\) from \(C\).  Hence
seven-connectivity and \(\lvert S\rvert=7\) force \(N_G(D)=S\).  If \(s_6\)
is the unused boundary vertex, \(D\cup\{s_6\}\) is therefore a connected
seventh bag,
disjoint from and adjacent to every earlier bag.  These are valid branch
sets of a \(K_7^-\)-minor model; extra adjacency in the zero-missing-edge
case is harmless.

Corollary 3.1 correctly combines the audited order-five and order-six
eliminations with the five-centre two-cut inequalities.  At
\(\lvert C\rvert=7\) those inequalities give exactly the edge lower bound
13 and closed-shore upper bound 43 required by Theorem 1.1, so the surviving
equality-response shore has order at least eight.

## 6. Trust boundary and unresolved assumptions

No mathematical gap was found.  The finite lemma remains computer-assisted:
the audit relies on CPython, the completeness of NetworkX 3.6.1's
order-seven atlas, the inspected encoding and allocation scan, and Z3
4.16.0's SAT/UNSAT answers.  This computation does not provide independently
checkable DRAT certificates.  That absence is an explicit trust limitation,
not a gap in the stated computer-assisted result.

The corollary additionally relies on its cited audited upstream theorems.
The result eliminates only the order-seven equality-response component; it
does not eliminate larger components, close the other five-centre branch,
prove the \(K_7^-\) six-colour conjecture, or prove \(HC_7\).
