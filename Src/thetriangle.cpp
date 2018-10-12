#include<iostream>
#include<cstring>
using namespace std;

int dp[100][100];
int triangle[5050];
int n,res = 0;

int grab(int r, int m){
  if (r == 0){
    return triangle[0];
  }
  if (dp[r][m] != -1){
    return dp[r][m];
  }
  if (m == 0){
    return dp[r][0] = grab(r-1,0) + triangle[(r+r*r)/2];
  }
  if (m == r){
    return dp[r][r] = grab(r-1,r-1) + triangle[(3*r + r*r)/2];
  }
  return dp[r][m] = max(grab(r-1,m-1),grab(r-1,m)) + triangle[(r+r*r)/2 + m];
}

int main(){
  cin >> n;
  memset(dp,-1,sizeof(dp));
  for (int i=0;i<(n*n+n)/2;i++){
    cin >> triangle[i];
  }
  for (int j = 0;j<n;j++){
    res = max(res,grab(n-1,j));
  }
  cout << res << endl;
}
