#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <vector>
using U=uint16_t;struct G{int n;std::vector<U>a;};void add(G&g,int x,int y){g.a[x]|=U(1)<<y;g.a[y]|=U(1)<<x;}int pc(U x){return std::popcount((unsigned)x);}bool conn(const G&g,U del){U r=((U(1)<<g.n)-1)&~del;U seen=r&-r,fr=seen;while(fr){U b=fr&-fr;fr^=b;int v=std::countr_zero((unsigned)b);U nx=g.a[v]&r&~seen;seen|=nx;fr|=nx;}return seen==r;}bool c5(const G&g){for(int i=0;i<g.n;i++)if(pc(g.a[i])<5)return false;U all=(U(1)<<g.n)-1;for(U s=0;s<=all;s++)if(pc(s)<=4&&!conn(g,s))return false;return true;}struct S{const G&g;U all;std::vector<char>co;std::vector<U>ex;std::array<U,7>b{};S(const G&x):g(x),all((U(1)<<x.n)-1),co(U(1)<<x.n),ex(U(1)<<x.n){for(U s=1;s<=all;s++){U q=s&-s;int v=std::countr_zero((unsigned)q);ex[s]=ex[s^q]|g.a[v];U seen=q,fr=q;while(fr){U z=fr&-fr;fr^=z;int w=std::countr_zero((unsigned)z);U nx=g.a[w]&s&~seen;seen|=nx;fr|=nx;}co[s]=seen==s;}}bool dfs(U r,int k,int m){if(k==7)return true;if(pc(r)<7-k)return false;U p=r&-r,rest=r^p;for(U s=rest;;s=(s-1)&rest){U q=s|p;if(co[q]){int mm=m;for(int i=0;i<k;i++)if(!(ex[q]&b[i]))mm++;if(mm<=1){b[k]=q;if(dfs(r^q,k+1,mm))return true;}}if(!s)break;}return dfs(r^p,k,m);}bool run(){return dfs(all,0,0);}};
int main(){int total=0,c5n=0,pos=0,neg=0; // boundary 0=u,1=d,2=v,3,4,5=U; comps 6,7 and 8,9
for(int uu=3;uu<=5;uu++)for(int du=3;du<=5;du++)for(int cu=6;cu<=7;cu++)for(int cd=6;cd<=7;cd++)for(int eu=8;eu<=9;eu++)for(int ed=8;ed<=9;ed++){
 G g{10,std::vector<U>(10)}; // K4 on v,U
 for(int i=2;i<=5;i++)for(int j=i+1;j<=5;j++)add(g,i,j);add(g,0,1);add(g,0,2);add(g,1,2);add(g,0,uu);add(g,1,du);
 add(g,6,7);add(g,8,9);for(int x=6;x<=9;x++)for(int r=2;r<=5;r++)add(g,x,r);add(g,0,cu);add(g,1,cd);add(g,0,eu);add(g,1,ed);total++;if(c5(g))c5n++;S s(g);if(s.run())pos++;else{neg++;std::cout<<"NEG uu="<<uu<<" du="<<du<<" cu="<<cu<<" cd="<<cd<<" eu="<<eu<<" ed="<<ed<<" c5="<<c5(g)<<"\n";}}
std::cout<<"total="<<total<<" 5conn="<<c5n<<" pos="<<pos<<" neg="<<neg<<"\n";}
