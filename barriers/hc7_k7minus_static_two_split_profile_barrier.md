# Static contact profiles do not terminalise two co-bagged coordinates

**Status:** explicit finite barrier with a deterministic exhaustive verifier.
This is a barrier to a static branch-set allocation claim, not to the
cross-signature root-bag theorem, the `K_7^-` six-colour conjecture, or
`HC_7`.

The verifier is
[`hc7_k7minus_static_two_split_profile_barrier_verify.py`](hc7_k7minus_static_two_split_profile_barrier_verify.py).

## 1. Exact assertion refuted

The following purely model-theoretic assertion is false.

> **Static two-split profile assertion.**  Suppose a graph `Q` has a
> labelled `K_6`-minor model
>
> \[
>                         R,S,B_1,B_2,B_3,B_4,
> \]
>
> where `R` and `S` are edges.  Split each of them into its two singleton
> ends.  If `Q` has no `K_5` subgraph and no `K_7^-` minor, then one of the
> two splits has at least four foreign model bags adjacent to both ends.

Here the five foreign bags for the split of `R` are `S,B_1,...,B_4`, and
symmetrically for `S`.

## 2. Construction

Let

\[
                     Q=K_{2,2,2,2}=K_8-4K_2.          \tag{2.1}
\]

Label its four independent parts as

\[
 \{0,6\},\qquad \{1,7\},\qquad
 \{2,4\},\qquad \{3,5\}.                             \tag{2.2}
\]

Take

\[
 R=\{0,1\},\qquad S=\{2,3\},\qquad
 B_1=\{4\},\ B_2=\{5\},\ B_3=\{6\},\ B_4=\{7\}.   \tag{2.3}
\]

The six sets in (2.3) are connected and pairwise adjacent, so they form a
labelled `K_6` model.  The two root bags are the coordinate edges

\[
                         e=01,\qquad f=23.             \tag{2.4}
\]

For the split of `R`, the bags `S,B_1,B_2` meet both ends, while `B_3`
meets only `1` and `B_4` only `0`.  Thus its double-contact score is
exactly three.  Symmetrically, the split of `S` also has score three.

The graph is complete four-partite, so it has no `K_5` subgraph.  It also
has no `K_7^-` minor.  Indeed, seven branch sets in an eight-vertex graph
use either seven singleton vertices or one connected pair and six
singletons.  In the first case at least three complete part-pairs remain
and give three missing adjacencies.  In the second case the two parts not
met twice by the connected pair remain as two missing adjacencies between
singleton branch sets.  Either count exceeds the one missing adjacency
allowed in `K_7^-`.

This proves the advertised counterexample.

## 3. Exhaustive profile diagnostic

There is a useful sharpness check.  Keep two split coordinate bags and
four singleton foreign bags.  Make the foreign bags a clique, require each
foreign bag to meet at least one side of each split, and require the two
coordinate bags to be adjacent.  These are exactly the static incidences
forced by the labelled `K_6` model when its two coordinate bags are
distinct.

There are `98,415` labelled incidence profiles.  The verifier checks every
one.  Of the `84,928` in which both double-contact scores are at most
three, `79,768` have no `K_7^-` minor in the eight-set quotient.  Even
requiring quotient clique number at most four leaves `30,652` profiles.
There are `384` target-free, clique-number-at-most-four profiles in which
both scores equal three.

If one additionally imposes minimum quotient degree six, precisely `24`
labelled profiles remain, and every one is isomorphic to (2.1).  This is
the unique unlabelled maximally saturated static obstruction.  Minimum
degree six in this contracted quotient is not a consequence of
seven-connectivity of the host.

## 4. What the profile abstraction can and cannot retain

The static quotient faithfully retains the following necessary data:

* the two co-bagged coordinate pairs and the common labelled `K_6` model;
* all contacts between the eight split branch sets; and
* target exclusion in the one useful direction: a `K_7^-` minor in the
  quotient would lift to the host.

It does **not** faithfully retain three other host hypotheses.

1. Vertex connectivity is not monotone under branch-set contraction.
   The example has connectivity six, and seven-connectivity of the host
   does not justify imposing seven-connectivity on this quotient.
2. Literal `K_5`-subgraph exclusion does not normally descend to a
   branch-set quotient, because its clique edges may have different
   witnesses.  The example satisfies the stronger quotient condition
   anyway.
3. The signatures `EP,PE,EE` and the universal absence of `PP` are
   properties of **all six-colourings of one deletion graph**.  A contact
   profile contains no colours, Kempe components or boundary partitions.
   Attaching the three positive signature labels to its vertices does not
   encode the universal fourth-corner prohibition.

The last point is visible in the example.  For `H=Q-\{e,f\}`, all four
signatures `EP,PE,EE,PP` occur.  Thus the construction does not refute a
theorem that genuinely converts the absence of `PP` into contact with the
fixed model.  It proves that target exclusion, even combined with the
strongest possible static two-split profile and quotient `K_5` exclusion,
does not perform that conversion by itself.

Consequently a successful cross-signature proof must retain an actual
Kempe transition or boundary partition while assigning model bags.  A
finite enumeration of uncoloured deficiency profiles cannot supply the
missing step.

## 5. Reproduction

From the repository root run

```text
python3 barriers/hc7_k7minus_static_two_split_profile_barrier_verify.py
```

The script uses only the Python standard library.  It verifies the explicit
barrier, enumerates all labelled profiles described in Section 3, checks
`K_7^-` minors exactly on eight vertices, and prints the retained counts.
