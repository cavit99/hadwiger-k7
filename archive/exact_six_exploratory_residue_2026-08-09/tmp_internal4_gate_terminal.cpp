#include <bit>
#include <iostream>
#include <string>
#include <vector>

static bool connected(const std::vector<unsigned>& a,unsigned m){if(!m)return false;unsigned seen=m&-m,todo=seen;while(todo){unsigned b=todo&-todo;todo^=b;int v=std::countr_zero(b);unsigned z=a[v]&m&~seen;seen|=z;todo|=z;}return seen==m;}
static bool touch(const std::vector<unsigned>&a,unsigned x,unsigned y){for(unsigned m=x;m;m&=m-1)if(a[std::countr_zero(m&-m)]&y)return true;return false;}
static bool search(const std::vector<unsigned>&a,int at,std::vector<unsigned>&b){if(at==(int)a.size()){if(b.size()!=7)return false;for(auto z:b)if(!connected(a,z))return false;int miss=0;for(int i=0;i<7;i++)for(int j=i+1;j<7;j++)if(!touch(a,b[i],b[j])&&++miss>1)return false;std::cout<<" model";for(auto z:b)std::cout<<' '<<z;std::cout<<'\n';return true;}unsigned z=1u<<at;for(int i=0;i<(int)b.size();i++){auto old=b[i];b[i]|=z;if(search(a,at+1,b))return true;b[i]=old;}if(b.size()<7){b.push_back(z);if(search(a,at+1,b))return true;b.pop_back();}return false;}
static std::vector<unsigned> decode(const std::string&g){int n=g[0]-63;std::vector<int>b;for(int k=1;k<(int)g.size();k++){int z=g[k]-63;for(int i=5;i>=0;i--)b.push_back(z>>i&1);}std::vector<unsigned>a(n);int p=0;for(int j=1;j<n;j++)for(int i=0;i<j;i++,p++)if(b[p]){a[i]|=1u<<j;a[j]|=1u<<i;}return a;}
static void add(std::vector<unsigned>&a,int x,int y){a[x]|=1u<<y;a[y]|=1u<<x;}
static std::vector<std::vector<int>> triangles(const std::vector<unsigned>&a){std::vector<std::vector<int>>r;for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)for(int k=j+1;k<8;k++)if((a[i]>>j&1)&&(a[i]>>k&1)&&(a[j]>>k&1))r.push_back({i,j,k});return r;}
int main(){std::vector<std::string>codes={"GCOcaO","GCOcbO","GCOcbW","GCOe`W","GCOebW","GCQQV?","GCQR@O"};
for(auto code:codes){auto base=decode(code);auto ts=triangles(base);bool all1=true,all2=true;
 for(auto T:ts)for(int gate_t:T){auto a=base;a.resize(12);int u=8,d=9,k=10,c=11;for(int x=0;x<8;x++){add(a,u,x);add(a,d,x);}for(int x=0;x<8;x++)if(x!=T[0]&&x!=T[1]&&x!=T[2])add(a,k,x);add(a,k,gate_t);add(a,k,c);for(int t:T)if(t!=gate_t)add(a,c,t);std::vector<unsigned>b;bool ok=search(a,0,b);if(!ok){all1=false;std::cout<<code<<" ONE_GATE T="<<T[0]<<T[1]<<T[2]<<" tg="<<gate_t<<" SURVIVE\n";}}
 for(auto T:ts)for(int mask=0;mask<64;mask++){bool covers=true;for(int i=0;i<3;i++)if(((mask>>(2*i))&3)==0)covers=false;if(!covers)continue;auto a=base;a.resize(13);int u=8,d=9,k=10,c1=11,c2=12;for(int x=0;x<8;x++){add(a,u,x);add(a,d,x);}for(int x=0;x<8;x++)if(x!=T[0]&&x!=T[1]&&x!=T[2])add(a,k,x);add(a,k,c1);add(a,k,c2);for(int i=0;i<3;i++){int m=(mask>>(2*i))&3;if(m&1)add(a,c1,T[i]);if(m&2)add(a,c2,T[i]);}std::vector<unsigned>b;bool ok=search(a,0,b);if(!ok){all2=false;std::cout<<code<<" TWO_GATE T="<<T[0]<<T[1]<<T[2]<<" mask="<<mask<<" SURVIVE\n";}}
 std::cout<<code<<" summary one="<<all1<<" two="<<all2<<"\n";
}}
