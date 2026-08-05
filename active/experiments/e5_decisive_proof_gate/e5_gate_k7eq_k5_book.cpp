#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <vector>
using U=uint16_t;
struct G{int n;std::vector<U>a;};
void add(G&g,int x,int y){g.a[x]|=U(1)<<y;g.a[y]|=U(1)<<x;}
int pc(U x){return std::popcount((unsigned)x);}
bool conn(const G&g,U del){U r=((U(1)<<g.n)-1)&~del;if(!r)return true;U seen=r&-r,fr=seen;while(fr){U b=fr&-fr;fr^=b;int v=std::countr_zero((unsigned)b);U nx=g.a[v]&r&~seen;seen|=nx;fr|=nx;}return seen==r;}
bool c5(const G&g){for(int i=0;i<g.n;i++)if(pc(g.a[i])<5)return false;U all=(U(1)<<g.n)-1;for(U s=0;s<=all;s++)if(pc(s)<=4&&!conn(g,s))return false;return true;}
struct S{const G&g;U all;std::vector<char>co;std::vector<U>ex;std::array<U,7>b{};S(const G&x):g(x),all((U(1)<<x.n)-1),co(U(1)<<x.n),ex(U(1)<<x.n){for(U s=1;s<=all;s++){U q=s&-s;int v=std::countr_zero((unsigned)q);ex[s]=ex[s^q]|g.a[v];U seen=q,fr=q;while(fr){U z=fr&-fr;fr^=z;int w=std::countr_zero((unsigned)z);U nx=g.a[w]&s&~seen;seen|=nx;fr|=nx;}co[s]=seen==s;}}bool dfs(U r,int k,int m){if(k==7)return true;if(pc(r)<7-k)return false;U p=r&-r,rest=r^p;for(U s=rest;;s=(s-1)&rest){U q=s|p;if(co[q]){int mm=m;for(int i=0;i<k;i++)if(!(ex[q]&b[i])){if(++mm>1)break;}if(mm<=1){b[k]=q;if(dfs(r^q,k+1,mm))return true;}}if(!s)break;}return dfs(r^p,k,m);}bool run(){return dfs(all,0,0);}};
G book(std::array<std::pair<int,int>,3> miss){G g{11,std::vector<U>(11)};for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)add(g,i,j);for(int t=0;t<3;t++){int a=5+2*t,b=a+1;add(g,a,b);for(int s=0;s<5;s++){if(s!=miss[t].first)add(g,a,s);if(s!=miss[t].second)add(g,b,s);}}return g;}
int main(){int total=0,c5n=0,pos=0,neg=0;for(int a=0;a<5;a++)for(int b=0;b<5;b++)if(a!=b)for(int c=0;c<5;c++)for(int d=0;d<5;d++)if(c!=d)for(int e=0;e<5;e++)for(int f=0;f<5;f++)if(e!=f){G g=book({{{a,b},{c,d},{e,f}}});total++;bool cc=c5(g);if(cc)c5n++;S s(g);if(s.run())pos++;else{neg++;std::cout<<"COUNTEREXAMPLE misses="<<a<<','<<b<<" / "<<c<<','<<d<<" / "<<e<<','<<f<<" c5="<<cc<<"\n";return 0;}}std::cout<<"total="<<total<<" c5="<<c5n<<" pos="<<pos<<" neg="<<neg<<"\n";}
