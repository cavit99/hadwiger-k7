#include <assert.h>
#include <stdint.h>
#include <stdio.h>

/*
 * Exhaust the attachment masks used in the Wood--Woodall exceptional-core
 * decoder.  Bit i means adjacency to boundary root i.  A missing core pair
 * xy is covered when the root assigned at x sees y, or conversely.
 */

typedef struct {
    int u;
    int v;
} Pair;

static int masks_at_least_3[42];
static int masks_at_least_4[22];

static int popcount6(unsigned value) {
    int count = 0;
    while (value != 0) {
        count += (int)(value & 1U);
        value >>= 1;
    }
    return count;
}

static int carrier_violation(const int *mask, int n) {
    for (int z = 0; z < 64; ++z) {
        if (popcount6((unsigned)z) != 4) {
            continue;
        }
        int count = 0;
        for (int i = 0; i < n; ++i) {
            count += ((mask[i] & z) == z);
        }
        if (count >= 3) {
            return 1;
        }
    }
    return 0;
}

static int covered_pairs(const int *mask, const int *root,
                         const Pair *missing, int missing_count) {
    int covered = 0;
    for (int k = 0; k < missing_count; ++k) {
        int u = missing[k].u;
        int v = missing[k].v;
        covered += ((mask[v] >> root[u]) & 1) ||
                   ((mask[u] >> root[v]) & 1);
    }
    return covered;
}

static int five_bag_decoder(const int *mask, const Pair *missing,
                            int missing_count, int needed) {
    int root[5];
    for (root[0] = 0; root[0] < 6; ++root[0]) {
        if (!((mask[0] >> root[0]) & 1)) continue;
        for (root[1] = 0; root[1] < 6; ++root[1]) {
            if (root[1] == root[0] || !((mask[1] >> root[1]) & 1)) continue;
            for (root[2] = 0; root[2] < 6; ++root[2]) {
                if (root[2] == root[0] || root[2] == root[1] ||
                    !((mask[2] >> root[2]) & 1)) continue;
                for (root[3] = 0; root[3] < 6; ++root[3]) {
                    if (root[3] == root[0] || root[3] == root[1] ||
                        root[3] == root[2] ||
                        !((mask[3] >> root[3]) & 1)) continue;
                    for (root[4] = 0; root[4] < 6; ++root[4]) {
                        if (root[4] == root[0] || root[4] == root[1] ||
                            root[4] == root[2] || root[4] == root[3] ||
                            !((mask[4] >> root[4]) & 1)) continue;
                        if (covered_pairs(mask, root, missing, missing_count)
                            >= needed) {
                            return 1;
                        }
                    }
                }
            }
        }
    }
    return 0;
}

static int k4_plus_singleton_decoder(const int *mask) {
    for (int singleton_root = 0; singleton_root < 6; ++singleton_root) {
        int seen = 0;
        for (int i = 0; i < 4; ++i) {
            seen += (mask[i] >> singleton_root) & 1;
        }
        if (seen < 3) continue;

        for (int r0 = 0; r0 < 6; ++r0) {
            if (r0 == singleton_root || !((mask[0] >> r0) & 1)) continue;
            for (int r1 = 0; r1 < 6; ++r1) {
                if (r1 == singleton_root || r1 == r0 ||
                    !((mask[1] >> r1) & 1)) continue;
                for (int r2 = 0; r2 < 6; ++r2) {
                    if (r2 == singleton_root || r2 == r0 || r2 == r1 ||
                        !((mask[2] >> r2) & 1)) continue;
                    for (int r3 = 0; r3 < 6; ++r3) {
                        if (r3 == singleton_root || r3 == r0 || r3 == r1 ||
                            r3 == r2 || !((mask[3] >> r3) & 1)) continue;
                        return 1;
                    }
                }
            }
        }
    }
    return 0;
}

