#include <algorithm>
#include <array>
#include <bit>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <random>
#include <set>
#include <vector>
using U=uint32_t;
struct G{int n;std::vector<U>a;};void add(G&g,int x,int y){g.a[x]|=U(1)<<y;g.a[y]|=U(1)<<x;}void rem(G&g,int x,int y){g.a[x]&=~(U(1)<<y);g.a[y]&=~(U(1)<<x);}bool has(const G&g,int x,int y){return (g.a[x]>>y)&1;}int pc(U x){return std::popcount(x);}bool conn(const G&g,U del){U r=((U(1)<<g.n)-1)&~del;if(!r)return true;U seen=r&-r,fr=seen;while(fr){U b=fr&-fr;fr^=b;int v=std::countr_zero(b);U nx=g.a[v]&r&~seen;seen|=nx;fr|=nx;}return seen==r;}bool c5(const G&g){for(int v=0;v<g.n;v++)if(pc(g.a[v])<5)return false;U all=(U(1)<<g.n)-1;for(U s=0;s<=all;s++)if(pc(s)<=4&&!conn(g,s))return false;return true;}
struct Search{const G&g;U all;std::vector<uint8_t>co;std::vector<U>ex;std::array<U,7>b{};uint64_t nodes=0,cap;Search(const G&x,uint64_t cp):g(x),all((U(1)<<x.n)-1),co(U(1)<<x.n),ex(U(1)<<x.n),cap(cp){for(U s=1;s<=all;s++){U q=s&-s;int v=std::countr_zero(q);ex[s]=ex[s^q]|g.a[v];U seen=q,fr=q;while(fr){U z=fr&-fr;fr^=z;int w=std::countr_zero(z);U nx=g.a[w]&s&~seen;seen|=nx;fr|=nx;}co[s]=seen==s;}}int dfs(U r,int k,int m){if(++nodes>cap)return -1;if(k==7)return 1;if(pc(r)<7-k)return 0;U p=r&-r,rest=r^p;int maxsz=pc(r)-(7-k)+1;for(int sz=1;sz<=maxsz;sz++){for(U s=rest;;s=(s-1)&rest){if(pc(s)==sz-1){U q=s|p;if(co[q]){int mm=m;for(int i=0;i<k;i++)if(!(ex[q]&b[i])){if(++mm>1)break;}if(mm<=1){b[k]=q;int z=dfs(r^q,k+1,mm);if(z)return z;}}}if(!s)break;}}return dfs(r^p,k,m);}int run(){return dfs(all,0,0);}};
std::mt19937_64 rng(0xE5BEEF);
template<class T> void reproducible_shuffle(std::vector<T>&v){for(size_t i=v.size();i>1;i--)std::swap(v[i-1],v[rng()%i]);}
void lowK2(G&g){add(g,6,7);for(int r:{0,1,2,3})add(g,6,r);for(int r:{0,1,4,5})add(g,7,r);}
bool connected_ind(const G&g,const std::vector<int>&vs){U m=0;for(int v:vs)m|=U(1)<<v;U q=m&-m,seen=q,fr=q;while(fr){U b=fr&-fr;fr^=b;int v=std::countr_zero(b);U nx=g.a[v]&m&~seen;seen|=nx;fr|=nx;}return seen==m;}
bool full(const G&g,const std::vector<int>&vs){U m=0;for(int v:vs)m|=U(1)<<v;for(int r=0;r<6;r++)if(!(g.a[r]&m))return false;return true;}
void report(const char*name,int trials,int built,int five,int pos,int unk,int neg,uint64_t mx){std::cout<<name<<" trials="<<trials<<" built="<<built<<" five="<<five<<" pos="<<pos<<" unk="<<unk<<" neg="<<neg<<" maxnodes="<<mx<<"\n";}
int main(){const int trials=12000;{
 int built=0,five=0,pos=0,unk=0,neg=0;uint64_t mx=0; // K2 one-six-full-only c=7 n=15
 for(int t=0;t<trials;t++){G g{15,std::vector<U>(15)};lowK2(g);add(g,0,1); // choose dP(0)=1; C contacts at 0 exactly2
  std::vector<std::pair<int,int>>var;for(int i=8;i<15;i++)for(int j=i+1;j<15;j++)var.push_back({i,j});for(int i=8;i<15;i++)for(int r=0;r<6;r++)var.push_back({i,r});
  reproducible_shuffle(var);int need=53-10; // total m53, fixed low9+boundary1=10 =>43 variable
  for(int i=0;i<need;i++)add(g,var[i].first,var[i].second);
  std::vector<int>C={8,9,10,11,12,13,14}; if(!connected_ind(g,C)||!full(g,C)||pc(g.a[0]&(((U)1<<15)-((U)1<<8)))!=2)continue;built++;if(!c5(g))continue;five++;Search s(g,20000000);int r=s.run();mx=std::max(mx,s.nodes);if(r==1)pos++;else if(r<0)unk++;else{neg++;std::cout<<"NEG K2one\n";break;}}
 report("K2-one-full",trials,built,five,pos,unk,neg,mx);
 }
 {
 int built=0,five=0,pos=0,unk=0,neg=0;uint64_t mx=0; // K2 two full C3,D4, boundary unique k7 n15
 for(int t=0;t<trials;t++){G g{15,std::vector<U>(15)};lowK2(g);for(auto e:std::vector<std::pair<int,int>>{{0,1},{1,2},{1,3},{1,4},{1,5},{2,3},{4,5}})add(g,e.first,e.second);
  std::vector<int>C={8,9,10},D={11,12,13,14};std::vector<std::pair<int,int>>var;for(auto V:{C,D}){for(int i=0;i<(int)V.size();i++)for(int j=i+1;j<(int)V.size();j++)var.push_back({V[i],V[j]});for(int v:V)for(int r=0;r<6;r++)var.push_back({v,r});}
  reproducible_shuffle(var);int fixed=9+7;int need=53-fixed;for(int i=0;i<need;i++)add(g,var[i].first,var[i].second);
  if(!connected_ind(g,C)||!connected_ind(g,D)||!full(g,C)||!full(g,D))continue;if(pc(g.a[0]&((U(1)<<8)|(U(1)<<9)|(U(1)<<10)))!=1||pc(g.a[0]&((U(1)<<11)|(U(1)<<12)|(U(1)<<13)|(U(1)<<14)))!=1)continue;built++;if(!c5(g))continue;five++;Search s(g,20000000);int r=s.run();mx=std::max(mx,s.nodes);if(r==1)pos++;else if(r<0)unk++;else{neg++;std::cout<<"NEG K2two\n";break;}}
 report("K2-two-full",trials,built,five,pos,unk,neg,mx);
 }
}
