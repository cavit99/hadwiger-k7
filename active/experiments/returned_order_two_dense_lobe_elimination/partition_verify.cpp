// Independent exact verifier for the returned order-two dense-lobe theorem.
//
// Unlike recursive_verify.py, this program does not search through minor
// operations.  It generates directly all partitions of every 7-, 8-, or
// 9-vertex subset of the quotient into seven nonempty branch sets.  There
// are exactly 750 such partitions.  It checks connectedness of every bag
// and accepts precisely when at most one pair of bags is nonadjacent.

#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <utility>
#include <vector>

using Partition = std::array<std::uint16_t, 7>;

namespace {

std::vector<Partition> partitions;

void generate_partitions(const std::vector<int>& vertices, int position,
                         std::vector<std::uint16_t>& blocks) {
  if (position == static_cast<int>(vertices.size())) {
    if (blocks.size() == 7) {
      Partition partition{};
      std::copy(blocks.begin(), blocks.end(), partition.begin());
      partitions.push_back(partition);
    }
    return;
  }

  const int remaining = static_cast<int>(vertices.size()) - position;
  if (blocks.size() > 7 ||
      static_cast<int>(blocks.size()) + remaining < 7) {
    return;
  }

  const std::uint16_t bit = std::uint16_t{1} << vertices[position];
  for (int index = 0; index < static_cast<int>(blocks.size()); ++index) {
    blocks[index] |= bit;
    generate_partitions(vertices, position + 1, blocks);
    blocks[index] ^= bit;
  }
  if (blocks.size() < 7) {
    blocks.push_back(bit);
    generate_partitions(vertices, position + 1, blocks);
    blocks.pop_back();
  }
}

void add_edge(std::array<std::uint16_t, 9>& adjacency, int left,
              int right) {
  adjacency[left] |= std::uint16_t{1} << right;
  adjacency[right] |= std::uint16_t{1} << left;
}

bool connected(std::uint16_t bag,
               const std::array<std::uint16_t, 9>& adjacency) {
  std::uint16_t reached = bag & -bag;
  std::uint16_t frontier = reached;
  while (frontier != 0) {
    const int vertex = __builtin_ctz(frontier);
    frontier &= frontier - 1;
    const std::uint16_t fresh = adjacency[vertex] & bag & ~reached;
    reached |= fresh;
    frontier |= fresh;
  }
  return reached == bag;
}

bool touching(std::uint16_t left, std::uint16_t right,
              const std::array<std::uint16_t, 9>& adjacency) {
  while (left != 0) {
    const int vertex = __builtin_ctz(left);
    left &= left - 1;
    if ((adjacency[vertex] & right) != 0) {
      return true;
    }
  }
  return false;
}

bool has_near_seven_minor(
    const std::array<std::uint16_t, 9>& adjacency) {
  for (const Partition& partition : partitions) {
    bool all_connected = true;
    for (std::uint16_t bag : partition) {
      if (!connected(bag, adjacency)) {
        all_connected = false;
        break;
      }
    }
    if (!all_connected) {
      continue;
    }

    int missing = 0;
    for (int left = 0; left < 7 && missing <= 1; ++left) {
      for (int right = left + 1; right < 7; ++right) {
        if (!touching(partition[left], partition[right], adjacency)) {
          ++missing;
          if (missing > 1) {
            break;
          }
        }
      }
    }
    if (missing <= 1) {
      return true;
    }
  }
  return false;
}

}  // namespace

int main() {
  for (int used_mask = 0; used_mask < (1 << 9); ++used_mask) {
    const int used_count = __builtin_popcount(
        static_cast<unsigned int>(used_mask));
    if (used_count < 7) {
      continue;
    }
    std::vector<int> vertices;
    for (int vertex = 0; vertex < 9; ++vertex) {
      if ((used_mask & (1 << vertex)) != 0) {
        vertices.push_back(vertex);
      }
    }
    std::vector<std::uint16_t> blocks;
    generate_partitions(vertices, 0, blocks);
  }
  assert(partitions.size() == 750);

  // Larger bags first makes positive certificates appear early, without
  // changing the exhaustive set of partitions.
  std::stable_sort(
      partitions.begin(), partitions.end(),
      [](const Partition& left, const Partition& right) {
        const auto score = [](const Partition& partition) {
          int answer = 0;
          for (std::uint16_t bag : partition) {
            const int size = __builtin_popcount(
                static_cast<unsigned int>(bag));
            answer += size * size;
          }
          return answer;
        };
        return score(left) > score(right);
      });

  std::vector<std::pair<int, int>> separator_edges;
  for (int left = 0; left < 6; ++left) {
    for (int right = left + 1; right < 6; ++right) {
      separator_edges.push_back({left, right});
    }
  }

  std::array<long long, 12> checked{};
  std::array<long long, 12> positive{};

  for (int edge_count = 9; edge_count <= 11; ++edge_count) {
    const int single_count = edge_count - 9;
    for (int separator_mask = 0; separator_mask < (1 << 15);
         ++separator_mask) {
      if (__builtin_popcount(
              static_cast<unsigned int>(separator_mask)) != edge_count) {
        continue;
      }

      for (int status_code = 0; status_code < 729; ++status_code) {
        int remainder = status_code;
        int non_both = 0;
        std::array<int, 6> status{};
        for (int vertex = 0; vertex < 6; ++vertex) {
          status[vertex] = remainder % 3;
          remainder /= 3;
          non_both += status[vertex] != 2;
        }
        if (non_both != single_count) {
          continue;
        }

        std::array<std::uint16_t, 9> adjacency{};
        for (int bit = 0; bit < 15; ++bit) {
          if ((separator_mask & (1 << bit)) != 0) {
            add_edge(adjacency, separator_edges[bit].first,
                     separator_edges[bit].second);
          }
        }
        add_edge(adjacency, 6, 7);
        for (int vertex = 0; vertex < 6; ++vertex) {
          if (status[vertex] != 1) {
            add_edge(adjacency, 6, vertex);
          }
          if (status[vertex] != 0) {
            add_edge(adjacency, 7, vertex);
          }
          add_edge(adjacency, 8, vertex);
        }

        ++checked[edge_count];
        if (!has_near_seven_minor(adjacency)) {
          std::cout << "COUNTEREXAMPLE eS=" << edge_count
                    << " separator_mask=" << separator_mask
                    << " status_code=" << status_code << '\n';
          return 1;
        }
        ++positive[edge_count];
      }
    }

    std::cout << "eS=" << edge_count
              << " checked=" << checked[edge_count]
              << " positive=" << positive[edge_count] << '\n';
  }

  std::array<std::uint16_t, 9> positive_control{};
  for (int left = 0; left < 7; ++left) {
    for (int right = left + 1; right < 7; ++right) {
      if (!(left == 0 && right == 1)) {
        add_edge(positive_control, left, right);
      }
    }
  }
  assert(has_near_seven_minor(positive_control));

  std::array<std::uint16_t, 9> negative_control{};
  for (int left = 0; left < 6; ++left) {
    for (int right = left + 1; right < 6; ++right) {
      add_edge(negative_control, left, right);
    }
  }
  assert(!has_near_seven_minor(negative_control));

  const long long total = checked[9] + checked[10] + checked[11];
  assert(total == 122941);
  std::cout << "partitions=" << partitions.size() << '\n';
  std::cout << "controls=PASS\n";
  std::cout << "total=" << total << '\n';
  return 0;
}
