/* Exhaustive labelled cross-check for the seven-vertex factor lemma.

   This verifier is not used to infer the unbounded host theorem.  It checks
   all 2^21 labelled graphs on seven vertices and confirms that every
   triangle-free graph with independence number at most three is either a
   literal C7 or has a spanning C5 plus disjoint edge.
*/

#include <stdint.h>
#include <stdio.h>

static int bit_index[7][7];

static uint32_t edge_bit(int a, int b) {
    if (a > b) { int t = a; a = b; b = t; }
    return UINT32_C(1) << bit_index[a][b];
}

static int has_triangle(uint32_t g) {
    for (int a = 0; a < 7; ++a)
        for (int b = a + 1; b < 7; ++b)
            for (int c = b + 1; c < 7; ++c) {
                uint32_t q = edge_bit(a,b) | edge_bit(a,c) | edge_bit(b,c);
                if ((g & q) == q) return 1;
            }
    return 0;
}

static int has_independent_four(uint32_t g) {
    for (int a = 0; a < 7; ++a)
        for (int b = a + 1; b < 7; ++b)
            for (int c = b + 1; c < 7; ++c)
                for (int d = c + 1; d < 7; ++d) {
                    int v[4] = {a,b,c,d};
                    uint32_t q = 0;
                    for (int i = 0; i < 4; ++i)
                        for (int j = i + 1; j < 4; ++j)
                            q |= edge_bit(v[i],v[j]);
                    if ((g & q) == 0) return 1;
                }
    return 0;
}

static int next_permutation(int *a, int n) {
    int i = n - 2;
    while (i >= 0 && a[i] >= a[i+1]) --i;
    if (i < 0) return 0;
    int j = n - 1;
    while (a[j] <= a[i]) --j;
    int t = a[i]; a[i] = a[j]; a[j] = t;
    for (int l = i + 1, r = n - 1; l < r; ++l, --r) {
        t = a[l]; a[l] = a[r]; a[r] = t;
    }
    return 1;
}

static int is_c7(uint32_t g) {
    if (__builtin_popcount(g) != 7) return 0;
    int degree[7] = {0};
    for (int a = 0; a < 7; ++a)
        for (int b = a + 1; b < 7; ++b)
            if (g & edge_bit(a,b)) { ++degree[a]; ++degree[b]; }
    for (int v = 0; v < 7; ++v) if (degree[v] != 2) return 0;
    return 1; /* a finite 2-regular graph on odd order 7 cannot be C3+C4 here */
}

static int has_c5_edge_factor(uint32_t g) {
    /* Choose the leftover edge x-y, then test all cyclic orders of the five
       remaining vertices with their least label fixed first. */
    for (int x = 0; x < 7; ++x) for (int y = x + 1; y < 7; ++y) {
        if (!(g & edge_bit(x,y))) continue;
        int p[5], k = 0;
        for (int v = 0; v < 7; ++v) if (v != x && v != y) p[k++] = v;
        int first = p[0];
        int tail[4] = {p[1],p[2],p[3],p[4]};
        do {
            int q[5] = {first,tail[0],tail[1],tail[2],tail[3]};
            int ok = 1;
            for (int i = 0; i < 5; ++i)
                if (!(g & edge_bit(q[i],q[(i+1)%5]))) { ok = 0; break; }
            if (ok) return 1;
        } while (next_permutation(tail,4));
    }
    return 0;
}

int main(void) {
    int k = 0;
    for (int a = 0; a < 7; ++a)
        for (int b = a + 1; b < 7; ++b)
            bit_index[a][b] = k++;

    uint64_t qualifying = 0, factored = 0, pure_c7 = 0, failures = 0;
    for (uint32_t g = 0; g < (UINT32_C(1) << 21); ++g) {
        if (has_triangle(g) || has_independent_four(g)) continue;
        ++qualifying;
        if (has_c5_edge_factor(g)) ++factored;
        else if (is_c7(g)) ++pure_c7;
        else {
            ++failures;
            if (failures <= 10) printf("failure mask=0x%06x\n",g);
        }
    }
    printf("qualifying=%llu factored=%llu pure_c7=%llu failures=%llu\n",
           (unsigned long long)qualifying,
           (unsigned long long)factored,
           (unsigned long long)pure_c7,
           (unsigned long long)failures);
    if (failures) return 1;
    puts("GREEN seven-vertex triangle-free alpha<=3 factor lemma");
    return 0;
}
