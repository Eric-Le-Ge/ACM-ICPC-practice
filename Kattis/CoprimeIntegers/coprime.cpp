#include<iostream>
using namespace std;
typedef long long ll;
int p[10000001],bad[10000001];
int a, b, c, d, maxV;
ll i2;
ll s(int e,int f){
  ll tmp;
  ll ret = (ll) e*f;
  for (int i=2;i<maxV;i++){
      if (bad[i]) continue;
      tmp = (ll) (e/i) * (f/i);
      if (p[i]&1) {
        ret -= tmp;
      }
      else {
        ret += tmp;
      }



  }
  return ret;
}


int main(){
  cin >> a >> b >> c >> d;
  maxV = min(b,d)+1;
  fill(bad,bad+10000001,0);
  fill(p,p+10000001,0);
  for (int i=2;i<maxV;i++){
      if (p[i]) continue;
      for (int j=i;j<maxV;j+=i){
         p[j] ++;
      }
      i2 = (ll) i*i;
      if (i2 < maxV){
        for (int k= i*i;k<maxV;k+=i*i){
          bad[k] = 1;
        }
      }

  }
  ll print =  s(a-1,c-1)+s(b,d)-s(a-1,d)-s(b,c-1);
  cout << print << endl;

}
