#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>
typedef long double ld;
using namespace std;
vector<ld> gauss(vector< vector<ld> > A) {
    int n = A.size();

    for (int i=0; i<n; i++) {
        // Search for maximum in this column
        ld maxEl = abs(A[i][i]);
        int maxRow = i;
        for (int k=i+1; k<n; k++) {
            if (abs(A[k][i]) > maxEl) {
                maxEl = abs(A[k][i]);
                maxRow = k;
            }
        }

        // Swap maximum row with current row (column by column)
        for (int k=i; k<n+1;k++) {
            ld tmp = A[maxRow][k];
            A[maxRow][k] = A[i][k];
            A[i][k] = tmp;
        }

        // Make all rows below this one 0 in current column
        for (int k=i+1; k<n; k++) {
            ld c = -A[k][i]/A[i][i];
            for (int j=i; j<n+1; j++) {
                if (i==j) {
                    A[k][j] = 0;
                } else {
                    A[k][j] += c * A[i][j];
                }
            }
        }
    }
    // Solve equation Ax=b for an upper triangular matrix A
    vector<ld> x(n);
    for (int i=n-1; i>=0; i--) {
        x[i] = A[i][n]/A[i][i];
        for (int k=i-1;k>=0; k--) {
            A[k][n] -= A[k][i] * x[i];
        }
    }
    return x;
}

void print(vector< vector<ld> > A) {
    int n = A.size();
    for (int i=0; i<n; i++) {
        for (int j=0; j<n+1; j++) {
            cout << A[i][j] << "\t";
            if (j == n-1) {
                cout << "| ";
            }
        }
        cout << "\n";
    }
    cout << endl;
}

int main(){
	int n;
	cin >> n;
	ld values[528];
	ld probs[528][5];
	int neighbors[528][4];
	for (int i=0;i<528;i++) for (int j=0;j<4;j++) neighbors[i][j] = -1;
	for (int i=0;i<n*(n+1)/2;i++) cin >> values[i];
	for (int i=0;i<n*(n+1)/2;i++) for (int j=0;j<5;j++) cin >> probs[i][j];
	vector< vector<ld> > A;
	
	int p0;
	for (int row=0;row<n;row++){
		for (int col=0;col<row+1;col++){
			p0 = ((row+1)*row)/2 + col;
			if (col>0) neighbors[p0][0] = p0-row-1;
			if (col<row) neighbors[p0][1] = p0-row;
			if (row<n-1) {
				neighbors[p0][2] = p0+row+1;
				neighbors[p0][3] = p0+row+2;
			}
		}
	}
	for (int row=0;row<n;row++){
		for (int col=0;col<row+1;col++){
			p0 = ((row+1)*row)/2 + col;

			vector<ld> v;
			for (int i=0;i<=n*(n+1)/2+1;i++) v.push_back(0.0);
			v[p0] = 1.0;
			for (int i=0;i<=3;i++){
				if (neighbors[p0][i] >= 0)
					v[neighbors[p0][i]] = -probs[p0][i];
			}
			v[n*(n+1)/2] = probs[p0][4] * values[p0];
			A.push_back(v);
		}
	}
	vector<ld> res = gauss(A);
	cout << setprecision(15) << res[0] << endl;
}



