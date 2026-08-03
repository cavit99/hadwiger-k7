# Internal audit: four-distinct-miss `P_3` atom

**Audited theorem:**
[`hc7_k7minus_p3_atom_yuan_draft.md`](hc7_k7minus_p3_atom_yuan_draft.md)

**Theorem SHA-256:**
`da61d9d2ff671a51055e86f7499fe7ec82ba5143919d7456cb5d7f84396ef452`

**Audited verifier:**
[`hc7_k7minus_p3_atom_yuan_verify.py`](hc7_k7minus_p3_atom_yuan_verify.py)

**Verifier SHA-256:**
`0be573df800d1c35d3ea740ea08ab0e5d30335bcfccf363b1c725a2655d257cf`

**Verdict:** **GREEN**, conditional on the stated generalised-atom
entrance.  The unbounded proof is written; its seven-vertex boundary lemma
is computer-assisted.  This is a separate internal audit, not external peer
review.

## Mathematical check

For the path `A=a-b-c`, the four distinct misses give

\[
 |N(a)\cap N(b)|=|N(b)\cap N(c)|=4.
\]

Thus both internal edges are density-safe when `q(G)>=1`.  Mader's atom
crossing lemma applied to the defining crossing separator puts all three
vertices of `A` in that separator.  Hence `H=G-A` is four-connected and has
a four-separator.

For every fragment `F` of `H`, seven-connectivity forces every vertex of
`A` to have a neighbour in `F`.  Its lifted separator is therefore
`N_H(F)\cup A`; it contains the safe edge `ab`.  Thus `F` is an
`\mathcal X`-fragment of `G`, and Mader's trace lemma gives

\[
                         |F\cap N(A)|\ge3.              \tag{1}
\]

If a boundary vertex `w` is good, its witnessing safe edge into `A` lies
in an order-seven separator.  The atom crossing lemma again puts `A` in
that separator, proving `\kappa(H-w)=3`.

The proof also checks the part of Yuan's definition that is easy to omit:
every fragment of `H-w` meets the remaining good set.  Indeed, a contrary
fragment with three-vertex boundary lifts to an exact seven-separator
containing the safe edge witnessing `w`.  Mader's trace lemma again gives
three boundary roots in the fragment, whereas at most the two non-good
roots are available.  This is a contradiction.

Consequently `H` is a noncomplete `W`-locally `1`-critical
four-connected graph in Yuan's exact `|W'|<=1` convention.  Yuan supplies
four fragments with pairwise disjoint good-root traces.  Trace bound (1)
immediately excludes at most one non-good root.  With two non-good roots,
at least three of the four good-root traces are singletons.  Two
corresponding fragments contain both non-good roots.  If their complementary
fragments are disjoint, their two disjoint three-root traces cannot fit in
the five good roots.  Otherwise standard fragment uncrossing produces a
fragment with empty good-root trace.  Both alternatives contradict local
criticality.

## Finite check

I reran

```text
uv run --with networkx==3.6.1 python \
  active/hc7_k7minus_p3_atom_yuan_verify.py
```

under NetworkX 3.6.1.  It reproduced:

```text
two_packet_target_free_boundaries=700
non_good_distribution=(451944, 121820, 14128, 108)
three_non_good_cases=108
three_non_good_graph6=FD^Ww
expanded_P3_K7minus_certificates=108
expanded_P3_survivors=0
exceptional_digest=3945e33ab729bfd1c709fcc3a326620f222de6a178a93dec60bae6cbdcd183ec
certificate_digest=1538af1f3ad9c958dc6411c2bbfb346b762ddacbaa8115f0478a90bf1a8e03d4
```

The search covers all 1,044 unlabelled seven-vertex boundary graphs and all
840 ordered choices of the four distinct misses.  The minor predicate is an
exact spanning partition search for seven connected branch sets with at
most one missing adjacency.  Every generated certificate is checked again
by a separate validation routine.  All checks remain active under
`python -O`.

The two recorded empty-boundary triangle quotients are diagnostics only;
they are not used to prove the path theorem.

## External inputs and scope

The proof uses Mader's generalised atom crossing and trace lemmas in the
form of Chan, *Contractible edges* (2016), Lemmas 7.7 and 7.19, and Yuan,
*A note on fragments in a locally k-critical n-connected graph* (2009),
Theorem 3.  Their hypotheses match the uses above.

The conclusion eliminates exactly the four-distinct-miss degree-seven
`P_3` atom once the live `\mathcal X`-critical atom entrance has been
established.  It does not eliminate singleton atoms, order-two atoms, or
the two mixed triangle residues at surplus one, and it does not prove the
`4n-2` extremal target.
