# Decisive E5 proof gate

**Repository baseline:** `2af5d1c2c0080acece7a71f976f6456f273bdf66`  
**Gate length:** six focused rounds  
**Status:** E5 is not proved; no counterexample was found. The gate nevertheless produced two unbounded coefficient-four theorems, one of which applies directly to the primary seven-connected `4n-2` target. The new deductions below have a written proof but have not yet received an independent repository audit.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## Gate verdict

The gate is a **qualified GO**, not an E5 victory.

- **No verified counterexample:** exhaustive exact-density search through order nine and targeted searches in the current one-six-full, two-six-full `K_2`, and both-endpoints families found none.
- **No E5 proof:** the one-six-full rows, the exact `K_2` two-six-full row, and the five-connected self-similar/both-endpoints rows are not all closed.
- **Qualifying theorem obtained:** the six-connected `K_4`-reserve inequality below transfers immediately to every essential-edge six-separation in the primary `4n-2` programme.
- **Ranked peel obtained:** the protected rooted-equality theorem gives a label-preserving, order-decreasing coefficient-four reduction at the sharp `4|V|-10` rooted threshold.

Further finite boundary catalogues would not be a qualifying continuation. The next useful work must attack the terminal rooted equality class or combine the reserve inequality over several boundary `K_4`s.

---

# Round 1 — global and live-family counterexample search

## Exact global search

The direct connected-branch-set oracle exhausts every partition of every used vertex subset into seven nonempty connected bags and checks whether the quotient has at most one missing pair.

- Order eight, exact E5 size `25`:

  ```text
  n8 exact total=3276 5conn=2996 negative=0
  ```

- Order nine, exact E5 size `29`:

  ```text
  n=9 m=29 total=8347680 target_free=0
  five_connected_target_free=0
  ```

Thus every labelled graph at the exact E5 density on eight or nine vertices already has a `K_7^-` minor; connectivity is unnecessary at order nine.

## Current residual families

The minimum live lobe has `a>=8`, so the smallest kernel hosts have order fifteen. Targeted generation retained the exact kernel contacts, exact total size, five-connectivity, and the current boundary restrictions.

```text
K2-one-full: trials=12000 built=307 five=210 pos=210 unk=0 neg=0
K2-two-full: trials=12000 built=65 five=44 pos=44 unk=0 neg=0

P3 favourable:   built=17   five=17   pos=17   neg=0
P3 other:         built=1166 five=1026 pos=1026 neg=0
K3 favourable:   built=24   five=22   pos=22   neg=0
K3 other:         built=1318 five=1079 pos=1079 neg=0
```

These are stochastic falsification screens, not unbounded evidence.

## Minimum literal hosts

```text
one-six-full/full-edge K2: total=35960 structural=2268 five=2268 negative=0
K2 two-full component orders 2+3: total=5718 structural=4896 negative=0
both-endpoints minimum hosts: total=144 five=132 positive=144 negative=0
```

**Round result:** no counterexample.

---

# Round 2 — structured exact-density constructions

The most dangerous clique-sum construction found was a common `K_5` with three two-vertex lobes. In each lobe the two vertices are adjacent and independently miss two distinct boundary roots. Each seven-vertex block is `K_7` with a two-edge matching deleted; three such blocks give

```text
n=11, e=37=4n-7,
```

and the resulting graph is five-connected. All `20^3=8000` labelled choices contain `K_7^-`:

```text
total=8000 c5=8000 pos=8000 neg=0
```

The alternative orientation in which both lobe vertices miss the same root is target-free in small quotients, but is only four-connected: deleting the other four members of the common `K_5` separates the lobe.

A broader random exact-density screen through order fifteen also found no negative five-connected graph. Two capped searches at orders fourteen and fifteen were rerun without the cap and were positive.

## Contractibility route

An exact E5 enemy has average degree

\[
\overline d=8-\frac{14}{n}.
\]

For `n>=28` this is at least `15/2`. The Ando–Egawa–Kriesell theorem therefore guarantees a 5-removable or 5-contractible edge. This does not close E5:

- deleting a removable edge leaves `4n-8`, one edge below the E5 threshold;
- contracting an edge preserves the coefficient-four threshold only when the edge has at most three common neighbours, which the theorem does not guarantee.

**Round result:** no counterexample; the global contractibility route fails exactly at the one-edge deficit.

---

# Round 3 — an unbounded theorem for the primary `4n-2` target

## Theorem A — six-connected `K_4`-reserve inequality

Let `H` be a six-connected `K_7^-`-minor-free graph. Let `S` be a six-cut such that

\[
H-S=A\mathbin{\dot\cup}B,
\]

where `A,B` are connected and every member of `S` has a neighbour in each shore. Suppose

\[
S=Z\mathbin{\dot\cup}\{r,s\},\qquad |Z|=4,
\qquad H[Z]=K_4.
\]

For `X in {A,B}`, put

\[
\delta_X=|E(H[X])|+|E_H(X,S)|-4|X|.
\]

