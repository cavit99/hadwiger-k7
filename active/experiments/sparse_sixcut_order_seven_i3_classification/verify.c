#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum { ORDER = 7, ROOTS = 6, GRAPH_COUNT = 1 << 21 };

typedef struct {
    uint32_t graph;
    unsigned centre;
} ColouredGraph;

static unsigned edge_index(unsigned left, unsigned right) {
    unsigned index = 0;
    if (left > right) {
        unsigned temporary = left;
        left = right;
        right = temporary;
    }
    for (unsigned first = 0; first < ORDER; ++first)
        for (unsigned second = first + 1; second < ORDER; ++second, ++index)
            if (first == left && second == right) return index;
    abort();
}

static uint32_t edge_bit(unsigned left, unsigned right) {
    return UINT32_C(1) << edge_index(left, right);
}

static void adjacency_from_graph(uint32_t graph, unsigned adjacency[ORDER]) {
    memset(adjacency, 0, ORDER * sizeof(*adjacency));
    for (unsigned left = 0; left < ORDER; ++left)
        for (unsigned right = left + 1; right < ORDER; ++right)
            if (graph & edge_bit(left, right)) {
                adjacency[left] |= 1u << right;
                adjacency[right] |= 1u << left;
            }
}

static int connected(unsigned mask, const unsigned adjacency[ORDER]) {
    if (mask == 0u) return 0;
    unsigned reached = mask & (0u - mask);
    for (;;) {
        unsigned old = reached;
        for (unsigned vertex = 0; vertex < ORDER; ++vertex)
            if ((reached >> vertex) & 1u)
                reached |= adjacency[vertex] & mask;
        if (reached == old) return reached == mask;
    }
}

static unsigned bag_contacts(const unsigned bags[5],
                             const unsigned adjacency[ORDER]) {
    unsigned contacts = 0;
    for (unsigned left = 0; left < 5; ++left)
        for (unsigned right = left + 1; right < 5; ++right) {
            int touch = 0;
            for (unsigned vertex = 0; vertex < ORDER; ++vertex)
                if (((bags[left] >> vertex) & 1u) &&
                    (adjacency[vertex] & bags[right])) {
                    touch = 1;
                    break;
                }
            contacts += (unsigned)touch;
        }
    return contacts;
}

/* Use only a Hall matching from C-u to the roots. */
static int has_matching_rooted_target(uint32_t graph) {
    unsigned adjacency[ORDER];
    adjacency_from_graph(graph, adjacency);
    for (unsigned unmatched = 0; unmatched < 3; ++unmatched) {
        unsigned matched[6], count = 0;
        for (unsigned vertex = 0; vertex < ORDER; ++vertex)
            if (vertex != unmatched) matched[count++] = vertex;
        for (unsigned omitted_index = 0; omitted_index < 6; ++omitted_index) {
            unsigned anchors[5], at = 0;
            for (unsigned index = 0; index < 6; ++index)
                if (index != omitted_index) anchors[at++] = matched[index];
            unsigned omitted = matched[omitted_index];
            for (int first_target = -1; first_target < 5; ++first_target) {
                for (int second_target = -1; second_target < 5; ++second_target) {
                    unsigned bags[5];
                    for (unsigned index = 0; index < 5; ++index)
                        bags[index] = 1u << anchors[index];
                    if (first_target >= 0)
                        bags[(unsigned)first_target] |= 1u << unmatched;
                    if (second_target >= 0)
                        bags[(unsigned)second_target] |= 1u << omitted;
                    int all_connected = 1;
                    for (unsigned index = 0; index < 5; ++index)
                        if (!connected(bags[index], adjacency)) {
                            all_connected = 0;
                            break;
                        }
                    if (all_connected && bag_contacts(bags, adjacency) >= 9u)
                        return 1;
                }
            }
        }
    }
    return 0;
}

static int root_bag_connected(unsigned root, unsigned mask,
                              const unsigned adjacency[ORDER],
                              const unsigned labels[ORDER]) {
    if (mask == 0u) return 1;
    unsigned reached = 0;
    for (unsigned vertex = 0; vertex < ORDER; ++vertex)
        if (((mask >> vertex) & 1u) && ((labels[vertex] >> root) & 1u))
            reached |= 1u << vertex;
    if (reached == 0u) return 0;
    for (;;) {
        unsigned old = reached;
        for (unsigned vertex = 0; vertex < ORDER; ++vertex)
            if ((reached >> vertex) & 1u)
                reached |= adjacency[vertex] & mask;
        if (reached == old) return reached == mask;
    }
}

