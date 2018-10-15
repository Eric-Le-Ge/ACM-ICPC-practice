#include<iostream>
using namespace std;
int n, m,res;
int main(){
cin >> n;
while (n--){
cin >> m;
res = 0;
while (m--){
res = res*2+1;
}
cout << res << endl;
}
}
