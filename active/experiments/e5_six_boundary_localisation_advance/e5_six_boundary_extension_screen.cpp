#include <array>
#include <bit>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

using Mask = std::uint16_t;

namespace {

constexpr int kBoundaryOrder = 6;
constexpr int kBranchSets = 7;

struct Partition {
    std::array<Mask, kBranchSets> bags{};
};

std::array<std::vector<Partition>, 13> partitions_by_order;
int current_order = 0;

const std::vector<std::pair<int, int>>& boundary_edges() {
    static const std::vector<std::pair<int, int>> edges = [] {
        std::vector<std::pair<int, int>> out;
        for (int u = 0; u < kBoundaryOrder; ++u) {
            for (int v = u + 1; v < kBoundaryOrder; ++v) {
                out.emplace_back(u, v);
            }
        }
        return out;
    }();
    return edges;
}

void add_edge(std::vector<Mask>& adjacency, int u, int v) {
    adjacency.at(u) |= static_cast<Mask>(Mask{1} << v);
    adjacency.at(v) |= static_cast<Mask>(Mask{1} << u);
}

void generate_partitions_recursive(const std::vector<int>& items,
                                   int index,
                                   int maximum_label,
                                   std::vector<int>& labels) {
    if (index == static_cast<int>(items.size())) {
        if (maximum_label != kBranchSets - 1) {
            return;
        }
        Partition partition;
        for (int i = 0; i < static_cast<int>(items.size()); ++i) {
            partition.bags.at(labels.at(i)) |=
                static_cast<Mask>(Mask{1} << items.at(i));
        }
        partitions_by_order.at(current_order).push_back(partition);
        return;
    }

    const int upper = std::min(maximum_label + 1, kBranchSets - 1);
    for (int label = 0; label <= upper; ++label) {
        labels.at(index) = label;
        const int new_maximum = std::max(maximum_label, label);
        const int remaining = static_cast<int>(items.size()) - index - 1;
        if (new_maximum + remaining >= kBranchSets - 1) {
            generate_partitions_recursive(items, index + 1, new_maximum, labels);
        }
    }
}

void generate_partitions(int order) {
    if (!partitions_by_order.at(order).empty()) {
        return;
    }
    current_order = order;
    for (int used_order = kBranchSets; used_order <= order; ++used_order) {
        std::vector<int> used_vertices(used_order);
        std::function<void(int, int)> choose = [&](int position, int start) {
            if (position == used_order) {
                std::vector<int> labels(used_order, 0);
                labels.at(0) = 0;
                generate_partitions_recursive(used_vertices, 1, 0, labels);
                return;
            }
            for (int vertex = start;
                 vertex <= order - (used_order - position);
                 ++vertex) {
                used_vertices.at(position) = vertex;
                choose(position + 1, vertex + 1);
            }
        };
        choose(0, 0);
    }
}

bool contains_k7_minus(const std::vector<Mask>& adjacency) {
    const int order = static_cast<int>(adjacency.size());
    const int subset_count = 1 << order;
    std::vector<std::uint8_t> connected(subset_count, 0);
    std::vector<Mask> external_neighbours(subset_count, 0);

    for (int subset = 1; subset < subset_count; ++subset) {
        const int first_bit = subset & -subset;
        const int first_vertex = std::countr_zero(static_cast<unsigned>(first_bit));
        external_neighbours.at(subset) =
            static_cast<Mask>(external_neighbours.at(subset ^ first_bit) |
                              adjacency.at(first_vertex));

        Mask seen = static_cast<Mask>(first_bit);
        Mask frontier = static_cast<Mask>(first_bit);
        while (frontier != 0) {
            const Mask next_bit = static_cast<Mask>(frontier & -frontier);
            frontier = static_cast<Mask>(frontier ^ next_bit);
            const int vertex = std::countr_zero(static_cast<unsigned>(next_bit));
            const Mask next = static_cast<Mask>(
                adjacency.at(vertex) & subset & static_cast<Mask>(~seen));
            seen = static_cast<Mask>(seen | next);
            frontier = static_cast<Mask>(frontier | next);
        }
        connected.at(subset) = (seen == subset);
    }

    for (const Partition& partition : partitions_by_order.at(order)) {
        bool all_connected = true;
        for (Mask bag : partition.bags) {
            if (!connected.at(bag)) {
                all_connected = false;
                break;
            }
        }
        if (!all_connected) {
            continue;
        }

        int missing_pairs = 0;
        for (int i = 0; i < kBranchSets && missing_pairs <= 1; ++i) {
            for (int j = i + 1; j < kBranchSets; ++j) {
                if ((external_neighbours.at(partition.bags.at(i)) &
                     partition.bags.at(j)) == 0) {
                    ++missing_pairs;
                    if (missing_pairs > 1) {
                        break;
                    }
                }
            }
        }
        if (missing_pairs <= 1) {
            return true;
        }
    }
    return false;
}

enum class Kernel { kK2, kP3, kK3 };
enum class Extras { kNone, kOneSingleton, kTwoSingletons, kOneEdge };

std::string kernel_name(Kernel kernel) {
    if (kernel == Kernel::kK2) return "K2";
    if (kernel == Kernel::kP3) return "P3";
    return "K3";
}

int low_kernel_order(Kernel kernel) {
    return kernel == Kernel::kK2 ? 2 : 3;
}


struct SplitContactPattern {
    // 1 = first split piece only, 2 = second split piece only, 3 = both.
    std::array<int, 6> contact{};
};

SplitContactPattern decode_split_pattern(int code, int universal_root) {
    SplitContactPattern pattern;
    pattern.contact.at(universal_root) = 3;
    int remaining = code;
    for (int root = 0; root < 6; ++root) {
        if (root == universal_root) continue;
        if (root == 1) {
            pattern.contact.at(root) = 1 + (remaining % 2);
            remaining /= 2;
        } else {
            pattern.contact.at(root) = 1 + (remaining % 3);
            remaining /= 3;
        }
    }
    return pattern;
}

int split_pattern_count(int universal_root) {
    int count = 2;  // root 1 has exactly one neighbour in the split component.
    for (int root = 0; root < 6; ++root) {
        if (root != universal_root && root != 1) count *= 3;
    }
    return count;
}

std::vector<Mask> build_k3_split_host(int boundary_mask,
                                      int universal_root,
                                      int pattern_code) {
    // Boundary 0..5, low K3 6..8, split component pieces 9,10,
    // and the other six-full representative 11.
    std::vector<Mask> adjacency(12, 0);
    const auto& edges = boundary_edges();
    for (int i = 0; i < static_cast<int>(edges.size()); ++i) {
        if (((boundary_mask >> i) & 1) != 0) {
            add_edge(adjacency, edges.at(i).first, edges.at(i).second);
        }
    }
    const int d = 6;
    const int f1 = 7;
    const int f2 = 8;
    add_edge(adjacency, d, f1);
    add_edge(adjacency, d, f2);
    add_edge(adjacency, f1, f2);
    for (int root : {0, 1, 2}) add_edge(adjacency, d, root);
    for (int leaf : {f1, f2}) {
        for (int root : {0, 3, 4, 5}) add_edge(adjacency, leaf, root);
    }

    const int first_piece = 9;
    const int second_piece = 10;
    const int other_full = 11;
    add_edge(adjacency, first_piece, second_piece);
    for (int root = 0; root < 6; ++root) {
        add_edge(adjacency, other_full, root);
    }
    const SplitContactPattern pattern =
        decode_split_pattern(pattern_code, universal_root);
    for (int root = 0; root < 6; ++root) {
        if ((pattern.contact.at(root) & 1) != 0) {
            add_edge(adjacency, first_piece, root);
        }
        if ((pattern.contact.at(root) & 2) != 0) {
            add_edge(adjacency, second_piece, root);
        }
    }
    return adjacency;
}


std::vector<Mask> build_two_u_split_host(Kernel kernel,
                                         int boundary_mask,
                                         int pattern_code) {
    // Boundary 0..5, low P3/K3 6..8, split component pieces 9,10,
    // and the other six-full representative 11.  Both split pieces meet
    // root 1; every other root meets at least one piece.
    if (kernel == Kernel::kK2) {
        throw std::runtime_error("two-u split host requires P3 or K3");
    }
    std::vector<Mask> adjacency(12, 0);
    const auto& edges = boundary_edges();
    for (int i = 0; i < static_cast<int>(edges.size()); ++i) {
        if (((boundary_mask >> i) & 1) != 0) {
            add_edge(adjacency, edges.at(i).first, edges.at(i).second);
        }
    }
    const int d = 6;
    const int f1 = 7;
    const int f2 = 8;
    add_edge(adjacency, d, f1);
    add_edge(adjacency, d, f2);
    if (kernel == Kernel::kK3) add_edge(adjacency, f1, f2);
    for (int root : {0, 1, 2}) add_edge(adjacency, d, root);
    for (int leaf : {f1, f2}) {
        for (int root : {0, 3, 4, 5}) add_edge(adjacency, leaf, root);
    }
    const int first_piece = 9;
    const int second_piece = 10;
    const int other_full = 11;
    add_edge(adjacency, first_piece, second_piece);
    add_edge(adjacency, first_piece, 1);
    add_edge(adjacency, second_piece, 1);
    for (int root = 0; root < 6; ++root) add_edge(adjacency, other_full, root);

    int remaining = pattern_code;
    for (int root : {0, 2, 3, 4, 5}) {
        const int contact = 1 + (remaining % 3);
        remaining /= 3;
        if ((contact & 1) != 0) add_edge(adjacency, first_piece, root);
        if ((contact & 2) != 0) add_edge(adjacency, second_piece, root);
    }
    return adjacency;
}

SplitContactPattern decode_two_u_split_pattern(int code) {
    SplitContactPattern pattern;
    pattern.contact.at(1) = 3;
    int remaining = code;
    for (int root : {0, 2, 3, 4, 5}) {
        pattern.contact.at(root) = 1 + (remaining % 3);
        remaining /= 3;
    }
    return pattern;
}

bool all_exclusive_on_one_side(const SplitContactPattern& pattern,
                               const std::vector<int>& roots) {
    const int side = pattern.contact.at(roots.front());
    if (side != 1 && side != 2) return false;
    for (int root : roots) {
        if (pattern.contact.at(root) != side) return false;
    }
    return true;
}

std::vector<Mask> build_host(Kernel kernel,
                             int boundary_mask,
                             int six_full_count,
                             Extras extras,
                             int missed_root) {
    const int low_order = low_kernel_order(kernel);
    const int extra_order =
        extras == Extras::kNone ? 0 :
        extras == Extras::kOneSingleton ? 1 : 2;
    const int order = kBoundaryOrder + low_order + six_full_count + extra_order;
    std::vector<Mask> adjacency(order, 0);

    const auto& edges = boundary_edges();
    for (int i = 0; i < static_cast<int>(edges.size()); ++i) {
        if (((boundary_mask >> i) & 1) != 0) {
            add_edge(adjacency, edges.at(i).first, edges.at(i).second);
        }
    }

    if (kernel == Kernel::kK2) {
        const int d = 6;
        const int w = 7;
        add_edge(adjacency, d, w);
        for (int root : {0, 1, 2, 3}) add_edge(adjacency, d, root);
        for (int root : {0, 1, 4, 5}) add_edge(adjacency, w, root);
    } else {
        const int d = 6;
        const int f1 = 7;
        const int f2 = 8;
        add_edge(adjacency, d, f1);
        add_edge(adjacency, d, f2);
        if (kernel == Kernel::kK3) add_edge(adjacency, f1, f2);
        for (int root : {0, 1, 2}) add_edge(adjacency, d, root);
        for (int leaf : {f1, f2}) {
            for (int root : {0, 3, 4, 5}) add_edge(adjacency, leaf, root);
        }
    }

    int next = kBoundaryOrder + low_order;
    for (int i = 0; i < six_full_count; ++i, ++next) {
        for (int root = 0; root < kBoundaryOrder; ++root) {
            add_edge(adjacency, next, root);
        }
    }

    if (extras != Extras::kNone) {
        const int first = next;
        const int last = next + extra_order;
        if (extras == Extras::kOneEdge) {
            add_edge(adjacency, first, first + 1);
        }
        for (int vertex = first; vertex < last; ++vertex) {
            for (int root = 0; root < kBoundaryOrder; ++root) {
                if (root != missed_root) add_edge(adjacency, vertex, root);
            }
        }
    }
    return adjacency;
}

int boundary_degree(int mask, int root) {
    int degree = 0;
    const auto& edges = boundary_edges();
    for (int i = 0; i < static_cast<int>(edges.size()); ++i) {
        if (((mask >> i) & 1) != 0 &&
            (edges.at(i).first == root || edges.at(i).second == root)) {
            ++degree;
        }
    }
    return degree;
}

bool induced_p3_disjoint_k2_on_roots_1_to_5(int mask) {
    std::array<int, 5> degrees{};
    int edges_seen = 0;
    const auto& edges = boundary_edges();
    for (int i = 0; i < static_cast<int>(edges.size()); ++i) {
        if (((mask >> i) & 1) == 0) continue;
        const auto [u, v] = edges.at(i);
        if (u == 0 || v == 0) continue;
        ++degrees.at(u - 1);
        ++degrees.at(v - 1);
        ++edges_seen;
    }
    std::sort(degrees.begin(), degrees.end());
    return edges_seen == 3 &&
           degrees == std::array<int, 5>{1, 1, 1, 1, 2};
}

std::string edge_string(int mask) {
    std::string out;
    const auto& edges = boundary_edges();
    for (int i = 0; i < static_cast<int>(edges.size()); ++i) {
        if (((mask >> i) & 1) != 0) {
            if (!out.empty()) out += ',';
            out += std::to_string(edges.at(i).first);
            out += std::to_string(edges.at(i).second);
        }
    }
    return out.empty() ? "(none)" : out;
}

struct ScreenResult {
    int tested = 0;
    std::map<int, int> negative_by_edges;
    int maximum_negative_edges = -1;
    std::vector<int> maximum_negative_masks;
    std::vector<int> all_negative_masks;
};

template <typename Predicate, typename Builder>
ScreenResult run_screen(int order, Predicate admissible, Builder builder) {
    generate_partitions(order);
    ScreenResult result;

    #pragma omp parallel
    {
        ScreenResult local;
        #pragma omp for schedule(dynamic, 16) nowait
        for (int mask = 0; mask < (1 << 15); ++mask) {
            if (!admissible(mask)) continue;
            ++local.tested;
            if (!contains_k7_minus(builder(mask))) {
                local.all_negative_masks.push_back(mask);
                const int edge_count = std::popcount(static_cast<unsigned>(mask));
                ++local.negative_by_edges[edge_count];
                if (edge_count > local.maximum_negative_edges) {
                    local.maximum_negative_edges = edge_count;
                    local.maximum_negative_masks = {mask};
                } else if (edge_count == local.maximum_negative_edges) {
                    local.maximum_negative_masks.push_back(mask);
                }
            }
        }
        #pragma omp critical
        {
            result.tested += local.tested;
            for (const auto& [edges, count] : local.negative_by_edges) {
                result.negative_by_edges[edges] += count;
            }
            result.all_negative_masks.insert(result.all_negative_masks.end(),
                                             local.all_negative_masks.begin(),
                                             local.all_negative_masks.end());
            if (local.maximum_negative_edges > result.maximum_negative_edges) {
                result.maximum_negative_edges = local.maximum_negative_edges;
                result.maximum_negative_masks = local.maximum_negative_masks;
            } else if (local.maximum_negative_edges == result.maximum_negative_edges) {
                result.maximum_negative_masks.insert(
                    result.maximum_negative_masks.end(),
                    local.maximum_negative_masks.begin(),
                    local.maximum_negative_masks.end());
            }
        }
    }
    std::sort(result.all_negative_masks.begin(), result.all_negative_masks.end());
    std::sort(result.maximum_negative_masks.begin(), result.maximum_negative_masks.end());
    return result;
}

void require(bool condition, const std::string& message) {
    if (!condition) throw std::runtime_error(message);
}

void print_result(const std::string& name, const ScreenResult& result) {
    std::cout << name << "\n";
    std::cout << "  tested: " << result.tested << "\n";
    std::cout << "  negative by boundary edges:";
    if (result.negative_by_edges.empty()) {
        std::cout << " none";
    } else {
        for (const auto& [edges, count] : result.negative_by_edges) {
            std::cout << ' ' << edges << ':' << count;
        }
    }
    std::cout << "\n";
    std::cout << "  maximum negative boundary size: "
              << result.maximum_negative_edges << "\n";
    if (!result.maximum_negative_masks.empty()) {
        std::cout << "  maximum negative masks:";
        for (int mask : result.maximum_negative_masks) {
            std::cout << " [" << edge_string(mask) << ']';
        }
        std::cout << "\n";
    }
}

void run_all() {
    const auto start = std::chrono::steady_clock::now();

    // Partition-universe sanity checks.
    generate_partitions(10);
    generate_partitions(11);
    generate_partitions(12);
    require(partitions_by_order.at(10).size() == 11880,
            "unexpected order-10 partition count");
    require(partitions_by_order.at(11).size() == 159027,
            "unexpected order-11 partition count");
    require(partitions_by_order.at(12).size() == 1899612,
            "unexpected order-12 partition count");
    std::cout << "partition counts: n=10 11880; n=11 159027; n=12 1899612\n\n";

    // In all labelled rows below, boundary edge 01 is the original
    // contraction edge.  Label 0 is the degree-five endpoint in the K2
    // and favourable P3/K3 rows; label 1 is that endpoint in the
    // unfavourable P3/K3 rows.
    auto edge01 = [](int mask) { return (mask & 1) != 0; };
    auto only_01_at_root0 = [&](int mask) {
        return edge01(mask) && boundary_degree(mask, 0) == 1;
    };

    for (Kernel kernel : {Kernel::kP3, Kernel::kK3}) {
        const ScreenResult one_singleton = run_screen(
            11,
            only_01_at_root0,
            [&](int mask) {
                return build_host(kernel, mask, 1, Extras::kOneSingleton, 0);
            });
        print_result(kernel_name(kernel) +
                         ": one six-full component plus one singleton missing root 0",
                     one_singleton);
        if (kernel == Kernel::kP3) {
            require(one_singleton.maximum_negative_edges == 4 &&
                        one_singleton.maximum_negative_masks.size() == 3,
                    "P3 favourable singleton threshold mismatch");
        } else {
            require(one_singleton.maximum_negative_edges == 3 &&
                        one_singleton.maximum_negative_masks.size() == 3,
                    "K3 favourable singleton threshold mismatch");
        }

        const ScreenResult tied_twins = run_screen(
            12,
            [&](int mask) {
                return only_01_at_root0(mask) &&
                       induced_p3_disjoint_k2_on_roots_1_to_5(mask);
            },
            [&](int mask) {
                return build_host(kernel, mask, 1, Extras::kTwoSingletons, 0);
            });
        print_result(kernel_name(kernel) +
                         ": one six-full component plus two tied singletons missing root 0",
                     tied_twins);
        require(tied_twins.tested == 30 && tied_twins.all_negative_masks.empty(),
                "tied-twin screen mismatch");

        const ScreenResult one_edge = run_screen(
            12,
            only_01_at_root0,
            [&](int mask) {
                return build_host(kernel, mask, 1, Extras::kOneEdge, 0);
            });
        print_result(kernel_name(kernel) +
                         ": one six-full component plus one full edge missing root 0",
                     one_edge);
        require(one_edge.tested == 1024 && one_edge.all_negative_masks.empty(),
                "favourable full-edge screen mismatch");
    }


    // In the unfavourable P3/K3 orientation, a pair of singleton
    // components with a common missed root already forces the target.  An
    // edge component is stronger, since adding its internal edge cannot
    // destroy a minor model.
    for (Kernel kernel : {Kernel::kP3, Kernel::kK3}) {
        for (int missed_root = 0; missed_root < 6; ++missed_root) {
            const ScreenResult twins = run_screen(
                12,
                [&](int mask) {
                    if ((mask & 1) == 0) return false;
                    if (missed_root == 1) {
                        return boundary_degree(mask, 1) <= 3;
                    }
                    return boundary_degree(mask, 1) == 1;
                },
                [&](int mask) {
                    return build_host(kernel, mask, 1,
                                      Extras::kTwoSingletons, missed_root);
                });
            require(twins.all_negative_masks.empty(),
                    "unfavourable one-full twin screen mismatch");
        }
        std::cout << kernel_name(kernel)
                  << ": every degree-compatible pair of full singleton extras"
                     " in the one-six-full unfavourable row is positive\n\n";
    }

    // The analogous K2 one-six-full row has one sharp edge-component
    // equality family.  Twin singleton components are excluded once the
    // tied five-cut boundary is P3 disjoint union K2.
    const ScreenResult k2_one_full_tied_twins = run_screen(
        11,
        [&](int mask) {
            return (mask & 1) != 0 && boundary_degree(mask, 0) <= 2 &&
                   induced_p3_disjoint_k2_on_roots_1_to_5(mask);
        },
        [&](int mask) {
            return build_host(Kernel::kK2, mask, 1,
                              Extras::kTwoSingletons, 0);
        });
    print_result("K2: one six-full representative plus tied twin singletons",
                 k2_one_full_tied_twins);
    require(k2_one_full_tied_twins.all_negative_masks.empty(),
            "K2 tied-twin screen mismatch");

    const ScreenResult k2_one_full_edge = run_screen(
        11,
        [&](int mask) {
            return (mask & 1) != 0 && boundary_degree(mask, 0) <= 2;
        },
        [&](int mask) {
            return build_host(Kernel::kK2, mask, 1,
                              Extras::kOneEdge, 0);
        });
    print_result("K2: one six-full representative plus one full edge missing root 0",
                 k2_one_full_edge);
    const std::vector<int> expected_k2_edge_survivors = {1, 513, 16385, 16897};
    require(k2_one_full_edge.all_negative_masks == expected_k2_edge_survivors,
            "K2 one-full edge equality family mismatch");

    const ScreenResult k2_two_full = run_screen(
        10,
        only_01_at_root0,
        [&](int mask) {
            return build_host(Kernel::kK2, mask, 2, Extras::kNone, -1);
        });
    print_result("K2: exactly two six-full representatives", k2_two_full);
    require(k2_two_full.tested == 1024 &&
                k2_two_full.maximum_negative_edges == 7 &&
                k2_two_full.maximum_negative_masks.size() == 1,
            "K2 two-full threshold mismatch");

    const ScreenResult k2_two_full_plus_singleton = run_screen(
        11,
        only_01_at_root0,
        [&](int mask) {
            return build_host(Kernel::kK2, mask, 2,
                              Extras::kOneSingleton, 0);
        });
    print_result("K2: two six-full representatives plus one singleton missing root 0",
                 k2_two_full_plus_singleton);
    require(k2_two_full_plus_singleton.tested == 1024 &&
                k2_two_full_plus_singleton.all_negative_masks.empty(),
            "K2 two-full extra screen mismatch");

    for (Kernel kernel : {Kernel::kP3, Kernel::kK3}) {
        const ScreenResult three_full = run_screen(
            12,
            [](int) { return true; },
            [&](int mask) {
                return build_host(kernel, mask, 3, Extras::kNone, -1);
            });
        print_result(kernel_name(kernel) + ": three six-full representatives",
                     three_full);
        require(three_full.tested == 32768 &&
                    three_full.all_negative_masks.empty(),
                "three-full screen mismatch");

        const ScreenResult two_full = run_screen(
            11,
            [&](int mask) {
                return edge01(mask) && boundary_degree(mask, 1) <= 2;
            },
            [&](int mask) {
                return build_host(kernel, mask, 2, Extras::kNone, -1);
            });
        print_result(kernel_name(kernel) +
                         ": two six-full representatives, degree(root 1)<=2",
                     two_full);
        require(two_full.tested == 5120 &&
                    two_full.maximum_negative_edges == 4 &&
                    two_full.maximum_negative_masks.size() == 3,
                "P3/K3 two-full threshold mismatch");

        std::vector<int> exact_degree_two_negatives;
        for (int mask : two_full.all_negative_masks) {
            if (boundary_degree(mask, 1) == 2) {
                exact_degree_two_negatives.push_back(mask);
            }
        }
        require(exact_degree_two_negatives.size() == 8,
                "expected eight exact-degree-two negative boundaries");
        std::cout << "  exact degree-two negative masks (8):";
        for (int mask : exact_degree_two_negatives) {
            std::cout << " [" << edge_string(mask) << ']';
        }
        std::cout << "\n";

        const ScreenResult two_full_plus_missing_u = run_screen(
            12,
            [&](int mask) {
                return edge01(mask) && boundary_degree(mask, 1) <= 2;
            },
            [&](int mask) {
                return build_host(kernel, mask, 2,
                                  Extras::kOneSingleton, 1);
            });
        print_result(kernel_name(kernel) +
                         ": two six-full representatives plus singleton missing root 1",
                     two_full_plus_missing_u);
        require(two_full_plus_missing_u.tested == 5120 &&
                    two_full_plus_missing_u.all_negative_masks.empty(),
                "two-full missing-u extra screen mismatch");

        for (int missed_root : {0, 2, 3, 4, 5}) {
            const ScreenResult other_singleton = run_screen(
                12,
                [&](int mask) {
                    return edge01(mask) && boundary_degree(mask, 1) == 1;
                },
                [&](int mask) {
                    return build_host(kernel, mask, 2,
                                      Extras::kOneSingleton, missed_root);
                });
            require(other_singleton.tested == 1024 &&
                        other_singleton.all_negative_masks.empty(),
                    "two-full other-root extra screen mismatch");
        }
        std::cout << kernel_name(kernel)
                  << ": every one-singleton extra allowed by the degree-five root is positive\n\n";
    }



    // When root 1 has boundary degree one, the degree-five count puts two
    // of its neighbours in one of the two six-full components.  Splitting
    // that connected component between those two neighbours leaves only
    // the following target-free contact pattern: all portals to roots
    // 3,4,5 are concentrated exclusively in one split piece.
    const std::vector<int> degree_one_boundary_masks = {
        1, 3, 4097, 4099, 8193, 8195, 16385, 16387,
    };
    for (Kernel kernel : {Kernel::kP3, Kernel::kK3}) {
        for (int boundary_mask : degree_one_boundary_masks) {
            int negative_count = 0;
            int concentrated_count = 0;
            for (int code = 0; code < 243; ++code) {
                const SplitContactPattern pattern =
                    decode_two_u_split_pattern(code);
                const bool concentrated = all_exclusive_on_one_side(
                    pattern, {3, 4, 5});
                if (concentrated) ++concentrated_count;
                const bool negative = !contains_k7_minus(
                    build_two_u_split_host(kernel, boundary_mask, code));
                if (negative) {
                    ++negative_count;
                    require(concentrated,
                            "unexpected two-u split-contact survivor");
                }
            }
            require(negative_count == 18 && concentrated_count == 18,
                    "two-u split-contact characterization mismatch");
        }
        std::cout << kernel_name(kernel)
                  << ": all eight degree-one-boundary split screens have"
                     " exactly the 18 concentrated-portal survivors\n";
    }
    std::cout << '\n';

    // Equality micro-screen used after the rooted-K4 argument in the exact
    // two-six-full K3 row.  It classifies every way a connected full
    // component can be split into two adjacent connected pieces when one
    // boundary root is adjacent to every vertex of that component.
    struct SplitCase {
        const char* name;
        int boundary_mask;
        int universal_root;
        std::vector<int> concentrated_roots;
        int expected_negatives;
    };
    const std::vector<SplitCase> split_cases = {
        {"boundary triangle, universal root 0", 35, 0, {3, 4, 5}, 12},
        {"boundary triangle, universal root 2", 35, 2, {3, 4, 5}, 12},
        {"boundary U-edge, universal root 3", 4129, 3, {0, 1, 2, 5}, 6},
        {"boundary U-edge, universal root 4", 4129, 4, {0, 1, 2, 5}, 6},
    };
    for (const SplitCase& split_case : split_cases) {
        int negative_count = 0;
        int concentrated_count = 0;
        const int patterns = split_pattern_count(split_case.universal_root);
        for (int code = 0; code < patterns; ++code) {
            const SplitContactPattern pattern =
                decode_split_pattern(code, split_case.universal_root);
            const bool concentrated = all_exclusive_on_one_side(
                pattern, split_case.concentrated_roots);
            if (concentrated) ++concentrated_count;
            const bool negative = !contains_k7_minus(build_k3_split_host(
                split_case.boundary_mask, split_case.universal_root, code));
            if (negative) {
                ++negative_count;
                require(concentrated,
                        std::string("unexpected split-contact survivor in ") +
                            split_case.name);
            }
        }
        require(negative_count == split_case.expected_negatives,
                std::string("split-contact negative count mismatch in ") +
                    split_case.name);
        require(concentrated_count == split_case.expected_negatives,
                std::string("split-contact characterization mismatch in ") +
                    split_case.name);
        std::cout << "K3 split-contact equality screen: "
                  << split_case.name << "\n"
                  << "  patterns: " << patterns
                  << "; target-free: " << negative_count
                  << "; exactly the concentrated-portal patterns\n";
    }
    std::cout << '\n';

    const auto elapsed = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - start).count();
    std::cout << "ALL CHECKS PASSED\n";
    std::cout << "wall_seconds: " << elapsed << "\n";
}

}  // namespace

int main() {
    try {
        run_all();
        return EXIT_SUCCESS;
    } catch (const std::exception& error) {
        std::cerr << "FAIL: " << error.what() << '\n';
        return EXIT_FAILURE;
    }
}
