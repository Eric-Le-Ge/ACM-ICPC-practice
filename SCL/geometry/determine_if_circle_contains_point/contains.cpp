#include<iostream>
#include<math.h>
using namespace std;
int contained(double centerx, double centery,double x,double y,double r){
  return pow(r, 2)+ 0.000001 >= pow(centerx-x, 2) + pow(centery-y, 2);
}
int main(){
	double a, b, c, d, e;
	cin >> a >> b>> c>> d>> e;
	cout << contained(a, b, c, d, e);

}


