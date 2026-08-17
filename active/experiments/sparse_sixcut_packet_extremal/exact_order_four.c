/* Exact order-four falsifier for the sparse six-cut component dichotomy.

   Compile with:
     cc -O3 -std=c17 -Wall -Wextra -pedantic exact_order_four.c -o exact4

   The six roots are prescribed and independent.  The six connected
   unlabelled internal graphs of order four are represented explicitly;
   every boundary-labelling is enumerated. */

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

enum { ORDER = 4, ALL_ROOTS = 63 };

static int popcount(unsigned value) { return __builtin_popcount(value); }

static bool connected_mask(const unsigned adj[ORDER], unsigned mask) {
    if (!mask) return false;
    unsigned reached = mask & (0u - mask);
    unsigned frontier = reached;
    while (frontier) {
        unsigned bit = frontier & (0u - frontier);
        int at = __builtin_ctz(bit);
        frontier ^= bit;
        unsigned fresh = adj[at] & mask & ~reached;
        reached |= fresh;
        frontier |= fresh;
    }
    return reached == mask;
}

static bool internally_six(const unsigned adj[ORDER], const unsigned label[ORDER]) {
    for (unsigned mask = 1; mask < (1u << ORDER); ++mask) {
        unsigned roots = 0, internal = 0;
        for (int vertex = 0; vertex < ORDER; ++vertex) {
            if (mask & (1u << vertex)) {
                roots |= label[vertex];
                internal |= adj[vertex] & ~mask;
            }
        }
        if (popcount(roots) + popcount(internal) < 6) return false;
    }
    return true;
}

static bool packet_one(const unsigned adj[ORDER], const unsigned label[ORDER]) {
    unsigned packets[15];
    int count = 0;
    for (unsigned mask = 1; mask < (1u << ORDER); ++mask) {
        if (!connected_mask(adj, mask)) continue;
        unsigned roots = 0;
        for (int vertex = 0; vertex < ORDER; ++vertex)
            if (mask & (1u << vertex)) roots |= label[vertex];
        if (roots == ALL_ROOTS) packets[count++] = mask;
    }
    if (!count) return false;
    for (int left = 0; left < count; ++left)
        for (int right = left + 1; right < count; ++right)
            if (!(packets[left] & packets[right])) return false;
    return true;
}

static bool bag_connected(
    int root, unsigned mask, const unsigned adj[ORDER], const unsigned label[ORDER]
) {
    if (!mask) return true;
    unsigned reached = 0;
    for (int vertex = 0; vertex < ORDER; ++vertex)
        if ((mask & (1u << vertex)) && (label[vertex] & (1u << root)))
            reached |= 1u << vertex;
    unsigned frontier = reached;
    while (frontier) {
        unsigned bit = frontier & (0u - frontier);
        int at = __builtin_ctz(bit);
        frontier ^= bit;
        unsigned fresh = adj[at] & mask & ~reached;
        reached |= fresh;
        frontier |= fresh;
    }
    return reached == mask;
}

static bool bags_touch(
    int root_left, unsigned left, int root_right, unsigned right,
    const unsigned adj[ORDER], const unsigned label[ORDER]
) {
    for (int vertex = 0; vertex < ORDER; ++vertex) {
        if (left & (1u << vertex)) {
            if (label[vertex] & (1u << root_right)) return true;
            if (adj[vertex] & right) return true;
        }
        if ((right & (1u << vertex)) && (label[vertex] & (1u << root_left)))
            return true;
    }
    return false;
}

static bool near_five_allocation(
    const int roots[5], const unsigned bags[5],
    const unsigned adj[ORDER], const unsigned label[ORDER]
) {
    for (int bag = 0; bag < 5; ++bag)
        if (!bag_connected(roots[bag], bags[bag], adj, label)) return false;
    int missing = 0;
    for (int left = 0; left < 5; ++left)
        for (int right = left + 1; right < 5; ++right)
            if (!bags_touch(roots[left], bags[left], roots[right], bags[right], adj, label)
                && ++missing > 1)
                return false;
    return true;
}

struct model_profile {
    bool found;
    bool one_internal_per_bag;
    bool incidence_only;
    bool common_pair_path;
    bool common_pair_cycle;
    int minimum_augmented_bags;
};

