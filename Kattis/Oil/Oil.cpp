#include <iostream> 
#include <iterator> 
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
int n,l,r,h,w,x0,_y0,x,y,res=0,run;
int main(){
	map<pair<int, int>, int> lp, rp;
	map<pair<int, int>, int>::iterator itr;
	vector<pair<int, int> > v;
	vector<pair<double, int> > rest;
	cin >> n;
	for (int i=0;i<n;i++){
		cin >> l >> r >> h;
		if (l>r){
			int tmp = r; r = l; l = tmp;
		}
		w = r-l;
		lp[pair<int, int>(l, h)] = w;
		rp[pair<int, int>(r, h)] = w;
		v.push_back(pair<int, int>(l,h));
		v.push_back(pair<int, int>(r,h));
	}
	for (int i=0;i<v.size();i++){
		x = v[i].first; y = v[i].second; rest.clear();
		for (itr = lp.begin(); itr != lp.end(); ++itr) { 
			x0 = itr->first.first; _y0 = itr->first.second; w = itr->second;
			if (_y0 > y) rest.push_back(pair<double, int> (((double) (x0-x))/(_y0-y), -w));
			else if (_y0 < y) rest.push_back(pair<double, int> (((double) (x0-x))/(_y0-y), w));
		}
		for (itr = rp.begin(); itr != rp.end(); ++itr) { 
			x0 = itr->first.first; _y0 = itr->first.second; w = itr->second;
			if (_y0 > y) rest.push_back(pair<double, int> (((double) (x0-x))/(_y0-y), w));
			else if (_y0 < y) rest.push_back(pair<double, int> (((double) (x0-x))/(_y0-y), -w));
		}
		if (!rest.empty()) sort(rest.begin(), rest.end());
		if (lp.find(v[i]) != lp.end()) run = lp[v[i]];
		else run = rp[v[i]];
		res = max(res, run);
		for (int j=0;j<(int) rest.size()-1;j++){
			run -= rest[j].second;
			res = max(res, run);
		}
	}
    cout << res << endl; 
}