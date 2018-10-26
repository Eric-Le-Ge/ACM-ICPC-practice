#include<iostream>
#include<cmath>
using namespace std;

int x[11],y[11];
int DP[11][1<<11+1];
int n, X, Y, b;
const int INF = 0x3f3f3f3f;

int TSP(int node, int mask){
  if (mask == (1<<(b+1))-1) return abs(x[node]-x[0]) + abs(y[node]-y[0]);
  if (DP[node][mask!=-1]) return DP[node][mask];
  int distance = INF;
  for (int i=0;i<b;i++){
    if (!(mask & (1<<i))){
      distance = min(distance, abs(x[node]-x[i])+abs(y[node]-y[i])+TSP(i,mask|(1<<i)));
    }
  }
  return DP[node][mask] = distance;
}


int main(){
  cin >> n;
  while(n--){
    cin >> X >> Y;
    cin >> x[0] >> y[0];
    cin >> b;
    // for (int i=0;i<=b;i++){
    //   for (int j=0;j<=1<<11+1;j++){
    //     DP[i][j] = -1;
    //   }
    // }
    fill(DP,DP+sizeof(DP)/sizeof(int), -1);
    for (int i=1;i<=b;i++){
      cin >> x[i] >> y[i];
    }
    cout << TSP(0,1);
  }






}
