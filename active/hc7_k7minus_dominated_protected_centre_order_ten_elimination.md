# A protected exceptional centre eliminates the two-nonterminal kernel

**Status:** active written host theorem with one computer-assisted finite
composition lemma; internal hash-pinned audit adjacent.  The exact
order-ten kernel classification used below has a separate independent
audit.  This eliminates one unbounded kernel branch of the dominated
degree-eight centre case; it does not eliminate the order-eight or
order-nine kernels, prove Conjecture 21, or prove `HC_7`.

## 1. Setting

Let `G` be a simple graph satisfying

\[
 \kappa(G)\geq7,
 \qquad K_7^-\npreccurlyeq G.                          \tag{1.1}
\]

Let `u` have degree eight and suppose that `v\in N_G(u)` is adjacent to
every member of

\[
                         Q=N_G(u)-\{v\}.              \tag{1.2}
\]

Assume that `u` belongs to a fixed independent set of five degree-eight
centres

\[
                         Z=\{u,w_1,w_2,w_3,w_4\}.     \tag{1.3}
\]

Assume the proved connected dominated-centre reductions:

\[
 H=G-\{u,v\}\text{ is five-connected},               \tag{1.4}
\]

and

\[
 Q\cong C_5\mathbin{\dot\cup}K_2,
 \quad C_5\text{ with a pendant path of length two},
 \quad\text{or}\quad C_7.                             \tag{1.5}
\]

Let `w` be any one of the other four independent degree-eight centres.
Then `w\notin N_G[u]`, and hence

\[
                     w\in V(H)-Q.                    \tag{1.6}
\]

Protect the eight terminals

\[
                     T=Q\cup\{w\}.                  \tag{1.7}
\]

Apply terminal-legal contractions in `H` until a `T`-irreducible simple
three-connected rooted minor `K` is reached.  The audited terminal-kernel
theorem gives

\[
                         8\leq |V(K)|\leq10.          \tag{1.8}
\]

The point of protecting `w` is that its branch set cannot be absorbed into
a `Q`-rooted bag during this reduction.

## 2. Exact finite composition

The independently audited order-ten classification says that, if
`|V(K)|=10`, the following exact description applies.  The terminal graph
`K[T]` is a cycle of order eight.  There are two nonterminals `x,y`, they
are nonadjacent, and their neighbourhoods form complementary four-subsets
`A,B` of `T`.  Around the terminal cycle the membership word is

```text
AABBAABB
```

up to reversal, rotation, and interchange of `A,B`.  Every pair

\[
                         (a,b)\in A\times B            \tag{2.1}
\]

is a legal pair of owners: absorb the `x`-bag into the terminal bag rooted
at `a` and the `y`-bag into the terminal bag rooted at `b`.

### Lemma 2.1 (protected-centre order-ten composition)

Let `Q` be any of the three graphs in (1.5), on seven labelled vertices,
and let `w` be an eighth label.  For every labelled order-ten normal form
above, there are owners `(a,b)\in A\times B` and a vertex `r\in Q` with
the following property.

After absorbing the two nonterminals at `a,b`, the bag rooted at `w` is
adjacent to the bag rooted at `r`.  Absorb the former into the latter.
The resulting seven `Q`-rooted bags have an adjacency quotient `F` such
that

\[
                         Q\cup F\text{ contains }K_5^-\text{ as a minor}.
                                                               \tag{2.2}
\]

#### Computer-assisted proof

The self-contained deterministic verifier
[`verify.py`](experiments/dominated_singleton_protected_centre_order_ten/verify.py)
generates all `2,520` labelled undirected terminal cycles and the four
ordered `AABBAABB` shifts on each.  It therefore checks all `10,080`
labelled exact normal forms.  The generated template list has the pinned
SHA-256 digest

```text
78217d8621685a5839aa55172a51e3470297e6f989516c0455a4884471923418.
```

For each normal form and each of the three fixed labelled graphs `Q`, the
verifier ranges over all sixteen legal pairs in `A\times B`.  For every
resulting quotient it ranges over every actual neighbour in `Q` of the
`w`-rooted bag, performs the absorption, adds the literal edges of `Q`, and
tests (2.2) by exact deletion-and-contraction recursion.  It reports

```text
FCQ`_ templates=10080 failures=0
FCQb_ templates=10080 failures=0
FCp`_ templates=10080 failures=0
protected-centre order-ten composition templates=10080 q_types=3 failures=0
witness_digest bacd9ed98b08a1a0a60829250f852e54763e6fc812404e807f2cebf2cdc62202
```

Assertions enforce the template count, template digest, and absence of a
failed composition.  The minor recursion is exact: if a model on five
branch sets uses fewer than all current vertices, delete an unused vertex;
otherwise some branch set has more than one vertex and contains an edge
which may be contracted.  At order five, at least nine edges is precisely
a `K_5^-` subgraph. `\square`

