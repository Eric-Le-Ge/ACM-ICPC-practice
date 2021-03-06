#include <iostream>
#include <vector>
#include <string>
using namespace std;

//disjoint sets
int par[1000002];
int Rank[1000002];
void init(int N){
    for (int i=0;i<N;i++){
        par[i] = i;
        Rank[i] = 0;
    }
}

int find(int x){
    if (par[x]==x){
        return x;
    } else {
        return par[x] = find(par[x]);
    }
}

void unite(int x,int y){
    x = find(x);
    y = find(y);
    if (x==y) return;
    if (Rank[x]<Rank[y]){
        par[x]=y;
    }
    else{
        par[y] = x;
        if (Rank[x]==Rank[y]) Rank[x]++;
    }
}

bool same(int x, int y){
    return find(x) == find(y);
}