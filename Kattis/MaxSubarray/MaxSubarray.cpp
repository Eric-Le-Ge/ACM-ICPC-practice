#include<iostream>
using namespace std;
typedef long long ll;

ll dp[50020002];
ll neginf = -50000000000000;
ll neginf0 = -100000000000000;
ll arr[5000];
ll final_res;
int n, k;

ll compute(int i,int j,int last){
	ll res;
	int idx = i*2*(k+1)+j*2+last;
	if (dp[idx] != neginf0) return dp[idx];
	if (j>i) res = neginf;
	else if (j==0) res = neginf * last;
	else {
		if (last) res = max(compute(i-1, j-1, 1), max(compute(i-1, j, 1), compute(i-1, j-1, 0))) + arr[i-1];
		else res = max(compute(i-1, j, 0), compute(i-1, j, 1));
	}
	dp[idx] = res;
	return res;
}

int main(){
	cin >> n >> k;
	for (int i=2;i<50020002;i++) dp[i] = neginf0;
	dp[0] = 0;
    dp[1] = 0;
	for (int i=0;i<n;i++) {cin >> arr[i];}
	final_res = max(compute(n, k, 1), compute(n, k, 0));
    cout << final_res << endl;
}