#include<iostream>
#include<vector>
#include<queue>          // std::priority_queue
#include<functional>
//#include<stdlib.h>     /* abs */
#include<math.h>       /* pow */ //fabs
#include<float.h> // for float,double macros
using namespace std;
long double X[102], Y[102];
typedef pair<long double, int> P;
typedef pair<int, long double> E;
long double D[102];
vector<pair<int,long double> > G[102];
int n;
long double sx, sy, tx, ty, x, y, d, weight ,run, shoot;

long double dist(long double x0,long double y0,long double x1,long double y1){
  d = sqrt(pow(x0-x1,2)+pow(y0-y1,2));
  run = d/5.0;
  shoot = 2.0+fabs((50-d)/5.0);
  return min(run, shoot);
}

long double ucs(){
  priority_queue<P, vector<P>, greater<P> > que;
  fill(D, D+102, DBL_MAX);
  D[n+1] = 0.0;
  que.push(P(0.0,n+1));

  while (!que.empty()){
    P p = que.top(); que.pop();
    int v = p.second;
    if (v==n) return D[v];
    if (D[v] < p.first) continue;
    for (int i=0;i<G[v].size();i++){
      E e = G[v][i];
      if (D[e.first] > D[v] + e.second){
        D[e.first] = D[v] + e.second;
        que.push(P(D[e.first],e.first));
      }
    }


  }
}

int main(){
  cin >> sx >> sy;
  cin >> tx >> ty >> n; //Load Graph
  for (int i=0; i<n; i++){
    cin >> X[i] >> Y[i];
    for (int j=0; j<i;j++){
      weight = dist(X[i],Y[i],X[j],Y[j]);
      G[i].push_back(E(j,weight));
      G[j].push_back(E(i,weight));
    }
  }
  X[n+1] = sx;
  Y[n+1] = sy;
  X[n] = tx;
  Y[n] = ty;
  for (int i=0; i<n; i++){
    weight = dist(tx, ty, X[i],Y[i]);
    G[i].push_back(E(n,weight));
    G[n].push_back(E(i,weight));
  }
  for (int i=0; i<n+1; i++){
    weight = sqrt(pow(sx-X[i],2)+pow(sy-Y[i],2))/5.0;

    G[i].push_back(E(n+1,weight));
    G[n+1].push_back(E(i,weight));
  }

  // for (int i=0; i<n+2; i++){
  //   for (int j=0;j<G[i].size();j++){
  //     E e = G[i][j];
  //     cout << e.first << " " << e.second << endl;
  //
  //   }
  //
  // }
  d = ucs();
  cout.precision(8);
  cout << d << endl;

}
