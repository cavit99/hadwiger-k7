# Boundary-fullness does not control separator degree

**Status:** RED postmortem for the retracted exact-six-connectivity branch proof.  This note records an invalid inference; it is not a counterexample to the proposed extremal theorem.

**Affected branch revision:** `af4bbe724875d858d9f3ae9b2092d1de308aa9bd` and its preceding exact-six-connectivity commits.

## 1. The invalid inference

Let `S` be a six-vertex separator of a six-connected graph `H`, and let the components of `H-S` be `C_1,...,C_r`.  Component fullness means

\[
N_H(C_i)=S
\]

for every `i`.  Hence every `s in S` has at least one neighbour in each component, so

\[
d_{H-S}(s)\ge r.
\]

Six-connectivity also gives

\[
d_H(s)\ge6.
\]

However,

\[
d_H(s)=d_{H[S]}(s)+d_{H-S}(s).
\]

Two lower bounds on the two quantities on the right do **not** imply

\[
d_{H[S]}(s)\ge6-r.
\]

That conclusion would require an upper bound `d_{H-S}(s)<=r`, not the available lower bound.  For example, with two full components, the data

\[
d_H(s)=6,\qquad d_{H-S}(s)=5,\qquad d_{H[S]}(s)=1
\]

are entirely compatible with fullness and minimum degree.

## 2. Every structural branch was affected

The retracted proof used the same invalid subtraction in all three places where it classified the separator graph.

1. In the four-component branch it inferred minimum separator degree two and used that to contradict the conclusion that `H[S]` is a matching.
2. In the two-component branch it inferred minimum separator degree four, then combined this with `e(H[S])<=12` to force `H[S]=K_6-3K_2`.
3. In the three-component branch it inferred minimum separator degree three, then combined this with a separately proved maximum-degree-three statement to force a cubic boundary.

Without those lower bounds:

- four components have not been eliminated;
- the two-component boundary has not been classified as `K_6-3K_2`;
- the three-component boundary has not been classified as cubic;
- the rooted excess sums that depend on those classifications do not apply.

Thus the exact-connectivity-six theorem, the downstream seven-connected `4n-2` theorem, and the claimed six-colour corollary were not proved.

## 3. Why the finite verifier did not protect the proof

The verifier enumerated six-vertex graphs only after imposing

- `min(boundary_degree)>=2` in the four-component case;
- `min(boundary_degree)>=4` in the two-component case;
- `min(boundary_degree)>=3` in the three-component case.

Those are exactly the unsupported premises above.  Its successful output therefore verified conditional finite classifications, not the missing host-graph implication that would make the premises valid.

The internal audit repeated the same subtraction and consequently did not provide an independent check of the critical step.

## 4. Correct status and repair requirement

The repository must retain the preceding main-line status:

- the seven-connected `4n-2` extremal theorem remains open;
- the `K_7^-` six-colour conjecture remains open;
- `HC_7` remains open;
- the strict labelled separator-shore terminalisation problem remains the active route.

A genuine exact-six repair would need new information that controls exterior incidence from above, or a different weighted inequality coupling exterior incidence, separator structure, density and target exclusion.  Boundary fullness and minimum degree alone cannot supply the missing separator-degree lower bounds.
