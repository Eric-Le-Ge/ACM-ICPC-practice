#include<iostream>
using namespace std;
typedef unsigned long long ll;
ll ct=0, a, b;
ll t;
ll sheldons[64*64*64];
ll ones[64];
int main(){
  cin >> a >> b;
  t=1;
  for (int i=1;i<64;i++){
    ones[i]=t;
    t=(t<<1)+1;
  }
  for (int i=1;i<64;i++){
    for (int j=1;j<64-i;j++){
      for (int k=1;k<=63/(i+j);k++){
        t = 0;
        for (int m=0;m<k;m++){
          t=((t<<i)+ones[i])<<j;
        }
        sheldons[ct++]=t;
        if ((i+j)*k+i<64){
          sheldons[ct++]=(t<<i)+ones[i];
        }
      }
    }
  }
  for (int i=1;i<64;i++){
    sheldons[ct++]=ones[i];
  }
  int res=0;
  for (int i=0;i<ct;i++){
    if (a<=sheldons[i] && b>=sheldons[i]){
      res++;
    }
  }
  cout << res << endl;

}