Then

\[
\boxed{\delta_X\le |E_H(X,\{r,s\})|.} \tag{A}
\]

### Proof

Fix a shore `X` and let `Y` be the other shore.

First, `(H[X union Z],Z)` is internally four-connected. A rooted separation of order at most three has its non-root side inside `X`; adjoining `r,s` to its separator gives a cut of `H` of order at most five separating that side from `Y`, contrary to six-connectivity.

Next, `(H[X union Z union {r}], Z union {r})` is internally five-connected. A forbidden rooted separation of order at most four, together with the omitted vertex `s`, again gives a cut of `H` of order at most five.

Suppose `H[X union Z]` contains a `Z`-rooted `K^*_{4,2}` model. View it in the larger graph `H[X union Z union {r}]`. The fifth-root augmentation lemma gives such a model with `r` in one helper bag. The four root bags are pairwise adjacent through the literal clique `H[Z]`, and the two helpers are adjacent by definition. Thus the six bags form a `K_6` model. The opposite shore `Y` is a seventh connected branch set adjacent to all four root bags and to the helper containing `r`; it may miss only the other helper. This is a `K_7^-` model, a contradiction.

Therefore `H[X union Z]` has no `Z`-rooted `K^*_{4,2}` model. Norin–Totschnig Lemma 12 gives

\[
 |E(H[X\cup Z])|\le4(|X|+4)-10=4|X|+6.
\]

Since `H[Z]=K_4`, this is

\[
 |E(H[X])|+|E_H(X,Z)|\le4|X|.
\]

Adding the contacts to `r,s` and subtracting `4|X|` proves (A). \(\square\)

## Direct transfer to the primary target

Apply Theorem A to the six-connected graph `H=G-xy` supplied by the audited essential-edge theorem for an edge-minimal seven-connected target-free graph. Its exact identity is

\[
\delta_A+\delta_B=21+q(G)-|E(G[S])|.
\]

If `Z` is a literal `K_4` in `G[S]` and `S-Z={r,s}`, Theorem A gives

\[
21+q(G)-|E(G[S])|
 \le |E_G(A\cup B,\{r,s\})|.
\tag{B}
\]

Writing `epsilon=1` when `rs` is a boundary edge and zero otherwise, exact cancellation inside the six-set yields the clean degree-sum consequence

\[
\boxed{d_G(r)+d_G(s)\ge15+q(G)+\epsilon.} \tag{C}
\]

In particular, the two vertices outside a boundary `K_4` cannot both have degree seven. If they are adjacent, their degree sum is at least sixteen even at zero surplus.

This is an unbounded theorem directly on the `4n-2` proof spine. It is not a finite case list.

**Round result:** qualifying success.

---

# Round 4 — a protected coefficient-four ranked peel

## Theorem B — protected rooted-equality peel

Let `Z` be a four-set in a graph `J`. Assume

\[
(J,Z)\text{ is internally four-connected},\qquad
|E(J)|=4|V(J)|-10,
\]

and `J` has no `Z`-rooted `K^*_{4,2}` model. Let `T` be any set of protected labelled vertices disjoint from `Z`.

Then at least one of the following holds.

1. `J` has no `Z`-rooted `K_{4,2}` model.
2. `J` has a `Z`-rooted `K_{4,2}` model in which one of the two helper bags meets `T`.
3. `J` has a proper minor `J'` such that:
   - all vertices of `Z union T` survive as distinct labelled vertices;
   - `(J',Z)` is internally four-connected;
   - `J'` has no `Z`-rooted `K^*_{4,2}` model; and
   -
     \[
     |E(J')|=4|V(J')|-10.
     \]

Consequently, if outcome 2 never occurs, repeated applications of outcome 3 terminate at a smaller equality pair with no rooted `K_{4,2}` model.

### Proof

Assume a rooted `K_{4,2}` model exists. Choose its four root subgraphs minimally and its two helper subgraphs `J_1,J_2` maximally, exactly as in the proof of Norin–Totschnig Lemma 12. If a helper meets `T`, outcome 2 holds. Hence assume both helpers avoid `T`.

The normalized model supplies four distinct portal vertices `Z'={v_1,v_2,v_3,v_4}`. Every neighbour of a helper outside it lies in `Z'`, the helpers are anticomplete, and each pair

