#include<iostream>
using namespace std;


struct edge{int to, cap, rev;}
vector<edge> G[MAX_V];
bool used[MAX_V];

void add_edge(int from, int to, int cap){
  G[from].push_back((edge){to, cap, G[to.size()]});
  G[to].push_back((edge){from, 0, G[from].size()-1});
}

int dfs(int v, int t, int f){
  if (v==t) return f;
  used[v] = true;
  for (int i=0;i<G[v].size();i++){
    edge &e = G[v][i];
    if (!used[e.to] && e.cap >0){



    }
  }


}
