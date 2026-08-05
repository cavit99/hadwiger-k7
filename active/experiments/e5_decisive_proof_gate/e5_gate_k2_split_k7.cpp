#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using U=uint16_t;struct G{int n;std::vector<U>a;};void add(G&g,int x,int y){g.a[x]|=U(1)<<y;g.a[y]|=U(1)<<x;}int pc(U x){return std::popcount((unsigned)x);}struct S{const G&g;U all;std::vector<char>co;std::vector<U>ex;std::array<U,7>b{};S(const G&x):g(x),all((U(1)<<x.n)-1),co(U(1)<<x.n),ex(U(1)<<x.n){for(U s=1;s<=all;s++){U q=s&-s;int v=std::countr_zero((unsigned)q);ex[s]=ex[s^q]|g.a[v];U seen=q,fr=q;while(fr){U z=fr&-fr;fr^=z;int w=std::countr_zero((unsigned)z);U nx=g.a[w]&s&~seen;seen|=nx;fr|=nx;}co[s]=seen==s;}}bool dfs(U r,int k,int m){if(k==7)return true;if(pc(r)<7-k)return false;U p=r&-r,rest=r^p;for(U s=rest;;s=(s-1)&rest){U q=s|p;if(co[q]){int mm=m;for(int i=0;i<k;i++)if(!(ex[q]&b[i]))mm++;if(mm<=1){b[k]=q;if(dfs(r^q,k+1,mm))return true;}}if(!s)break;}return dfs(r^p,k,m);}bool run(){return dfs(all,0,0);}};
void edge(G&g,int a,int b){add(g,a,b);}G host(int code){G g{11,std::vector<U>(11)};for(auto [a,b]:std::vector<std::pair<int,int>>{{0,1},{1,2},{1,3},{1,4},{1,5},{2,3},{4,5}})edge(g,a,b);edge(g,6,7);for(int r:{0,1,2,3})edge(g,6,r);for(int r:{0,1,4,5})edge(g,7,r);int A=8,B=9,D=10;edge(g,A,B);edge(g,A,0);for(int r=0;r<6;r++)edge(g,D,r);int z=code;for(int r=1;r<6;r++){int t=1+z%3;z/=3;if(t&1)edge(g,A,r);if(t&2)edge(g,B,r);}return g;}
int main(){int neg=0;std::map<int,int> nB,nBoth;for(int code=0;code<243;code++){S s(host(code));if(!s.run()){neg++;int z=code,b=0,both=0;std::array<int,6>c{};c[0]=1;for(int r=1;r<6;r++){c[r]=1+z%3;z/=3;if(c[r]&2)b++;if(c[r]==3)both++;}nB[b]++;nBoth[both]++;std::cout<<"code="<<code<<" c=";for(int r=0;r<6;r++)std::cout<<c[r];std::cout<<"\n";}}std::cout<<"neg="<<neg<<" Bsizes";for(auto[x,y]:nB)std::cout<<' '<<x<<':'<<y;std::cout<<" both";for(auto[x,y]:nBoth)std::cout<<' '<<x<<':'<<y;std::cout<<'\n';}
