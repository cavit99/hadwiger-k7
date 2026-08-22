#include <stdint.h>

/* Exact K_7^- minor checker for connected graphs on eleven vertices.

   A minor model can be made spanning by absorbing each unused component
   into an adjacent branch set.  A spanning seven-bag model has a spanning
   forest of four graph edges.  We enumerate all four-edge subsets, retain
   precisely forests, and inspect their seven-vertex quotient. */

static int parent_[11];
static unsigned char rank_[11];

static int find_(int x) {
    while (parent_[x] != x) {
        parent_[x] = parent_[parent_[x]];
        x = parent_[x];
    }
    return x;
}

static int unite_(int x, int y) {
    x = find_(x); y = find_(y);
    if (x == y) return 0;
    if (rank_[x] < rank_[y]) { int t = x; x = y; y = t; }
    parent_[y] = x;
    if (rank_[x] == rank_[y]) ++rank_[x];
    return 1;
}

int has_k7minus11(const uint16_t *adj, unsigned char *certificate) {
    unsigned char eu[55], ev[55];
    int m = 0;
    for (int u = 0; u < 11; ++u) {
        for (int v = u + 1; v < 11; ++v) {
            if ((adj[u] >> v) & 1u) {
                eu[m] = (unsigned char)u;
                ev[m] = (unsigned char)v;
                ++m;
            }
        }
    }

    for (int a = 0; a < m - 3; ++a)
    for (int b = a + 1; b < m - 2; ++b)
    for (int c = b + 1; c < m - 1; ++c)
    for (int d = c + 1; d < m; ++d) {
        for (int v = 0; v < 11; ++v) {
            parent_[v] = v;
            rank_[v] = 0;
        }
        if (!unite_(eu[a], ev[a]) || !unite_(eu[b], ev[b]) ||
            !unite_(eu[c], ev[c]) || !unite_(eu[d], ev[d])) continue;

        int root[7], labels[11], bags = 0;
        for (int v = 0; v < 11; ++v) {
            int r = find_(v), label = -1;
            for (int i = 0; i < bags; ++i) {
                if (root[i] == r) { label = i; break; }
            }
            if (label < 0) { root[bags] = r; label = bags++; }
            labels[v] = label;
        }
        if (bags != 7) continue;

        uint32_t quotient = 0;
        for (int u = 0; u < 11; ++u) {
            int lu = labels[u];
            for (int v = u + 1; v < 11; ++v) {
                if (!((adj[u] >> v) & 1u)) continue;
                int lv = labels[v];
                if (lu == lv) continue;
                int lo = lu < lv ? lu : lv;
                int hi = lu < lv ? lv : lu;
                int bit = lo * 7 - lo * (lo + 1) / 2 + (hi - lo - 1);
                quotient |= UINT32_C(1) << bit;
            }
        }
        if (__builtin_popcount(quotient) >= 20) {
            if (certificate) {
                for (int v = 0; v < 11; ++v)
                    certificate[v] = (unsigned char)labels[v];
            }
            return 1;
        }
    }
    return 0;
}
