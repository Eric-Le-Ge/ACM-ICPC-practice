#include <iostream>
#include <vector>
#include <iomanip>      // std::setprecision
using namespace std;

int N;
double K;
vector<double> heights;

// h 0, 0, n+1, 0
double fp(int ind) {
    return K * (N+1-ind) * ind;
}

double h(int ind) {
    if (ind == 0 || ind == N+1) return 0.;
    return heights[ind-1];
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N >> K;
    heights.resize(N);
    for (int i=0; i<N;++i) cin >> heights[i];
    // construct an ordinary linear convex hull
    vector<int> hull = {0};
    for (int i=1; i<=N+1; ++i) {
        while (hull.size() > 1) {
            int prev = hull[hull.size()-1];
            int prev2 = hull[hull.size()-2];
            if ((h(i)-fp(i)-h(prev)+fp(prev)) / (i-prev) >= (h(i)-fp(i)-h(prev2)+fp(prev2)) / (i-prev2)) {
                hull.pop_back();
            } else {
                break;
            }
        }
        hull.push_back(i);
    }

    double res = 0;
    for (int i=1; i<hull.size(); ++i) {
        int prevind = hull[i-1], ind = hull[i];
        for (int j=prevind+1; j<ind; ++j) {
            res = max(res, h(prevind)-fp(prevind) + double(h(ind)-fp(ind)-h(prevind)+fp(prevind)) * (j-prevind) / (ind-prevind) + fp(j));
        }
        res = max(res, h(hull[i]));
    }
    cout << setprecision(9) << res << endl;
}
