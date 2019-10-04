#include <iostream>
using namespace std;
int H, B, h[100], b[100];

int main(){
	cin >> H;
	for (int i=0;i<H;i++) cin >> h[i];
	cin >> B;
	for (int i=0;i<B;i++) cin >> b[i];
	int dph[102000], dpb[102000];
	for (int i=0;i<102000;i++) dph[i] = dpb[i] = -1;
	dph[0] = 0;
	dpb[0] = 0;
	for (int i=0;i<H;i++){
		for (int j=100000;j>=0;j--){
			if (dph[j] != -1){
				if (dph[j+h[i]] == -1) dph[j+h[i]] = dph[j] + 1;
				else dph[j+h[i]] = min(dph[j+h[i]], dph[j] + 1);
			}
		}
	}
	for (int i=0;i<B;i++){
		for (int j=100000;j>=0;j--){
			if (dpb[j] != -1){
				if (dpb[j+b[i]] == -1) dpb[j+b[i]] = dpb[j] + 1;
				else dpb[j+b[i]] = min(dpb[j+b[i]], dpb[j] + 1);
			}
		}
	}
	int res = 201;
	for (int j=1;j<=100000;j++){
		if (dpb[j] != -1 and dph[j] != -1){
			res = min(res, dpb[j] + dph[j]);
		}
	}
	if (res == 201) cout << "impossible" << endl;
	else cout << res << endl;
}