static void run_five_equal_masks(const char *name, const Pair *missing,
                                 int missing_count, int needed,
                                 uint64_t expected_bad) {
    uint64_t tested = 0;
    uint64_t bad = 0;
    uint64_t unexplained = 0;
    int mask[5];

    for (int i0 = 0; i0 < 22; ++i0)
    for (int i1 = 0; i1 < 22; ++i1)
    for (int i2 = 0; i2 < 22; ++i2)
    for (int i3 = 0; i3 < 22; ++i3)
    for (int i4 = 0; i4 < 22; ++i4) {
        mask[0] = masks_at_least_4[i0];
        mask[1] = masks_at_least_4[i1];
        mask[2] = masks_at_least_4[i2];
        mask[3] = masks_at_least_4[i3];
        mask[4] = masks_at_least_4[i4];
        ++tested;
        if (!five_bag_decoder(mask, missing, missing_count, needed)) {
            ++bad;
            unexplained += !carrier_violation(mask, 5);
        }
    }

    assert(tested == UINT64_C(5153632));
    assert(bad == expected_bad);
    assert(unexplained == 0);
    printf("%s tested=%llu decoder_failures=%llu carrier_admissible_failures=%llu\n",
           name, (unsigned long long)tested, (unsigned long long)bad,
           (unsigned long long)unexplained);
}

static void run_w4(void) {
    static const Pair missing[] = {{1, 3}, {2, 4}};
    uint64_t tested = 0;
    uint64_t bad = 0;
    uint64_t unexplained = 0;
    int mask[5];

    for (int ih = 0; ih < 42; ++ih)
    for (int i1 = 0; i1 < 22; ++i1)
    for (int i2 = 0; i2 < 22; ++i2)
    for (int i3 = 0; i3 < 22; ++i3)
    for (int i4 = 0; i4 < 22; ++i4) {
        mask[0] = masks_at_least_3[ih];
        mask[1] = masks_at_least_4[i1];
        mask[2] = masks_at_least_4[i2];
        mask[3] = masks_at_least_4[i3];
        mask[4] = masks_at_least_4[i4];
        ++tested;
        if (!five_bag_decoder(mask, missing, 2, 1)) {
            ++bad;
            unexplained += !carrier_violation(mask, 5);
        }
    }

    assert(tested == UINT64_C(9838752));
    assert(bad == UINT64_C(75));
    assert(unexplained == 0);
    printf("W4 tested=%llu decoder_failures=%llu carrier_admissible_failures=%llu\n",
           (unsigned long long)tested, (unsigned long long)bad,
           (unsigned long long)unexplained);
}

static void run_w3(void) {
    uint64_t tested = 0;
    uint64_t bad = 0;
    uint64_t unexplained = 0;
    int mask[4];

    for (int i0 = 0; i0 < 22; ++i0)
    for (int i1 = 0; i1 < 22; ++i1)
    for (int i2 = 0; i2 < 22; ++i2)
    for (int i3 = 0; i3 < 22; ++i3) {
        mask[0] = masks_at_least_4[i0];
        mask[1] = masks_at_least_4[i1];
        mask[2] = masks_at_least_4[i2];
        mask[3] = masks_at_least_4[i3];
        ++tested;
        if (!k4_plus_singleton_decoder(mask)) {
            ++bad;
            unexplained += !carrier_violation(mask, 4);
        }
    }

    assert(tested == UINT64_C(234256));
    assert(bad == UINT64_C(15));
    assert(unexplained == 0);
    printf("W3 tested=%llu decoder_failures=%llu carrier_admissible_failures=%llu\n",
           (unsigned long long)tested, (unsigned long long)bad,
           (unsigned long long)unexplained);
}

int main(void) {
    int n3 = 0;
    int n4 = 0;
    for (int mask = 0; mask < 64; ++mask) {
        int size = popcount6((unsigned)mask);
        if (size >= 3) masks_at_least_3[n3++] = mask;
        if (size >= 4) masks_at_least_4[n4++] = mask;
    }
    assert(n3 == 42);
    assert(n4 == 22);

    static const Pair long_wheel_missing[] = {{1, 3}, {1, 4}, {2, 4}};
    static const Pair prism_missing[] = {{0, 1}, {1, 2}, {2, 3}, {3, 4}};
    static const Pair k33_missing[] = {{0, 1}, {0, 2}, {1, 2}, {3, 4}};

    run_w3();
    run_w4();
    run_five_equal_masks("long-wheel", long_wheel_missing, 3, 2,
                         UINT64_C(15));
    run_five_equal_masks("prism", prism_missing, 4, 3, UINT64_C(15));
    run_five_equal_masks("K33", k33_missing, 4, 3, UINT64_C(15));
    return 0;
}
