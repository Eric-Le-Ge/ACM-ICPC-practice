#include<iostream>
using namespace std;


int total[5001][5001], ma[5001][5001], mi[5001][5001], n, run, rmin, rmax;
int main(){
	string data;
	cin >> data;
	n = data.length();
	for (int start=0;start<=n;start++) {
		total[start][start] = 0;
		ma[start][start] = 0;
		mi[start][start] = 0;
		run = 0; rmax = 0; rmin = 0;
		for (int end=start+1;end<=n;end++){
			run += 2*(data[end-1] == '(')-1;
			rmax = max(rmax, run); rmin = min(rmin, run);
			total[start][end] = run;
			ma[start][end] = rmax;
			mi[start][end] = rmin;
		}
	}
	for (int start=n;start>0;start--) {
		run = 0; rmax = 0; rmin = 0;
		for (int end=start-1;end>=0;end--){
			run += 2*(data[end] == ')')-1;
			rmax = max(rmax, run); rmin = min(rmin, run);
			ma[start][end] = rmax;
			mi[start][end] = rmin;
		}
	}
	// for (int start=0;start<=n;start++) {
	// 	for (int end=0;end<=n;end++){
	// 		cout << total[start][end] << ',' << ma[start][end] << ',' << mi[start][end] << '|';
	// 	}
	// 	cout <<endl;
	// }
	for (int start=0;start<n;start++) {
		for (int end=start;end<=n;end++){
			if ((total[0][start]-total[start][end]+total[end][n] == 0) and
			     mi[0][start] >= 0 and -ma[start][end] + total[0][start] >= 0 and
			     mi[n][end] >= 0 and ma[end][start] + total[end][n] <= 0){
				cout << "possible" <<  endl;
				return 0;
			}
		}
	}
	cout << "impossible" << endl;
}