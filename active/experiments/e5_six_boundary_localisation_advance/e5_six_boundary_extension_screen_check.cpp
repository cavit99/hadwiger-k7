#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <initializer_list>
#include <map>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

// Independent exhaustive checker for the E5 six-boundary extension screen.
//
// The checked hosts have at most twelve vertices.  A K_7^- minor is therefore
// equivalent to seven disjoint nonempty connected vertex sets whose quotient
// has at most one nonedge.  This checker generates the complete model universe
// by scanning host vertices once and deciding independently whether each
// vertex is unused, joins an existing block, or starts the next block.  This
// differs from the primary screen's subset-then-partition generator.

namespace {

using Bits = std::uint16_t;

constexpr int kRoots = 6;
constexpr int kTargetOrder = 7;
constexpr int kBoundaryChoices = 15;

struct Graph {
    std::vector<Bits> neighbours;

    explicit Graph(int order) : neighbours(order, 0) {}

    int order() const { return static_cast<int>(neighbours.size()); }

    void join(int left, int right) {
        if (left == right) throw std::runtime_error("loop in host construction");
        neighbours.at(left) |= static_cast<Bits>(Bits{1} << right);
        neighbours.at(right) |= static_cast<Bits>(Bits{1} << left);
    }
};

struct SevenBlocks {
    std::array<Bits, kTargetOrder> block{};
};

class MinorOracle {
  public:
    const std::vector<SevenBlocks>& models(int order) {
        auto found = model_cache_.find(order);
        if (found != model_cache_.end()) return found->second;

        std::array<std::vector<SevenBlocks>, 13> by_used_order;
        std::array<Bits, kTargetOrder> blocks{};
        generate_assignments(order, 0, 0, 0, blocks, by_used_order);

        std::vector<SevenBlocks> catalogue;
        for (int used = kTargetOrder; used <= order; ++used) {
            catalogue.insert(catalogue.end(), by_used_order.at(used).begin(),
                             by_used_order.at(used).end());
        }
        return model_cache_.emplace(order, std::move(catalogue)).first->second;
    }

    bool contains_target(const Graph& graph) {
        const int order = graph.order();
        const int subset_limit = 1 << order;
        std::vector<bool> connected(subset_limit, false);
        std::vector<Bits> contacts(subset_limit, 0);

        for (int subset = 1; subset < subset_limit; ++subset) {
            Bits unused = static_cast<Bits>(subset);
            Bits reached = static_cast<Bits>(unused & static_cast<Bits>(-unused));
            Bits frontier = reached;
            while (frontier != 0) {
                const Bits vertex_bit =
                    static_cast<Bits>(frontier & static_cast<Bits>(-frontier));
                frontier = static_cast<Bits>(frontier ^ vertex_bit);
                const int vertex = std::countr_zero(vertex_bit);
                const Bits next = static_cast<Bits>(
                    graph.neighbours.at(vertex) & subset &
                    static_cast<Bits>(~reached));
                reached = static_cast<Bits>(reached | next);
                frontier = static_cast<Bits>(frontier | next);
            }
            connected.at(subset) = reached == subset;

            Bits union_of_neighbours = 0;
            Bits vertices = static_cast<Bits>(subset);
            while (vertices != 0) {
                const Bits vertex_bit =
                    static_cast<Bits>(vertices & static_cast<Bits>(-vertices));
                vertices = static_cast<Bits>(vertices ^ vertex_bit);
                union_of_neighbours = static_cast<Bits>(
                    union_of_neighbours |
                    graph.neighbours.at(std::countr_zero(vertex_bit)));
            }
            contacts.at(subset) = union_of_neighbours;
        }

        for (const SevenBlocks& candidate : models(order)) {
            bool valid = true;
            for (Bits block : candidate.block) {
                if (!connected.at(block)) {
                    valid = false;
                    break;
                }
            }
            if (!valid) continue;

            int absent_pairs = 0;
            for (int first = 0; first < kTargetOrder && absent_pairs <= 1;
                 ++first) {
                for (int second = first + 1; second < kTargetOrder; ++second) {
                    if ((contacts.at(candidate.block.at(first)) &
                         candidate.block.at(second)) == 0) {
                        ++absent_pairs;
                        if (absent_pairs > 1) break;
                    }
                }
            }
            if (absent_pairs <= 1) return true;
        }
        return false;
    }

  private:
    std::map<int, std::vector<SevenBlocks>> model_cache_;

