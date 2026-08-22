/* Independent 2^21 verifier for the seven-vertex factor lemma.

   Every triangle-free graph T on seven labelled vertices with alpha(T)<=3
   has either a Hamilton C7 or a spanning C5 plus a disjoint edge.  The
   program checks the statement directly from edge masks; it uses no graph
   generation or isomorphism code. */

#include <stdint.h>
#include <stdio.h>

static int bit_index(int u, int v) {
    if (u > v) { int z = u; u = v; v = z; }
    int bit = 0;
    for (int i = 0; i < u; ++i) bit += 7 - i - 1;
    return bit + v - u - 1;
}

static int edge(uint32_t graph, int u, int v) {
    return (graph >> bit_index(u, v)) & 1U;
}

static int triangle_free(uint32_t graph) {
    for (int a = 0; a < 7; ++a)
        for (int b = a + 1; b < 7; ++b)
            for (int c = b + 1; c < 7; ++c)
                if (edge(graph, a, b) && edge(graph, a, c) && edge(graph, b, c))
                    return 0;
    return 1;
}

static int alpha_at_most_three(uint32_t graph) {
    for (int a = 0; a < 7; ++a)
        for (int b = a + 1; b < 7; ++b)
            for (int c = b + 1; c < 7; ++c)
                for (int d = c + 1; d < 7; ++d)
                    if (!edge(graph, a, b) && !edge(graph, a, c) &&
                        !edge(graph, a, d) && !edge(graph, b, c) &&
                        !edge(graph, b, d) && !edge(graph, c, d))
                        return 0;
    return 1;
}

static int next_permutation(int *a, int n) {
    int i = n - 2;
    while (i >= 0 && a[i] >= a[i + 1]) --i;
    if (i < 0) return 0;
    int j = n - 1;
    while (a[j] <= a[i]) --j;
    int z = a[i]; a[i] = a[j]; a[j] = z;
    for (int l = i + 1, r = n - 1; l < r; ++l, --r) {
        z = a[l]; a[l] = a[r]; a[r] = z;
    }
    return 1;
}

static int has_c7(uint32_t graph) {
    int p[6] = {1, 2, 3, 4, 5, 6};
    do {
        if (p[0] > p[5]) continue; /* quotient reversal */
        int last = 0, ok = 1;
        for (int i = 0; i < 6; ++i) {
            if (!edge(graph, last, p[i])) { ok = 0; break; }
            last = p[i];
        }
        if (ok && edge(graph, last, 0)) return 1;
    } while (next_permutation(p, 6));
    return 0;
}

static int five_cycle_on(uint32_t graph, int vertices[5]) {
    /* Fix vertices[0] and enumerate the other four, quotienting reversal. */
    int p[4] = {vertices[1], vertices[2], vertices[3], vertices[4]};
    do {
        if (p[0] > p[3]) continue;
        int last = vertices[0], ok = 1;
        for (int i = 0; i < 4; ++i) {
            if (!edge(graph, last, p[i])) { ok = 0; break; }
            last = p[i];
        }
        if (ok && edge(graph, last, vertices[0])) return 1;
    } while (next_permutation(p, 4));
    return 0;
}

static int has_c5_plus_edge(uint32_t graph) {
    for (int u = 0; u < 7; ++u) {
        for (int v = u + 1; v < 7; ++v) {
            if (!edge(graph, u, v)) continue;
            int rest[5], at = 0;
            for (int x = 0; x < 7; ++x)
                if (x != u && x != v) rest[at++] = x;
            if (five_cycle_on(graph, rest)) return 1;
        }
    }
    return 0;
}

int main(void) {
    uint64_t trianglefree = 0, eligible = 0, c7 = 0, c5e = 0, both = 0;
    uint64_t nonham_min_degree_two = 0;
    uint32_t first_failure = 0;
    for (uint32_t graph = 0; graph < (1U << 21); ++graph) {
        if (!triangle_free(graph)) continue;
        ++trianglefree;
        if (!alpha_at_most_three(graph)) continue;
        ++eligible;
        int seven = has_c7(graph);
        int five_edge = has_c5_plus_edge(graph);
        c7 += seven;
        c5e += five_edge;
        both += seven && five_edge;
        if (!seven) {
            int minimum = 7;
            for (int u = 0; u < 7; ++u) {
                int degree = 0;
                for (int v = 0; v < 7; ++v)
                    if (u != v && edge(graph, u, v)) ++degree;
                if (degree < minimum) minimum = degree;
            }
            if (minimum >= 2) ++nonham_min_degree_two;
        }
        if (!seven && !five_edge && !first_failure) first_failure = graph + 1;
    }
    printf("graphs %u\n", 1U << 21);
    printf("triangle_free %llu\n", (unsigned long long)trianglefree);
    printf("triangle_free_alpha_at_most_3 %llu\n", (unsigned long long)eligible);
    printf("with_C7 %llu\n", (unsigned long long)c7);
    printf("with_C5_plus_edge %llu\n", (unsigned long long)c5e);
    printf("with_both %llu\n", (unsigned long long)both);
    printf("nonhamiltonian_min_degree_at_least_2 %llu\n",
           (unsigned long long)nonham_min_degree_two);
    printf("failures %d\n", first_failure != 0);
    if (first_failure) printf("first_failure_mask %u\n", first_failure - 1);
    return first_failure != 0;
}