\[
(J[J_i\cup Z'],Z')
\]

is internally four-connected and has no rooted `K^*_{4,2}` model.

Complete `Z'` to a clique inside each helper-side graph. Adding edges only between distinct root vertices cannot create a rooted `K^*_{4,2}` model: those added edges join different root bags, whereas the target requires only root–helper and helper–helper adjacencies. Lemma 12 therefore gives

\[
 |E(J[J_i\cup Z'])|-|E(J[Z'])|\le4|J_i|. \tag{D}
\]

If one helper is non-singleton, the rooted-diamond contraction in the published proof contracts both helpers onto `Z'`, makes `Z'` complete, and produces a proper minor `J'` with

\[
 |E(J')|\ge |E(J)|-4|J_1|-4|J_2|
           =4|V(J')|-10.
\]

The construction preserves internal four-connectivity and the original four roots. A rooted model in `J'` would lift to one in `J`. Since the helpers avoid `T`, every protected label survives; contracting a helper into a protected portal does not identify two protected vertices. Lemma 12 supplies the reverse inequality, so equality holds.

If both helpers are singletons, the first contraction in the published proof loses at most four edges. If internal four-connectivity survives, it gives outcome 3 immediately. Otherwise the exact separation analysis in that proof gives two helper-to-portal contractions losing at most eight edges in total and restoring internal four-connectivity. The same density, model-lifting, and protected-label arguments again force exact equality.

Each peel strictly reduces order, so iteration terminates. \(\square\)

This theorem turns the sharp rooted threshold into a genuine well-founded reduction. Its terminal object is not classified here; the theorem is therefore a transfer tool, not an E5 proof.

**Round result:** a second unbounded theorem, label-preserving at the coefficient-four equality threshold.

---

# Round 5 — application to the live E5 branches

The two new theorems were pushed against the current residual families.

## Both-endpoints

At the rigid eleven-edge boundary, total opposite excess is six and the four-vertex core is a literal `K_4`. If the lifted six-cut has exactly two full shores and the relevant rooted pairs meet the hypotheses above, the rooted-model argument forces each closed shore onto the exact `4|V|-10` line. Theorem B can then peel density neutrally while preserving selected endpoint labels until a helper captures one of them or a terminal rooted-`K_{4,2}`-free equality pair appears.

The five-connected E5 host does not automatically give the six-connectivity used in Theorem A. Thus the theorem does not close every both-endpoints row in E5, even though it applies directly in the primary target.

## `K_2` one-six-full/full-edge equality

The live equality already has

\[
|E(G[C\cup(P-\{u\})])|=4|C\cup(P-\{u\})|-10.
\]

Theorem B applies after choosing four roots and protecting the fifth boundary label together with the two vertices of `C` adjacent to `u`. It gives a finite-rank, label-preserving rooted reduction unless a helper captures one of those protected contacts.

What remains unproved is that the resulting rooted minor preserves the full five-connected host when reinserted. Internal four-connectivity of the rooted pair is not enough by itself.

## `K_2` two-six-full

At boundary size seven, the exact negative quotient remains possible. Theorem A does not apply because the boundary has no literal `K_4`; Theorem B requires first producing an exact rooted equality shore with the correct four labels. No such unbounded placement theorem was proved in this round.

## One-six-full-only `K_2,P_3,K_3`

The closed shores lie at `4|V|-8` or `4|V|-9`, but the unrooted near-clique supplied by density still need not align with the low kernel. No label-preserving upgrade was obtained.

**Round result:** the theorems materially organize the live branches but do not prove E5.

---

# Round 6 — hostile falsification and stopping rule

A direct split-interface search was run to test whether the remaining `K_2` rows could be closed from contact distribution alone.

```text
negative split hosts=16840
194 distinct contact codes
```

Even for the unique seven-edge boundary in the two-six-full `K_2` row, there are sixty-six target-free split contact patterns. Thus a contact-only split lemma is false. This is not an E5 counterexample: the finite split hosts discard internal density and host connectivity. It proves that the next theorem must use the exact rooted equality or an equivalent internal invariant.

No actual five-connected `4n-7` counterexample survived any search.

Under the requested gate rule, the campaign stops here. The qualifying reason to continue later is Theorem A (direct transfer to `4n-2`) and Theorem B (unbounded ranked peel), not any finite catalogue.

---

# Exact final status

## Established in this gate, pending independent audit

1. **Six-connected `K_4`-reserve inequality** (Theorem A).
2. **Primary-target degree-sum corollary**
   \[
   d(r)+d(s)\ge15+q+\mathbf1_{rs}.
   \]
3. **Protected rooted-equality peel** (Theorem B).
4. **Contact-only splitting is insufficient**, even in the sharp seven-edge `K_2` boundary.

## Not established

- E5.
- A five-connected `4n-7` counterexample.
- A classification of terminal internally four-connected `4|V|-10` rooted pairs with no rooted `K_{4,2}` model.
- Preservation of five- or seven-connectivity after every protected equality peel.
- A label-preserving split of the exact `K_2` two-six-full family.

## Recommended next proof target

Do not run another boundary census. Attack the following unbounded terminal theorem:

> Classify internally four-connected equality pairs `(J,Z)` with
> `|E(J)|=4|V(J)|-10` and no `Z`-rooted `K_{4,2}` model, with one or two protected external-contact vertices. Show that the terminal pair either supplies the host composition, has a strict rooted separation yielding high-excess descent, or belongs to an explicit structural family that can be ruled out in both E5 and the `4n-2` essential-edge shore.

Theorem B ensures this target is well-founded; Theorem A supplies its first direct application on the primary proof spine.