static int rooted_bags_touch(unsigned left_root, unsigned left_mask,
                             unsigned right_root, unsigned right_mask,
                             const unsigned adjacency[ORDER],
                             const unsigned labels[ORDER]) {
    for (unsigned vertex = 0; vertex < ORDER; ++vertex) {
        if ((left_mask >> vertex) & 1u) {
            if ((labels[vertex] >> right_root) & 1u) return 1;
            if (adjacency[vertex] & right_mask) return 1;
        }
        if (((right_mask >> vertex) & 1u) &&
            ((labels[vertex] >> left_root) & 1u)) return 1;
    }
    return 0;
}

static int has_exact_target(uint32_t graph, unsigned centre) {
    unsigned adjacency[ORDER], labels[ORDER] = {0};
    adjacency_from_graph(graph, adjacency);
    unsigned leaves[2], leaf_count = 0;
    for (unsigned vertex = 0; vertex < 3; ++vertex)
        if (vertex != centre) leaves[leaf_count++] = vertex;
    labels[centre] = (1u << 0) | (1u << 1);
    labels[leaves[0]] = 1u << 0;
    labels[leaves[1]] = 1u << 1;
    for (unsigned vertex = 3; vertex < ORDER; ++vertex)
        labels[vertex] = 1u << (vertex - 1);

    const unsigned assignment_count = 279936u; /* 6^7 */
    for (unsigned omitted = 0; omitted < ROOTS; ++omitted) {
        unsigned roots[5], root_count = 0;
        for (unsigned root = 0; root < ROOTS; ++root)
            if (root != omitted) roots[root_count++] = root;
        for (unsigned code = 0; code < assignment_count; ++code) {
            unsigned bags[5] = {0}, value = code;
            for (unsigned vertex = 0; vertex < ORDER; ++vertex) {
                unsigned target = value % 6u;
                value /= 6u;
                if (target != 0u) bags[target - 1u] |= 1u << vertex;
            }
            int all_connected = 1;
            for (unsigned index = 0; index < 5; ++index)
                if (!root_bag_connected(roots[index], bags[index], adjacency,
                                        labels)) {
                    all_connected = 0;
                    break;
                }
            if (!all_connected) continue;
            unsigned contacts = 0;
            for (unsigned left = 0; left < 5; ++left)
                for (unsigned right = left + 1; right < 5; ++right)
                    contacts += (unsigned)rooted_bags_touch(
                        roots[left], bags[left], roots[right], bags[right],
                        adjacency, labels);
            if (contacts >= 9u) return 1;
        }
    }
    return 0;
}

static void add_collective_edges(uint32_t graph, unsigned vertex,
                                 unsigned char *seen) {
    while (vertex < ORDER) {
        int covered = 0;
        for (unsigned root_vertex = 0; root_vertex < 3; ++root_vertex)
            covered |= (graph & edge_bit(root_vertex, vertex)) != 0u;
        if (!covered) break;
        ++vertex;
    }
    if (vertex == ORDER) {
        seen[graph] = 1;
        return;
    }
    for (unsigned root_vertex = 0; root_vertex < 3; ++root_vertex)
        add_collective_edges(graph | edge_bit(root_vertex, vertex),
                             vertex + 1, seen);
}

static void choose_quotient_edges(unsigned at, unsigned count,
                                  unsigned option_count[9],
                                  uint32_t options[9][9],
                                  uint32_t graph, unsigned char *seen) {
    if (at == count) {
        add_collective_edges(graph, 3, seen);
        return;
    }
    for (unsigned choice = 0; choice < option_count[at]; ++choice)
        choose_quotient_edges(at + 1, count, option_count, options,
                              graph | options[at][choice], seen);
}

static void generate_shape(unsigned first_size, unsigned char *seen) {
    unsigned bags[5] = {1u << 0, 1u << 1, 1u << 2, 0, 0};
    if (first_size == 3) {
        bags[3] = (1u << 3) | (1u << 4) | (1u << 5);
        bags[4] = 1u << 6;
    } else {
        bags[3] = (1u << 3) | (1u << 4);
        bags[4] = (1u << 5) | (1u << 6);
    }

    uint32_t trees[3];
    unsigned tree_count = 0;
    if (first_size == 3) {
        trees[tree_count++] = edge_bit(3, 4) | edge_bit(3, 5);
        trees[tree_count++] = edge_bit(3, 4) | edge_bit(4, 5);
        trees[tree_count++] = edge_bit(3, 5) | edge_bit(4, 5);
    } else {
        trees[tree_count++] = edge_bit(3, 4) | edge_bit(5, 6);
    }

    unsigned pairs[10][2], pair_count = 0;
    for (unsigned left = 0; left < 5; ++left)
        for (unsigned right = left + 1; right < 5; ++right) {
            pairs[pair_count][0] = left;
            pairs[pair_count][1] = right;
            ++pair_count;
        }

    for (unsigned missing = 0; missing < pair_count; ++missing) {
        unsigned option_count[9] = {0};
        uint32_t options[9][9] = {{0}};
        unsigned required = 0;
        for (unsigned pair = 0; pair < pair_count; ++pair) {
            if (pair == missing) continue;
            unsigned left_bag = bags[pairs[pair][0]];
            unsigned right_bag = bags[pairs[pair][1]];
            for (unsigned left = 0; left < ORDER; ++left)
                if ((left_bag >> left) & 1u)
                    for (unsigned right = 0; right < ORDER; ++right)
                        if ((right_bag >> right) & 1u)
                            options[required][option_count[required]++] =
                                edge_bit(left, right);
            ++required;
        }
        for (unsigned tree = 0; tree < tree_count; ++tree)
            choose_quotient_edges(0, required, option_count, options,
                                  trees[tree], seen);
    }
}

