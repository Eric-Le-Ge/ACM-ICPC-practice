#include <iostream>
#include <vector>
using namespace std;
#define INF 0x3fffffff;
// static ints

int T , r, c;
char tgrid[256][256];
int grid[256][256];
int rgrid[256][256];
int rgridcpy[256][256];
int maxplace, maxi, maxj;
vector<int> vi;
vector<int> vj;  

int solve()
{
	maxplace=-1; maxi=1; maxj=1;
	for (int it = 0; it< r+c;it++){
		for (int i = 1;i<=r;i++){
			for (int j=1;j<=c;j++){
				rgrid[i][j] = min(rgrid[i][j], rgrid[i][j+1] + 1);
				rgrid[i][j] = min(rgrid[i][j], rgrid[i][j-1] + 1);
				rgrid[i][j] = min(rgrid[i][j], rgrid[i+1][j] + 1);
				rgrid[i][j] = min(rgrid[i][j], rgrid[i-1][j] + 1);
			}
		}
	}
	for (int i = 1;i<=r;i++){
		for (int j=1;j<=c;j++){
			if (rgrid[i][j] > maxplace){
				vi.clear();vj.clear();
				vi.push_back(i); vj.push_back(j);
				maxplace = rgrid[i][j];
				maxi = i;
				maxj = j;
			}
			else if (rgrid[i][j] == maxplace){
				vi.push_back(i); vj.push_back(j);
			}
		}
	}
	// for (int i = 1;i<=r;i++){
	// 	for (int j=1;j<=c;j++){
	// 		cout << "&" << rgrid[i][j] << " ";
	// 	}
	// 	cout << endl;
	// }
	int res = INF;
	for (int k =0;k<vi.size();k++){
		maxi = vi[k];maxj = vj[k];
		for (int i = 0;i<=r+1;i++){
			for (int j=0;j<=c+1;j++){
				rgridcpy[i][j] = rgrid[i][j];
			}
		}
		rgridcpy[maxi][maxj] = 0; maxplace = -1;
		//cout << maxi << "---"<< maxj << endl;
		for (int it = 0; it< max(r,c)+1;it++){
			for (int i = 1;i<=r;i++){
				for (int j=1;j<=c;j++){
					rgridcpy[i][j] = min(rgridcpy[i][j], rgridcpy[i][j+1] + 1);
					rgridcpy[i][j] = min(rgridcpy[i][j], rgridcpy[i][j-1] + 1);
					rgridcpy[i][j] = min(rgridcpy[i][j], rgridcpy[i+1][j] + 1);
					rgridcpy[i][j] = min(rgridcpy[i][j], rgridcpy[i-1][j] + 1);
				}
			}
		}
		for (int i = 1;i<=r;i++){
			for (int j=1;j<=c;j++){
				if (rgridcpy[i][j] > maxplace){
					maxplace = rgridcpy[i][j];
				}
			}
		}
		res = min(res, maxplace);
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
		for (int i = 1;i<=r;i++){
			cin >> tgrid[i];
			for (int j=1;j<=c;j++){
				grid[i][j] = tgrid[i][j-1]-'0';
				if (grid[i][j])
					rgrid[i][j] = 0;
				else{
					rgrid[i][j] = INF;
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

