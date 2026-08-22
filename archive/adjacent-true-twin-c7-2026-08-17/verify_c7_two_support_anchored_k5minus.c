/* Exhaustive verifier for the finite C7 anchoring lemma.

   X and Y are disjoint connected adjacent exterior bags.  U and V are
   their respective supports on a literal C7.  For every |U|,|V| >= 5,
   search for five disjoint connected T-hitting bags X',Y',A,B,C whose
   contact graph has at least nine of ten edges.  Vertices of C7 may be
   unused.  A cycle vertex assigned to X' (respectively Y') is required to
   lie in U (respectively V), so adjoining it preserves connectivity.

   This verifier is deliberately independent of any host-minor solver: it
   checks exactly the displayed five-bag construction.
*/

#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

enum { NX = 7, LABELS = 5, UNUSED = 5 };

static int pop7(unsigned x) { return __builtin_popcount(x & 127u); }

static int cycle_connected(unsigned mask) {
    if (!mask) return 0;
    unsigned seen = mask & -mask;
    unsigned todo = seen;
    while (todo) {
        unsigned bit = todo & -todo;
        todo ^= bit;
        int v = __builtin_ctz(bit);
        unsigned nb = (1u << ((v + 1) % 7)) | (1u << ((v + 6) % 7));
        unsigned add = nb & mask & ~seen;
        seen |= add;
        todo |= add;
    }
    return seen == mask;
}

static int assignment_works(unsigned U, unsigned V, const int lab[7]) {
    unsigned bags[5] = {0,0,0,0,0};
    for (int t = 0; t < 7; ++t)
        if (lab[t] < 5) bags[lab[t]] |= 1u << t;
    for (int i = 0; i < 5; ++i) if (!bags[i]) return 0;
    if (bags[0] & ~U) return 0;
    if (bags[1] & ~V) return 0;
    for (int i = 2; i < 5; ++i)
        if (!cycle_connected(bags[i])) return 0;

    int contacts = 0;
    for (int i = 0; i < 5; ++i) for (int j = i + 1; j < 5; ++j) {
        int hit = (i == 0 && j == 1); /* literal X--Y exterior edge */
        if (!hit && i == 0 && (bags[j] & U)) hit = 1;
        if (!hit && i == 1 && (bags[j] & V)) hit = 1;
        if (!hit && j == 0 && (bags[i] & U)) hit = 1;
        if (!hit && j == 1 && (bags[i] & V)) hit = 1;
        for (int t = 0; !hit && t < 7; ++t) if (bags[i] >> t & 1u) {
            int p = (t + 6) % 7, q = (t + 1) % 7;
            if ((bags[j] >> p & 1u) || (bags[j] >> q & 1u)) hit = 1;
        }
        contacts += hit;
    }
    return contacts >= 9;
}

static int find_assignment(unsigned U, unsigned V) {
    int lab[7];
    uint64_t total = 1;
    for (int i = 0; i < 7; ++i) total *= 6;
    for (uint64_t code = 0; code < total; ++code) {
        uint64_t q = code;
        for (int t = 0; t < 7; ++t) { lab[t] = q % 6; q /= 6; }
        if (assignment_works(U, V, lab)) return 1;
    }
    return 0;
}

int main(int argc, char **argv) {
    int minimum = argc >= 2 ? atoi(argv[1]) : 5;
    int print_all = argc >= 3 ? atoi(argv[2]) : 0;
    int require_full_union = argc >= 4 ? atoi(argv[3]) : 0;
    if (minimum < 0 || minimum > 7) return 2;
    int pairs = 0, failures = 0;
    for (unsigned U = 0; U < 128; ++U) if (pop7(U) >= minimum)
        for (unsigned V = 0; V < 128; ++V) if (pop7(V) >= minimum) {
            if (require_full_union && (U | V) != 127u) continue;
            ++pairs;
            if (!find_assignment(U, V)) {
                ++failures;
                if (failures <= 30 || print_all)
                    printf("FAIL U=%u V=%u\n", U, V);
            }
        }
    if (minimum == 5 && !require_full_union) assert(pairs == 29 * 29);
    printf("%s support_pairs=%d failures=%d minimum=%d full_union=%d\n",
           failures ? "NEGATIVE" : "GREEN", pairs, failures, minimum,
           require_full_union);
    return failures != 0;
}
