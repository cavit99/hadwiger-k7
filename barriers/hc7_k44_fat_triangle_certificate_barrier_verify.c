/*
 * Exact spanning-partition minor screen for K_{4,4} plus a fat triangle.
 *
 * Vertices 0..3 are A, 4..7 are B.  For each of p01,p12,p20,
 * add that many internally disjoint length-two paths between the named A
 * vertices.  Since the graph is connected, every minor model can be made
 * spanning by absorbing unused components.  A spanning seven-bag model has
 * a spanning forest with n-7 edges; hence enumerating all such edge subsets
 * is complete.  We report the first quotient with at least 20 of 21 edges.
 */

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct { int x, y; } Edge;

static int parent_[32], rank_[32];

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
    if (rank_[x] < rank_[y]) { int t=x; x=y; y=t; }
    parent_[y] = x;
    if (rank_[x] == rank_[y]) rank_[x]++;
    return 1;
}

static Edge edges[64];
static int m, n, need, pick[32];
static unsigned long long checked;
static int best_qedges=-1, best_labels[32], best_pick[32];

static void evaluate(void) {
    int i, j, comps, labels[32], roots[32], qedges = 0;
    uint64_t qmask = 0;
    for (i=0; i<n; i++) { parent_[i]=i; rank_[i]=0; }
    for (i=0; i<need; i++) {
        if (!unite_(edges[pick[i]].x, edges[pick[i]].y)) return;
    }
    comps=0;
    for (i=0; i<n; i++) {
        int r=find_(i), lab=-1;
        for (j=0; j<comps; j++) if (roots[j]==r) { lab=j; break; }
        if (lab<0) { roots[comps]=r; lab=comps++; }
        labels[i]=lab;
    }
    if (comps != 7) return;
    checked++;
    for (i=0; i<m; i++) {
        int a=labels[edges[i].x], b=labels[edges[i].y];
        int lo, hi, bit;
        if (a==b) continue;
        lo = a<b ? a:b; hi = a<b ? b:a;
        bit = lo*7 - lo*(lo+1)/2 + (hi-lo-1);
        qmask |= UINT64_C(1) << bit;
    }
    qedges=__builtin_popcountll(qmask);
    if (qedges > best_qedges) {
        best_qedges=qedges;
        for (i=0;i<n;i++) best_labels[i]=labels[i];
        for (i=0;i<need;i++) best_pick[i]=pick[i];
    }
    if (qedges >= 20) {
        printf("TARGET n=%d m=%d quotient_edges=%d checked=%llu\n", n,m,qedges,checked);
        for (i=0; i<7; i++) {
            printf("bag%d", i);
            for (j=0; j<n; j++) if (labels[j]==i) printf(" %d",j);
            putchar('\n');
        }
        printf("forest");
        for (i=0; i<need; i++) printf(" (%d,%d)",edges[pick[i]].x,edges[pick[i]].y);
        putchar('\n');
        exit(0);
    }
}

static void rec(int pos, int start) {
    int e;
    if (pos==need) { evaluate(); return; }
    for (e=start; e<=m-(need-pos); e++) {
        pick[pos]=e;
        rec(pos+1,e+1);
    }
}

static void add(int x, int y) { edges[m++]=(Edge){x,y}; }

int main(int argc, char **argv) {
    int p[3]={3,2,2}, pair[3][2]={{0,1},{1,2},{2,0}}, t, k;
    if (argc==4) for (t=0;t<3;t++) p[t]=atoi(argv[t+1]);
    m=0; n=8;
    for (int a=0;a<4;a++) for (int b=4;b<8;b++) add(a,b);
    for (t=0;t<3;t++) for (k=0;k<p[t];k++) {
        int z=n++;
        add(pair[t][0],z); add(z,pair[t][1]);
    }
    need=n-7;
    if (need<0 || need>31) return 2;
    printf("SCREEN profile=%d,%d,%d n=%d m=%d choose=%d\n",p[0],p[1],p[2],n,m,need);
    rec(0,0);
    printf("NO_TARGET checked=%llu best=%d\n",checked,best_qedges);
    for (int i=0;i<7;i++) {
        printf("bestbag%d",i);
        for (int j=0;j<n;j++) if (best_labels[j]==i) printf(" %d",j);
        putchar('\n');
    }
    printf("bestforest");
    for (int i=0;i<need;i++)
        printf(" (%d,%d)",edges[best_pick[i]].x,edges[best_pick[i]].y);
    putchar('\n');
    return 1;
}
