#include<iostream>
using namespace std;
int n;
int c[102];
int dp[2000000] = {0};
int main(){
	cin >> n;
	for (int i=0;i<n;i++){
		cin >> c[i];
	}
	c[n] = 2000000;
	int m = c[n-1]+c[n-2];
	int trak = 0;
	int j;
	int tmp;
	bool good = true;
	for (int i=1;i<=m;i++){
		if (i>=c[trak+1]) trak ++;
		tmp = dp[i-c[trak]] + 1;
		dp[i] = tmp;
		for (j=0; j<trak; j++) tmp = min(tmp, dp[i-c[j]] + 1);
		if (tmp < dp[i]){
			cout << "non-canonical" << endl;
			good = false;
			break;
		}
	}
	if (good) cout << "canonical" << endl;
}