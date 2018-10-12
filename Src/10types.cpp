#include <iostream>
#include <vector>
#include <string>
using namespace std;

//disjoint sets
int row, col, t, tl, tu;
int B[1000002];
int par[1000002];
int Rank[1000002];
void init(int N){
    for (int i=0;i<N;i++){
        par[i] = i;
        Rank[i] = 0;
    }
}

int find(int x){
    if (par[x]==x){
        return x;
    } else {
        return par[x] = find(par[x]);
    }
}

void unite(int x,int y){
    x = find(x);
    y = find(y);
    if (x==y) return;
    if (Rank[x]<Rank[y]){
        par[x]=y;
    }
    else{
        par[y] = x;
        if (Rank[x]==Rank[y]) Rank[x]++;
    }
}

bool same(int x, int y){
    return find(x) == find(y);
}

int lin(int x, int y){
    return y*col+x;
}

int main() {
	cin >> row;
	cin >> col;
	string line = "";
	vector<string> vec;
	for (int i = 0; i < row; i++) {
		cin >> line;
		vec.push_back(line);
	}
	int num = 0;
	cin >> num;
	vector<int> queries;
	while (num > 0) {
		num--;
		int rs = 0, cs = 0, re = 0, ce = 0;
		cin >> rs >> cs >> re >> ce;
		queries.push_back(rs);
		queries.push_back(cs);
		queries.push_back(re);
		queries.push_back(ce);
	}
  init(row*col);
  for (int j = 0; j < col; j++) {
    t = vec[0][j] - '0';
    B[j] = t;
    if (j){
      tl = vec[0][j-1] - '0';
      if (t==tl) unite(j,j-1);
    }
  }
  for (int i=1;i<row;i++){
    for (int j = 0; j < col; j++) {
      t = vec[i][j] - '0';
      B[lin(j,i)] = t;
      tu = B[lin(j,i-1)];
      if (j){
        tl = B[lin(j-1,i)];
        if (t==tl) unite(lin(j-1,i), lin(j,i));
        if (t==tu) unite(lin(j,i-1), lin(j,i));
      }
      else{
        if (t==tu) unite(lin(j,i-1), lin(j,i));
      }
    }
  }
	for (int in = 0; in < queries.size(); in+=4) {
		int rs = queries[in]-1;
		int cs = queries[in + 1]-1;
		int re = queries[in + 2]-1;
		int ce = queries[in + 3]-1;
    if (B[lin(cs, rs)]){
      if (same(lin(cs, rs), lin(ce, re))) cout << "decimal" << endl;
      else cout << "neither" << endl;
    }
    else{
      if (same(lin(cs, rs), lin(ce, re))) cout << "binary" << endl;
      else cout << "neither" << endl;
    }
	}
}