## 3. Host theorem

### Theorem 3.1 (the protected order-ten kernel is impossible)

Under (1.1)--(1.7), the `T`-irreducible kernel `K` cannot have order ten.
Consequently

\[
                          |V(K)|\in\{8,9\}.           \tag{3.1}
\]

This holds separately for every choice of `w\in Z-\{u\}`.

#### Proof

Suppose that `|V(K)|=10`.  Lift its ten vertices through the
terminal-legal contractions to ten pairwise disjoint connected branch sets
which partition `V(H)`.  Eight contain their prescribed terminals, and
the other two contain no terminal.

Use the audited exact classification and choose the two legal owner bags
and the protected-terminal absorption supplied by Lemma 2.1.  The two
nonterminal bags may first be united with their owner bags because the
corresponding kernel edges are present.  The two owners are distinct, as
one lies in `A` and one in `B`.  The resulting eight terminal-rooted bags
remain connected and disjoint.

The bag rooted at `w` is adjacent to the selected bag rooted at `r\in Q`,
so their union is connected.  After this second absorption there are seven
pairwise disjoint connected bags, each containing a distinct member of
`Q`.  Their adjacency graph contains the quotient `F` in Lemma 2.1.  The
literal edges of `G[Q]` give all additional adjacencies of `Q`, so Lemma
2.1 and the rooted quotient lift give a `K_5^-` model in `H`, every branch
set of which meets `Q`.

Both `u` and `v` are adjacent to every member of `Q`, and `uv\in E(G)`.
The singleton branch sets `\{u\},\{v\}` therefore extend that model to a
`K_7^-` model in `G`, contrary to (1.1).  This excludes order ten.  The
bounds in (1.8) leave exactly (3.1).  The proof used no property of `w`
beyond (1.6), so it applies to each of the four choices. `\square`

## 4. Exact remaining residue and trust boundary

The proved conclusion is the unbounded elimination of the
two-nonterminal kernel.  For each protected exterior centre, the only
remaining irreducible kernels have:

1. order eight, with all vertices terminal; or
2. order nine, with one nonterminal and its complete legal-owner family.

The current exact-bundle generator gives a sharper **discovery diagnostic**
for these two orders.  After the same protected-centre absorption, it finds

\[
\begin{array}{c|ccc|c}
 &C_5\dot\cup K_2&C_5\text{ with pendant }P_2&C_7&\text{total}\\ \hline
 |K|=8&210&74&141&425\\
 |K|=9&430&86&287&803.
\end{array}                                            \tag{4.1}
\]

These are failed labelled compositions or exact owner families, not
unlabelled host types.  The order-eight census contains 196,976 labelled
minimal carriers; the order-nine census contains 2,408,280 exact labelled
owner families.  Their generation is deterministic and digest-pinned, but
the exact order-eight and order-nine catalogues have not received the
independent audit required for promotion.  Accordingly, neither the counts
in (4.1) nor a classification inferred from them is used in Theorem 3.1.

The four choices of protected centre now provide four overlapping rooted
kernel reductions of orders eight or nine.  A terminal continuation must
compare those overlapping reductions or use the operation labels to split
one of their rooted bags.  It may not assume that the four centres occupy
distinct bags in a seven-terminal model: protecting one centre at a time is
exactly what prevents that loss of provenance.

A further deterministic diagnostic tested the strongest direct use of the
coarser eight-terminal carrier theorem permitted by five-connectivity.
After deleting one `Q`-root and protecting two centres, every rooted
`K_{3,5}` and `F_8` carrier closes, but rooted cycle carriers survive for
every possible omitted root.  After deleting two `Q`-roots and protecting
three centres, every rooted `K_{3,5}` again closes, but cycle carriers and
some `F_8` carriers survive for every omitted pair.  These are quotient
route nonclosures, not host counterexamples.  They show why the exact
kernel contacts used in Theorem 3.1 cannot simply be replaced by the
coarse carrier trichotomy, even when more centres are protected.

## Dependencies and scope

- [three surviving dominated common-neighbour types and their rooted lift](hc7_k7minus_dominated_degree_eight_rooted_seven_carrier.md);
- [exact dominated exterior and four-coordinate response interface](hc7_k7minus_dominated_degree_eight_exterior_connectivity.md);
- [the exact eight-terminal bundle, order-ten classification](hc7_eight_terminal_exact_bundle.md);
- [independent audit of that order-ten classification](hc7_eight_terminal_exact_bundle_audit.md); and
- [the terminal-legal kernel theorem](../results/hc7_five_terminal_rooted_fan.md).

The degree-eight and response properties of the protected centre are not
spent in Theorem 3.1; they remain available for terminalising (3.1).  The
five-centre matching coordinates here are distinct from the eight-edge
induced forest used in the other global reduction.