    static void generate_assignments(
        int order, int vertex, int block_count, int used_order,
        std::array<Bits, kTargetOrder>& blocks,
        std::array<std::vector<SevenBlocks>, 13>& by_used_order) {
        const int remaining = order - vertex;
        if (block_count + remaining < kTargetOrder) return;
        if (vertex == order) {
            if (block_count == kTargetOrder) {
                SevenBlocks model;
                model.block = blocks;
                by_used_order.at(used_order).push_back(model);
            }
            return;
        }

        // The vertex is unused.
        generate_assignments(order, vertex + 1, block_count, used_order,
                             blocks, by_used_order);

        const Bits vertex_bit = static_cast<Bits>(Bits{1} << vertex);
        // It joins a block whose least vertex has already fixed that block's
        // canonical position.
        for (int block = 0; block < block_count; ++block) {
            blocks.at(block) = static_cast<Bits>(blocks.at(block) | vertex_bit);
            generate_assignments(order, vertex + 1, block_count,
                                 used_order + 1, blocks, by_used_order);
            blocks.at(block) = static_cast<Bits>(blocks.at(block) ^ vertex_bit);
        }

        // Or it is the least vertex of the next canonical block.
        if (block_count < kTargetOrder) {
            blocks.at(block_count) = vertex_bit;
            generate_assignments(order, vertex + 1, block_count + 1,
                                 used_order + 1, blocks, by_used_order);
            blocks.at(block_count) = 0;
        }
    }
};

const std::array<std::pair<int, int>, kBoundaryChoices>& root_pairs() {
    static const std::array<std::pair<int, int>, kBoundaryChoices> pairs = [] {
        std::array<std::pair<int, int>, kBoundaryChoices> result{};
        int next = 0;
        for (int left = 0; left < kRoots; ++left) {
            for (int right = left + 1; right < kRoots; ++right) {
                result.at(next++) = {left, right};
            }
        }
        return result;
    }();
    return pairs;
}

int edge_bit(int left, int right) {
    if (left > right) std::swap(left, right);
    for (int bit = 0; bit < kBoundaryChoices; ++bit) {
        if (root_pairs().at(bit) == std::pair{left, right}) return 1 << bit;
    }
    throw std::runtime_error("unknown root pair");
}

int edges(std::initializer_list<std::pair<int, int>> selected) {
    int mask = 0;
    for (auto [left, right] : selected) mask |= edge_bit(left, right);
    return mask;
}

void add_boundary(Graph& graph, int mask) {
    for (int bit = 0; bit < kBoundaryChoices; ++bit) {
        if ((mask >> bit) & 1) {
            const auto [left, right] = root_pairs().at(bit);
            graph.join(left, right);
        }
    }
}

int degree_in_boundary(int mask, int root) {
    int degree = 0;
    for (int bit = 0; bit < kBoundaryChoices; ++bit) {
        const auto [left, right] = root_pairs().at(bit);
        if (((mask >> bit) & 1) && (left == root || right == root)) ++degree;
    }
    return degree;
}

enum class LowGraph { kAdjacentPair, kPath, kTriangle };
enum class Addition { kNothing, kSingleton, kTwins, kEdge };

int low_order(LowGraph low) {
    return low == LowGraph::kAdjacentPair ? 2 : 3;
}

void add_low_graph(Graph& graph, LowGraph low) {
    if (low == LowGraph::kAdjacentPair) {
        graph.join(6, 7);
        for (int root : {0, 1, 2, 3}) graph.join(6, root);
        for (int root : {0, 1, 4, 5}) graph.join(7, root);
        return;
    }

    graph.join(6, 7);
    graph.join(6, 8);
    if (low == LowGraph::kTriangle) graph.join(7, 8);
    for (int root : {0, 1, 2}) graph.join(6, root);
    for (int leaf : {7, 8}) {
        for (int root : {0, 3, 4, 5}) graph.join(leaf, root);
    }
}

Graph ordinary_host(LowGraph low, int boundary_mask, int full_components,
                    Addition addition, int absent_root = -1) {
    const int added_vertices =
        addition == Addition::kNothing ? 0 :
        addition == Addition::kSingleton ? 1 : 2;
    Graph graph(kRoots + low_order(low) + full_components + added_vertices);
    add_boundary(graph, boundary_mask);
    add_low_graph(graph, low);

    int next = kRoots + low_order(low);
    for (int index = 0; index < full_components; ++index, ++next) {
        for (int root = 0; root < kRoots; ++root) graph.join(next, root);
    }

    if (addition != Addition::kNothing) {
        const int first = next;
        if (addition == Addition::kEdge) graph.join(first, first + 1);
        for (int vertex = first; vertex < first + added_vertices; ++vertex) {
            for (int root = 0; root < kRoots; ++root) {
                if (root != absent_root) graph.join(vertex, root);
            }
        }
    }
    return graph;
}

bool is_path_plus_edge_on_roots_1_to_5(int mask) {
    std::array<int, 5> degree{};
    int edge_count = 0;
    for (int bit = 0; bit < kBoundaryChoices; ++bit) {
        if (!((mask >> bit) & 1)) continue;
        const auto [left, right] = root_pairs().at(bit);
        if (left == 0 || right == 0) continue;
        ++degree.at(left - 1);
        ++degree.at(right - 1);
        ++edge_count;
    }
    std::sort(degree.begin(), degree.end());
    return edge_count == 3 && degree == std::array<int, 5>{1, 1, 1, 1, 2};
}

struct Distribution {
    int tested = 0;
    std::array<int, 16> target_free_by_edges{};
    std::vector<int> target_free_masks;
};

template <typename Admissible, typename Builder>
Distribution catalogue(MinorOracle& oracle, Admissible admissible,
                       Builder builder) {
    Distribution result;
    for (int mask = 0; mask < (1 << kBoundaryChoices); ++mask) {
        if (!admissible(mask)) continue;
        ++result.tested;
        if (!oracle.contains_target(builder(mask))) {
            ++result.target_free_by_edges.at(std::popcount(
                static_cast<unsigned>(mask)));
            result.target_free_masks.push_back(mask);
        }
    }
    return result;
}

void insist(bool condition, const std::string& message) {
    if (!condition) throw std::runtime_error(message);
}

void expect_distribution(const Distribution& actual, int tested,
                         std::initializer_list<std::pair<int, int>> counts,
                         const std::string& label) {
    insist(actual.tested == tested, label + ": catalogue size mismatch");
    std::array<int, 16> expected{};
    for (auto [edge_count, count] : counts) expected.at(edge_count) = count;
    insist(actual.target_free_by_edges == expected,
           label + ": target-free distribution mismatch");
}

void sanity_checks(MinorOracle& oracle) {
    Graph positive(7);
    Graph two_missing(7);
    for (int left = 0; left < 7; ++left) {
        for (int right = left + 1; right < 7; ++right) {
            if (std::pair{left, right} != std::pair{0, 1}) {
                positive.join(left, right);
            }
            if (std::pair{left, right} != std::pair{0, 1} &&
                std::pair{left, right} != std::pair{0, 2}) {
                two_missing.join(left, right);
            }
        }
    }
    insist(oracle.contains_target(positive), "K7-minus sanity false negative");
    insist(!oracle.contains_target(two_missing), "K7-vee sanity false positive");

    Graph complement_of_path(8);
    for (int left = 0; left < 8; ++left) {
        for (int right = left + 1; right < 8; ++right) {
            if (right != left + 1) complement_of_path.join(left, right);
        }
    }
    insist(!oracle.contains_target(complement_of_path),
           "complement(P8) sanity false positive");
}

void check_favourable_one_full(MinorOracle& oracle, LowGraph low,
                               const std::string& label) {
    const auto only_original_edge_at_zero = [](int mask) {
        return (mask & 1) && degree_in_boundary(mask, 0) == 1;
    };

    const Distribution singleton = catalogue(
        oracle, only_original_edge_at_zero,
        [&](int mask) {
            return ordinary_host(low, mask, 1, Addition::kSingleton, 0);
        });
    if (low == LowGraph::kPath) {
        expect_distribution(singleton, 1024, {{1, 1}, {2, 7}, {3, 9}, {4, 3}},
                            label + " favourable singleton");
        const std::vector<int> maximum = {
            edges({{0, 1}, {1, 2}, {1, 5}, {3, 4}}),
            edges({{0, 1}, {1, 2}, {1, 4}, {3, 5}}),
            edges({{0, 1}, {1, 2}, {1, 3}, {4, 5}}),
        };
        std::vector<int> actual;
        for (int mask : singleton.target_free_masks) {
            if (std::popcount(static_cast<unsigned>(mask)) == 4) {
                actual.push_back(mask);
            }
        }
        auto expected = maximum;
        std::sort(expected.begin(), expected.end());
        insist(actual == expected, label + ": maximum singleton masks mismatch");
    } else {
        expect_distribution(singleton, 1024, {{1, 1}, {2, 4}, {3, 3}},
                            label + " favourable singleton");
        std::vector<int> expected = {
            edges({{0, 1}, {1, 2}, {3, 4}}),
            edges({{0, 1}, {1, 2}, {3, 5}}),
            edges({{0, 1}, {1, 2}, {4, 5}}),
        };
        std::sort(expected.begin(), expected.end());
        std::vector<int> actual;
        for (int mask : singleton.target_free_masks) {
            if (std::popcount(static_cast<unsigned>(mask)) == 3) {
                actual.push_back(mask);
            }
        }
        insist(actual == expected, label + ": maximum singleton masks mismatch");
    }

    const Distribution tied_twins = catalogue(
        oracle,
        [&](int mask) {
            return only_original_edge_at_zero(mask) &&
                   is_path_plus_edge_on_roots_1_to_5(mask);
        },
        [&](int mask) {
            return ordinary_host(low, mask, 1, Addition::kTwins, 0);
        });
    expect_distribution(tied_twins, 30, {}, label + " tied twins");

    const Distribution full_edge = catalogue(
        oracle, only_original_edge_at_zero,
        [&](int mask) {
            return ordinary_host(low, mask, 1, Addition::kEdge, 0);
        });
    expect_distribution(full_edge, 1024, {}, label + " full edge");
}

void check_unfavourable_one_full(MinorOracle& oracle, LowGraph low,
                                 const std::string& label) {
    int total = 0;
    for (int absent_root = 0; absent_root < kRoots; ++absent_root) {
        const Distribution twins = catalogue(
            oracle,
            [&](int mask) {
                if (!(mask & 1)) return false;
                return absent_root == 1 ? degree_in_boundary(mask, 1) <= 3
                                        : degree_in_boundary(mask, 1) == 1;
            },
            [&](int mask) {
                return ordinary_host(low, mask, 1, Addition::kTwins,
                                     absent_root);
            });
        const int expected = absent_root == 1 ? 11264 : 1024;
        expect_distribution(twins, expected, {}, label + " unfavourable twins");
        total += twins.tested;
    }
    insist(total == 16384, label + ": unfavourable aggregate mismatch");
}

void check_adjacent_pair_rows(MinorOracle& oracle) {
    const Distribution tied_twins = catalogue(
        oracle,
        [](int mask) {
            return (mask & 1) && degree_in_boundary(mask, 0) <= 2 &&
                   is_path_plus_edge_on_roots_1_to_5(mask);
        },
        [](int mask) {
            return ordinary_host(LowGraph::kAdjacentPair, mask, 1,
                                 Addition::kTwins, 0);
        });
    expect_distribution(tied_twins, 150, {}, "K2 tied twins");

    const Distribution full_edge = catalogue(
        oracle,
        [](int mask) {
            return (mask & 1) && degree_in_boundary(mask, 0) <= 2;
        },
        [](int mask) {
            return ordinary_host(LowGraph::kAdjacentPair, mask, 1,
                                 Addition::kEdge, 0);
        });
    expect_distribution(full_edge, 5120, {{1, 1}, {2, 2}, {3, 1}},
                        "K2 one-full edge");
    std::vector<int> expected_edge_masks = {
        edges({{0, 1}}),
        edges({{0, 1}, {2, 3}}),
        edges({{0, 1}, {4, 5}}),
        edges({{0, 1}, {2, 3}, {4, 5}}),
    };
    std::sort(expected_edge_masks.begin(), expected_edge_masks.end());
    insist(full_edge.target_free_masks == expected_edge_masks,
           "K2 one-full edge survivor mismatch");

    const auto only_original_edge_at_zero = [](int mask) {
        return (mask & 1) && degree_in_boundary(mask, 0) == 1;
    };
    const Distribution two_full = catalogue(
        oracle, only_original_edge_at_zero,
        [](int mask) {
            return ordinary_host(LowGraph::kAdjacentPair, mask, 2,
                                 Addition::kNothing);
        });
    expect_distribution(two_full, 1024,
                        {{1, 1}, {2, 10}, {3, 37}, {4, 64},
                         {5, 54}, {6, 14}, {7, 1}},
                        "K2 two-full");
    std::vector<int> seven_edge_masks;
    for (int mask : two_full.target_free_masks) {
        if (std::popcount(static_cast<unsigned>(mask)) == 7) {
            seven_edge_masks.push_back(mask);
        }
    }
    insist(seven_edge_masks == std::vector<int>{edges(
               {{0, 1}, {1, 2}, {1, 3}, {1, 4}, {1, 5}, {2, 3}, {4, 5}})},
           "K2 unique seven-edge boundary mismatch");

    const Distribution extra = catalogue(
        oracle, only_original_edge_at_zero,
        [](int mask) {
            return ordinary_host(LowGraph::kAdjacentPair, mask, 2,
                                 Addition::kSingleton, 0);
        });
    expect_distribution(extra, 1024, {}, "K2 two-full plus singleton");
}

std::vector<int> expected_two_full_survivors() {
    std::vector<int> result;
    for (bool use_02 : {false, true}) {
        for (bool use_12 : {false, true}) {
            for (int extra : {0, edge_bit(3, 4), edge_bit(3, 5), edge_bit(4, 5)}) {
                int mask = edge_bit(0, 1) | extra;
                if (use_02) mask |= edge_bit(0, 2);
                if (use_12) mask |= edge_bit(1, 2);
                result.push_back(mask);
            }
        }
    }
    std::sort(result.begin(), result.end());
    return result;
}

void check_path_triangle_multi_full(MinorOracle& oracle, LowGraph low,
                                    const std::string& label) {
    const Distribution three_full = catalogue(
        oracle, [](int) { return true; },
        [&](int mask) {
            return ordinary_host(low, mask, 3, Addition::kNothing);
        });
    expect_distribution(three_full, 32768, {}, label + " three-full");

    const Distribution two_full = catalogue(
        oracle,
        [](int mask) {
            return (mask & 1) && degree_in_boundary(mask, 1) <= 2;
        },
        [&](int mask) {
            return ordinary_host(low, mask, 2, Addition::kNothing);
        });
    expect_distribution(two_full, 5120,
                        {{1, 1}, {2, 5}, {3, 7}, {4, 3}},
                        label + " two-full");
    insist(two_full.target_free_masks == expected_two_full_survivors(),
           label + ": exact two-full survivor mismatch");

    const Distribution missing_u = catalogue(
        oracle,
        [](int mask) {
            return (mask & 1) && degree_in_boundary(mask, 1) <= 2;
        },
        [&](int mask) {
            return ordinary_host(low, mask, 2, Addition::kSingleton, 1);
        });
    expect_distribution(missing_u, 5120, {}, label + " extra missing u");

    int other_total = 0;
    for (int absent_root : {0, 2, 3, 4, 5}) {
        const Distribution other = catalogue(
            oracle,
            [](int mask) {
                return (mask & 1) && degree_in_boundary(mask, 1) == 1;
            },
            [&](int mask) {
                return ordinary_host(low, mask, 2, Addition::kSingleton,
                                     absent_root);
            });
        expect_distribution(other, 1024, {}, label + " other extra");
        other_total += other.tested;
    }
    insist(other_total == 5120, label + ": other-extra aggregate mismatch");
}

std::array<int, 6> ternary_contacts(int code, int forced_both,
                                    bool root_one_both) {
    std::array<int, 6> contact{};
    if (forced_both >= 0) contact.at(forced_both) = 3;
    if (root_one_both) contact.at(1) = 3;
    for (int root = 0; root < kRoots; ++root) {
        if (root == forced_both || (root == 1 && root_one_both)) continue;
        if (root == 1) {
            contact.at(root) = 1 + code % 2;
            code /= 2;
        } else {
            contact.at(root) = 1 + code % 3;
            code /= 3;
        }
    }
    return contact;
}

Graph split_component_host(LowGraph low, int boundary_mask,
                           const std::array<int, 6>& contact) {
    Graph graph(12);
    add_boundary(graph, boundary_mask);
    add_low_graph(graph, low);
    graph.join(9, 10);
    for (int root = 0; root < kRoots; ++root) {
        if (contact.at(root) & 1) graph.join(9, root);
        if (contact.at(root) & 2) graph.join(10, root);
        graph.join(11, root);
    }
    return graph;
}

bool exclusively_one_side(const std::array<int, 6>& contact,
                          std::initializer_list<int> roots) {
    const int side = contact.at(*roots.begin());
    if (side != 1 && side != 2) return false;
    return std::all_of(roots.begin(), roots.end(),
                       [&](int root) { return contact.at(root) == side; });
}

void check_portal_catalogues(MinorOracle& oracle) {
    std::vector<int> degree_one_boundaries;
    for (bool use_02 : {false, true}) {
        for (int extra : {0, edge_bit(3, 4), edge_bit(3, 5), edge_bit(4, 5)}) {
            int mask = edge_bit(0, 1) | extra;
            if (use_02) mask |= edge_bit(0, 2);
            degree_one_boundaries.push_back(mask);
        }
    }

    int two_u_hosts = 0;
    for (LowGraph low : {LowGraph::kPath, LowGraph::kTriangle}) {
        for (int mask : degree_one_boundaries) {
            int target_free = 0;
            for (int code = 0; code < 243; ++code) {
                const auto contact = ternary_contacts(code, -1, true);
                const bool negative =
                    !oracle.contains_target(split_component_host(low, mask, contact));
                insist(negative == exclusively_one_side(contact, {3, 4, 5}),
                       "two-u portal characterization mismatch");
                target_free += negative;
                ++two_u_hosts;
            }
            insist(target_free == 18, "two-u portal count mismatch");
        }
    }
    insist(two_u_hosts == 3888, "two-u portal coverage mismatch");

    struct EqualityCase {
        int mask;
        int universal_root;
        std::vector<int> concentrated_roots;
        int target_free;
    };
    const std::vector<EqualityCase> equality_cases = {
        {edges({{0, 1}, {0, 2}, {1, 2}}), 0, {3, 4, 5}, 12},
        {edges({{0, 1}, {0, 2}, {1, 2}}), 2, {3, 4, 5}, 12},
        {edges({{0, 1}, {1, 2}, {3, 4}}), 3, {0, 1, 2, 5}, 6},
        {edges({{0, 1}, {1, 2}, {3, 4}}), 4, {0, 1, 2, 5}, 6},
    };

    int equality_hosts = 0;
    for (const EqualityCase& item : equality_cases) {
        int negatives = 0;
        for (int code = 0; code < 162; ++code) {
            const auto contact = ternary_contacts(code, item.universal_root, false);
            const int side = contact.at(item.concentrated_roots.front());
            const bool vector_concentrated =
                (side == 1 || side == 2) &&
                std::all_of(item.concentrated_roots.begin(),
                            item.concentrated_roots.end(),
                            [&](int root) { return contact.at(root) == side; });
            const bool negative = !oracle.contains_target(
                split_component_host(LowGraph::kTriangle, item.mask, contact));
            insist(negative == vector_concentrated,
                   "K3 equality portal characterization mismatch");
            negatives += negative;
            ++equality_hosts;
        }
        insist(negatives == item.target_free,
               "K3 equality portal count mismatch");
    }
    insist(equality_hosts == 648, "K3 equality portal coverage mismatch");
}

void run() {
    MinorOracle oracle;
    sanity_checks(oracle);

    insist(oracle.models(10).size() == 11880,
           "order-10 model universe mismatch");
    insist(oracle.models(11).size() == 159027,
           "order-11 model universe mismatch");
    insist(oracle.models(12).size() == 1899612,
           "order-12 model universe mismatch");

    check_favourable_one_full(oracle, LowGraph::kPath, "P3");
    check_favourable_one_full(oracle, LowGraph::kTriangle, "K3");
    check_unfavourable_one_full(oracle, LowGraph::kPath, "P3");
    check_unfavourable_one_full(oracle, LowGraph::kTriangle, "K3");
    check_adjacent_pair_rows(oracle);
    check_path_triangle_multi_full(oracle, LowGraph::kPath, "P3");
    check_path_triangle_multi_full(oracle, LowGraph::kTriangle, "K3");
    check_portal_catalogues(oracle);

    std::cout << "PASS independent E5 six-boundary extension check\n"
              << "ordinary hosts checked: 140498\n"
              << "portal hosts checked: 4536\n"
              << "total finite hosts checked: 145034\n"
              << "model universes: n=10 11880; n=11 159027; n=12 1899612\n";
}

}  // namespace

int main() {
    try {
        run();
        return EXIT_SUCCESS;
    } catch (const std::exception& error) {
        std::cerr << "FAIL: " << error.what() << '\n';
        return EXIT_FAILURE;
    }
}
