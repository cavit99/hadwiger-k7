#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using Graph = std::array<uint16_t, 12>;

static Graph parse(const std::string& code) {
    Graph graph{};
    int character = 1;
    int bit = 5;
    for (int right = 1; right < 8; ++right) {
        for (int left = 0; left < right; ++left) {
            const int value = static_cast<unsigned char>(code[character]) - 63;
            if ((value >> bit) & 1) {
                graph[left] |= uint16_t{1} << right;
                graph[right] |= uint16_t{1} << left;
            }
            if (--bit < 0) {
                bit = 5;
                ++character;
            }
        }
    }
    return graph;
}

static void add_edge(Graph& graph, int left, int right) {
    graph[left] |= uint16_t{1} << right;
    graph[right] |= uint16_t{1} << left;
}

static bool connected(uint16_t set, const Graph& graph) {
    if (!set) return false;
    uint16_t seen = set & -set;
    uint16_t todo = seen;
    while (todo) {
        const int vertex = __builtin_ctz(todo);
        todo &= todo - 1;
        const uint16_t add = graph[vertex] & set & ~seen;
        seen |= add;
        todo |= add;
    }
    return seen == set;
}

static bool touch(uint16_t left, uint16_t right, const Graph& graph) {
    while (left) {
        const int vertex = __builtin_ctz(left);
        left &= left - 1;
        if (graph[vertex] & right) return true;
    }
    return false;
}

static bool target(const Graph& graph) {
    std::array<uint16_t, 7> bags{};
    auto search = [&](auto&& self, int vertex, int used) -> bool {
        if (vertex == 12) {
            if (used != 7) return false;
            for (const uint16_t bag : bags) if (!connected(bag, graph)) return false;
            int misses = 0;
            for (int left = 0; left < 7; ++left) {
                for (int right = left + 1; right < 7; ++right) {
                    if (!touch(bags[left], bags[right], graph) && ++misses > 1) return false;
                }
            }
            return true;
        }
        if (self(self, vertex + 1, used)) return true;
        for (int index = 0; index < used; ++index) {
            bags[index] |= uint16_t{1} << vertex;
            if (self(self, vertex + 1, used)) return true;
            bags[index] &= ~(uint16_t{1} << vertex);
        }
        if (used < 7) {
            bags[used] |= uint16_t{1} << vertex;
            if (self(self, vertex + 1, used + 1)) return true;
            bags[used] &= ~(uint16_t{1} << vertex);
        }
        return false;
    };
    return search(search, 0, 0);
}

int main() {
    const std::vector<std::string> codes = {
        "GCOcaO", "GCOcbO", "GCOcbW", "GCOe`W", "GCOebW", "GCQQV?", "GCQR@O"
    };
    for (const std::string& code : codes) {
        const Graph boundary = parse(code);
        long failures = 0;
        std::pair<int, int> example{-1, -1};
        for (int first = 0; first < 256; ++first) {
            if (__builtin_popcount(static_cast<unsigned>(first)) < 6) continue;
            for (int second = 0; second < 256; ++second) {
                if (__builtin_popcount(static_cast<unsigned>(second)) < 6) continue;
                Graph graph = boundary;
                for (int vertex = 0; vertex < 8; ++vertex) {
                    add_edge(graph, 8, vertex);
                    add_edge(graph, 9, vertex);
                    if ((first >> vertex) & 1) add_edge(graph, 10, vertex);
                    if ((second >> vertex) & 1) add_edge(graph, 11, vertex);
                }
                add_edge(graph, 10, 11);
                if (!target(graph)) {
                    ++failures;
                    if (example.first < 0) example = {first, second};
                }
            }
        }
        std::cout << code << " failures=" << failures;
        if (failures) std::cout << " example=" << std::hex << example.first << ',' << example.second << std::dec;
        std::cout << '\n';
    }
}
