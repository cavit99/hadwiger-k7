/*
 * Independent exhaustive check for Lemma 2.1 of
 * exceptional_degree8_true_twin_exclusion.md.
 *
 * Enumerates all labelled simple graphs on {0,...,6}.  Every triangle-free
 * graph with no independent four-set must contain a spanning C7 or a
 * spanning C5 plus the edge on the two unused vertices.
 */
#include <stdint.h>
#include <stdio.h>

static int edge_id[7][7];

static int has_edge(uint32_t g, int u, int v) {
    return (int)((g >> edge_id[u][v]) & 1U);
}

static int triangle_free(uint32_t g) {
    for (int a = 0; a < 7; ++a)
        for (int b = a + 1; b < 7; ++b)
            for (int c = b + 1; c < 7; ++c)
                if (has_edge(g,a,b) && has_edge(g,a,c) && has_edge(g,b,c))
                    return 0;
    return 1;
}

static int alpha_at_most_three(uint32_t g) {
    for (int a = 0; a < 7; ++a)
        for (int b = a + 1; b < 7; ++b)
            for (int c = b + 1; c < 7; ++c)
                for (int d = c + 1; d < 7; ++d) {
                    int x[4] = {a,b,c,d};
                    int independent = 1;
                    for (int i = 0; i < 4; ++i)
                        for (int j = i + 1; j < 4; ++j)
                            independent &= !has_edge(g,x[i],x[j]);
                    if (independent) return 0;
                }
    return 1;
}

static int next_permutation(int *a, int n) {
    int i = n - 2;
    while (i >= 0 && a[i] >= a[i+1]) --i;
    if (i < 0) return 0;
    int j = n - 1;
    while (a[j] <= a[i]) --j;
    int t = a[i]; a[i] = a[j]; a[j] = t;
    for (int l = i + 1, r = n - 1; l < r; ++l, --r) {
        t = a[l]; a[l] = a[r]; a[r] = t;
    }
    return 1;
}

static int has_hamilton_cycle(uint32_t g) {
    int p[6] = {1,2,3,4,5,6};
    do {
        if (p[0] > p[5]) continue; /* quotient reversal */
        int old = 0, ok = 1;
        for (int i = 0; i < 6; ++i) {
            ok &= has_edge(g,old,p[i]);
            old = p[i];
        }
        ok &= has_edge(g,old,0);
        if (ok) return 1;
    } while (next_permutation(p,6));
    return 0;
}

static int cycle5_on(uint32_t g, int mask) {
    int v[5], k = 0;
    for (int i = 0; i < 7; ++i) if ((mask >> i) & 1) v[k++] = i;
    int p[4] = {v[1],v[2],v[3],v[4]};
    do {
        if (p[0] > p[3]) continue;
        int old = v[0], ok = 1;
        for (int i = 0; i < 4; ++i) {
            ok &= has_edge(g,old,p[i]);
            old = p[i];
        }
        ok &= has_edge(g,old,v[0]);
        if (ok) return 1;
    } while (next_permutation(p,4));
    return 0;
}

static int has_c5_plus_edge(uint32_t g) {
    for (int mask = 0; mask < (1 << 7); ++mask) {
        int count = 0;
        for (int i = 0; i < 7; ++i) count += (mask >> i) & 1;
        if (count != 5 || !cycle5_on(g,mask)) continue;
        int x = -1, y = -1;
        for (int i = 0; i < 7; ++i) if (!((mask >> i) & 1)) {
            if (x < 0) x = i; else y = i;
        }
        if (has_edge(g,x,y)) return 1;
    }
    return 0;
}

int main(void) {
    int id = 0;
    for (int i = 0; i < 7; ++i)
        for (int j = i + 1; j < 7; ++j)
            edge_id[i][j] = edge_id[j][i] = id++;

    uint64_t eligible = 0, c7 = 0, c5e_only = 0, failures = 0;
    for (uint32_t g = 0; g < (1U << 21); ++g) {
        if (!triangle_free(g) || !alpha_at_most_three(g)) continue;
        ++eligible;
        if (has_hamilton_cycle(g)) { ++c7; continue; }
        if (has_c5_plus_edge(g)) { ++c5e_only; continue; }
        ++failures;
        printf("FAIL mask=0x%06x\n", g);
    }
    printf("eligible=%llu c7=%llu c5_plus_edge_only=%llu failures=%llu\n",
           (unsigned long long)eligible, (unsigned long long)c7,
           (unsigned long long)c5e_only, (unsigned long long)failures);
    return failures ? 1 : 0;
}
