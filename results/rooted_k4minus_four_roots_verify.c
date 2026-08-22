/*
 * Independent bounded audit for the universal four-root K4-minus theorem.
 *
 * Enumerates every labelled simple graph on n=4,...,7 vertices.  By label
 * symmetry it suffices to nominate roots 0,1,2,3: every graph/root-four-set
 * pair on n vertices is isomorphic to one appearing with these nominated
 * labels.  For every 3-connected graph, exhaust all assignments of each
 * nonroot vertex to one of the four rooted bags or to the unused class.
 *
 * This file deliberately uses no graph library and shares no model-search
 * code with rooted_k4minus_base_check.py.
 */

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static int connected_after_delete(const uint8_t adj[7], int n, uint8_t del) {
    uint8_t alive = (uint8_t)(((1u << n) - 1u) & ~del);
    if (!alive) return 1;
    uint8_t seen = 0;
    uint8_t todo = (uint8_t)(alive & (uint8_t)(-alive));
    while (todo) {
        uint8_t bit = (uint8_t)(todo & (uint8_t)(-todo));
        int v = __builtin_ctz((unsigned)bit);
        todo ^= bit;
        if (seen & bit) continue;
        seen |= bit;
        todo |= (uint8_t)(adj[v] & alive & ~seen);
    }
    return seen == alive;
}

static int is_three_connected(const uint8_t adj[7], int n) {
    for (int v = 0; v < n; ++v)
        if (__builtin_popcount((unsigned)adj[v]) < 3) return 0;
    if (!connected_after_delete(adj, n, 0)) return 0;
    for (int x = 0; x < n; ++x) {
        if (!connected_after_delete(adj, n, (uint8_t)(1u << x))) return 0;
        for (int y = x + 1; y < n; ++y)
            if (!connected_after_delete(adj, n,
                    (uint8_t)((1u << x) | (1u << y)))) return 0;
    }
    return 1;
}

static int connected_bag(const uint8_t adj[7], uint8_t bag) {
    uint8_t seen = 0;
    uint8_t todo = (uint8_t)(bag & (uint8_t)(-bag));
    while (todo) {
        uint8_t bit = (uint8_t)(todo & (uint8_t)(-todo));
        int v = __builtin_ctz((unsigned)bit);
        todo ^= bit;
        if (seen & bit) continue;
        seen |= bit;
        todo |= (uint8_t)(adj[v] & bag & ~seen);
    }
    return seen == bag;
}

static int bags_touch(const uint8_t adj[7], uint8_t a, uint8_t b) {
    while (a) {
        uint8_t bit = (uint8_t)(a & (uint8_t)(-a));
        int v = __builtin_ctz((unsigned)bit);
        a ^= bit;
        if (adj[v] & b) return 1;
    }
    return 0;
}

static int has_rooted_k4minus(const uint8_t adj[7], int n) {
    int free_count = n - 4;
    int assignments = 1;
    for (int i = 0; i < free_count; ++i) assignments *= 5;

    for (int code0 = 0; code0 < assignments; ++code0) {
        int code = code0;
        uint8_t bag[4] = {1u, 2u, 4u, 8u};
        for (int k = 0; k < free_count; ++k) {
            int value = code % 5;
            code /= 5;
            if (value < 4) bag[value] |= (uint8_t)(1u << (k + 4));
        }
        int good = 1;
        for (int i = 0; i < 4; ++i)
            if (!connected_bag(adj, bag[i])) { good = 0; break; }
        if (!good) continue;

        int contacts = 0;
        for (int i = 0; i < 4; ++i)
            for (int j = i + 1; j < 4; ++j)
                contacts += bags_touch(adj, bag[i], bag[j]);
        if (contacts >= 5) return 1;
    }
    return 0;
}

int main(void) {
    for (int n = 4; n <= 7; ++n) {
        int eu[21], ev[21], m = 0;
        for (int u = 0; u < n; ++u)
            for (int v = u + 1; v < n; ++v) {
                eu[m] = u; ev[m] = v; ++m;
            }

        uint64_t limit = 1ull << m;
        uint64_t three_connected = 0, tested_assignments = 0;
        for (uint64_t emask = 0; emask < limit; ++emask) {
            uint8_t adj[7] = {0,0,0,0,0,0,0};
            for (int e = 0; e < m; ++e) if (emask & (1ull << e)) {
                adj[eu[e]] |= (uint8_t)(1u << ev[e]);
                adj[ev[e]] |= (uint8_t)(1u << eu[e]);
            }
            if (!is_three_connected(adj, n)) continue;
            ++three_connected;
            int p = 1;
            for (int k = 4; k < n; ++k) p *= 5;
            tested_assignments += (uint64_t)p;
            if (!has_rooted_k4minus(adj, n)) {
                fprintf(stderr, "COUNTEREXAMPLE n=%d edge_mask=%llu\n",
                        n, (unsigned long long)emask);
                return 1;
            }
        }
        printf("n=%d three_connected_labelled=%llu assignment_upper_bound=%llu all_green\n",
               n, (unsigned long long)three_connected,
               (unsigned long long)tested_assignments);
    }
    return 0;
}
