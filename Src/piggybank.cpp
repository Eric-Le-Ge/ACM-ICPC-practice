#include<iostream>
using namespace std;
int dp[10001];
int inf = 214748363;
int v[500],w[500],t,n,W,w1,w2;
int main(){
cin >> t;
for (;t>0;t--){
fill(dp,dp+10001,inf);
dp[0] = 0;
cin >> w1 >> w2;
W = w2-w1;
cin >> n;
for (int i=0;i<n;i++){
cin >> v[i] >> w[i];
}
for (int i=0;i<n;i++){
for (int j = w[i]; j<=W;j++){
dp[j] = min(dp[j],dp[j-w[i]]+v[i]);
}

}
if (dp[W]==inf) cout << "This is impossible." << endl;
else{
cout << "The minimum amount of money in the piggy-bank is " << dp[W] << "." << endl;
}
}
return 0;
}
