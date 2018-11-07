#include<iostream>
#include<math.h>
using namespace std;


int contained(double centerx, double centery,double x,double y,double r){
  return pow(r, 2)+ 0.000001 >= pow(centerx-x, 2) + pow(centery-y, 2);
}

int main(){
  int l, m, res, count1, count2;
  double X[32], Y[32], centerx1, centery1, centerx2, centery2, r, q, x1, x2, y1, y2, x3, y3;
  double basex, basey;
  cin >> l;

  while(l--){
    res = 1;
    cin >> m >> r;
    r/=2.0000;
    for (int i=0;i<m;i++){
      cin >> X[i] >> Y[i];
    }
    for (int i=0;i<m;i++){
      for (int j=i+1;j<m;j++){
        count1 = 0;
        count2 = 0;
        x1 = X[i];
        y1 = Y[i];
        x2 = X[j];
        y2 = Y[j];
        q = sqrt(pow((x2-x1),2) + pow((y2-y1),2));
        if (q>2*r) continue;
    		y3 = (y1+y2)/2;
    	  x3 = (x1+x2)/2;
    		basex = sqrt(pow(r,2)-pow((q/2),2))*(y1-y2)/q; //calculate once
    	  basey = sqrt(pow(r,2)-pow((q/2),2))*(x2-x1)/q; //calculate once
    		centerx1 = x3 + basex; //center x of circle 1
    		centery1 = y3 + basey; //center y of circle 1
    		centerx2 = x3 - basex; //center x of circle 2
    		centery2 = y3 - basey; //center y of circle 2
        for (int k=0;k<m; k++){
          count1 += contained(centerx1, centery1, X[k], Y[k], r);
          count2 += contained(centerx2, centery2, X[k], Y[k], r);
        }
        res = max(res, count1);
        res = max(res, count2);
      }
    }
    cout << res << endl;
  }
}

