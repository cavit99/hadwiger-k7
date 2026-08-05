#include <algorithm>
#include <array>
#include <bit>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif
using Bits=std::uint16_t;
using EMask=std::uint64_t;
struct Part { std::array<Bits,7> b{}; int used=0; };
std::vector<Part> parts;
std::array<std::pair<int,int>,36> ep;
std::array<std::array<int,9>,9> ei;

void gen_assign(int n,int v,int k,std::array<Bits,7>&b){
    if(v==n){if(k==7){Part p;p.b=b; for(auto x:b)p.used+=std::popcount((unsigned)x);parts.push_back(p);}return;}
    if(k+(n-v)<7)return;
    // unused
    gen_assign(n,v+1,k,b);
    Bits bit=Bits(1)<<v;
    for(int i=0;i<k;i++){b[i]|=bit;gen_assign(n,v+1,k,b);b[i]^=bit;}
    if(k<7){b[k]=bit;gen_assign(n,v+1,k+1,b);b[k]=0;}
}
inline bool connected(Bits s,const std::array<Bits,9>&adj){
    if((s&(s-1))==0)return true;
    Bits seen=s&-s,fr=seen;
    while(fr){Bits q=fr&-fr;fr^=q;int v=std::countr_zero((unsigned)q);Bits nx=adj[v]&s&~seen;seen|=nx;fr|=nx;}
    return seen==s;
}
inline bool target(EMask missing){
    std::array<Bits,9> adj{};
    Bits all=(Bits(1)<<9)-1;
    for(int i=0;i<9;i++)adj[i]=all^(Bits(1)<<i);
    EMask mm=missing;
    while(mm){EMask q=mm&-mm;int e=std::countr_zero(q);mm^=q;auto [u,v]=ep[e];adj[u]&=~(Bits(1)<<v);adj[v]&=~(Bits(1)<<u);}
    // parts sorted by used/order naturally generation; check
    for(const auto&p:parts){
        bool ok=true;
        for(auto b:p.b)if(!connected(b,adj)){ok=false;break;}
        if(!ok)continue;
        int miss=0;
        for(int i=0;i<7&&miss<=1;i++)for(int j=i+1;j<7;j++){
            Bits x=p.b[i], contacts=0;
            while(x){Bits q=x&-x;x^=q;contacts|=adj[std::countr_zero((unsigned)q)];}
            if(!(contacts&p.b[j])){if(++miss>1)break;}
        }
        if(miss<=1)return true;
    }
    return false;
}
inline bool conn_after_del(const std::array<Bits,9>&adj,Bits del){
    Bits r=((Bits(1)<<9)-1)&~del;if(!r)return true;Bits seen=r&-r,fr=seen;
    while(fr){Bits q=fr&-fr;fr^=q;int v=std::countr_zero((unsigned)q);Bits nx=adj[v]&r&~seen;seen|=nx;fr|=nx;}return seen==r;
}
inline bool fiveconn(EMask missing){
    std::array<Bits,9> adj{};Bits all=(Bits(1)<<9)-1;for(int i=0;i<9;i++)adj[i]=all^(Bits(1)<<i);
    EMask mm=missing;while(mm){EMask q=mm&-mm;int e=std::countr_zero(q);mm^=q;auto [u,v]=ep[e];adj[u]&=~(Bits(1)<<v);adj[v]&=~(Bits(1)<<u);}
    for(int i=0;i<9;i++)if(std::popcount((unsigned)adj[i])<5)return false;
    for(Bits s=0;s<(Bits(1)<<9);s++)if(std::popcount((unsigned)s)<=4&&!conn_after_del(adj,s))return false;
    return true;
}

int main(){int z=0;for(int i=0;i<9;i++)for(int j=i+1;j<9;j++){ep[z]={i,j};ei[i][j]=ei[j][i]=z++;}
 std::array<Bits,7>b{};gen_assign(9,0,0,b);
 std::stable_sort(parts.begin(),parts.end(),[](auto&a,auto&b){return a.used<b.used;});
 std::cerr<<"parts="<<parts.size()<<"\n";
 auto t0=std::chrono::steady_clock::now();
 unsigned long long total=0,neg=0,neg5=0;
 std::vector<EMask>wit;
 // split by first edge for omp
 #pragma omp parallel for schedule(dynamic,1) reduction(+:total,neg,neg5)
 for(int a=0;a<=29;a++){
   std::vector<EMask> local;
   for(int b=a+1;b<=30;b++)for(int c=b+1;c<=31;c++)for(int d=c+1;d<=32;d++)for(int e=d+1;e<=33;e++)for(int f=e+1;f<=34;f++)for(int g=f+1;g<=35;g++){
     EMask m=(EMask(1)<<a)|(EMask(1)<<b)|(EMask(1)<<c)|(EMask(1)<<d)|(EMask(1)<<e)|(EMask(1)<<f)|(EMask(1)<<g);total++;
     if(target(m))continue;neg++;if(fiveconn(m)){neg5++;local.push_back(m);}
   }
   if(!local.empty()){
    #pragma omp critical
    wit.insert(wit.end(),local.begin(),local.end());
   }
 }
 auto sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-t0).count();
 std::cout<<"n=9 m=29 total="<<total<<" target_free="<<neg<<" five_connected_target_free="<<neg5<<" seconds="<<sec<<"\n";
 for(auto m:wit){std::cout<<"WIT";for(int i=0;i<36;i++)if((m>>i)&1)std::cout<<' '<<i;std::cout<<"\n";}
}