static uint32_t image_graph(uint32_t graph, const unsigned image[ORDER]) {
    uint32_t answer = 0;
    for (unsigned left = 0; left < ORDER; ++left)
        for (unsigned right = left + 1; right < ORDER; ++right)
            if (graph & edge_bit(left, right))
                answer |= edge_bit(image[left], image[right]);
    return answer;
}

static void swap(unsigned *left, unsigned *right) {
    unsigned temporary = *left;
    *left = *right;
    *right = temporary;
}

static int next_permutation(unsigned *values, unsigned count) {
    int pivot = (int)count - 2;
    while (pivot >= 0 && values[pivot] >= values[pivot + 1]) --pivot;
    if (pivot < 0) return 0;
    int successor = (int)count - 1;
    while (values[successor] <= values[pivot]) --successor;
    swap(&values[pivot], &values[successor]);
    for (unsigned left = (unsigned)pivot + 1, right = count - 1;
         left < right; ++left, --right)
        swap(&values[left], &values[right]);
    return 1;
}

static uint32_t canonical_coloured(uint32_t graph, unsigned centre) {
    unsigned leaves[2], leaf_count = 0;
    for (unsigned vertex = 0; vertex < 3; ++vertex)
        if (vertex != centre) leaves[leaf_count++] = vertex;
    uint32_t best = UINT32_MAX;
    for (unsigned leaf_swap = 0; leaf_swap < 2; ++leaf_swap) {
        unsigned w_permutation[4] = {3, 4, 5, 6};
        do {
            unsigned image[ORDER];
            image[centre] = 0;
            image[leaves[0]] = leaf_swap ? 2 : 1;
            image[leaves[1]] = leaf_swap ? 1 : 2;
            for (unsigned index = 0; index < 4; ++index)
                image[3 + index] = w_permutation[index];
            uint32_t candidate = image_graph(graph, image);
            if (candidate < best) best = candidate;
        } while (next_permutation(w_permutation, 4));
    }
    return best;
}

int main(void) {
    unsigned char *shape31 = calloc(GRAPH_COUNT, 1);
    unsigned char *shape22 = calloc(GRAPH_COUNT, 1);
    if (!shape31 || !shape22) return 2;
    generate_shape(3, shape31);
    generate_shape(2, shape22);

    unsigned count31 = 0, count22 = 0;
    unsigned matching_fail31 = 0, matching_fail22 = 0;
    ColouredGraph failures[100];
    unsigned failure_count = 0;
    for (uint32_t graph = 0; graph < GRAPH_COUNT; ++graph) {
        if (shape31[graph]) {
            ++count31;
            if (!has_matching_rooted_target(graph)) ++matching_fail31;
        }
        if (shape22[graph]) {
            ++count22;
            if (!has_matching_rooted_target(graph)) {
                ++matching_fail22;
                for (unsigned centre = 0; centre < 3; ++centre)
                    if (!has_exact_target(graph, centre)) {
                        if (failure_count >= 100) return 3;
                        failures[failure_count++] =
                            (ColouredGraph){graph, centre};
                    }
            }
        }
    }

    if (count31 != 5391u || count22 != 4032u ||
        matching_fail31 != 0u || matching_fail22 != 24u ||
        failure_count != 24u) return 4;

    const uint32_t representative = UINT32_C(0x69e33);
    for (unsigned index = 0; index < failure_count; ++index) {
        if (__builtin_popcount(failures[index].graph) != 11) return 5;
        if (canonical_coloured(failures[index].graph,
                               failures[index].centre) != representative)
            return 6;
        for (unsigned edge = 0; edge < 21; ++edge)
            if (((failures[index].graph >> edge) & 1u) == 0u &&
                !has_exact_target(failures[index].graph | (1u << edge),
                                  failures[index].centre))
                return 7;
    }

    printf("shape(3,1): supports=%u matching_failures=%u\n",
           count31, matching_fail31);
    printf("shape(2,2): supports=%u matching_failures=%u "
           "exact_coloured_failures=%u\n",
           count22, matching_fail22, failure_count);
    printf("residual_orbits=1 representative=0x%05x one_edge_failures=0\n",
           representative);
    printf("order-seven i=3 internal classification: PASS\n");
    free(shape31);
    free(shape22);
    return 0;
}