static bool triple_on_cycle(const unsigned adj[ORDER], unsigned triple) {
    int vertices[ORDER];
    for (int length = 3; length <= 4; ++length) {
        unsigned supersets = (1u << ORDER) - 1;
        for (unsigned mask = triple; mask < (1u << ORDER); ++mask) {
            if ((mask & triple) != triple || popcount(mask) != length) continue;
            int count = 0;
            for (int vertex = 0; vertex < ORDER; ++vertex)
                if (mask & (1u << vertex)) vertices[count++] = vertex;
            /* ORDER is four, so brute-force all vertex orders directly. */
            for (int a = 0; a < count; ++a)
                for (int b = 0; b < count; ++b) if (b != a)
                    for (int c = 0; c < count; ++c) if (c != a && c != b)
                        for (int d = 0; d < (count == 3 ? 1 : count); ++d) {
                            if (count == 4 && (d == a || d == b || d == c)) continue;
                            int order[4] = {vertices[a], vertices[b], vertices[c],
                                count == 3 ? vertices[a] : vertices[d]};
                            bool cycle = true;
                            for (int index = 0; index < count; ++index) {
                                int left = order[index];
                                int right = order[(index + 1) % count];
                                if (!(adj[left] & (1u << right))) cycle = false;
                            }
                            if (cycle) return true;
                        }
        }
        (void)supersets;
    }
    return false;
}

static struct model_profile near_five_profile(
    const unsigned adj[ORDER], const unsigned label[ORDER]
) {
    struct model_profile profile = {false, false, false, false, false, 6};
    const unsigned empty_adj[ORDER] = {0, 0, 0, 0};
    for (int omitted = 0; omitted < 6; ++omitted) {
        int roots[5], next = 0;
        for (int root = 0; root < 6; ++root)
            if (root != omitted) roots[next++] = root;
        for (int code = 0; code < 6 * 6 * 6 * 6; ++code) {
            int value = code;
            unsigned bags[5] = {0, 0, 0, 0, 0};
            for (int vertex = 0; vertex < ORDER; ++vertex) {
                int owner = value % 6;
                value /= 6;
                if (owner) bags[owner - 1] |= 1u << vertex;
            }
            if (!near_five_allocation(roots, bags, adj, label)) continue;
            profile.found = true;
            int augmented = 0;
            bool one_per = true;
            for (int bag = 0; bag < 5; ++bag) {
                if (bags[bag]) ++augmented;
                if (popcount(bags[bag]) > 1) one_per = false;
            }
            if (augmented < profile.minimum_augmented_bags)
                profile.minimum_augmented_bags = augmented;
            if (one_per) profile.one_internal_per_bag = true;
            if (near_five_allocation(roots, bags, empty_adj, label))
                profile.incidence_only = true;
            if (augmented == 3 && one_per) {
                unsigned triple = 0;
                for (int bag = 0; bag < 5; ++bag) triple |= bags[bag];
                int internal_edges = 0;
                for (int vertex = 0; vertex < ORDER; ++vertex)
                    if (triple & (1u << vertex))
                        internal_edges += popcount(adj[vertex] & triple);
                internal_edges /= 2;
                if (internal_edges >= 2) profile.common_pair_path = true;
                if (triple_on_cycle(adj, triple)) profile.common_pair_cycle = true;
            }
            if (profile.minimum_augmented_bags == 3
                && profile.one_internal_per_bag && profile.incidence_only
                && profile.common_pair_path && profile.common_pair_cycle)
                return profile;
        }
    }
    return profile;
}

static bool four_allocation(
    const int roots[4], const unsigned bags[4],
    const unsigned adj[ORDER], const unsigned label[ORDER]
) {
    for (int bag = 0; bag < 4; ++bag)
        if (!bag_connected(roots[bag], bags[bag], adj, label)) return false;
    for (int left = 0; left < 4; ++left)
        for (int right = left + 1; right < 4; ++right)
            if (!bags_touch(roots[left], bags[left], roots[right], bags[right], adj, label))
                return false;
    return true;
}

static bool has_rooted_four(const unsigned adj[ORDER], const unsigned label[ORDER]) {
    for (int omit_left = 0; omit_left < 6; ++omit_left) {
        for (int omit_right = omit_left + 1; omit_right < 6; ++omit_right) {
            int roots[4], next = 0;
            for (int root = 0; root < 6; ++root)
                if (root != omit_left && root != omit_right) roots[next++] = root;
            for (int code = 0; code < 5 * 5 * 5 * 5; ++code) {
                int value = code;
                unsigned bags[4] = {0, 0, 0, 0};
                for (int vertex = 0; vertex < ORDER; ++vertex) {
                    int owner = value % 5;
                    value /= 5;
                    if (owner) bags[owner - 1] |= 1u << vertex;
                }
                if (four_allocation(roots, bags, adj, label)) return true;
            }
        }
    }
    return false;
}

static int excess(int edge_count, const unsigned label[ORDER]) {
    int incidence = 0;
    for (int vertex = 0; vertex < ORDER; ++vertex) incidence += popcount(label[vertex]);
    return edge_count + incidence - 4 * ORDER;
}

