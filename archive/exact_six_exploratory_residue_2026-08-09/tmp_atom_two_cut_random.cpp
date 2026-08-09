#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <random>
#include <tuple>
#include <vector>

struct DSU {
  std::array<int, 16> p{};
  explicit DSU(int n) { std::iota(p.begin(), p.end(), 0); }
  int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
  bool join(int x, int y) {
    x = find(x); y = find(y); if (x == y) return false; p[x] = y; return true;
  }
};

static bool has_model(int n, const std::vector<std::pair<int,int>>& edges, bool vee=false) {
  const int need = n - 7;
  std::vector<int> pick;
  auto rec = [&](auto&& self, int at, int left, DSU dsu) -> bool {
    if (left == 0) {
      std::array<int,16> id{}; id.fill(-1); int k=0;
      for (int v=0;v<n;++v) { int r=dsu.find(v); if (id[r]<0) id[r]=k++; }
      if (k != 7) return false;
      std::array<uint8_t,7> q{};
      for (auto [u,v]:edges) { int x=id[dsu.find(u)], y=id[dsu.find(v)]; if(x!=y){q[x]|=1u<<y;q[y]|=1u<<x;} }
      int miss=0, x0=-1,y0=-1,x1=-1,y1=-1;
      for(int i=0;i<7;++i) for(int j=i+1;j<7;++j) if(!(q[i]>>j&1)) {
        if(!miss){x0=i;y0=j;} else if(miss==1){x1=i;y1=j;} ++miss;
        if(miss>(vee?2:1)) return false;
      }
      return !vee || miss<=1 || x0==x1 || x0==y1 || y0==x1 || y0==y1;
    }
    if ((int)edges.size()-at < left) return false;
    for (int i=at;i<=(int)edges.size()-left;++i) {
      auto next=dsu; auto [u,v]=edges[i];
      if(!next.join(u,v)) continue;
      if(self(self,i+1,left-1,next)) return true;
    }
    return false;
  };
  return rec(rec,0,need,DSU(n));
}

static void add(std::array<uint16_t,16>& a, std::vector<std::pair<int,int>>& e, int u,int v){
  if(u==v || (a[u]>>v&1)) return; a[u]|=1u<<v;a[v]|=1u<<u;e.push_back({u,v});
}

int main(int argc,char**argv){
  int kind=argc>1?std::atoi(argv[1]):0; // 0 K2, 1 P3, 2 K3
  int r=argc>2?std::atoi(argv[2]):0;
  int trials=argc>3?std::atoi(argv[3]):1000;
  int a=kind?3:2, p=7-a-r, w=7-r, n=a+(7-a)+w;
  std::mt19937_64 rng(1234567+100*kind+r);
  int survivors=0;
  for(int z=0;z<trials;++z){
    std::array<uint16_t,16> adj{}; std::vector<std::pair<int,int>> e;
    if(kind==0) add(adj,e,0,1); else {add(adj,e,0,1);add(adj,e,1,2);if(kind==2)add(adj,e,0,2);}
    int t0=a, w0=7; // T outside A occupies [a,7); first r are old S roots. W roots [7,n).
    int gcount=(a==3?2:((r<=1 && (rng()&1))?3:2));
    std::vector<int> sizes;
    if(gcount==2){int lo=a,hi=w-a;int x=lo+(rng()%(hi-lo+1));sizes={x,w-x};}
    else {int rem=w;for(int i=0;i<2;++i){int hi=rem-a*(2-i);int x=a+(rng()%(hi-a+1));sizes.push_back(x);rem-=x;}sizes.push_back(rem);}
    std::vector<std::vector<int>> groups; int cur=w0;
    for(int sz:sizes){groups.push_back({});for(int j=0;j<sz;++j)groups.back().push_back(cur++);}
    // random atom misses, retry until each atom vertex sees every group and each root sees atom.
    bool ok=false;
    for(int retry=0;retry<100&&!ok;++retry){
      auto base_adj=adj; auto base_e=e;
      std::vector<int> caps(a);
      for(int u=0;u<a;++u){int din=kind==0?1:(kind==1?(u==1?2:1):2);caps[u]=7-din;}
      for(int u=0;u<a;++u){
        std::vector<int> roots;for(int s=0;s<7;++s)roots.push_back(s<r?a+s:w0+s-r);
        std::shuffle(roots.begin(),roots.end(),rng); roots.resize(caps[u]);
        for(int v:roots)add(adj,e,u,v);
      }
      ok=true;
      for(int s=0;s<7;++s){int v=s<r?a+s:w0+s-r;bool seen=false;for(int u=0;u<a;++u)seen|=adj[v]>>u&1;if(!seen)ok=false;}
      for(auto&g:groups)for(int u=0;u<a;++u){bool seen=false;for(int v:g)seen|=adj[u]>>v&1;if(!seen)ok=false;}
      if(!ok){adj=base_adj;e=base_e;}
    }
    if(!ok){--z;continue;}
    // connect each group by a random tree.
    for(auto g:groups){std::shuffle(g.begin(),g.end(),rng);for(int i=1;i<(int)g.size();++i)add(adj,e,g[i],g[rng()%i]);}
    // each group is full to R union P; atom fullness already checked.
    for(auto&g:groups)for(int v=a;v<7;++v)add(adj,e,v,g[rng()%g.size()]);
    bool hit=has_model(n,e);
    if(!hit){
      bool vee=has_model(n,e,true);
      ++survivors; std::cout<<"SURV vee="<<vee<<" kind="<<kind<<" r="<<r<<" groups=";for(int x:sizes)std::cout<<x<<",";std::cout<<" edges="<<e.size()<<" ";for(auto [u,v]:e)std::cout<<u<<"-"<<v<<",";std::cout<<"\n"; if(survivors>=5)break;
    }
  }
  std::cerr<<"kind="<<kind<<" r="<<r<<" survivors="<<survivors<<"\n";
}
