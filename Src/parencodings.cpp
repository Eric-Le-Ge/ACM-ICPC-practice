#include<iostream>

using namespace std;

int main(){
int par[40],res[20];
int t,n,m,cur,rc,count,mark,prev;
cin >> t;
for (int i = 0;i<t;i++){
  m = 0;
  prev = 0;
  cin >> n;
  for (int j =0; j<n;j++){
    cin >> cur;
    for (int k =0; k<cur-prev;k++){
      par[m++] = 1;
    }
    par[m++] = 0;
    prev = cur;
  }
  for (int j0=0; j0<m;j0++){
    if (par[j0] == 0){
      count = 1;
      rc = 1;
      mark = j0-1;
      while(count > 0){
        if(par[mark--] == 1){
          count --;
        }
        else{
          count ++;
          rc ++;
        }
      } 
    
      if (j0<m-1){
        cout << rc << " ";
      }
      else{
        cout << rc << endl;
      }
    }
  }



//results



}
return 0;
}
