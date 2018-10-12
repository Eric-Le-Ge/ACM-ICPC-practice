#include<iostream>
using namespace std;
int p,q,n,m;
int gcd(int x, int y){
if (y==0) return x;
return gcd(y, x%y);


}


int main(){
cin >> p >> q >> n;
m = q*p/gcd(p,q);
if (m>n) cout << "no" << endl;
else cout << "yes" << endl;

}
