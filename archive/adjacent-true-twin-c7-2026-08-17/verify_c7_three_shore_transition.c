/* Exact screen for the three-shore st-transition construction on C7.

   Underlying bags: adjacent twins A,B and connected exterior bags L,M,R
   with guaranteed edges L--M, M--R, and L--R.  Their C7 supports are
   LS,MS,RS.  The third edge follows in the intended application because
   D-M is connected and L,R partition it into two connected sets.
   Each cycle vertex may be absorbed into A,B,L,M,R, either of two
   connected cycle-only bags I,J, or be unused.  We require >=20/21
   contacts in the resulting seven-bag quotient.

   The screened transition profiles are the abstract consequences of a
   first prefix whose support reaches four in an st-order:
     |LS| <= 3, |LS union MS| >= 4, LS union RS = C7;
   MS is a target-free one-vertex portal profile (size <=2 or a
   consecutive triple).  The last equality follows because a cycle vertex
   outside LS union RS would have all its D-neighbours at M, contradicting
   d_D(t)>=4.  No claim is made here that these are all host constraints.
*/

#include <stdint.h>
#include <stdio.h>
#include <string.h>

enum { N=7, ALL=127, LABS=8 };

static int pop7(unsigned x){ return __builtin_popcount(x&ALL); }

static int connected_c7(unsigned x){
  if(!x) return 0;
  unsigned seen=x&-x,todo=seen;
  while(todo){
    unsigned bit=todo&-todo; todo^=bit;
    int v=__builtin_ctz(bit);
    unsigned nb=(1u<<((v+1)%7))|(1u<<((v+6)%7));
    unsigned add=nb&x&~seen; seen|=add; todo|=add;
  }
  return seen==x;
}

static int cycle_contact(unsigned p,unsigned q){
  unsigned nb=((p<<1)|(p>>6)|(p>>1)|(p<<6))&ALL;
  return (nb&q)!=0;
}

static int consecutive_triple(unsigned x){
  for(int i=0;i<7;++i)
    if(x==((1u<<i)|(1u<<((i+1)%7))|(1u<<((i+2)%7)))) return 1;
  return 0;
}

static int local_profile(unsigned x){ return pop7(x)<=2 || consecutive_triple(x); }

/* labels 0=A,1=B,2=L,3=M,4=R,5=I,6=J,7=unused */
static int works(unsigned LS,unsigned MS,unsigned RS,const unsigned bag[7]){
  if((bag[2]&~LS)||(bag[3]&~MS)||(bag[4]&~RS)) return 0;
  if(!connected_c7(bag[5])||!connected_c7(bag[6])) return 0;
  unsigned supp[7]={0,0,LS,MS,RS,0,0};
  int edges=0;
  for(int i=0;i<7;++i) for(int j=i+1;j<7;++j){
    int hit=(i==0&&j==1)||(i==2&&j==3)||(i==3&&j==4)||
            (i==2&&j==4);
    if(!hit&&(i<=1||j<=1)){
      int twin=(i<=1)?i:j, other=(i<=1)?j:i;
      if(bag[other]) hit=1; /* twin sees cycle vertex in other bag */
      if(!hit&&other>=2&&other<=4&&(bag[twin]&supp[other])) hit=1;
    }
    if(!hit&&cycle_contact(bag[i],bag[j])) hit=1;
    if(!hit&&i>=2&&i<=4&&(bag[j]&supp[i])) hit=1;
    if(!hit&&j>=2&&j<=4&&(bag[i]&supp[j])) hit=1;
    edges+=hit;
  }
  return edges>=20;
}

static int solve(unsigned LS,unsigned MS,unsigned RS,unsigned out[7]){
  uint64_t total=1;
  for(int i=0;i<7;++i) total*=8;
  for(uint64_t code=0;code<total;++code){
    uint64_t q=code; unsigned bag[7]={0,0,0,0,0,0,0};
    for(int t=0;t<7;++t){ int lab=q&7u; q>>=3; if(lab<7) bag[lab]|=1u<<t; }
    if(works(LS,MS,RS,bag)){ memcpy(out,bag,7*sizeof(unsigned)); return 1; }
  }
  return 0;
}

static void pset(unsigned x){
  putchar('{'); int first=1;
  for(int i=0;i<7;++i)if((x>>i)&1u){if(!first)putchar(',');printf("%d",i);first=0;}
  putchar('}');
}

int main(int argc,char **argv){
  int profiles=0,fail=0;
  int threecut=(argc>1 && strcmp(argv[1],"--threecut")==0);
  if(threecut){
    for(unsigned L=0;L<128;++L)if(pop7(L)>=4)
      for(unsigned M=0;M<128;++M)if(local_profile(M))
        for(unsigned R=0;R<128;++R)if(pop7(R)>=4){
          ++profiles; unsigned w[7];
          if(!solve(L,M,R,w)){
            ++fail; printf("FAIL L=");pset(L);printf(" M=");pset(M);
            printf(" R=");pset(R);putchar('\n');
          }
        }
    printf("threecut_profiles=%d failures=%d\n",profiles,fail);
    return fail!=0;
  }
  for(unsigned L=0;L<128;++L)if(pop7(L)<=3)
    for(unsigned M=0;M<128;++M)if(local_profile(M)&&(pop7(L|M)>=4))
      for(unsigned R=0;R<128;++R)if((L|R)==ALL){
        ++profiles; unsigned w[7];
        if(!solve(L,M,R,w)){
          ++fail; printf("FAIL L=");pset(L);printf(" M=");pset(M);printf(" R=");pset(R);putchar('\n');
        }
      }
  printf("profiles=%d failures=%d\n",profiles,fail);
  return fail!=0;
}
