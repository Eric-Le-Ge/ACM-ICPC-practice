#include <iostream>
#include <vector>
using namespace std;
#define INF 0x3fffffff;
// static ints

int T , r, c;
char tgrid[256][256];
int grid[256][256];
int rgrid[256][256];
int dgrid[256][256];

int maxplace;
int x0,x1,y0,y1;
vector<int> vi;
vector<int> vi0;
vector<int> vj; 
vector<int> vj0;

int solve()
{
	for (int i=0;i<=r;i++){
		for (int j=0;j<=c;j++){
			dgrid[i][j] = INF;
		}
	}
	
	if (vi.size()==r*c)
		return 0;
	for (int k = 0;k<vi0.size();k++){
		for (int l = 0;l<vi.size();l++){
			x0 = vi0[k];y0=vj0[k];
			x1=vi[l];y1=vj[l];
			dgrid[x0][y0]= min(dgrid[x0][y0], abs(x0-x1)+abs(y0-y1));
		}
	}

	int res = INF;
	for (int k = 0;k<vi0.size();k++){
		maxplace = -1;
		for (int l = 0;l<vi0.size();l++){
			x0 = vi0[k];y0=vj0[k];
			x1=vi0[l];y1=vj0[l];
			maxplace = max(maxplace, min(abs(x0-x1)+abs(y0-y1), dgrid[x1][y1]));
		}
		res = min(maxplace, res);
	}
	return res;


	
}


int main()
{
	cin >> T;
	for (int t = 0;t < T; t++)
	{
		// IO
		cin >> r >> c;
		vi.clear();
		vj.clear();
		vi0.clear();
		vj0.clear();
		for (int i = 1;i<=r;i++){
			cin >> tgrid[i];
			for (int j=1;j<=c;j++){
				grid[i][j] = tgrid[i][j-1]-'0';
				if (grid[i][j]){
					rgrid[i][j] = 0;
					vi.push_back(i);
					vj.push_back(j);
				}
				else{
					rgrid[i][j] = INF;
					vi0.push_back(i);
					vj0.push_back(j);
				}
			}
			grid[i][0] = 0; grid[i][c+1] = 0;
			rgrid[i][0] = INF; rgrid[i][c+1] = INF;
		}
		for (int j=0;j<=c+1;j++){
			grid[0][j] = 0; grid[r+1][j] = 0;
			rgrid[0][j] = INF; rgrid[r+1][j] = INF;
		}
		// solve
		int ans = solve();
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
}

