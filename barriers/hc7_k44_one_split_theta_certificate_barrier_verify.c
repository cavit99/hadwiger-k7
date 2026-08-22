/* Exact K7-minus screen for one split K4,4 vertex plus q x-y paths. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct { int x,y; } Edge;
static Edge e[80]; static int m,n,need,pick[40],par[40],rk[40];
static unsigned long long checked; static int best=-1,bestlab[40];
static int f(int x){while(par[x]!=x){par[x]=par[par[x]];x=par[x];}return x;}
static int u(int x,int y){x=f(x);y=f(y);if(x==y)return 0;if(rk[x]<rk[y]){int t=x;x=y;y=t;}par[y]=x;if(rk[x]==rk[y])rk[x]++;return 1;}
static void add(int x,int y){e[m++]=(Edge){x,y};}
static void eval(void){
 int i,j,c=0,roots[40],lab[40]; uint64_t qm=0;
 for(i=0;i<n;i++){par[i]=i;rk[i]=0;}
 for(i=0;i<need;i++)if(!u(e[pick[i]].x,e[pick[i]].y))return;
 for(i=0;i<n;i++){int r=f(i),z=-1;for(j=0;j<c;j++)if(roots[j]==r){z=j;break;}if(z<0){roots[c]=r;z=c++;}lab[i]=z;}
 if(c!=7)return; checked++;
 for(i=0;i<m;i++){int a=lab[e[i].x],b=lab[e[i].y],lo,hi,bit;if(a==b)continue;lo=a<b?a:b;hi=a<b?b:a;bit=lo*7-lo*(lo+1)/2+(hi-lo-1);qm|=UINT64_C(1)<<bit;}
 int q=__builtin_popcountll(qm);if(q>best){best=q;for(i=0;i<n;i++)bestlab[i]=lab[i];}
 if(q>=20){printf("TARGET n=%d m=%d checked=%llu q=%d\n",n,m,checked,q);for(i=0;i<7;i++){printf("bag%d",i);for(j=0;j<n;j++)if(lab[j]==i)printf(" %d",j);putchar('\n');}exit(0);}
}
static void rec(int pos,int start){if(pos==need){eval();return;}for(int z=start;z<=m-(need-pos);z++){pick[pos]=z;rec(pos+1,z+1);}}
int main(int ac,char**av){
 int left=2,q=6;if(ac>1)left=atoi(av[1]);if(ac>2)q=atoi(av[2]);
 /* x=0, A1..A3=1..3, B=4..7, y=8. */
 n=9;m=0;for(int a=1;a<4;a++)for(int b=4;b<8;b++)add(a,b);add(0,8);
 for(int b=4;b<8;b++)add(b,b<4+left?0:8);
 for(int k=0;k<q;k++){int z=n++;add(0,z);add(z,8);}
 need=n-7;printf("SCREEN split=%d+%d theta=%d n=%d m=%d choose=%d\n",left,4-left,q,n,m,need);rec(0,0);
 printf("NO_TARGET checked=%llu best=%d\n",checked,best);for(int i=0;i<7;i++){printf("bestbag%d",i);for(int j=0;j<n;j++)if(bestlab[j]==i)printf(" %d",j);putchar('\n');}return 1;
}
