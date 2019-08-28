#include<iostream>
#include<vector>
using namespace std;
int sev[32000];
vector<int> primes;
int main(){
	int T, l, r, res, two, odd;
	cin >> T;
	for (int i=0;i<32000;i++){
		sev[i]=1;
	}
	for (int i=2;i<32000;i++){
		if (sev[i]){
			for (int j=2*i;j<32000;j+=i){
				sev[j] = 0;
			}
		}
	}
	for (int i=3;i<32000;i++){
		if (sev[i]) primes.push_back(i);
	}
	for (int t=1;t<=T;t++){
		res = 0;
		cin >> l >> r;
		if (l==1){
			res ++;
			l ++;
		}
		for (int snum=l;snum<=r;snum++){
			int num = snum;
			two = 0;
			odd = 1;
			while (num%2==0){
				num /= 2;
				two ++;
			}
			if (two>=4){
				continue;
			}
			for (int i=0;i<primes.size();i++){
				if (!(num%primes[i])){
					num /= primes[i];
					odd ++;
					break;
				}
			}
			if (num != 1) odd ++;
			if (odd==2 && two<3) res ++;
			else if (odd>2 && two==1) res ++;
			else if (odd<2) res ++;
		}
		cout << "Case #" << t << ": " << res << endl;
	}

}