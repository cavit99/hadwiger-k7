#include <algorithm>
#include <array>
#include <bit>
#include <chrono>
#include <cstdint>
#include <functional>
#include <iostream>
#include <vector>
using U=uint32_t;
struct Graph{int n;std::vector<U>adj;};
void add(Graph&g,int a,int b){g.adj[a]|=U(1)<<b;g.adj[b]|=U(1)<<a;}
int pc(U x){return std::popcount(x);} 
struct MinorSearch{
 const Graph&g;U all;std::vector<uint8_t>conn;std::vector<U>ext;std::array<U,7>bags{};uint64_t nodes=0;
 MinorSearch(const Graph&x):g(x),all((U(1)<<x.n)-1),conn(U(1)<<x.n),ext(U(1)<<x.n){
  for(U s=1;s<=all;s++){U b=s&-s;int v=std::countr_zero(b);ext[s]=ext[s^b]|g.adj[v];U seen=b,fr=b;while(fr){U q=fr&-fr;fr^=q;int y=std::countr_zero(q);U nx=g.adj[y]&s&~seen;seen|=nx;fr|=nx;}conn[s]=(seen==s);} }
 bool dfs(U rem,int nb,int miss){++nodes;if(nb==7)return true;int need=7-nb;if(pc(rem)<need)return false;U p=rem&-rem,rest=rem^p;int maxsz=pc(rem)-need+1;
  for(int sz=1;sz<=maxsz;sz++){for(U sub=rest;;sub=(sub-1)&rest){if(pc(sub)==sz-1){U bag=sub|p;if(conn[bag]){int nm=miss;for(int i=0;i<nb;i++){if(!(ext[bag]&bags[i])){nm++;if(nm>1)break;}}if(nm<=1){bags[nb]=bag;if(dfs(rem^bag,nb+1,nm))return true;}}}if(sub==0)break;}}
  return dfs(rem^p,nb,miss);
 }
 bool run(){return dfs(all,0,0);} };

std::vector<std::pair<int,int>> bedges(){std::vector<std::pair<int,int>>e;for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)e.push_back({i,j});return e;}
Graph quotient(int mask){Graph g{10,std::vector<U>(10)};auto e=bedges();for(int i=0;i<15;i++)if(mask>>i&1)add(g,e[i].first,e[i].second);add(g,6,7);for(int r:{0,1,2,3})add(g,6,r);for(int r:{0,1,4,5})add(g,7,r);for(int x:{8,9})for(int r=0;r<6;r++)add(g,x,r);return g;}
Graph base_actual(int mask,int uc,int ud){Graph g{13,std::vector<U>(13)};auto e=bedges();for(int i=0;i<15;i++)if(mask>>i&1)add(g,e[i].first,e[i].second);add(g,6,7);for(int r:{0,1,2,3})add(g,6,r);for(int r:{0,1,4,5})add(g,7,r);
 // max components C=8,9 D=10,11,12. internal complete; roots1..5 complete; root0 chosen one each
 add(g,8,9);for(int i=10;i<13;i++)for(int j=i+1;j<13;j++)add(g,i,j);
 for(int x=8;x<13;x++)for(int r=1;r<6;r++)add(g,x,r);add(g,uc,0);add(g,ud,0);return g;}
std::vector<std::pair<int,int>> maxvar(int uc,int ud){std::vector<std::pair<int,int>>e; e.push_back({8,9});for(int i=10;i<13;i++)for(int j=i+1;j<13;j++)e.push_back({i,j});for(int x=8;x<13;x++)for(int r=1;r<6;r++)e.push_back({x,r});e.push_back({uc,0});e.push_back({ud,0});return e;}
void rem(Graph&g,int a,int b){g.adj[a]&=~(U(1)<<b);g.adj[b]&=~(U(1)<<a);} 
bool comp_conn_full(const Graph&g,int lo,int hi){U cm=0;for(int x=lo;x<hi;x++)cm|=U(1)<<x;U seen=cm&-cm,fr=seen;while(fr){U b=fr&-fr;fr^=b;int v=std::countr_zero(b);U nx=g.adj[v]&cm&~seen;seen|=nx;fr|=nx;}if(seen!=cm)return false;for(int r=0;r<6;r++)if(!(g.adj[r]&cm))return false;return true;}
bool conn_del(const Graph&g,U del){U remm=((U(1)<<g.n)-1)&~del;U seen=remm&-remm,fr=seen;while(fr){U b=fr&-fr;fr^=b;int v=std::countr_zero(b);U nx=g.adj[v]&remm&~seen;seen|=nx;fr|=nx;}return seen==remm;}
bool conn5(const Graph&g){for(int v=0;v<g.n;v++)if(pc(g.adj[v])<5)return false;U all=(U(1)<<g.n)-1;for(U s=0;s<=all;s++){int k=pc(s);if(k<=4&&!conn_del(g,s))return false;}return true;}
int main(){auto st=std::chrono::steady_clock::now();auto be=bedges();std::vector<int> negmasks;for(int mask=0;mask<(1<<15);mask++){
 // edge01 present; no other edge incident0; k 5..7
 bool ok=false;for(int i=0;i<15;i++)if(be[i]==std::pair<int,int>{0,1}){ok=(mask>>i)&1;break;}if(!ok)continue;bool bad=false;for(int i=0;i<15;i++)if((mask>>i&1)&&be[i].first==0&&be[i].second!=1)bad=true;if(bad)continue;int k=pc(mask);if(k<5||k>7)continue;Graph q=quotient(mask);MinorSearch ms(q);if(!ms.run())negmasks.push_back(mask);
 }
 std::cout<<"negative quotient masks k5-7="<<negmasks.size()<<"\n";
 uint64_t total=0,structok=0,neg=0,connneg=0;uint64_t maxnodes=0;
 for(int mask:negmasks){int k=pc(mask),missing=k-5;for(int uc:{8,9})for(int ud:{10,11,12}){auto ve=maxvar(uc,ud);std::vector<int>ch(missing);std::function<void(int,int)>rec=[&](int p,int s){if(p==missing){total++;Graph g=base_actual(mask,uc,ud);for(int idx:ch)rem(g,ve[idx].first,ve[idx].second);if(!comp_conn_full(g,8,10)||!comp_conn_full(g,10,13))return;structok++;MinorSearch ms(g);bool has=ms.run();maxnodes=std::max(maxnodes,ms.nodes);if(!has){neg++;bool c5=conn5(g);if(c5)connneg++;std::cout<<"NEG mask="<<mask<<" k="<<k<<" uc="<<uc<<" ud="<<ud<<" miss";for(int x:ch)std::cout<<' '<<x;std::cout<<" 5conn="<<c5<<" nodes="<<ms.nodes<<"\n";}return;}for(int i=s;i<=int(ve.size())-(missing-p);i++){ch[p]=i;rec(p+1,i+1);}};rec(0,0);}}
 double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-st).count();std::cout<<"total="<<total<<" struct="<<structok<<" negative="<<neg<<" 5conn_negative="<<connneg<<" maxnodes="<<maxnodes<<" sec="<<sec<<"\n";
}
