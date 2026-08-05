# Internal audit of the decisive E5 proof gate

**Submitted branch tip:** `f5363b1`

**Submitted baseline:** `2af5d1c`
**Verdict:** mergeable as experimental provenance.  Two computation-free
theorems have been rewritten, separately audited and promoted outside this
directory.  The finite searches remain experimental, and the later rooted
placement programme remains conjectural.

This is an internal mathematical and implementation audit, not external
peer review.

## Mathematical classification

The following deductions survive hostile audit.

1. The report's six-connected `K_4`-reserve inequality is correct.  Its
   primary-target corollary is
   \[
   d_G(r)+d_G(s)\ge15+q(G)+\mathbf1_{rs\in E(G)}.
   \]
   It is promoted, with a self-contained proof and pinned audit, as
   [`hc7_k7minus_six_cut_k4_reserve_inequality.md`](../../../results/hc7_k7minus_six_cut_k4_reserve_inequality.md).
2. The protected rooted-equality peel is correct after expanding the
   contractions in the proof of Norin--Totschnig, Lemma 12, and checking
   every protected label.  It is promoted separately as
   [`hc7_protected_rooted_k42_equality_peel.md`](../../../results/hc7_protected_rooted_k42_equality_peel.md).
3. In the later attack note, helper localisation over a full opposite shore
   and the `K_2` full-edge rooted-separation lemma are sound after their
   stated proof details are supplied.  They remain working lemmas here.
4. The returned-full-edge matching conclusion omits the density calculation
   selecting the distinguished root and the selected-potential argument
   forcing the returned edge to be full.  It is not promoted from this
   note.
5. The four-root `K_6`-placement theorem and the proposed terminal
   clique-sum/cone classification are conjectural.  Neither `(E5)` nor the
   primary theorem follows from this gate.

The report's applications of the protected peel to live E5 lobes remain
conditional: the rooted hypotheses and the preservation of full host
five-connectivity after reinsertion have not all been proved.

## Computational audit

All ten C++ sources compile with Apple Clang in C++20 mode.  Fresh runs
reproduced the substantive deterministic counts:

| screen | reproduced conclusion |
|---|---|
| order eight | `3276` graphs, `2996` five-connected, no negative graph |
| order nine | `8347680` graphs, no negative graph |
| minimum one-full family | `35960 / 2268 / 2268 / 0` |
| minimum two-full family | `5718 / 4896 / 0` |
| both-endpoints family | `144 / 132 / 144 / 0` |
| three-lobe `K_5` book | `8000 / 8000 / 8000 / 0` |
| broad split screen | `181` boundary masks, `16840` negative split hosts, `194` contact codes |
| seven-edge split | `66` negative contact patterns |

The two stochastic programs originally used library-dependent
`std::shuffle`.  The integrated versions use an explicit seeded shuffle and
their stored outputs were regenerated.  They remain falsification screens,
not exhaustive results.

The exact positive screens share essentially the same branch-set oracle and
do not emit independently checked certificates.  Their host encodings and
oracle logic were inspected, but they are not promoted computer-assisted
theorems without an implementation-independent checker.  The report's
broader random search through order fifteen and uncapped order-fourteen and
order-fifteen reruns have no retained source or output in this directory.

The negative split hosts legitimately show that boundary contacts alone do
not force `K_7^-`; they are not five-connected dense counterexamples to
`(E5)`.

## Exact stopping conclusion

The gate found neither an E5 proof nor an E5 counterexample.  It did meet
the predeclared transfer criterion through the `K_4`-reserve inequality,
which applies directly to the primary `4n-2` programme.  The appropriate
strategic response is therefore to preserve this experiment, stop further
open-ended E5 boundary enumeration, and test the new inequality globally
across essential-edge six-separations of a strict-surplus primary enemy.