static void add_edge(unsigned adj[ORDER], int left, int right) {
    adj[left] |= 1u << right;
    adj[right] |= 1u << left;
}

static void run_graph(const char *name, const int edges[][2], int edge_count) {
    unsigned adj[ORDER] = {0, 0, 0, 0};
    for (int edge = 0; edge < edge_count; ++edge)
        add_edge(adj, edges[edge][0], edges[edge][1]);
    unsigned domains[ORDER][64];
    int sizes[ORDER] = {0, 0, 0, 0};
    for (int vertex = 0; vertex < ORDER; ++vertex) {
        int minimum = 6 - popcount(adj[vertex]);
        for (unsigned label = 0; label < 64; ++label)
            if (popcount(label) >= minimum) domains[vertex][sizes[vertex]++] = label;
    }

    uint64_t labelled = 0, threshold = 0, relative = 0, packet_thin = 0;
    uint64_t avoiding = 0, rooted_four = 0;
    uint64_t minimum_three = 0, minimum_four = 0;
    uint64_t one_per_bag = 0, incidence_only = 0;
    uint64_t common_pair_path = 0, common_pair_cycle = 0;
    unsigned label[ORDER];
    for (int a = 0; a < sizes[0]; ++a) {
        label[0] = domains[0][a];
        for (int b = 0; b < sizes[1]; ++b) {
            label[1] = domains[1][b];
            for (int c = 0; c < sizes[2]; ++c) {
                label[2] = domains[2][c];
                for (int d = 0; d < sizes[3]; ++d) {
                    label[3] = domains[3][d];
                    ++labelled;
                    if (excess(edge_count, label) < 6) continue;
                    ++threshold;
                    if (!internally_six(adj, label)) continue;
                    ++relative;
                    if (!packet_one(adj, label)) continue;
                    ++packet_thin;
                    struct model_profile profile = near_five_profile(adj, label);
                    if (profile.found) {
                        if (profile.minimum_augmented_bags == 3) ++minimum_three;
                        else if (profile.minimum_augmented_bags == 4) ++minimum_four;
                        else {
                            fprintf(stderr, "unexpected augmented-bag count %d\n",
                                profile.minimum_augmented_bags);
                            exit(2);
                        }
                        if (profile.one_internal_per_bag) ++one_per_bag;
                        if (profile.incidence_only) ++incidence_only;
                        if (profile.common_pair_path) ++common_pair_path;
                        if (profile.common_pair_cycle) ++common_pair_cycle;
                        continue;
                    }
                    ++avoiding;
                    bool rooted = has_rooted_four(adj, label);
                    if (rooted) ++rooted_four;
                    fprintf(stderr,
                        "COUNTEREXAMPLE graph=%s labels=%u,%u,%u,%u eta=%d "
                        "rooted_four=%s\n",
                        name, label[0], label[1], label[2], label[3],
                        excess(edge_count, label), rooted ? "yes" : "no");
                    exit(1);
                }
            }
        }
    }
    printf("%s labelled=%llu threshold=%llu relative=%llu packet_one=%llu "
           "packet_rich=%llu min_aug3=%llu min_aug4=%llu one_per=%llu "
           "incidence_only=%llu W_path=%llu W_cycle=%llu "
           "no_near_five=%llu rooted_four=%llu\n",
        name, (unsigned long long)labelled, (unsigned long long)threshold,
        (unsigned long long)relative, (unsigned long long)packet_thin,
        (unsigned long long)(relative - packet_thin),
        (unsigned long long)minimum_three, (unsigned long long)minimum_four,
        (unsigned long long)one_per_bag, (unsigned long long)incidence_only,
        (unsigned long long)common_pair_path, (unsigned long long)common_pair_cycle,
        (unsigned long long)avoiding, (unsigned long long)rooted_four);
}

int main(void) {
    const int p4[][2] = {{0,1},{1,2},{2,3}};
    const int star[][2] = {{0,1},{0,2},{0,3}};
    const int cycle[][2] = {{0,1},{1,2},{2,3},{3,0}};
    const int paw[][2] = {{0,1},{1,2},{2,0},{0,3}};
    const int diamond[][2] = {{0,1},{0,2},{0,3},{1,2},{1,3}};
    const int clique[][2] = {{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
    run_graph("P4", p4, 3);
    run_graph("K1,3", star, 3);
    run_graph("C4", cycle, 4);
    run_graph("paw", paw, 4);
    run_graph("K4-e", diamond, 5);
    run_graph("K4", clique, 6);
    puts("GREEN exact independent-six-root order-four dichotomy");
    return 0;
}
