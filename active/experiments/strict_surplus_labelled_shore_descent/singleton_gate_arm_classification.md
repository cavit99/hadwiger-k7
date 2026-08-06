# Classification of a minimum singleton/root gate

**Status:** experimental computation-free reduction; independent audit
pending.

Let

\[
\mathcal M=(D,Q_1,\ldots,Q_5)
\]

be a spanning contact-maximal `K_6` model in `G-x`.  Choose the multiply
rooted donor `D` with minimum order among all spanning contact-maximal
models.  Fix an uncontacted foreign bag `U`, and suppose a one-root blocker
has been obtained:

\[
y\in C\subseteq D,
\qquad C\cap N(x)=\{y\},
\qquad D-C\text{ connected},
\qquad E(C,U)=\varnothing.                             \tag{1.1}
\]

Choose `C` with minimum order among all blockers satisfying (1.1) for the
fixed model, donor root and missed bag.

## 1. Exact form of a minimum blocker

Let

\[
A_0,A_1,\ldots,A_m
\]

be the components of `D-y`, indexed so that `D-C subseteq A_0`.

### Lemma 1.1

One has

\[
D-C=A_0,
\qquad
C=\{y\}\cup A_1\cup\cdots\cup A_m.                   \tag{1.2}
\]

Every `A_i`, `i>=1`, is root-free and anticomplete to `U`.

### Proof

The connected set `D-C` avoids `y`, so it lies in one component `A_0` of
`D-y`.  Every other component of `D-y` must lie in `C`.  The set

\[
C_0=\{y\}\cup\bigcup_{i=1}^m A_i
\]

is connected, because every component of `D-y` has a neighbour at `y`.
Its complement in `D` is the connected set `A_0`.  Moreover
`C_0 subseteq C`, and it has the same unique root and is still
anticomplete to `U`.  Minimality of `C` gives `C=C_0`, proving (1.2).
The root and missed-bag assertions follow from (1.1).  `\square`

Thus a non-singleton minimum blocker is a root gate `y` together with a
nonempty family of root-free arms, while all other model roots lie in the
single retained component `A_0`.

## 2. Every arm owns at least two model duties

For a connected set `A subseteq D`, define

\[
\Omega(A)=\{Q_i:\text{every }D-Q_i\text{ edge has its }D
                    \text{-end in }A\}.                \tag{2.1}
\]

### Lemma 2.1

For every arm `A_i`, `i>=1`,

\[
                         |\Omega(A_i)|\ge2.             \tag{2.2}
\]

The ownership sets of distinct arms are disjoint and none contains `U`.
Consequently

\[
                         m\le2.                         \tag{2.3}
\]

### Proof

The complement `D-A_i` is connected: it consists of `y`, the retained
component `A_0`, and all other arms, each joined through `y`.

Suppose first that `A_i` owns no duty.  Seven-connectivity implies that the
arm meets at least one foreign bag; otherwise its neighbourhood would be
contained in `{y}`.  Move the entire arm into any foreign bag which it
meets.  The target bag remains connected, an `A_i-y` edge restores its
adjacency to the residual donor, and every old donor duty survives.

If `A_i` owns exactly `Q_j`, move it into `Q_j`.  An actual `A_i-Q_j`
edge makes the enlarged target bag connected; an `A_i-y` edge restores the
adjacency between the target and the residual donor; and every other donor
duty survives.

In either case the model remains spanning and contact-maximal, all roots
survive, and the multiply rooted donor `D-A_i` is strictly smaller.  This
contradicts the choice of `D`, proving (2.2).

A nonempty model duty cannot be owned by two disjoint arms, so their owner
sets are disjoint.  The arms lie in `C`, which is anticomplete to `U`, and
therefore no arm owns `U`.  At least two disjoint duties per arm must fit
inside the four-label set of accessible foreign bags, giving (2.3).
`\square`

### Corollary 2.2 (the two-arm equality state)

If `m=2`, then after relabelling

\[
\Omega(A_1)=\{Q_1,Q_2\},
\qquad
\Omega(A_2)=\{Q_3,Q_4\},                              \tag{2.4}
\]

and the four sets exhaust all foreign duties other than `U`.
Consequently every `D-Q_1,D-Q_2` edge has its `D`-end in `A_1`, every
`D-Q_3,D-Q_4` edge has its `D`-end in `A_2`, and every `D-U` edge has its
`D`-end in `A_0`.  In particular,

\[
E(A_1,Q_3\cup Q_4\cup U)=\varnothing,
\qquad
E(A_2,Q_1\cup Q_2\cup U)=\varnothing.                 \tag{2.5}
\]

## 3. Seven-connectivity gives literal portal surplus

For each arm `A_i`,

\[
N_G(A_i)\subseteq\{y\}\cup
       \bigcup_{Q_j\ne U}N_{Q_j}(A_i).                 \tag{3.1}
\]

The root-free arm has no edge to `x`, no edge to another component of
`D-y`, and no edge to `U`.  The bag `U` survives outside
`A_i union N(A_i)`, so the displayed set is an actual separator.
Seven-connectivity therefore gives

\[
\sum_{Q_j\ne U}|N_{Q_j}(A_i)|\ge6.                    \tag{3.2}
\]

Thus every arm has at least six actual portal vertices distributed among
four foreign bags.

In the two-arm equality state, (2.5) strengthens this to

\[
|N_{Q_1}(A_1)|+|N_{Q_2}(A_1)|\ge6,
\qquad
|N_{Q_3}(A_2)|+|N_{Q_4}(A_2)|\ge6.                    \tag{3.3}
\]

Hence one owned bag of each arm contains at least three distinct literal
arm portals.

## 4. Exact terminal

The minimum singleton/root obstruction is therefore one of only three
unbounded structural forms.

1. `m=0`: `D-y` is connected, so the blocker is the singleton `{y}`.
2. `m=1`: one root-free arm owns at least two of the four accessible
   duties and has at least six literal portal vertices.
3. `m=2`: two root-free arms own complementary duty pairs as in (2.4),
   each has at least six literal portals across its own two bags, and the
   remaining component `A_0` carries every other root of `D` and the entire
   `U` duty.

This is a host-level classification, not a quotient contact list.  The
remaining closure must use the repeated literal portals in (3.2)--(3.3) to
split a foreign carrier, or combine the safe contraction of `xy` with the
exact one- or two-arm gate.  Static duty ownership alone admits reversible
`K_3 join C_4`-type rotations and is not terminal.
