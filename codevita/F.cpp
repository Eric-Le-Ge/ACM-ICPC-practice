#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main() {
	int N;
	cin >> N;
	string s;
	cin >> s;
	int qcount;
	cin >> qcount;
	vector<int> q;
	int tmp;
	for (int i=0;i<qcount;++i) {
		cin >> tmp;
		q.push_back(tmp);
	}
	int* counts = new int[10001] {0};
	for (int center=0;center<N;++center) { // odd
		int ext = 0;
		while (center - ext >= 0 && center + ext < N && s[center - ext] == s[center + ext]) {
			counts[1 + ext * 2]++;
			ext++;
		}
	}
	for (int center=0;center<N-1;++center) { // even
		int ext = 0;
		while (center - ext >= 0 && center + ext < N-1 && s[center - ext] == s[center + 1+ext]) {
			counts[2 + ext * 2]++;
			ext++;
		}
	}
	int res = 0;
	for (auto qr : q){
		res += counts[qr];
	}
	cout << res;

}