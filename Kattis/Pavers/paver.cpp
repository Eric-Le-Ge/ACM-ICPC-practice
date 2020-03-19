#include<iostream>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    if (n==0) {
        cout << "0 0 0 0" << endl;
        return 0;
    }
    int counts0[3][4] = {0};
    int counts1[3][4] = {0};
    int counts2[3][4] = {0};
    counts0[0][0] = 1;
    counts1[0][0] = 2;
    counts1[0][1] = 2;
    counts1[0][2] = 1;
    counts1[1][0] = 1;
    counts1[1][1] = 1;
    counts1[2][0] = 1;
    counts1[2][1] = 1;
    n -= 1;
    while (n--) {
        //base
        counts2[0][0] = counts1[0][0] * 2 + counts1[1][0] * 2 + counts1[2][0] * 2 + 3 * counts0[0][0];
        counts2[0][1] = 2 * counts1[0][0] + 2 * counts1[0][1] + counts1[1][0] + 2 * counts1[1][1] + counts1[2][0] + 2 * counts1[2][1] + 3 * counts0[0][1] + 2 * counts0[0][0];
        counts2[0][2] = counts1[0][0] + 2 * counts1[0][2] + counts1[1][0] + 2 * counts1[1][2] + counts1[2][0] + 2 * counts1[2][2] + 2 * counts0[0][0] + 3 * counts0[0][2];
        counts2[0][3] = 2 * counts1[0][3] + counts1[1][0] + 2 * counts1[1][3] + counts1[2][0] + 2 * counts1[2][3] + 3 * counts0[0][3] + 2 * counts0[0][0];
        //left taken
        counts2[1][0] = counts1[0][0] + counts1[2][0] + counts0[0][0];
        counts2[1][1] = counts1[0][0] + counts1[0][1] + counts1[2][1] + counts0[0][1];
        counts2[1][2] = counts1[1][0] + counts1[0][2] + counts1[2][2] + counts0[0][2];
        counts2[1][3] = counts0[0][0] + counts1[0][3] + counts1[2][3] + counts0[0][3];


        //right taken
        counts2[2][0] = counts2[1][0];
        counts2[2][1] = counts2[1][1];
        counts2[2][2] = counts2[1][2];
        counts2[2][3] = counts2[1][3];


        swap(counts0, counts2);
        swap(counts1, counts0);
    }

    cout << counts1[0][0] << ' ' << counts1[0][1] << ' ' << counts1[0][2] << ' ' << counts1[0][3]<< endl;
}