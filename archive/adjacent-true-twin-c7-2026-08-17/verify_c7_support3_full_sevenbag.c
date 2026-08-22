/* Exact screen for a flexible seven-bag construction at a C7 twin seam.

   Fixed underlying bags are A={a}, B={b}, X and Y, where a,b are
   adjacent twins complete to C7 and anticomplete to the adjacent connected
   exterior bags X,Y.  U=N_C7(X), V=N_C7(Y).  Each cycle vertex may be
   absorbed into A,B,X,Y, one of three connected cycle-only bags I,J,K,
   or left unused.  Absorption into X (Y) is allowed only from U (V).
   The program asks whether the resulting seven bags have at least 20 of
   21 contacts.  It checks all ordered |U|,|V|>=3 with U union V=C7.
*/

#include <stdint.h>
#include <stdio.h>
#include <string.h>

enum { N = 7, ALL = 127, LABS = 8 };

static int pop7(unsigned x) { return __builtin_popcount(x & ALL); }

static int connected_c7(unsigned mask) {
  if (!mask) return 0;
  unsigned seen = mask & -mask, todo = seen;
  while (todo) {
    unsigned bit = todo & -todo;
    todo ^= bit;
    int v = __builtin_ctz(bit);
    unsigned nb = (1u << ((v + 1) % N)) | (1u << ((v + N - 1) % N));
    unsigned add = nb & mask & ~seen;
    seen |= add;
    todo |= add;
  }
  return seen == mask;
}

static int cycle_contact(unsigned p, unsigned q) {
  unsigned nb = ((p << 1) | (p >> 6) | (p >> 1) | (p << 6)) & ALL;
  return (nb & q) != 0;
}

/* Labels: 0=A,1=B,2=X,3=Y,4=I,5=J,6=K,7=unused. */
static int contact_score(unsigned U, unsigned V, const unsigned bag[7]) {
  if ((bag[2] & ~U) || (bag[3] & ~V)) return -1;
  for (int i = 4; i < 7; ++i) if (!connected_c7(bag[i])) return -1;

  int edges = 0;
  for (int i = 0; i < 7; ++i) for (int j = i + 1; j < 7; ++j) {
    int hit = 0;
    if (i == 0 && j == 1) hit = 1;             /* ab */
    if (i == 2 && j == 3) hit = 1;             /* X--Y */
    if ((i <= 1 || j <= 1) && (bag[i] || bag[j])) {
      /* A or B sees every cycle vertex placed in the other bag. */
      int twin = (i <= 1) ? i : j;
      int other = (i <= 1) ? j : i;
      if (bag[other]) hit = 1;
      /* A/B can instead use one of its own supported anchors to meet X/Y. */
      if (!hit && other == 2 && (bag[twin] & U)) hit = 1;
      if (!hit && other == 3 && (bag[twin] & V)) hit = 1;
    }
    if (!hit && cycle_contact(bag[i],bag[j])) hit = 1;
    /* Underlying X or Y sees supported vertices in the other bag. */
    if (!hit && i == 2 && (bag[j] & U)) hit = 1;
    if (!hit && j == 2 && (bag[i] & U)) hit = 1;
    if (!hit && i == 3 && (bag[j] & V)) hit = 1;
    if (!hit && j == 3 && (bag[i] & V)) hit = 1;
    edges += hit;
  }
  return edges;
}

static int solve(unsigned U, unsigned V, unsigned witness[7], int *best) {
  uint64_t total = 1;
  *best = -1;
  for (int i = 0; i < N; ++i) total *= LABS;
  for (uint64_t code = 0; code < total; ++code) {
    uint64_t q = code;
    unsigned bag[7] = {0,0,0,0,0,0,0};
    for (int t = 0; t < N; ++t) {
      int lab = q & 7u;
      q >>= 3;
      if (lab < 7) bag[lab] |= 1u << t;
    }
    int score = contact_score(U,V,bag);
    if (score > *best) *best = score;
    if (score >= 20) {
      memcpy(witness,bag,7*sizeof(unsigned));
      return 1;
    }
  }
  return 0;
}

static void print_set(unsigned x) {
  putchar('{');
  int first=1;
  for (int i=0;i<7;++i) if ((x>>i)&1u) {
    if (!first) putchar(',');
    printf("%d",i); first=0;
  }
  putchar('}');
}

int main(void) {
  int pairs=0, failures=0;
  for (unsigned U=0;U<128;++U) if (pop7(U)>=3)
    for (unsigned V=0;V<128;++V) if (pop7(V)>=3 && (U|V)==ALL) {
      ++pairs;
      unsigned w[7];
      int best;
      if (!solve(U,V,w,&best)) {
        ++failures;
        printf("FAIL U="); print_set(U); printf(" V="); print_set(V);
        printf(" max_contacts=%d\n",best);
      }
    }
  printf("union_full_support_pairs=%d failures=%d\n",pairs,failures);
  return failures != 0;
}
