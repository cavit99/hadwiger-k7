#include <bit>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

static bool connected(const std::vector<unsigned>& a, unsigned m) {
    if (!m) return false;
    unsigned seen=m&-m, todo=seen;
    while(todo){unsigned b=todo&-todo;todo^=b;int v=std::countr_zero(b);unsigned add=a[v]&m&~seen;seen|=add;todo|=add;}
    return seen==m;
}
static bool touch(const std::vector<unsigned>& a,unsigned x,unsigned y){
    for(unsigned m=x;m;m&=m-1)if(a[std::countr_zero(m&-m)]&y)return true;
    return false;
}
static bool search(const std::vector<unsigned>& a,int next,std::vector<unsigned>& bags){
    int n=a.size();
    if(next==n){
        if(bags.size()!=7)return false;
        for (auto bag : bags) if (!connected(a, bag)) return false;
        int miss=0;for(int i=0;i<7;i++)for(int j=i+1;j<7;j++)if(!touch(a,bags[i],bags[j])&&++miss>1)return false;
        std::cout<<" model";for(auto b:bags)std::cout<<' '<<b;std::cout<<'\n';return true;
    }
    unsigned bit=1u<<next;
    for(int i=0;i<(int)bags.size();i++){
        unsigned old=bags[i];bags[i]|=bit;
        // connectivity is checked only at the leaf; n=12 is small.
        if(search(a,next+1,bags))return true;
        bags[i]=old;
    }
    if(bags.size()<7){bags.push_back(bit);if(search(a,next+1,bags))return true;bags.pop_back();}
    return false;
}
static std::vector<unsigned> decode(const std::string& g){
    int n=g[0]-63;std::vector<int>b;for(int k=1;k<(int)g.size();k++){int z=g[k]-63;for(int i=5;i>=0;i--)b.push_back((z>>i)&1);}
    std::vector<unsigned>a(n,0);int p=0;for(int j=1;j<n;j++)for(int i=0;i<j;i++,p++)if(b[p]){a[i]|=1u<<j;a[j]|=1u<<i;}return a;
}
static void add(std::vector<unsigned>&a,int x,int y){a[x]|=1u<<y;a[y]|=1u<<x;}
int main(){
    std::vector<std::string> codes={"GCOcaO","GCOcbO","GCOcbW","GCOe`W","GCOebW","GCQQV?","GCQR@O"};
    for(auto g:codes){auto a=decode(g);std::vector<std::vector<int>> ts;
        for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)for(int k=j+1;k<8;k++)if((a[i]>>j&1)&&(a[i]>>k&1)&&(a[j]>>k&1))ts.push_back({i,j,k});
        a.resize(10+ts.size());int u=8,d=9;
        for(int x=0;x<8;x++){add(a,u,x);add(a,d,x);}
        for(int i=0;i<(int)ts.size();i++){
            int k=10+i;
            for(int x=0;x<8;x++){
                bool in=false;for(int y:ts[i])in|=x==y;
                if(!in)add(a,k,x);
            }
        }
        std::vector<unsigned> bags;bool ok=search(a,0,bags);
        std::cout<<g<<" triangles="<<ts.size()<<" "<<(ok?"TARGET":"SURVIVE")<<'\n';
    }
}
