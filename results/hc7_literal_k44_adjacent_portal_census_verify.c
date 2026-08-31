#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

/* Exact branch-partition census for K4,4 plus adjacent portal vertices c,d.
 * Vertices 0..3 and 4..7 are the shores; c=8,d=9.  Unused vertices are
 * allowed.  We classify all ordered attachment masks of size at least MINP.
 */

#ifndef MINP
#define MINP 4
#endif

typedef struct { uint16_t b[7]; } Partition;
static Partition *parts;
static int nparts, cap;

static int pc(unsigned x) { return __builtin_popcount(x); }

static void save_partition(uint16_t *b) {
    if (nparts == cap) {
        cap = cap ? 2 * cap : 16384;
        parts = realloc(parts, (size_t)cap * sizeof(*parts));
        if (!parts) abort();
    }
    for (int i = 0; i < 7; ++i) parts[nparts].b[i] = b[i];
    ++nparts;
}

static void setpart_rec(int v, int maxlab, int used_count, int need_used,
                        uint16_t *b) {
    if (v == 10) {
        if (used_count == need_used && maxlab == 6) save_partition(b);
        return;
    }
    if (used_count > need_used || used_count + 10 - v < need_used) return;
    /* unused */
    setpart_rec(v + 1, maxlab, used_count, need_used, b);
    int hi = maxlab + 1;
    if (hi > 6) hi = 6;
    for (int lab = 0; lab <= hi; ++lab) {
        b[lab] |= (uint16_t)(1u << v);
        setpart_rec(v + 1, lab > maxlab ? lab : maxlab,
                    used_count + 1, need_used, b);
        b[lab] ^= (uint16_t)(1u << v);
    }
}

static void generate_partitions(void) {
    uint16_t b[7] = {0};
    for (int k = 7; k <= 10; ++k) setpart_rec(0, -1, 0, k, b);
}

static int is_connected(uint16_t mask, const uint16_t *adj) {
    uint16_t seen = (uint16_t)(mask & (uint16_t)(-(int16_t)mask));
    uint16_t todo = seen;
    while (todo) {
        uint16_t bit = (uint16_t)(todo & (uint16_t)(-(int16_t)todo));
        todo ^= bit;
        int v = __builtin_ctz(bit);
        uint16_t add = (uint16_t)(adj[v] & mask & ~seen);
        seen |= add;
        todo |= add;
    }
    return seen == mask;
}

static int bags_contact(uint16_t x, uint16_t y, const uint16_t *adj) {
    while (x) {
        uint16_t bit = (uint16_t)(x & (uint16_t)(-(int16_t)x));
        x ^= bit;
        if (adj[__builtin_ctz(bit)] & y) return 1;
    }
    return 0;
}

static int has_target_extra(unsigned nc, unsigned nd, int extra_u, int extra_v) {
    uint16_t adj[10] = {0};
#define ADD(x,y) do { adj[(x)] |= (uint16_t)(1u << (y)); \
                      adj[(y)] |= (uint16_t)(1u << (x)); } while (0)
    for (int a = 0; a < 4; ++a) for (int b = 4; b < 8; ++b) ADD(a,b);
    ADD(8,9);
    if (extra_u >= 0) ADD(extra_u,extra_v);
    for (int v = 0; v < 8; ++v) {
        if ((nc >> v) & 1u) ADD(8,v);
        if ((nd >> v) & 1u) ADD(9,v);
    }
#undef ADD
    uint8_t conn[1024] = {0};
    for (int m = 1; m < 1024; ++m) conn[m] = (uint8_t)is_connected((uint16_t)m,adj);
    for (int z = 0; z < nparts; ++z) {
        const uint16_t *b = parts[z].b;
        int ok = 1;
        for (int i = 0; i < 7; ++i) if (!conn[b[i]]) { ok = 0; break; }
        if (!ok) continue;
        int edges = 0;
        for (int i = 0; i < 7; ++i) for (int j = i + 1; j < 7; ++j) {
            edges += bags_contact(b[i],b[j],adj);
            if (edges + (20 - (i * (13-i))/2) < 20) { /* harmless weak skip */ }
        }
        if (edges >= 20) return 1;
    }
    return 0;
}

static int has_target(unsigned nc, unsigned nd) {
    return has_target_extra(nc,nd,-1,-1);
}

static int special_five_negative(unsigned nc, unsigned nd) {
    if (pc(nc) != 5 || pc(nd) != 5) return 0;
    unsigned mc = 255u ^ nc, md = 255u ^ nd;
    unsigned common = mc & md;
    if (pc(common) != 1 || pc(mc) != 3 || pc(md) != 3) return 0;
    int z = __builtin_ctz(common);
    unsigned opposite = z < 4 ? 0xf0u : 0x0fu;
    return (mc | md) == (common | opposite);
}

int main(void) {
    generate_partitions();
    fprintf(stderr,"partitions=%d\n",nparts);
    int total = 0, negative = 0, special = 0, crossing_checks = 0;
    int hist[9][9] = {{0}};
    for (unsigned nc = 0; nc < 256; ++nc) if (pc(nc) >= MINP) {
        for (unsigned nd = 0; nd < 256; ++nd) if (pc(nd) >= MINP) {
            ++total;
            if (!has_target(nc,nd)) {
                ++negative;
                ++hist[pc(nc)][pc(nd)];
                printf("NEG %02x %02x miss %02x %02x\n",nc,nd,255u^nc,255u^nd);
                if (pc(nc) >= 5 && pc(nd) >= 5) {
                    if (!special_five_negative(nc,nd)) {
                        fprintf(stderr,"unexpected five-portal negative %02x %02x\n",nc,nd);
                        return 2;
                    }
                    ++special;
                    unsigned common = (255u ^ nc) & (255u ^ nd);
                    int z = __builtin_ctz(common);
                    unsigned opposite = z < 4 ? 0xf0u : 0x0fu;
                    unsigned left = (255u ^ nc) & opposite;
                    unsigned right = (255u ^ nd) & opposite;
                    for (int a = 0; a < 8; ++a) if ((left >> a) & 1u)
                        for (int b = 0; b < 8; ++b) if ((right >> b) & 1u) {
                            ++crossing_checks;
                            if (!has_target_extra(nc,nd,a,b)) {
                                fprintf(stderr,"crossing-edge failure %02x %02x %d %d\n",nc,nd,a,b);
                                return 3;
                            }
                        }
                }
            }
        }
    }
    fprintf(stderr,"total=%d negative=%d\n",total,negative);
    for (int i = MINP; i <= 8; ++i) for (int j = MINP; j <= 8; ++j)
        if (hist[i][j]) fprintf(stderr,"hist %d %d %d\n",i,j,hist[i][j]);
    fprintf(stderr,"special_five=%d crossing_edge_positive=%d\n",special,crossing_checks);
    if (MINP <= 5 && (special != 48 || crossing_checks != 192)) return 4;
    free(parts);
    return 0;
}
