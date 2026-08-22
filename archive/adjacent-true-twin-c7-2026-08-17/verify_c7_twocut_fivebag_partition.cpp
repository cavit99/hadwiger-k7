#include <array>
#include <cstdint>
#include <iostream>

// Exhaust the finite boundary assertion used in the pure-C7 two-cut lift.
// A,B are supports of two components and have size at least five.  Labels
// 0,1 are exterior bags whose assigned cycle vertices must lie in A,B;
// labels 2,3,4 must induce connected nonempty C7 intervals.  Bags 0,1 are
// declared adjacent through the two cut vertices.  Support contacts and
// literal cycle edges must give at least nine of ten bag contacts.

static bool connected_c7(int mask) {
  if (!mask) return false;
  int seen = mask & -mask;
  while (true) {
    int next = seen;
    for (int v = 0; v < 7; ++v)
      if ((seen >> v) & 1) {
        int a = (v + 1) % 7, b = (v + 6) % 7;
        if ((mask >> a) & 1) next |= 1 << a;
        if ((mask >> b) & 1) next |= 1 << b;
      }
    if (next == seen) return seen == mask;
    seen = next;
  }
}

static bool solve(int A, int B, std::array<int, 5>* witness) {
  int total = 1;
  for (int i = 0; i < 7; ++i) total *= 5;
  for (int code = 0; code < total; ++code) {
    int x = code;
    std::array<int, 5> bags{};
    for (int v = 0; v < 7; ++v) {
      int label = x % 5;
      x /= 5;
      bags[label] |= 1 << v;
    }
    bool nonempty = true;
    for (int i = 0; i < 5; ++i) nonempty &= bags[i] != 0;
    if (!nonempty || (bags[0] & ~A) || (bags[1] & ~B)) continue;
    if (!connected_c7(bags[2]) || !connected_c7(bags[3]) ||
        !connected_c7(bags[4])) continue;

    int edges = 1;  // exterior bags 0 and 1 are adjacent through the cut.
    for (int i = 0; i < 5; ++i) {
      for (int j = i + 1; j < 5; ++j) {
        if (i == 0 && j == 1) continue;
        bool hit = false;
        for (int u = 0; u < 7; ++u)
          if ((bags[i] >> u) & 1)
            for (int v = 0; v < 7; ++v)
              if ((bags[j] >> v) & 1)
                if ((u - v + 7) % 7 == 1 || (v - u + 7) % 7 == 1)
                  hit = true;
        if (i == 0 && (bags[j] & A)) hit = true;
        if (j == 0 && (bags[i] & A)) hit = true;
        if (i == 1 && (bags[j] & B)) hit = true;
        if (j == 1 && (bags[i] & B)) hit = true;
        edges += hit;
      }
    }
    if (edges >= 9) {
      *witness = bags;
      return true;
    }
  }
  return false;
}

int main() {
  int pairs = 0, failures = 0;
  for (int A = 0; A < 128; ++A) {
    if (__builtin_popcount(A) < 5) continue;
    for (int B = 0; B < 128; ++B) {
      if (__builtin_popcount(B) < 5) continue;
      ++pairs;
      std::array<int, 5> witness{};
      if (!solve(A, B, &witness)) {
        ++failures;
        std::cout << "FAIL A=" << A << " B=" << B << "\n";
      }
    }
  }
  std::cout << "support_pairs " << pairs << " failures " << failures
            << "\n";
  return failures != 0;
}
