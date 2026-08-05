#include <algorithm>
#include <array>
#include <bit>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <functional>
#include <numeric>
#include <string>
#include <vector>
using U=uint32_t;

struct Graph {
 int n; std::vector<U> adj;
};
void add(Graph&g,int a,int b){g.adj[a]|=U(1)<<b; g.adj[b]|=U(1)<<a;}
int pc(U x){return std::popcount(x);}

bool connected_after_delete(const Graph&g,U del){
 U rem=((U(1)<<g.n)-1)&~del; if(!rem) return true;
 U seen=rem&-rem, fr=seen;
 while(fr){U b=fr&-fr;fr^=b;int v=std::countr_zero(b);U nx=g.adj[v]&rem&~seen;seen|=nx;fr|=nx;}
 return seen==rem;
}
bool is_5conn(const Graph&g){
 for(int v=0;v<g.n;v++) if(pc(g.adj[v])<5) return false;
 U all=(U(1)<<g.n)-1;
 for(int k=0;k<=4;k++){
  // enumerate masks of size k
  for(U s=0;s<=all;s++) if(pc(s)==k && !connected_after_delete(g,s)) return false;
 }
 return true;
}

struct MinorSearch {
 const Graph&g; U all; std::vector<uint8_t> conn; std::vector<U> ext; std::array<U,7> bags{};
 uint64_t nodes=0;
 MinorSearch(const Graph&gg):g(gg),all((U(1)<<gg.n)-1),conn(U(1)<<gg.n),ext(U(1)<<gg.n){
  conn[0]=0;
  for(U s=1;s<=all;s++){
   U b=s&-s; int v=std::countr_zero(b); ext[s]=ext[s^b]|g.adj[v];
   U seen=b,fr=b;
   while(fr){U q=fr&-fr;fr^=q;int x=std::countr_zero(q);U nx=g.adj[x]&s&~seen;seen|=nx;fr|=nx;}
   conn[s]=(seen==s);
  }
 }
 bool dfs(U rem,int nb,int miss){
  ++nodes;
  if(nb==7) return true;
  int need=7-nb;
  if(pc(rem)<need) return false;
  U pivot=rem&-rem;
  // First try singleton and small connected bags by submask enumeration sorted implicitly via size loops.
  U rest=rem^pivot;
  for(int sz=1; sz<=pc(rem)-need+1; ++sz){
   U sub=rest;
   while(true){
    if(pc(sub)==sz-1){U bag=sub|pivot; if(conn[bag]){
      int nm=miss;
      for(int i=0;i<nb;i++) if((ext[bag]&bags[i])==0) {if(++nm>1) break;}
      if(nm<=1){bags[nb]=bag; if(dfs(rem^bag,nb+1,nm)) return true;}
    }}
    if(sub==0) break; sub=(sub-1)&rest;
   }
  }
  // pivot unused
  return dfs(rem^pivot,nb,miss);
 }
 bool run(){return dfs(all,0,0);}
};

std::vector<std::pair<int,int>> var_edges(int c){
 std::vector<std::pair<int,int>> e;
 // C starts 10
 for(int i=0;i<c;i++) for(int j=i+1;j<c;j++) e.push_back({10+i,10+j});
 for(int i=0;i<c;i++) for(int r=0;r<6;r++) e.push_back({10+i,r});
 return e;
}
Graph base_graph(int c,int bmask){
 Graph g{10+c,std::vector<U>(10+c)};
 // boundary 01 plus optional 23 bit0, 45 bit1
 add(g,0,1); if(bmask&1)add(g,2,3); if(bmask&2)add(g,4,5);
 // low K2 d=6,w=7
 add(g,6,7); for(int r: {0,1,2,3})add(g,6,r); for(int r:{0,1,4,5})add(g,7,r);
 // extra full edge missing u=0: 8,9 complete to 1..5
 add(g,8,9); for(int x:{8,9}) for(int r=1;r<6;r++) add(g,x,r);
 return g;
}
bool C_connected_sixfull(const Graph&g,int c){
 U cm=0;for(int i=0;i<c;i++)cm|=U(1)<<(10+i);
 // connected induced
 U seen=cm&-cm,fr=seen;while(fr){U b=fr&-fr;fr^=b;int v=std::countr_zero(b);U nx=g.adj[v]&cm&~seen;seen|=nx;fr|=nx;} if(seen!=cm)return false;
 for(int r=0;r<6;r++) if((g.adj[r]&cm)==0)return false;
 if(pc(g.adj[0]&cm)!=2)return false;
 return true;
}

int main(){
 auto start=std::chrono::steady_clock::now();
 uint64_t total=0,structok=0,connok=0,minorpos=0,negative=0;
 for(int bmask=0;bmask<4;bmask++){
  int k=1+pc(bmask); int c=4; auto ve=var_edges(c); int maxe=ve.size(); int required=4*c+13-k; int missing=maxe-required;
  std::cout<<"boundary_mask "<<bmask<<" k="<<k<<" missing_variable="<<missing<<"\n";
  // choose missing positions
  std::vector<int> choose(missing);
  std::function<void(int,int)> rec=[&](int pos,int st){
   if(pos==missing){
    total++; Graph g=base_graph(c,bmask); std::vector<char> miss(maxe,0);for(int x:choose)miss[x]=1;
    for(int i=0;i<maxe;i++)if(!miss[i])add(g,ve[i].first,ve[i].second);
    if(!C_connected_sixfull(g,c))return; structok++;
    if(!is_5conn(g))return; connok++;
    MinorSearch ms(g); bool has=ms.run();
    if(has){minorpos++;}
    else {negative++; std::cout<<"NEGATIVE candidate bmask="<<bmask<<" missing:";for(int x:choose)std::cout<<' '<<x;std::cout<<" nodes="<<ms.nodes<<"\n";}
    return;
   }
   for(int i=st;i<=maxe-(missing-pos);i++){choose[pos]=i;rec(pos+1,i+1);}
  };
  rec(0,0);
 }
 auto sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
 std::cout<<"total="<<total<<" struct="<<structok<<" 5conn="<<connok<<" minor="<<minorpos<<" negative="<<negative<<" sec="<<sec<<"\n";
}
