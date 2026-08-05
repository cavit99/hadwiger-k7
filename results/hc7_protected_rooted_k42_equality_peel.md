# A protected peel at the rooted `K_{4,2}` equality threshold

**Status:** written proof; separate internal audit GREEN for the revision
identified in the adjacent audit.  This is a computation-free rooted-minor
reduction.  It does not prove `(E5)`, the seven-connected `4n-2` target,
Conjecture 21, or `HC_7`.

Let `Z` be a four-set in a graph `J`.  A `Z`-rooted `K_{4,2}` model has
four disjoint connected root bags, one containing each member of `Z`, and
two further connected helper bags, each adjacent to every root bag.  A
`Z`-rooted `K^*_{4,2}` model additionally requires the helper bags to be
adjacent.

The proof refines the contractions in Norin--Totschnig, Lemma 12.  We use
their terminology below.  In a normalised rooted `K_{4,2}` model, the four
minimal root trees end at distinct **portal vertices**

\[
                         Z'=\{v_1,v_2,v_3,v_4\},
\]

and the two maximal helper subgraphs have all their external neighbours in
`Z'`.  Because a rooted `K^*_{4,2}` model is excluded, the helpers are
anticomplete.  Completing `Z'` to a clique cannot create a rooted
`K^*_{4,2}` model: each added edge has its ends in two distinct nominated
root bags and is irrelevant to every required root--helper or
helper--helper adjacency.

## Theorem (protected rooted-equality peel)

Let `(J,Z)` be internally four-connected and suppose

\[
                        |E(J)|=4|V(J)|-10.             \tag{1}
\]

Assume that `J` has no `Z`-rooted `K^*_{4,2}` model.  Let `T` be any set
of protected labelled vertices disjoint from `Z`.  Then at least one of the
following holds.

1. `J` has no `Z`-rooted `K_{4,2}` model.
2. `J` has a `Z`-rooted `K_{4,2}` model in which a helper bag meets `T`.
3. There is a minor `J'` of `J` with strictly fewer vertices such that:

   - every vertex of `Z\cup T` survives as a distinct labelled vertex;
   - `(J',Z)` is internally four-connected;
   - `J'` has no `Z`-rooted `K^*_{4,2}` model; and
   -
     \[
                          |E(J')|=4|V(J')|-10.         \tag{2}
     \]

Consequently, if outcome 2 never occurs, repeated applications of outcome
3 terminate at a smaller equality pair with no `Z`-rooted `K_{4,2}`
model.

### Proof

Suppose outcome 1 fails.  Choose a `Z`-rooted `K_{4,2}` model with its four
root subgraphs minimal and its two helper subgraphs `J_1,J_2` maximal, as in
the proof of Norin--Totschnig, Lemma 12.  If a helper meets `T`, outcome 2
holds.  We may therefore assume

\[
                         T\cap(V(J_1)\cup V(J_2))=\varnothing.       \tag{3}
\]

The normalisation in that proof gives the portal set `Z'` described above.
For `i\in\{1,2\}`, the helper-side pair

\[
                  (J[V(J_i)\cup Z'],Z')
\]

is internally four-connected and has no `Z'`-rooted `K^*_{4,2}` model; a
model on that side would extend along the four root paths to a forbidden
`Z`-rooted model in `J`.  After completing `Z'` to a clique,
Norin--Totschnig, Lemma 12, gives

\[
 |E(J[V(J_i)\cup Z'])|-|E(J[Z'])|
 \le4|V(J_i)|.                                      \tag{4}
\]

We now use the two contractions constructed explicitly in their proof.

If at least one helper is nonsingleton, the rooted-`K_4^-` contraction on
that helper followed by contraction of the other helper produces a minor
`J'` with

\[
 V(J')=V(J)\setminus(V(J_1)\cup V(J_2)),
\]

where the helper vertices have been contracted onto their portals.  The
portal set becomes a clique, `(J',Z)` is internally four-connected, and a
`Z`-rooted `K^*_{4,2}` model in `J'` would lift to one in `J`.  Inequality
(4) gives

\[
 |E(J')|
 \ge |E(J)|-4|V(J_1)|-4|V(J_2)|
 =4|V(J')|-10.                                      \tag{5}
\]

If both helpers are singletons, write `V(J_i)=\{u_i\}`.  Their external
neighbourhood is exactly `Z'`.  The first minor in the published proof is
`J/u_1v_1`, which loses at most four edges.  If the resulting rooted pair
is internally four-connected, take it as `J'`.  Otherwise the separation
analysis in that proof, after relabelling the portals, produces

\[
                         J'=J/u_1v_2/u_2v_4.          \tag{6}
\]

The two contractions lose at most eight edges in total, make `Z'` a
clique, and restore internal four-connectivity.  Again a forbidden rooted
model in `J'` would lift to `J`.  In either singleton subcase,

\[
                         |E(J')|\ge4|V(J')|-10.       \tag{7}
\]

In all cases only helper vertices are removed.  By (3), no protected
vertex is removed.  A helper is contracted into a portal, and in the
two-contraction repair the two helpers are contracted into distinct
portals.  Thus no two vertices of `Z\cup T` are identified; a protected
portal remains the labelled surviving vertex of its contracted bag.

Finally, `(J',Z)` is internally four-connected and has no rooted
`K^*_{4,2}` model.  Lemma 12 supplies the reverse inequality

\[
                         |E(J')|\le4|V(J')|-10.
\]

Together with (5) or (7), this proves (2).  At least one helper vertex was
contracted, so `|V(J')|<|V(J)|`.  This proves outcome 3 and the theorem.
\(\square\)

## Scope

The theorem preserves specified labels inside the rooted pair and gives a
well-founded equality reduction.  It does not show that replacing a lobe
of a five- or seven-connected host by `J'` preserves the host's
connectivity, external incidences, or exact separator structure.  A host
reinsertion theorem and a classification of the terminal equality pairs
remain separate obligations.

## External source

Sergey Norin and Agnès Totschnig,
[*Every graph with no `K_7^\vee`-minor is 6-colourable*, Lemma 12 and its proof](https://arxiv.org/abs/2507.03244).
