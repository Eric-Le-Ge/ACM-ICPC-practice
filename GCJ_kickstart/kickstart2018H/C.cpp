#include <iostream>
#include <utility>


using namespace std;
typedef long long ll;




int mul_inv(ll a, ll b)
{
	ll b0 = b, t, q;
	ll x0 = 0, x1 = 1;
	if (b == 1) return 1;
	while (a > 1) {
		q = a / b;
		t = b, b = a % b, a = t;
		t = x0, x0 = x1 - q * x0, x1 = t;
	}
	if (x1 < 0) x1 += b0;
	return x1;
}

ll MOD = 1000000007;
ll DP[200005];


ll EXPO[200005];

long long combinations(int n, int k, long long p) {

  return DP[n]*mul_inv(DP[k]*DP[n-k]%p, p)%p;
}

int main() {
  EXPO[0] = 1;
  DP[0] = 1;


  for (int i = 1;i<200005;i++){
    EXPO[i] = (EXPO[i-1]*2)%MOD;
  }

  int t, n0, m0;
  ll result;
  result = 1;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    result = 1;
    cin >> m0 >> n0;  // read n and then m.
    for (int j=1; j<=m0*2;j++){
      result = result*j%MOD;
      DP[j] = result;

    }
    for (int k=1; k<=n0;k++){
      ll tmp = ((combinations((m0-k)*2+k,(m0-k)*2,MOD)*DP[k]%MOD*DP[(m0-k)*2]%MOD)*EXPO[k]%MOD*combinations(n0,k,MOD)%MOD);
      //cout <<(m0-k)*2+k << DP[(m0-k)*2] << EXPO[k] << combinations(n0,k,MOD) << endl;
      if (k%2){
        result = ((result - tmp)+MOD)%MOD;
      }
      else{
        result = ((result + tmp)+MOD)%MOD;
      }
    }


    cout << "Case #" << i << ": " << result << endl;
  }

  return 0;
}
