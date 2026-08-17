# The order-seven `i=3` Hall return is terminal

**Status:** proved by one finite internal-support classification followed by
a singleton degree contradiction, and independently cold-audited.  The excess
and packet hypotheses are not needed.

## 1. Normalised return

Let `U={u_0,u_1,u_2}` be the three singleton bags in an
inclusion-minimal Hall-deficient family.  Put

```text
R=N_S(U),        W=C-U,        T=S-R.
```

The order-seven Hall profile gives

```text
|R|=2,   |W|=|T|=4,
```

a perfect matching from `W` to `T`, and a perfect matching from `U-{u}`
to `R` for every `u in U`.  It also gives the collective domination

```text
N_C(U)=W.                                           (1.1)
```

The other two bags of the spanning ordinary `K_5^-` model partition `W`.
Their sizes are `3,1` or `2,2`, both are connected, and together with the
three singleton bags their quotient has at most one missing pair.

The bipartite incidence graph between `U` and `R` contains a spanning
four-edge path.  Indeed, some vertex of `U` must see both roots: otherwise
all three vertices have a unique root neighbour and deleting the vertex
with the other neighbour violates Hall.  After naming this vertex `u_0`,
the other two vertices must see different roots.  Retain just the path

```text
u_1-r_0-u_0-r_1-u_2.                               (1.2)
```

Deleting other boundary incidences only makes a rooted model harder.

## 2. Exact finite support lemma

### Lemma 2.1

Retain a spanning tree in each of the two complementary model bags, one
actual edge for nine required quotient contacts, one `U`-neighbour for every
vertex of `W` not yet covered, the matching from `W` to `T`, and the path
(1.2).  Then either this retained graph has a punctured rooted `K_5^-`
model, or, up to exchanging `u_1,u_2` and arbitrarily relabelling `W`, its
internal edge set is

```text
u_0u_1, u_0u_2, u_0w_2, u_0w_3,
u_1w_2, u_1w_3,
u_2w_0, u_2w_1,
w_0w_1, w_0w_3, w_1w_2.                            (2.1)
```

Moreover, adding any one missing internal edge to (2.1) creates a punctured
rooted model.

### Finite proof

There are only two bag-size shapes.  For each, the verifier chooses the two
bag-tree edges, chooses the one quotient pair allowed to be absent, chooses
one endpoint edge for each of the other nine pairs, and then gives every
still-uncovered vertex of `W` one neighbour in `U`.  Duplicate edge masks
are coalesced.  This gives exactly

```text
shape (3,1): 5391 supports,
shape (2,2): 4032 supports.
```

First the verifier tries every model obtained solely from one of the six
perfectly matched shore vertices as the anchor of each rooted bag, with the
two remaining vertices distributed among those bags or left unused.  Every
`(3,1)` support closes.  Exactly `24` of the `(2,2)` supports need the full
rooted check.

For each of the three possible centres in (1.2), the full check assigns each
of the seven shore vertices to one of five rooted bags or to no bag, for
each omitted root.  It tests rooted connectedness and all ten bag contacts.
Exactly `24` coloured supports survive.  Canonicalisation under the exchange
of the two Hall leaves and all `4!` permutations of `W` puts all of them in
one orbit, represented by the 21-bit edge mask

```text
0x69e33,
```

which is precisely (2.1).  It has eleven edges.  Finally, the checker tests
all `24*10=240` one-edge extensions and finds a rooted model in every one.
This proves both assertions.  \(\square\)

The enumeration is over the protocol-generated retained supports described
above.  Every graph in the Hall return contains one such support, and every
generated support is tested.  If the support already roots, so does the
original graph; if it is (2.1), any additional internal edge roots by the
last assertion.

## 3. Degree contradiction

Suppose the Hall return has no punctured rooted model.  Lemma 2.1 forces the
whole internal graph to be (2.1).  Both Hall leaves `u_1,u_2` have exactly
three neighbours in `C`.  By definition of the deficient root set,

```text
N_S(u_j) subseteq R,       |R|=2.
```

Thus each Hall leaf has total degree at most five.  Equivalently, the
singleton set `{u_j}` violates

```text
|N_C({u_j})|+|N_S({u_j})|>=6.
```

This contradicts the relative six-connectivity inherited from a
six-connected host.  Hence every `i=3` order-seven Hall return has a
punctured rooted `K_5^-` model.

## 4. Reproduction

Build and run the standard-C verifier with

```text
cc -std=c11 -O2 -Wall -Wextra -Werror -pedantic \
  active/experiments/sparse_sixcut_order_seven_i3_classification/verify.c \
  -o /tmp/order7_i3_verify
/tmp/order7_i3_verify
```

The expected terminal line is

```text
order-seven i=3 internal classification: PASS
```
